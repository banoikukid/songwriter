---
name: songwriting-min
description: "Sáng tác, sửa và hoàn thiện ca khúc tiếng Việt từ title/lời, Tứ, melody, groove/track, chord/harmony, brief hoặc bản nháp. Quy trình writer-first hội tụ ở central intent → working hook + form + song system → bản thô → nghe/đọc → chẩn đúng triệu chứng → handoff Suno hoặc production. Dùng cho lời bài hát, melody-first, phổ thơ, hook/chorus, audit ca khúc và AI-music; không hứa tự tạo hit hay siêu phẩm."
---

# SONGWRITING-MIN

Sáng tác bằng tai, cảm xúc và mạch. Runtime mặc định phải đủ nhẹ để người viết còn viết; bộ kiểm tra chỉ được gọi khi bản nháp bộc lộ đúng triệu chứng.

## Nguyên tắc

- Không ép một cửa vào: title/lời, melody, groove/track, chord/harmony, brief và cowrite đều hợp lệ.
- Chốt **central intent** để lời, melody, harmony, rhythm và form cùng phục vụ một cảm xúc.
- Chọn đúng **engine phát triển**: kể/chuyển hóa, tuyên ngôn/khuếch đại hoặc trạng thái/duy trì.
- Viết một rough pass liền mạch trước micro-audit; sau đó nghe/đọc rồi mới chẩn bệnh.
- Giữ **nghĩa > vần**, tiếng Việt tự nhiên và provenance của material.
- Hình ảnh quen không phải lỗi; chỉ loại khi sáo, thay thế tùy ý hoặc không còn lực cảm xúc trong bài cụ thể.
- Demo rẻ dùng để kiểm lời–nhạc trước full production. Lyrics-only không tự biết melody và Suno không deterministic.
- Tai người quyết định “chạm”, “tươi” và bản cuối.

## Chọn lane

### Mặc định

Chạy tám bước dưới. Chỉ mở diagnostic chuyên biệt khi rough pass hoặc demo cho thấy triệu chứng tương ứng.

### Draft nhanh

Khi user yêu cầu demo/test Suno/một lượt:

1. Chốt goal, cảm xúc, voice, genre, constraint nhạc tối thiểu và **expression target** nếu user đã nêu.
2. Chọn seed, Tứ và working hook một vòng.
3. Dựng form + section jobs + music direction và phrase behavior tối thiểu.
4. Viết trọn rough pass, đọc/hát lại, sửa lỗi nghe thấy.
5. Chạy **ROUGH-LYRIC SEMANTIC GATE** tại `references/stage-validation-loop.md`; fail ở tầng nào thì quay đúng tầng đó, chưa chuyển sang sửa âm–vần.
6. Chưa có audio thì chạy **SCOPE-A RELEASE GATE** trước handoff.
7. Chỉ gắn `[SUNO PROTOTYPE-READY — Scope A PASS; music-fit UNKNOWN]` khi semantic gate và Scope A đều PASS; nếu chưa thì dùng `[LYRIC DRAFT — Scope A chưa qua; music-fit UNKNOWN]` và ghi tầng cần sửa.

Với test/fragment yêu cầu một sự vật hay hiện tượng **gợi hoặc chuyển hóa thành cảm xúc** mà không gọi thẳng tên cảm xúc, độ ngắn không miễn semantic gate: provenance chỉ khóa carrier được phép dùng, không chứng minh cầu chuyển hóa đã PASS. Chạy **MICRO-BRIDGE AUDITION** tại `references/idea-and-structure.md`, rồi đọc `Tông vật liệu` và `ASSOCIATION-CARRIER` tại `references/vietnamese-line-and-sound.md`; với một bộ mini, một cụm fail thì rewrite cụm ấy, không lấy các cụm còn lại bù điểm.

Khi lyric đã nằm trong file, có thể chạy `scripts/lyric_static_check.py <file>` để báo độ dài dòng, trùng từ cuối liền kề và dòng lặp. Đây chỉ là detector tĩnh; không thay semantic gate, đọc/hát thành tiếng hoặc Scope B.

Thiếu genre thì giữ `genre=UNKNOWN` ở tầng DOMAIN-SENSE và lyric routing. Chỉ khi user yêu cầu handoff ngay mới dùng **production assumption** pop/acoustic trung tính; ghi rõ đây là giả định phối thử và không dùng nó để chọn sense, Tứ hoặc truyền thống ca từ.

### Tham vọng phá cách

