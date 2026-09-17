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

Chạy theo flow khám phá thích nghi; các mục tham chiếu bên dưới mô tả dụng cụ có điều kiện, không phải checklist phải điền:

1. Đánh giá độ mạnh của material và vùng chưa xác định. Hỏi seed đang cần được **giải quyết/biến đổi** hay được **ở trong/vọng lại**; nếu cả hai còn sống và dẫn tới cách viết khác hẳn, giữ hai giả thuyết ngắn tới pilot. Nén một **working central intent** có thể đổi sau khi nghe câu hát, không coi nó là đáp án lyric phải diễn giải.
   Khi user yêu cầu mở ngân hàng nguyên liệu/liên tưởng đa tầng, hoặc chất lượng Tứ phụ thuộc rõ vào việc chọn một carrier cụ thể, chạy **MATERIAL AFFORDANCE AUDITION** tại `references/idea-and-structure.md` trước khi sinh Tứ. Đây là route tuyển ứng viên theo chức năng trong bài, không phải danh sách vật thể “thơ”; lời trực tiếp và phương án không dùng vật thể luôn được quyền thắng.
2. Thử một Tứ sống trực tiếp từ material. Với narrative/declaration, Generate có thể đến từ chuyển tình thế hoặc khuếch đại mệnh đề; với state/constellation, Generate có thể đến từ lần trở lại sâu/rộng/đổi âm hưởng mà không cần cú lật hay kết luận. Chỉ fan-out thêm hai hoặc ba Tứ khi Tứ đầu chưa Generate, hai behavior của seed còn ngang bằng, brief có ambiguity làm đổi miền nghĩa, user yêu cầu lựa chọn hoặc session có evidence lặp gốc. Không fan-out để hoàn thành quy trình.
3. Audition nhanh working hook/title behavior, form và chức năng section ở mức tối thiểu. Form được sinh từ engine, material và constraint nhạc; không mặc định Verse–Pre–Chorus–Bridge.
4. Chọn **pilot ở nơi cần chứng minh nhất**: Chorus/hook cho declaration; Verse mở + turn cho narrative; một chu kỳ Verse–Refrain cho sustain; một quãng liền 8–12 dòng nơi trường ảnh phải cộng hưởng cho constellation; section làm hình tượng biến nghĩa cho image-led; phrase khó nhất cho melody-first. `Verse 1 + Chorus` chỉ là một lựa chọn, không phải mặc định.
5. Đọc/hát pilot như người nghe. Ghi nhận cả lỗi lẫn khám phá mới: được giữ hướng, cập nhật central intent/Tứ, đổi form hoặc Song System, hay reseed. Không chấm pilot theo việc nó có lặp đúng worksheet hay không.
6. Khi hướng đã sống, decompile thành generation packet ngắn và để LLM viết trọn rough lyric bằng năng lực ngôn ngữ tự do. Pilot là bằng chứng, không phải khuôn câu/cadence cho mọi section.
7. Đọc/hát raw lyric; mọi diagnostic mặc định `N/A` tới khi có triệu chứng chỉ được vào artifact cụ thể. Giao đúng một diagnostic owner mỗi lượt; sửa cục bộ hoặc quay đúng tầng gốc rồi chạy rewrite closure.
8. Chỉ sau khi nghĩa và tự nhiên đã ổn mới chạy Scope A và handoff Suno.

Không bắt writer-pass tái hiện worksheet Tứ/Cốt, danh sách trường liên tưởng, camera arc, rhetorical carrier hoặc tên cơ chế. Skill giữ quyền **route, chẩn đoán và release**; LLM giữ quyền chọn câu, cú pháp, độ dài, vần và hình ảnh trong các constraint đã duyệt.

`PRE-WRITER RELEASE` và verdict pilot là trạng thái hậu trường; chỉ hiển thị khi user/web app cần duyệt. Chúng không được trở thành prompt bắt LLM kể lại quá trình kiểm tra trong lyric.

Chỉ mở discovery/gate trước writer-pass khi brief thật sự cần lựa chọn nhiều Tứ, có ambiguity làm đổi miền nghĩa, material chưa Generate, user khóa expression/scale khó, hoặc artifact nhạc tạo constraint bắt buộc. Sự tồn tại của một diagnostic trong skill không phải lý do kích hoạt nó.

### Kỷ luật vận hành chống Overthinking (Operational Discipline)

- **INTERNAL TERM ≠ OUTPUT TERM (Thuật ngữ nội bộ không rò rỉ ra output):** Các khái niệm như *Material Affordance, Central Intent, Tứ, Working Hook, Generation Packet, Scope A/B, Diagnostic Owner, Rewrite Closure, Association Carrier, Scale Continuity, Agency Balance* là ngôn ngữ hậu trường phục vụ định hướng và chẩn đoán. Tuyệt đối không bao giờ để các thuật ngữ này rò rỉ vào bề mặt ca từ hoặc giao tiếp sáng tác thông thường với người dùng.
- **INTERNAL CONCEPTS ARE ROUTING KEYS, NOT REASONING STEPS (Khái niệm nội bộ là khóa định tuyến, không phải bước suy luận bắt buộc):** Một concept sinh ra để giúp agent chọn đúng hướng khi gặp tình huống phức tạp, hoàn toàn không có nghĩa agent phải "chạy qua" hay liệt kê từng concept trong suy luận nội bộ. Khi đề bài đã rõ, đi con đường ngắn nhất đến câu hát.
- **REFERENCE LOADED ≠ REFERENCE ACTIVATED (Nạp tài liệu không đồng nghĩa với kích hoạt):** Việc host agent tải một reference vào context không đồng nghĩa với việc phải áp dụng toàn bộ checklist trong tài liệu đó. Mọi công cụ chẩn đoán mặc định ở trạng thái ngủ (`N/A`), chỉ kích hoạt đúng tầng khi bản nháp bộc lộ đúng triệu chứng.
- **GENERATION CONTEXT POLICY (Chính sách ngữ cảnh tối thiểu):**
  - Tuyệt đối không preload các tệp evaluation (JSON test suites, grader schemas), báo cáo audit lịch sử (`*audit*.md`) vào context sáng tác thông thường.
  - Chỉ truy xuất tập tài liệu tối thiểu phục vụ đúng lane đang kích hoạt:
    - *Lyric-first thông thường:* `SKILL.md` + $1 - 2$ refs (`idea-and-structure.md`, `vietnamese-line-and-sound.md`).
    - *Suno production:* `SKILL.md` + $2 - 3$ refs (`suno-production.md`, `suno-handoff.md`, `vocal-realization.md`).
    - *Failure diagnosis:* `SKILL.md` + đúng ref sở hữu tầng lỗi cần vá.
    - *Audit / Benchmark:* Chỉ mở `audit-and-evaluation.md` và test suites khi có yêu cầu kiểm thử hệ thống.


