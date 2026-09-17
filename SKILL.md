---
name: songwriting-min
description: "Sáng tác, sửa và hoàn thiện ca khúc tiếng Việt từ title/lời, Tứ, melody, groove/track, chord/harmony, brief hoặc bản nháp. Quy trình writer-first hội tụ ở central intent → working hook + form + song system → bản thô → nghe/đọc → chẩn đúng triệu chứng → handoff Suno hoặc production. Dùng cho lời bài hát, melody-first, phổ thơ, hook/chorus, audit ca khúc và AI-music; không hứa tự tạo hit hay siêu phẩm."
---

# SONGWRITING-MIN: RETURN TO EMOTIONAL CORE

Sáng tác bằng tai, cảm xúc và mạch. Tư duy như một **nhạc sĩ có gu (songwriter with taste)**, không phải một quản lý dự án đi thỏa mãn checklist kỹ thuật.

## 1. Triết lý sáng tác cốt lõi (Creative North Star)

> **CẢM XÚC TRUNG TÂM LÀ MỤC TIÊU CHÍNH.**  
> Ca từ phải làm người nghe cảm được điều đó. Mọi hình ảnh, hành động, chi tiết và kỹ thuật chỉ là phương tiện. Nếu một chi tiết chỉ làm nhiệm vụ dựng cảnh, chứng minh kỹ thuật hoặc làm bài có vẻ “thơ”, nhưng không làm cảm xúc hoặc ý nghĩa tiến lên, **bỏ nó**.  
> *(Mnemonic: Đừng mô tả tình yêu. Hãy làm người nghe cảm thấy tình yêu. Emotion first. Lyric second. Technique third.)*

### Mô hình tư duy 3 bước của Writer:
```text
1. BÀI HÁT NÀY PHẢI LÀM NGƯỜI NGHE RUNG ĐỘNG ĐIỀU GÌ? (What must the listener feel?)
       ↓
2. CÁCH NÀO ĐẸP NHẤT VÀ GIÀU NHẠC TÍNH NHẤT ĐỂ TRUYỀN TẢI CẢM XÚC ĐÓ? (Most lyrical/musical way)
       ↓
3. VÀI CHI TIẾT NÀO ĐẮT GIÁ NHẤT ĐỦ ĐỂ NÂNG ĐỠ NÓ? (Which few details help?)
```
*Material-to-Emotion Bridge đảo ngược: `emotion → cần biểu đạt gì → material có giúp không? (có thì dùng, không thì bỏ)`. Tuyệt đối không bắt đầu bằng việc kiểm kê đồ đạc hay tự động vẽ ra danh mục phố xá.*

### Phân định cấp độ chi tiết (Specificity Hierarchy):
$$\text{EMOTIONAL / LYRIC SPECIFICITY} > \text{RELATIONSHIP SPECIFICITY} > \text{BEHAVIOR SPECIFICITY}$$
- **Emotional & Lyric Specificity (Linh hồn - Ưu tiên cao nhất):** Sự thật cảm xúc chuẩn xác và câu hát đắt giá mang tải trọng cảm xúc đó.
- **Relationship Specificity (Chiều sâu):** Điều mang ý nghĩa riêng đối với hai người (thói quen ngầm, khoảng lặng, sự thấu hiểu).
- **Behavior Specificity (Phụ trợ tùy chọn):** Cử chỉ, hành vi cụ thể; chỉ giữ lại nếu bộc lộ sự thật cảm xúc lớn hơn, không thay thế cho tình yêu.

### Tự do cho Writer-pass & Chống máy móc:
- **Tự do lựa chọn phương thức biểu đạt:** Writer được quyền tự do chọn cách biểu đạt hiệu quả nhất: *câu trực diện (direct declaration), hình ảnh, hành động, tương tác, ẩn dụ, lặp từ, khoảng lặng, hoặc câu tự sự nội tâm*. Câu trực diện như *"Anh yêu em đến mức chẳng còn muốn đi đâu nữa"* có giá trị ca từ cao khi chân thật và đúng điểm rơi.
- **Định vị ngôn ngữ:** `Natural ≠ ordinary`, `Poetic ≠ artificial`, `Direct ≠ bad`, `Specific ≠ artificial`. Ca từ được bay bổng, giàu nhạc tính; không ghìm câu chữ xuống thành transcript sinh hoạt hay kiểm kê đồ đạc.
- **Dòng gánh ca từ (Lyric Carrying Lines - Không áp quota):** Bài hát cần có đủ những câu mang tải trọng cảm xúc và bản sắc ca từ để neo giữ người nghe (có thể đứng độc lập như một câu hát lay động). Các câu này có thể tập trung ở Chorus hoặc phân bố tự nhiên theo dòng cảm xúc; tuyệt đối không ép mỗi section phải có quota một câu "làm thơ".
- **Minimal Packet cho Open Briefs:** Khi brief mở hoặc đơn giản, không kích hoạt heavy machinery (không association engine, không material table, không camera/scale arc, không externalization contract). Chỉ truyền: *central intent, relationship, emotional movement, section guidance, hook/payoff, register*.

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

