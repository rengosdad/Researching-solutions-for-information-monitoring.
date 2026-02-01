import os
import requests
import pandas as pd
from flask import Flask, render_template_string, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# ===== CẤU HÌNH =====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_FILE = os.path.join(BASE_DIR, "data.xlsx")
START_DATE_FILE = os.path.join(BASE_DIR, "start_date.txt")
CURRENT_DATE_FILE = os.path.join(BASE_DIR, "current_date.txt")
ESP32_IP = "http://192.168.1.21/json"

# ===== HÀM TIỆN ÍCH =====
def read_date(path):
    if os.path.exists(path):
        return open(path).read().strip()
    return datetime.now().strftime("%Y-%m-%d")

def save_date(path, value):
    with open(path, "w") as f:
        f.write(value)

def read_excel():
    if not os.path.exists(EXCEL_FILE):
        return pd.DataFrame()

    try:
        df_raw = pd.read_excel(EXCEL_FILE, header=None)
        header_idx = None
        for idx, row in df_raw.iterrows():
            if pd.notna(row.iloc[0]) and str(row.iloc[0]).strip() == "Ngày":
                header_idx = idx
                break

        if header_idx is None:
            return pd.DataFrame()

        headers = df_raw.iloc[header_idx].values
        df = df_raw.iloc[header_idx + 1:].copy()
        df.columns = headers
        df.reset_index(drop=True, inplace=True)
        df.columns = df.columns.str.strip()

        column_map = {
            'Ngày': 'Ngay',
            'Giai đoạn': 'Giai_Doan',
            'Temp Min': 'Temp_Min',
            'Temp Max': 'Temp_Max',
            'Hum Min': 'Hum_Min',
            'Hum Max': 'Hum_Max',
            'Nhiệm vụ AI nhắc nhở': 'Nhiemvu',
        }
        df.rename(columns=column_map, inplace=True)

        if 'Ngay' in df.columns:
            df['Ngay'] = pd.to_numeric(df['Ngay'], errors='coerce')
            df = df.dropna(subset=['Ngay']).copy()
            df['Ngay'] = df['Ngay'].astype(int)
            return df
        else:
            return pd.DataFrame()

    except Exception as e:
        print("Lỗi đọc file Excel:", e)
        return pd.DataFrame()

def ai_evaluate(temp, hum, cfg):
    if cfg is None:
        return "INFO", "Chưa có dữ liệu lộ trình – Upload file XLSX có phần lộ trình theo ngày"

    status = "SAFE"
    msg_parts = []

    tmin_str = str(cfg.get('Temp_Min', '--')).strip()
    tmax_str = str(cfg.get('Temp_Max', '--')).strip()
    if tmin_str != '--' and tmax_str != '--':
        try:
            tmin, tmax = float(tmin_str), float(tmax_str)
            if temp > tmax:
                status = "DANGER"
                msg_parts.append(f"Quá nóng ({temp}°C > {tmax}°C)")
            elif temp < tmin:
                status = "DANGER"
                msg_parts.append(f"Quá lạnh ({temp}°C < {tmin}°C)")
            else:
                msg_parts.append(f"Nhiệt độ tốt ({temp}°C)")
        except:
            msg_parts.append("Nhiệt độ: Không yêu cầu")
    else:
        msg_parts.append("Nhiệt độ: Không yêu cầu")

    hmin_str = str(cfg.get('Hum_Min', '--')).strip()
    hmax_str = str(cfg.get('Hum_Max', '--')).strip()
    if hmin_str != '--' and hmax_str != '--':
        try:
            hmin, hmax = float(hmin_str), float(hmax_str)
            if hum > hmax:
                status = "DANGER"
                msg_parts.append(f"Quá ẩm ({hum}% > {hmax}%)")
            elif hum < hmin:
                status = "DANGER"
                msg_parts.append(f"Quá khô ({hum}% < {hmin}%)")
            else:
                msg_parts.append(f"Độ ẩm tốt ({hum}%)")
        except:
            msg_parts.append("Độ ẩm: Không yêu cầu")
    else:
        msg_parts.append("Độ ẩm: Không yêu cầu")

    if status == "SAFE":
        msg = "Môi trường lý tưởng ✓"
    else:
        msg = "Cần điều chỉnh: " + "; ".join(msg_parts)

    return status, msg

# ===== ROUTE UPLOAD =====
@app.route('/upload', methods=['POST'])
def upload():
    if 'excel_file' not in request.files:
        return redirect(url_for('index'))
    file = request.files['excel_file']
    if file.filename == '' or not file.filename.lower().endswith(('.xlsx', '.xls')):
        return redirect(url_for('index'))
    file.save(EXCEL_FILE)
    return redirect(url_for('index'))