### Sửa nhanh / Chỉnh sửa cục bộ (Micro-rewrite / Polish)

Khi user chỉ yêu cầu sửa 2–4 câu Chorus/Verse, đổi vần, thay từ, gọt một câu hoặc làm cho câu mượt hơn:
- **Tuyệt đối KHÔNG chạy lại cả quy trình Tứ, Cốt, Form hay Discovery từ đầu.** Không biến yêu cầu sửa nhỏ thành bài kiểm định toàn bài.
- Giữ nguyên bối cảnh, nhân vật và trọng lực cảm xúc hiện có của đoạn.
- Sửa trực tiếp tại chỗ theo thứ tự ưu tiên: **Tiếng Việt tự nhiên > Sáng nghĩa > Nhịp điệu, điểm rơi và vần**.
- Với micro-rewrite, chỉ dùng lens liên quan khi cần: **Naturalness**, **Emotional Temperature**, **Mouth-feel** hoặc **local rhyme/prosody**; không ép chạy đồng loạt.
- Đọc/hát nhẩm để kiểm tra hơi thở và độ ca hóa; đưa ra 2–3 phương án tinh gọn để user chọn.

### Draft nhanh

Khi user yêu cầu demo/test Suno/một lượt:

1. Chốt goal, cảm xúc, voice, genre, constraint nhạc tối thiểu và **expression target** nếu user đã nêu.
2. Chọn seed, Tứ và working hook một vòng.
3. Dựng form + section jobs + music direction và phrase behavior tối thiểu.
4. Viết trọn rough pass, đọc/hát lại, sửa lỗi nghe thấy.
5. Chạy **ROUGH-LYRIC SEMANTIC GATE** tại `references/stage-validation-loop.md`; fail ở tầng nào thì quay đúng tầng đó, chưa chuyển sang sửa âm–vần.
6. Chưa có audio thì chạy **SCOPE-A RELEASE GATE** trước handoff.
7. Chỉ gắn `[SUNO PROTOTYPE-READY — Scope A PASS; music-fit UNKNOWN]` khi semantic gate và Scope A đều PASS; nếu chưa thì dùng `[LYRIC DRAFT — Scope A chưa qua; music-fit UNKNOWN]` và ghi tầng cần sửa.

Khi cần kiểm tra tĩnh lyric, tự rà nhanh:
- dòng dài/ngắn bất thường;
- từ kết dòng lặp sát nhau;
- dòng trùng hoặc gần trùng;
- phrase có dấu hiệu quá tải hơi.
Đây chỉ là diagnostic nhanh; không thay Semantic Gate, đọc/hát thành tiếng hoặc Scope B.

Thiếu genre thì giữ `genre=UNKNOWN` ở tầng DOMAIN-SENSE và lyric routing. Chỉ khi user yêu cầu handoff ngay mới dùng **production assumption** pop/acoustic trung tính; ghi rõ đây là giả định phối thử và không dùng nó để chọn sense, Tứ hoặc truyền thống ca từ.

### Tham vọng phá cách

Chỉ bật khi user gọi rõ “tham vọng”, “phá cách”, “đột phá”, “để đời” hoặc “siêu phẩm”. Giữ nguyên brief, provenance và expression target, rồi fan-out ở cấp **arm card** trước khi viết full lyric: một baseline mạch lạc; một arm khám phá biến đổi một trục sâu; một arm biên kết hợp các biến đổi tương thích để Tứ và song system kể cùng một điều. Trục sâu có thể nằm ở cơ chế Tứ, expression carrier/image route, scale/camera movement, speech act, hook–form, phrase behavior hoặc music frame; đổi genre, POV, đạo cụ hay device đơn lẻ không được tính là phá cách.

Chọn bằng các gate hiện hành trước, độ mới sau. Nếu arm mạo hiểm thua baseline về cảm xúc, tiếng Việt, material necessity hoặc khả năng sống trong nhạc, baseline thắng. Chỉ viết full lyric cho arm đã chọn; giữ baseline để A/B, không trộn mọi ý lạ vào một bài. Không hứa siêu phẩm. Đọc `references/idea-and-structure.md` mục “Chế độ tham vọng phá cách”.

Trước writer-pass, **decompile arm thắng**: giữ tiền đề cảm xúc, quan hệ, section jobs, expression target và constraint phrase/nhạc nghe được; bỏ nhãn arm, tên cơ chế và từ vựng dùng để phân tích phép biến đổi. Cơ chế có thể sống trong form, phrase hoặc production mà không cần được lyric gọi tên.

## Route theo input

| Input | Route |
|---|---|
| Sửa vài câu / Polish cục bộ | Micro-rewrite lane: sửa trực tiếp tại chỗ, không chạy lại Tứ/Cốt/Discovery |
| Đề/ý/title mới | Bước 1–8; TITLE/LYRIC hoặc BRIEF/STORY entry; chạy DOMAIN-SENSE nếu title đa nghĩa |
| Melody/hum/demo | MELODY entry; khóa phrase/range rồi viết theo Scope B |
| Groove/track/chords | GROOVE/TRACK hoặc CHORD/HARMONY entry |
| Bản nháp lời | Chẩn ngược intent, Tứ, Cốt và payoff; sửa gốc trước sửa chữ |
| Bài thơ | Đọc `references/poem-to-song.md`; chỉ mở luật thể thơ tại `references/folk-prosody.md` khi user chủ ý giữ form |
| Chỉ hook/chorus | Chốt brief rút gọn, Tứ và vai section |
| Packet Tứ/Cốt/Song System đã khóa | **FROZEN WRITER PACKET**: không chạy lại discovery hay đổi hướng; viết raw lyric rồi chẩn artifact |
| Audit/tối ưu skill | Đọc `references/audit-and-evaluation.md`; corpus không vào generation |
| Xuất/khắc phục Suno | Đọc `references/suno-handoff.md` |

### Lane FROZEN WRITER PACKET

Khi user, web app hoặc stage trước đã duyệt central intent, Tứ, section jobs, hook và constraint nhạc:

