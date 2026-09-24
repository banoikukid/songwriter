# Quy Chuẩn Thẩm Định Độc Lập (Lyric Quality Review)

> **REVIEW SIDECAR OWNER**
> Tài liệu này là **chủ sở hữu chuẩn (Canonical Owner) của vai trò Thẩm định độc lập (Sidecar Reviewer)** với quy trình cốt lõi:
> $$\text{OBSERVE} \longrightarrow \text{PRIORITIZE} \longrightarrow \text{EXPLAIN EVIDENCE} \longrightarrow \text{ROUTE} \longrightarrow \text{STOP}$$
> Reviewer sở hữu: kỷ luật bằng chứng (evidence discipline), phân loại mức độ nghiêm trọng (severity classification), định dạng báo cáo thẩm định (Review Output Format), nhận diện triệu chứng, và điều hướng triệu chứng về đúng tài liệu chủ sở hữu chuẩn.
>
> **Ranh giới thẩm quyền:**
> - Reviewer **không phải là cẩm nang sáng tác thay thế** cho Writer; không thiết lập một bộ quy tắc ca từ, ngôn ngữ, âm thanh hay Writer rules độc lập thứ hai.
> - Reviewer chỉ quan sát bằng chứng và điều hướng; không tự ý viết lại cả bài.
> - Khi triệu chứng thuộc về tinh lọc ca từ / kỹ nghệ lời hát $\rightarrow$ điều hướng về **`references/lyric-refinement.md`**.
> - Khi triệu chứng thuộc về ngôn ngữ / âm thanh / thanh điệu $\rightarrow$ điều hướng về **`references/vietnamese-line-and-sound.md`**.
> - Khi bằng chứng chứng minh gốc rễ lỗi nằm ở Tứ hoặc kiến trúc bài $\rightarrow$ điều hướng về **`references/idea-and-structure.md`**.

---

## 1. Nguyên Tắc Tách Bạch Vai Trò & Kỷ Luật Bằng Chứng (Role Separation & Evidence Discipline)

```text
CREATIVE BRAIN (Tứ, Cốt, Hook, Cảm xúc) → WRITER (Viết rough pass mạch lạc, tự nhiên)
                                               ↓ (Chỉ kích hoạt khi có yêu cầu audit/review)
                                      [SIDECAR] REVIEWER (Soi triệu chứng, phân loại, điều hướng)
```

- **Reviewer là một Sidecar (Không nằm trên đường đi mặc định):** Reviewer chỉ được kích hoạt khi: (1) người dùng yêu cầu đánh giá, thẩm định hoặc phản biện (Audit / Critique / QA); hoặc (2) chạy formal audit trước release candidate. Tuyệt đối không tự động chèn vào giữa flow viết thông thường gây ức chế sáng tạo.
- **Không ngắt lời Writer:** Reviewer chỉ vào cuộc sau khi bản nháp hoặc section đã được viết trọn vẹn; định vị chính xác vị trí lỗi, không xóa bài để viết lại theo gu cá nhân.
- **Kích hoạt tối thiểu & Quy tắc dừng (Stop After 1–2 Issues):**
  - Reviewer **không tự động quét toàn bộ** các lăng kính hay checklist.
  - Reviewer: (1) soi xét artifact; (2) nhận diện triệu chứng có bằng chứng rõ nhất; (3) báo cáo tối đa **1–2 vấn đề ưu tiên cao nhất** theo mặc định; (4) điều hướng về canonical owner; (5) **DỪNG**.
  - Không bới thêm lỗi vụn vặt để làm dày bản review. Khi `CRITICAL = 0` và không có vấn đề `SUGGESTED` đáng kể: **kết luận PASS & STOP ngay lập tức**. Tuyệt đối không tự tạo việc ở nhóm OPTIONAL.
- **Kỷ luật bằng chứng âm thanh (Audio Evidence Discipline):**
  - Khi **chưa có audio thực tế / render**: Reviewer chỉ được nhận định rủi ro (`RISK`, `LIKELY`, `UNVERIFIED`); tuyệt đối không khẳng định *"độ ngân tự nhiên"*, *"điểm rơi vang"*, hay stress mismatch từ văn bản trần.
