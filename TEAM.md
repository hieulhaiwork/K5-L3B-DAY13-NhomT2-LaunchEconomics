# Team

## Thông tin nhóm

- Tên nhóm: NhomT2
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-NhomT2-LaunchEconomics`
- URL repo, nhánh nộp, commit chốt: https://github.com/hieulhaiwork/K5-L3B-DAY13-NhomT2-LaunchEconomics, branch `main`, commit `placeholder` 

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

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-
