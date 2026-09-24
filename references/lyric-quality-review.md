# Quy Chuẩn Thẩm Định Độc Lập (Lyric Quality Review)

> **REVIEW SIDECAR OWNER**
> Tài liệu này là **chủ sở hữu chuẩn (Canonical Owner) của vai trò Thẩm định độc lập (Sidecar Reviewer)** với quy trình cốt lõi:
> $$\text{OBSERVE} \longrightarrow \text{CLASSIFY} \longrightarrow \text{PRIORITIZE} \longrightarrow \text{ROUTE}$$
> Reviewer sở hữu: kỷ luật bằng chứng (evidence discipline), phân loại mức độ nghiêm trọng (severity classification), định dạng báo cáo thẩm định (Review Output Format), báo cáo vị trí/vấn đề/nguyên nhân (Location/Problem/Why), nhận diện triệu chứng, và điều hướng triệu chứng về đúng tài liệu chủ sở hữu chuẩn.
>
> **Ranh giới thẩm quyền:**
> - Reviewer **không phải là cẩm nang sáng tác thay thế** cho Writer; không thiết lập một bộ quy tắc ca từ, ngôn ngữ, âm thanh hay Writer rules độc lập thứ hai.
> - Reviewer có thể gợi ý phương án sửa cục bộ tại chỗ (targeted/local fixes).
> - Khi triệu chứng thuộc về tinh lọc ca từ / kỹ nghệ lời hát $\rightarrow$ điều hướng về **`references/lyric-refinement.md`**.
> - Khi triệu chứng thuộc về ngôn ngữ / âm thanh / thanh điệu $\rightarrow$ điều hướng về **`references/vietnamese-line-and-sound.md`**.

> **Mục đích:** Đóng vai trò chuyên gia thẩm định (Reviewer) độc lập, đánh giá chất lượng ca từ hoàn thiện nhằm phát hiện sáo rỗng (AI-slop), văn xuôi xuống dòng, thesis line, writerly phrasing, camera sweep, hoạt cảnh tự sự (sitcom narrative) và lỗi điểm rơi mà không làm gián đoạn dòng chảy của người viết (Writer).

---

## 1. Nguyên Tắc Tách Bạch Vai Trò & Kỷ Luật Bằng Chứng (Role Separation & Evidence Discipline)

```text
CREATIVE BRAIN (Tứ, Cốt, Hook, Cảm xúc)
       ↓
    WRITER (Viết mạch lạc, ngôn từ tự nhiên, giàu nhạc tính)
       ↓
   [SIDECAR] REVIEWER (Thẩm định độc lập: Soi lỗi, phân loại mức độ, đề xuất sửa cục bộ)
```

- **Reviewer là một Sidecar (Không nằm trên đường đi mặc định):** Reviewer chỉ được kích hoạt khi:
  1. Người dùng yêu cầu đánh giá, thẩm định hoặc phản biện (Audit / Critique / QA).
  2. Hoặc khi chạy quy trình formal kiểm định chất lượng trước khi release candidate.
  3. Tuyệt đối không tự động chèn vào giữa flow viết thông thường gây ức chế sáng tạo.
- **Không ngắt lời Writer:** Reviewer chỉ vào cuộc sau khi bản nháp hoặc section đã được viết trọn vẹn.
- **Không tự ý viết lại cả bài:** Reviewer định vị chính xác vị trí lỗi và đề xuất cách sửa cục bộ; tuyệt đối không xóa bài để viết lại theo gu cá nhân.
- **Kỷ luật bằng chứng âm thanh (Audio Claim & Evidence Discipline):**
  - **Khi CHƯA CÓ audio thực tế / render:**
    - Reviewer ĐƯỢC PHÉP nhận định rủi ro: `potential singability risk`, `likely phrase-density issue`, `possible landing risk`, `phonetic/melismatic risk`.
    - Reviewer TUYỆT ĐỐI KHÔNG tuyên bố khẳng định: *"độ ngân tự nhiên"*, *"điểm rơi vang tự nhiên"*, *"hát chắc chắn ổn"*, *"vocal landing tự nhiên"*.
    - Từ vựng bằng chứng bắt buộc: Dùng `OBSERVED`, `LIKELY`, `RISK`, `UNVERIFIED` thay cho các từ khẳng định tuyệt đối `ABSOLUTELY PASS`, `DEFINITELY NATURAL`, `CERTAINLY SINGABLE`.
