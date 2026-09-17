---
name: songwriting-min
description: "Sáng tác, sửa và hoàn thiện ca khúc tiếng Việt từ title/lời, Tứ, melody, groove/track, chord/harmony, brief hoặc bản nháp. Quy trình writer-first hội tụ ở central intent → working hook + form + song system → bản thô → nghe/đọc → chẩn đúng triệu chứng → handoff Suno hoặc production. Dùng cho lời bài hát, melody-first, phổ thơ, hook/chorus, audit ca khúc và AI-music; không hứa tự tạo hit hay siêu phẩm."
---

# SONGWRITING-MIN: RETURN TO EMOTIONAL CORE

Sáng tác bằng tai, cảm xúc và mạch. Runtime mặc định phải đủ nhẹ để người viết thực sự viết; các bộ kiểm định kỹ thuật chỉ là công cụ chẩn đoán hậu kỳ khi bản nháp bộc lộ triệu chứng cấn rõ rệt.

## 1. Triết lý sáng tác cốt lõi (Creative North Star)

> **Nguyên tắc cha (Parent Principle):**  
> Cảm xúc trung tâm là đích đến tối thượng của bài hát. Chi tiết, hình ảnh, hành động, kỹ thuật và chẩn đoán chỉ là phương tiện để khơi dậy cảm xúc đó trong lòng người nghe. Nếu một chi tiết không làm cảm xúc sâu hơn hoặc không làm ý nghĩa tiến lên, nó không cần xuất hiện.

### Thang bậc ưu tiên sáng tác (Writer's Priority Hierarchy):
1. **CENTRAL EMOTIONAL TRUTH:** Chân thực cảm xúc trung tâm — điều bài hát muốn người nghe thực sự rung động.
2. **RELATIONSHIP / HUMAN MEANING:** Ý nghĩa mối quan hệ và kết nối giữa người với người.
3. **LYRIC EXPRESSION:** Biểu đạt ca từ giàu nhạc tính, có khả năng đọng lại trong tâm trí.
4. **NATURAL VIETNAMESE:** Tiếng Việt tự nhiên trong thế giới phong cách của bài (`Natural ≠ Ordinary`, `Simple ≠ Flat`, `Poetic ≠ Artificial`, `Direct ≠ Bad`).
5. **SPECIFICITY / IMAGE:** Chuyển hóa cảm xúc (`Detail → Relational Meaning → Emotional Response`). Không thu thập đồ vật vô cảm.
6. **SINGABILITY:** Dễ hát, thuận hơi, nhịp thở ca từ tự nhiên.
7. **RHYME / SONIC POLISH:** Vần điệu và âm thanh kết dính.
8. **TECHNICAL OPTIMIZATION:** Tối ưu hóa kỹ thuật (để sau cùng).

### Hiệu chỉnh quan trọng:
- **Tự nhiên không có nghĩa là tầm thường (Natural ≠ Ordinary):** Ca từ được phép bay bổng, ẩn dụ, trực diện, điệp từ hoặc phóng đại cảm xúc khi giọng điệu của bài đòi hỏi. Không ghìm ca từ xuống thành văn xuôi đời thường tẻ nhạt.
- **Show, Don't Tell không phải tuyệt đối:** SHOW là mặc định tốt, nhưng câu cảm xúc trực diện (DIRECT EMOTIONAL LANGUAGE) hoàn toàn được chào đón khi nó tạo ra cú nổ cảm xúc (payoff), được tích lũy từ trước (earned), và không phải khẩu hiệu sáo mòn.
- **Chống liệt kê đồ vật/hành động (Anti-Object Dumping):** Chuỗi `đồ vật → hành động → đồ vật` (dắt xe, treo mũ, dép lê, chốt cửa, dầu ăn, hành phi...) là rủi ro làm phẳng bài (`SCENE-HEAVY RISK`). Luôn tự hỏi: *"Tại sao người kể lại chú ý chi tiết này vì tình yêu/cảm xúc?"*
- **Chi tiết lãng mạn ≠ Chi tiết gia dụng:** Ưu tiên chi tiết quan hệ riêng tư (câu nói chỉ hai người hiểu, thói quen chung, khoảng lặng có nghĩa, sự thay đổi của bản thân khi ở bên người kia) hơn là đạo cụ sinh hoạt vật lý.
- **Nén cảm xúc ca từ (Emotional Compression):** Ưu tiên 1 hình tượng/hành động đắt gánh trọn vẹn trạng thái lớn hơn là 8 câu diễn giải dông dài.