1. Chỉ kiểm packet có mâu thuẫn hoặc thiếu điều kiện khiến không thể viết; nếu không, giữ nguyên.
2. Bỏ nhãn phân tích và dịch section jobs thành việc cảm xúc nghe được; không tái fan-out Tứ, thêm camera arc, kho ảnh hoặc payoff mới.
3. Để LLM viết một rough pass liền mạch.
4. Chạy semantic gate trên chính raw lyric. Ưu tiên hard fail tiếng Việt tự nhiên trước các điểm cộng về thơ, vần hay độ mới; chỉ những dòng có evidence mới mở `NATURALNESS-SWEEP`.
5. Sửa cục bộ, giữ phần còn lại và section contract. Chỉ quay Tứ/Cốt khi lỗi lan nhiều section và truy được về packet.

Lane này ngăn skill làm lại công việc định hướng đã được duyệt. Một packet tốt không được xem là giấy phép giữ câu gượng; writer realization là artifact độc lập.

### Bốn tầng trách nhiệm

- **Song Brain:** bài đang cảm gì và cần nói gì — central intent, Tứ, hook và song system.
- **Emotional Arc:** cảm xúc mở, sâu, đổi, tích lũy hoặc vọng lại như thế nào qua các section.
- **Wordcraft:** câu chữ nghe và cảm ra sao — tự nhiên, chính xác, hình ảnh, mức trực diện, vần và âm sắc.
- **Prosody / Singability:** câu chữ sống trong phrase và melody ra sao — hơi, điểm nhấn nghĩa, âm tiết–nốt, slot ngân, phát âm và groove.

Đây là bản đồ trách nhiệm để chẩn đoán lỗi, không phải bốn pass bắt buộc. Sau rough pass, chỉ mở tầng có triệu chứng rõ:

```
ROUGH LYRIC
     ↓
READ / SING / LISTEN
     ↓
DIAGNOSE
     │
     ├─ concept / central intent sai
     │      → Song Brain
     │
     ├─ section không tiến hoặc cảm xúc đứng yên
     │      → Emotional Arc
     │
     ├─ câu gượng / sáo / sai cường độ / hình ảnh yếu
     │      → Wordcraft
     │
     ├─ khó phát âm / khó lấy hơi / không vừa phrase
     │      → Prosody / Mouth-feel
     │
     └─ không có lỗi rõ
            → KEEP
```

Tuyệt đối không biến bốn nhánh trên thành checklist chạy tuần tự.

### Đường suy luận tối thiểu & Phân tách Writer / Reviewer

- **Minimum Sufficient Reasoning Path (Đường suy luận tối thiểu đủ dùng):** Đi con đường ngắn nhất từ brief/cảm hứng đến câu hát sống động. Không lạm dụng bộ khung lý thuyết để giải thích dài dòng khi đề bài đã rõ. Chỉ mở tài liệu tham chiếu chuyên sâu khi bản nháp bộc lộ triệu chứng cần xử lý.
- **Thứ bậc ưu tiên tối thượng (Semantic & Musical Hierarchy):**
  ```
  Ý nghĩa (Meaning)
     > Tiếng Việt tự nhiên (Natural Vietnamese)
        > Tính ca hát & hơi thở (Singability)
           > Vần (Rhyme)
              > Tối ưu hóa thanh học (Phonetic optimization)
  ```
  *Quy tắc mềm:* Tối ưu hóa thanh học (như kiểm soát âm khép `-p, -t, -c, -ch` hay độ mở nguyên âm) chỉ là hỗ trợ; tuyệt đối không bao giờ được phép bẻ gãy cú pháp tự nhiên hoặc làm méo mó ý nghĩa câu hát chỉ để phục vụ kỹ thuật phát âm.

- **Ma trận kích hoạt năng lực (Capability Activation Matrix):**
  | Capability | Vai trò | Trạng thái Runtime |
  |---|---|---|
  | **Song Brain** | Core | Luôn hoạt động (Always) |
  | **Wordcraft / Prosody** | Core | Khi viết hoặc sửa lyric |
  | **Vietnamese Vocal Realization** | Core Extension | Khi có yêu cầu hát / vocal affordance / demo |
  | **Suno Production Adapter** | External Adapter | Chỉ khi người dùng yêu cầu đóng gói sang Suno |
  | **Failure Diagnosis Matrix** | Diagnostic Sidecar | Chỉ khi có lỗi thực tế quan sát được |
  | **Lyric Quality Review** | Diagnostic Sidecar | Chỉ khi người dùng yêu cầu review độc lập hoặc QA |
  | **Style DNA** | Research | Chỉ khi cần nghiên cứu phong cách âm nhạc |
  | **Music Blueprint** | Production | Chỉ khi dựng phối khí/demo (Dormant khi lyric-first) |

- **Phân tách Writer / Reviewer:**
  - **Writer Pass (Sáng tác):** Viết liền mạch, dấn thân vào nhân vật/tình huống và cảm xúc; tuyệt đối không tự ngắt mạch giữa chừng để làm micro-audit hoặc giải trình thuật ngữ.
  - **Reviewer Pass (Độc lập đánh giá):** Là một **sidecar**, không nằm trên default execution path. Chỉ kích hoạt sau khi đã có bản nháp hoàn chỉnh hoặc khi người dùng yêu cầu review/audit. Phân loại theo 3 cấp độ: `CRITICAL` (lỗi sinh tử: gượng gạo tiếng Việt, sai provenance, hỏng cấu trúc), `SUGGESTED` (cải thiện rõ lực ca từ), `OPTIONAL` (tinh chỉnh sở thích). Luôn trả phản hồi theo cấu trúc: `LOCATION → PROBLEM → WHY → TARGETED FIX` (chi tiết tại `references/lyric-quality-review.md`).

### Điều kiện dừng bắt buộc (Stop Conditions — Chống Overthinking)

Agent phải biết chính xác khi nào dừng và không được tự ý kích hoạt các tầng không cần thiết:

