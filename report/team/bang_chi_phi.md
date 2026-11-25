# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 · ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 · ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 · ĐẠT |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút) | simulated |
| Tổng chi phí | 4.373.585 | | simulated (có phần giả lập) |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | đo từ trace |

Kiểm số: người kiểm số tính độc lập bằng `awk` trên hai file CSV (token 245.585 · tool 84.000 · chạy lại 93.804 · 890 và 1.132 phút · 978 việc thành công), khớp 100% với `src/lab13.py`.

- Chi phí mỗi việc thành công 4.472 đ gấp **16,3 lần** hoá đơn chia số yêu cầu (274,7 đ) [simulated]; giờ nhân viên (xem lại + làm lại) chiếm 92,5% tổng chi phí [simulated].
- Lớn nhất là **làm lại, 51,8%** tổng chi phí [simulated], tiếp theo là xem lại 40,7% [simulated]; token + tool chỉ 7,5%.
- So công bằng với 12.000 đ phải cộng 222 yêu cầu không thành công do nhân viên làm thay: (4.373.585 + 222 × 12.000) ÷ 1.200 = **5.865 đ/yêu cầu = 0,49×** [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× |

Tỉ lệ lần chạy `ok` theo lần thử (lần 1 · 2 · 3): noi_dia 91,0 · 75,7 · 38,9% · hang_nang 70,9 · 39,1 · 17,9% · quoc_te 30,0 · 11,4 · 2,2% · doi_tac 51,5 · 18,2 · 14,8%.

- **quoc_te** không đáng để trợ lý xử lý: 22.515 đ = 1,88× nhân viên tự làm [simulated], chỉ thành công 27,3%.
- Chạy lại tới 3 lần không giúp: với quoc_te lần 2 chỉ đúng 11,4%, lần 3 chỉ 2,2%; lỗi lặp lại trên cùng yêu cầu nên chạy lại chỉ thêm tiền (2,32 lần chạy/yêu cầu).
- doi_tac sát ngưỡng (0,85×) và có điều khoản riêng, nên cũng để ngoài phạm vi pilot; phạm vi đề xuất là noi_dia + hang_nang.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Phạm vi noi_dia + hang_nang trong mẫu: 982 yêu cầu, 900 việc thành công, chi phí mỗi việc thành công chưa cộng cố định 3.072.513 ÷ 900 = **3.414 đ** [simulated]. Chi phí cố định 40.000.000 đ/tháng; việc thành công mỗi tháng = khối lượng × 900 ÷ 1.200.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng (22.500 yêu cầu/tháng) | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× |

- Ở 45.000 yêu cầu/tháng, cố định chỉ thêm 1.185 đ/việc (4.599 đ = 0,38×) [simulated], không đổi kết luận.
- Khối lượng giảm một nửa thì cố định gấp đôi (2.370 đ/việc, 5.784 đ = 0,48×) [simulated]; giai đoạn pilot ít việc nên phải ghi rõ số đã cộng cố định ở khối lượng nào.

## B1 · Đổi từng yếu tố

Gốc (A2): 4.472 đ [simulated]. Mọi dòng dưới đây là simulated vì đều chứa tiền xem lại và làm lại.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ [simulated] | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ [simulated] | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ [simulated] | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ [simulated] | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ [simulated] | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ [simulated] | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ [simulated] | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ [simulated] | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ [simulated] | −8,1% |

Tự kiểm tra: mỗi kịch bản "giảm một nửa" giảm đúng bằng nửa mức tăng của "gấp đôi" (5,6 → 2,8 · 40,7 → 20,3 · 51,8 → 25,9); `src/lab13.py` in `DAT`.

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated], đúng bằng tổng hai tác động riêng (+5,6% + 40,7%) vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **Số ca làm lại** (+51,8%) · 2. **Tỉ lệ xem lại** (+40,7%) · 3. **Lương nhân viên** (+23,1% khi tăng 25%) [simulated]; giá token chỉ +5,6%, nên pilot phải theo dõi tỉ lệ làm lại và xem lại chứ không phải giá token.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay).

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ [simulated] | 319 | 7.449.781 đ [simulated] | **4.111 đ (thấp nhất)** [simulated] |
| 2 lần | 4.093.220 đ [simulated] | 234 | **6.901.220 đ (rẻ nhất)** [simulated] | 4.237 đ [simulated] |
| 3 lần | 4.373.585 đ [simulated] | 222 | 7.037.585 đ [simulated] | 4.472 đ [simulated] |

- **Giới hạn 2 lần** rẻ nhất cho công ty (6.901.220 đ) [simulated], **không trùng** với giới hạn 1 lần cho chi phí mỗi việc thành công thấp nhất (4.111 đ).
- Giới hạn 1 lần làm đẹp chỉ số nhưng đẩy thêm 85 yêu cầu sang nhân viên (319 so với 234), tốn thêm 548.561 đ cho cả hệ thống [simulated].

## B4 · Nếu phải xem lại tất cả

Phạm vi noi_dia + hang_nang: 982 yêu cầu, 948 yêu cầu có ít nhất một lần chạy ok × 5 phút xem lại = 9.480.000 đ; 48 ca làm lại; token + tool 224.513 đ; chia cho 900 việc thành công.

- Xem lại 100%: **11.743 đ = 0,98×** của 12.000 đ với 9 phút/ca làm lại; dùng trung bình dữ liệu 15,3 phút/ca thì **12.415 đ = 1,03×**, đắt hơn nhân viên tự làm [simulated].
- Hoà vốn chỉ khi mỗi lần xem lại ≤ 5,1 phút (9 phút làm lại) hoặc ≤ 4,8 phút (15,3 phút) [simulated]; tiền xem lại chiếm khoảng 90% chi phí.
- Pilot phải học được tỉ lệ xem lại có thể giảm an toàn xuống mức nào và thời gian mỗi lần xem lại có dưới 5 phút không; nếu bắt buộc xem lại 100% thì trợ lý gần như không tiết kiệm được gì.
