# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: NhomT2 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc thành công (simulated), gấp 16,3x hoá đơn token/tool (274,7 đ/YC); làm lại 51,8%, xem lại 40,7% | Giả lập | Kỹ sư AI |
| 2 · Ba yếu tố nhạy nhất | (1) Số ca làm lại x2: +51,8% (6.787 đ); (2) Tỉ lệ xem lại x2: +40,7% (6.292 đ); (3) Lương NV +25%: +23,1% (5.506 đ) — giá token x2 chỉ +5,6%; giới hạn 2 lần chạy rẻ nhất cả hệ thống (6,90 tr đ) (simulated) | Giả lập | Kỹ sư AI |
| 3 · So với nhân viên tự làm | Toàn bộ 5.865 đ/YC = 0,49x (simulated), riêng quoc_te 1,88x (lỗ); thu hẹp noi_dia+hang_nang + 40 tr/tháng cố định: 4.599 đ = 0,38x (45k YC/tháng) hoặc 5.784 đ = 0,48x (22,5k YC/tháng) (simulated) | Giả lập | Quản lý vận hành CSKH |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử: chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), lỗi lọt khách 4,25% (51/1.200); thêm 2 chỉ số tự đề xuất, 10 event có trace_id | Xong, có bằng chứng | Kỹ sư Dữ liệu |
| 5 · Bảng lỗi và cách khắc phục | 20 ca gắn nhãn độc lập, đồng thuận 18/20 (90%), đủ 5 loại Google PAIR; 5 ca khắc phục có event/ngưỡng đo được và 1 vai trò phụ trách | Xong, có bằng chứng | Kỹ sư AI |
| 6 · Pilot plan | Chia theo NV (20 vs 20, phân tầng 12 depot), phạm vi noi_dia+hang_nang; MDE 6 điểm (n=859, DE=6,96, ≥299 YC/NV); bất lợi: nếu tác động thật chỉ 5 điểm thì power = 0,64 (36% bỏ sót), chấp nhận vì 40 NV không đủ mẫu cho 5 điểm; rollout 10%→25%→50%, 3 luật dừng đủ 4 vế (chi phí >8.000 đ simulated), rollback 30 phút, chốt 2027-01-15 | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại x2: CPS +51,8% (6.787 đ); xem lại 100% kéo dài: 11.743–12.415 đ (0,98–1,03×); khối lượng giảm 50%: cố định +2.370 đ/việc (tổng 5.784 đ) (simulated) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go có điều kiện

- Điều kiện 1 (Phạm vi, giới hạn chạy & đánh đổi power): Chỉ mở pilot cho noi_dia + hang_nang (loại quoc_te 1,88× lỗ và doi_tac 0,85×, simulated), giới hạn tối đa 2 lần chạy (rẻ nhất cả hệ thống 6,90 tr đ, simulated), và xác nhận văn bản chấp nhận đánh đổi MDE 6 điểm (power = 0,64 nếu tác động thật 5 điểm) trước khi chạy — Phụ trách: Giám đốc vận hành LogiX-VN · Kiểm tra: 2026-12-04 (trước ngày bắt đầu 2026-12-07).
- Điều kiện 2 (Đo giờ thật thay số giả lập & kiểm soát xem lại): Ghi nhận phut_xem_lai, phut_lam_lai thật từ event để thay 2 cột simulated; áp dụng lộ trình giảm xem lại khi tỉ lệ sua + bo < 15% và thời gian xem ≤ 4,8 phút/lần để tránh biên lợi nhuận âm (1,03× nếu xem lại 100%, simulated) — Phụ trách: Trưởng nhóm CSKH · Kiểm tra: 2026-12-21 (cuối tuần rollout 25%).
- Điều kiện 3 (Vá lỗi nghiêm trọng trước khi mở): Hoàn tất khoá chống hoàn trùng (idempotency_key — Ca 20), đối soát giá sau giảm (Ca 5) và guardrail ngoài phạm vi bảo hiểm (Ca 13); tuân thủ đủ 3 luật dừng và quyền tắt trong 30 phút ở pilot_plan.yaml — Phụ trách: Kỹ sư Backend · Kiểm tra: 2026-12-04.