1. **STOP 1 — Không kích hoạt Suno / Music Blueprint khi Lyric-First:** Khi người dùng chỉ yêu cầu sáng tác ca từ (lyric-first), không yêu cầu phối khí, không có file audio/render $\rightarrow$ Giữ `Music Blueprint` và `Suno Adapter` ở trạng thái **Dormant (Ngủ yên)**. Không tự chém BPM, Key, Mode hay dán thẻ Style khi không ai yêu cầu.
2. **STOP 2 — Không viết lại toàn bài khi gặp lỗi cục bộ (Targeted Patch):** Khi lỗi chỉ xảy ra ở 1–2 câu, 1 đoạn, hoặc ở tầng kỹ thuật (phát âm, trôi giọng) $\rightarrow$ Chỉ vá đúng tầng lỗi đó (`Style` hoặc `Lyrics` hoặc `Controls`). Nếu lỗi trên Suno chỉ xuất hiện 1 lần (`Single-output anomaly`), thực hiện **Re-roll** trước khi can thiệp sửa prompt/lyric.
3. **STOP 3 — Dừng tinh chỉnh khi đạt độ chín:** Dừng ngay lập tức khi:
   - Ý đồ cốt lõi (Central Intent) và Tứ đã được truyền tải trọn vẹn và tự nhiên.
   - Các điểm cấn còn lại chỉ thuộc mức `OPTIONAL` (sở thích cá nhân hoặc có thể hát được theo phrasing khác).
   - Việc sửa tiếp có nguy cơ gây lệch nghĩa (*semantic drift*) hoặc làm mất đi tia sáng cảm xúc thô mộc ban đầu.


## Quy trình runtime

### 1. Chốt Goal và Brief

Lấy đủ để viết: mục tiêu sử dụng; người hát/người nghe; chủ đề và quan hệ; material/provenance user đã cấp nếu có; mood/năng lượng; register/thị trường; genre và constraint giọng/range. Không truy nguồn đời tư hoặc mặc định người viết, người kể và người hát là một. Ghi thêm **expression target** khi user nêu rõ hoặc lặp lại một ưu tiên như `DIRECT`, `EXTERNALIZED`, `MIXED` hay `FIELD-DOMINANT`; giữ target đó trong phiên cho đến khi user đổi. Đây là constraint của brief, không phải suy luận từ genre.

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
- Đề mỏng thì để LLM thử nén một Tứ tối giản từ chính khả năng nghĩa của material, không điền ngay một cốt truyện quen. Chỉ fan-out bằng **MOTIF DISCOVERY** tại `references/idea-and-structure.md` khi user yêu cầu nhiều hướng, Tứ đầu không Generate, có blocking ambiguity hoặc rough lyric lộ mô-típ lặp; không chạy chỉ vì user chưa đặt tên Tứ.
- Khi các phương án vẫn chỉ là nhiều cách bình luận cùng một đề, hoặc chất lượng bài phụ thuộc vào một tình thế/hình tượng/trường nghĩa có sức sinh, chạy **ASSOCIATION-ENGINE DISCOVERY** trong cùng reference. Chỉ bỏ qua route này khi lời trực tiếp, tuyên ngôn hoặc tự sự đã đủ lực **và** brief không khóa `EXTERNALIZED/FIELD-DOMINANT` hay yêu cầu liên tưởng gánh bài; negative control không được ghi đè expression target đã giữ trong phiên.
- Khi user muốn tự chọn từ một ngân hàng liên tưởng, hoặc nhiều carrier cụ thể đều có vẻ hợp mood nhưng chưa biết cái nào thật sự sinh được câu/Tứ, chạy **MATERIAL AFFORDANCE AUDITION** trước khi khóa Tứ. Giữ provenance và trạng thái lựa chọn; không biến shortlist thành quota phải dùng hết trong lyric. Nếu user đã khóa một material đời thường, không tự loại vì nó “thô”: tìm đúng chức năng của nó hoặc nêu xung đột thật sự.

### 3. Chốt Central Intent, Tứ và Working Hook

Ở lane mặc định, chỉ cần khóa một central intent, một Tứ có `nguồn lực → chuyển động/lần trở lại → payoff hoặc dư vang` và một working hook. `Generate` không đồng nghĩa phải có quan hệ nhân quả, phát hiện cuối hay câu tổng kết: một state/constellation đủ sống khi mỗi lần trở lại mở thêm chiều cảm xúc, quy mô, âm hưởng hoặc quan hệ. Các closure, image audition, scale arc và association engine bên dưới là route có điều kiện, không phải worksheet phải hoàn thành trước khi LLM được viết.

Trước khi chốt, khai thác các sức căng, khả năng biến nghĩa và chuyển động thật sự có trong seed/material để sinh các giả thuyết mô-típ **khác cơ chế cảm xúc**, rồi bỏ danh từ/đạo cụ để khử các phương án cùng skeleton. Không suy ra chia xa, chờ đợi, đoàn tụ hoặc một tình huống quen chỉ từ dáng người đơn độc, màu buồn hay title hình ảnh. `Đại chúng · tươi · tham vọng` chỉ là nhãn rủi ro sau khi đã có các mô-típ khác gốc; chúng không được tính là độ đa dạng của Tứ. Mô-típ quen vẫn được chọn khi provenance và brief thực sự làm nó tối ưu, không phải vì nó dễ viết.

Khi user yêu cầu một **bộ nhiều Tứ**, trước khi xuất phải chạy closure `REFRAME-COLLAPSE` trong `references/idea-and-structure.md`: nếu từ ba hướng trở lên chỉ có lực nhờ cú phủ định/đảo nghĩa trung tâm, giữ tối đa hai hướng mạnh và reseed phần dư bằng cơ chế khác có căn cứ. Không đếm từ nối; không cấm reframe user yêu cầu và không áp ngưỡng khi user khóa toàn bộ set vào các biến thể reframe.

Không chọn từ các câu pitch một tầng. Với những arm còn sống, phát triển vừa đủ để nghe thấy `nguồn sức căng/kết dính → chuyển động qua các section → lần trở lại/payoff`; thường giữ một hoặc hai arm qua vài vòng thay vì tham lam khóa nhánh đầu tiên. Phương án tốt nhất tương đối vẫn phải bị loại nếu chỉ là một nhận xét kéo dài, không sinh các vai đoạn khác nhau hoặc cần rải hình ảnh thay thế tùy ý để lấp bài. Khi đó reseed thay vì chuyển sang lyric.