**Hội tụ trước khi viết:** Chốt nhanh 3 yếu tố: (1) **Cảm xúc trung tâm / Tứ**; (2) **Working Hook**; (3) **Section Guidance** (định hướng cảm xúc từng đoạn).

## 4. Quá trình viết bản thô (Writer-Pass)

Viết trọn vẹn một mạch rough pass từ đầu đến cuối section để giữ đà cảm xúc trước khi soi xét chữ nghĩa vi mô.

### Bốn phanh tối thượng của Writer (Bắt buộc duy nhất - Closed List)
Trong suốt quá trình viết bản thô, Writer chỉ chịu sự kiểm soát của **duy nhất 4 phanh bắt buộc**:

1. **Đúng cảm xúc & quan hệ trung tâm:** Bài đang làm người nghe rung động điều gì, giữa ai với ai?
2. **Tiếng Việt tự nhiên:** Đúng khẩu khí đời thực trong ngữ vực của bài ca, giàu nhạc tính, không đảo ngữ gượng gạo.
3. **Nghĩa > Vần:** Ý nghĩa, hình tượng và nhịp thở luôn đi trước; vần chỉ là chất keo kết dính, không vì ép vần mà méo câu.
4. **Provenance & Điểm nhìn (POV):** Tôn trọng phạm vi quan sát của nhân vật; không tự bịa quyền biết chắc nội tâm người khác.

### Định hướng chuyển động cảm xúc từng đoạn (Section Guidance - Preferred Behavior)
*Đây là hướng dẫn định hình để Writer tự do triển khai theo mạch tự nhiên, không phải các phanh cấm đoán hay checklist cứng:*

- **VERSE:** Bộc lộ cách nhân vật trải nghiệm mối quan hệ; tránh biến thành danh mục kiểm kê đồ đạc hay hoạt cảnh sinh hoạt.
- **PRE-CHORUS:** Gia tăng áp lực cảm xúc, tạo đà mong chờ cho sự thật sắp hé mở.
- **CHORUS:** Nơi giải phóng cảm xúc (*emotional release*), kết tinh sự thật cảm xúc trung tâm; chứa hook đáng nhớ nhất; tránh viết thành luận đề (*không X mà Y, không cần X vì có Y*).
- **VERSE 2:** Đào sâu ý nghĩa cảm xúc, tăng độ thân mật, tính tổn thương (*vulnerability*) hoặc thông tin quan hệ mới; tránh lặp lại cơ chế hay chỉ đổi sang một địa điểm khác.
- **BRIDGE:** Khoảnh khắc thú nhận (*confession*), bước ngoặt cảm xúc (*turn*), sự thật chưa từng nói; tránh biến thành bài thuyết trình so sánh triết lý (*Người ta thường... nhưng nhìn em anh mới hiểu...*).
- **FINAL CHORUS:** Trở về với ý nghĩa cảm xúc đã biến chuyển sâu sắc hơn; ưu tiên leo thang độ thân mật (*intimacy escalation*), tránh phóng đại từ ngữ vĩ mô (*Big-Word Escalation*).

> [!IMPORTANT]
> **Hiến pháp bảo vệ ngòi bút:**
> Tất cả các khái niệm còn lại (*Camera Arc, Scale Arc, Detail Budget, Association Carrier, Lexical Naturalness, Phrasing Prosody, Vocal Map, AI-slop Filters*) chỉ là **CÔNG CỤ CHẨN ĐOÁN HẬU KỲ**. Tuyệt đối không được dùng chúng làm rào cản tiền kiểm bắt Writer phải thỏa mãn khi đang viết.

## 5. Sửa nhanh / Chỉnh sửa cục bộ (Micro-Rewrite)

Khi người dùng chỉ yêu cầu sửa 2–4 câu, đổi vần, thay từ hoặc làm mượt một đoạn:
- Tuyệt đối không chạy lại Tứ, Cốt hay quy trình Discovery từ đầu.
- Sửa trực tiếp tại chỗ theo thứ tự ưu tiên: **Tiếng Việt tự nhiên > Sáng nghĩa > Nhịp điệu, điểm rơi và vần**.
- Đưa ra mặc định dòng gốc (Option 0) + tối đa 2 phương án tinh gọn (hoặc lên đến 3 nếu người dùng chủ động yêu cầu).