Chỉ bật khi user gọi rõ “tham vọng”, “phá cách”, “đột phá”, “để đời” hoặc “siêu phẩm”. Giữ nguyên brief, provenance và expression target, rồi fan-out ở cấp **arm card** trước khi viết full lyric: một baseline mạch lạc; một arm khám phá biến đổi một trục sâu; một arm biên kết hợp các biến đổi tương thích để Tứ và song system kể cùng một điều. Trục sâu có thể nằm ở cơ chế Tứ, expression carrier/image route, scale/camera movement, speech act, hook–form, phrase behavior hoặc music frame; đổi genre, POV, đạo cụ hay device đơn lẻ không được tính là phá cách.

Chọn bằng các gate hiện hành trước, độ mới sau. Nếu arm mạo hiểm thua baseline về cảm xúc, tiếng Việt, material necessity hoặc khả năng sống trong nhạc, baseline thắng. Chỉ viết full lyric cho arm đã chọn; giữ baseline để A/B, không trộn mọi ý lạ vào một bài. Không hứa siêu phẩm. Đọc `references/idea-and-structure.md` mục “Chế độ tham vọng phá cách”.

Trước writer-pass, **decompile arm thắng**: giữ tiền đề cảm xúc, quan hệ, section jobs, expression target và constraint phrase/nhạc nghe được; bỏ nhãn arm, tên cơ chế và từ vựng dùng để phân tích phép biến đổi. Cơ chế có thể sống trong form, phrase hoặc production mà không cần được lyric gọi tên.

## Route theo input

| Input | Route |
|---|---|
| Đề/ý/title mới | Bước 1–8; TITLE/LYRIC hoặc BRIEF/STORY entry; chạy DOMAIN-SENSE nếu title đa nghĩa |
| Melody/hum/demo | MELODY entry; khóa phrase/range rồi viết theo Scope B |
| Groove/track/chords | GROOVE/TRACK hoặc CHORD/HARMONY entry |
| Bản nháp lời | Chẩn ngược intent, Tứ, Cốt và payoff; sửa gốc trước sửa chữ |
| Bài thơ | Đọc `references/poem-to-song.md`; chỉ mở luật thể thơ tại `references/folk-prosody.md` khi user chủ ý giữ form |
| Chỉ hook/chorus | Chốt brief rút gọn, Tứ và vai section |
| Audit/tối ưu skill | Đọc `references/audit-and-evaluation.md`; corpus không vào generation |
| Xuất/khắc phục Suno | Đọc `references/suno-handoff.md` |

## Quy trình runtime

### 1. Chốt Goal và Brief

Lấy đủ để viết: mục tiêu sử dụng; người hát/người nghe; chủ đề và quan hệ; material/provenance user đã cấp nếu có; mood/năng lượng; register/thị trường; genre và constraint giọng/range. Không truy nguồn đời tư hoặc mặc định người viết, người kể và người hát là một. Ghi thêm **expression target** khi user nêu rõ hoặc lặp lại một ưu tiên như `DIRECT`, `EXTERNALIZED`, `MIXED` hay `FIELD-DOMINANT`; giữ target đó trong phiên cho đến khi user đổi. Đây là constraint của brief, không phải suy luận từ genre.

Khi user yêu cầu rõ `sự vật/hiện tượng → gợi hoặc mang cảm xúc` và hạn chế gọi thẳng tên cảm xúc, ghi target `EXTERNALIZED` hoặc `MIXED` theo brief, đồng thời khóa **CARRIER-RENDER**: mặc định `TRANSFIGURED`; chỉ dùng `LITERAL` khi user/genre/provenance cần realist detail, EVENT hay onomatopoeia. Nếu user yêu cầu mềm, mơ, trữ tình hoặc lặp lại phản hồi rằng concrete nghe thô, khóa thêm `MATERIAL-TEXTURE=SOFT-LYRICAL` trong phiên. Đây là yêu cầu biểu đạt trực tiếp của user, không phải suy lane từ image-title. Material user cấp khóa carrier nhưng không khóa phép ánh xạ hay động tác bề mặt.

Câu thoại, đạo cụ hoặc vi cảnh do model tự thêm để giải thích brief chỉ là **semantic note**, không có provenance như material user cấp. Trước generation, bỏ nguyên văn các ví dụ này khỏi packet và chỉ giữ quan hệ/chức năng của chúng; chỉ khóa chữ khi user đã cung cấp hoặc yêu cầu giữ motif ấy. Đọc “Generation-packet hygiene” tại `references/idea-and-structure.md`.

