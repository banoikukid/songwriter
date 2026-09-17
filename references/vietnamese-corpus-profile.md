# Vietnamese Corpus Profile: Thống Kê Quần Thể & Độ Lệch Nhạc Việt

> **Nguồn nghiên cứu tham chiếu:** Dataset VietLyrics (*BatmanofZuhandArrgh/VietLyrics* - Nghiên cứu Automatic Lyrics Transcription cho âm nhạc Việt Nam).  
> **Quy mô khảo sát:** 647.1 giờ âm thanh; 8,440 ca khúc có phiên âm từng dòng; hơn 4,000 nghệ sĩ độc lập; trường metadata gồm: *song, title, genre, artist, token_count, wpm, duration_mins, songwriter attribution*.  
> 
> **NGUYÊN TẮC BẤT BIẾN:**  
> Dữ liệu thống kê quần thể chỉ dùng làm **Ưu tiên mềm (Soft Prior) & Kiểm tra độ hợp lý (Sanity Check)**.  
> Tuyệt đối **KHÔNG** dùng để tạo ra một *"bài hát trung bình mẫu"* (Average-Song Generator).  
> Tuyệt đối **KHÔNG** ép mọi ca khúc phải đạt đúng số phút hoặc số chữ trung bình.  
> Tuyệt đối **KHÔNG** nhúng kho lời bài hát bản quyền vào runtime của skill.

---

## 1. Các Chỉ Số Quần Thể Cơ Bản (Corpus Baseline Observations)

| Chỉ số (Metric) | Giá trị trung bình quan sát (Observed Average) | Dải phân bố phổ biến (Common Range) | Ý nghĩa thực hành cho Songwriter (Practical Implication) |
|---|---|---|---|
| **Thời lượng ca khúc (Duration)** | **~4.6 phút** (4 phút 36 giây) | **3.2 – 5.5 phút** | Nhạc Việt truyền thống và ballad thường có thời lượng tự sự dài hơn chuẩn streaming phương Tây (2.5 – 3 phút). Không cần cắt gọt cơ học nếu cảm xúc cần không gian phát triển. |
| **Tốc độ hát (Singing Speed)** | **~90.1 WPM** (Từ/phút) | **65 – 125 WPM** | Tốc độ hát trung bình tiếng Việt chậm hơn đáng kể so với tốc độ nói thông thường (160–200 WPM). Điều này phản ánh độ ngân của nguyên âm và độ luyến của thanh điệu. |
| **Dung lượng từ ngữ (Token Count)** | **~350 – 450 từ/bài** (Ballad/Pop) | **180 – 700+ từ** | Các bài tự sự (Bolero, Rap, Storytelling Ballad) có mật độ từ cao hơn; các bài Dance/EDM/Indie-wash có dung lượng từ tối giản. |

---

## 2. Heuristic Mối Quan Hệ: Thời Lượng ↔ Số Từ ↔ Mật Độ Hát

Sử dụng tam giác tương quan làm thước đo sanity check khi thiết kế form hoặc thẩm định độ dày ca từ:

$$\text{Tốc độ hát ước tính (WPM)} \approx \frac{\text{Tổng số từ trong lời}}{\text{Thời lượng hát thực tế (phút)}}$$

### Bảng đối chiếu mật độ nhả chữ theo thể loại:

```text
DENSE (Dày chữ - 110–140 WPM):
→ Rap Việt, Melodic Hip-hop, Pop-Rock nhanh, R&B dồn chữ.
→ Cần: câu từ gãy gọn, nhiều phụ âm nảy, hạn chế luyến láy phức tạp.

MODERATE (Vừa phải - 80–105 WPM):
→ Modern V-Pop, R&B Soul, Acoustic Pop, Nhạc Trữ tình quê hương.
→ Cần: cân bằng giữa câu tự sự và câu ngân nga giai điệu.

SPACIOUS (Thoáng chữ - 60–80 WPM):
→ Emotional Ballad chậm, Bolero hoài niệm, Dream Pop, Ambient / Folktronica.
→ Cần: từ ngữ giàu nguyên âm mở, khoảng nghỉ rộng cho dàn nhạc và hơi thở.
```

