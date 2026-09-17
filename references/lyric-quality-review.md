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

## 2. Cấu Trúc Báo Cáo Thẩm Định (Review Output Format)

Mỗi lỗi được phát hiện phải tuân thủ đúng 4 trường thông tin:

```text
- LOCATION: [Tên Section, Dòng số X]
- PROBLEM:  [Tên triệu chứng: Cliché / Thesis Line / Prose / Weak Landing / Forced Rhyme]
- WHY:      [Lý do tại sao dòng này làm giảm chất lượng hoặc phẳng cảm xúc]
- TARGETED FIX: [1–2 phương án sửa tại chỗ, giữ nguyên mạch của section]
```

---

## 3. Danh Mục Các Lỗi Trọng Tâm (Anti-Slop & Quality Checklist)

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

### C. OPTIONAL (Trau chuốt thêm)
1. **Sonic Polish:**
   - Thêm echo phụ âm đầu, lặp nguyên âm vang ở nốt ngân để tăng độ bắt tai.
2. **Image Freshness:**
   - Thay một động từ quen thuộc bằng một động từ mang tính vật lý/cử chỉ đời thường hơn.
