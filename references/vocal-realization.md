# Hiện Thực Hóa Giọng Hát (Vocal Realization Protocol)

> **Mục đích:** Định hướng bản sắc, phong cách trình diễn và xử lý tương thích giữa ca từ và giọng hát tiếng Việt (Vocal Affordance) trong ca khúc và môi trường AI Audio (Suno), đảm bảo giọng hát truyền cảm, rõ chữ và không bị biến dạng.

---

## 1. Phân Tách Ba Tầng Giọng Hát (The Three Vocal Layers)

Tuyệt đối không gộp toàn bộ mô tả giọng vào một cụm prompt duy nhất. Tách biệt rõ ràng 3 tầng quyết định:

```
                      VOCAL REALIZATION
                              │
     ┌────────────────────────┼────────────────────────┐
     ▼                        ▼                        ▼
[1] VOCAL IDENTITY      [2] VOCAL PERFORMANCE    [3] VOCAL PRODUCTION
(Bản sắc cốt lõi)       (Cách xử lý biểu cảm)    (Không gian & Hiệu ứng)
```

### Tầng 1: VOCAL IDENTITY (Bản sắc & Màu giọng cốt lõi)
Thuộc tính sinh học/âm sắc cố định của người hát, đưa vào phần **STYLE PROMPT**:
- **Giới tính & Độ tuổi:** `male vocal`, `female vocal`, `youthful tenor`, `mature warm alto`, `deep baritone`.
- **Màu sắc âm sắc (Timbre):** `airy`, `raspy`, `smoky`, `husky`, `silky`, `clear`, `resonant`, `breathy`.
- **Bản sắc văn hóa:** `Vietnamese contemporary pop vocal`, `indie folk singer-songwriter tone`.

### Tầng 2: VOCAL PERFORMANCE (Phong cách trình diễn theo Section)
Cách ca sĩ diễn đạt cảm xúc theo chuyển động của từng đoạn, thể hiện qua **SECTION CUES** hoặc nhịp ca từ:
- **Cường độ & Lực hát:** `soft whispered`, `intimate delivery`, `restrained confession`, `conversational`, `passionate belt`, `soaring vocals`.
- **Vùng cất giọng (Register):** `chest voice`, `mixed voice`, `head voice`, `falsetto`.
- **Kỹ thuật luyến láy & Ngân rung:** `controlled subtle vibrato`, `straight-tone`, `minimal melisma`, `clean phrase endings`.

### Tầng 3: VOCAL PRODUCTION (Không gian & Hiệu ứng phòng thu)
Cách giọng hát được đặt trong bản phối, đưa vào **STYLE** hoặc **CUES** chuyên biệt:
- **Vị trí không gian:** `intimate dry up-front vocal`, `distant ethereal vocal`, `wide stereo vocals`.
- **Lớp bè & Độ dày:** `subtle vocal doubles`, `whisper track layer`, `octave-lower double`, `lush choir harmonies`, `sparse backing vocals`.
- **Hiệu ứng:** `warm plate reverb`, `tape slapback delay`, `lo-fi telephone filter`.

---

## 2. Giao Diện Ca Từ ↔ Khả Năng Giọng Hát (Lyric Line → Vocal Affordance)

Mô tả vocal chỉ có giá trị khi nó bám chặt vào cấu trúc dòng ca từ. Khi chẩn đoán hoặc thiết kế câu đinh (Hook / Climax), agent xem xét tương quan:

```text
DÒNG CA TỪ: "Ngỡ bên người qua nghìn năm mộng cũ"
    │
    ├── Số âm tiết: 8 (gọn trong một nhịp thở tự nhiên)
    ├── Chữ chốt nghĩa (Semantic Landing Word): "cũ"
    │     ├── Loại âm: Nguyên âm bán khép, dấu ngã (falling-rising)
    │     ├── Chỉ dấu rủi ro (Risk Indicator): High melisma risk nếu ngân dài qua nhiều cao độ
    │     └── Hướng xử lý: Phát âm dứt khoát hoặc lướt nhẹ, tránh uốn nốt phức tạp làm lệch dấu
    └── Điểm lấy hơi (Breath Group): [Ngỡ bên người] / [qua nghìn năm mộng cũ]
```

- **Phân biệt Semantic Landing vs Transit Words:**
  - *Semantic Landing Word:* Từ mang trọng lực ý nghĩa và cảm xúc chính của dòng. Cần nằm ở vị trí nốt có điểm rơi tự nhiên của giai điệu (downbeat hoặc điểm giải phóng năng lượng).
  - *Transit/Filler Words:* Các từ nối, trợ từ. Không đặt nốt cao hoặc ngân dài vào các từ này.

---

## 3. Ngữ Âm Tiếng Việt Cho Giọng Hát (Vietnamese Vocal Prosody — Ràng Buộc Mềm)

