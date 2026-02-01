SỞ GIÁO DỤC VÀ ĐÀO TẠO ĐÀ NẴNG
TRƯỜNG THPT NGUYỄN KHUYẾN
**********************************
ĐỀ TÀI DỰ THI
CUỘC THI KHOA HỌC KỸ THUẬT
NĂM HỌC 2025 - 2026
Nghiên cứu giải pháp giám sát thông minh 
cho mô hình trồng nấm ứng dụng AI và IoT
Lĩnh vực: 嵌入式系統
Tác giả: 		       Đặng Nhật Tân
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Trong bối cảnh cách mạng công nghiệp 4.0 và chuyển đổi số trong nông nghiệp, việc áp dụng công nghệ Internet of Things (IoT) và Trí tuệ Nhân tạo (AI) vào các hoạt động trồng trọt đang trở thành một xu hướng tất yếu nhằm nâng cao năng suất lao động, giảm thiểu chi phí sản xuất và tối ưu hóa quy trình quản lý. Đặc biệt, ngành trồng nấm – một lĩnh vực nông nghiệp đòi hỏi sự kiểm soát chặt chẽ các yếu tố môi trường như nhiệt độ, độ ẩm, nồng độ CO2 và độ chiếu sáng – thường phải đối mặt với những thách thức lớn do biến động thời tiết, dịch bệnh và thiếu hệ thống giám sát tự động hóa. Theo báo cáo của Tổ chức Lương thực và Nông nghiệp Liên Hợp Quốc (FAO, 2023), sản lượng nấm toàn cầu đã tăng trung bình 10-15% hàng năm trong thập kỷ qua, nhưng tại Việt Nam, tỷ lệ thất thoát sản phẩm do điều kiện môi trường không phù hợp có thể lên đến 20-30%, dẫn đến thiệt hại kinh tế đáng kể cho nông hộ [1].
Để minh họa cho vấn đề này, hãy xem xét trường hợp trồng nấm rơm tại các tỉnh miền Trung Việt Nam như Quảng Nam. Nấm rơm yêu cầu nhiệt độ ổn định từ 28-32°C và độ ẩm 75-85%. Nếu nhiệt độ vượt quá 35°C, nấm có thể bị héo úa, dẫn đến mất trắng vụ mùa. Theo thống kê từ Bộ Nông nghiệp và Phát triển Nông thôn Việt Nam (2022), hàng năm có hàng nghìn tấn nấm bị hỏng do không kiểm soát được môi trường, gây thiệt hại hàng tỷ đồng. Các hệ thống giám sát truyền thống chủ yếu dựa vào cảm biến thủ công và ghi chép bằng tay, thiếu khả năng dự báo thời gian thực và hỗ trợ quyết định dựa trên dữ liệu, từ đó làm giảm hiệu quả sản xuất tổng thể. Ví dụ, nông dân thường phải kiểm tra thủ công hàng ngày, dẫn đến sai sót và chậm trễ trong điều chỉnh.
Trong khi đó, các giải pháp thương mại như hệ thống FarmBot hay IBM Watson Agriculture cung cấp các tính năng tiên tiến nhưng lại có chi phí cao, thường vượt quá khả năng đầu tư của các nông hộ nhỏ lẻ tại các quốc gia đang phát triển như Việt Nam [2]. FarmBot, ví dụ, là một robot trồng trọt tự động với giá khoảng 50-100 triệu VND, trong khi IBM Watson yêu cầu đăng ký đám mây với phí hàng tháng. Những giải pháp này phù hợp với nông trại lớn ở châu Âu hoặc Mỹ, nhưng không khả thi cho nông hộ Việt Nam với diện tích trồng nhỏ (dưới 1.000 m²). Cộng đồng mã nguồn mở đã phát triển nhiều nền tảng hỗ trợ, chẳng hạn như Arduino cho IoT và Google Apps Script cho tích hợp AI, nhưng vẫn thiếu sự tích hợp toàn diện để hỗ trợ cụ thể cho ngành trồng nấm. Các nghiên cứu tiêu biểu từ Journal of Agriculture and Food Research (2022) cho thấy việc kết hợp IoT với AI có thể giảm thiểu thất thoát lên đến 25-40% thông qua dự báo môi trường và nhắc nhở kịp thời [3]. Tuy nhiên, các hệ thống hiện tại chưa hỗ trợ lộ trình trồng nấm linh hoạt theo từng loại giống, đánh giá AI thời gian thực dựa trên dữ liệu cảm biến, và giao diện web thân thiện với người dùng không chuyên.
Ví dụ, trong nghiên cứu của Hossain et al. (2022), một hệ thống IoT dựa trên ESP32 đã được triển khai để giám sát tự động hóa trang trại nấm, đạt độ chính xác phân loại nấm độc hại lên đến 100% bằng cách sử dụng mô hình học máy tổng hợp (ensemble ML), nhưng vẫn thiếu tích hợp với AI ngôn ngữ lớn như Gemini để tạo lộ trình trồng tự động [3]. Nghiên cứu này được thực hiện tại Bangladesh, với điều kiện khí hậu tương tự Việt Nam, và kết quả cho thấy hệ thống giảm thời gian giám sát từ 4 giờ/ngày xuống còn 30 phút. Tương tự, bài đánh giá toàn diện của Zhang et al. (2024) trên PMC nhấn mạnh rằng việc tích hợp AI với IoT không chỉ cải thiện kiểm soát môi trường mà còn góp phần vào sản xuất nấm bền vững, giảm tiêu thụ năng lượng lên đến 20% [4]. Những khoảng trống này nhấn mạnh nhu cầu về một hệ thống mã nguồn mở, chi phí thấp, phù hợp với điều kiện Việt Nam, nơi nông nghiệp vẫn chiếm tỷ lệ lớn trong GDP (khoảng 14% theo World Bank, 2023).
Với bối cảnh trên, đề tài “Hệ thống giám sát và hỗ trợ trồng nấm thông minh dựa trên AI và IoT” mang ý nghĩa cấp thiết ở cả hai khía cạnh khoa học và thực tiễn:
Về mặt khoa học: Đề tài góp phần phát triển mô hình tích hợp IoT-AI dựa trên mã nguồn mở, mở rộng khả năng nghiên cứu giám sát môi trường thời gian thực và tối ưu hóa quy trình nông nghiệp thông minh, đồng thời cung cấp dữ liệu thực nghiệm để đánh giá hiệu suất hệ thống trong điều kiện thực tế. Cụ thể, đề tài sẽ khám phá cách sử dụng mô hình Gemini để tạo lộ trình trồng nấm động, điều mà các nghiên cứu trước chưa đề cập chi tiết, và phân tích dữ liệu với công cụ như Pandas để đánh giá sai số.
Về mặt thực tiễn: Đề tài hướng tới việc xây dựng một hệ thống chi phí thấp (dưới 10 triệu VND cho mô hình prototype), phục vụ cho nông hộ nhỏ lẻ, các cơ sở đào tạo và nghiên cứu, góp phần thúc đẩy nông nghiệp bền vững và an toàn thực phẩm tại Việt Nam. Hệ thống có thể được triển khai tại các tỉnh miền Trung như Quảng Nam, nơi trồng nấm đang phát triển mạnh với sản lượng hàng nghìn tấn/năm.

