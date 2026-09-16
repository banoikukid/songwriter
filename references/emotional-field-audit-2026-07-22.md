# Emotional-field audit — 2026-07-22

## Câu hỏi

Các tình khúc nổi tiếng có thường đưa cảm xúc ra khỏi độc thoại nhân vật để thời gian, không gian và hình tượng cùng mang cảm xúc không? Nếu có, cơ chế nào đáng route vào skill mà không biến thành quota cảnh vật?

## Mẫu và cách đọc

Mẫu nhỏ, chọn để có ca kinh điển, nhạc trẻ và phản-ví-dụ trực tiếp. Chỉ mã hóa chức năng; không lưu câu/hook/đạo cụ làm seed.

| Ca | Lane | Phân bố agency | Kết luận chức năng |
|---|---|---|---|
| *Diễm xưa* — Trịnh Công Sơn | FIELD-DOMINANT | mưa, lá, đường, đất rộng, sỏi đá cùng mang mòn mỏi và biến động | cảm xúc được tạo bởi cả một môi trường; nhân vật không phải chủ thể duy nhất |
| *Biển nhớ* — Trịnh Công Sơn | FIELD-DOMINANT | biển, đồi núi, sỏi đá, thành phố và ánh đèn thực hiện nhớ, chờ, gọi, buồn | personification kết thành một emotional field nhất quán quanh sự ra đi |
| *Nỗi nhớ mùa đông* — Phú Quang | MIXED | gió mùa, lá, cánh buồm, dòng sông, cây cầu biến vắng mặt thành không gian có thể bước vào | người kể vẫn neo bài nhưng cảnh vật gánh phần lớn dư âm |
| *Bước qua mùa cô đơn* — Vũ. | MIXED-MODERN | mưa, hàng cây, mùa thu, mây tham gia kéo ký ức trở lại và mang chia xa | nhạc trẻ vẫn dùng externalization, xen chi tiết thân thể/đối thoại |
| *Tháng tư là lời nói dối của em* — Phạm Toàn Thắng | MIXED-CINEMATIC | mùa xuân, gió, hoa, nắng, mây tạo chuyển động từ hiện diện sang mất mát | field mở quy mô cho cốt cá nhân; không xóa nhân vật |
| *Hơn cả yêu* — Khắc Hưng | DIRECT/DECLARATION | người hát ở trung tâm; núi, sông, đất, trời là thang khuếch đại chứ không thành hệ agency | phản-ví-dụ: lời trực tiếp vẫn thành công; không được bắt emotional field cho mọi tình ca |

## Đối chứng lý thuyết

- `Objective correlative` mô tả một tập vật, tình huống hoặc chuỗi sự kiện có quan hệ tích cực với cảm xúc cần gợi, thay vì chỉ mô tả trạng thái nội tâm. Đây gần với cơ chế emotional field nhưng không đồng nghĩa bắt buộc thiên nhiên: https://www.poetryfoundation.org/education/glossary/objective-correlative
- Pat Pattison nhấn mạnh intimacy, imagery và pronoun choice đều định hình tình ca; bài trực tiếp có thể mạnh khi POV và hình ảnh phục vụ cùng tiêu điểm: https://online.berklee.edu/takenote/best-and-worst-romantic-song-lyrics/
- Nghiên cứu corpus indie 30 ca tìm metaphor và personification là hai nhóm trội, củng cố rằng trao agency cho hình tượng là thủ pháp phổ biến nhưng không chứng minh nhân quả với thành công: https://rsucon.rsu.ac.th/2021/paper/2101

## Nguồn lyric/metadata

- *Diễm xưa*: https://www.tcs-home.org/songs/titles/diem-xua
- *Biển nhớ*: https://www.tcs-home.org/ban-be/articles/tcs-nguoi-tinh-cua-cuoc-song-phan-2
- *Nỗi nhớ mùa đông*: https://lyric.tkaraoke.com/15899/noi_nho_mua_dong.html
- *Bước qua mùa cô đơn*: https://lyric.tkaraoke.com/56078/buoc_qua_mua_co_don.html
- *Tháng tư là lời nói dối của em*: https://lyric.tkaraoke.com/48191/thang_tu_la_loi_noi_doi_cua_em.html
- *Hơn cả yêu*: https://lyric.tkaraoke.com/47757/hon_ca_yeu.htm