Với `EXTERNALIZED`, chọn carrier thích hợp: **situational** (thân phận, biến cố, hành động, nghi lễ), **environmental/field** (thời gian, không gian, âm thanh, hệ hình tượng) hoặc **communal/cultural** (ký ức chung, tiếng nói, cội nguồn). Nhân vật vẫn có thể là điểm neo, nhưng không để mọi vị ngữ quay về `nhớ–đau–hỏi–trách–muốn bên nhau`. Ngoại hiện không đồng nghĩa nhân hóa cảnh vật, rải mưa–mây–đêm hay bắt buộc `FIELD-DOMINANT`.

Không tự nhập một vấn đề ngoài brief để làm Tứ “mới”. Reference chỉ định target về feel, form, register và production space; không lấy lyric, hook, đạo cụ hay skeleton làm seed.

Không dùng một nhãn thể loại để quyết định luôn cách viết lời. Khi user, audio hoặc reference đã xác nhận genre/tradition, tách ba trục: **MUSIC GENRE/PRODUCTION · LYRIC TRADITION/REGISTER · EXPRESSION LANE**. Genre định form, density và production space; brief, seed, artifact nghe được và giọng nghệ sĩ quyết định cách viết. Chỉ có title thì giữ genre `UNKNOWN`, không đoán thể loại từ nhan đề. `references/genre-and-lyric-routing.md` hiện là calibration **PROVISIONAL**: chỉ đọc khi audit/đối chiếu genre, không tải vào generation packet và không dùng bảng prior để loại Tứ.

Với input chỉ là title hoặc một cụm đa nghĩa, chạy **DOMAIN-SENSE** trước Tứ: tách hai hoặc ba cách hiểu hợp văn hóa ở các quy mô quan hệ khác nhau, rồi chọn bằng toàn cụm từ, register, genre/reference **đã được xác nhận** và brief—không mặc định một từ như `tình`, `nghĩa`, `duyên`, `phận`, `đời` thuộc tình yêu đôi lứa. Nếu các sense còn ngang bằng và làm đổi hẳn người nói–người nghe hoặc quy mô bài, đưa user lựa chọn ngắn trước khi viết toàn bài. Chỉ tự chọn khi user yêu cầu một lượt ngay; lúc đó nêu rõ giả định. Chỉ fan-out Tứ sau khi khóa sense.

Nén intent theo lane phù hợp, không ép mọi bài vào độc thoại nhân vật:

- **Utterance-led:** `Trong [tình thế], [ai] nói với [ai], cảm xúc đi từ [A] đến [B], để người nghe [nhận/cảm điều gì].`
- **Field-led:** `Từ [hạt nhân], cảm xúc lan qua [thời gian/không gian/hệ hình] theo [chuyển động], để người nghe ở trong [trạng thái].`

Với tình ca đại chúng có title là mùa, thời tiết, cảnh vật hoặc biểu tượng, thử **MIXED** như một arm đầu: con người giữ quan hệ/lời gọi, hình tượng khuếch đại và trở lại ở hook. Nếu brief khóa `EXTERNALIZED` hoặc material/reference cho thấy cả một trường hình tượng đang gánh cảm xúc, phải audition thêm arm **FIELD-DOMINANT** thay vì để prior `MIXED` thắng mặc định. Title hình ảnh một mình không quyết định lane.

### 2. Chọn Cửa vào và bắt Seed

Chọn một entry chính: **TITLE/LYRIC · MELODY · GROOVE/TRACK · CHORD/HARMONY · BRIEF/STORY · COWRITE**.

- Có melody/track/chord thì nghe artifact trước và khóa constraint thật sự nghe được.
- Seed mới xuất hiện được ghi ngay bằng chữ, hum/voice memo hoặc sketch; chưa cần sạch.
- Đề mỏng thì fan-out vài seed ngắn từ chính khả năng nghĩa của material, không điền ngay một cốt truyện quen. Khi user chưa khóa Tứ hoặc rough lyric có dấu hiệu lặp mô-típ, chạy **MOTIF DISCOVERY** ở `references/idea-and-structure.md` trước khi chọn bằng lực cảm xúc, khả năng phát triển và music-fit.
- Khi các phương án vẫn chỉ là nhiều cách bình luận cùng một đề, hoặc chất lượng bài phụ thuộc vào một tình thế/hình tượng/trường nghĩa có sức sinh, chạy **CARRIER-SUITABILITY AUDITION → ASSOCIATION-ENGINE DISCOVERY** trong cùng reference. Chọn vật có lực cảm xúc và lyric-texture fit trước khi đào cơ chế; không thưởng một vật thô chỉ vì cụ thể hoặc lạ. Khi user đã khóa sự vật, provenance giữ vật trong scope nhưng chưa chứng minh nó nên xuất hiện trên bề mặt: route sang `SURFACE-READY · REGISTER-SHIFT · BACKSTAGE-ONLY · RESEED` thay vì ép ca hóa. Chỉ bỏ qua khi lời trực tiếp, tuyên ngôn hoặc tự sự đã đủ lực **và** brief không khóa `EXTERNALIZED/FIELD-DOMINANT` hay yêu cầu liên tưởng gánh bài; negative control không được ghi đè expression target đã giữ trong phiên.

