# Songwriting-Min (Songwriter Skill)

> **Writer-First Vietnamese Songwriting Skill for AI & Human Cowriting.**  
> Sáng tác, sửa và hoàn thiện ca khúc tiếng Việt từ title/lời, Tứ, melody, groove/track, chord/harmony, brief hoặc bản nháp thô.

---

## 🌟 Triết Lý Cốt Lõi (Writer-First Principles)

1. **Sáng tác bằng tai, cảm xúc và mạch:** Runtime mặc định phải đủ nhẹ để người viết còn viết; bộ kiểm tra chuyên sâu chỉ được gọi khi bản nháp bộc lộ đúng triệu chứng.
2. **Nghĩa > Vần (Meaning Over Rhyme):** Ưu tiên tiếng Việt tự nhiên, cảm xúc chân thực và tính tất yếu của hình ảnh (provenance) hơn là ép gieo vần gượng gạo.
3. **Chốt Central Intent linh hoạt:** Lời, melody, harmony, rhythm và form cùng phục vụ một cảm xúc và một thông điệp cốt lõi, nhưng có thể tinh chỉnh sau khi nghe câu hát thực tế.
4. **Chọn đúng Engine phát triển:**
   - *Kể / Chuyển hóa (Narrative / Transformation)*
   - *Tuyên ngôn / Khuếch đại (Anthem / Amplification)*
   - *Trạng thái / Duy trì (Atmospheric / State-Holding)*
5. **Flow khám phá thích nghi & Pilot Proofing (Adaptive Discovery Flow):** Chọn pilot ở nơi cần chứng minh nhất (Chorus cho declaration; Verse mở + turn cho narrative; quãng liền 8–12 dòng cho constellation; phrase khó cho melody-first). Đọc/hát pilot như người nghe trước khi viết trọn bài.
6. **Suno & AI Music Handoff thực tế:** Lyrics-only không tự biết melody; Suno không deterministic. Demo rẻ dùng để kiểm lời–nhạc trước full production.
7. **Tai người quyết định cuối cùng:** AI là bạn đồng sáng tác (cowriter); tai người quyết định điểm “chạm”, độ “tươi” và bản hoàn thiện cuối cùng. Không hứa tự tạo hit hay siêu phẩm.

---

## 🚀 Quy Trình Khám Phá Thích Nghi (Adaptive Discovery Flow)

```
                       User Brief / Seed / Melody / Chord
                                      │
                                      ▼
             [1] Đánh giá Material Affordance & Central Intent
                                      │
                                      ▼
             [2] Chọn Seed, Tứ & Working Hook (1 vòng cô đọng)
                                      │
                                      ▼
             [3] Dựng Form & Section Jobs theo Engine phát triển
                                      │
                                      ▼
             [4] Pilot Audition tại điểm cần chứng minh nhất
                                      │
                                      ▼
             [5] Decompile thành Generation Packet & Viết Rough Pass
                                      │
                                      ▼
             [6] ROUGH-LYRIC SEMANTIC GATE (Chẩn bệnh & hồi phục tầng sai)
                                      │
                                      ▼
             [7] SCOPE-A RELEASE GATE (Kiểm tra trước khi handoff)
                                      │
                                      ▼
             [8] Suno / AI Prototype Handoff ([SUNO PROTOTYPE-READY])
```

---

## 📂 Cấu Trúc Thư Mục Repository

```
songwriter/
├── README.md                              # Giới thiệu tổng quan & hướng dẫn sử dụng
├── SKILL.md                               # Entry point, Adaptive Flow, Pilot Proofing, Gates & Checklists
├── MANIFEST.md                            # Danh mục tài liệu tham chiếu & scripts
├── agents/
│   └── openai.yaml                        # Cấu hình interface agent
├── scripts/
│   ├── lyric_static_check.py              # Kiểm tra độ dài dòng, trùng từ cuối, dòng lặp
│   └── clean_context_eval.py              # Bộ test context và eval suite ca từ
└── references/
    ├── idea-and-structure.md              # Khung ý tưởng, Tứ, Form, Hook, Material Affordance, Phá cách
    ├── vietnamese-line-and-sound.md       # Âm thanh, thanh điệu tiếng Việt, nhịp điệu & vần
    ├── stage-validation-loop.md           # Các cổng kiểm định ngữ nghĩa (Semantic Gate & Scope-A)
    ├── suno-handoff.md                    # Quy chuẩn đóng gói prompt & tag cho Suno AI
    ├── music-sketch-and-demo.md           # Hướng dẫn dựng demo và kiểm tra nhạc-lời
    ├── genre-and-lyric-routing.md         # Định tuyến ca từ theo thể loại âm nhạc
    ├── folk-prosody.md                    # Thơ dân gian, lục bát và biến thể vào ca khúc
    ├── poem-to-song.md                    # Phương pháp phổ thơ thành ca khúc
    ├── style-mining.md                    # Khai thác phong cách tác giả & bản sắc riêng
    ├── dominant-analysis.md               # Phân tích hợp âm, hòa thanh & trục cảm xúc
    ├── case-log.md                        # Nhật ký các case thực chiến
    ├── audit-and-evaluation.md            # Phương pháp tự chấm điểm và đánh giá ca khúc
    ├── semantic-movement-suite.json       # Bộ test chuyển động ngữ nghĩa
    ├── writer-realization-suite.json      # Bộ test hiện thực hóa ca từ
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

## 🤖 Hướng Dẫn Nạp Vào AI Agent (Usage with AI Agents)

Để sử dụng bộ kỹ năng này với bất kỳ AI coding assistant nào mà không tốn chi phí API riêng:

### 1. Claude Code
Clone trực tiếp vào thư mục skills toàn cục:
```bash
git clone https://github.com/banoikukid/songwriter.git ~/.claude/skills/songwriting-min
```
Hoặc đặt vào thư mục `.claude/skills/songwriting-min` trong project hiện tại của bạn.

### 2. Antigravity IDE & CLI
```bash
git clone https://github.com/banoikukid/songwriter.git ~/.antigravity/skills/songwriting-min
```

### 3. Codex CLI & VS Code
```bash
git clone https://github.com/banoikukid/songwriter.git ~/.codex/skills/songwriting-min
```

### 4. Hệ sinh thái Agent chung (`.agents`)
```bash
git clone https://github.com/banoikukid/songwriter.git ~/.agents/skills/songwriting-min
```

Sau khi cài đặt, bạn chỉ cần yêu cầu agent trong terminal:
> *"Hãy áp dụng skill songwriting-min để sáng tác một ca khúc từ ý tưởng: [Brief của bạn]"*

---

## 📄 Bản Quyền & Tác Quyền

Phát triển phục vụ cộng đồng nhạc sĩ, nhà sản xuất và người sáng tạo nội dung ca khúc tiếng Việt.
