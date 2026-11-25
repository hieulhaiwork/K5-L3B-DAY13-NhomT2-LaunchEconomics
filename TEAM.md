# Team

## Thông tin nhóm

- Tên nhóm: NhomT2
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-NhomT2-LaunchEconomics`
- URL repo, nhánh nộp, commit chốt: https://github.com/hieulhaiwork/K5-L3B-DAY13-NhomT2-LaunchEconomics, nhánh `main`, commit 

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Lê Hiền Hiếu       | 2A202603940     |  hieulh.work@gmail.com     | hieulhaiwork        | Người giữ hồ sơ + Người gắn nhãn 2        |
|   2 | Hoàng Đức An       | 2A202603800     | anduchoang2701@gmail.com      | katogithub2701       | Người viết code 1 + Người gắn nhãn 1        |
|   3 | Lã Quốc Nghị       | 2A202603947     | quocnghidev@gmail.com      | quocnghidev       | Người kiểm số + Người viết code 2        |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## HoangDucAn-2A202603800

### Phần việc phụ trách

- **Người viết code 1** (CP1–CP2) trong `src/lab13.py`, bàn giao quyền sửa file cho TV2 sau giờ giải lao.
- **Người gắn nhãn 1** (CP3): gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR và đối chiếu đồng thuận với TV3.
- Phụ trách đặc tả chỉ số, danh sách event và rủi ro kinh tế trong `report/team/chi_so.md`.

### Đóng góp cụ thể

- Code A1–A4 (3 phép thử `mo_hinh`, tách theo `loai`, chi phí cố định 40 triệu đ/tháng) và B1–B4 (9 kịch bản độ nhạy, đổi cặp + xếp hạng, chi phí cả hệ thống theo giới hạn chạy lại, kịch bản xem lại 100%) trong `src/lab13.py`.
- Tham gia gắn nhãn độc lập 20 ca lỗi và thống nhất bộ nhãn, 5 ca đại diện với TV3 ở CP3.
- Hoàn thiện `report/team/chi_so.md`: tính thử 3 chỉ số (Chính, Dùng, An toàn), đề xuất 2 chỉ số bổ sung, viết 10 event có `trace_id` kèm kiểm tra chéo, và điền 3 dòng rủi ro kinh tế.

### Bằng chứng

- `src/lab13.py`: 3 phép thử A1 đạt (`1,20`, `1,25`, `1,25`); CPS A2 = `4.472 đ` `[simulated]`; kiểm tra tuyến tính B1 đạt; B3 giới hạn 2 lần rẻ nhất cho cả hệ thống (`6.901.220 đ` `[simulated]`).
- `report/team/chi_so.md` (commits `28057a5`, `2c67c75`): chỉ số trong đợt chạy thử `82,83%` / `27,12%` / `4,25%`, 10 event có `trace_id`, 3 dòng rủi ro kinh tế `[simulated]`.
- Tham gia gắn nhãn 20 ca lỗi (commit `517c87f`).

## LaQuocNghi-2A202603947

### Phần việc phụ trách

- **Người kiểm số** (CP1–CP2): kiểm số độc lập kết quả code của TV1, điền A1–A4 và B1–B4 vào `report/team/bang_chi_phi.md`.
- **Người viết code 2** (CP4): nhận bàn giao `src/lab13.py` sau giờ giải lao, viết phần cỡ mẫu D1.
- Phụ trách kế hoạch pilot `report/team/pilot_plan.yaml`, và đối chiếu số giữa các file hồ sơ ở CP5.

### Đóng góp cụ thể

- Kiểm số A2 bằng `awk` đọc thẳng hai file CSV, độc lập với code của TV1; khớp 100%.
- Điền đủ A1–A4, B1–B4 trong `bang_chi_phi.md`, gắn nhãn `simulated` cho mọi số từ cột `_simulated`; thêm so sánh công bằng với nhân viên tự làm (`5.865 đ/yêu cầu = 0,49x` `[simulated]`).
- Viết `TODO CP4` trong `src/lab13.py`: năm câu D1, power khi tác động thật chỉ 5 điểm, ba tỉ lệ hiện tại để đặt luật dừng; sửa lỗi in tiếng Việt trên console Windows.
- Viết `pilot_plan.yaml`: chia theo nhân viên 20 + 20, mức chênh 6 điểm kèm đánh đổi, 3 luật dừng đủ bốn vế, rollback và ngày quyết định.

### Bằng chứng

- `report/team/bang_chi_phi.md` (commits `53cdcd2`, `2cd6ab2`): CPS `4.472 đ` `[simulated]`, gấp `16,3x` hoá đơn; giới hạn 2 lần rẻ nhất cả hệ thống (`6.901.220 đ` `[simulated]`); xem lại 100% `0,98x`–`1,03x` `[simulated]`.
- `src/lab13.py` (commit `5be467e`): D1 in `1.251` · `3.103` · `1.000` · `300` · `m ≥ 299`, `DE = 6,96`; power `0,64`; chạy được trên Windows không cần `PYTHONUTF8`.
- `report/team/pilot_plan.yaml` (commit `53cdcd2`): đọc được bằng `yaml.safe_load`, không còn dấu `?`, 3 luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ.
- Báo cáo cá nhân: `report/team/2A202603947_LaQuocNghi.md`.

## LeHienHieu-2A202603940

### Phần việc phụ trách

- **Người gắn nhãn 2 kiêm giữ hồ sơ** (CP1–CP5): quản trị `TEAM.md`, tổng hợp xuyên suốt `report/team/ho_so_launch_v0.md`.
- Gắn nhãn độc lập 20 ca lỗi theo Google PAIR và hoàn thiện bảng đồng thuận, quy tắc phân biệt, bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- Thực hiện chấm chéo hội đồng Gate 2a cho nhóm **CR7** (`report/team/phieu_cham.md`) và tổng hợp báo cáo nhóm (`report/team/group_report.md`).

### Đóng góp cụ thể

- Khởi tạo thông tin nhóm, bảng thành viên (3 người kiêm nhiệm đủ 4 vai trò) trong `TEAM.md` và cập nhật đầy đủ 7 mục + đề xuất **Go có điều kiện** (kèm bất lợi `power = 0,64` và nhãn `simulated`) trong `report/team/ho_so_launch_v0.md` trước 17:00.
- Gắn nhãn độc lập 20 ca lỗi đạt đồng thuận `18/20 = 90%`, viết quy tắc phân biệt Ca 8 & Ca 13 và xây dựng bảng khắc phục 5 ca đại diện đủ 5 loại Google PAIR trong `report/team/bang_loi.md`.
- Hoàn thiện phiếu chấm hội đồng cho nhóm `CR7` (`30/30`, `Go có điều kiện`, khớp hồ sơ thực tế của CR7) trong `report/team/phieu_cham.md` và tổng hợp báo cáo nhóm `report/team/group_report.md`.

### Bằng chứng

- `TEAM.md` & `report/team/ho_so_launch_v0.md` (commits `efb1fea`, `244bb21`, `b4cb475`, `1f3cfdd`).
- `report/team/bang_loi.md` (commit `87345a9`): đồng thuận `18/20 = 90%`, bảng khắc phục 5 ca đủ 5 loại lỗi.
- `report/team/phieu_cham.md` (commit `fff48ca`), `report/team/group_report.md` và báo cáo cá nhân `report/team/2A202603940_LeHienHieu.md`.
