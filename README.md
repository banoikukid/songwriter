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
5. **Điều hướng Thích nghi Fast / Deep (Adaptive Fast / Deep Routing):**
   - *Brief mở / đơn giản / rõ ràng:* Sử dụng `WRITE — FAST` từ `SKILL.md` (`Emotion → Relationship → 1 Tứ khả thi → Working Hook → Section Guidance → Write`), viết ngay bản thô mà không cần nạp tài liệu kiến trúc ngoài.
   - *Brief chuyên sâu / đa nghĩa / gieo vật liệu / yêu cầu kiến trúc:* Kích hoạt `WRITE — DEEP` và nạp `references/idea-and-structure.md`.
   - *Pilot proofing có điều kiện:* Chỉ áp dụng trong nhánh `WRITE — DEEP` khi thực sự cần chứng minh một ý niệm, cơ chế đoạn, chiến lược vật liệu hoặc điểm cấn chưa chắc chắn trước khi triển khai toàn bài.
6. **Suno & AI Music Handoff thực tế:** Lyrics-only không tự biết melody; Suno không deterministic. Demo rẻ dùng để kiểm lời–nhạc trước full production.
7. **Tai người quyết định cuối cùng:** AI là bạn đồng sáng tác (cowriter); tai người quyết định điểm “chạm”, độ “tươi” và bản hoàn thiện cuối cùng. Không hứa tự tạo hit hay siêu phẩm.

---

## 🚀 Quy Trình Khám Phá Thích Nghi (Adaptive Discovery Flow)

```text
                        USER REQUEST / BRIEF
                                 │
        ┌────────────────────────┴────────────────────────┐
        ▼                                                 ▼
  [WRITE — FAST]                                   [WRITE — DEEP]
 (Brief mở/đơn giản,                              (Brief gieo vật liệu nặng,
  miền nghĩa rõ ràng)                              title đa nghĩa, ẩn dụ sâu,
        │                                          yêu cầu dựng Tứ/Cốt/Form)
        │                                                 │
  SKILL.md ONLY                                    idea-and-structure.md
 (0 reference nạp ngoài)                          (Pilot proofing nếu cần)
        │                                                 │
        └────────────────────────┬────────────────────────┘
                                 ▼
                         ROUGH LYRIC PASS
                                 │
        ┌────────────────────────┼────────────────────────┐
        │                        │                        │
        ▼                        ▼                        ▼
[Không có symptom /      [Có symptom cụ thể       [User yêu cầu lyrics-first /
 task đã đạt chuẩn]       bộc lộ sau bản nháp]     Suno prototype handoff]
        │                        │                        │
        ▼                        ▼                        ▼
  DELIVER / STOP        Nạp đúng 1 Canonical     SCOPE-A RELEASE GATE
 (Không gọi diagnostic   Owner cần thiết:         (Kiểm tra phrasing, hơi thở,
  không cần thiết)       - REFINE (Nén ca từ)     vần, mouth-feel trên lyric)
                         - LANGUAGE/SOUND (Vần,           │
                           ngữ âm, từ vựng)               ▼
                         - IDEA (Tứ/Cốt gãy)      SUNO PRODUCTION HANDOFF
                                 │                (references/suno-production.md)
                                 ▼
                         TARGETED PATCH & STOP
```

---

## 📂 Cấu Trúc Thư Mục Repository (Pure Agent Skill — v1.4.0)

