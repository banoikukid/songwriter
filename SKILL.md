---
name: songwriting-min
description: "Sáng tác, sửa và hoàn thiện ca khúc tiếng Việt từ title/lời, Tứ, melody, groove/track, chord/harmony, brief hoặc bản nháp. Kiến trúc Vietnamese-first music intelligence hiểu sâu style DNA, corpus profile, singability và spoken-form/prosody nhưng giữ Writer tự do tối đa; quy trình writer-first hội tụ ở central intent → working hook + form → bản thô → chẩn đúng triệu chứng → handoff Suno hoặc production. Không hứa tự tạo hit hay siêu phẩm."
---

# SONGWRITING-MIN: VIETNAMESE-FIRST MUSIC INTELLIGENCE (v1.4.0)

Sáng tác bằng tai, cảm xúc và mạch. Tư duy như một **nhạc sĩ có gu (songwriter with taste)**, không phải một quản lý dự án đi thỏa mãn checklist kỹ thuật. Ca từ tiếng Việt phải tự nhiên, hát được, chạm đến sự thật tâm hồn và có bản sắc âm nhạc riêng.

## 1. Triết lý sáng tác cốt lõi (Creative North Star)

> **"STRUCTURE SERVES THE EMOTION, NOT THE OTHER WAY AROUND."**  
> Cấu trúc phục vụ cảm xúc, không phải cảm xúc phục vụ cấu trúc. Mọi quy tắc (*Show don't tell, contrast, rhyme, form*) chỉ là **chỉ dẫn (guidelines, not rules)**. Ca từ phải làm người nghe cảm được sự thật tâm hồn của nhân vật. Nếu một chi tiết, kỹ thuật hay hình ảnh chỉ làm bài có vẻ “thơ” nhưng không làm cảm xúc tiến lên: **bỏ nó**.  
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
- **Tự do lựa chọn phương thức biểu đạt (Hermes & regiellis):** Writer được quyền tự do chọn cách biểu đạt hiệu quả nhất: *câu trực diện (direct declaration), hình ảnh, hành động, tương tác, ẩn dụ, lặp từ, khoảng lặng, hoặc câu tự sự nội tâm*. Câu trực diện như *"Anh yêu em đến mức chẳng còn muốn đi đâu nữa"* có giá trị ca từ cao khi chân thật và đúng điểm rơi. Không cố ép câu trực tiếp thành ẩn dụ gượng gạo.
- **Song, Not Prose (NuNaught):** Viết để hát chứ không chỉ để đọc. Ưu tiên nhịp thở tự nhiên (singable phrasing), dấu thanh ăn khớp ngữ điệu (natural stress), ngắt dòng có chủ ý. Vần là chất keo hỗ trợ, không phải chiếc lồng giam câu chữ.
- **1–3 Human Details (Guidance, không áp quota):** Mỗi bài có thể có 1–3 chi tiết người thật nhớ được (cử chỉ, thói quen, cách gọi riêng). Không ép mỗi Verse phải có đồ vật; không biến việc chọn chi tiết thành worksheet. Chi tiết chỉ tồn tại nếu giúp người nghe cảm sâu hơn điều bài hát đang nói.
- **Dòng gánh ca từ (Lyric Carrying Lines - Không áp quota):** Bài hát cần có đủ những câu mang tải trọng cảm xúc và bản sắc ca từ để neo giữ người nghe (có thể đứng độc lập như một câu hát lay động). Các câu này có thể tập trung ở Chorus hoặc phân bố tự nhiên theo dòng cảm xúc; tuyệt đối không ép mỗi section phải có quota một câu "làm thơ".
- **Minimal Packet cho Open Briefs:** Khi brief mở hoặc đơn giản, không kích hoạt heavy machinery (không association engine, không material table, không camera/scale arc, không externalization contract). Chỉ truyền: *central intent, relationship, emotional movement, section guidance, hook/payoff, register*.

## 2. Kiến trúc Vietnamese-First Music Intelligence & Kỷ luật phân tách vai trò

```text
                    USER BRIEF
                        │
                        ▼
                CENTRAL EMOTION (Tối cao, không thể bị ghi đè)
                        │
                        ▼
                    TỨ + HOOK
                        │
                        ▼
                 VIETNAMESE WRITER ◄─── [Vietnamese Style DNA & Corpus Profile (Background)]
                        │
                        ▼
                    ROUGH LYRIC
                        │
             ┌──────────┼──────────┐
             ▼          ▼          ▼
         LANGUAGE     LYRIC     MUSIC-FIT / PROSODY
          REVIEW      REVIEW     REVIEW (Spoken Form Diagnostics)
             │          │          │
             └──────────┼──────────┘
                        ▼
                  TARGETED PATCH
                        │
                        ▼
                    FINAL LYRIC
```

- **Tầng Cảm Xúc Trung Tâm (Central Authority):** Cảm xúc trung tâm và Tứ luôn giữ quyền tối cao; không một lớp kiến thức hay kỹ thuật nào được phép ghi đè.
- **Tầng Tri Thức Nền Tảng (Background Knowledge):** `Vietnamese Style DNA` và `Vietnamese Corpus Profile` định vị không gian âm nhạc và kiểm tra độ hợp lý (sanity check); tuyệt đối không biến thành công thức viết lời hay bộ chỉ tiêu cứng.
- **Tầng Chẩn Đoán Hậu Kỳ (Diagnostic Knowledge):** `Spoken Form` và `Prosody Review` hoạt động như công cụ tham vấn sau khi bản thô hoàn thành; không tự động viết lại (rewrite mặc định) câu chữ của tác giả khi chưa có nguy cơ phát âm thực tế.
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
| **Xuất / Khắc phục Suno** | Mặc định đọc `references/suno-production.md` (Primary Owner: chuẩn 3-block, ma trận lỗi & character budgets). Không tự động nạp cùng sidecar; chỉ đọc `references/suno-handoff.md` khi thực sự cần compatibility / quick-handoff. |

### Điều hướng ngữ cảnh âm nhạc Việt (Vietnamese Context Routing):
- **Open / Simple Brief ("Viết một ca khúc...", miền nghĩa rõ, không vật liệu ràng buộc):** SKILL.md tự thân sở hữu quy trình sáng tác tinh gọn (Fast Path). **TUYỆT ĐỐI KHÔNG NẠP** `references/idea-and-structure.md` mặc định. Đi thẳng: `Emotion → Relationship → 1 Tứ khả thi → Working Hook → Section Guidance → Writer`. Chỉ leo thang nạp `idea-and-structure.md` khi xuất hiện blocking ambiguity ở title/miền nghĩa, brief gieo vật liệu nặng (seeded/material-heavy), người dùng yêu cầu nhiều Tứ/kiến trúc ẩn dụ sâu, hoặc có triệu chứng gãy cấu trúc rõ rệt sau bản nháp.
- **Genre / Lane đã xác định (Ballad, Bolero, Indie, R&B...):** Tùy chọn nạp `references/vietnamese-style-dna.md` làm nền tảng định vị soundscape và nhả chữ; Writer vẫn hoàn toàn tự do sáng tác.
- **Brief chỉ nói chung chung ("Viết nhạc Việt"):** Không auto chọn V-Pop. Đối chiếu cảm xúc/ngữ vực để chọn lane phù hợp (trưởng thành $\rightarrow$ Ballad/Acoustic; trẻ trung $\rightarrow$ V-Pop/R&B; hoài niệm $\rightarrow$ Bolero/Trữ tình).
- **Ca từ có số, tiếng Anh, viết tắt hoặc cần hát chuẩn AI:** Nạp `references/vietnamese-spoken-form.md` để chẩn đoán rủi ro phát âm mà không làm bẩn bản hiển thị.
- **Cần nghiên cứu phân bố thời lượng, mật độ từ (WPM) hoặc benchmark:** Nạp `references/vietnamese-corpus-profile.md`.

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
*Đây là hướng dẫn định hình theo regiellis & Hermes để Writer tự do triển khai, không phải các phanh cấm đoán hay checklist cứng:*

- **VERSE:** Đưa người nghe bước vào thế giới cảm xúc và hoàn cảnh quan hệ (*concrete situation/relationship*); chỉ giữ chi tiết nếu nó giúp cảm xúc vận động, tránh kiểm kê ngoại cảnh.
- **PRE-CHORUS:** Gia tăng áp lực cảm xúc (*pressure/lift*), tạo đà mong chờ cho sự thật sắp hé mở (không bắt buộc bài nào cũng phải có).
- **CHORUS:** Nơi giải phóng cảm xúc (*emotional release*), kết tinh **sự thật cảm xúc giản dị và sâu sắc nhất (simplest emotional truth)**; chứa hook mang danh tính cảm xúc (*emotional identity*); tránh viết thành luận đề (*không X mà Y, không cần X vì có Y*).
- **VERSE 2:** Đào sâu ý nghĩa cảm xúc, tăng độ thân mật, tính tổn thương (*vulnerability*) hoặc góc nhìn mới; tránh lặp lại cơ chế hay chỉ đổi sang một địa điểm khác.
- **BRIDGE:** Khoảnh khắc thú nhận (*confession*), góc nhìn mới (*new angle*), mâu thuẫn cảm xúc (*contradiction*) hoặc bước ngoặt cảm xúc (*turn*); tránh biến thành bài thuyết trình so sánh triết lý (*Người ta thường... nhưng nhìn em anh mới hiểu...*).
- **FINAL CHORUS:** Trở về hook với ý nghĩa hoặc trạng thái cảm xúc đã biến chuyển sâu sắc hơn (*return to hook with changed meaning / deeper emotional state*); ưu tiên leo thang độ thân mật (*intimacy escalation*), tránh phóng đại từ ngữ vĩ mô (*Big-Word Escalation*).

> [!IMPORTANT]
> **Hiến pháp bảo vệ ngòi bút & Phân định thẩm quyền (Authority Boundaries):**
> - **4 phanh tối thượng trên là nguồn duy nhất có quyền phủ quyết (single canonical veto list) trong Writer-pass.** Các tài liệu tham chiếu có thể giải thích công cụ chẩn đoán hạ nguồn, nhưng **tuyệt đối không được định nghĩa lại, mở rộng hay thay thế** 4 phanh này.
> - **Chủ sở hữu chuẩn (Canonical Ownership):**
>   - **`LANGUAGE / SOUND`** $\rightarrow$ `references/vietnamese-line-and-sound.md`
>   - **`REFINE`** $\rightarrow$ `references/lyric-refinement.md`
>   - **`REVIEW`** $\rightarrow$ `references/lyric-quality-review.md`
> - Tất cả các khái niệm còn lại (*Camera Arc, Scale Arc, Detail Budget, Association Carrier, Lexical Naturalness, Phrasing Prosody, Vocal Map, AI-slop Filters*) chỉ là **CÔNG CỤ CHẨN ĐOÁN HẬU KỲ**. Tuyệt đối không được dùng chúng làm rào cản tiền kiểm bắt Writer phải thỏa mãn khi đang viết.

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
- **P0: Cảm xúc có sống không?** Người nghe có rung động trước central emotion không?
- **P0: Có phải bài hát (lyric/song) không, hay là văn xuôi (prose)?** Câu từ có nhịp thở âm nhạc không?
- **P1: Hook có bản sắc (identity) riêng không?** Dễ nhớ, có thể ngân nga, neo giữ được người nghe.
- **P1: Cảm xúc có chuyển động (emotional progression) không?** Hay các section đứng yên một chỗ?
- **P1: Verse 2 có phát triển không?** Đi sâu hơn, tăng vulnerability, không twin lặp lại Verse 1.
- **P1: Có thesis/explanation dư thừa không?** Có dòng nào đang đứng ngoài giải thích bài hát không?
- **P2: Nhạc tính, nhịp thở & miệng hát (Prosody & singability):** Điểm rơi, ngắt hơi tự nhiên.
- **P2: Vần điệu, hình ảnh & chi tiết (Rhyme, cliché, imagery):** Đẹp câu chữ không được phép thắng cảm xúc.

### 3 câu hỏi kiểm tra nhanh trước khi release:
1. **Nếu bỏ phần mô tả bối cảnh, cảm xúc cốt lõi còn sống không?** (Bối cảnh có nâng đỡ cảm xúc hay chỉ là cảnh tĩnh/kê khai?)
2. **Có section nào đang kể việc hoặc giải thích ý thay vì hát cảm xúc không?** (Tránh hoạt cảnh tự sự và tiểu luận tâm lý).
3. **Sau khi đọc xong, có câu/hook nào còn ở lại vì cảm xúc hoặc cách nói, không chỉ vì thông tin?** (Đủ sức nặng ca từ).
*(Nếu không đạt $\rightarrow$ nén cảnh, cắt giải thích, tập trung vào sự thật cảm xúc theo quy trình: CUT → COMPRESS → REPOSITION → REPURPOSE → only then ADD).*

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

> [!IMPORTANT]
> **Nguyên tắc điều hướng Runtime (Runtime Routing Policy):**
> - Một tài liệu có liên quan đến chủ đề **KHÔNG** đồng nghĩa với việc nó phải được nạp. Chỉ nạp tài liệu tham chiếu khi: (1) yêu cầu của người dùng đòi hỏi năng lực chuyên sâu của tài liệu đó; HOẶC (2) xuất hiện triệu chứng cấn rõ ràng cần giải quyết. Với sáng tác mở/đơn giản thông thường: **không nạp bất kỳ tài liệu tham chiếu WRITE chuyên biệt nào là hoàn toàn chuẩn mực (zero specialized WRITE references is valid).**
> - Router mặc định chỉ expose các lane cần thiết cho task hiện tại. Chỉ load 1–2 reference cần thiết khi có thể.
> - **AUDIT là lane riêng:** Chỉ bật khi user yêu cầu review/audit/regression hoặc có failure artifact cần truy tầng.
> - Tuyệt đối **không load** `stage-validation-loop.md`, eval suites, historical audits hoặc `dominant-analysis.md` vào normal writer-pass.

| Lane | Nhu cầu chuyên sâu | Tài liệu tham chiếu |
|---|---|---|
| **WRITE — FAST** | Brief mở/đơn giản, miền nghĩa rõ, sáng tác trọn bài thông thường | **SKILL.md built-in Fast Path** (không nạp tài liệu tham chiếu ngoài mặc định) |
| **WRITE — DEEP** | Khái niệm phức tạp/đa nghĩa/giàu vật liệu, nhiều Tứ, reseed cấu trúc, kiến trúc liên tưởng/ngoại hóa | `references/idea-and-structure.md` |
| **WRITE** | Phổ thơ sang ca khúc | `references/poem-to-song.md` (+ `references/folk-prosody.md`) |
| **LANGUAGE** | Tiếng Việt, ngữ âm, vần điệu, dấu thanh, thanh điệu ca từ | `references/vietnamese-line-and-sound.md` |
| **REFINE** | Tinh lọc ca từ, nén nghĩa, điểm rơi, subtext, sonic craft | `references/lyric-refinement.md` |
| **MUSIC** | Giai điệu, hòa âm, groove, demo mộc, feedback | `references/music-sketch-and-demo.md` |
| **MUSIC** | Định tuyến ca từ theo thể loại âm nhạc | `references/genre-and-lyric-routing.md` |
| **STYLE** | Vietnamese Style DNA (12 lanes nhạc Việt & soundscape) | `references/vietnamese-style-dna.md` |
| **STYLE** | Khai phá phong cách âm nhạc (Style Prompt & DNA) | `references/style-mining.md` |
| **STYLE** | Thống kê quần thể & mật độ hát (Corpus Profile, WPM) | `references/vietnamese-corpus-profile.md` |
| **PRONUNCIATION** | Khẩu khí & ngữ âm khi hát (Spoken Form & Prosody) | `references/vietnamese-spoken-form.md` |
| **PRONUNCIATION** | Định hướng giọng hát (Vocal Realization) & vocal prosody | `references/vocal-realization.md` |
| **SUNO** | Suno 3-block production, character budgets & ma trận lỗi | `references/suno-production.md` (Mặc định nạp cho Suno tasks; Primary Owner của Suno production/output) |
| **SUNO** | Suno Handoff & thẻ lệnh xuất | `references/suno-handoff.md` (Compatibility / quick-handoff sidecar — KHÔNG tự động nạp cùng; chỉ nạp khi cần đóng gói nhanh thẻ lệnh/handoff) |
| **AUDIT** *(Lane riêng)* | Reviewer độc lập (Evidence discipline, 6 lenses + music-fit) | `references/lyric-quality-review.md` |
| **AUDIT** *(Lane riêng)* | Audit / failure tracing xuyên tầng | `references/stage-validation-loop.md` (Chỉ audit/debug khi có failure artifact hoặc user yêu cầu review/regression; KHÔNG load trong normal generation) |
| **AUDIT** *(Lane riêng)* | Phân tích hợp âm, hòa thanh & trục cảm xúc | `references/dominant-analysis.md` (ANALYSIS-ONLY / DEMOTED — KHÔNG load trong normal generation) |
| **AUDIT** *(Lane riêng)* | Bộ dữ liệu kiểm thử & hồi quy (Eval & Regression Suite) | `references/audit-and-evaluation.md` (Tier 3 - không nạp khi viết) |