## 2. Kỷ luật phân tách vai trò (Token & Role Discipline)

- `SKILL.md = Routing + Hiến pháp Runtime + 4 Phanh + Điều kiện dừng` (ngắn gọn, khung điều hướng thường trực).
- `references/*.md = Domain Knowledge + Diagnostic Procedures` (chứa tri thức chuyên sâu; chỉ nạp khi cần).
- Tuyệt đối không nhồi checklist kỹ thuật, ma trận lỗi hay bài test vào generation context của writer.

## 3. Khám phá thích nghi & Cửa vào (Adaptive Discovery)

| Cửa vào (Input) | Lối xử lý (Discovery Route) |
|---|---|
| **Sửa vài câu / Polish** | Sửa trực tiếp tại chỗ theo lane Micro-rewrite; không chạy lại Tứ hay Cốt. |
| **Đề tài / Ý tưởng / Title** | Tìm hạt mầm cảm xúc (Seed) $\rightarrow$ Tứ $\rightarrow$ Cốt; chạy DOMAIN-SENSE nếu title đa nghĩa. |
| **Melody / Demo mộc** | Khóa phrase, biên hơi và âm vực rồi dệt lời theo giai điệu (`references/music-sketch-and-demo.md`). |
| **Groove / Beat / Chords** | Lắng nghe chuyển động nhịp và không gian hòa âm để tìm cảm xúc chủ đạo. |
| **Bản nháp lời có sẵn** | Đọc thành tiếng $\rightarrow$ chẩn ngược Tứ, Cốt và payoff; sửa gốc trước khi sửa chữ. |
| **Bài thơ** | Chuyển hóa nhịp thơ sang nhịp ca từ hát được (`references/poem-to-song.md`). |
| **Packet đã duyệt** | **FROZEN WRITER PACKET:** Giữ nguyên Tứ và form; tập trung 100% vào viết bản thô. |
| **Xuất / Khắc phục Suno** | Đọc `references/suno-production.md` (chuẩn 3-block & ma trận lỗi) + `references/suno-handoff.md`. |

**Hội tụ trước khi viết:** Chốt nhanh 3 yếu tố: (1) **Cảm xúc trung tâm / Tứ**; (2) **Working Hook**; (3) **Section Jobs** (định hướng cảm xúc từng đoạn).

## 4. Quá trình viết bản thô & Nhiệm vụ từng đoạn (Writer-Pass)

Viết trọn vẹn một mạch rough pass từ đầu đến cuối section để giữ đà cảm xúc trước khi soi xét chữ nghĩa vi mô.

### Định hướng nhiệm vụ từng đoạn (Section Jobs):
- **VERSE:** Bộc lộ cách nhân vật trải nghiệm mối quan hệ; không chỉ dựng bối cảnh hay kiểm kê đồ đạc.
- **PRE-CHORUS:** Gia tăng áp lực cảm xúc, tạo đà mong chờ cho sự thật sắp hé mở.
- **CHORUS:** Kết tinh hoặc giải phóng sự thật cảm xúc trung tâm; chứa carrier đáng nhớ nhất; **chống viết thành bài luận** (không liệt kê mệnh đề: *không X, mà Y, nên Z*).
- **VERSE 2:** Đào sâu ý nghĩa cảm xúc, đưa vào thông tin quan hệ mới; tránh lặp lại tâm lý đã nói ở Chorus.
- **BRIDGE:** Tạo bước ngoặt góc nhìn (Perspective Shift), làm sáng tỏ điều chưa thấy; **chống viết thành bài giảng** (ưu tiên: *niềm tin cũ → mâu thuẫn cụ thể → bước ngoặt cảm xúc*, tránh *trước nghĩ X, sau hiểu Y, vậy nên Z*).
- **FINAL CHORUS:** Trở về với ý nghĩa cảm xúc đã biến chuyển sâu sắc hơn; không copy nguyên xi; không cần nhồi thêm chữ (`Final Chorus ≠ More Words`).