> [!TIP]
> **Dấu hiệu cảnh báo mật độ (`DENSITY-RISK`):**  
> Nếu một bài Ballad được dự kiến dài 3.5 phút nhưng chứa đến hơn 550 từ mà không có đoạn rap hay recitation $\rightarrow$ Ca từ đang có nguy cơ quá dày, ca sĩ hoặc AI engine sẽ phải hát vội, nuốt chữ hoặc mất khoảng thở cảm xúc.

---

## 3. Các Giới Hạn & Độ Lệch Của Dữ Liệu (Corpus Caveats & Biases)

Từ các phát hiện học thuật của nghiên cứu VietLyrics, hệ thống ghi nhận các cảnh báo sau:

### A. Sự bất tương thích của hệ thống phân loại phương Tây (Western Genre Ontology Mismatch)
- Nghiên cứu chỉ ra rằng việc ánh xạ các thể loại âm nhạc Việt Nam (từ ZingMP3 / nền tảng nội địa) sang 50 nhãn thể loại chuẩn phương Tây (MagnaTagATune) đạt độ tin cậy rất thấp.
- Âm nhạc Việt Nam có những dòng chảy đặc thù không thể nhét vừa vào khuôn khổ phương Tây: *Bolero Việt Nam, Nhạc Vàng, Ca khúc Trữ tình quê hương, Hát ru, Nhạc Trẻ biến thể...*
- **Hành động của Skill:** Luôn sử dụng **Vietnamese Genre DNA** (hệ thống lane nhạc Việt bản địa) thay vì cố ép qua lăng kính thể loại phương Tây.

### B. Phương ngữ & Vùng miền: Nhãn tham khảo, không phải sự thật tuyệt đối (Dialect Caveats)
- Các mô hình phân loại phương ngữ tự động (Bắc / Trung / Nam) trong các nghiên cứu thường chịu sự thiên lệch dữ liệu (dataset skew) và sai số nhận dạng.
- Nhiều ca khúc viết bằng từ ngữ phổ thông nhưng được thể hiện bởi nghệ sĩ miền Nam hoặc miền Trung, và ngược lại.
- **Hành động của Skill:**
  - Coi nhãn phương ngữ là thuộc tính phong cách tùy chọn (`optional stylistic flavor`), không coi là chân lý cố định.
  - Tuyệt đối **không tự tiện gán giọng Bắc/Trung/Nam** cho một ca khúc chỉ dựa trên tựa đề hoặc một vài từ vựng lẻ tẻ.

### C. Dữ liệu tác giả & Nghệ sĩ (Author / Artist Metadata)
- Thông tin tác giả và nghệ sĩ trong corpus được dùng cho mục đích:
  1. Nghiên cứu phong cách và thói quen nhả chữ;
  2. Phân tầng đánh giá chất lượng (stratified evaluation);
  3. Đối chiếu xu hướng thể loại qua các thời kỳ.
- Tuyệt đối **không dùng để sao chép ý tưởng, câu chữ hay phong cách độc quyền** của bất kỳ cá nhân nghệ sĩ nào vào bài viết mới.

---

## 4. Ứng Dụng Trong Quy Trình Sáng Tác (Runtime Integration)

1. **Khi nhận Open Brief:** Không nạp bảng Corpus Profile. Giữ Writer hoàn toàn tự do với Tứ và cảm xúc.
2. **Khi Thẩm Định Ca Từ (Reviewer Check):** Đối chiếu tổng số dòng và dung lượng từ với lane nhạc dự kiến:
   - Bài ballad quá nhiều chữ $\rightarrow$ nhắc nhở tinh gọn để tạo chỗ thở.
   - Bài dance quá dài dòng $\rightarrow$ nhắc nhở nén lại cho bắt nhịp groove.
3. **Khi Nghiên Cứu Benchmark:** Dùng phân bố WPM và duration làm ngưỡng tham chiếu khoa học để đánh giá tính khả thi trong thực tế biểu diễn.