Sau đó chọn engine **NARRATIVE/TRANSFORM · DECLARATION/AMPLIFY · STATE/SUSTAIN** và trọng tâm biểu đạt: người hát trực tiếp, hỗn hợp, hoặc một **emotional field** nơi thời gian/không gian/hình tượng cùng mang cảm xúc. Trước khi biến title giàu hình tượng thành luận điểm, audition xem nó đang đòi một câu trả lời/biến nghĩa hay chỉ là neo cảm xúc cần được ngân rộng; đừng cho hướng dễ giải thích thắng hướng cộng hưởng chỉ vì nó dễ tóm tắt. Chỉ chọn field-dominant khi seed, genre hoặc toàn bộ thi pháp thật sự cần thế giới hình tượng gánh bài; không chọn chỉ vì title là danh từ cảnh vật hay vì muốn tránh độc thoại. Nếu brief khóa `EXTERNALIZED`, Tứ phải chỉ ra carrier và chuyển động của carrier ngay từ đầu; không đợi đến bước sửa câu mới rải thêm hình ảnh. Tứ tốt khi có lực cảm xúc, làm material trở nên cần thiết, đúng lời hứa của brief, sinh được nhiều section và sống được trong nhạc dự kiến. Độ mới là tiêu chí chọn giữa các phương án đã có cảm xúc, không phải giấy phép hy sinh độ ấm.

Nếu bài đi bằng liên tưởng, chọn **nguồn kết dính** trước kho ảnh: tình thế, nghịch lý, động từ/lời gọi, hình tượng chịu tải, quan hệ văn hóa, cú pháp hoặc một cơ chế khác thật sự có trong seed. Liên tưởng từ vựng, công năng, giác quan, thành ngữ và biểu tượng quen được phép dùng để fan-out ứng viên, nhưng chưa đủ làm bằng chứng chọn carrier. Trước khi giữ một ứng viên cụ thể, phải đào xuống hành vi, quy luật, chu kỳ, nghịch lý hoặc biến đổi thật của nó; chỉ giữ khi cơ chế ấy có cầu với hạt nhân cảm xúc, sinh được progression/return/payoff và không thể bị thay tùy ý. Cho các miền nghĩa đào sâu, mở rộng, biến nghĩa hoặc vọng lại quanh nguồn đã chọn. Không bắt buộc dựng sơ đồ và không dùng tên các engine đã biết như menu. Hình ảnh quen như trăng, hoa, mùa, sông, quê, tuổi thơ vẫn dùng được nếu quan hệ giữa chúng đang sống và không chép bài tham chiếu.

Khi **material necessity** của Tứ đã chọn thật sự phụ thuộc vào một hình tượng hoặc hệ ảnh, chạy **IMAGE-ROLE AUDITION** rất ngắn trong `references/idea-and-structure.md` trước khi dựng Cốt. Trước hết route hình tượng vào đúng cách tồn tại: `LITERAL/EVENT · EMBLEMATIC · EMOTIONAL-FIELD/CONSTELLATION · HOOK-ONLY`; không dùng phép ánh xạ một-một của nhánh biểu trưng để ép một trường cảm xúc, không đặt quota ảnh. Chỉ giữ ảnh có việc nghe được và dừng khi hình tượng chính đã đủ hoặc lời trực tiếp mạnh hơn.

Chọn **working hook**: lyric/title, phonetic, melodic, rhythmic, instrumental hoặc production. Lyric-only chỉ xác nhận chắc hai loại đầu; hook được phép đổi sau demo.

Khi Tứ hứa một quy mô rộng hơn chuyện riêng—như nhân thế, quê hương, cộng đồng, thời gian, căn tính, duyên–kiếp—khóa **scale arc** tối thiểu cho bài/section: `PERSONAL · MIXED · FIELD · COMMUNAL · PHILOSOPHICAL`. Xác định trước nơi được phép co về lời riêng và nơi phải mở lại. Đây là bản đồ chuyển độ, không phải quota: `ta/người` vẫn được dùng, nhưng một mở đầu rộng không được mặc định rơi ngay thành chuỗi gặp–nhớ–sợ–mất của đôi lứa nếu chưa có cầu chuyển hoặc section job chủ ý. Đọc mục “Giữ quy mô liên tưởng” trong `references/idea-and-structure.md` khi Tứ có scale rộng.

Nếu title có khả năng trùng bài đã tồn tại, coi đó là cảnh báo chống sao chép lời/hook/skeleton, không phải lệnh cấm trường hình ảnh quen hoặc ép bài phải xa cảm xúc gốc.

### 4. Dựng Song System tối thiểu

Chốt Hook + Form + Cốt + music frame. Gán cho mỗi section một việc nghe được: đặt tình thế, mở cảm xúc, tăng lực, đổi góc, trả hook hoặc để dư âm. Với Tứ có scale rộng, ghi luôn section đang giữ, co hay mở quy mô để chuyển động không bị lực hút cá nhân làm lệch. Verse 2 cần đem thêm điều đáng nghe thay vì diễn đạt lại Verse 1; Bridge chỉ tồn tại khi tạo được bước chuyển hoặc độ mở cần thiết; payoff phải được phần trước chuẩn bị.

Khi expression target là `EXTERNALIZED`, hoặc Tứ đã chọn `MIXED/FIELD-DOMINANT` hay hứa một quy mô rộng, nén một **EXTERNALIZATION CONTRACT** trước khi khóa section jobs: carrier nào đang chuyển động; chuyển động nào tự nhiên trong miền ấy; quan hệ người nào giữ nó có cảm xúc; section nào làm nó đổi, mở hoặc trở lại. Chạy deletion-test hai chiều để tránh cả `PROTAGONIST-LOCK` lẫn `SCENERY-LOCK`. Nếu không tìm được carrier tự nhiên, không nhân hóa hoặc rải cảnh để vá: reseed khi target đã khóa; nếu target không khóa thì được hạ về `MIXED/DIRECT`. Chi tiết và gate nằm tại `references/idea-and-structure.md` và `references/stage-validation-loop.md`.

Song System tối thiểu chỉ cần form, section jobs, hook behavior, phrase tendency và music frame đủ để LLM không viết ngược bài. Không thiết kế trước từng dòng, số tiếng, loại hình ảnh, phép tu từ hoặc vần. Chỉ mở camera arc, melody-reuse map hay concept coupling chi tiết khi bài thực sự phụ thuộc vào chúng.

Khi Tứ có một cơ chế trung tâm đủ rõ, audition tối đa một hoặc hai **hệ quả nghe được** của chính cơ chế ấy trong melody, harmony, rhythm, form, vocal hoặc production. Chỉ giữ khi bỏ hệ quả đó làm bài mất một phần nghĩa hoặc cảm giác nhận diện; không gắn một arrangement cinematic/pop quen rồi gọi là concept-coupled. Ngược lại, không bắt mọi chữ trong Tứ phải có một phép minh họa âm nhạc: genre-fit, cảm xúc trực tiếp và hook vẫn thắng một thiết kế thông minh nhưng khó nghe.

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

