# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Hoàng Đức An · Người gắn nhãn 2: Lê Hiền Hiếu (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Ngầm | Không | Ngầm |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng (ghi "Do khách hàng") | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 18 / 20 = 90%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 8 (Hệ thống vs Ngầm → chốt Ngầm):** Khi trợ lý bịa căn cứ ("Điều 7.2") nhưng kết quả số tiền hoàn vẫn đúng khiến cả khách lẫn hệ thống không phát hiện hay báo lỗi, gắn nhãn **Ngầm** thay vì Hệ thống.
- **Ca 13 (Giới hạn hệ thống vs Hệ thống → chốt Giới hạn hệ thống):** Gắn nhãn theo nguyên nhân gốc là yêu cầu bảo hiểm đối tác nằm ngoài phạm vi trợ lý (**Giới hạn hệ thống**), không gắn theo việc trợ lý xử lý câu từ chưa khéo.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `bank_transfer_failed` mã lỗi sai định dạng STK, ngưỡng > 1% tổng lệnh/ngày, kiểm tra hằng ngày | Thêm kiểm tra định dạng & số chữ số STK theo ngân hàng ngay trước khi tạo lệnh hoàn | Kỹ sư Backend |
| 20 | Hệ thống | Event `refund_issued` xuất hiện ≥ 2 lần cho cùng `order_id`, ngưỡng > 0 ca/ngày, cảnh báo tức thời | Thêm khoá chống trùng (`idempotency_key` theo `order_id`) và khoá trạng thái đơn khi đang xử lý | Kỹ sư Backend |
| 3 | Ngữ cảnh | Event `ticket_reopened` kèm lý do "chưa nhận tiền" trên đơn đã hoàn ví, ngưỡng > 2%/tuần, rà soát hằng tuần | Ghi rõ kênh nhận tiền ("Ví LogiX trong 5 phút") và hướng dẫn rút về ngân hàng ngay trong tin nhắn xác nhận | Quản lý sản phẩm |
| 13 | Giới hạn hệ thống | Event `out_of_scope_detected` hoặc khách mở lại sau câu trả lời chung chung về bảo hiểm, ngưỡng > 1%/tuần, rà soát hằng tuần | Thêm bộ phân loại phạm vi (guardrail) nhận diện yêu cầu bảo hiểm đối tác để từ chối rõ ràng và chuyển nhân viên kèm tóm tắt | Kỹ sư AI |
| 5 | Ngầm | Job đối soát cuối ngày so `refund_amount > paid_amount` trên event `refund_issued`, ngưỡng > 0 đơn/ngày, chạy hằng ngày | Sửa công thức lấy giá sau giảm (`net_paid_amount`) từ sổ cái và chạy kiểm tra tự động trước khi xuất lệnh hoàn | Kỹ sư Dữ liệu |