- **Ngôn ngữ thẩm định khách quan (Evidence-Aware, Not Self-Congratulatory):**
  - Không dùng từ tự khen vô căn cứ (*“hoàn hảo”*, *“tuyệt đối tự nhiên”*). Diễn đạt đúng thực tế bằng chứng: *“Không thấy lỗi đáng kể ở mức lyric-only...”*, *“Có risk nhẹ ở...”*, *“Chưa thể xác nhận điểm rơi nếu chưa có audio...”*.
- **Phân loại theo 3 cấp độ nghiêm trọng (Severity Classification):**
  - `CRITICAL`: Lỗi sinh tử bắt buộc sửa (Provenance Breach, Forced Rhyme Harm, hoặc Escalated Thesis Line phá vỡ section job).
  - `SUGGESTED`: Khuyến nghị nâng cấp (Thesis line mặc định, văn xuôi giải thích, camera sweep, dồn đạo cụ, sáo mòn, điểm rơi yếu...).
  - `OPTIONAL`: Lựa chọn trau chuốt thêm chỉ khi người dùng chủ động yêu cầu (tuyệt đối không tự động tạo việc khi không được yêu cầu).

---

## 2. Các Lăng Kính Thẩm Định Sẵn Có (The 6 Quality Lenses)

Sáu lăng kính dưới đây là **các góc nhìn thẩm định khi cần (available lenses), KHÔNG PHẢI quy trình 6 bước bắt buộc phải quét đủ**. Reviewer chỉ mở lăng kính tương ứng với bằng chứng quan sát được:

1. **Semantic Correctness:** Tính chính xác ngữ nghĩa, đúng Tứ, logic nhân vật và sự thật cảm xúc của section.
2. **Natural Vietnamese (Register-Relative):** Ca từ tự nhiên theo từng ngữ vực (`Mainstream Pop ≠ Folk ≠ Literary ≠ Cổ phong`); không lấy chuẩn khẩu ngữ pop thường ngày để gạt bỏ từ ngữ trang trọng trong không gian phù hợp.
3. **Emotional Credibility & Show vs. Tell Nuance:** Cảm xúc chân thực, hành động/hình ảnh tự bộc lộ.
   - **Bảo vệ câu cảm xúc trực diện (Direct Emotional Language):** Câu trực diện chân thành, đắt giá và đúng điểm rơi cảm xúc là ca từ có giá trị cao; tuyệt đối không tự động gắn mác lỗi "Tell" hay ép đổi thành ẩn dụ.
   - Ẩn dụ phục vụ cảm xúc trung tâm được **GIỮ LẠI (KEEP)**.
4. **Lyric Behavior / Singability (Lyric-Only):** Phân đoạn hơi thở khả dĩ, mật độ âm tiết, biên từ và điểm rơi. Số âm tiết chỉ là tín hiệu tham khảo, không phải bằng chứng lỗi hát.
5. **Image Necessity & Density:** Chi tiết có chức năng nâng đỡ cảm xúc hay chỉ là đạo cụ trang trí? Nhận diện và cắt tỉa camera sweep (dồn dập liệt kê nhiều vật thể mà thiếu payoff).
6. **Lexical / Writerly Naturalness:** Nhận diện cụm từ làm dáng (*staged / writerly*), nhân hóa làm màu. Triết lý: *Reduce ornament before adding ornament*.

*Tiêu chuẩn cốt lõi (Gỡ bỏ False Positives):* Hành vi đời thường, hội thoại tự nhiên hay việc không chứa từ cấm chưa đủ chứng minh chất lượng ca từ. Ca từ cần tạo được rung cảm thẩm mỹ, có nhịp thở âm nhạc và sức nặng vượt lên trên văn xuôi kể sự việc. Không bắt buộc phải trả lời mọi câu hỏi kiểm tra trên mọi lần review.

