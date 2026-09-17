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

## 📂 Cấu Trúc Thư Mục Repository (Pure Agent Skill — v1.3.6)

```
songwriter/
├── LICENSE                                # Giấy phép mã nguồn mở MIT License
├── README.md                              # Giới thiệu tổng quan & hướng dẫn sử dụng
├── SKILL.md                               # Entry point, Adaptive Flow, Pilot Proofing, Micro-Polish & Gates
├── MANIFEST.md                            # Danh mục tài liệu tham chiếu & version registry (v1.3.6)
├── agents/
│   └── openai.yaml                        # Cấu hình interface agent
└── references/                            # 33 tệp tri thức chuyên sâu (Phân tầng 3-Tier)
    ├── [Nhóm 1: Tri thức cốt lõi & Handoff — 13 tệp]
    │   ├── idea-and-structure.md          # Tứ, Form, Hook, Material Affordance, Phá cách
    │   ├── vietnamese-line-and-sound.md   # Âm thanh, thanh điệu tiếng Việt, nhịp điệu & Lexical Naturalness
    │   ├── lyric-refinement.md            # Tinh lọc ca từ, compression, subtext, điểm rơi, sonic craft
    │   ├── vocal-realization.md           # Phân tầng vocal (Identity, Performance, Production) & vocal prosody
    │   ├── suno-production.md             # Chuẩn 3-block Suno, Character Budgets & Cause Confidence Matrix
    │   ├── stage-validation-loop.md       # Cổng kiểm định ngữ nghĩa (Semantic Gate & Scope-A)
    │   ├── suno-handoff.md                # Tóm tắt vận hành đóng gói prompt & tag cho Suno AI
    │   ├── music-sketch-and-demo.md       # Dựng demo, Music Blueprint & kiểm tra nhạc-lời
    │   ├── genre-and-lyric-routing.md     # Định tuyến ca từ theo thể loại âm nhạc
    │   ├── folk-prosody.md                # Thơ dân gian, lục bát và biến thể vào ca khúc
    │   ├── poem-to-song.md                # Phương pháp phổ thơ thành ca khúc
    │   ├── style-mining.md                # Style DNA, phong cách tác giả & bản sắc riêng
    │   └── dominant-analysis.md           # Phân tích hợp âm, hòa thanh & trục cảm xúc
    ├── [Nhóm 2: Công cụ thẩm định chẩn đoán — 2 tệp]
    │   ├── lyric-quality-review.md        # Đánh giá độc lập 6 lăng kính (CRITICAL / SUGGESTED / OPTIONAL)
    │   └── case-log-protocol.md           # Session memory protocol (CHỈ nạp khi host cần session continuity)
    └── [Nhóm 3: Tài nguyên kiểm định & Báo cáo audit — 18 tệp (KHÔNG nạp vào generation context)]
        ├── eval-suite.json, semantic-movement-suite.json, writer-realization-suite.json... (8 schemas/suites)
        └── audit-process-audit-*, b6-baseline-*, cot-corpus-*, tu-corpus-*... (10 historical reports)
```

> **Nguyên Tắc Tiết Kiệm Ngữ Cảnh (Context Budget Policy):**  
> 33 tệp trong `references/` **không phải** là 33 tài liệu runtime đồng thời nạp vào prompt. Skill vận hành theo nguyên tắc tối thiểu ngữ cảnh:
> - **Generation thông thường:** Chỉ nạp $1 - 2$ tệp thuộc Nhóm 1 theo đúng lane nghiệp vụ đang mở.
> - **Review độc lập / Diagnostic:** Chỉ nạp tệp tương ứng thuộc Nhóm 2 khi chẩn đoán ca từ có vấn đề.
> - **Tuyệt đối không nạp Nhóm 3:** Toàn bộ schemas, test suites JSON và báo cáo audit lịch sử chỉ dùng cho benchmark hồi quy offline, không đưa vào context sáng tác của agent.

> **Đặc điểm Pure-Skill:** Không chứa bất kỳ script Python, binary hay dependency thực thi nào. Toàn bộ logic được trừu tượng hóa thành Knowledge Architecture & Instruction Rules, attack surface tối thiểu. Skill không chứa executable runtime hay dependency bên ngoài. Package không tự gọi shell/network; context usage và quyền dữ liệu phụ thuộc host agent khi nạp vào Hermes, OpenClaw, Claude Code hay Codex.

---

## 🏷️ Quy Chuẩn Nhãn Trạng Thái (Status Tags)

- `[SUNO PROTOTYPE-READY — Scope A PASS; music-fit UNKNOWN]`: Bản lời đã qua Semantic Gate và Scope A, sẵn sàng nạp vào Suno để test giai điệu/phối khí.
- `[LYRIC DRAFT — Scope A chưa qua; music-fit UNKNOWN]`: Bản nháp đang trong quá trình hiệu chỉnh, cần sửa ở tầng chỉ định trước khi demo.

---

## 🤖 Hướng Dẫn Nạp Vào AI Agent (Usage with AI Agents)

Để sử dụng bộ kỹ năng này với các AI coding assistant (Skill không yêu cầu API/service riêng của chính nó; model quota/cost phụ thuộc provider đang dùng):

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

## 📄 Giấy Phép & Bản Quyền (License)

Dự án được phân phối dưới giấy phép **[MIT License](LICENSE)**. Phát triển phục vụ cộng đồng nhạc sĩ, nhà sản xuất âm nhạc và người sáng tạo nội dung ca khúc tiếng Việt.