# ===== ROUTE CHÍNH =====
@app.route('/')
def index():
    start_str = read_date(START_DATE_FILE)
    current_str = read_date(CURRENT_DATE_FILE)

    try:
        start_date = datetime.strptime(start_str, "%Y-%m-%d").date()
        current_date = datetime.strptime(current_str, "%Y-%m-%d").date()
    except:
        start_date = current_date = datetime.now().date()
        start_str = current_str = datetime.now().strftime("%Y-%m-%d")

    day_index = (current_date - start_date).days + 1
    if day_index < 1:
        day_index = 1

    df = read_excel()
    config = None
    stage_ranges = {}
    selected_range = ""

    if not df.empty:
        stage_ranges = df.groupby("Giai_Doan")["Ngay"].agg(["min", "max"]).to_dict("index")
        row = df[df["Ngay"] == day_index]
        if not row.empty:
            config = row.iloc[0].to_dict()

        s = request.args.get("search_stage")
        if s in stage_ranges:
            r = stage_ranges[s]
            selected_range = f"Giai đoạn {s}: ngày {r['min']} → {r['max']}"

    temp, hum = 0.0, 0.0
    try:
        js = requests.get(ESP32_IP, timeout=2).json()
        temp = round(float(js.get("temp", 0)), 1)
        hum = round(float(js.get("hum", 0)), 1)
    except Exception as e:
        print("Lỗi đọc ESP32:", e)

    status, msg = ai_evaluate(temp, hum, config)

    return render_template_string(HTML, **locals())

# ===== SET NGÀY =====
@app.route('/set_start', methods=['POST'])
def set_start():
    save_date(START_DATE_FILE, request.form['start_date'])
    return redirect(url_for('index'))

@app.route('/set_current', methods=['POST'])
def set_current():
    save_date(CURRENT_DATE_FILE, request.form['current_date'])
    return redirect(url_for('index'))