---

## 3. Cấu Trúc Báo Cáo Thẩm Định (Review Output Format)

Báo cáo thẩm định tuân thủ định dạng tinh gọn, báo cáo tối đa **1–2 vấn đề ưu tiên cao nhất**:

```text
- LOCATION:       [Section, Dòng X]
- SEVERITY:       [CRITICAL / SUGGESTED / OPTIONAL]
- SYMPTOM:        [Tên triệu chứng nhận diện được]
- EVIDENCE / WHY: [Bằng chứng câu từ cụ thể và lý do làm giảm chất lượng hoặc phẳng cảm xúc]
- ROUTE:          [Canonical owner / tài liệu tham chiếu chịu trách nhiệm sửa chữa phù hợp với triệu chứng]
- PATCH DIRECTION (Tùy chọn): [Tối đa 1 hướng sửa cục bộ ngắn gọn; chỉ khi hữu ích hoặc user yêu cầu; không phải cẩm nang dạy viết lại; không đưa 1–2 phương án viết lại chi tiết mặc định]
```
Reviewer nhận diện và báo cáo; việc sửa chi tiết thuộc thẩm quyền của Canonical Owner được điều hướng.

### Chế Độ Phản Biện Xuất Bản (Release Falsification Mode)

- **Kích hoạt:** Kích hoạt khi chạy formal audit trước release candidate hoặc chuẩn bị handoff ca từ mới/biên tập sâu sang đóng gói Suno. (Trong flow review/critique thông thường theo yêu cầu user, reviewer vẫn tuân thủ quy tắc dừng sau 1–2 vấn đề).
- **Mục tiêu phản biện (Adversarial Objective):** Không tìm kiếm sự xác nhận (confirmation bias) để tự khen; mục tiêu là tích cực tìm kiếm bằng chứng nhằm **BÁC BỎ (falsify)** tính sẵn sàng release của bản nháp.
- **4 bài test phản biện bắt buộc:**
  1. *Backstage Exposure Test:* Có dòng nào đọc to mô hình tâm lý hay cơ chế quan hệ không (kể cả thuyết minh bên ngoài hay **Analytical Self-Diagnosis ở ngôi thứ nhất**)? Cấm cho qua một cụm câu chỉ vì nó mang đại từ `anh/em`, giọng điệu tổn thương hay được gắn nhãn thú nhận (confession).
     - *Self-Diagnosis Strip Test:* Nếu gỡ bỏ đại từ xưng hô, sắc thái tổn thương và vỏ bọc thú nhận, cụm câu/đoạn có còn đọc giống một chuỗi tự chẩn đoán (`nguyên nhân → động cơ → phản xạ né tránh → dán nhãn lại → hậu quả`) không? Nếu CÓ, coi đó là bằng chứng Backstage Exposure.
     - *Ngưỡng chặn (Blocking threshold):* Đánh FAIL Lyric Readiness khi chuỗi tự chẩn đoán chiếm lĩnh hoặc phá vỡ nhiệm vụ cốt lõi của một section (nhất là Bridge/Chorus). Một câu bộc bạch nguyên nhân đơn lẻ, tức thời (*"Anh tiếc vì đã để em chờ"*) không cấu thành lỗi chặn.
  2. *Section Essay Test:* Có cả section (nhất là Chorus/Bridge) biến thành chuỗi mệnh đề phân tích, so sánh triết lý hoặc thuyết trình thay vì đẩy cảm xúc?
  3. *Semantic Escalation / Tứ Drift Test:* Có đoạn nào cố tạo cao trào bằng cách leo thang từ ngữ đao to búa lớn (*vũ trụ, định mệnh, mãi mãi...*) hoặc trôi xa khỏi Tứ cốt lõi?
  4. *Claim Falsification Test:* Cấm reviewer đưa ra nhận định tự kiểm tra suông không bằng chứng, và **cấm tuyệt đối biện minh kiểu "đây là lời thú nhận nên an toàn"**. Nếu tuyên bố *"không có Backstage Exposure đáng chặn"*, bắt buộc trích dẫn cụm câu nghi vấn nhất (kể cả lời thú nhận) và chứng minh bằng chứng đó là lời bộc bạch tức thời, không triển khai mô hình tự chẩn đoán, không dán nhãn cơ chế và không biến section thành bài phân tích.