Kết quả của đề tài không chỉ tạo ra một nền tảng mở cho giám sát nấm mà còn có thể mở rộng ứng dụng sang các loại cây trồng khác như rau củ hoặc hoa, hỗ trợ AI dựa trên mô hình Gemini và giao diện web sử dụng Flask, từ đó thúc đẩy xu hướng công nghệ mở trong nông nghiệp. Ngoài ra, đề tài cũng sẽ cung cấp các khuyến nghị thực tiễn cho việc triển khai hệ thống tại các trang trại nhỏ, bao gồm cách tích hợp với các thiết bị di động để nông dân dễ dàng theo dõi qua app, và đánh giá kinh tế như ROI (Return on Investment) ước tính 150% trong 2 năm.
II.TỔNG QUAN VẤN ĐỀ NGHIÊN CỨU
2.1. Sự phát triển của nông nghiệp thông minh và hệ thống giám sát môi trường
Trong những năm gần đây, cùng với sự phát triển của cuộc cách mạng công nghiệp lần thứ tư (Industry 4.0), nông nghiệp thông minh đã trở thành một trong những hướng nghiên cứu và ứng dụng trọng điểm nhằm nâng cao hiệu quả sản xuất nông nghiệp. Nông nghiệp thông minh là mô hình sản xuất ứng dụng các công nghệ hiện đại như Internet vạn vật (IoT), trí tuệ nhân tạo (AI), điện toán đám mây và tự động hóa để giám sát, phân tích và tối ưu hóa các quá trình canh tác.Một số thành tự trong việc ứng dụng các công nghệ hiện đại để tối ưu hóa các quá trình canh tác:

<img width="189" height="150" alt="image" src="https://github.com/user-attachments/assets/c5cdc222-b31b-413c-99d4-31528360dc7b" />
<img width="323" height="149" alt="image" src="https://github.com/user-attachments/assets/5d4111b0-5e36-453e-b5d2-a95a59b94915" />

Dự án Hands Free Hectare (Anh)               Công ty FarmWise (Mỹ) đã phát triển robot nhổ cỏ tự động sử dụng 
Là một mô hình canh tác                        các thuật toán AIvà thị giác máy tínhđể phân biệt cây trồng và cỏ dại,
hoàn toàn tự động                                       rồi nhổ bỏ cỏ một cách chính xác mà không cần hóa chất.

2.2. Đặc thù kỹ thuật trong quy trình trồng nấm
Trồng nấm là một lĩnh vực nông nghiệp có đặc thù kỹ thuật cao so với nhiều loại cây trồng khác. Nấm là sinh vật dị dưỡng, không quang hợp, sinh trưởng và phát triển phụ thuộc chặt chẽ vào các điều kiện môi trường xung quanh. Các thông số như nhiệt độ, độ ẩm không khí, độ ẩm giá thể và mức độ thông gió có ảnh hưởng trực tiếp đến sự phát triển của sợi nấm và quá trình hình thành quả thể.
Mỗi loại nấm có yêu cầu môi trường khác nhau, đồng thời trong từng giai đoạn sinh trưởng, các thông số kỹ thuật cũng thay đổi đáng kể. Ví dụ, giai đoạn nuôi tơ yêu cầu độ ẩm cao và môi trường kín, trong khi giai đoạn ra quả thể cần thông gió tốt và ánh sáng tán xạ. Việc kiểm soát chính xác các thông số này là yếu tố quyết định đến năng suất và chất lượng nấm.
Trong thực tế sản xuất, nhiều hộ trồng nấm vẫn dựa chủ yếu vào kinh nghiệm cá nhân để điều chỉnh môi trường. Phương pháp này tiềm ẩn nhiều rủi ro, đặc biệt khi điều kiện thời tiết thay đổi đột ngột, dẫn đến tình trạng nhiễm bệnh, thối tơ hoặc giảm sản lượng. Do đó, nhu cầu ứng dụng các hệ thống kỹ thuật hỗ trợ kiểm soát quy trình trồng nấm ngày càng trở nên cấp thiết.một yêu cầu khắc khe đối với một số loại nấm:
Nhiệt độ: Thích hợp nhất trong khoảng 30–38°C; nhiệt độ thấp làm nấm chậm phát triển, dễ nhiễm bệnh.
Độ ẩm không khí: Cần duy trì 80–90% để nấm hình thành và phát triển tốt.
Độ ẩm giá thể: Giá thể (rơm) phải đủ ẩm, không khô, không úng nước, nếu quá ướt dễ thối và nhiễm mốc.
<img width="147" height="147" alt="image" src="https://github.com/user-attachments/assets/bf863a0a-160c-44eb-ba39-d9fb1b9f833f" />