### Bốn phanh tối thượng của Writer (Danh sách đóng)
Trong suốt quá trình viết bản thô, Writer chỉ chịu sự kiểm soát của **duy nhất 4 phanh** (Closed List):

1. **Đúng cảm xúc & quan hệ trung tâm:** Bài đang kể điều gì, giữa ai với ai, và để lại dư vị gì trong lòng người nghe?
2. **Tiếng Việt tự nhiên:** Đúng khẩu khí đời thực, đúng ngữ vực (register), không đảo ngữ gượng gạo.
3. **Nghĩa > Vần:** Ý nghĩa, hình tượng và nhịp thở luôn đi trước; vần chỉ là chất keo kết dính, không vì ép vần mà méo câu.
4. **Provenance & Điểm nhìn (POV):** Tôn trọng phạm vi quan sát của nhân vật; không tự bịa quyền biết chắc nội tâm người khác.

> [!IMPORTANT]
> **Hiến pháp bảo vệ ngòi bút:**
> Tất cả các khái niệm còn lại (*Camera Arc, Scale Arc, Detail Budget, Association Carrier, Lexical Naturalness, Phrasing Prosody, Vocal Map, AI-slop Filters*) chỉ là **CÔNG CỤ CHẨN ĐOÁN HẬU KỲ**. Tuyệt đối không được dùng chúng làm rào cản tiền kiểm bắt Writer phải thỏa mãn khi đang viết.

## 5. Sửa nhanh / Chỉnh sửa cục bộ (Micro-Rewrite)

Khi người dùng chỉ yêu cầu sửa 2–4 câu, đổi vần, thay từ hoặc làm mượt một đoạn:
- Tuyệt đối không chạy lại Tứ, Cốt hay quy trình Discovery từ đầu.
- Sửa trực tiếp tại chỗ theo thứ tự ưu tiên: **Tiếng Việt tự nhiên > Sáng nghĩa > Nhịp điệu, điểm rơi và vần**.
- Đưa ra mặc định dòng gốc (Option 0) + tối đa 2 phương án tinh gọn (hoặc lên đến 3 nếu người dùng chủ động yêu cầu).

## 6. Chẩn đoán lỗi & Vá đúng tầng (Diagnostic & Targeted Patching)

Chỉ mở các công cụ chẩn đoán chuyên biệt khi bản nháp đã viết xong và bộc lộ triệu chứng cấn:

```
ARTIFACT → ĐỌC/HÁT THÀNH TIẾNG → XÁC ĐỊNH TRIỆU CHỨNG → TÌM TẦNG LỖI → VÁ ĐÚNG DUY NHẤT TẦNG ĐÓ → DỪNG
```

### Phân tầng xử lý:
1. **Lỗi ở Tứ / Ý niệm cốt lõi:** Lạc đề, sai miền nghĩa brief $\rightarrow$ sửa Tứ tại `references/idea-and-structure.md`.
2. **Lỗi ở Cấu trúc / Section Jobs:** Bài đều đều, thiếu chuyển động cảm xúc, Hook loãng, Bridge luận đề $\rightarrow$ gọt Hook, đổi góc nhìn Bridge.
3. **Lỗi ở Tự nhiên / Cảm xúc (Lyric Voltage):** Liệt kê sự việc vô cảm (`SCENE DENSITY`) hoặc lặp lại cùng một kết luận cảm xúc (`PARAPHRASE DENSITY`) $\rightarrow$ chuyển thành chi tiết quan hệ hoặc nén thành carrier đắt giá (`references/lyric-refinement.md`).
4. **Lỗi ở Ngữ âm / Miệng hát (Prosody & Mouth-feel):** Nuốt chữ, dồn hơi, cấn dấu thanh $\rightarrow$ tinh chỉnh vần, cắt chữ thừa (`references/vietnamese-line-and-sound.md`).
5. **Lỗi ở Engine AI / Render (Suno & Vocal):** 
   - Tuân thủ bất biến: `OBSERVATION (User/Audio) → REPEATABILITY CHECK → LIKELY CAUSE → FAILED LAYER → TARGETED PATCH`.
   - `MODEL_INFERENCE` đơn độc không được quyền tự ý sửa lời khi chưa có bằng chứng audio thực tế.
   - Tham chiếu chi tiết: `references/suno-production.md` và `references/vocal-realization.md`.

