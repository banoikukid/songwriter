---
name: songwriting-min
description: "Sáng tác, sửa và hoàn thiện ca khúc tiếng Việt từ title/lời, Tứ, melody, groove/track, chord/harmony, brief hoặc bản nháp. Quy trình writer-first hội tụ ở central intent → working hook + form + song system → bản thô → nghe/đọc → chẩn đúng triệu chứng → handoff Suno hoặc production. Dùng cho lời bài hát, melody-first, phổ thơ, hook/chorus, audit ca khúc và AI-music; không hứa tự tạo hit hay siêu phẩm."
---

# SONGWRITING-MIN: RETURN TO ROOTS

Sáng tác bằng tai, cảm xúc và mạch. Runtime mặc định phải đủ nhẹ để người viết thực sự viết; các bộ kiểm định kỹ thuật chỉ được kích hoạt khi bản nháp bộc lộ triệu chứng cấn rõ rệt.

## 1. Triết lý sáng tác cốt lõi (Creative North Star)

- **Cảm xúc trung tâm là mục tiêu tối thượng:** Bài hát tồn tại để truyền tải một rung động, một tâm sự hoặc một sự thật cảm xúc có thật giữa người với người.
- **Viết điều người nghe cần cảm, không chỉ điều họ cần biết:** Ca từ không phải bản tóm tắt tâm lý, báo cáo sinh hoạt hay biên bản liệt kê hiện trường.
- **Mọi chi tiết, hình ảnh và kỹ thuật chỉ là phương tiện:** Nếu một chi tiết không làm cảm xúc sâu hơn hoặc không làm ý nghĩa tiến lên, hãy kiên quyết bỏ nó.
- **Vật bình thường có thể rất hay nếu đã được cảm xúc chuyển hóa:** Đừng sa đà vào việc kiểm tra chi tiết có "earned" hay "realistic" không; câu hỏi quan trọng hơn là: *Chi tiết này có làm tình cảm hiện lên không?*
- **Không ép mỗi dòng phải có kỹ thuật, độ mới hay một "cú":** Cho phép câu trực tiếp, câu đơn và hình ảnh đời thường. Mỗi section chỉ cần một hoặc hai điểm nâng; phần còn lại là nhịp cầu tự nhiên nâng đỡ cảm xúc.
- **Đừng tự động mở Verse bằng giờ–địa điểm–hành động:** Cảnh cụ thể chỉ ở lại khi mang ký ức, quan hệ, biểu tượng hoặc âm sắc cần thiết.
- **Final Chorus ≠ More Words:** Kết bài bằng biến chuyển ý nghĩa, chiều sâu lắng đọng hoặc đổi góc nhìn; không nhồi thêm chữ.

## 2. Kỷ luật phân tách vai trò (Token & Role Discipline)

- `SKILL.md = Routing + Hiến pháp Runtime + 4 Phanh + Điều kiện dừng` (ngắn gọn, giữ vai trò khung điều hướng thường trực).
- `references/*.md = Domain Knowledge + Diagnostic Procedures` (chứa tri thức chuyên môn sâu; chỉ nạp theo nhu cầu cụ thể).
- Tuyệt đối không nhồi checklist kỹ thuật, ma trận lỗi hay bài test vào generation context của writer.

## 3. Khám phá thích nghi & Cửa vào (Adaptive Discovery)

Nhận diện linh hoạt mọi điểm xuất phát, không ép một khuôn mẫu cứng nhắc:

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

**Hội tụ trước khi viết:** Chốt nhanh 3 yếu tố: (1) **Cảm xúc trung tâm / Tứ**; (2) **Working Hook**; (3) **Section Jobs** (nhiệm vụ cảm xúc của từng đoạn: mở đầu, đẩy tới, cao trào, lắng đọng) cùng **Phrase behavior** phù hợp groove.

## 4. Quá trình viết bản thô (Writer-Pass)

Viết trọn vẹn một mạch rough pass từ đầu đến cuối section để giữ đà cảm xúc trước khi soi xét chữ nghĩa vi mô.

### Bốn phanh tối thượng của Writer (Danh sách đóng)
Trong suốt quá trình viết bản thô, Writer chỉ chịu sự kiểm soát của **duy nhất 4 phanh sau đây** (Closed List):

