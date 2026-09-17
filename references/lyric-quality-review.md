# Quy Chuẩn Thẩm Định Độc Lập (Lyric Quality Review)

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
  - `CRITICAL` (Lỗi sinh tử bắt buộc sửa: gượng ép tiếng Việt nặng, sai provenance, hỏng cấu trúc);
  - `SUGGESTED` (Khuyến nghị nâng cấp: khử writerly, dọn camera sweep, nén câu, show don't explain, narrative-to-lyric, psychology-to-lyric);
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
- PROBLEM:  [Tên triệu chứng: Cliché / Thesis Line / Provenance / Forced Rhyme / Prose-to-Lyric / Weak Landing / Writerly Phrase / Decorative Specificity / Show-Don't-Explain / Semantic Redundancy / Camera Sweep / Narrative Density / Paraphrase Density / Generic Emotion / Chorus Anti-Essay / Bridge Anti-Essay / Narrative-to-Lyric / Psychology-to-Lyric / SCENE-REPORT / PSYCHOLOGY-ESSAY / BIG-WORD-ESCALATION / Audio-Claim-Violation]
- WHY:      [Lý do tại sao dòng này làm giảm chất lượng, phẳng cảm xúc hoặc phô diễn chữ]
- TARGETED FIX: [1–2 phương án sửa tại chỗ bằng cách GIẢN HÓA hoặc NÉN NGHĨA, giữ nguyên mạch section]
```

---

## 4. Danh Mục Các Lỗi Trọng Tâm (Anti-Slop & Quality Checklist)

### A. CRITICAL (Bắt buộc sửa)
1. **Thesis Line & Analysis Leakage:**
   - Dòng mở đầu bằng *"hóa ra...", "điều đau nhất là...", "thì ra...", "chỉ là..."* hoặc câu kết luận giải thích triết lý của bài hát thay vì để hành động tự nói lên cảm xúc.
2. **Provenance Breach (Vi phạm thẩm quyền trần thuật):**
   - Người kể tự khẳng định như đinh đóng cột về nội tâm, suy nghĩ hoặc hành vi tương lai của người khác khi dữ liệu brief không cho phép.
3. **Forced Rhyme Harm (Ép vần phá nghĩa):**
   - Đảo cú pháp bất thường hoặc chọn một từ xa lạ, ngô nghê chỉ để bắt vần với câu trên.

### B. SUGGESTED (Khuyến nghị nâng cấp)
1. **SCENE-REPORT (Báo cáo cảnh vật / Dồn dập ngoại cảnh thiếu tải trọng cảm xúc):**
   - *Dấu hiệu:* Nhiều dòng chỉ thuần túy ghi nhận cảnh vật, thời tiết, hoạt động thường nhật (*phố xá, đèn đường, dắt xe, kéo khóa, quạt gió, ngã tư...*). Thấy hai người đang làm gì nhưng chưa cảm được họ có ý nghĩa gì với nhau; bỏ cảnh đi cảm xúc bài vẫn nguyên.
   - *4 câu hỏi xử lý cục bộ:*
     1. *Cảnh này đang làm người nghe cảm gì?*
     2. *Quan hệ thay đổi ở đâu?*
     3. *Nếu bỏ chi tiết này, emotional meaning có mất không?*
     4. *Có câu cảm xúc / tương tác nào mạnh hơn đang bị cảnh che mất không?*
   - *Xử lý:* Cắt bớt cảnh thuần túy; chuyển $1 - 2$ dòng quan sát thành câu bộc lộ cảm xúc trực diện hoặc chi tiết mang tải trọng quan hệ (*Lyric Carrying Line*).
2. **PSYCHOLOGY-ESSAY (Hội chứng thuyết trình tâm lý & nghị luận tình cảm):**
   - *Dấu hiệu:* Tác giả đứng ngoài phân tích tâm lý thay vì để nhân vật cất lời; giải thích quá nhiều *"tình yêu là..."*, *"anh hiểu rằng..."*; đưa ra các chân lý tổng quát đao to búa lớn (*"Điều dũng cảm nhất của một người đàn ông..."*); Bridge giống bài phát biểu so sánh triết lý (`Người ta thường gom nhặt những điều lớn lao... nhưng nhìn em anh mới hiểu...`).
   - *Câu hỏi xử lý:* *"Đây có phải câu hát bật ra từ nhân vật, hay tác giả đang đứng ngoài giải thích bài hát cho người nghe?"*
   - *Xử lý:* Nén lại, chuyển thành câu cảm xúc trực diện chân thành (*"Anh mệt lắm, nhưng thấy em cười là quên hết"*), thế đối lập, hoặc bỏ hẳn đoạn nghị luận.
3. **BIG-WORD-ESCALATION (Leo thang từ ngữ giả tạo ở Final Chorus):**
   - *Dấu hiệu:* Cố tạo cảm giác cao trào, vĩ mô bằng cách phóng đại kích cỡ từ ngữ: từ *con đường, góc phố* ở Verse nhảy vọt lên *năm tháng, cuộc đời, kỳ diệu, mãi mãi, định mệnh, tất cả* ở Final Chorus mà không có tích lũy chiều sâu quan hệ.
   - *Xử lý:* Ngăn chặn việc tăng kích cỡ từ ngữ. Thay bằng **leo thang độ thân mật (intimacy escalation)**: một sự thật dễ tổn thương hơn, một lời thú nhận phụ thuộc, hoặc một hình ảnh quen quay lại mang nghĩa mới.
4. **Show, Don't Explain & Over-Explanation (Thuyết minh thừa thãi):**
   - Mô thức: `Hình ảnh / Hành động + Câu giải thích nghĩa của hình ảnh đó`.
     *Ví dụ:* `Mẹ lau lại chiếc ly của cha` $\rightarrow$ Hành động này đã đủ mạnh và đắt giá. Nếu viết tiếp: `Đủ để con hiểu người đã không còn...` $\rightarrow$ Đây là over-explanation làm loãng dư ba.
5. **Semantic Redundancy (Trùng lặp chức năng ngữ nghĩa giữa các đoạn):**
   - Hai câu ở các section liền kề cùng thực hiện một nhiệm vụ ngữ nghĩa (ví dụ: Verse 1 kết bằng *"Mọi thứ trôi đi như một buổi sáng bình thường"*, sau đó Chorus lại mở bằng *"Nhà mình sáng nay chẳng thiếu một thứ gì..."*).
   - *Xử lý:* Đánh dấu `SUGGESTED - Semantic redundancy between sections`. Ưu tiên giữ câu mạnh hơn ở Chorus, làm câu ở Verse cụ thể hơn bằng chi tiết vật lý, hoặc bỏ hẳn câu tổng kết ở Verse.
6. **Image Density & Camera Sweep (Dồn dập liệt kê đạo cụ thiếu payoff):**
   - Quét lia lịa qua quá nhiều đối tượng: `vật A → địa điểm B → thời tiết C → phương tiện D → bức tường E → chậu cây F → nền đất G` mà các chi tiết không cùng phục vụ một chức năng cảm xúc hay dẫn tới payoff.
   - *Xử lý:* Gom cụm hoặc lược bớt $1 - 2$ chi tiết giá trị thấp để không gian có chỗ thở. Tuyệt đối không viết lại toàn bộ Verse.
7. **Narrative-to-Lyric Failure (Tỉ lệ tự sự / hoạt cảnh sitcom quá cao):**
   - Kích hoạt khi ca từ có thể được tóm tắt thành một chuỗi sự kiện, hành vi hoặc hội thoại đời thường mà không mất đi phần lớn giá trị cảm xúc (ví dụ: *em mở cửa → em kéo tay → em cười → em hát → anh trêu → em nhìn → anh bật cười → anh mê em*).
   - *Xử lý:* Thay thế $1 - 3$ dòng tự sự/hành vi bằng các dòng mang hình tượng cảm xúc (*Lyric Carrying Lines*) hoặc sự nén cảm xúc.
8. **Chorus Anti-Essay (Chống Chorus biến thành bản luận đề):**
   - Ngăn chặn việc Chorus biến thành một danh sách các mệnh đề logic: `không X, mà Y, nên Z, thành ra A, thành ra B` hoặc `Không cần X vì có Y là đủ`.
   - Chorus cần sự nén lại về nhạc tính và cảm xúc: 1 ý niệm trung tâm + 1 carrier đáng nhớ + 1 bước giải phóng cảm xúc (emotional release). Vẫn cho phép ngôn từ trực diện.
9. **Bridge Anti-Essay (Chống Bridge biến thành bài giảng triết lý):**
   - Không để Bridge rơi vào mô thức bài giảng: `Ngày trước tôi nghĩ X, sau đó tôi nhận ra Y, vậy nên tình yêu là Z` hoặc `Người ta thường... nhưng nhìn em anh mới hiểu...`.
   - Ưu tiên: `Niềm tin cũ → Một mâu thuẫn cụ thể → Bước ngoặt cảm xúc (Confession / Turn)`. Để người nghe tự hoàn thiện một phần sự nhận ra.
10. **Generic Emotional Language (Ngôn ngữ cảm xúc chung chung):**
   - Đặt câu hỏi: *"Câu này có thể bê sang 10 bài tình ca khác mà không thay đổi điều gì không?"* (ví dụ: *em muốn anh tốt hơn, anh được là chính mình, em luôn ở bên anh, anh thấy bình yên, tình yêu làm mọi thứ tốt đẹp*).
   - Nếu có: Gắn nhãn `SUGGESTED`. Yêu cầu tìm kiếm một hình tượng riêng của bài, một quan sát riêng về mối quan hệ, một cách nén từ đáng nhớ hoặc một góc nhìn cảm xúc mới mẻ (không ép dùng ẩn dụ).
11. **Writerly / Staged Phrasing (Làm dáng văn vẻ / Nhân hóa trang trí):**
   - Cụm từ nghe như được tạo ra để "làm thơ", kết hợp từ lạ tai (*unusual collocation*), trừu tượng chồng trừu tượng, hoặc nhân hóa đồ vật làm màu (*decorative personification*).
   - *Xử lý:* Gắn nhãn `SUGGESTED - Writerly Phrase`. Đề xuất giản hóa về cách nói chân thực mà vẫn giữ được không khí.
12. **Decorative Specificity (Chi tiết cụ thể thiếu chức năng):**
   - Reviewer đặt câu hỏi: `Does this detail earn its place?` (Chi tiết này có tự chứng minh sự tất yếu không?).
   - Một chi tiết được giữ lại nếu nó có ít nhất một chức năng đáng kể: *provenance từ brief, ký ức vật lý, giá trị giác quan, chức năng tình huống, tín hiệu quan hệ, hoặc narrative turn*.
   - Nếu không có: Khuyến nghị **Giữ nguyên hoặc Giản hóa** (`KEEP or SIMPLIFY`, ví dụ: `sân gạch` $\rightarrow$ `sân nhà`). Tuyệt đối **không lập danh sách đen từ ngữ** (No Word Blacklisting).
13. **Prose-to-Lyric (Văn xuôi xuống dòng):**
   - Câu đúng ngữ pháp nhưng chứa quá nhiều từ nối (*"nên", "vì", "thực ra là"*), nhịp điệu phẳng lỳ, thiếu tính nén của ca từ.
14. **Weak Line Landing (Điểm rơi cuối dòng lửng lơ):**
   - Dòng trọng tâm của Chorus hoặc chốt đoạn kết thúc bằng một từ chức năng (*"nữa đâu", "được gì", "thế này"*); cần chuyển trọng tâm về động từ, danh từ cảm xúc hoặc khoảng lặng.
15. **Cliché & Generic Tropes (Sáo mòn):**
   - Sử dụng các cụm từ mòn vẹt: *"con tim tan vỡ", "định mệnh an bài", "nước mắt tuôn rơi", "yêu đến điên dại", "thanh xuân của anh"*; hoặc mặc định gọi mưa/mùa đông/hoàng hôn làm công cụ tạo buồn vô cớ.

### C. OPTIONAL (Trau chuốt thêm)
1. **Sonic Polish:** Thêm echo phụ âm đầu, lặp nguyên âm vang ở nốt ngân dự kiến (gợi ý tùy chọn).
2. **Image Freshness:** Thay một động từ quen thuộc bằng một động từ mang tính cử chỉ đời thường hơn.