### 3. Chốt Central Intent, Tứ và Working Hook

Vận hành Tứ theo vòng thích nghi, không coi phương án đầu là định luật của cả bài:

`DIVERGE → LYRIC-YIELD AUDITION → COMMIT TEMPORARILY → WRITE SECTION → HARVEST STATE → REASSESS/PIVOT → NEXT SECTION → GLOBAL AUDIT`

Fan-out các hướng khác **cơ chế phát triển**, thử mỗi hướng bằng một vi đoạn có khả năng được hát thay vì câu pitch hoặc phần giải thích. Chỉ chốt tạm hướng sinh được nhiều biểu hiện khác nhau, có sức ép cảm xúc và có thể đổi nghĩa qua các section. Sau mỗi section, thu lại điều mới về giọng, trường hình ảnh, quan hệ, phrase behavior và payoff; giữ Tứ nếu section làm nó giàu hơn, chỉnh Cốt nếu chỉ sai việc đoạn, hoặc pivot/reseed nếu lời chỉ còn minh họa luận đề. Các engine liên tưởng là khả năng để khám phá, không phải menu bắt buộc hay khung phải điền.

Trước khi chốt, khai thác các sức căng, khả năng biến nghĩa và chuyển động thật sự có trong seed/material để sinh các giả thuyết mô-típ **khác cơ chế cảm xúc**, rồi bỏ danh từ/đạo cụ để khử các phương án cùng skeleton. Không suy ra chia xa, chờ đợi, đoàn tụ hoặc một tình huống quen chỉ từ dáng người đơn độc, màu buồn hay title hình ảnh. `Đại chúng · tươi · tham vọng` chỉ là nhãn rủi ro sau khi đã có các mô-típ khác gốc; chúng không được tính là độ đa dạng của Tứ. Mô-típ quen vẫn được chọn khi provenance và brief thực sự làm nó tối ưu, không phải vì nó dễ viết.

Khi user yêu cầu một **bộ nhiều Tứ**, trước khi xuất phải chạy closure `REFRAME-COLLAPSE` trong `references/idea-and-structure.md`: nếu từ ba hướng trở lên chỉ có lực nhờ cú phủ định/đảo nghĩa trung tâm, giữ tối đa hai hướng mạnh và reseed phần dư bằng cơ chế khác có căn cứ. Không đếm từ nối; không cấm reframe user yêu cầu và không áp ngưỡng khi user khóa toàn bộ set vào các biến thể reframe.

Không chọn từ các câu pitch một tầng. Với những arm còn sống, phát triển vừa đủ để nghe thấy `nguồn sức căng/kết dính → chuyển động qua các section → lần trở lại/payoff`; thường giữ một hoặc hai arm qua vài vòng thay vì tham lam khóa nhánh đầu tiên. Phương án tốt nhất tương đối vẫn phải bị loại nếu chỉ là một nhận xét kéo dài, không sinh các vai đoạn khác nhau hoặc cần rải hình ảnh thay thế tùy ý để lấp bài. Khi đó reseed thay vì chuyển sang lyric.

Sau đó chọn engine **NARRATIVE/TRANSFORM · DECLARATION/AMPLIFY · STATE/SUSTAIN** và trọng tâm biểu đạt: người hát trực tiếp, hỗn hợp, hoặc một **emotional field** nơi thời gian/không gian/hình tượng cùng mang cảm xúc. Chỉ chọn field-dominant khi seed, genre hoặc toàn bộ thi pháp thật sự cần thế giới hình tượng gánh bài; không chọn chỉ vì title là danh từ cảnh vật hay vì muốn tránh độc thoại. Nếu brief khóa `EXTERNALIZED`, Tứ phải chỉ ra carrier và chuyển động của carrier ngay từ đầu; không đợi đến bước sửa câu mới rải thêm hình ảnh. Tứ tốt khi có lực cảm xúc, làm material trở nên cần thiết, đúng lời hứa của brief, sinh được nhiều section và sống được trong nhạc dự kiến. Độ mới là tiêu chí chọn giữa các phương án đã có cảm xúc, không phải giấy phép hy sinh độ ấm.