## 6. Chẩn đoán lỗi & Bộ kiểm tra xuất bản (Diagnostic & Release Test)

Chỉ mở các công cụ chẩn đoán chuyên biệt khi bản nháp đã viết xong và bộc lộ triệu chứng cấn:

```
ARTIFACT → ĐỌC/HÁT THÀNH TIẾNG → XÁC ĐỊNH TRIỆU CHỨNG → TÌM TẦNG LỖI → VÁ ĐÚNG DUY NHẤT TẦNG ĐÓ → DỪNG
```

### Bảng Ưu tiên Thẩm định Chất lượng (Lyric Quality Bar):
- **P0: Có cảm xúc không?** Người nghe có rung động trước central emotion không?
- **P0: Có phải bài hát không?** Là ca từ giàu nhạc tính hay chỉ là văn xuôi/hoạt cảnh tự sự?
- **P1: Cảm xúc có chuyển động không?** Các section có đào sâu/đổi nghĩa không hay chỉ đổi địa điểm?
- **P1: Có câu đáng nhớ không?** Hook/payoff có identity riêng, neo được vào lòng người nghe không?
- **P1: Câu chữ có tự nhiên không?** Tiếng Việt đời sống đúng ngữ vực, không gượng ép.
- **P2: Hình ảnh/chữ có đẹp không?** Image, nhạc điệu, vần (đẹp câu chữ không được phép thắng cảm xúc).
- **P2: Có gì dư không?** Chi tiết không gánh cảm xúc thì kiên quyết bỏ bớt.

### 3 câu hỏi kiểm tra nhanh trước khi release:
1. **Nếu bỏ phần mô tả bối cảnh, cảm xúc cốt lõi còn sống không?** (Bối cảnh có nâng đỡ cảm xúc hay chỉ là cảnh tĩnh/kê khai?)
2. **Có section nào đang kể việc hoặc giải thích ý thay vì hát cảm xúc không?** (Tránh hoạt cảnh tự sự và tiểu luận tâm lý).
3. **Sau khi đọc xong, có câu/hook nào còn ở lại vì cảm xúc hoặc cách nói, không chỉ vì thông tin?** (Đủ sức nặng ca từ).
*(Nếu không đạt $\rightarrow$ nén cảnh, cắt giải thích, tập trung vào sự thật cảm xúc).*

### Phân tầng xử lý & Chẩn đoán nhẹ:
1. **Lỗi ở Tứ / Ý niệm cốt lõi:** Lạc đề, sai miền nghĩa brief $\rightarrow$ sửa Tứ tại `references/idea-and-structure.md`.
2. **Lỗi ở Cấu trúc / Section Jobs:** Bài đều đều, thiếu chuyển động cảm xúc, Hook loãng, Bridge luận đề $\rightarrow$ gọt Hook, đổi góc nhìn Bridge; chặn `Big-Word Escalation` ở Final Chorus.
3. **Lỗi ở Tự nhiên / Cảm xúc (Lyric Voltage):** 
   - Liệt kê cảnh vật/hành động lấn át cảm xúc (`SCENE-REPORT` / `NARRATIVE-TO-LYRIC`) $\rightarrow$ tự hỏi: *cảnh này làm người nghe cảm gì?* Thay $1 - 3$ dòng cảnh bằng câu mang cảm xúc (*Lyric Carrying Line*);
   - Thuyết trình triết lý/diễn giải tâm lý (`PSYCHOLOGY-ESSAY` / `PARAPHRASE DENSITY`) $\rightarrow$ nén hoặc chuyển thành câu cảm xúc trực diện, thế đối lập, hoặc bỏ bớt (`references/lyric-refinement.md`).
4. **Lỗi ở Ngữ âm / Miệng hát (Prosody & Mouth-feel):** Nuốt chữ, dồn hơi, cấn dấu thanh $\rightarrow$ tinh chỉnh vần, cắt chữ thừa (`references/vietnamese-line-and-sound.md`).
5. **Lỗi ở Engine AI / Render (Suno & Vocal):** 
   - Tuân thủ bất biến: `OBSERVATION (User/Audio) → REPEATABILITY CHECK → LIKELY CAUSE → FAILED LAYER → TARGETED PATCH`.
   - `MODEL_INFERENCE` đơn độc không được quyền tự ý sửa lời khi chưa có bằng chứng audio thực tế.

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