Nấm rơm
Nhiệt độ: Thích hợp trong khoảng 18–25°C; nhiệt độ cao làm nấm phát triển kém, cuống ngắn, mũ nhỏ.
Độ ẩm không khí: Cần duy trì 85–95% để nấm phát triển tốt.
Độ ẩm giá thể: Giá thể phải đủ ẩm, không khô, không úng nước, tránh gây thối sợi nấm.
<img width="151" height="151" alt="image" src="https://github.com/user-attachments/assets/df0f3b80-2847-453d-8d2c-61307c71c140" />

Nấm đùi gà
Nhiệt độ: Thích hợp trong khoảng 22–30°C.
Độ ẩm không khí: Cần duy trì 80–90%.
Độ ẩm giá thể: Khoảng 60–65%, không khô, không úng.
<img width="158" height="123" alt="image" src="https://github.com/user-attachments/assets/1d90130c-bfc2-4a64-8bbe-3662a2f4d8ac" />

Nấm bào ngư
2.3. Ứng dụng hệ thống IoT trong trồng nấm
Internet vạn vật (IoT) đã được ứng dụng rộng rãi trong lĩnh vực nông nghiệp, đặc biệt là trong giám sát môi trường nhà trồng. Trong các mô hình trồng nấm, hệ thống IoT thường bao gồm các cảm biến đo nhiệt độ, độ ẩm và ánh sáng, kết hợp với vi điều khiển để thu thập và truyền dữ liệu về trung tâm giám sát.
Một số nghiên cứu đã chứng minh rằng việc áp dụng IoT giúp người trồng nấm theo dõi điều kiện môi trường một cách liên tục và chính xác, từ đó giảm sự phụ thuộc vào cảm quan và kinh nghiệm. Tuy nhiên, phần lớn các hệ thống IoT hiện nay chỉ thực hiện chức năng thu thập và hiển thị dữ liệu, chưa tích hợp khả năng phân tích và đưa ra khuyến nghị kỹ thuật cụ thể cho người trồng.
Bên cạnh đó, nhiều hệ thống IoT thương mại có chi phí đầu tư cao, cấu hình phức tạp, khó triển khai ở quy mô hộ gia đình. Điều này làm hạn chế khả năng phổ biến và ứng dụng rộng rãi trong thực tế sản xuất nông nghiệp tại Việt Nam.

