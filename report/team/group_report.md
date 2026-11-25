# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- **Tên nhóm:** NhomT2
- **Lớp:** L3B
- **Repo nhóm:** `K5-L3B-DAY13-NhomT2-LaunchEconomics`
- **Thành viên**:
  - **Lê Hiền Hiếu** (`2A202603940`) — Người giữ hồ sơ + Người gắn nhãn 2
  - **Hoàng Đức An** (`2A202603800`) — Người viết code 1 (CP1–CP2) + Người gắn nhãn 1 + Phụ trách chỉ số/event
  - **Lã Quốc Nghị** (`2A202603947`) — Người kiểm số + Người viết code 2 (CP4) + Phụ trách bảng chi phí & Pilot

## 2. Mục tiêu và cách tiếp cận

Xây dựng bộ **hồ sơ launch v0** cho trợ lý hoàn phí của công ty giả định **LogiX-VN** (12 depot, 40 nhân viên CSKH, 45.000 yêu cầu/tháng) dựa trên dữ liệu giả lập gồm 1.200 yêu cầu (1.624 lần chạy) để trình hội đồng **Gate 2a** xét duyệt kế hoạch pilot.

Cách làm việc của nhóm 3 người: phân quyền sở hữu file độc lập theo từng checkpoint (tránh xung đột khi merge GitHub), đổi người viết code sau giờ giải lao để ít nhất 2 thành viên tự tay lập trình tính toán (`Hoàng Đức An` phụ trách CP1–CP2, `Lã Quốc Nghị` phụ trách CP4), gắn nhãn độc lập 20 ca lỗi không trao đổi, và kiểm số độc lập bằng `awk` đối chiếu với Python.

## 3. Giải pháp

