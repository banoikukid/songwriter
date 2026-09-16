# Songwriting-Min (Songwriter Skill)

> **Writer-First Vietnamese Songwriting Skill for AI & Human Cowriting.**  
> Sáng tác, sửa và hoàn thiện ca khúc tiếng Việt từ title/lời, Tứ, melody, groove/track, chord/harmony, brief hoặc bản nháp thô.

---

## 🌟 Triết Lý Cốt Lõi (Writer-First Principles)

1. **Sáng tác bằng tai, cảm xúc và mạch:** Runtime mặc định phải đủ nhẹ để người viết còn viết; bộ kiểm tra chuyên sâu chỉ được gọi khi bản nháp bộc lộ đúng triệu chứng.
2. **Nghĩa > Vần (Meaning Over Rhyme):** Ưu tiên tiếng Việt tự nhiên, cảm xúc chân thực và tính tất yếu của hình ảnh (provenance) hơn là ép gieo vần gượng gạo.
3. **Chốt Central Intent:** Lời, melody, harmony, rhythm và form cùng phục vụ một cảm xúc và một thông điệp cốt lõi.
4. **Chọn đúng Engine phát triển:**
   - *Kể / Chuyển hóa (Narrative / Transformation)*
   - *Tuyên ngôn / Khuếch đại (Anthem / Amplification)*
   - *Trạng thái / Duy trì (Atmospheric / State-Holding)*
5. **Viết rough pass liền mạch:** Hoàn thành trọn vẹn bản nháp thô trước khi micro-audit; nghe/đọc lại thành tiếng rồi mới chẩn bệnh.
6. **Suno & AI Music Handoff thực tế:** Lyrics-only không tự biết melody; Suno không deterministic. Demo rẻ dùng để kiểm lời–nhạc trước full production.
7. **Tai người quyết định cuối cùng:** AI là bạn đồng sáng tác (cowriter); tai người quyết định điểm “chạm”, độ “tươi” và bản hoàn thiện cuối cùng. Không hứa tự tạo hit hay siêu phẩm.

---

## 🚀 Quy Trình Vận Hành 8 Bước

```
                       User Brief / Seed / Melody / Chord
                                      │
                                      ▼
             [1] Chốt Central Intent & Music Frame (Genre, Voice, Goal)
                                      │
                                      ▼
             [2] Chọn Seed, Tứ & Working Hook (1 vòng cô đọng)
                                      │
                                      ▼
             [3] Dựng Form, Section Jobs & Phrase Behavior
                                      │
                                      ▼
             [4] Viết Rough Pass Liền Mạch (Đọc/hát lại thành tiếng)
                                      │
                                      ▼
             [5] ROUGH-LYRIC SEMANTIC GATE (Chẩn bệnh & hồi phục tầng sai)
                                      │
                                      ▼
             [6] SCOPE-A RELEASE GATE (Kiểm tra trước khi handoff)
                                      │
                                      ▼
             [7] Suno / AI Prototype Handoff ([SUNO PROTOTYPE-READY])
                                      │
                                      ▼
             [8] Human Ear Audition & Final Production Refinement
```

---

## 📂 Cấu Trúc Thư Mục Repository

```
songwriter/
├── README.md                              # Giới thiệu tổng quan & hướng dẫn sử dụng
├── SKILL.md                               # Entry point, 8 bước sáng tác, lane chọn, gates & checklist
├── MANIFEST.md                            # Danh mục tài liệu tham chiếu & scripts
├── scripts/
│   ├── lyric_static_check.py              # Kiểm tra độ dài dòng, trùng từ cuối, dòng lặp
│   └── clean_context_eval.py              # Bộ test context và eval suite ca từ
└── references/
    ├── idea-and-structure.md              # Khung ý tưởng, Tứ, Form, Hook, Chế độ phá cách
    ├── vietnamese-line-and-sound.md       # Âm thanh, thanh điệu tiếng Việt, nhịp điệu & vần
    ├── stage-validation-loop.md           # Các cổng kiểm định ngữ nghĩa (Semantic Gate)
    ├── suno-handoff.md                    # Quy chuẩn đóng gói prompt & tag cho Suno AI
    ├── music-sketch-and-demo.md           # Hướng dẫn dựng demo và kiểm tra nhạc-lời
    ├── genre-and-lyric-routing.md         # Định tuyến ca từ theo thể loại âm nhạc
    ├── folk-prosody.md                    # Thơ dân gian, lục bát và biến thể vào ca khúc
    ├── poem-to-song.md                    # Phương pháp phổ thơ thành ca khúc
    ├── style-mining.md                    # Khai thác phong cách tác giả & bản sắc riêng
    ├── dominant-analysis.md               # Phân tích hợp âm, hòa thanh & trục cảm xúc
    ├── case-log.md                        # Nhật ký các case thực chiến
    ├── audit-and-evaluation.md            # Phương pháp tự chấm điểm và đánh giá ca khúc
    └── *.json & *.md                      # Schemas kiểm định, test suites & báo cáo audit
```

---

## 🛠️ Công Cụ Kiểm Tra Hỗ Trợ (Scripts)

### 1. Kiểm tra tĩnh ca từ (`lyric_static_check.py`)
Kiểm tra độ dài dòng, trùng từ cuối liền kề và phát hiện dòng lặp tự động:
```bash
python scripts/lyric_static_check.py path/to/lyric.txt
```

### 2. Chạy bộ kiểm thử ngữ cảnh sạch (`clean_context_eval.py`)
```bash
python scripts/clean_context_eval.py
```

---

## 🏷️ Quy Chuẩn Nhãn Trạng Thái (Status Tags)

- `[SUNO PROTOTYPE-READY — Scope A PASS; music-fit UNKNOWN]`: Bản lời đã qua Semantic Gate và Scope A, sẵn sàng nạp vào Suno để test giai điệu/phối khí.
- `[LYRIC DRAFT — Scope A chưa qua; music-fit UNKNOWN]`: Bản nháp đang trong quá trình hiệu chỉnh, cần sửa ở tầng chỉ định trước khi demo.

---

## 📄 Bản Quyền & Tác Quyền

Phát triển phục vụ cộng đồng nhạc sĩ, nhà sản xuất và người sáng tạo nội dung ca khúc tiếng Việt.
