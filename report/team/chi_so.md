# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | ... |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | ... |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | ... |
| Dùng | Nhóm tự đề xuất: ... | ... | Không cần tính |
| An toàn | Nhóm tự đề xuất: ... | ... | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien`, `arm` (control/treatment), `trace_id` | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý của trợ lý hiện ra |
| `staff_review_decision` | Nhân viên | `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai`, `trace_id` | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | `phut_lam_lai`, `ly_do`, `trace_id` | Khi nhân viên hoàn tất làm lại |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi nhận hoàn tiền vào sổ cái |
| `handoff_to_staff` | Agent | `reason`, `tom_tat`, `trace_id` | Khi chuyển yêu cầu sang nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `trace_id` | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | `reopened_at`, `reason`, `trace_id` | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | `so_tien_da_hoan`, `so_tien_dung`, `trace_id` | Khi kiểm tra mẫu hằng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (% đóng trong 24h & không mở lại trong 7 ngày):** nối `refund_request_created` với `ticket_closed` (kiểm tra `closed_at - created_at <= 24h`) và `ticket_reopened` (không có event trong 7 ngày sau khi đóng) qua `trace_id`.
- **Chỉ số dùng (Tỉ lệ bỏ qua gợi ý):** lấy từ `staff_review_decision` (`quyet_dinh` là `sua` hoặc `bo`) chia cho tổng số `staff_review_decision` (hoặc `agent_suggestion_shown`) có cùng `trace_id`.
- **Chỉ số an toàn (Tỉ lệ lỗi lọt đến khách):** lấy số `ticket_reopened` trong 7 ngày chia cho tổng số `refund_request_created`.
- **Chỉ số dùng (tự đề xuất — sẽ chốt ở CP4):** có thể đo bằng `agent_suggestion_shown` / `refund_request_created` (theo `arm = treatment`).
- **Chỉ số an toàn (tự đề xuất — sẽ chốt ở CP4):** có thể đo bằng `audit_sample_checked` (`so_tien_da_hoan != so_tien_dung`) hoặc đối soát `refund_ledger_write` theo `trace_id`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | CPS tăng **+51,8%**, lên **6.787 đ** [simulated] | Tỉ lệ ca `lam_lai` theo tuần > 7% (mẫu chạy thử trong phạm vi `noi_dia` + `hang_nang`: 4,9%) | Thu hẹp phạm vi về `noi_dia`, rà 20 trace làm lại gần nhất để sửa lỗi gốc | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | CPS **11.743 đ = 0,98×** nếu làm lại 9 phút; hoặc **12.415 đ = 1,03×** (đắt hơn nhân viên tự làm) nếu làm lại 15,3 phút [simulated] | Tỉ lệ yêu cầu bị xem lại còn > 50% ở cuối bước rollout 0.25 | Bật giảm xem lại theo bậc khi tỉ lệ `sua + bo` < 15% và thời gian xem lại ≤ 4,8 phút/lần | Trưởng nhóm CSKH |
| Khối lượng thực tế thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng làm tăng thêm **+1.185 đ/việc** ở 45.000 YC/tháng, lên **+2.370 đ/việc** (tổng **5.784 đ = 0,48×** [simulated]) nếu còn một nửa | Số việc thành công theo tuần < 50% kế hoạch | Tạm dừng mở rộng phạm vi pilot, đàm phán lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