*Dừng khi bài hát đã chạm được cảm xúc người nghe hoặc đã giải quyết xong triệu chứng được báo; không polish vô tận.*

## 7. Trạng thái Handoff & UX

- `[LYRIC DRAFT — Scope A chưa qua; music-fit UNKNOWN]`
- `[SUNO PROTOTYPE-READY — Scope A PASS; music-fit UNKNOWN]`
- `[PROSODY PASS — Scope B]` chỉ sau demo có melody và lời
- `[PRODUCTION CANDIDATE]` chỉ sau Scope B, performance và feedback gate

*Lưu ý UX:* Các nhãn trạng thái này mặc định là telemetry/audit nội bộ; trong giao tiếp sáng tác thông thường, trả ca từ tự nhiên mà không chèn nhãn kỹ thuật.

## 8. Điều không thương lượng (Non-negotiables)

- Ví dụ, corpus, bài tham chiếu không được dùng làm seed câu/Tứ hoặc sao chép nguyên văn cấu trúc.
- Không mặc định người viết = người kể = người hát; không bắt buộc trải nghiệm đời tư mới được sáng tác.
- Nghĩa và cảm xúc tự nhiên luôn thắng vần; không gọi bản lời trần là bài hát hoàn chỉnh khi chưa có âm nhạc.
- Kỷ luật bằng chứng âm thanh: Chưa có audio thực tế, chỉ nhận định rủi ro (`RISK / LIKELY / UNVERIFIED`), tuyệt đối không tuyên bố hát hay hoặc điểm rơi hoàn hảo.
- Skill là Pure Agent Skill (100% Markdown & JSON); không gọi lệnh chạy ngầm hay script thực thi.

## 9. Router tài liệu tham chiếu (Reference Router)

| Nhu cầu chuyên sâu | Tài liệu tham chiếu |
|---|---|
| Ý tưởng, Tứ, Cốt, Form, Hook, Chế độ tham vọng | `references/idea-and-structure.md` |
| Giai điệu, hòa âm, groove, demo mộc, feedback | `references/music-sketch-and-demo.md` |
| Tiếng Việt, ngữ âm, vần điệu, dấu thanh, thanh điệu ca từ | `references/vietnamese-line-and-sound.md` |
| Tinh lọc ca từ, nén nghĩa, điểm rơi, subtext, sonic craft | `references/lyric-refinement.md` |
| Định hướng giọng hát (Vocal Realization) & vocal prosody | `references/vocal-realization.md` |
| Suno 3-block production, character budgets & ma trận lỗi | `references/suno-production.md` |
| Reviewer độc lập (Evidence discipline, 6 lenses) | `references/lyric-quality-review.md` |
| Quy trình kiểm định tầng (Stage validation loop) | `references/stage-validation-loop.md` |
| Suno Handoff & thẻ lệnh xuất | `references/suno-handoff.md` |
| Khai phá phong cách âm nhạc (Style Prompt & DNA) | `references/style-mining.md` |
| Phổ thơ sang ca khúc | `references/poem-to-song.md` (+ `references/folk-prosody.md`) |
| Bộ dữ liệu kiểm thử & hồi quy (Eval & Regression Suite) | `references/audit-and-evaluation.md` (Tier 3 - không nạp khi viết) |