Sau `PRE-WRITER RELEASE`, viết đủ đầu–cuối trước micro-edit. Nếu route đã yêu cầu pilot, chỉ viết đúng section/quãng đã chọn ở bước 4, chấm nó như một artifact thật rồi mới mở phần còn lại; không dùng một pilot fail làm nguyên liệu để “cố viết cho đủ”. Trong writer-pass chỉ giữ bốn phanh:

1. đúng cảm xúc, quan hệ trung tâm, expression target và scale arc đã chủ ý chọn; khi tự sinh chi tiết cụ thể, ưu tiên material vốn đã mang được quan hệ, dấu vết, cái giá hoặc chuyển động cảm xúc; nếu chi tiết chỉ cấp đạo cụ, thao tác hay âm nền thì dùng lời trực tiếp hoặc chọn material khác thay vì “thơ hóa” nó;
2. tiếng Việt tự nhiên;
3. nghĩa thắng vần;
4. không bịa dữ kiện thật, quan hệ hai chiều, POV hay nội tâm người khác; được sáng tạo cảnh/hình tượng hư cấu từ Tứ nếu không giả làm material user cung cấp, không mâu thuẫn brief và không mượn corpus.

Bốn phanh trên là **danh sách đóng** của writer-pass. Trước khi có rough lyric hoàn chỉnh, không dùng `LYRIC-VOLTAGE`, `AGENCY-BALANCE`, `NATURALNESS-SWEEP`, `ASSOCIATION-CARRIER`, `SURFACE-OVERLAP` hoặc Scope A để veto từ/câu; các diagnostic ấy chỉ được quyền chẩn artifact đã nghe/đọc.

Không yêu cầu LLM trình bày suy luận Tứ/Cốt trong lyric và không thưởng câu vì nó minh họa đúng thuật ngữ của skill. Cho phép writer-pass lệch nhẹ khỏi scaffold khi câu hát tìm được một biểu đạt tự nhiên hơn mà vẫn giữ central intent, section job và payoff; cập nhật scaffold sau nếu khám phá ấy tốt hơn.

Generation packet chỉ mang user material được phép giữ, tiền đề cảm xúc/quan hệ, section jobs, expression target và music constraint nghe được. Với `DIRECT/NARRATIVE/DECLARATION`, central intent được decompile thành điều người hát thật sự muốn nói hoặc làm; với `STATE/SUSTAIN · FIELD/CONSTELLATION`, central intent ở hậu trường và packet chỉ mang **lực cảm xúc · relation anchor · chuyển động/lần trở lại của trường · việc nghe được của section**. Không truyền mệnh đề tổng kết, bảng `ảnh/màu = cảm xúc`, phép ánh xạ một-một hay payoff wording để writer minh họa. Khi `MATERIAL AFFORDANCE AUDITION` đã chạy, chỉ truyền **vai · hành vi tự nhiên · relation anchor** của material đã chọn; bỏ bảng ứng viên, điểm so sánh và mọi micro-phrase thử. Khi EXTERNALIZATION CONTRACT đã kích hoạt, chỉ truyền chuyển động carrier và relation anchor đã decompile vào section job bằng lời tự nhiên; không truyền tên contract, bảng phân bố chủ thể hay kho ảnh. Chỉ thêm session-negative fingerprint khi `SESSION-DECONTAMINATION` đã được kích hoạt bởi dấu hiệu trùng cụ thể; sự tồn tại của bài cũ một mình chưa đủ. Không mang câu minh họa do model tự đặt, nhãn arm, transformation trace, tên cơ chế, phương án sửa cũ hoặc ví dụ diagnostic xuống writer-pass. Nếu một section chỉ viết được bằng cách diễn xuôi hay đối xứng hóa ghi chú brief, quay section job/immediate utterance trước khi tối ưu phrase.

Với Tứ giàu ý niệm hoặc hệ thống nghĩa, chạy một **embodiment bridge** rất ngắn trước writer-pass: giữ kiến trúc nghĩa ở hậu trường, rồi tìm cho từng section một cách để người nghe sống trong nó qua quan hệ, hành động, âm thanh, không gian, cảm giác hoặc lời trực tiếp. Đây không phải quota vật thể và không có tỷ lệ trừu tượng/cụ thể cố định. Chi tiết chỉ ở lại khi chứng minh hoặc làm cảm được Tứ; nếu chỉ trang trí, đặt camera hay biến bài thành danh mục phong cảnh thì bỏ. Một Tứ sâu chưa tự bảo đảm lyric sâu; writer-pass vẫn phải được chấm như artifact riêng.