Nếu bài đi bằng liên tưởng, chọn **nguồn kết dính** trước kho ảnh: tình thế, nghịch lý, động từ/lời gọi, hình tượng chịu tải, quan hệ văn hóa, cú pháp hoặc một cơ chế khác thật sự có trong seed. Liên tưởng từ vựng, công năng, giác quan, thành ngữ và biểu tượng quen được phép dùng để fan-out ứng viên, nhưng chưa đủ làm bằng chứng chọn carrier. Trước khi giữ một ứng viên cụ thể, phải đào xuống hành vi, quy luật, chu kỳ, nghịch lý hoặc biến đổi thật của nó; chỉ giữ khi cơ chế ấy có cầu với hạt nhân cảm xúc, sinh được progression/return/payoff và không thể bị thay tùy ý. Cho các miền nghĩa đào sâu, mở rộng, biến nghĩa hoặc vọng lại quanh nguồn đã chọn. Không bắt buộc dựng sơ đồ và không dùng tên các engine đã biết như menu. Hình ảnh quen như trăng, hoa, mùa, sông, quê, tuổi thơ vẫn dùng được nếu quan hệ giữa chúng đang sống và không chép bài tham chiếu.

Khi **material necessity** của Tứ đã chọn thật sự phụ thuộc vào một hình tượng hoặc hệ ảnh, chạy **IMAGE-ROLE AUDITION** rất ngắn trong `references/idea-and-structure.md` trước khi dựng Cốt. Trước hết route hình tượng vào đúng cách tồn tại: `LITERAL/EVENT · EMBLEMATIC · EMOTIONAL-FIELD/CONSTELLATION · HOOK-ONLY`; không dùng phép ánh xạ một-một của nhánh biểu trưng để ép một trường cảm xúc, không đặt quota ảnh. Chỉ giữ ảnh có việc nghe được và dừng khi hình tượng chính đã đủ hoặc lời trực tiếp mạnh hơn.

Chọn **working hook**: lyric/title, phonetic, melodic, rhythmic, instrumental hoặc production. Lyric-only chỉ xác nhận chắc hai loại đầu; hook được phép đổi sau demo.

Khi Tứ hứa một quy mô rộng hơn chuyện riêng—như nhân thế, quê hương, cộng đồng, thời gian, căn tính, duyên–kiếp—khóa **scale arc** tối thiểu cho bài/section: `PERSONAL · MIXED · FIELD · COMMUNAL · PHILOSOPHICAL`. Xác định trước nơi được phép co về lời riêng và nơi phải mở lại. Đây là bản đồ chuyển độ, không phải quota: `ta/người` vẫn được dùng, nhưng một mở đầu rộng không được mặc định rơi ngay thành chuỗi gặp–nhớ–sợ–mất của đôi lứa nếu chưa có cầu chuyển hoặc section job chủ ý. Đọc mục “Giữ quy mô liên tưởng” trong `references/idea-and-structure.md` khi Tứ có scale rộng.

Nếu title có khả năng trùng bài đã tồn tại, coi đó là cảnh báo chống sao chép lời/hook/skeleton, không phải lệnh cấm trường hình ảnh quen hoặc ép bài phải xa cảm xúc gốc.

### 4. Dựng Song System tối thiểu

Chốt Hook + Form + Cốt + music frame. Gán cho mỗi section một việc nghe được: đặt tình thế, mở cảm xúc, tăng lực, đổi góc, trả hook hoặc để dư âm. Với Tứ có scale rộng, ghi luôn section đang giữ, co hay mở quy mô để chuyển động không bị lực hút cá nhân làm lệch. Verse 2 cần đem thêm điều đáng nghe thay vì diễn đạt lại Verse 1; Bridge chỉ tồn tại khi tạo được bước chuyển hoặc độ mở cần thiết; payoff phải được phần trước chuẩn bị.

Chọn **phrase behavior** trước khi sinh câu: cân/điệp để bắt lại, ngắn–dài hội thoại, nén rồi mở, call–response hoặc một hình khác phù hợp groove và section job. Với các section tương ứng, khóa một **melody-reuse policy**:

- `REUSE`: giữ số phrase, biên phrase, điểm lấy hơi và slot nhấn tương thích; không bắt bằng số tiếng tuyệt đối.
- `VARIATION`: giữ anchor/cadence nhận ra được nhưng cho phép một chỗ co, kéo hoặc đổi pickup có chủ ý.
- `NEW BEHAVIOR`: đổi nhịp phát ngôn khi section job thật sự đổi và music frame có chỗ đỡ.

Không chọn lưới số tiếng làm mặc định. Đây là thiết kế phrase cho lyric; Suno vẫn có thể không tái dùng melody cho tới khi nghe render.