# ===== HTML ĐÃ CHỈNH PHẦN DƯỚI + DESKTOP SIÊU ĐẸP =====
HTML = """
<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Mushroom AI Dashboard</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet">
<style>
/* ===== ROOT VARIABLES ===== */
:root {
    --bg-gradient: linear-gradient(135deg, #74ebd5, #9face6);
    --card-bg: #ffffff;
    --text-primary: #2d3436;
    --text-secondary: #636e72;
    --primary: #00b894;
    --danger: #d63031;
    --safe: #10b981;
    --info: #0984e3;
    --shadow: 0 20px 40px rgba(0,0,0,0.12);
    --radius: 24px;
    --transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

/* DARK MODE */
.dark {
    --bg-gradient: linear-gradient(135deg, #1e272e, #2f3640);
    --card-bg: #1e272e;
    --text-primary: #dfe4ea;
    --text-secondary: #a4b0be;
    --shadow: 0 20px 40px rgba(0,0,0,0.4);
}

/* ===== RESET & BODY ===== */
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    font-family: 'Segoe UI', system-ui, sans-serif;
    background: var(--bg-gradient);
    color: var(--text-primary);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    padding: 20px 16px;
    transition: var(--transition);
}

/* ===== FORCE MOBILE / DESKTOP ===== */
.force-mobile {
    --card-max-width: 100%;
    --card-padding: 24px;
    --grid-columns: 1fr;
    --grid-gap: 16px;
    --controls-layout: column;
}
.force-desktop {
    --card-max-width: 800px;
    --card-padding: 40px;
    --grid-columns: 1fr 1fr;
    --grid-gap: 30px;
    --controls-layout: row;
    --controls-wrap: wrap;
    --section-width: 48%;
}

/* ===== CARD ===== */
.card {
    background: var(--card-bg);
    width: 100%;
    max-width: var(--card-max-width, 460px);
    border-radius: var(--radius);
    padding: var(--card-padding, 28px);
    box-shadow: var(--shadow);
    transition: var(--transition);
    position: relative;
    animation: fadeIn 0.8s ease-out;
}

/* ===== GRID SENSOR ===== */
.grid {
    display: grid;
    grid-template-columns: var(--grid-columns, 1fr 1fr);
    gap: var(--grid-gap, 16px);
    margin-bottom: 30px;
}

/* ===== CONTROLS AREA (PHẦN DƯỚI) ===== */
.controls-area {
    display: flex;
    flex-direction: var(--controls-layout, column);
    flex-wrap: var(--controls-wrap, nowrap);
    gap: 20px;
    margin-top: 20px;
}
.control-section {
    flex: 1;
    min-width: var(--section-width, 100%);
    background: rgba(238,242,247,0.6);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    animation: slideUp 1.8s ease-out;
}
.dark .control-section { background: rgba(45,52,54,0.5); }

/* ===== ANIMATIONS ===== */
@keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
@keyframes slideUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
@keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.05); } 100% { transform: scale(1); } }

/* Các phần khác (header, status, box, task-box, button) giữ nguyên đẹp như trước */
.header { text-align: center; margin-bottom: 20px; }
.day-badge { background: var(--primary); color: white; padding: 12px 28px; border-radius: 50px; font-size: clamp(24px, 6vw, 32px); font-weight: 900; display: inline-block; box-shadow: 0 4px 15px rgba(0,184,148,0.3); animation: slideUp 0.8s ease-out; }
.stage { margin-top: 10px; font-size: 16px; font-weight: 700; color: var(--text-secondary); animation: slideUp 1s ease-out; }
.status { margin: 24px 0; padding: 18px; border-radius: 20px; font-weight: 900; text-align: center; font-size: 16px; animation: slideUp 1.2s ease-out; }
.SAFE { background: #e8f8f5; color: var(--safe); border: 3px solid var(--safe); }
.DANGER { background: #fff5f5; color: var(--danger); border: 3px solid #fab1a0; animation: pulse 2s infinite; }
.INFO { background: #e8f4fd; color: var(--info); border: 3px solid #81d4fa; }
.box { background: rgba(248,249,250,0.7); padding: 20px; border-radius: 20px; text-align: center; backdrop-filter: blur(10px); animation: slideUp 1.4s ease-out; }
.dark .box { background: rgba(45,52,54,0.6); }
.value { font-size: clamp(28px, 7vw, 36px); font-weight: 900; margin: 8px 0; }
.task-box { background: rgba(240,255,244,0.8); padding: 18px; border-radius: 18px; margin: 20px 0; border-left: 6px solid var(--safe); font-size: 15px; line-height: 1.5; animation: slideUp 1.6s ease-out; }
.dark .task-box { background: rgba(16,185,129,0.15); }

/* Button chung */
.btn-refresh, .btn-upload {
    width: 100%;
    margin-top: 20px;
    padding: 16px;
    border: none;
    border-radius: 20px;
    font-weight: 900;
    font-size: 16px;
    cursor: pointer;
    transition: var(--transition);
}
.btn-refresh { background: #2d3436; color: white; }
.btn-upload { background: var(--info); color: white; }
.btn-refresh:hover, .btn-upload:hover { transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0,0,0,0.2); }

/* Input & Label */
label { font-size: 13px; font-weight: 900; color: var(--text-secondary); margin-bottom: 8px; display: block; }
input, select {
    width: 100%;
    padding: 14px;
    border-radius: 16px;
    border: 1px solid #dfe6e9;
    background: white;
    font-size: 15px;
}
.dark input, .dark select { background: #2d3436; color: white; }

/* Toggle buttons */
.toggle-container {
    position: absolute;
    top: 16px;
    right: 16px;
    display: flex;
    gap: 10px;
}
.toggle-btn {
    background: rgba(255,255,255,0.7);
    border: none;
    padding: 10px 14px;
    border-radius: 14px;
    font-size: 22px;
    cursor: pointer;
    transition: var(--transition);
}
.dark .toggle-btn { background: rgba(45,52,54,0.8); }
.toggle-btn.active { background: var(--primary); color: white; }
.toggle-btn:hover { transform: scale(1.1); }
</style>
</head>
<body>
<div class="card">
    <!-- Toggle chế độ -->
    <div class="toggle-container">
        <button class="toggle-btn" id="mobileBtn" onclick="setViewMode('mobile')"><i class="fa-solid fa-mobile-alt"></i></button>
        <button class="toggle-btn" id="desktopBtn" onclick="setViewMode('desktop')"><i class="fa-solid fa-desktop"></i></button>
        <button class="toggle-btn" id="themeBtn" onclick="toggleTheme()">
            <i class="fa-solid fa-moon" id="moon"></i>
            <i class="fa-solid fa-sun" id="sun" style="display:none;"></i>
        </button>
    </div>

    <div class="header">
        <div class="day-badge">NGÀY {{ day_index }}</div>
        <div class="stage">Giai đoạn: {{ config.Giai_Doan if config else "Chưa có dữ liệu" }}</div>
        <div class="live-time" id="liveTime"><i class="fa-solid fa-clock"></i> --:--:--</div>
    </div>

    <div class="status {{ status }}">
        <i class="fa-solid fa-robot"></i> AI: {{ msg }}
    </div>

    <div class="grid">
        <div class="box">
            <i class="fa-solid fa-temperature-half" style="font-size:36px;color:#e17055"></i>
            <div class="value">{{ temp }}°C</div>
            <div class="limit">
                {% if config and config.get('Temp_Min') != '--' %}
                    {{ config.Temp_Min }} – {{ config.Temp_Max }}°C
                {% else %}
                    Không yêu cầu
                {% endif %}
            </div>
        </div>
        <div class="box">
            <i class="fa-solid fa-droplet" style="font-size:36px;color:#0984e3"></i>
            <div class="value">{{ hum }}%</div>
            <div class="limit">
                {% if config and config.get('Hum_Min') != '--' %}
                    {{ config.Hum_Min }} – {{ config.Hum_Max }}%
                {% else %}
                    Không yêu cầu
                {% endif %}
            </div>
        </div>
    </div>

    {% if config and config.get('Nhiemvu') %}
    <div class="task-box">
        <div style="font-weight:900;margin-bottom:10px;"><i class="fa-solid fa-tasks"></i> Nhiệm vụ hôm nay:</div>
        {{ config.Nhiemvu }}
    </div>
    {% endif %}

    <!-- PHẦN DƯỚI ĐÃ CHỈNH ĐẸP + DESKTOP SIÊU RỘNG RÃI -->
    <div class="controls-area">
        <!-- Upload file -->
        <div class="control-section">
            <form method="POST" action="/upload" enctype="multipart/form-data">
                <label>TẢI LÊN FILE XLSX MỚI</label>
                <input type="file" name="excel_file" accept=".xlsx" required>
                <button type="submit" class="btn-upload">
                    <i class="fa-solid fa-upload"></i> Tải lên & Áp dụng
                </button>
            </form>
        </div>

        <!-- Set ngày -->
        <div class="control-section">
            <label>NGÀY XUỐNG GIỐNG</label>
            <form method="POST" action="/set_start">
                <input type="date" name="start_date" value="{{ start_str }}" onchange="this.form.submit()">
            </form>

            <label style="margin-top:20px;">NGÀY HIỆN TẠI</label>
            <form method="POST" action="/set_current">
                <input type="date" name="current_date" value="{{ current_str }}" onchange="this.form.submit()">
            </form>
        </div>

        <!-- Tra cứu giai đoạn (full width nếu có) -->
        {% if stage_ranges %}
        <div class="control-section" style="flex: 1 1 100%;">
            <form method="GET">
                <label>TRA CỨU GIAI ĐOẠN</label>
                <select name="search_stage" onchange="this.form.submit()">
                    <option value="">-- chọn giai đoạn --</option>
                    {% for s in stage_ranges.keys() %}
                    <option value="{{ s }}" {% if s == request.args.get('search_stage') %}selected{% endif %}>{{ s }}</option>
                    {% endfor %}
                </select>
            </form>
            {% if selected_range %}
            <div style="margin-top:16px;padding:14px;background:#fff3cd;border-radius:16px;text-align:center;font-weight:900;">
                <i class="fa-solid fa-calendar-days"></i> {{ selected_range }}
            </div>
            {% endif %}
        </div>
        {% endif %}
    </div>

    <!-- Nút refresh full width -->
    <button class="btn-refresh" onclick="location.reload()" style="margin-top:30px;">
        <i class="fa-solid fa-arrows-rotate"></i> LÀM MỚI TRANG
    </button>
</div>

<script>
// Chế độ giao diện
function setViewMode(mode) {
    const body = document.body;
    body.classList.remove('force-mobile', 'force-desktop');
    if (mode === 'mobile') body.classList.add('force-mobile');
    else if (mode === 'desktop') body.classList.add('force-desktop');
    localStorage.setItem('viewMode', mode || '');
    updateViewButtons();
}

function updateViewButtons() {
    const mobileBtn = document.getElementById('mobileBtn');
    const desktopBtn = document.getElementById('desktopBtn');
    const viewMode = localStorage.getItem('viewMode') || '';
    
    mobileBtn.classList.toggle('active', viewMode === 'mobile');
    desktopBtn.classList.toggle('active', viewMode === 'desktop');
}

const savedView = localStorage.getItem('viewMode');
if (savedView) setViewMode(savedView);
else updateViewButtons();

// Dark mode
function toggleTheme() {
    const body = document.body;
    const moon = document.getElementById('moon');
    const sun = document.getElementById('sun');
    
    if (body.classList.contains('dark')) {
        body.classList.remove('dark');
        moon.style.display = 'block';
        sun.style.display = 'none';
        localStorage.setItem('theme', 'light');
    } else {
        body.classList.add('dark');
        moon.style.display = 'none';
        sun.style.display = 'block';
        localStorage.setItem('theme', 'dark');
    }
}
if (localStorage.getItem('theme') === 'dark') {
    document.body.classList.add('dark');
    document.getElementById('moon').style.display = 'none';
    document.getElementById('sun').style.display = 'block';
}

// Clock
const fixedDate = "{{ current_str }}";
function updateClock(){
    const now = new Date();
    const time = now.toLocaleTimeString('vi-VN');
    const [y,m,d] = fixedDate.split("-");
    const displayDate = `${d}/${m}/${y}`;
    document.getElementById("liveTime").innerHTML = `<i class="fa-solid fa-clock"></i> ${time} - ${displayDate}`;
}
setInterval(updateClock, 1000);
updateClock();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)