1. **Đúng cảm xúc & quan hệ trung tâm:** Bài đang kể câu chuyện gì, giữa ai với ai, và để lại dư vị gì trong lòng người nghe?
2. **Tiếng Việt tự nhiên:** Dùng ngôn từ mà người Việt thực sự cất lên thành lời, đúng khẩu khí đời thực, đúng ngữ vực (register), không đảo ngữ gượng gạo.
3. **Nghĩa > Vần:** Ý nghĩa, hình tượng và nhịp thở luôn đi trước; vần chỉ là chất keo kết dính, tuyệt đối không vì ép vần mà làm méo mó câu hát.
4. **Provenance & Điểm nhìn (POV):** Tôn trọng phạm vi quan sát của nhân vật; không tự bịa quyền biết chắc nội tâm, suy nghĩ hay hành động tương lai của người khác nếu chưa được chứng kiến.

> [!IMPORTANT]
> **Hiến pháp bảo vệ ngòi bút:**
> Tất cả các khái niệm còn lại (*Camera Arc, Scale Arc, Detail Budget, Association Carrier, Lexical Naturalness, Phrasing Prosody, Vocal Map, AI-slop Filters*) chỉ là **CÔNG CỤ CHẨN ĐOÁN HẬU KỲ**. Tuyệt đối không được dùng chúng làm rào cản hay checklist tiền kiểm bắt Writer phải thỏa mãn khi đang viết.

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
2. **Lỗi ở Cấu trúc / Section Jobs:** Bài đều đều, thiếu chuyển động cảm xúc, Hook bị loãng $\rightarrow$ gọt Hook, tái định vị vai trò đoạn.
3. **Lỗi ở Tự nhiên / Cảm xúc (Lyric Voltage):** Câu khô như văn xuôi, nói lý lẽ thay vì cất lời hát $\rightarrow$ chuyển thành hành động, hình ảnh hoặc thế đối lập (`references/lyric-refinement.md`).
4. **Lỗi ở Ngữ âm / Miệng hát (Prosody & Mouth-feel):** Nuốt chữ, dồn hơi, cấn dấu thanh $\rightarrow$ tinh chỉnh vần chân/lưng, cắt chữ thừa (`references/vietnamese-line-and-sound.md`).
5. **Lỗi ở Engine AI / Render (Suno & Vocal):** 
   - Tuân thủ bất biến: `OBSERVATION (User/Audio) → REPEATABILITY CHECK → LIKELY CAUSE → FAILED LAYER → TARGETED PATCH`.
   - Heuristic âm học hay `MODEL_INFERENCE` đơn độc không được quyền tự ý sửa lời khi chưa có bằng chứng audio thực tế.
   - Tham chiếu chi tiết: `references/suno-production.md` và `references/vocal-realization.md`.

*Dừng khi bài hát đã chạm được cảm xúc người nghe hoặc đã giải quyết xong triệu chứng được báo; không polish vô tận.*

## 7. Trạng thái Handoff & UX

- `[LYRIC DRAFT — Scope A chưa qua; music-fit UNKNOWN]`
- `[SUNO PROTOTYPE-READY — Scope A PASS; music-fit UNKNOWN]`
- `[PROSODY PASS — Scope B]` chỉ sau demo có melody và lời
- `[PRODUCTION CANDIDATE]` chỉ sau Scope B, performance và feedback gate

*Lưu ý UX:* Các nhãn trạng thái này mặc định là telemetry/audit nội bộ; chỉ xuất ra khi người dùng yêu cầu quy trình formal hoặc export Suno. Trong giao tiếp sáng tác thông thường, trả ca từ tự nhiên mà không chèn nhãn kỹ thuật.

## 8. Điều không thương lượng (Non-negotiables)

- Ví dụ, corpus, bài tham chiếu không được dùng làm seed câu/Tứ hoặc sao chép nguyên văn cấu trúc.
- Không mặc định người viết = người kể = người hát; không bắt buộc trải nghiệm đời tư mới được sáng tác.
- Nghĩa và cảm xúc tự nhiên luôn thắng vần; không gọi bản lời trần là bài hát hoàn chỉnh khi chưa có âm nhạc.
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