Với section cần co/mở quy mô, nén thêm một **camera arc** cho cụm hai đến bốn câu, chẳng hạn `PHILOSOPHICAL → FIELD → MIXED → PERSONAL`. Chỉ định câu nào giữ độ rộng, câu nào làm bản lề và câu nào được phép thu vào quan hệ riêng. Dùng chuỗi trung gian `section job → scale role → immediate utterance/ý phát ngôn → phrase → từ`; không để nhãn Tứ/Cốt sinh thẳng bề mặt câu chữ.

`Immediate utterance/ý phát ngôn` là điều section cần làm người nghe cảm thấy ngay, không đồng nghĩa lời thoại hay động từ `nói–gọi–hỏi`. Nó có thể sống bằng một khẳng định, thế đối, chuyển động hình tượng, nhịp cú pháp hoặc khoảng trống phù hợp lane.

Không bắt buộc điền `pressure · cost · speech act · withheld core` cho từng section. Chúng chỉ là câu hỏi chẩn đoán khi bản nháp lạnh hoặc giống bản phân tích tâm lý.

Chạy kiểm tra sơ bộ: intent, độ căng/thả của form, phrase density, register, range và production feel không đánh nhau. Đọc `references/idea-and-structure.md`; với ca khúc đầy đủ đọc thêm `references/music-sketch-and-demo.md`.

### 5. Viết Rough Pass

Viết theo thứ tự section của Cốt nhưng giữ đà tới hết một section trước micro-edit. Sau mỗi section, ghi **harvest state** rất ngắn: điều vừa xuất hiện có lực, điều không được lặp, thay đổi về scale/voice/phrase và tiền đề thật sự hữu ích cho section kế. Packet của section sau nhận section jobs cùng harvest state, không nhận câu minh họa, trace phân tích hay một công thức cú pháp. Khi các section đã nối được bằng movement/payoff, hoàn tất rough pass đầu–cuối rồi mới audit vi mô. Trong writer-pass chỉ giữ bốn phanh:

1. đúng cảm xúc, quan hệ trung tâm, expression target và scale arc đã chủ ý chọn;
2. tiếng Việt tự nhiên;
3. nghĩa thắng vần;
4. không bịa dữ kiện thật, quan hệ hai chiều, POV hay nội tâm người khác; được sáng tạo cảnh/hình tượng hư cấu từ Tứ nếu không giả làm material user cung cấp, không mâu thuẫn brief và không mượn corpus.

Bốn phanh trên là **danh sách đóng** của writer-pass. Trước khi có rough lyric hoàn chỉnh, không dùng `LYRIC-VOLTAGE`, `AGENCY-BALANCE`, `NATURALNESS-SWEEP`, `ASSOCIATION-CARRIER`, `SURFACE-OVERLAP` hoặc Scope A để veto từ/câu; các diagnostic ấy chỉ được quyền chẩn artifact đã nghe/đọc.

Generation packet chỉ mang user material được phép giữ, central intent, tiền đề cảm xúc/quan hệ, section jobs, expression target và music constraint nghe được. Chỉ thêm session-negative fingerprint khi `SESSION-DECONTAMINATION` đã được kích hoạt bởi dấu hiệu trùng cụ thể; sự tồn tại của bài cũ một mình chưa đủ. Không mang câu minh họa do model tự đặt, nhãn arm, transformation trace, tên cơ chế, phương án sửa cũ hoặc ví dụ diagnostic xuống writer-pass. Nếu một section chỉ viết được bằng cách diễn xuôi hay đối xứng hóa ghi chú brief, quay section job/immediate utterance trước khi tối ưu phrase.

Khi đã khóa camera arc, giữ cùng quy mô trong một câu hoặc một cặp câu cho tới bản lề đã chọn. Hai vế cùng khái quát phải làm nghĩa tiến bằng quan hệ, chuyển động hoặc hệ quả; không ghép hai mệnh đề rộng chỉ để tạo một chân lý chung chung. Chỉ co/mở ngay giữa câu khi từ nối, cú pháp hoặc hình tượng làm người nghe nhận ra chuyển độ.

Đừng tự động mở Verse bằng giờ–địa điểm–hành động. Cảnh cụ thể chỉ ở lại khi mang ký ức, quan hệ, biểu tượng, áp lực hoặc âm sắc cần thiết. Cũng không né sự cụ thể một cách máy móc: vật bình thường có thể rất hay nếu đã được cảm xúc chuyển hóa.

Cho phép câu trực tiếp, câu đơn và hình ảnh quen. Không ép mỗi dòng phải có kỹ thuật, độ mới hoặc một “cú”. Mỗi đoạn chỉ cần một hay hai điểm nâng; phần còn lại có thể làm nhịp cầu.

### 6. Đọc/Hát và tạo Demo thô

