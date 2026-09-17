# Quy Chuẩn Thẩm Định Độc Lập (Lyric Quality Review)

> **Mục đích:** Đóng vai trò chuyên gia thẩm định (Reviewer) độc lập, đánh giá chất lượng ca từ hoàn thiện nhằm phát hiện sáo rỗng (AI-slop), văn xuôi xuống dòng, thesis line và lỗi điểm rơi mà không làm gián đoạn dòng chảy của người viết (Writer).

---

## 1. Nguyên Tắc Tách Bạch Vai Trò (Writer / Reviewer Separation)

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
- **Thay thế điểm số bằng mức độ ưu tiên:** Bỏ các thang điểm cảm tính (7/10, 8/10). Báo cáo thẩm định phân loại theo 3 cấp độ:
  - `CRITICAL` (Bắt buộc sửa trước khi phát hành);
  - `SUGGESTED` (Khuyến nghị nâng cấp để bài sắc sảo hơn);
  - `OPTIONAL` (Lựa chọn trau chuốt thêm nếu muốn).
- **Điều kiện dừng thẩm định (Review Stop Condition):** Khi không còn lỗi `CRITICAL` và các điểm còn lại chỉ thuộc mức `OPTIONAL`, Reviewer kết luận `PASS` và khuyên người dùng giữ nguyên bản, tránh sửa quá đà (*over-polishing*) làm mất đi độ tươi của cảm xúc.

---

## 2. Sáu Lớp Thẩm Định Chất Lượng (The 6 Quality Lenses)

Khi thẩm định độc lập, reviewer soi xét ca từ qua 6 lăng kính độc lập:

1. **Semantic Correctness:** Tính chính xác của ngữ nghĩa, đúng Tứ, logic nhân vật và section jobs.
2. **Natural Vietnamese:** Cú pháp tiếng Việt tự nhiên, trật tự từ đời sống, không gượng ép.
3. **Emotional Credibility:** Độ tin cậy cảm xúc, đúng nhiệt độ (không làm nguội, không bi lụy hóa giả tạo).
4. **Lyric Behavior / Singability:** Tính nén của ca từ, phân đoạn hơi thở, nhịp điệu và điểm rơi có lực.
5. **Image Necessity:** Tính tất yếu của hình ảnh (chi tiết có chức năng đẩy chuyện/quan hệ hay chỉ là đạo cụ trang trí?).
6. **Lexical Naturalness:** Độ tự nhiên từ vựng (từ ngữ dung dị chân thật hay cố ý chọn chữ/làm dáng văn vẻ?).
   *(Lưu ý phân biệt: `Image Necessity ≠ Lexical Naturalness`)*

---

## 3. Cấu Trúc Báo Cáo Thẩm Định (Review Output Format)

Mỗi lỗi được phát hiện phải tuân thủ đúng 4 trường thông tin:

```text
- LOCATION: [Tên Section, Dòng số X]
- PROBLEM:  [Tên triệu chứng: Cliché / Thesis Line / Provenance / Forced Rhyme / Prose-to-Lyric / Weak Landing / Lexical Naturalness / Decorative Specificity / Sonic Polish / Image Freshness]
- WHY:      [Lý do tại sao dòng này làm giảm chất lượng hoặc phẳng cảm xúc]
- TARGETED FIX: [1–2 phương án sửa tại chỗ, giữ nguyên mạch của section]
```

---

## 4. Danh Mục Các Lỗi Trọng Tâm (Anti-Slop & Quality Checklist)

### A. CRITICAL (Bắt buộc sửa)
1. **Thesis Line & Analysis Leakage:**
   - Dòng mở đầu bằng *"hóa ra...", "điều đau nhất là...", "thì ra...", "chỉ là..."* hoặc câu kết luận giải thích triết lý của bài hát thay vì để hành động tự nói lên cảm xúc.
2. **Provenance Breach (Vi phạm thẩm quyền trần thuật):**
   - Người kể tự khẳng định như đinh đóng cột về nội tâm, suy nghĩ hoặc hành vi tương lai của người khác khi dữ liệu không cho phép.
3. **Forced Rhyme Harm (Ép vần phá nghĩa):**
   - Đảo cú pháp bất thường hoặc chọn một từ xa lạ, ngô nghê chỉ để bắt vần với câu trên.

### B. SUGGESTED (Khuyến nghị nâng cấp)
1. **Prose-to-Lyric (Văn xuôi xuống dòng):**
   - Câu đúng ngữ pháp nhưng chứa quá nhiều từ nối (*"nên", "vì", "thực ra là"*), nhịp điệu phẳng lỳ, thiếu tính nén của ca từ.
2. **Weak Line Landing (Điểm rơi cuối dòng lửng lơ):**
   - Dòng trọng tâm của Chorus hoặc chốt đoạn kết thúc bằng một từ chức năng (*"nữa đâu", "được gì", "thế này"*); cần chuyển trọng tâm về động từ, danh từ cảm xúc hoặc khoảng lặng.
3. **Cliché & Generic Tropes (Sáo mòn):**
   - Sử dụng các cụm từ mòn vẹt: *"con tim tan vỡ", "định mệnh an bài", "nước mắt tuôn rơi", "yêu đến điên dại", "thanh xuân của anh"*; hoặc mặc định gọi mưa/mùa đông/hoàng hôn làm công cụ tạo buồn vô cớ.
4. **Lexical Naturalness / Decorative Specificity (Độ tự nhiên từ vựng vs. Chi tiết trang trí):**
   - **Bản chất (Soft Lens — lăng kính mềm, không phải luật cứng):**
     - *Chi tiết / từ ngữ đó có sai không?* $\rightarrow$ **Không.** (Đúng cú pháp, không lỗi vần, tả thực chính xác).
     - *Nó có thực sự cần thiết không?* $\rightarrow$ Xem xét qua **Provenance** (brief có đưa vào không) và **Material Necessity** (chi tiết đó có làm việc gì cho Tứ, cảm xúc hay hành động không, hay chỉ được ném vào để tỏ ra "cụ thể/văn vẻ"?).
     - *Nếu không cần thiết:* $\rightarrow$ Thử cách gọi tự nhiên, mộc mạc và chân thật hơn của đời sống thường nhật (ví dụ: *“sân gạch” $\rightarrow$ “sân nhà”*). Tuyệt đối không thay bằng một từ ước lệ hoa mỹ khác (*“thềm xưa”, “gạch rêu”*).
     - *Nếu cần thiết:* $\rightarrow$ (Nếu có lai lịch từ đề bài, hoặc chất liệu gạch mang tính va đập/đối thoại với cảm xúc) $\rightarrow$ Giữ nguyên *“sân gạch”*.
5. **Lexical Pretentiousness / Over-Writerly (Làm dáng từ vựng):**
   - Dùng từ ngữ hoa mỹ ước lệ để cố gắng "thơ hơn" (*"thềm xưa", "tiếng tơ", "mộng tàn"*...) trong khi một cách nói chân thật sẽ truyền cảm hơn nhiều.

### C. OPTIONAL (Trau chuốt thêm)
1. **Sonic Polish:**
   - Thêm echo phụ âm đầu, lặp nguyên âm vang ở nốt ngân để tăng độ bắt tai.
2. **Image Freshness:**
   - Thay một động từ quen thuộc bằng một động từ mang tính vật lý/cử chỉ đời thường hơn.