- **Phán quyết xuất bản (Release Verdict):**
  - `LYRIC READINESS PASS` (vượt qua cả 4 bài test không có CRITICAL/SUGGESTED nghiêm trọng).
  - `LYRIC READINESS FAIL — refinement required` (kèm 1–2 bằng chứng cụ thể và điều hướng sửa chữa).
- **Báo cáo phản biện xuất bản tối giản:**
  ```text
  ### RELEASE FALSIFICATION REPORT
  - BACKSTAGE EXPOSURE:   [PASS / Bằng chứng dòng nghi vấn]
  - SECTION ESSAY:        [PASS / Bằng chứng dòng nghi vấn]
  - TỨ DRIFT / ESCALATION:[PASS / Bằng chứng dòng nghi vấn]
  - CLAIM INTEGRITY:      [PASS / Trích dẫn dòng kiểm chứng thực tế]
  - VERDICT:              [LYRIC READINESS PASS / LYRIC READINESS FAIL — refinement required]
  ```

---

## 4. Danh Mục Nhận Diện Triệu Chứng (Symptom Recognition)

### A. CRITICAL (Bắt buộc sửa)

1. **Provenance Breach (Vi phạm thẩm quyền trần thuật):** Người kể tự khẳng định chắc chắn về nội tâm, suy nghĩ thầm kín hoặc hành vi tương lai của người khác khi ngôi kể và dữ liệu brief không cho phép. $\rightarrow$ Route: **SKILL.md** (Writer Brake 4: Provenance & POV) cho vi phạm cục bộ; hoặc **references/idea-and-structure.md** nếu sai lệch toàn bộ ngôi kể / kiến trúc Tứ.
2. **Forced Rhyme Harm (Ép vần phá nghĩa):** Đảo cú pháp bất thường hoặc chọn từ ngữ xa lạ, ngô nghê chỉ để gieo vần với câu trên mà làm hỏng câu từ tự nhiên. $\rightarrow$ Route: `references/vietnamese-line-and-sound.md`.
3. **Escalated Thesis Line / Analysis Leakage:** Câu thuyết minh/giải thích **CHỈ LEO THANG THÀNH CRITICAL** khi có bằng chứng thực tế thỏa mãn ít nhất một trong 4 điều kiện: (1) Phá vỡ ý nghĩa trung tâm; (2) Phá vỡ nhiệm vụ cốt lõi của một section lớn như Chorus hoặc Bridge; (3) Gây ra vi phạm điểm nhìn / thẩm quyền trần thuật; HOẶC (4) Biến cả section thành bài nghị luận/thuyết minh nghiêm trọng làm hỏng hệ thống ca khúc. $\rightarrow$ Route: `references/lyric-refinement.md` (hoặc `references/idea-and-structure.md` nếu phá vỡ cấu trúc bài).

### B. SUGGESTED (Khuyến nghị nâng cấp)