Đọc thành tiếng hoặc hát theo phrase dự kiến. Với ca khúc đầy đủ, tạo artifact rẻ nhất đủ nghe lời + melody + tonal center: voice memo, piano/guitar-vocal, MIDI/loop hoặc Suno prototype.

Nghe central intent, natural speech/stress tiếng Việt, breath/range, hook recall, section contrast và payoff. Chưa có audio chỉ được kết luận Scope A; không gọi `PROSODY PASS` hay `music-fit PASS`.

### 7. Chẩn đúng triệu chứng rồi Rewrite

Sửa theo tầng: **Tứ/Cốt → section/form → melody/prosody → line/sound → arrangement**. Không dùng sửa từ để cứu Tứ hoặc melody yếu.

Khi nhiều rule cùng flag, xử theo thứ tự: **DOMAIN/PROVENANCE/REFERENT → CENTRAL INTENT/TỨ/CỐT → NATURAL VIETNAMESE/EMOTIONAL CREDIBILITY → LANE/IMAGE/GENRE PRIOR → SOUND/SURFACE**. Rule tầng thấp không được phá tầng cao. Chọn một diagnostic owner cho một pass, rewrite rồi đọc lại trước khi mở diagnostic kế tiếp; nếu bản mới chỉ chuyển từ `PROTAGONIST-LOCK` sang `SCENERY-LOCK` hoặc ngược lại, hoàn nguyên và sửa quan hệ/scale ở tầng cao hơn.

Chỉ bật công cụ tương ứng:

- Bài viết trôi chảy nhưng đang trả lời một nghĩa khác của title/brief: chạy **DOMAIN-SENSE**, quay về Bước 1 và reseed; không polish câu trên miền nghĩa sai.
- Bài giống lời khuyên, bản tóm tắt, phân tích tâm lý hoặc báo cáo `chủ thể → hành động → kết quả`: chạy **LYRIC-VOLTAGE**; hỏi “đây là người đang hát từ trong cảm xúc hay người đứng ngoài thông báo?” rồi đổi speech act bằng lời gọi/hỏi, thế đối, nhịp, khoảng lặng hoặc chuyển động biểu tượng. Cụm đối xứng kiểu `A nói/làm X → một carrier trang trí → B cũng nói/làm X` cũng thuộc pass này khi không có xung đột, hồi đáp hay hệ quả mới. Ở Hook/Chorus/Bridge/Outro, một câu đinh phẳng hoặc chỉ diễn giải ghi chú Tứ/Cốt cũng đủ bật subcase **ANALYSIS-LEAKAGE**; quay section job/immediate utterance, không thay đồng nghĩa hoặc máy móc xóa chủ ngữ.
- Bài co sai quy mô trong một cụm hoặc qua nhiều section: chạy **SCALE-CONTINUITY** tại `references/stage-validation-loop.md`, tìm đúng scale role/bản lề làm nghĩa sụp và sửa ý phát ngôn trước khi sửa từ. Chỉ sau khi scale PASS mới mở **AGENCY-BALANCE** nếu cụm vẫn bị khóa trong chủ thể người hoặc cảnh vật; không đếm đại từ hay đổi máy móc `anh nhớ ↔ mưa nhớ`.
- Chuỗi ảnh rời/thô, phải giảng vì sao ẩn dụ đúng, hoặc một câu chỉ diễn lại hành vi vật lý của carrier để câu kề gánh toàn bộ cảm xúc: chạy **ASSOCIATION-CARRIER**. Không flag hành vi literal có provenance, EVENT, groove/onomatopoeia hoặc section job riêng.
- Khi user flag trực tiếp một từ/câu là `thô · cứng · gượng · chưa mềm · không hợp câu/đoạn`, coi đó là evidence kích hoạt **NATURALNESS-SWEEP** local cho `từ · collocation · register · material`; không thay đồng nghĩa ngay. Nếu lỗi nằm ở quan hệ nghĩa/section job/Tứ, chuyển owner sang **ROUGH-LYRIC SEMANTIC GATE**; nếu nằm ở phrase/hơi/cadence, chuyển sang **SCOPE A**. Giữ dòng gốc làm option 0, viết lại tối đa hai phương án trong owner đúng rồi chạy **REWRITE CLOSURE** trên toàn section trước khi trả.
- Body/material/thành ngữ gây cấn: chạy một **NATURALNESS-SWEEP** và chọn đúng một subcase chính. Lượng từ có nghi vấn mới chạy **QUANTITY-PROVENANCE** riêng; không chồng hai sweep trên cùng câu trong một pass.
- Vần, âm tiết, điểm lấy hơi hoặc cuối câu cấn: chạy line/sound pass và phrase-map. Khi sửa scale trên lyric đã có melody/audio tốt, giữ phrase length, điểm ngắt, slot nhấn và chất âm cuối như constraint; chỉ đổi chúng khi câu mới không thể tự nhiên hoặc cần nghe lại Scope B.
- Nhiều bài trong cùng phiên lặp skeleton/hook grammar: chạy **SESSION-DECONTAMINATION/SURFACE-OVERLAP**; sửa tầng gốc, không thay đồng nghĩa từng chữ.

