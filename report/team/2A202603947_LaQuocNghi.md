# Báo cáo cá nhân — LaQuocNghi-2A202603947

## 1. Thông tin thành viên

- Họ tên: Lã Quốc Nghị
- MSSV: 2A202603947
- Email: quocnghidev@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): **Người kiểm số** (CP1–CP2) + **Người viết code 2** (CP4, nhận bàn giao `src/lab13.py` sau giờ giải lao) + phụ trách bảng chi phí và kế hoạch pilot

## 2. Phần việc phụ trách

- **CP1 (Nhiệm vụ A):** kiểm số độc lập kết quả code của TV1; điền A1–A4 vào `report/team/bang_chi_phi.md`.
- **CP2 (Nhiệm vụ B):** điền B1–B4 (bảng độ nhạy, đổi cặp và xếp hạng, giới hạn số lần chạy, xem lại 100%) vào `report/team/bang_chi_phi.md`.
- **CP4 (Nhiệm vụ D):** viết `TODO CP4` trong `src/lab13.py` (cỡ mẫu D1, power, tỉ lệ hiện tại); viết toàn bộ `report/team/pilot_plan.yaml`.
- **CP5:** đối chiếu số giữa `bang_chi_phi.md`, `pilot_plan.yaml`, `chi_so.md` và `ho_so_launch_v0.md`; trả lời phần chi phí, độ nhạy, cỡ mẫu khi duyệt chéo.

## 3. Đóng góp cụ thể

- Kiểm số độc lập bằng `awk` đọc thẳng hai file CSV (không chạy lại code của TV1), ra token 245.585 đ, tool 84.000 đ, lần chạy 2–3 là 93.804 đ, 890 và 1.132 phút, 978 việc thành công: khớp 100% với `src/lab13.py`.
- Điền đủ A1–A4 và B1–B4 trong `bang_chi_phi.md`, gắn nhãn `simulated` cho mọi số từ hai cột `_simulated`; thêm phép so công bằng với nhân viên tự làm (5.865 đ/yêu cầu = 0,49× [simulated], đã cộng 222 yêu cầu không thành công) và chi phí đẩy sang nhân viên khi giới hạn 1 lần chạy (thêm 85 yêu cầu, 548.561 đ [simulated]).
- Viết code D1 trong `src/lab13.py`: hàm `co_mau` theo công thức của đề, hệ số thiết kế, năm câu a–e, power khi tác động thật chỉ 5 điểm (`proportion_effectsize` + `NormalIndPower`), và ba tỉ lệ hiện tại để đặt luật dừng.
- Sửa lỗi `UnicodeEncodeError` khiến `lab13.py` dừng ngay dòng đầu trên console Windows (`sys.stdout.reconfigure(encoding='utf-8')`), để file chạy được trên máy khác trong nhóm.
- Viết `pilot_plan.yaml`: chọn chia theo nhân viên 20 + 20, chấp nhận mức chênh 6 điểm và ghi rõ đánh đổi; ba luật dừng (an toàn, chi phí, sử dụng) đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ, ngưỡng đặt dựa trên tỉ lệ hiện tại; rollback, ngày quyết định và danh sách số giả lập.
- Đối chiếu `chi_so.md` của TV1 và `ho_so_launch_v0.md` của TV3 với số của mình; báo nhóm các chỗ lệch (tên vai trò phụ trách, giới hạn 2 lần chạy trong điều kiện 1 của hồ sơ).

## 4. Bằng chứng

- Commit `53cdcd2` (CP1 + CP4): A1–A4 trong `bang_chi_phi.md` và `pilot_plan.yaml`.
- Commit `2cd6ab2` (CP2): B1–B4 trong `bang_chi_phi.md`.
- Commit `5be467e` (CP4): code D1 và sửa lỗi in tiếng Việt trong `src/lab13.py`.
- Số chính:
  - A2: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ).
  - B3: giới hạn 2 lần chạy rẻ nhất cho cả hệ thống, 6.901.220 đ [simulated].
  - B4: xem lại 100% ra 11.743 đ (0,98×) hoặc 12.415 đ (1,03×) [simulated].
  - D1: 1.251 · 3.103 (42 người mỗi nhóm) · 1.000 · 300 · m ≥ 299, DE 6,96; power 0,64 nếu tác động thật là 5 điểm.
  - Tỉ lệ hiện tại: mở lại 4,25% (3,97% trong phạm vi), bỏ qua gợi ý 27,1%.
- Kiểm tra: `python lab13.py` chạy hết, ba phép thử in ĐẠT; `pilot_plan.yaml` đọc được bằng `yaml.safe_load`, không còn dấu `?` ngoài chú thích, cả ba luật dừng đủ bốn vế.

## 5. Công cụ AI đã dùng

- **Claude Code (Claude):** phân tích đề và rubric; viết code D1 trong `lab13.py`; soạn nội dung `bang_chi_phi.md` và `pilot_plan.yaml`; tìm và sửa lỗi in tiếng Việt trên Windows; đối chiếu số giữa các file của nhóm.
- **Cách tự kiểm tra:**
  - Tính lại các số A2 bằng `awk` trên hai file CSV, độc lập với code; khớp 100%.
  - Đối chiếu mọi số với bảng số tham khảo trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (sai số cho phép 2%).
  - Bấm tay các phép tính chính: 4.373.585 ÷ 978 = 4.472; (4.373.585 + 222 × 12.000) ÷ 1.200 = 5.865; DE = 1 + 74 × 0,02 = 2,48; 20 ÷ 0,02 = 1.000; thay m = 299 vào 20m ÷ (1 + (m − 1) × 0,02) được khoảng 859.
  - Chạy `yaml.safe_load` và lệnh tìm dấu `?` cho `pilot_plan.yaml`; tìm từ cấm theo quy tắc 5 của lab trong `report/team/`.
- Mọi lựa chọn AI đưa ra (đơn vị chia pilot, mức chênh 6 điểm, các ngưỡng luật dừng, ngày quyết định) đều được giải thích lý do và phương án bị loại trước khi đưa vào file.

## 6. Tự đánh giá

- **Đã làm tốt:**
  - Hoàn thành đủ phần việc được giao ở CP1, CP2, CP4 và phần đối chiếu số ở CP5; số trong `bang_chi_phi.md` và `pilot_plan.yaml` khớp đáp án tham khảo (sai số dưới 2%) và khớp với `chi_so.md`, `ho_so_launch_v0.md` của nhóm.
  - Kiểm số bằng một đường độc lập (`awk` trên CSV) thay vì chạy lại code của TV1, nên phép kiểm thật sự bắt được lỗi nếu có.
  - Chủ động nêu con số bất lợi thay vì che đi: xem lại 100% có thể đắt hơn nhân viên (1,03× [simulated]); thiết kế pilot chỉ có power 0,64 nếu tác động thật là 5 điểm.
  - Giữ đúng quy tắc mỗi file một người sửa, pull trước khi push; không phát sinh conflict, không force-push.
- **Chưa tốt và cách cải thiện:**
  - Dựa nhiều vào trợ lý AI để viết code D1 và soạn nội dung. Tôi đã tự kiểm lại từng số và hiểu lý do từng lựa chọn, nhưng lần sau sẽ tự viết phần tính cỡ mẫu trước rồi mới dùng AI để soát.
  - Mất thời gian ở khâu cài đặt (pip timeout, lỗi mã hoá tiếng Việt trên Windows); lần sau sẽ cài môi trường và chạy thử trước buổi lab.