1. **Thesis Line & Analysis Leakage (Mặc định):** Tác giả đứng ngoài phân tích triết lý, thuyết minh kết luận thay vì để hành động và cảm xúc tự lên tiếng. Các cụm *"hóa ra"*, *"thì ra"*, *"chỉ là"*, *"điều đau nhất là"* chỉ là detectors nhận diện điểm rơi nghi vấn; không tự động cấu thành lỗi và không phải từ cấm. $\rightarrow$ Route: `references/lyric-refinement.md`.
2. **SCENE-REPORT:** Nhiều dòng thuần túy ghi nhận cảnh vật, thời tiết, hoạt động thường nhật thiếu tải trọng cảm xúc; bỏ cảnh đi cảm xúc bài vẫn nguyên. $\rightarrow$ Route: `references/lyric-refinement.md`.
3. **PSYCHOLOGY-ESSAY:** Tác giả đứng ngoài phân tích tâm lý, đưa ra định nghĩa triết lý tổng quát (*"tình yêu là..."*, *"người ta thường..."*); Bridge giống bài phát biểu so sánh triết lý thay vì nhân vật cất lời. $\rightarrow$ Route: `references/lyric-refinement.md`.
4. **BIG-WORD-ESCALATION:** Cố tạo cao trào giả tạo ở Final Chorus bằng cách phóng đại kích cỡ từ ngữ (*vũ trụ, cuộc đời, mãi mãi, định mệnh*) mà không có tích lũy chiều sâu quan hệ. $\rightarrow$ Route: `references/lyric-refinement.md`.
5. **Show, Don't Explain & Over-Explanation:** Mô thức `hình ảnh/hành động + câu giải thích nghĩa thừa thãi` làm loãng dư ba thẩm mỹ. $\rightarrow$ Route: `references/lyric-refinement.md`.
6. **Semantic Redundancy:** Hai câu ở hai section kề nhau cùng thực hiện một nhiệm vụ ngữ nghĩa. $\rightarrow$ Route: `references/lyric-refinement.md`.
7. **Image Density & Camera Sweep:** Liệt kê dồn dập nhiều đạo cụ, địa điểm, vật thể thiếu payoff hoặc không cùng phục vụ một chức năng cảm xúc. $\rightarrow$ Route: `references/lyric-refinement.md`.
8. **Narrative-to-Lyric Failure:** Hoạt cảnh sitcom/tự sự lấn át; ca từ chỉ là chuỗi sự kiện đời thường chép lại mà thiếu tính nén nghệ thuật. $\rightarrow$ Route: `references/lyric-refinement.md`.
9. **Chorus / Bridge Anti-Essay:** Chorus biến thành chuỗi mệnh đề logic (*không X mà Y*); Bridge biến thành bài giảng triết lý thay vì bước ngoặt cảm xúc/thú nhận. $\rightarrow$ Route: `references/lyric-refinement.md`.
10. **Generic Emotional Language:** Câu cảm xúc chung chung có thể bê sang bất kỳ bài hát nào khác (*anh muốn em bình yên, tình yêu thật đẹp*). Tuyệt đối không cấm câu trực diện nếu có sức nặng riêng. $\rightarrow$ Route: `references/lyric-refinement.md`.
11. **Writerly / Staged Phrasing:** Cụm từ làm dáng văn vẻ, kết hợp từ lạ tai gượng gạo, nhân hóa làm màu phô diễn chữ. $\rightarrow$ Route: `references/vietnamese-line-and-sound.md`.
12. **Decorative Specificity:** Chi tiết cụ thể thiếu chức năng (không có provenance, không neo quan hệ, không tạo narrative turn). $\rightarrow$ Route: `references/lyric-refinement.md`.
13. **Prose-to-Lyric / Prose-AI-Tell:** Văn xuôi bẻ dòng, lạm dụng từ nối giải thích (*"để rồi", "thực ra", "bởi vì thế"*), nhịp điệu phẳng lỳ thiếu nhạc tính. $\rightarrow$ Route: `references/lyric-refinement.md`.
14. **Weak Line Landing:** Dòng trọng tâm của Chorus hoặc chốt đoạn kết thúc bằng từ chức năng lửng lơ (*"nữa đâu", "được gì"*). $\rightarrow$ Route: `references/vietnamese-line-and-sound.md`.
15. **Cliché & Cliché Escalation:** Cụm từ mòn vẹt (*con tim tan vỡ, định mệnh an bài*) hoặc chuỗi từ ngữ phóng đại sáo rỗng ở cao trào. $\rightarrow$ Route: `references/lyric-refinement.md`.
16. **Abstract Noun Stacking:** Xếp chồng quá nhiều danh từ trừu tượng (*tình yêu, hy vọng, ánh sáng, bình yên*) làm phím tắt cảm xúc thay vì chạm vào cảm giác thật. $\rightarrow$ Route: `references/lyric-refinement.md`.
17. **Over-Explained Metaphor:** Ẩn dụ vừa xuất hiện đã bị tác giả nhảy vào giải thích cặn kẽ ý nghĩa ở câu tiếp theo. $\rightarrow$ Route: `references/lyric-refinement.md`.
18. **Missing Idiosyncrasy:** Bài hát đúng kỹ thuật nhưng vắng bóng cách nói, thói quen ngầm hoặc góc nhìn riêng biệt của nhân vật. $\rightarrow$ Route: `references/lyric-refinement.md`.