- **Nhiệm vụ A (CP1 — Mô hình chi phí):** Lập trình 3 hàm kiểm thử đáp án biết trước `(1,20 · 1,25 · 1,25)` và mô hình chi phí `mo_hinh()` trong [src/lab13.py](../../src/lab13.py); đối chiếu tay bằng `awk` và tổng hợp bảng A1–A4 trong [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ B (CP2 — Độ nhạy):** Chạy 9 kịch bản đổi từng yếu tố (B1), đổi cặp (B2), so sánh giới hạn 1/2/3 lần chạy trên toàn hệ thống (B3) và kịch bản xem lại 100% (B4) trong [src/lab13.py](../../src/lab13.py) và [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C (CP3 — Phân loại lỗi):** Hai thành viên gắn nhãn độc lập 20 ca lỗi theo 5 nhóm Google PAIR trong 8 phút, so nhãn, viết quy tắc phân biệt cho ca lệch và xây dựng bảng khắc phục 5 ca đại diện đủ 5 loại lỗi kèm event/ngưỡng đo được tại [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (CP4 — Kế hoạch pilot):** Tính cỡ mẫu D1, `power` và tỉ lệ mở lại hiện tại trong [src/lab13.py](../../src/lab13.py); trả lời 5 câu tách tác động (D2), ghi rõ đánh đổi MDE và hoàn thiện 3 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ` trong [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E & Duyệt chéo Gate 2a (CP5):** Đặc tả 5 chỉ số, 10 event có `trace_id` và 3 rủi ro kinh tế tại [chi_so.md](chi_so.md); tổng hợp hồ sơ một trang tại [ho_so_launch_v0.md](ho_so_launch_v0.md) và thực hiện duyệt chéo hội đồng với nhóm **CR7** tại [phieu_cham.md](phieu_cham.md).

## 4. Kết quả

- **Chi phí mỗi việc thành công (CP1):** `4.472 đ` (`simulated`), gấp `16,3×` hoá đơn token/tool (`274,7 đ/YC`); giờ nhân viên chiếm `92,5%` (`51,8%` làm lại + `40,7%` xem lại). Chi phí cả hệ thống đạt `5.865 đ/YC = 0,49×` so với `12.000 đ` (`simulated`). Thu hẹp về `noi_dia` (`0,22×`) + `hang_nang` (`0,69×`), cộng cố định `40 triệu đ/tháng` cho `4.599 đ = 0,38×` ở `45.000` YC/tháng hoặc `5.784 đ = 0,48×` khi khối lượng giảm một nửa (`simulated`); loại `quoc_te` (`1,88×`, lỗ) và `doi_tac` (`0,85×`, sát ngưỡng hoà vốn).
- **Độ nhạy (CP2):** Top 3 yếu tố ảnh hưởng mạnh nhất: (1) Số ca làm lại x2 (`+51,8%`), (2) Tỉ lệ xem lại x2 (`+40,7%`), (3) Lương nhân viên +25% (`+23,1%`) (`simulated`); giá token x2 chỉ `+5,6%`. Giới hạn **2 lần chạy** rẻ nhất cho cả hệ thống (`6.901.220 đ`, `simulated`). Nếu xem lại 100% ở `noi_dia + hang_nang`, chi phí lên `11.743–12.415 đ` (`0,98–1,03×`, `simulated`).
- **Lỗi & khắc phục (CP3):** Đồng thuận `18/20 = 90%` (lệch Ca 8 và Ca 13, đã thống nhất quy tắc 1 câu); 5 ca khắc phục đại diện đủ 5 loại Google PAIR có event, ngưỡng, tần suất đo được và 1 vai trò phụ trách.
- **Kế hoạch pilot & chỉ số (CP4–CP5):** Chia theo nhân viên `20 vs 20` (phân tầng 12 depot), MDE `6 điểm` (`n = 859`, `DE = 6,96`, `≥ 299` YC/NV), chấp nhận đánh đổi `power = 0,64` nếu tác động thật chỉ `5 điểm`; rollout `10% → 25% → 50%`, 3 luật dừng đủ 4 vế, rollback trong 30 phút, chốt `2027-01-15`. Chỉ số trong đợt chạy thử: chính `82,83%`, bỏ qua gợi ý `27,12%`, lỗi lọt khách `4,25%`.
- **Đề xuất cuối tại [ho_so_launch_v0.md](ho_so_launch_v0.md):** **Go có điều kiện** (3 điều kiện về phạm vi `noi_dia + hang_nang` & giới hạn 2 lần chạy + xác nhận đánh đổi `power 0,64`, đo giờ thật thay số `simulated` & lộ trình giảm xem lại, và vá 3 lỗi nghiêm trọng trước khi mở pilot).
- **Kết quả duyệt chéo Gate 2a:** Nhóm `NhomT2` hoàn thành đánh giá chéo cho nhóm `CR7` tại [phieu_cham.md](phieu_cham.md) (quyết định `Go có điều kiện`, `30/30`), đồng thời hoàn tất phiên hỏi–đáp bảo vệ hồ sơ của nhóm trước hội đồng.

## 5. Khó khăn và cách xử lý

- **Nhóm chỉ có 3 người thay vì 4 người:** Giải quyết bằng cách phân vai kiêm nhiệm rõ ràng trong `TEAM.md` và cố định quyền sở hữu từng file cho từng người, tránh hoàn toàn lỗi xung đột khi merge trên GitHub.
- **Lỗi hiển thị tiếng Việt trong terminal Windows khi chạy `src/lab13.py`:** `Lã Quốc Nghị` xử lý lại phần xuất chuẩn UTF-8 trong `src/lab13.py` (commit `5be467e`) để code chạy mượt trên cả Windows và macOS/Linux.
- **Nhầm lẫn phạm vi con số bất lợi trong hồ sơ một trang:** Khi rà soát chéo nội bộ trước 17:00, nhóm phát hiện Mục 6 thiếu con số bất lợi `power = 0,64` (đánh đổi từ MDE 5 điểm lên 6 điểm) và bổ sung ngay kèm điều kiện xác nhận của Giám đốc vận hành để đảm bảo tiêu chí C6.

## 6. Tổng hợp đóng góp

| Thành viên | Vai trò chính | Sản phẩm & đóng góp chính |
| --- | --- | --- |
| **Hoàng Đức An** (`2A202603800`) | Code 1 (CP1–CP2), Gắn nhãn 1, Chỉ số/Event | Code A1–A4, B1–B4 trong `src/lab13.py`; gắn nhãn 20 ca lỗi (`bang_loi.md`); hoàn thiện `chi_so.md` (5 chỉ số, 10 event có `trace_id`, 3 rủi ro kinh tế). |
| **Lã Quốc Nghị** (`2A202603947`) | Kiểm số, Code 2 (CP4), Pilot Plan | Kiểm số độc lập bằng `awk`; hoàn thiện `bang_chi_phi.md` (A1–A4, B1–B4); code D1 (`power 0,64`) & sửa UTF-8 trong `src/lab13.py`; hoàn thiện `pilot_plan.yaml`. |
| **Lê Hiền Hiếu** (`2A202603940`) | Giữ hồ sơ, Gắn nhãn 2, Duyệt chéo | Quản trị `TEAM.md`; gắn nhãn độc lập & hoàn thiện bảng đồng thuận + bảng khắc phục 5 ca trong `bang_loi.md`; tổng hợp `ho_so_launch_v0.md`; hoàn thiện `phieu_cham.md` (chấm CR7) và `group_report.md`. |

Chi tiết đóng góp và bằng chứng commit của từng thành viên nằm trong [TEAM.md](../../TEAM.md) và các báo cáo cá nhân `report/team/<MSSV>_<HoTen>.md`.

## 7. Hạn chế và hướng cải thiện

- **Dữ liệu giờ nhân viên còn ở dạng giả lập (`_simulated`):** Chiếm `92,5%` tổng chi phí nên biên lợi nhuận thực tế chưa được chứng minh; hướng khắc phục là bắt buộc ghi nhận `phut_xem_lai` và `phut_lam_lai` thật từ tuần 1 của pilot.
- **Đánh đổi sức mạnh thống kê (`power = 0,64` ở mức 5 điểm):** Do giới hạn 40 nhân viên, pilot có `36%` khả năng bỏ sót nếu tác động thật chỉ đạt 5 điểm; nếu kết quả ngày `2027-01-15` nằm sát ngưỡng nhưng tích cực, có thể cân nhắc kéo dài thời gian đo để tăng số yêu cầu/nhân viên và kiểm chứng ICC thực tế.
- **Rủi ro tràn tác động (spillover) cùng depot:** Cần theo dõi chặt log truy cập theo `staff_id` trong suốt thời gian pilot để phát hiện sớm việc dùng chung tài khoản giữa nhóm can thiệp và nhóm đối chứng.

## 8. Tài liệu tham khảo

- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com).
- Đề bài và tài liệu nội bộ Lab 13: [docs/du_lieu_va_cong_thuc.md](../../docs/du_lieu_va_cong_thuc.md), [docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).
