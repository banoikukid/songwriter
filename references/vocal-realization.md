# Hiện Thực Hóa Giọng Hát (Vocal Realization Protocol)

> **Mục đích:** Định hướng bản sắc, phong cách trình diễn và xử lý ngữ âm cho giọng hát tiếng Việt trong ca khúc và môi trường AI Audio (Suno), đảm bảo giọng hát truyền cảm, rõ chữ và không bị biến dạng.

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
Thuộc tính cố định của người hát, đưa vào phần **STYLE PROMPT** của Suno:
- **Giới tính & Độ tuổi:** `male vocal`, `female vocal`, `youthful tenor`, `mature warm alto`, `deep baritone`.
- **Màu sắc âm sắc (Timbre):** `airy`, `raspy`, `smoky`, `husky`, `silky`, `clear`, `resonant`, `breathy`.
- **Bản sắc văn hóa / Vùng miền:** `Vietnamese contemporary pop vocal`, `indie folk singer-songwriter tone`.

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

## 2. Ngữ Âm Tiếng Việt Cho Giọng Hát (Vietnamese Vocal Prosody)

Tiếng Việt là ngôn ngữ đơn âm và có 6 thanh điệu. Một từ hoàn hảo về mặt ngữ nghĩa vẫn có thể là thảm họa khi hát nếu không xét đến ngữ âm học:

### A. Phù Hợp Điểm Ngân (Long-Note & Sustain Suitability)
- **Ưu tiên nguyên âm mở (Open Vowels):** Các nguyên âm rộng như `a`, `o`, `ơ`, `e` (*hoa, xa, mơ, nghe, chờ*) cho phép cột hơi duy trì tự nhiên, âm vang tròn trịa ở các nốt ngân của Chorus/Payoff.
- **Thận trọng với nguyên âm khép (Close Vowels):** Các âm như `i`, `u`, `ư` (*khi, đi, thu, từ*) cần khẩu hình hẹp; khi ngân nốt cao dễ bị bí hoặc gắt tiếng nếu ca sĩ ảo thiếu kỹ thuật.
- **Khóa âm tắc đuôi (Checked-Coda Trap):** Các từ kết thúc bằng phụ âm tắc vô thanh `-p`, `-t`, `-c`, `-ch` (*mắt, khóc, một, kết, thắt*) đóng luồng hơi ngay lập tức.
  - **Quy tắc:** Tuyệt đối tránh đặt âm tắc đuôi vào nốt ngân dài chính của Chorus/Hook trừ khi chủ ý tạo nhịp ngắt giật (staccato) sắc nhọn.
  - **Sửa nhanh:** Đảo cú pháp để đưa từ mang nguyên âm mở/âm vang mũi (`-m`, `-n`, `-ng`) về cuối dòng.

### B. Kiểm Soát Luyến Láy (Melisma & Run Restraint)
- Trong tiếng Việt, luyến láy quá nhiều nốt trên một từ (`melisma`) rất dễ làm **bẻ gãy thanh điệu**, khiến người nghe nghe nhầm nghĩa (*ví dụ: "yêu" luyến nốt thấp thành "yểu" hoặc "yếu"*).
- **Quy định:** Mặc định yêu cầu `clean articulation`, `minimal runs/melisma`. Chỉ cho phép luyến nhẹ ở các từ thanh bằng (ngang, huyền) không có phụ âm tắc.

### C. Nhóm Hơi & Biên Từ (Breath Grouping & Word Boundaries)
- Không ngắt hơi giữa các từ ghép cố định (*"hạnh - [lấy hơi] - phúc"* là lỗi nghiêm trọng).
- Một cụm câu hát chuẩn phải hoàn tất trong một hơi thở tự nhiên (`One-Breath Rule`). Nếu câu quá 11–13 âm tiết mà không có dấu nghỉ tự nhiên, câu sẽ bị ca sĩ ảo dồn chữ hoặc nuốt âm.

---

## 3. Bảng Định Hướng Giọng Hát Mẫu (Vocal Archetypes)

| Phong cách ca khúc | Tầng 1: Identity | Tầng 2: Performance | Tầng 3: Production |
|---|---|---|---|
| **Indie / Ballad Tự Sự** | `Vietnamese female vocal, breathy warm alto` | `intimate whispered Verse, emotional chest voice Pre-Chorus, restrained fragile falsetto Chorus` | `dry up-front lead, subtle acoustic room reverb` |
| **RnB / Chill Pop** | `Male vocal, silky smooth tenor` | `laid-back groove, conversational delivery, tight phrase endings, subtle head voice ad-libs` | `warm compression, close-mic, soft octave doubles` |
| **Anthemic / Pop Rock** | `Female vocal, powerful raspy chest-mix` | `building energy, dynamic delivery, resonant belt on chorus climax` | `wide stereo backing vocals, plate reverb, subtle saturation` |
| **Cổ Phong / Dân Gian Đương Đại** | `Female vocal, clear ethereal soprano` | `gentle traditional ornamentation, airy delivery, delicate legato` | `spacious hall reverb, distant airy vocal echoes` |