### C. VIETNAMESE MUSIC-FIT & PROSODY (Advisory Diagnostics — Tham Vấn, Không Block Writer)

> **Nguyên tắc:** Reviewer không sở hữu quy trình sửa âm thanh hay thay thế LANGUAGE/SOUND. Chỉ ghi nhận rủi ro quan sát được trên văn bản và điều hướng xử lý:

1. **MOUTHFUL-LINE / AWKWARD-BREATH:** Dòng chứa quá nhiều phụ âm tắc liên tiếp trong tiết tấu nhanh, hoặc điểm ngắt dòng cắt đôi cụm từ tự nhiên. Lyric-only chỉ ghi nhận `RISK`. $\rightarrow$ Route: `references/vietnamese-line-and-sound.md`.
2. **STRESS-RISK:** Khi có melody / melodic contour / audio thực tế, Reviewer nhận diện rủi ro cấn thanh điệu / điểm rơi (`RISK`) dựa trên bằng chứng âm nhạc. Khi CHỈ CÓ văn bản lời (lyric-only) và chưa có melody/contour: độ tương thích thanh điệu - giai điệu là `UNVERIFIED / NOT ASSESSABLE`; tuyệt đối không tự suy đoán nốt cao trào hay đáy trầm từ văn bản trần. $\rightarrow$ Route: `references/vietnamese-line-and-sound.md`.
3. **SPOKEN-FORM-RISK:** Ca từ chứa số, từ ngoại lai đa âm tiết, viết tắt gây mơ hồ cách phát âm. Reviewer gợi ý ghi chú phát âm cho sản xuất/Suno mà không sửa văn bản nghệ thuật gốc. $\rightarrow$ Route: `references/vietnamese-spoken-form.md`.
4. **GENRE-MISMATCH:** Chỉ áp dụng khi soundscape/lane âm nhạc đã được xác nhận từ user/brief mà hành vi ca từ nghịch hướng hoàn toàn; không tự suy đoán genre để bắt lỗi. $\rightarrow$ Route: `references/genre-and-lyric-routing.md`.
5. **DENSITY-RISK:** Cảnh báo ngữ cảnh khi mật độ từ ngữ quá dày đặc làm bài thiếu khoảng thở. Không áp dụng ngưỡng đếm từ cố định (như "ballad 3.5 phút > 500 từ"); mật độ phụ thuộc vào thời lượng, groove, delivery và audio thực tế. $\rightarrow$ Route: `references/lyric-refinement.md`.

### D. OPTIONAL (Trau chuốt thêm — Chỉ khi người dùng chủ động yêu cầu)

Mục này **CHỈ ĐƯỢC XUẤT HIỆN** khi người dùng chủ động yêu cầu trau chuốt thêm (*extra polish / alternatives / refinement*) ngoài phạm vi kiểm định chất lượng:
- **Sonic Polish:** Gợi ý lặp nguyên âm mở, phụ âm đầu ở nốt ngân dự kiến.
- **Image Freshness:** Gợi ý thay thế một động từ quen thuộc bằng cử chỉ đời thường hơn.

*Quy tắc:* Nếu không có vấn đề CRITICAL hoặc SUGGESTED có ý nghĩa $\rightarrow$ kết luận **PASS & STOP** ngay lập tức; tuyệt đối không tự động đề xuất OPTIONAL chỉ vì bài viết đã tốt hay để làm dày bản review.