Các công cụ nằm trong `references/vietnamese-line-and-sound.md` và `references/idea-and-structure.md`. Trước mọi handoff Suno lyrics-first, bản lời phải PASS **ROUGH-LYRIC SEMANTIC GATE** trong `references/stage-validation-loop.md`, rồi mới chạy **SCOPE-A RELEASE GATE**: phrase-map cho Chorus/Pre-Chorus và section dùng lại melody; kiểm biên phrase, hơi, mật độ âm tiết, slot nhấn, cadence/vần, từ cuối và terminal-repeat. Chênh âm tiết được phép nếu có phrasing hợp lý.

Sau mỗi diagnostic rewrite, chạy **REWRITE CLOSURE** tại `references/stage-validation-loop.md` trên toàn section; không PASS chỉ vì triệu chứng ban đầu đã biến mất. Chỉ sau semantic non-regression mới chạy lại Scope A hoặc re-demo phần đã sửa. Dừng khi không còn cải thiện rõ hoặc cần tai người; không polish vô hạn.

### 8. Chọn, Xuất và Học

Trạng thái handoff:

- `[LYRIC DRAFT — Scope A chưa qua; music-fit UNKNOWN]`
- `[SUNO PROTOTYPE-READY — Scope A PASS; music-fit UNKNOWN]`
- `[PROSODY PASS — Scope B]` chỉ sau demo có melody và lời
- `[PRODUCTION CANDIDATE]` chỉ sau Scope B, performance và feedback gate

Nếu dùng Suno, đọc `references/suno-handoff.md`; render đầu là prototype, nghe–sửa–re-render. Append `references/case-log.md` bằng fingerprint ngắn; chỉ ghi diagnostic chi tiết khi fail, không biến case-log thành kho seed.

## Điều không thương lượng

- Ví dụ, corpus, bài tham chiếu và case-log không được làm seed câu/Tứ hoặc bị chép lyric/hook/skeleton.
- Không mặc định người viết = người kể = người hát; không yêu cầu trải nghiệm đời tư làm điều kiện để sinh Tứ.
- Không tự bịa material, quan hệ hai chiều hoặc nội tâm người khác từ một hành động một phía.
- Nghĩa và tiếng Việt tự nhiên thắng vần; lỗi phrase/sound phải được nghe hoặc đánh dấu đúng scope.
- Không dùng mood/genre làm proxy cho nhau; không ép một cửa vào hay một engine cho mọi bài.
- Không gọi lyric-only là ca khúc hoàn chỉnh hoặc `music-fit PASS` khi chưa có artifact nghe được.
- Không dùng `Suno-ready` trần; phải ghi `PROTOTYPE-READY` hay `PRODUCTION CANDIDATE` và Scope A/B.
- Không thêm rule runtime từ một ca lỗi. Khi rule tích tụ làm bài lạnh, ưu tiên xóa, hạ cấp hoặc định tuyến lại trước khi thêm gate.

## Router tài liệu

| Nhu cầu | Đọc |
|---|---|
| Brief, cửa vào, Tứ, Hook+Form, Cốt, ambition | `references/idea-and-structure.md` |
| Melody/harmony/groove, rough demo, feedback | `references/music-sketch-and-demo.md` |
| Câu tiếng Việt, material, vần, thanh, Scope A | `references/vietnamese-line-and-sound.md` |
| Audit/A-B/corpus/release | `references/audit-and-evaluation.md` + `references/stage-validation-loop.md` |
| Suno export và sau-gen | `references/suno-handoff.md` |
| Style prompt | `references/style-mining.md` |
| Audit genre × truyền thống ca từ × lane biểu đạt (PROVISIONAL) | `references/genre-and-lyric-routing.md` |
| Line device/dominant khi audit | `references/dominant-analysis.md` |
| Phổ thơ | `references/poem-to-song.md`; form Việt có chủ ý đọc thêm `references/folk-prosody.md` |

Các audit chuyên biệt nằm trong `references/*audit*.md`; không tải mặc định. Không tải playbook của skill `songwriting` cũ vào generation: mọi claim vận hành về lời, vần, phổ thơ, Style và Suno phải đi qua reference local ở bảng trên.