```
songwriter/
├── LICENSE                                # Giấy phép mã nguồn mở MIT License
├── README.md                              # Giới thiệu tổng quan & hướng dẫn sử dụng
├── SKILL.md                               # Runtime Constitution, Fast/Deep Routing, 4 Phanh Writer, Micro-Rewrite, Điều hướng Chẩn đoán & Điều kiện dừng
├── MANIFEST.md                            # Danh mục tài liệu tham chiếu & version registry (v1.4.0 Stable)
├── agents/
│   └── openai.yaml                        # Cấu hình interface agent
└── references/                            # 36 tệp tri thức chuyên sâu (Phân tầng 3-Tier)
    ├── [Nhóm 1: Tri thức cốt lõi & Handoff — 14 tệp runtime nghiệp vụ]
    │   ├── idea-and-structure.md          # Tứ, Form, Hook, Material Affordance, Phá cách (WRITE — DEEP)
    │   ├── vietnamese-line-and-sound.md   # Âm thanh, thanh điệu tiếng Việt, nhịp điệu & Lexical Naturalness
    │   ├── lyric-refinement.md            # Tinh lọc ca từ, compression, subtext, điểm rơi, sonic craft
    │   ├── vocal-realization.md           # Phân tầng vocal (Identity, Performance, Production) & vocal prosody
    │   ├── suno-production.md             # PRIMARY OWNER: Chuẩn 3-block Suno, Character Budgets & Cause Confidence Matrix
    │   ├── suno-handoff.md                # Compatibility / quick-handoff sidecar cho Suno AI
    │   ├── music-sketch-and-demo.md       # Dựng demo, Music Blueprint & kiểm tra nhạc-lời
    │   ├── genre-and-lyric-routing.md     # Định tuyến ca từ theo thể loại âm nhạc
    │   ├── folk-prosody.md                # Thơ dân gian, lục bát và biến thể vào ca khúc
    │   ├── poem-to-song.md                # Phương pháp phổ thơ thành ca khúc
    │   ├── style-mining.md                # Style DNA, phong cách tác giả & bản sắc riêng
    │   ├── vietnamese-style-dna.md        # 12 lanes nhạc Việt & soundscape DNA
    │   ├── vietnamese-spoken-form.md      # Khẩu khí, ngữ âm & written-to-spoken diagnostics
    │   └── vietnamese-corpus-profile.md   # Thống kê VietLyrics & WPM benchmark
    ├── [Nhóm 2: Công cụ thẩm định, chẩn đoán & bộ nhớ phiên — 4 tệp sidecars]
    │   ├── lyric-quality-review.md        # Đánh giá độc lập 6 lăng kính (REVIEW SIDECAR / explicit review only)
    │   ├── case-log-protocol.md           # Giao thức ghi nhớ phiên làm việc (Session continuity only)
    │   ├── stage-validation-loop.md       # Cổng đối chiếu xuyên tầng (AUDIT / FAILURE DEBUGGER ONLY — không nạp khi viết)
    │   └── dominant-analysis.md           # Phân tích hợp âm, hòa thanh (ANALYSIS-ONLY / DEMOTED — không nạp khi viết)
    └── [Nhóm 3: Tài nguyên kiểm định & Báo cáo audit — 18 tệp (Offline / Không nạp vào generation context)]
        ├── eval-suite.json, semantic-movement-suite.json, writer-realization-suite.json... (8 schemas/suites)
        └── audit-process-audit-*, b6-baseline-*, cot-corpus-*, tu-corpus-*... (10 historical reports)
```

> **Nguyên Tắc Tiết Kiệm Ngữ Cảnh (Context Budget Policy):**  
> 36 tệp trong `references/` **không phải** là 36 tài liệu runtime đồng thời nạp vào prompt. Skill vận hành theo nguyên tắc tối thiểu ngữ cảnh:
> - **WRITE — FAST (Brief mở/đơn giản):** Mặc định nạp **0 tài liệu tham chiếu chuyên biệt** (zero specialized WRITE references); quy trình nội tại của `SKILL.md` là đủ để viết.
> - **Các lane chuyên sâu / Hiệu chỉnh:** Ưu tiên nạp **đúng 1 Canonical Owner** cho task hoặc triệu chứng hiện tại; chỉ nạp reference thứ hai khi năng lực thực sự cần phối hợp xuyên owner (ví dụ: `poem-to-song.md` + `folk-prosody.md`). Tuyệt đối không nạp tài liệu chỉ vì có liên quan chung chung.
> - **AUDIT / Offline:** `stage-validation-loop.md` (chỉ nạp khi audit/failure tracing), `dominant-analysis.md` (analysis-only/demoted), cùng toàn bộ schemas, test suites JSON và báo cáo audit lịch sử hoàn toàn bị cô lập khỏi normal writer context.

> **Đặc điểm Pure-Skill:** Không chứa bất kỳ script Python, binary hay dependency thực thi nào. Toàn bộ logic được trừu tượng hóa thành Knowledge Architecture & Instruction Rules, attack surface tối thiểu. Skill không chứa executable runtime hay dependency bên ngoài. Package không tự gọi shell/network; context usage và quyền dữ liệu phụ thuộc host agent khi nạp vào Hermes, OpenClaw, Claude Code hay Codex.

---

## 🏷️ Quy Chuẩn Nhãn Trạng Thái (Status Tags)

- `[SUNO PROTOTYPE-READY — Scope A PASS; music-fit UNKNOWN]`: Bản lời đã qua kiểm định Scope A (lyrics-first verification) về phrasing, điểm lấy hơi, cadence/rhyme và các rủi ro mouth-feel nhìn thấy trên lyric sheet, đủ sạch để thử nghiệm prototype trên Suno AI; trạng thái này **không yêu cầu** ROUGH-LYRIC SEMANTIC GATE, **không chứng minh** melody/prosody/music-fit thực tế, và duy trì `music-fit UNKNOWN` cho đến khi có audio/melody kiểm chứng.
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