Khi scene dễ rơi vào thao tác đời thường hoặc đạo cụ thô, dùng **MATERIAL-TO-EMOTION BRIDGE** tại `references/vietnamese-line-and-sound.md`: nén điều vật liệu phải làm người nghe cảm trước khi chọn bề mặt câu. Không gửi một danh sách đạo cụ cho writer và không bắt mọi vật thành ẩn dụ; câu trực tiếp hoặc hành động giản dị vẫn thắng khi nó mang quan hệ rõ hơn.

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
- Chuỗi ảnh rời/thô hoặc phải giảng vì sao ẩn dụ đúng: chạy **ASSOCIATION-CARRIER**.
- Đạo cụ/chi tiết đời thường bị liệt kê quá nhiều làm loãng bài: chạy **DETAIL BUDGET** tại `references/vietnamese-line-and-sound.md`; chỉ giữ vật có chức năng đẩy chuyện, mang quan hệ hoặc tạo payoff.
- Câu đúng nghĩa nhưng giống văn xuôi xuống dòng, nhiều từ nối/giải thích: chạy **PROSE-TO-LYRIC**; nén về một ý chính, đưa từ trọng tâm gần điểm rơi và đảm bảo nói được trong một hơi (One-breath).
- Câu giải thích lại điều hành động/hình ảnh đã nói rõ: chạy **EXPLAINING LINE**; bỏ thesis line nếu action đã đủ.
- Chorus bị loãng bởi các câu kể/giải thích hoàn cảnh: chạy **HOOK DISTILLATION** tại `references/idea-and-structure.md`; cắt bớt các câu giải thích để làm nổi bật câu hook payoff.
- Final Chorus bị dài dòng, nhồi chữ hoặc gượng ép cao trào: tuân thủ **FINAL CHORUS ≠ MORE WORDS**; kết luận bằng biến nghĩa, rút bớt từ hoặc đổi góc nhìn, không nhồi thêm chữ.
- Khi user flag trực tiếp một từ/câu là `thô · cứng · gượng · chưa mềm · không hợp câu/đoạn`, coi đó là evidence kích hoạt **NATURALNESS-SWEEP** local cho `từ · collocation · register · material`; không thay đồng nghĩa ngay. Nếu lỗi nằm ở quan hệ nghĩa/section job/Tứ, chuyển owner sang **ROUGH-LYRIC SEMANTIC GATE**; nếu nằm ở phrase/hơi/cadence, chuyển sang **SCOPE A**. Giữ dòng gốc làm option 0, viết lại tối đa hai phương án trong owner đúng rồi chạy **REWRITE CLOSURE** trên toàn section trước khi trả.
- Body/material/thành ngữ gây cấn: chạy một **NATURALNESS-SWEEP** và chọn đúng một subcase chính. Lượng từ có nghi vấn mới chạy **QUANTITY-PROVENANCE** riêng; không chồng hai sweep trên cùng câu trong một pass.
- Vần, âm tiết, điểm lấy hơi hoặc cuối câu cấn: chạy line/sound pass và phrase-map. Trước khi xuất bản lời, chạy **PRE-RELEASE MOUTH-FEEL SPOT CHECK** trên các line rủi ro cao (hook, line dài nhất, final payoff, sustain slot) để đảm bảo không nuốt chữ hay hụt hơi.
- Nhiều bài trong cùng phiên lặp skeleton/hook grammar: chạy **SESSION-DECONTAMINATION/SURFACE-OVERLAP**; sửa tầng gốc, không thay đồng nghĩa từng chữ.

Các công cụ nằm trong `references/vietnamese-line-and-sound.md`, `references/lyric-refinement.md` và `references/idea-and-structure.md`. Trước mọi handoff Suno lyrics-first, bản lời phải PASS **ROUGH-LYRIC SEMANTIC GATE** trong `references/stage-validation-loop.md`, rồi mới chạy **SCOPE-A RELEASE GATE**: phrase-map cho Chorus/Pre-Chorus và section dùng lại melody; kiểm biên phrase, hơi, mật độ âm tiết, slot nhấn, cadence/vần, từ cuối và terminal-repeat. Chênh âm tiết được phép nếu có phrasing hợp lý.

Sau mỗi diagnostic rewrite, chạy **REWRITE CLOSURE** tại `references/stage-validation-loop.md` trên toàn section; không PASS chỉ vì triệu chứng ban đầu đã biến mất. Chỉ sau semantic non-regression mới chạy lại Scope A hoặc re-demo phần đã sửa. Dừng khi không còn cải thiện rõ hoặc cần tai người; không polish vô hạn.

### Thứ tự ưu tiên xử lý khi có lỗi (Troubleshooting Priority)

Khi phát hiện cấn hoặc artifact có lỗi, xử lý theo thứ tự ưu tiên:
1. **Provenance:** Lời kể có vượt quá phạm vi quan sát/dữ kiện brief cho phép không?
2. **Meaning & Emotional Temperature:** Đúng mức nhiệt cảm xúc không (tránh bi lụy hóa hoặc làm nguội cảm xúc)?
3. **Hook Clarity & Distillation:** Chorus đã có câu hook kết tinh payoff chưa hay đang over-explaining?
4. **Natural Vietnamese:** Collocation tự nhiên, tránh cú pháp đảo gượng gạo?
5. **Prose-to-Lyric:** Đã có lyric behavior và nhịp điệu ca từ chưa (1 ý chính/line, bỏ từ nối thừa)?
6. **Mouth-feel Spot Check & One-Breath Test:** Có bị vấp cụm phụ âm, nuốt chữ, dồn hơi ở các line trọng tâm không?
7. **Local Rhyme & Sound Polish:** Tinh chỉnh vần chân, vần lưng cục bộ.

### LYRIC REFINEMENT — từ bản nháp đúng ý thành ca từ

Rough lyric không mặc định là release-ready. Với full-song hoặc section mới được viết từ đầu, sau khi central meaning đã ổn, thực hiện một lượt refinement ngắn:

**Mục tiêu:**
- Giữ nguyên Tứ, POV và section job; không viết lại concept; không thêm drama; không “làm thơ” toàn bộ bài.
- Chỉ nâng những line còn mang tính báo cáo, giải thích hoặc quá literal.

**Refinement hỏi 5 câu:**
1. Câu này đang hát hay đang giải thích?
2. Có thể nói ít hơn mà cảm nhiều hơn không?
3. Hình ảnh / action có thể mang phần nghĩa này thay cho thesis không?
4. Từ khóa quan trọng có nằm ở điểm rơi tốt không?
5. Line ending có đủ lực và dễ nhớ không?

Chỉ sửa line cần sửa. Không polish đồng đều toàn bài. Micro-rewrite 2–4 câu không cần chạy toàn bộ refinement pass. Chi tiết kỹ thuật tại `references/lyric-refinement.md`.

### LYRIC QUALITY BAR

Trước khi trả full lyrics cuối cùng, tự kiểm ở cấp toàn bài:
- Có section nào chỉ đang kể việc?
- Có section nào chỉ đang giải thích theme?
- Hook có câu thực sự đáng nhớ không?
- Có line nào đúng nghĩa nhưng quá prose?
- Có line nào quá "AI thơ" so với voice còn lại?
- Có đủ khoảng trống cho listener tự hiểu không?
- Có chi tiết nào dư?
- Có từ/cụm nào được giữ chỉ vì vần?

Chỉ rewrite những điểm fail. Không tái viết toàn bài nếu phần lớn đã tốt. Đây là quality bar cho artifact cuối, không phải checklist line-by-line.

### 8. Chọn, Xuất và Học

Trạng thái handoff:
- `[LYRIC DRAFT — Scope A chưa qua; music-fit UNKNOWN]`
- `[SUNO PROTOTYPE-READY — Scope A PASS; music-fit UNKNOWN]`
- `[PROSODY PASS — Scope B]` chỉ sau demo có melody và lời
- `[PRODUCTION CANDIDATE]` chỉ sau Scope B, performance và feedback gate