## Kết luận và scope patch

Evidence hỗ trợ ba lane `DIRECT · MIXED · FIELD-DOMINANT`, không hỗ trợ luật “ca hay phải ngoại hiện”. Earliest failure của incident *Cuộc tình xưa phai dấu* là Tứ/Cốt chọn image-system nhưng mọi động từ cảm xúc lại quay về người kể; hình tượng chỉ làm illustration.

Patch thấp:

1. Cho brief/intent có formulation field-led thay vì bắt `ai nói với ai` cho mọi bài.
2. Chọn trọng tâm biểu đạt direct/mixed/field theo brief và engine.
3. Chỉ route `EMOTIONAL-FIELD` sau rough pass khi cụm động từ nội tâm làm bài hẹp hơn Tứ.
4. Không đếm đại từ, không thay máy móc `người nhớ → mưa nhớ`, không rải cảnh vật.
5. Giữ direct declaration làm negative control trong regression.

Trạng thái: **PROVISIONAL — multi-song corpus calibration; cần fresh holdout + direct-declaration regression**.

## Calibration theo truyền thống ca từ — mẫu live bổ sung

Mẫu user cung cấp sau audit cho thấy phải tách genre/production khỏi lyric tradition. Nhóm bolero–trữ tình tự sự nổi bật ở ngoại hiện bằng thân phận, nghi lễ, chiến tranh, sang ngang và nơi chốn gắn biến cố; environmental field có thể cao hoặc thấp. Nhóm V-pop ballad mainstream nổi bật ở lời trực tiếp, hook lặp và tình huống chia lìa/đoàn tụ; cảnh vật thường làm support, nhưng một nơi chốn-ký ức vẫn có thể gánh cốt.

Kết luận provisional:

1. `Externalization` không phải một biến nhị phân: tối thiểu tách **situational**, **environmental/field** và **communal/cultural**.
2. Bolero/trữ tình không đồng nghĩa field-dominant; thường mạnh ở `DIRECT + SITUATIONAL`.
3. V-pop ballad không đồng nghĩa protagonist-lock; hành động tiễn đưa, hồi ức hoặc đoàn tụ có thể ngoại hiện rất cao dù câu chữ trực tiếp.
4. Title-only không đủ xác nhận production genre. Không dùng ký ức về một bài trùng tên để route generation; giữ genre `UNKNOWN` nếu user/audio/reference chưa cấp.

Calibration chi tiết nằm ở `genre-and-lyric-routing.md`. Trạng thái vẫn **PROVISIONAL** vì mẫu nhỏ, lệch về tình ca và chưa có fresh holdout cho indie, folk/quê hương, rap/R&B, dance-pop và rock; vì vậy bảng chỉ dùng thiết kế audit/eval, chưa được tải vào generation packet hoặc làm runtime gate.

## Regression bổ sung — “Mưa tuyết”

Fresh holdout đầu tiên thất bại theo hướng ngược lại: title thời tiết bị route thẳng sang `FIELD-DOMINANT`, làm trời, mưa, đường và dấu chân liên tiếp chiếm agency; quan hệ tình yêu chỉ trở lại muộn. Bản đối chứng user cung cấp giữ người kể, người vắng mặt, kỷ niệm và lời gọi ở trung tâm, còn mưa/tuyết/băng/nắng làm hoàn cảnh, tương phản và khuếch đại.

Kết luận sửa: image-title trong tình ca mainstream dùng **MIXED prior**; thêm `SCENERY-LOCK` vào diagnostic hai chiều `AGENCY-BALANCE`. Không suy rộng thành quota đại từ/chủ ngữ và không hạ cấp field-dominant ở ca có thi pháp phù hợp.