- **Ngôn ngữ Self-Review khách quan (Evidence-Aware, Not Self-Congratulatory):**
  - Tuyệt đối không dùng các từ tự khen hay khẳng định vô căn cứ: *“hoàn toàn”*, *“tuyệt đối”*, *“chắc chắn”*, *“đều có độ ngân tự nhiên”*, *“không có vấn đề”*.
  - Thay bằng lối diễn đạt đúng thực tế bằng chứng: *“Không phát hiện rõ lỗi...”*, *“Không thấy lỗi đáng kể ở mức lyric-only...”*, *“Có risk nhẹ ở...”*, *“Chưa thể xác nhận điểm rơi/ngân nếu chưa có audio...”*.
- **Phân loại theo 3 cấp độ ưu tiên (thay thế điểm số cảm tính):**
  - `CRITICAL` (Lỗi sinh tử bắt buộc sửa: gượng ép tiếng Việt nặng, sai provenance, hỏng cấu trúc, hoặc thesis line leo thang phá vỡ section job);
  - `SUGGESTED` (Khuyến nghị nâng cấp: thesis line / analysis leakage mặc định, khử writerly, dọn camera sweep, nén câu, show don't explain, narrative-to-lyric, psychology-to-lyric);
  - `OPTIONAL` (Lựa chọn trau chuốt thêm nếu người dùng muốn).
- **Quy tắc dừng sau chẩn đoán (Stop After Diagnosis):**
  - Sau khi chỉ ra $1 - 2$ vấn đề cụ thể, Reviewer KHÔNG tiếp tục bới thêm lỗi vụn vặt chỉ để bản review trông dày dặn.
  - Khi `CRITICAL = 0`, các điểm `SUGGESTED` đã được giải quyết hoặc ở mức kiểm soát được, và phần còn lại chỉ là `OPTIONAL` $\rightarrow$ **KẾT LUẬN PASS & STOP NGAY LẬP TỨC**. Tuyệt đối không polish quá đà (*over-polishing*) khi ý đồ người dùng đã đạt.

---

## 2. Sáu Lớp Thẩm Định Chất Lượng (The 6 Quality Lenses)

Khi thẩm định độc lập, reviewer soi xét ca từ qua 6 lăng kính độc lập:

1. **Semantic Correctness:** Tính chính xác của ngữ nghĩa, đúng Tứ, logic nhân vật và section jobs.
2. **Natural Vietnamese (Register-Relative):**
   ```text
   grammatically correct ≠ naturally spoken ≠ emotionally credible ≠ poetically effective
   Specific ≠ Artificial  |  Common ≠ Better  |  Poetic ≠ Better  |  Simple ≠ Flat
   ```
   - **Tính tương đối theo Register:** Ca từ tự nhiên của `Mainstream Pop ≠ Folk / Dân gian ≠ Literary / Thơ ≠ Cổ phong`. Ví dụ: *"cố nhân"* hoàn toàn tự nhiên và mang sức nặng trong không gian cổ phong/văn học, không bị ép đổi về *"người cũ"* của khẩu ngữ pop đời thường.
3. **Emotional Credibility & Show vs. Tell Nuance:** 
   - Độ tin cậy cảm xúc; để hành động và hình ảnh tự nói lên cảm xúc thay vì kèm câu thuyết minh giải thích bài học.
   - **SHOW KHÔNG PHẢI LÀ TUYỆT ĐỐI:** Câu cảm xúc trực diện (DIRECT EMOTIONAL LANGUAGE) hoàn toàn được phép và có giá trị cao khi nó tạo ra cú nổ cảm xúc (payoff), được tích lũy từ trước (earned), và không phải slogan tình yêu chung chung. Tuyệt đối không tự động gắn mác lỗi "Tell" cho câu cảm xúc trực diện đắt giá.
   - Ẩn dụ phục vụ cảm xúc trung tâm được **GIỮ LẠI (KEEP)**. Chi tiết quan hệ riêng tư có giá trị cao dù không hoa mỹ.
4. **Lyric Behavior / Singability (Lyric-Only Heuristics):** Phân đoạn hơi thở khả dĩ, mật độ âm tiết, biên từ và điểm rơi. Syllable count chỉ là risk signal, không phải bằng chứng lỗi hát.
5. **Image Necessity & Density:** Chi tiết có chức năng hay chỉ là đạo cụ trang trí? Nhận diện và cắt tỉa camera sweep (dồn dập liệt kê nhiều vật thể mà thiếu payoff).
6. **Lexical / Writerly Naturalness:** Nhận diện các cụm từ làm dáng (*staged / writerly*), nhân hóa làm màu (*decorative personification*). Áp dụng triết lý: **"Reduce ornament before adding ornament"** (giản hóa, đưa về cách nói chân thực trước khi nghĩ đến việc thêm ẩn dụ hay chi tiết mới).

### Tiêu chuẩn Thẩm định Thực chất (Gỡ bỏ False Positives):
Reviewer TUYỆT ĐỐI KHÔNG coi những yếu tố sau là bằng chứng của một ca khúc hay:
- Hành vi cụ thể/dễ thương của cặp đôi (behavior specificity);
- Không có từ cliché trong blacklist;
- Hội thoại đời thường tự nhiên;
- Nhiều chi tiết hành động thực tế.
Đây chỉ là vật liệu phụ trợ, không chứng minh chất lượng ca từ. Reviewer bắt buộc soi xét qua 3 câu hỏi thực chất:
1. **Lyricicity Check (Chất ca từ):** Dòng này có tạo ra trải nghiệm thẩm mỹ/ca từ mà văn xuôi tự sự không làm được không?
2. **Emotional Resonance Check (Rung cảm):** Dòng này làm người nghe RUNG ĐỘNG hay chỉ giúp họ HIỂU điều nhân vật đang làm/nghĩ?
3. **Musical-Language Check (Nhạc tính):** Câu từ có được gọt giũa theo nhịp thở của một câu hát không, hay chỉ là câu văn nói chép lại?

---

## 3. Cấu Trúc Báo Cáo Thẩm Định (Review Output Format)

Mỗi lỗi được phát hiện phải tuân thủ đúng 4 trường thông tin:

```text
- LOCATION: [Tên Section, Dòng số X]
- PROBLEM:  [Tên triệu chứng: Cliché / Thesis Line / Provenance / Forced Rhyme / Prose-to-Lyric / Weak Landing / Writerly Phrase / Decorative Specificity / Show-Don't-Explain / Semantic Redundancy / Camera Sweep / Narrative Density / Paraphrase Density / Generic Emotion / Chorus Anti-Essay / Bridge Anti-Essay / Narrative-to-Lyric / Psychology-to-Lyric / SCENE-REPORT / PSYCHOLOGY-ESSAY / BIG-WORD-ESCALATION / ABSTRACT-NOUN-STACKING / OVER-EXPLAINED-METAPHOR / CLICHE-ESCALATION / MISSING-IDIOSYNCRASY / PROSE-AI-TELL / MOUTHFUL-LINE / STRESS-RISK / SPOKEN-FORM-RISK / GENRE-MISMATCH / DENSITY-RISK / AWKWARD-BREATH / Audio-Claim-Violation]
- WHY:      [Lý do tại sao dòng này làm giảm chất lượng, phẳng cảm xúc hoặc phô diễn chữ]
- TARGETED FIX: [1–2 phương án sửa tại chỗ bằng cách GIẢN HÓA hoặc NÉN NGHĨA theo thứ tự: CUT → COMPRESS → REPOSITION → REPURPOSE → only then ADD, giữ nguyên mạch section]
```

---

## 4. Danh Mục Các Lỗi Trọng Tâm (Anti-Slop & Quality Checklist)

### A. CRITICAL (Bắt buộc sửa)
1. **Provenance Breach (Vi phạm thẩm quyền trần thuật):**
   - Người kể tự khẳng định như đinh đóng cột về nội tâm, suy nghĩ hoặc hành vi tương lai của người khác khi dữ liệu brief không cho phép.
2. **Forced Rhyme Harm (Ép vần phá nghĩa):**
   - Đảo cú pháp bất thường hoặc chọn một từ xa lạ, ngô nghê chỉ để bắt vần với câu trên.
3. **Escalated Thesis Line / Analysis Leakage:**
   - Mục này **CHỈ ÁP DỤNG** khi có bằng chứng thực tế cho thấy câu thuyết minh:
     - Phá vỡ ý nghĩa trung tâm (*breaks central meaning*); HOẶC
     - Phá vỡ nhiệm vụ cốt lõi của một section lớn như Chorus hoặc Bridge (*breaks a major section job*); HOẶC
     - Gây ra vi phạm điểm nhìn / thẩm quyền trần thuật (*causes a POV/provenance violation*); HOẶC
     - Biến section thành bài nghị luận/thuyết minh đủ nghiêm trọng để phá vỡ hệ thống ca khúc (*turns a major section into an essay severe enough to break the song system*).

### B. SUGGESTED (Khuyến nghị nâng cấp)
1. **Thesis Line & Analysis Leakage (Mặc định / Default):**
   - *Phân loại mặc định:* Đây là phân loại mặc định (DEFAULT) cho các câu mang tính giải thích triết lý, thuyết minh kết luận thay vì để hành động và cảm xúc tự lên tiếng.
   - *Bộ nhận diện nghi vấn (Detectors Only — KHÔNG PHẢI blacklist từ cấm):* Sự xuất hiện của các cụm như *"hóa ra...", "thì ra...", "chỉ là...", "điều đau nhất là..."* chỉ đóng vai trò detectors nhận diện điểm rơi nghi vấn. Chúng **không tự động cấu thành lỗi** và **không phải danh sách từ cấm**. Ngữ cảnh và chức năng biểu đạt trong câu hát sẽ quyết định.
   - *Khả năng leo thang:* Vấn đề SUGGESTED này chỉ có thể leo thang sang `CRITICAL` (mục A.3) khi có bằng chứng rõ ràng thỏa mãn các điều kiện phá vỡ cấu trúc tại mục A.
   - *Xử lý:* Điều hướng xử lý về `references/lyric-refinement.md` để nén câu, giản hóa hoặc chuyển thành câu cảm xúc trực diện.
2. **SCENE-REPORT (Báo cáo cảnh vật / Dồn dập ngoại cảnh thiếu tải trọng cảm xúc):**
   - *Dấu hiệu:* Nhiều dòng chỉ thuần túy ghi nhận cảnh vật, thời tiết, hoạt động thường nhật (*phố xá, đèn đường, dắt xe, kéo khóa, quạt gió, ngã tư...*). Thấy hai người đang làm gì nhưng chưa cảm được họ có ý nghĩa gì với nhau; bỏ cảnh đi cảm xúc bài vẫn nguyên.
   - *4 câu hỏi xử lý cục bộ:*
     1. *Cảnh này đang làm người nghe cảm gì?*
     2. *Quan hệ thay đổi ở đâu?*
     3. *Nếu bỏ chi tiết này, emotional meaning có mất không?*
     4. *Có câu cảm xúc / tương tác nào mạnh hơn đang bị cảnh che mất không?*
   - *Quy trình sửa chữa (Repair Order: CUT → COMPRESS → REPURPOSE → only then ADD):*
     1. **CUT:** Cắt bỏ các chi tiết/dòng ghi nhận cảnh quan thuần túy không đóng góp cho cảm xúc;
     2. **COMPRESS:** Nén bối cảnh lại thành một điểm tựa tối thiểu để người nghe chạm vào được;
     3. **REPURPOSE:** Tận dụng vật liệu sẵn có để gắn với một cử chỉ, thói quen quan hệ hoặc điểm rơi cảm xúc;
     4. **ADD (chỉ sau cùng khi thực sự cần):** Tuyệt đối không vội vã nhét thêm các câu nói chung chung (*"anh yêu em / anh bình yên"*); chỉ bổ sung câu cảm xúc khi mạch bài thực sự thiếu điểm tựa.
3. **PSYCHOLOGY-ESSAY (Hội chứng thuyết trình tâm lý & nghị luận tình cảm):**
   - *Dấu hiệu:* Tác giả đứng ngoài phân tích tâm lý thay vì để nhân vật cất lời; giải thích quá nhiều *"tình yêu là..."*, *"anh hiểu rằng..."*; đưa ra các chân lý tổng quát đao to búa lớn (*"Điều dũng cảm nhất của một người đàn ông..."*); Bridge giống bài phát biểu so sánh triết lý (`Người ta thường gom nhặt những điều lớn lao... nhưng nhìn em anh mới hiểu...`).
   - *Câu hỏi xử lý:* *"Đây có phải câu hát bật ra từ nhân vật, hay tác giả đang đứng ngoài giải thích bài hát cho người nghe?"*
   - *Xử lý:* Nén lại, chuyển thành câu cảm xúc trực diện chân thành (*"Anh mệt lắm, nhưng thấy em cười là quên hết"*), thế đối lập, hoặc bỏ hẳn đoạn nghị luận.
4. **BIG-WORD-ESCALATION (Leo thang từ ngữ giả tạo ở Final Chorus):**
   - *Dấu hiệu:* Cố tạo cảm giác cao trào, vĩ mô bằng cách phóng đại kích cỡ từ ngữ: từ *con đường, góc phố* ở Verse nhảy vọt lên *năm tháng, cuộc đời, kỳ diệu, mãi mãi, định mệnh, tất cả* ở Final Chorus mà không có tích lũy chiều sâu quan hệ.
   - *Xử lý:* Ngăn chặn việc tăng kích cỡ từ ngữ. Thay bằng **leo thang độ thân mật (intimacy escalation)**: một sự thật dễ tổn thương hơn, một lời thú nhận phụ thuộc, hoặc một hình ảnh quen quay lại mang nghĩa mới.
5. **Show, Don't Explain & Over-Explanation (Thuyết minh thừa thãi):**
   - Mô thức: `Hình ảnh / Hành động + Câu giải thích nghĩa của hình ảnh đó`.
     *Ví dụ:* `Mẹ lau lại chiếc ly của cha` $\rightarrow$ Hành động này đã đủ mạnh và đắt giá. Nếu viết tiếp: `Đủ để con hiểu người đã không còn...` $\rightarrow$ Đây là over-explanation làm loãng dư ba.
6. **Semantic Redundancy (Trùng lặp chức năng ngữ nghĩa giữa các đoạn):**
   - Hai câu ở các section liền kề cùng thực hiện một nhiệm vụ ngữ nghĩa (ví dụ: Verse 1 kết bằng *"Mọi thứ trôi đi như một buổi sáng bình thường"*, sau đó Chorus lại mở bằng *"Nhà mình sáng nay chẳng thiếu một thứ gì..."*).
   - *Xử lý:* Đánh dấu `SUGGESTED - Semantic redundancy between sections`. Ưu tiên giữ câu mạnh hơn ở Chorus, làm câu ở Verse cụ thể hơn bằng chi tiết vật lý, hoặc bỏ hẳn câu tổng kết ở Verse.
7. **Image Density & Camera Sweep (Dồn dập liệt kê đạo cụ thiếu payoff):**
   - Quét lia lịa qua quá nhiều đối tượng: `vật A → địa điểm B → thời tiết C → phương tiện D → bức tường E → chậu cây F → nền đất G` mà các chi tiết không cùng phục vụ một chức năng cảm xúc hay dẫn tới payoff.
   - *Xử lý:* Gom cụm hoặc lược bớt $1 - 2$ chi tiết giá trị thấp để không gian có chỗ thở. Tuyệt đối không viết lại toàn bộ Verse.
8. **Narrative-to-Lyric Failure (Tỉ lệ tự sự / hoạt cảnh sitcom quá cao):**
   - Kích hoạt khi ca từ có thể được tóm tắt thành một chuỗi sự kiện, hành vi hoặc hội thoại đời thường mà không mất đi phần lớn giá trị cảm xúc (ví dụ: *em mở cửa → em kéo tay → em cười → em hát → anh trêu → em nhìn → anh bật cười → anh mê em*).
   - *Xử lý:* Thay thế $1 - 3$ dòng tự sự/hành vi bằng các dòng mang hình tượng cảm xúc (*Lyric Carrying Lines*) hoặc sự nén cảm xúc.
9. **Chorus Anti-Essay (Chống Chorus biến thành bản luận đề):**
   - Ngăn chặn việc Chorus biến thành một danh sách các mệnh đề logic: `không X, mà Y, nên Z, thành ra A, thành ra B` hoặc `Không cần X vì có Y là đủ`.
   - Chorus cần sự nén lại về nhạc tính và cảm xúc: 1 ý niệm trung tâm + 1 carrier đáng nhớ + 1 bước giải phóng cảm xúc (emotional release). Vẫn cho phép ngôn từ trực diện.
10. **Bridge Anti-Essay (Chống Bridge biến thành bài giảng triết lý):**
   - Không để Bridge rơi vào mô thức bài giảng: `Ngày trước tôi nghĩ X, sau đó tôi nhận ra Y, vậy nên tình yêu là Z` hoặc `Người ta thường... nhưng nhìn em anh mới hiểu...`.
   - Ưu tiên: `Niềm tin cũ → Một mâu thuẫn cụ thể → Bước ngoặt cảm xúc (Confession / Turn)`. Để người nghe tự hoàn thiện một phần sự nhận ra.
11. **Generic Emotional Language (Ngôn ngữ cảm xúc chung chung):**
   - Đặt câu hỏi: *"Câu này có thể bê sang 10 bài tình ca khác mà không thay đổi điều gì không?"* (ví dụ: *em muốn anh tốt hơn, anh được là chính mình, em luôn ở bên anh, anh thấy bình yên, tình yêu làm mọi thứ tốt đẹp*).
   - Nếu có: Gắn nhãn `SUGGESTED`.
   - *Thứ tự ưu tiên sửa:* `Specific Feeling > Specific Relationship Truth > Specific Phrasing > Image (chỉ khi thực sự hữu ích)`. Tuyệt đối không để model vô thức hiểu lầm rằng gặp câu chung chung là phải đi tìm ẩn dụ / metaphor.
12. **Writerly / Staged Phrasing (Làm dáng văn vẻ / Nhân hóa trang trí):**
   - Cụm từ nghe như được tạo ra để "làm thơ", kết hợp từ lạ tai (*unusual collocation*), trừu tượng chồng trừu tượng, hoặc nhân hóa đồ vật làm màu (*decorative personification*).
   - *Xử lý:* Gắn nhãn `SUGGESTED - Writerly Phrase`. Đề xuất giản hóa về cách nói chân thực mà vẫn giữ được không khí.
13. **Decorative Specificity (Chi tiết cụ thể thiếu chức năng):**
   - Reviewer đặt câu hỏi: `Does this detail earn its place?` (Chi tiết này có tự chứng minh sự tất yếu không?).
   - Một chi tiết được giữ lại nếu nó có ít nhất một chức năng đáng kể: *provenance từ brief, ký ức vật lý, giá trị giác quan, chức năng tình huống, tín hiệu quan hệ, hoặc narrative turn*.
   - Nếu không có: Khuyến nghị **Giữ nguyên hoặc Giản hóa** (`KEEP or SIMPLIFY`, ví dụ: `sân gạch` $\rightarrow$ `sân nhà`). Tuyệt đối **không lập danh sách đen từ ngữ** (No Word Blacklisting).
14. **Prose-to-Lyric (Văn xuôi xuống dòng):**
   - Câu đúng ngữ pháp nhưng chứa quá nhiều từ nối (*"nên", "vì", "thực ra là"*), nhịp điệu phẳng lỳ, thiếu tính nén của ca từ.
15. **Weak Line Landing (Điểm rơi cuối dòng lửng lơ):**
   - Dòng trọng tâm của Chorus hoặc chốt đoạn kết thúc bằng một từ chức năng (*"nữa đâu", "được gì", "thế này"*); cần chuyển trọng tâm về động từ, danh từ cảm xúc hoặc khoảng lặng.
16. **Cliché & Generic Tropes (Sáo mòn):**
    - Sử dụng các cụm từ mòn vẹt: *"con tim tan vỡ", "định mệnh an bài", "nước mắt tuôn rơi", "yêu đến điên dại", "thanh xuân của anh"*; hoặc mặc định gọi mưa/mùa đông/hoàng hôn làm công cụ tạo buồn vô cớ.
17. **Abstract Noun Stacking (Xếp chồng danh từ trừu tượng — voice-checker):**
    - *Dấu hiệu:* Quá nhiều danh từ trừu tượng đứng cạnh nhau trong cùng một câu/đoạn (*tình yêu, hy vọng, ánh sáng, định mệnh, bình yên, tổn thương, ký ức*).
    - *Nguy cơ:* Dùng danh từ trừu tượng làm phím tắt cảm xúc thay vì chạm vào cảm giác thật.
    - *Xử lý:* Gắn nhãn `SUGGESTED - Abstract Noun Stacking`. Nén bớt danh từ trừu tượng, giữ lại 1 hạt nhân và neo bằng cử chỉ hoặc sự thật quan hệ. (Không cấm danh từ trừu tượng, chỉ cảnh báo khi lạm dụng).
18. **Over-Explained Metaphor (Ẩn dụ bị giải thích thừa thãi — voice-checker):**
    - *Dấu hiệu:* Ẩn dụ vừa xuất hiện thì ngay sau đó tác giả đã nhảy vào giải thích cặn kẽ ý nghĩa của nó: `image → explanation → explanation`.
    - *Xử lý:* Gắn nhãn `SUGGESTED - Over-Explained Metaphor`. Cắt bỏ phần giải thích thừa, để người nghe tự hoàn thiện khoảng trống thẩm mỹ.
19. **Cliché Escalation (Leo thang từ ngữ sáo mòn — voice-checker):**
    - *Dấu hiệu:* Đoạn kết cố tạo cảm giác cao trào bằng chuỗi từ phóng đại: *yêu → mãi mãi → cả đời → vĩnh cửu → định mệnh* mà không có sự khám phá cảm xúc mới.
    - *Xử lý:* Gắn nhãn `SUGGESTED - Cliché Escalation`. Chuyển sang leo thang độ thân mật (*intimacy escalation*), một sự thật dễ tổn thương hơn của nhân vật.
20. **Missing Idiosyncrasy (Thiếu dấu vân tay riêng của bài hát — voice-checker):**
    - *Dấu hiệu:* Bài hát đúng chủ đề, đúng kỹ thuật nhưng hoàn toàn vắng bóng một chi tiết, một cách nói hay một góc nhìn riêng biệt của cặp đôi, nghe như bài hát chung chung AI viết cho bất kỳ ai.
    - *Xử lý:* Gắn nhãn `SUGGESTED - Missing Idiosyncrasy`. Nhắc: *"Bài đang đúng chủ đề nhưng chưa có một chi tiết/câu nói mang dấu vân tay riêng"*. Khuyến khích đưa vào 1 thói quen ngầm hoặc cách nói riêng (tuyệt đối không ép thêm chi tiết kỳ quặc/quirky khiên cưỡng).
21. **Prose-AI-Tell (Câu văn xuôi AI kể chuyện — voice-checker):**
    - *Dấu hiệu:* Câu ca từ có cấu trúc giống văn xuôi giải thích được ngắt dòng, chứa nhiều từ nối giải thích (*"để rồi", "thực ra", "bởi vì thế"*), nhịp phẳng, thiếu nhạc tính.
    - *Xử lý:* Gắn nhãn `SUGGESTED - Prose-AI-Tell`. Reviewer chỉ flag và đề xuất nén hoặc chuyển đổi nhịp điệu; tuyệt đối không tự động viết lại cả bài.

### C. VIETNAMESE MUSIC-FIT & PROSODY (Advisory Diagnostics — Tham Vấn, Không Block Writer)
> **Nguyên tắc:** Các chẩn đoán dưới đây giúp hoàn thiện tính khả thi khi hát (singability) và tương thích thể loại, **tuyệt đối không dùng để bóp nghẹt ngòi bút hay ghi đè cảm xúc trung tâm của tác giả**.

1. **MOUTHFUL-LINE (Nghẽn khẩu hình / Dồn ứ âm tiết):**
   - *Dấu hiệu:* Dòng chứa quá nhiều phụ âm tắc (`t, p, c, k, ch`) hoặc cụm từ ghép liên tiếp trong tiết tấu nhanh, khiến người hát không kịp nhả chữ hoặc AI engine líu lưỡi.
   - *Xử lý:* Gắn nhãn `SUGGESTED - Mouthful Line`. Cắt bỏ hư từ nối thừa, tạo khoảng nghỉ cho nguyên âm mở ngân dài.
2. **AWKWARD-BREATH / FORCED-PUNCTUATION (Ngắt nhịp xé nghĩa):**
   - *Dấu hiệu:* Điểm ngắt dòng hoặc lấy hơi cắt đôi một từ ghép hoặc cụm ngữ nghĩa tự nhiên.
   - *Xử lý:* Gắn nhãn `SUGGESTED - Awkward Breath`. Đẩy từ sang dòng mới hoặc nén lại để điểm lấy hơi trùng với ranh giới ngữ nghĩa.
3. **STRESS-RISK / STRESS-MISMATCH (Cấn dấu thanh & Trọng âm):**
   - *Dấu hiệu:* Âm tiết mang thanh điệu trầm/khép (nặng, huyền) rơi vào đỉnh cao trào giai điệu, hoặc thanh sắc/ngã rơi vào đáy trầm khiến khi hát dễ bị lệch thanh điệu tiếng Việt.
   - *Xử lý:* Gắn nhãn `SUGGESTED - Stress Risk`. Nhắc tác giả chú ý độ luyến thanh hoặc hoán vị từ. *(Chỉ áp dụng mức độ chắc chắn khi đã có audio/demo; khi chưa có audio chỉ ghi nhận `LIKELY/RISK`).*
4. **SPOKEN-FORM-RISK (Rủi ro phát âm dạng nói / Số / Ngoại lai):**
   - *Dấu hiệu:* Lời bài hát chứa số (ví dụ: *0h, 2026*), từ tiếng Anh đa âm tiết (*joker, running*), viết tắt (*AI, FB*) hoặc ký tự đặc biệt (*&, %*) mà không rõ cách engine/ca sĩ sẽ xướng âm.
   - *Xử lý:* Gắn nhãn `SUGGESTED - Spoken Form Risk`. Đề xuất bổ sung ghi chú phát âm (spoken guidance note) cho phần sản xuất/Suno mà không cần xóa văn bản nghệ thuật gốc.
5. **GENRE-MISMATCH (Lệch ngữ vực & Hành vi ca từ so với Soundscape):**
   - *Dấu hiệu:* Đã chọn lane âm nhạc cụ thể nhưng phong cách ca từ lại hoàn toàn nghịch hướng (ví dụ: làm dance-pop điện tử nhưng viết lời triết lý dài dòng không chỗ ngắt; hoặc làm acoustic mộc nhưng dùng khẩu khí hô hào stadium rock).
   - *Xử lý:* Gắn nhãn `SUGGESTED - Genre Mismatch`. Điều chỉnh mật độ câu và cách giải phóng hook cho tương thích với soundscape của lane.
6. **DENSITY-RISK (Rủi ro mật độ nhả chữ quá tải):**
   - *Dấu hiệu:* Số lượng từ ngữ trong bài vượt quá xa ngưỡng hát tự nhiên của thời lượng dự kiến (ví dụ: bài ballad 3.5 phút nhưng nhồi hơn 500 từ).
   - *Xử lý:* Gắn nhãn `SUGGESTED - Density Risk`. Đề xuất tinh gọn, cắt tỉa câu từ phụ trợ để bài hát có không gian thở.

### D. OPTIONAL (Trau chuốt thêm)
1. **Sonic Polish:** Thêm echo phụ âm đầu, lặp nguyên âm vang ở nốt ngân dự kiến (gợi ý tùy chọn).
2. **Image Freshness:** Thay một động từ quen thuộc bằng một động từ mang tính cử chỉ đời thường hơn.
