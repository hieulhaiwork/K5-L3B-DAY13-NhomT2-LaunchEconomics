# Báo cáo cá nhân — LeHienHieu-2A202603940

## 1. Thông tin thành viên

- Họ tên: Lê Hiền Hiếu
- MSSV: 2A202603940
- Email: hieulh.work@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): **Người gắn nhãn 2 kiêm giữ hồ sơ** (CP1–CP5) + Phụ trách bảng lỗi (`bang_loi.md`), duyệt chéo (`phieu_cham.md`) và báo cáo nhóm (`group_report.md`)

## 2. Phần việc phụ trách

- **Bước 0 & Quản trị repo:** Tạo repo nhóm đúng quy ước `K5-L3B-DAY13-NhomT2-LaunchEconomics`, điền thông tin nhóm và phân công vai trò kiêm nhiệm cho 3 thành viên trong `TEAM.md`.
- **CP1–CP5 (Người giữ hồ sơ):** Theo dõi tiến độ các checkpoint, tổng hợp liên tục 7 mục và đề xuất cuối cùng trong `report/team/ho_so_launch_v0.md` sẵn sàng trước mốc 17:00.
- **CP3 (Người gắn nhãn 2):** Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR, so khớp đồng thuận với TV1 (`Hoàng Đức An`), viết quy tắc phân biệt ca lệch và hoàn thiện bảng khắc phục 5 ca đại diện trong `report/team/bang_loi.md`.
- **CP5 (Duyệt chéo Gate 2a & Đóng gói):** Thực hiện chấm chéo nhóm `CR7` trong `report/team/phieu_cham.md` và tổng hợp báo cáo nhóm `report/team/group_report.md`.

## 3. Đóng góp cụ thể

- Khởi tạo thông tin nhóm, bảng thành viên (3 người kiêm nhiệm đủ 4 vai trò) trong `TEAM.md` và điền thông tin đầu trang `report/team/ho_so_launch_v0.md`.
- Xuyên suốt CP1–CP5, cập nhật đầy đủ 7 mục trong `report/team/ho_so_launch_v0.md` từ số liệu đã đối chiếu của TV1 và TV2, đảm bảo gắn nhãn `simulated` cho mọi số giả lập, nêu rõ con số bất lợi (`power = 0,64` nếu tác động thật chỉ 5 điểm; xem lại 100% lên `0,98–1,03×`, `simulated`) và chốt đề xuất **Go có điều kiện** (3 điều kiện có người phụ trách và ngày kiểm tra).
- Gắn nhãn độc lập 20 ca lỗi ở CP3, đối chiếu đạt đồng thuận **18/20 (90%)**, chuẩn hóa Ca 14 về `Do người dùng`, viết quy tắc phân biệt 1 câu cho 2 ca không trùng (Ca 8 → `Ngầm`, Ca 13 → `Giới hạn hệ thống`) và xây dựng bảng khắc phục 5 ca (Ca 1, 20, 3, 13, 5) đủ 5 loại Google PAIR với event, ngưỡng, tần suất đo được và 1 vai trò phụ trách trong `report/team/bang_loi.md`.
- Hoàn thiện phiếu chấm hội đồng Gate 2a cho nhóm **CR7** (`30/30`, quyết định `Go có điều kiện`, ghi lại câu hỏi về chỉ số đợt chạy thử `82,83%` & ngưỡng mở lại `4,25%` cùng câu trả lời tại buổi) trong `report/team/phieu_cham.md`.
- Tổng hợp báo cáo nhóm `report/team/group_report.md` (8 mục) từ các file hồ sơ và lịch sử commit thực tế của cả 3 thành viên.

## 4. Bằng chứng

- `TEAM.md` và `report/team/ho_so_launch_v0.md`:
  - Commit `efb1fea`: Điền `TEAM.md` và Mục 1, Mục 3 (CP1: CPS `4.472 đ` `[simulated]`, cả hệ thống `5.865 đ = 0,49×`, thu hẹp `noi_dia + hang_nang` + cố định `4.599 đ = 0,38×` `[simulated]`).
  - Commit `244bb21`: Cập nhật Mục 2 (CP2: top 3 yếu tố nhạy nhất `+51,8%` / `+40,7%` / `+23,1%`, giới hạn 2 lần chạy `6,90 tr đ` `[simulated]`).
  - Commit `b4cb475`: Cập nhật Mục 6 (CP4: kế hoạch pilot chia theo nhân viên 20 vs 20, MDE 6 điểm, 3 luật dừng).
  - Commit `1f3cfdd`: Hoàn thiện Mục 4, Mục 7, bổ sung bất lợi `power = 0,64` ở Mục 6 và chốt đề xuất **Go có điều kiện** (3 điều kiện cụ thể).
- `report/team/bang_loi.md` (commit `87345a9`): Hai bộ nhãn độc lập 20 ca, tỉ lệ đồng thuận `18/20 = 90%`, quy tắc phân biệt Ca 8 & Ca 13, bảng khắc phục 5 ca đủ 5 loại Google PAIR.
- `report/team/phieu_cham.md` (commit `fff48ca`): Phiếu chấm hội đồng Gate 2a cho nhóm **CR7** (`30/30`, `Go có điều kiện`).
- `report/team/group_report.md`: Báo cáo nhóm ngắn đủ 8 mục, đã kiểm tra không có từ cấm trong toàn thư mục `report/team/`.

## 5. Công cụ AI đã dùng

- Sử dụng trợ lý AI (Antigravity) để hỗ trợ lập kế hoạch phân việc chống xung đột Git cho nhóm 3 người, trích xuất 20 ca lỗi từ file `.docx`, tổng hợp bảng khắc phục, rà soát tiêu chí rubric (C6–C8) cho `ho_so_launch_v0.md`.
- Tự kiểm tra kết quả bằng cách tự gắn nhãn độc lập 20 ca lỗi trước khi đối chiếu với TV1, kiểm tra chéo từng con số trong `ho_so_launch_v0.md` với `bang_chi_phi.md`, `pilot_plan.yaml`, `chi_so.md`, tiếp thu nhận xét chéo từ TV2 để bổ sung `power = 0,64`, và kiểm tra tự động không còn từ cấm trong toàn bộ hồ sơ `report/team/`.

## 6. Tự đánh giá

- Hoàn thành đầy đủ, đúng mốc 17:00 toàn bộ hồ sơ launch v0 và phiếu chấm duyệt chéo; phối hợp tốt với 2 thành viên còn lại theo nguyên tắc phân quyền sở hữu file nên không xảy ra lỗi merge conflict trên GitHub.