> **Thứ bậc ưu tiên:**  
> `Ý nghĩa (Meaning) > Tiếng Việt tự nhiên (Natural Vietnamese) > Tính ca hát (Singability) > Vần (Rhyme) > Tối ưu hóa thanh học (Phonetic optimization)`.  
> *Quy tắc thanh học chỉ là ràng buộc mềm hỗ trợ; không bao giờ được phép làm méo nghĩa hay gượng cú pháp.*

### A. Phù Hợp Điểm Ngân (Long-Note & Sustain Suitability)
- **Nguyên âm mở (Open Vowels):** Các nguyên âm rộng như `a`, `o`, `ơ`, `e` (*hoa, xa, mơ, nghe, chờ*) cho phép cột hơi duy trì tự nhiên, âm vang tròn trịa ở các nốt ngân cao trào của Chorus.
- **Nguyên âm khép (Close Vowels):** Các âm như `i`, `u`, `ư` (*khi, đi, thu, từ*) cần khẩu hình hẹp; khi ngân nốt rất cao dễ bị bí tiếng nếu thiếu kỹ thuật. Tuy nhiên nếu từ ngữ đó tự nhiên và đúng nghĩa nhất, vẫn giữ nguyên.
- **Âm tắc đuôi (Checked-Coda `-p, -t, -c, -ch`):**
  - **Không phải lỗi mặc định:** Âm tắc đuôi (*mắt, khóc, một, kết, thắt*) đóng luồng hơi ngay lập tức. Đây là công cụ cực kỳ đắt giá khi muốn tạo hiệu ứng dứt khoát (*staccato*), kìm nén, nhát cắt dứt khoát hoặc nhịp điệu mạnh mẽ.
  - **Chỉ xử lý khi:** Section job yêu cầu một nốt ngân dài mênh mang (*soaring sustain*) mà từ kết dòng lại bị khóa cụt bởi âm tắc, gây cảm giác hụt hơi khó chịu trên tai nghe. Lúc đó mới xem xét hoán đổi cú pháp hoặc chọn từ đồng nghĩa mở.

### B. Kiểm Soát Luyến Láy (Melisma & Run Restraint)
- Trong tiếng Việt, luyến láy quá nhiều nốt trên một âm tiết (`melisma`) rất dễ làm **bẻ gãy thanh điệu**, khiến người nghe hiểu sai nghĩa (*ví dụ: "yêu" luyến nốt thấp thành "yểu" hoặc "yếu"*).
- **Khuyến nghị âm học:** Mặc định ưu tiên `clean articulation`, `minimal runs/melisma`. Hạn chế luyến phức tạp trên các từ mang thanh trắc gãy (hỏi, ngã, nặng); nếu muốn phô diễn kỹ thuật luyến (runs), ưu tiên đặt vào các từ thanh bằng (ngang, huyền) có âm vị mở để tránh bẻ gãy ngữ nghĩa.

### C. Nhóm Hơi & Biên Từ (Breath Grouping & Word Boundaries)
- Không ngắt hơi giữa các từ ghép cố định (*"hạnh - [lấy hơi] - phúc"* là lỗi nghiêm trọng).
- **Chỉ dẫn phân đoạn hơi thở (One-Breath Guideline):** Một phrase hát tự nhiên thường thoải mái trong khoảng 6–10 âm tiết tùy tempo và thể loại. Nếu câu dài hơn, cần bố trí biên từ và dấu ngắt hợp lý để người hát hoặc AI không bị dồn hơi, nuốt âm ở cuối dòng.

---

## 4. Bảng Định Hướng Giọng Hát Mẫu (Vocal Archetypes)

| Phong cách ca khúc | Tầng 1: Identity | Tầng 2: Performance | Tầng 3: Production |
|---|---|---|---|
| **Indie / Ballad Tự Sự** | `Vietnamese female vocal, breathy warm alto` | `intimate whispered Verse, emotional chest voice Pre-Chorus, restrained fragile falsetto Chorus` | `dry up-front lead, subtle acoustic room reverb` |
| **RnB / Chill Pop** | `Male vocal, silky smooth tenor` | `laid-back groove, conversational delivery, tight phrase endings, subtle head voice ad-libs` | `warm compression, close-mic, soft octave doubles` |
| **Anthemic / Pop Rock** | `Female vocal, powerful raspy chest-mix` | `building energy, dynamic delivery, resonant belt on chorus climax` | `wide stereo backing vocals, plate reverb, subtle saturation` |
| **Cổ Phong / Dân Gian Đương Đại** | `Female vocal, clear ethereal soprano` | `gentle traditional ornamentation, airy delivery, delicate legato` | `spacious hall reverb, distant airy vocal echoes` |