2.4. Vai trò của trí tuệ nhân tạo trong hỗ trợ lập quy trình trồng nấm
Trí tuệ nhân tạo (AI) đang ngày càng được ứng dụng rộng rãi trong nhiều lĩnh vực, trong đó có nông nghiệp. AI có khả năng tổng hợp, phân tích dữ liệu từ nhiều nguồn khác nhau và đưa ra các quyết định hoặc khuyến nghị dựa trên các mô hình đã được huấn luyện.
Trong trồng nấm, AI có thể được sử dụng để xây dựng quy trình kỹ thuật trồng phù hợp cho từng loại nấm và từng giai đoạn sinh trưởng. Thay vì người trồng phải tự tìm kiếm tài liệu hoặc dựa vào kinh nghiệm cá nhân, AI có thể tự động đề xuất các thông số kỹ thuật như nhiệt độ, độ ẩm và các lưu ý quan trọng trong từng giai đoạn.
Tuy nhiên, hiện nay các nghiên cứu và ứng dụng AI trong trồng nấm vẫn còn hạn chế, chủ yếu tập trung vào nhận dạng bệnh hoặc phân tích hình ảnh. Các hệ thống AI hỗ trợ lập quy trình kỹ thuật và kết hợp trực tiếp với hệ thống giám sát môi trường theo thời gian thực vẫn chưa được nghiên cứu và triển khai rộng rãi.
2.5. Khoảng trống nghiên cứu và hướng tiếp cận của đề tài
Từ các phân tích trên có thể rút ra một số nhận định sau:
-Các hệ thống IoT trong trồng nấm chủ yếu tập trung vào giám sát môi trường, chưa hỗ trợ đầy đủ cho việc ra quyết định kỹ thuật.
-Ứng dụng AI trong trồng nấm còn rời rạc, thiếu sự tích hợp với hệ thống giám sát môi trường thực tế.
-Chưa có nhiều giải pháp tích hợp AI và IoT có chi phí thấp, phù hợp với điều kiện sản xuất nhỏ lẻ tại Việt Nam.
Do đó, đề tài “Xây dựng hệ thống AI hỗ trợ lập quy trình, giám sát môi trường và hướng dẫn trồng nấm thông minh sử dụng ESP32” được thực hiện nhằm tiếp cận theo hướng tích hợp giữa trí tuệ nhân tạo và hệ thống nhúng chi phí thấp. Đề tài hướng tới xây dựng một hệ thống hoàn chỉnh, có khả năng hỗ trợ người trồng nấm từ khâu lập quy trình kỹ thuật đến giám sát và cảnh báo môi trường, góp phần nâng cao hiệu quả và tính bền vững của sản xuất nông nghiệp.
III. MÔ HÌNH HOẠT ĐỘNG CỦA HỆ THỐNG TRỒNG NẤM THÔNG MINH
<img width="550" height="331" alt="image" src="https://github.com/user-attachments/assets/f15e2d20-3b3e-499d-b026-cd319c0befdf" />
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
DEPARTMENT OF EDUCATION AND TRAINING OF DA NANG
NGUYEN KHUYEN HIGH SCHOOL
**********************************
SUBMISSION TOPIC
SCIENCE AND TECHNOLOGY COMPETITION
2025 - 2026 ACADEMIC YEAR
Research on intelligent monitoring solutions
for mushroom cultivation models using AI and IoT
Field: 嵌入式系統
Author: Dang Nhat Tan
In the context of the 4.0 industrial revolution and digital transformation in agriculture, the application of Internet of Things (IoT) and Artificial Intelligence (AI) technology to cultivation activities is becoming an inevitable trend to improve labor productivity, reduce production costs, and optimize management processes. In particular, the mushroom cultivation industry – an agricultural sector requiring strict control of environmental factors such as temperature, humidity, CO2 concentration, and light intensity – often faces major challenges due to weather fluctuations, diseases, and a lack of automated monitoring systems. According to a report by the United Nations Food and Agriculture Organization (FAO, 2023), global mushroom production has increased by an average of 10-15% annually over the past decade, but in Vietnam, the rate of product loss due to unsuitable environmental conditions can reach 20-30%, leading to significant economic losses for farmers [1].

To illustrate this issue, consider the case of straw mushroom cultivation in central Vietnamese provinces such as Quang Nam. Straw mushrooms require a stable temperature of 28-32°C and humidity of 75-85%. If the temperature exceeds 35°C, the mushrooms can wilt, leading to a complete crop loss. According to statistics from the Ministry of Agriculture and Rural Development of Vietnam (2022), thousands of tons of mushrooms are damaged annually due to uncontrolled environmental conditions, causing billions of dong in losses. Traditional monitoring systems mainly rely on manual sensors and handwritten records, lacking real-time forecasting capabilities and data-driven decision support, thus reducing overall production efficiency. For example, farmers often have to manually check daily, leading to errors and delays in adjustments.

Meanwhile, commercial solutions such as FarmBot or IBM Watson Agriculture systems offer advanced features but are expensive, often exceeding the investment capacity of smallholder farmers in developing countries like Vietnam [2]. FarmBot, for example, is an automated farming robot costing around 50-100 million dong, while IBM Watson requires a cloud subscription with a monthly fee. These solutions are suitable for large farms in Europe or the US, but not feasible for Vietnamese households with small growing areas (under 1,000 m²). The open-source community has developed many supporting platforms, such as Arduino for IoT and Google Apps Script for AI integration, but there is still a lack of comprehensive integration to specifically support the mushroom cultivation industry. Typical studies from the Journal of Agriculture and Food Research (2022) show that combining IoT with AI can reduce losses by up to 25-40% through environmental forecasting and timely reminders [3]. However, current systems do not support flexible mushroom cultivation routes according to each strain, real-time AI assessment based on sensor data, and user-friendly web interfaces for non-experts.