*Lưu ý UX:* Các nhãn trạng thái này mặc định là telemetry/audit nội bộ; chỉ xuất ra khi user yêu cầu quy trình formal, export file Suno hoặc debug. Trong giao tiếp sáng tác thông thường, trả ca từ tự nhiên mà không chèn nhãn kỹ thuật vào output.

Nếu người dùng yêu cầu xuất sang Suno, kích hoạt **Suno Adapter** (`references/suno-production.md` và `references/suno-handoff.md`).
- **Suno Adapter Output Contract:** Khối định dạng `STYLE PROMPT` – `LYRICS BLOCK` – `CONTROLS / SETTINGS` chỉ là *hợp đồng định dạng xuất ra* (output contract) dành cho Suno, **tuyệt đối không phải mô hình tư duy nội tại** (cognitive model) của người viết. Quá trình sáng tác luôn đi từ: `Tứ → Central Intent → Hook → Image System → Form → Lyric`.
- **Chính sách chẩn đoán lỗi Suno (Suno Failure Diagnosis Runtime Policy):**
  1. **Nguồn quan sát (Observation Source & Confidence):**
     - `USER_REPORT`: Người dùng nghe trực tiếp và báo lỗi cụ thể (Confidence = High).
     - `AUDIO_OBSERVATION`: Phân tích file audio demo thực tế (Confidence = High/Medium).
     - `MODEL_INFERENCE`: Mô hình tự suy đoán rủi ro (Confidence = Low / Provisional Hypothesis). *Tuyệt đối không tự ý patch bài hát chỉ dựa trên suy diễn chủ quan khi chưa có bằng chứng quan sát thực tế!*
  2. **Kiểm tra tính lặp lại (Repeatability Check):**
     - Suno là hệ thống ngẫu nhiên (stochastic). Nếu lỗi chỉ xảy ra 1 lần (`Single-output anomaly`), giải pháp đầu tiên luôn là **Re-roll** (tạo lại lượt mới) với cùng prompt.
     - Chỉ can thiệp chỉnh sửa khi lỗi lặp lại có tính quy luật (`Repeatable pattern`).
  3. **Vá lỗi đúng tầng (Targeted Layer Patching):**
     ```
     OBSERVATION → REPEATABILITY CHECK → FAILED LAYER → MINIMAL PATCH → RE-GENERATE
     ```
     - Lỗi phát âm $\rightarrow$ Vá tầng *Lyrics / Phonetic*.
     - Trôi giọng/đổi giới tính $\rightarrow$ Vá tầng *Style Vocal Identity*.
     - Bẹt năng lượng / thiếu tương phản $\rightarrow$ Vá tầng *Arrangement Cues / Controls*.
     - *Tuyệt đối không rewrite toàn bài hát hay thay đổi Tứ vì lỗi render của engine!*
- **Vocal Realization:** Khi cần chỉ dẫn vocal chi tiết, tham chiếu `references/vocal-realization.md` (phân 3 tầng: Identity, Performance, Production; vocal prosody tiếng Việt) để lập **VOCAL-DIRECTION MAP**; không mặc định công thức rập khuôn. Lưu session fingerprint ngắn hạn (nếu host hỗ trợ session memory theo `references/case-log-protocol.md`) để tránh lặp cơ chế trong cùng phiên; không ghi đè file tĩnh trong skill.

## Điều không thương lượng

- Ví dụ, corpus, bài tham chiếu và session fingerprint không được làm seed câu/Tứ hoặc bị chép lyric/hook/skeleton.
- Không mặc định người viết = người kể = người hát; không yêu cầu trải nghiệm đời tư làm điều kiện để sinh Tứ.
- **PROVENANCE GATE — Lời kể không được biết quá điều brief cho phép:** Không khẳng định như fact nội tâm, ý định, hành vi tương lai hoặc sự kiện tương lai của nhân vật khác nếu brief/scene không cấp quyền biết. Suy đoán, mong ước hoặc khả năng vẫn được phép khi câu đánh dấu rõ đó là suy đoán/mong ước (ví dụ: *"anh mong...", "liệu rằng..."*).
- Nghĩa và tiếng Việt tự nhiên thắng vần; lỗi phrase/sound phải được nghe hoặc đánh dấu đúng scope.
- Không dùng mood/genre làm proxy cho nhau; không ép một cửa vào hay một engine cho mọi bài.
- Không gọi lyric-only là ca khúc hoàn chỉnh hoặc `music-fit PASS` khi chưa có artifact nghe được.
- Không dùng `Suno-ready` trần; phải ghi `PROTOTYPE-READY` hay `PRODUCTION CANDIDATE` và Scope A/B.
- Skill này là Pure Agent Skill (100% Markdown & JSON Knowledge Base), hoàn toàn không chứa mã thực thi runtime, script Python hay dependency bên ngoài; agent không tự động gọi shell execution hay network requests ngầm.

## Router tài liệu

| Nhu cầu | Đọc |
|---|---|
| Brief, cửa vào, Tứ, Hook+Form, Cốt, ambition | `references/idea-and-structure.md` |
| Melody/harmony/groove, rough demo, feedback | `references/music-sketch-and-demo.md` |
| Câu tiếng Việt, material, vần, thanh, Scope A | `references/vietnamese-line-and-sound.md` |
| Tinh lọc ca từ, compression, subtext, điểm rơi, sonic craft | `references/lyric-refinement.md` |
| Vocal realization, 3 tầng vocal & vocal prosody tiếng Việt | `references/vocal-realization.md` |
| Suno 3-block production, character budgets & failure matrix | `references/suno-production.md` |
| Đánh giá chất lượng lời độc lập (Reviewer protocol) | `references/lyric-quality-review.md` |
| Audit/A-B/corpus/release | `references/audit-and-evaluation.md` + `references/stage-validation-loop.md` |
| Suno export và sau-gen (tóm tắt vận hành) | `references/suno-handoff.md` |
| Style prompt & Style DNA | `references/style-mining.md` |
| Audit genre × truyền thống ca từ × lane biểu đạt (PROVISIONAL) | `references/genre-and-lyric-routing.md` |
| Line device/dominant khi audit | `references/dominant-analysis.md` |
| Phổ thơ | `references/poem-to-song.md`; form Việt có chủ ý đọc thêm `references/folk-prosody.md` |

Các audit chuyên biệt nằm trong `references/*audit*.md`; không tải mặc định. Không tải playbook của skill `songwriting` cũ vào generation: mọi claim vận hành về lời, vần, phổ thơ, Style và Suno phải đi qua reference local ở bảng trên.
