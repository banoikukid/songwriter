# Genre, truyền thống ca từ và lane biểu đạt

> **Trạng thái: PROVISIONAL — audit/calibration only. Không tải bảng này vào generation packet hoặc dùng nó để loại Tứ cho tới khi qua holdout + regression theo từng scope.**

## Mục đích

Dùng tài liệu này khi audit hỏi thủ pháp nào thường xuất hiện ở đâu hoặc cần thiết kế corpus/holdout theo thể loại. Trong runtime, chỉ giữ nguyên tắc tách ba trục; không dùng bảng họ thể loại để đoán nghĩa title, cấp material hay chấm fail output.

## Tách ba trục

1. **MUSIC GENRE/PRODUCTION:** ballad, bolero, pop, indie, folk, rock, rap/R&B, dance/EDM, cổ phong/cinematic... Trục này chủ yếu chi phối form, groove, phrase density, range và production space.
2. **LYRIC TRADITION/REGISTER:** mainstream-direct, situational-narrative, poetic-field, communal-rooted, urban-discursive, symbolic-philosophical hoặc hook-driven.
3. **EXPRESSION LANE:** `DIRECT · MIXED · FIELD-DOMINANT`, kèm carrier chính như lời gọi, hành động, hoàn cảnh xã hội, nơi chốn-ký ức, hệ hình tượng, tuyên ngôn hoặc phonetic hook.

Cùng một music genre có thể nhận nhiều tradition. Không suy mood, cốt, ngoại hiện hay chất lượng từ genre một mình. Chỉ có title mà chưa có audio/reference/genre thì ghi `genre=UNKNOWN`; fan-out sense bằng ngôn ngữ và văn hóa trước.

## Prior theo họ thể loại

| Họ thể loại/truyền thống thường gặp | Prior biểu đạt | Carrier ngoại hiện hay gặp | Không được mặc định |
|---|---|---|---|
| Bolero/trữ tình tự sự | `DIRECT + SITUATIONAL` | thân phận, gia đình, cưới hỏi, sang ngang, cách trở, hành động tiễn/chờ, nơi chốn gắn biến cố | rải mưa–trăng–sông thay cho tình thế; mọi bài đều nghèo hoặc phụ duyên |
| V-pop ballad mainstream | `DIRECT → MIXED` | lời thú nhận, chia tay/tỏ tình, hành động quan hệ, một image-title hoặc cảnh nền hỗ trợ hook | cốt phải phức tạp; image-title phải thành extended conceit; mưa/đêm tự đủ cảm xúc |
| Singer-songwriter/tình khúc thi ca | `MIXED → FIELD-DOMINANT` | thời gian, không gian, âm thanh và hệ hình tượng cùng mang chuyển động cảm xúc | nhân hóa tùy ý; chuỗi danh từ đẹp thay cho lực hút liên tưởng |
| Indie/alternative hiện đại | `MIXED-CINEMATIC` | lát cắt ký ức, ellipsis, chi tiết đời thường đã được quan hệ chuyển hóa, thành phố/mùa/ánh sáng | giờ giấc, con hẻm, điện thoại, đồ uống tự tạo chất indie |
| Dân gian, quê hương, folk-rooted | `MIXED/FIELD + COMMUNAL` | tiếng nói, ca dao, phong tục, mùa màng, dòng sông, ký ức và cội nguồn chung | biến quê thành vật thể hoặc co toàn bài về một đôi nhân vật; dùng danh mục biểu tượng vùng miền |
| Cổ phong/cinematic phương Đông | `MIXED/FIELD + SYMBOLIC/PHILOSOPHICAL` | duyên–kiếp, nhân thế, tương phùng, vô thường và hệ biểu tượng có scale arc | xếp trăng–mây–mộng–sơn hà không quan hệ; mở triết lý rồi rơi ngay vào nhật ký đôi lứa |
| Rap/R&B/urban | `DIRECT + NARRATIVE/ATTITUDE` | khẩu khí, đối thoại, hành vi, xung đột, chi tiết xã hội, nhịp và wordplay | thiên nhiên hóa để nghe “thơ”; hy sinh natural speech cho vần |
| Dance-pop/EDM | `DIRECT/HOOK-DOMINANT` | câu gọi, repetition, phonetic/rhythmic hook, production payoff | nhồi liên tưởng hoặc cốt dày vào phrase ngắn; gọi lyric-only là music-fit |
| Rock/anthemic | `DECLARATION` hoặc `NARRATIVE/COMMUNAL` | khẩu khí, xung lực tập thể, đối lập, biểu tượng quy mô lớn, performance lift | từ lớn tự tạo chiều sâu; mọi rock lyric đều phải hùng tráng |

Các hàng là prior khởi động, không phải xác suất đã được chuẩn hóa. Artist voice, era, subgenre, brief và audio có quyền đảo lane. Một ballad có thể field-dominant; một folk song có thể là lời tỏ tình trực tiếp; một ca khúc thi ca có thể thành công bằng declaration.

## Route audit tối thiểu

1. Ghi bằng chứng thật cho music genre: audio/track, metadata/reference được phép dùng hoặc `UNKNOWN`; lyrics-only không tự xác nhận production genre.
2. Mã hóa lyric tradition, engine, expression lane và carrier sau khi có artifact; không dùng nhãn table làm expected answer.
3. So positive/negative control trong cùng `genre × era × register × mood`.
4. Chỉ sau promotion mới viết runtime route riêng; trước đó bảng chỉ sinh hypothesis cho eval, không sinh Tứ/câu.

## Audit theo genre

- Thiết kế corpus theo `genre × era × register × mood`; không gộp mọi “ballad” thành một nhóm.
- Lyrics-only chỉ mã hóa lyric tradition và expression lane; không xác nhận production genre nếu thiếu audio/metadata.
- Có positive lẫn negative control: bài field mạnh và bài direct vẫn thành công trong cùng phạm vi.
- Đếm chức năng: direct statement, situational externalization, environmental field, communal scale, hook repetition và arc behavior; không chỉ đếm danh từ cảnh vật.
- Chỉ promotion prior sau fresh holdout và regression ngoài nhóm đã dùng để rút insight. Không suy rằng thủ pháp gây ra thành công thương mại.