For example, in the study by Hossain et al. (2022), an IoT system based on ESP32 was deployed to monitor mushroom farm automation, achieving up to 100% accuracy in classifying harmful mushrooms using an ensemble ML model, but still lacking integration with big AI languages ​​like Gemini to create automated planting routes [3]. This study was conducted in Bangladesh, with similar climatic conditions to Vietnam, and the results showed that the system reduced monitoring time from 4 hours/day to 30 minutes. Similarly, the comprehensive review by Zhang et al. (2024) on PMC highlighted that integrating AI with IoT not only improves environmental control but also contributes to sustainable mushroom production, reducing energy consumption by up to 20% [4]. These gaps highlight the need for an open-source, low-cost system suitable for Vietnam's conditions, where agriculture still accounts for a large proportion of GDP (approximately 14% according to the World Bank, 2023). Given the above context, the topic "Smart Mushroom Cultivation Monitoring and Support System Based on AI and IoT" is of urgent importance in both scientific and practical aspects:
Scientifically: The topic contributes to the development of an integrated IoT-AI model based on open-source code, expanding the research capabilities for real-time environmental monitoring and optimizing smart agricultural processes, while providing experimental data to evaluate system performance under real-world conditions. Specifically, the topic will explore how to use the Gemini model to create dynamic mushroom cultivation pathways, something that previous studies have not addressed in detail, and analyze data with tools like Pandas to assess errors.
Practically: The topic aims to build a low-cost system (under 10 million VND for the prototype model) serving smallholder farmers, training and research institutions, contributing to promoting sustainable agriculture and food safety in Vietnam. The system can be deployed in the central provinces.
For example, Quang Nam province, where mushroom cultivation is thriving with an annual output of thousands of tons.

The results of this project not only create an open platform for mushroom monitoring but can also be extended to other crops such as vegetables or flowers, supporting AI based on the Gemini model and a web interface using Flask, thereby promoting the trend of open technology in agriculture. In addition, the project will also provide practical recommendations for implementing the system on small farms, including how to integrate with mobile devices so that farmers can easily monitor via app, and economic evaluation such as ROI (Return on Investment) estimated at 150% in 2 years.

II. OVERVIEW OF THE RESEARCH PROBLEM
2.1. The Development of Smart Agriculture and Environmental Monitoring Systems
In recent years, along with the development of the Fourth Industrial Revolution (Industry 4.0), smart agriculture has become one of the key research and application directions aimed at improving agricultural production efficiency. Smart agriculture is a production model that applies modern technologies such as the Internet of Things (IoT), artificial intelligence (AI), cloud computing, and automation to monitor, analyze, and optimize farming processes. Some achievements in applying modern technologies to optimize farming processes include:

<img width="189" height="150" alt="image" src="https://github.com/user-attachments/assets/c5cdc222-b31b-413c-99d4-31528360dc7b" />
<img width="323" height="149" alt="image" src="https://github.com/user-attachments/assets/5d4111b0-5e36-453e-b5d2-a95a59b94915" />

Hands Free Hectare Project (UK) FarmWise (USA) has developed an automated weed-removing robot using AI algorithms and computer vision to distinguish between crops and weeds,

completely automatically removing weeds accurately without chemicals.

2.2. Technical Specifics in Mushroom Cultivation
Mushroom cultivation is an agricultural field with highly technical specifics compared to many other crops. Mushrooms are heterotrophic organisms, non-photosynthetic, and their growth and development depend heavily on surrounding environmental conditions. Parameters such as temperature, air humidity, substrate moisture, and ventilation directly affect the development of mycelium and the formation of fruiting bodies.
Each type of mushroom has different environmental requirements, and the technical parameters change significantly during each growth stage. For example, the mycelium growth stage requires high humidity and a closed environment, while the fruiting body stage requires good ventilation and diffused light. Precisely controlling these parameters is crucial to mushroom yield and quality.

In practice, many mushroom growers still rely primarily on personal experience to adjust the growing environment. This method carries many risks, especially when weather conditions change suddenly, leading to disease, mycelial rot, or reduced yield. Therefore, the need to apply technical systems to support the control of the mushroom cultivation process is becoming increasingly urgent. Some strict requirements for certain types of mushrooms include:

Temperature: The most suitable range is 30–38°C; low temperatures slow mushroom growth and make them susceptible to disease.

Air humidity: Must be maintained at 80–90% for optimal mushroom formation and growth.

Substrate moisture: The substrate (straw) must be sufficiently moist, neither dry nor waterlogged; excessive wetness can easily lead to rot and mold infection.

<img width="147" height="147" alt="image" src="https://github.com/user-attachments/assets/bf863a0a-160c-44eb-ba39-d9fb1b9f833f" />

Straw Mushrooms

Temperature: Suitable temperature is between 18–25°C; high temperatures hinder mushroom growth, resulting in short stems and small caps.

Air humidity: Maintain 85–95% for optimal mushroom growth.

Substrate humidity: The substrate must be sufficiently moist, neither dry nor waterlogged, to prevent mycelial rot.

<img width="151" height="151" alt="image" src="https://github.com/user-attachments/assets/df0f3b80-2847-453d-8d2c-61307c71c140" />

Elephant's Leg Mushroom
Temperature: Suitable range is 22–30°C.

Air humidity: Needs to be maintained at 80–90%.

Substrate humidity: Approximately 60–65%, not dry, not waterlogged.

<img width="158" height="123" alt="image" src="https://github.com/user-attachments/assets/1d90130c-bfc2-4a64-8bbe-3662a2f4d8ac" />

Oyster Mushroom
2.3. IoT System Applications in Mushroom Cultivation
The Internet of Things (IoT) has been widely applied in agriculture, especially in monitoring the growing environment. In mushroom cultivation models, IoT systems typically include sensors that measure temperature, humidity, and light, combined with microcontrollers to collect and transmit data to a monitoring center.
Several studies have shown that applying IoT helps mushroom growers continuously and accurately monitor environmental conditions, thereby reducing reliance on intuition and experience. However, most current IoT systems only perform data collection and display functions, lacking the ability to analyze and provide specific technical recommendations to growers.
In addition, many commercial IoT systems have high investment costs and complex configurations.
The process is complex and difficult to implement at the household level. This limits its widespread adoption and application in agricultural production in Vietnam.

2.4. The Role of Artificial Intelligence in Supporting Mushroom Cultivation Process Development
Artificial intelligence (AI) is increasingly being applied in many fields, including agriculture. AI has the ability to synthesize and analyze data from various sources and make decisions or recommendations based on trained models.
In mushroom cultivation, AI can be used to develop appropriate cultivation techniques for each type of mushroom and each growth stage. Instead of growers having to search for documents or rely on personal experience, AI can automatically suggest technical parameters such as temperature, humidity, and important considerations at each stage.

However, currently, research and applications of AI in mushroom cultivation are still limited, mainly focusing on disease identification or image analysis. AI systems that support technical process planning and integrate directly with real-time environmental monitoring systems have not yet been widely researched and implemented.
2.5. Research Gaps and Approaches of the Project
From the above analysis, the following observations can be made:
- IoT systems in mushroom cultivation mainly focus on environmental monitoring and do not fully support technical decision-making.

- AI applications in mushroom cultivation are fragmented and lack integration with actual environmental monitoring systems.

- There are not many low-cost AI and IoT integration solutions suitable for small-scale production in Vietnam.

Therefore, the project "Building an AI system to support process planning, environmental monitoring, and guidance for smart mushroom cultivation using ESP32" is undertaken to approach the integration of artificial intelligence and low-cost embedded systems. This project aims to build a complete system capable of supporting mushroom growers from technical process planning to environmental monitoring and warning, contributing to improved efficiency and sustainability of agricultural production.

III. OPERATING MODEL OF THE SMART MUSHROOM CULTIVATION SYSTEM
<img width="1766" height="606" alt="eb7722b8-ffb7-4186-88a7-bac6fcf405fe" src="https://github.com/user-attachments/assets/43d5bf9f-021d-4128-a338-928939b3aa57" />










