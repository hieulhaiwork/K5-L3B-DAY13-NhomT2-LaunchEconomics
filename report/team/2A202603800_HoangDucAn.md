# Báo cáo cá nhân — HoangDucAn-2A202603800

## 1. Thông tin thành viên

- Họ tên: Hoàng Đức An
- MSSV: 2A202603800
- Email: anduchoang2701@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): **Người viết code 1** (CP1–CP2) + **Người gắn nhãn 1** (CP3) + Phụ trách chỉ số/event (`chi_so.md`)

## 2. Phần việc phụ trách

- **CP1 & CP2 (Nhiệm vụ A & B):** Code phần A1–A4 và B1–B4 trong `src/lab13.py`; kiểm tra 3 phép thử A1 và quy luật tuyến tính B1; bàn giao quyền sửa `src/lab13.py` cho TV2 sau giờ giải lao.
- **CP3 (Nhiệm vụ C):** Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR, đối chiếu đồng thuận với TV3 và chọn 5 ca đại diện.
- **CP3–CP4 (Nhiệm vụ E1, E2):** Soạn đặc tả chỉ số, danh sách 10 event có `trace_id`, kiểm tra chéo event và bảng rủi ro kinh tế trong `report/team/chi_so.md`.

## 3. Đóng góp cụ thể

- Hoàn thành 3 hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`), hàm `mo_hinh(...)` (A2), tách theo `loai` (A3), và tính chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` (A4) trong `src/lab13.py`.
- Hoàn thành bảng độ nhạy B1 (9 kịch bản), B2 (đổi cặp + xếp hạng top 3 yếu tố), B3 (chi phí cả hệ thống với giới hạn 1/2/3 lần chạy) và B4 (xem lại 100% trong phạm vi `noi_dia` + `hang_nang`) trong `src/lab13.py`.
- Gắn nhãn độc lập 20 ca lỗi ở CP3, đối chiếu thống nhất với TV3 để hoàn thiện `report/team/bang_loi.md`.
- Hoàn thiện `report/team/chi_so.md`: tính thử 3 chỉ số trên 1.200 yêu cầu, đề xuất 2 chỉ số bổ sung (Dùng + An toàn), viết 10 event có `trace_id` kèm kiểm tra chéo, và điền 3 dòng rủi ro kinh tế lấy số từ bảng độ nhạy CP2.

## 4. Bằng chứng

- File code `src/lab13.py`:
  - 3 phép thử A1 đạt (`1,20`, `1,25`, `1,25`).
  - A2: tổng chi phí `4.373.585 đ`, `978` việc thành công, CPS `4.472 đ` `[simulated]` (gấp `16,3x` hoá đơn token+tool/YC `274,7 đ`).
  - B1–B4: top 3 yếu tố nhạy nhất là số ca làm lại (`+51,8%`), tỉ lệ xem lại (`+40,7%`), lương nhân viên `+25%` (`+23,1%`); giới hạn 2 lần chạy cho chi phí cả hệ thống thấp nhất (`6.901.220 đ` `[simulated]`); xem lại 100% ra `11.743 đ` (`0,98x`) với 9 phút/ca hoặc `12.415 đ` (`1,03x`) với 15,3 phút/ca `[simulated]`.
- File `report/team/chi_so.md` (commits `28057a5`, `2c67c75`):
  - Chỉ số trong đợt chạy thử: Chính `82,83%` (`994/1.200`), Dùng `27,12%` (`48/177`), An toàn `4,25%` (`51/1.200`).
  - 10 event có `trace_id` và 3 dòng rủi ro kinh tế `[simulated]`.
- Gắn nhãn 20 ca lỗi cùng nhóm (commit `517c87f`).

## 5. Công cụ AI đã dùng

- Sử dụng trợ lý lập trình AI (Antigravity) để hỗ trợ viết code phần B1–B4 trong `src/lab13.py` và soạn cấu trúc `report/team/chi_so.md`.
- Tự kiểm tra kết quả bằng cách chạy `python lab13.py` trong `.venv`, đối chiếu 3 phép thử A1, kiểm tra quy luật tuyến tính *"giảm một nửa = 1/2 mức tăng gấp đôi"* trong B1, và chạy script kiểm tra các con số trên `src/logix_requests.csv` cũng như rà soát không dùng từ cấm theo quy định của lab.

## 6. Tự đánh giá

- Hoàn thành đúng tiến độ các phần việc được giao ở CP1, CP2, CP3 và CP4; giữ đúng quy tắc sở hữu file nên không phát sinh conflict khi merge với các thành viên khác.
