# Đối chiếu quy trình sáng tác ca khúc từ nguồn chuyên môn — 2026-07-18

## Mục tiêu và giới hạn

Đối chiếu runtime `songwriting-min` với quy trình được mô tả bởi trường đào tạo, hiệp hội nghề nghiệp, tạp chí chuyên ngành và nhạc sĩ Việt Nam. Đây không phải một công thức tạo hit. Nguồn được dùng để tìm phần giao nhau, các cửa vào khác nhau và gate nghề nghiệp; không dùng tác phẩm hay câu chữ làm seed sáng tác.

## Nguồn chính

1. [Berklee Online — Prosody in Music and Songwriting](https://online.berklee.edu/takenote/prosody-in-music-and-songwriting/): Pat Pattison đặt central intent và prosody làm nguyên tắc liên kết lời, melody, harmony, melodic rhythm và harmonic rhythm.
2. [Berklee Online — Writing From the Title](https://online.berklee.edu/courses/lyric-writing-writing-from-the-title): title-first là một đường chuyên nghiệp; title tạo nền cho các section phát triển.
3. [Berklee Online — Writing Lyrics to Music](https://online.berklee.edu/courses/lyric-writing-writing-lyrics-to-music): melody-first cần khớp word stress, rhythm, phrasing, rhyme placement và melodic pattern.
4. [Berklee Online — Writing and Analyzing Hit Songs](https://online.berklee.edu/courses/writing-and-analyzing-hit-songs): có thể bắt đầu từ lyric concept, melody, groove/hook hoặc chord set; hook có thể là lyric, melodic, rhythmic, instrumental hay production; dùng critical feedback và nhiều revision.
5. [American Songwriter — Foundations](https://americansongwriter.com/foundations-songwriting-course/): workflow đào tạo đi qua idea, lyric, melody, harmony, structure/arrangement, development/editing rồi demo; feedback xuất hiện trong quá trình.
6. [Songwriting Magazine — Principles of Modern Songwriting](https://www.songwritingmagazine.co.uk/tips/principles-of-modern-songwriting): form, lyric, melody, harmony và rhythm cùng tạo bài; “writing is re-writing”; form mẫu không phải đường duy nhất.
7. [NSAI — Song Evaluations](https://www.nashvillesongwriters.com/nsai-song-evaluations): ưu tiên guitar-vocal/piano-vocal sạch trước full-band demo, lấy nhiều ý kiến và không đầu tư full demo cho mọi bài.
8. [Thanh Niên — Đời sống ca khúc Việt](https://thanhnien.vn/doi-song-ca-khuc-viet-lat-cat-2005-185180042.htm): nhạc sĩ Đức Trí và Lê Quang nhấn mạnh cấu trúc gọn, giai điệu đẹp, ca từ gần gũi, dễ nhớ và dễ ngân nga với ca khúc phổ thông.
9. [Tuổi Trẻ — Người sáng tác dân ca](https://tuoitre.vn/nguoi-sang-tac-dan-ca-523593.htm): nhạc sĩ Cao Văn Lý nói tới nghiên cứu “gen” thể loại, sự chân tình và việc hình dung câu hát có thể được quần chúng hát chung.

## Quy trình giao nhau giữa các nguồn

Không có thứ tự duy nhất. Quy trình hợp lý là một vòng hội tụ:

1. **Goal/brief:** mục tiêu bài, người thể hiện/nghe, genre, hoàn cảnh sử dụng và cảm xúc trung tâm.
2. **Entry seed:** vào từ title/lyric, melody, groove/track, chord/harmony, brief/story hoặc co-write.
3. **Central intent:** nén điều bài muốn truyền và trạng thái ổn định/bất ổn cần biểu đạt.
4. **Song system:** chọn hook, form, arc lời, melodic contour, rhythm/groove, harmony và section contrast để cùng phục vụ intent.
5. **Rough pass:** tạo bản bài đủ đầu-cuối; giữ đà writer trước micro-edit.
6. **Cheap demo:** voice memo, hum, guitar-vocal, piano-vocal hoặc prototype render đủ nghe lời–melody–harmony.
7. **Prosody + rewrite:** kiểm lời, melody, harmony và rhythm có cùng biểu đạt intent; đổi qua lại writer/editor và sửa nhiều vòng có mục tiêu.
8. **Feedback:** nói rõ mục tiêu bài, lấy nhiều ý kiến độc lập; coi triệu chứng lặp lại là tín hiệu, không tự động nhận mọi giải pháp.
9. **Selection/production:** chỉ đưa bài đủ cạnh tranh sang full demo/production; render xong tiếp tục feedback nếu cần.

## Ma trận với skill trước audit

| Tầng nghề nghiệp | Trạng thái cũ | Chẩn đoán |
|---|---|---|
| Goal/brief | Có chủ đề, mood, register, genre | **PARTIAL:** thiếu mục tiêu sử dụng, performer/range và tiêu chí feedback |
| Nhiều cửa vào | Đề mới mặc định idea-first; melody chỉ là input ngoại lệ | **FAIL:** biến một đường tốt thành trình tự chung |
| Central intent | Tứ, TỨ-FIT, hook | **PASS lyric-side** |
| Song system | Hook+Form+Cốt; melody coi là tầng riêng | **PARTIAL:** thiếu melody/harmony/rhythm/production hook và stability map |
| Prosody | Có Scope A/B nhưng chủ yếu ở bước biên tập | **PARTIAL:** đúng khái niệm nhưng vào quá muộn |
| Rough pass | Viết hết bản nháp rồi audit | **PASS có điều kiện:** tốt cho giữ đà; không nên cấm section-loop khi melody bắn lỗi |
| Cheap demo | Chỉ có handoff Suno ở cuối | **FAIL:** thiếu demo thô trước polish/full production |
| Rewrite | Hai tầng, tối đa hai vòng | **PARTIAL:** giới hạn vòng hữu ích cho runtime nhưng quá cứng khi lỗi lyric–music còn tồn tại |
| Feedback | Tai người gate cuối; verdict case-log | **PARTIAL:** thiếu goal-specific critique và nhiều ý kiến trước full demo |
| Selection/full demo | Mọi bài có thể đi thẳng Suno | **FAIL:** chưa tách prototype, rough demo và production candidate |

## Thay đổi được phép

- Giữ idea-first như một entry mode, không làm universal order.
- Thêm router `TITLE/LYRIC · MELODY · GROOVE/TRACK · CHORD/HARMONY · BRIEF/STORY · COWRITE`.
- Đổi Hook thành **working hook** cho tới khi rough demo xác nhận lyric–music fit.
- Thêm Song System Card và prosody map ở trước rough pass.
- Thêm rough-demo gate trước polish/full production; Suno lần đầu có thể là prototype, không tự động là final.
- Cho writer/editor luân phiên theo pass hoặc section sau khi đã có material đủ; không micro-audit mỗi dòng trong lúc nảy seed.
- Thêm feedback theo mục tiêu và production-selection gate.

## Tier bằng chứng

- Nhiều cửa vào, prosody đa tầng, rough demo, rewrite và feedback: **VALIDATED AS PROCESS PRIOR** qua nhiều nguồn độc lập.
- Cách ánh xạ cụ thể sang runtime AI/Suno: **PROVISIONAL**, cần forward-test và verdict tai người.
- Không có nguồn nào chứng minh một pipeline cố định tạo hit hoặc siêu phẩm.
