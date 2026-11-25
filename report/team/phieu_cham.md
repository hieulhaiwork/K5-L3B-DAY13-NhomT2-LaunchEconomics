# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): NhomT2 (Lớp L3B)
- Nhóm được chấm: CR7 (Lớp L3B)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất Go có điều kiện khớp số liệu: nêu đủ con số bất lợi (xem lại 100% lên 11.743 đ = 0,98–1,03×, làm lại x2 lên 6.787 đ/+51,8%, khối lượng giảm một nửa +2.370 đ/việc [simulated]; power còn 0,64 nếu tác động thật 5 điểm; lỗi Ca 7, Ca 20) kèm 4 điều kiện xử lý có vai trò phụ trách và ngày kiểm tra (2026-12-04, 2026-12-14, 2026-12-21) |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Gắn nhãn `[simulated]` nhất quán ở mọi mục dùng hai cột giờ (Mục 1, 2, 3, 7, điều kiện giảm xem lại và `simulated_inputs` trong `pilot_plan.yaml`); thu hẹp phạm vi về `noi_dia` (0,22×) + `hang_nang` (0,69×, cộng cố định 4.599 đ = 0,38×), loại `quoc_te` (1,88×) và `doi_tac` (0,85×) có lý do bằng số |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Đối chứng song song 20 + 20 nhân viên, ngẫu nhiên phân tầng theo 12 depot; đủ mẫu hiệu dụng 859 cho MDE 6 điểm (`DE = 6,96`, `m ≥ 299`), có kiểm soát tràn tác động theo tài khoản/`staff_id`; đủ 3 luật dừng (an toàn: vượt đối chứng +2 điểm hoặc trần 6% / ≥ 1 ca hoàn trùng trong 3 ngày; chi phí: > 8.000 đ simulated hoặc làm lại > 7% trong 2 tuần; sử dụng: bỏ qua > 40% hoặc mở < 60% trong 1 tuần) kèm rollback 30 phút (Giám đốc vận hành), chốt 2027-01-05 |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ của nhóm CR7 có đầy đủ bằng chứng bằng số, gắn nhãn `[simulated]` chặt chẽ, thu hẹp phạm vi hợp lý về `noi_dia + hang_nang` (3.414 đ chưa cố định, 4.599 đ = 0,38× ở 45.000 YC/tháng và 0,48× ở một nửa khối lượng, simulated), ghi nhận đúng chỉ số đợt chạy thử 82,83% (chưa kết luận nâng chỉ số), đồng thời nêu thẳng đánh đổi power 0,64 và có 4 điều kiện kèm 3 luật dừng đủ ngưỡng, thời hạn và vai trò quyết định.

**Một câu hỏi cho đội trình:** Đợt chạy thử đã đạt 82,83% đóng trong 24h và không mở lại (cao hơn baseline 70% hơn 12 điểm), sao chưa duyệt chạy rộng luôn? Và tỉ lệ mở lại 4,25% hiện tại ảnh hưởng gì đến việc đặt luật dừng?

**Câu trả lời của đội trình (ghi lại tại buổi):** Đợt chạy thử không có nhóm đối chứng nên chỉ được ghi nhận "chỉ số trong đợt chạy thử là 82,83%", không thể kết luận trợ lý đã nâng chỉ số — bắt buộc phải chạy pilot có đối chứng song song mới ra quyết định được. Ngoài ra, tỉ lệ mở lại trong 7 ngày hiện đã là 4,25% toàn mẫu (3,97% trong `noi_dia + hang_nang`), nên nếu đặt ngưỡng dừng an toàn cứng quá thấp (ví dụ 3%) thì pilot sẽ dừng ngay tuần đầu; luật dừng phải so với nhóm đối chứng cùng thời điểm (cao hơn ≥ 2 điểm) kèm trần tuyệt đối 6%.
