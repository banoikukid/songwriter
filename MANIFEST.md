# MANIFEST — songwriting-min

> Single source of truth cho version và cấu trúc skill `songwriting-min` (Songwriter).

---

## Thông Tin Phiên Bản

```yaml
skill: songwriting-min
version: 1.4.0
release_date: 2026-08-11
last_updated: 2026-09-24
purpose: "Writer-First Vietnamese Songwriting Skill with Fast/Deep adaptive routing, 4 canonical Writer Brakes, symptom-triggered domain diagnostics, Reviewer sidecar, Suno production ownership, and isolated audit/evaluation lanes (v1.4.0 Stable)"
repository: "https://github.com/banoikukid/songwriter"
source_canonical: "https://github.com/banoikukid/songwriter"
upstream_lineage: "TearusVN/songwriting-studio/plugins/songwriting-studio/skills/songwriting-min (Internal Origin)"
```

---

## Danh Mục Tệp Tin (File Registry - Pure Agent Skill)

| Tệp tin | Vai trò | Trạng thái |
| :--- | :--- | :--- |
| `LICENSE` | Giấy phép mã nguồn mở MIT License | ✅ Active |
| `README.md` | Giới thiệu tổng quan & hướng dẫn nạp vào Agent | ✅ Active |
| `SKILL.md` | Hiến pháp sáng tác cốt lõi (Return to Roots), 4 Phanh Writer, Flow khám phá thích nghi & Điều kiện dừng (v1.4.0) | ✅ Active |
| `MANIFEST.md` | Bảng kê khai tài nguyên và phiên bản | ✅ Active |
| `agents/openai.yaml` | Cấu hình interface cho agent | ✅ Active |

> **Lưu ý:** Đây là bản **Pure Agent Skill** (100% Markdown & JSON Knowledge Base), hoàn toàn không chứa mã thực thi runtime, script Python hay dependency bên ngoài; attack surface tối thiểu và có tính portable cao trên mọi hệ thống Agent (Hermes, OpenClaw, Claude Code, Antigravity, Codex).

### Phân Tầng Tài Nguyên Tham Chiếu (3-Tier Reference Taxonomy — 36 tệp)

> **Nguyên tắc Context Budget:** 36 tệp trong thư mục `references/` **không phải** là 36 tài liệu runtime đồng thời nạp vào prompt. Agent tuân thủ chính sách ngữ cảnh tối thiểu:
> - **WRITE — FAST (Brief mở/đơn giản):** Mặc định nạp **0 tài liệu tham chiếu chuyên biệt** (zero specialized WRITE references); quy trình nội tại của `SKILL.md` là đủ để viết.
> - **Các lane chuyên sâu / Hiệu chỉnh:** Ưu tiên nạp **đúng 1 Canonical Owner** cho task hoặc triệu chứng hiện tại; chỉ nạp reference thứ hai khi năng lực thực sự cần phối hợp xuyên owner (ví dụ: `poem-to-song.md` + `folk-prosody.md`). Tuyệt đối không nạp tài liệu chỉ vì có liên quan chung chung.
> - **AUDIT / Offline:** `stage-validation-loop.md` (chỉ nạp khi audit/failure tracing), `dominant-analysis.md` (analysis-only/demoted), cùng toàn bộ schemas, test suites JSON và báo cáo audit lịch sử hoàn toàn bị cô lập khỏi normal writer context.

#### Nhóm 1: Tri thức Cốt lõi & Handoff Sản xuất (Runtime Knowledge — 14 tệp)
*Chỉ nạp tệp tương ứng khi lane nghiệp vụ cụ thể được kích hoạt (ưu tiên 1 owner chính):*
1. `references/idea-and-structure.md`: Khung ý tưởng, Tứ, Form, Hook, Material Affordance Audition, Chế độ phá cách (WRITE — DEEP)
2. `references/vietnamese-line-and-sound.md`: Âm thanh, thanh điệu tiếng Việt, nhịp điệu, tông vật liệu, vần & Lexical Naturalness
3. `references/lyric-refinement.md`: Quy chuẩn tinh lọc ca từ (Lyric Craft, Compression, Subtext, Sonic Realization)
4. `references/vocal-realization.md`: Phân tầng vocal (Identity, Performance, Production), âm sắc & vocal prosody tiếng Việt
5. `references/suno-production.md`: Chuẩn sản xuất 3-block Suno (Style, Lyrics, Controls), Character Budgets & Cause Confidence Diagnosis (PRIMARY OWNER của Suno production/output behavior)
6. `references/suno-handoff.md`: Quy chuẩn đóng gói prompt, structure tags & handoff Suno AI (Compatibility / quick-handoff sidecar)
7. `references/music-sketch-and-demo.md`: Hướng dẫn dựng demo, Music Blueprint & kiểm tra nhạc-lời
8. `references/genre-and-lyric-routing.md`: Định tuyến ca từ theo thể loại âm nhạc
9. `references/folk-prosody.md`: Thơ dân gian, lục bát và biến thể vào ca khúc
10. `references/poem-to-song.md`: Phương pháp phổ thơ thành ca khúc
11. `references/style-mining.md`: Khai thác Style DNA, phong cách tác giả & bản sắc riêng
12. `references/vietnamese-style-dna.md`: 12 lanes nhạc Việt, soundscape DNA & nhả chữ
13. `references/vietnamese-spoken-form.md`: Khẩu khí, ngữ âm khi hát & written-to-spoken diagnostics
14. `references/vietnamese-corpus-profile.md`: Thống kê quần thể VietLyrics & WPM benchmark

#### Nhóm 2: Công cụ Thẩm định, Chẩn đoán & Bộ nhớ Phiên (Diagnostic / Audit / Continuity Sidecars — 4 tệp)
*Chỉ nạp khi người dùng yêu cầu review độc lập, session continuity hoặc audit formal:*
15. `references/lyric-quality-review.md`: Đánh giá chất lượng lời độc lập theo 6 lăng kính (REVIEW SIDECAR / explicit review only)
16. `references/case-log-protocol.md`: Giao thức ghi nhớ phiên làm việc (Session Memory Protocol — Session continuity only)
17. `references/stage-validation-loop.md`: Cổng đối chiếu ngữ nghĩa xuyên tầng (AUDIT / FAILURE DEBUGGER ONLY — tuyệt đối không nạp trong normal generation)
18. `references/dominant-analysis.md`: Phân tích hợp âm, hòa thanh & trục cảm xúc (ANALYSIS-ONLY / DEMOTED — tuyệt đối không nạp khi viết)

#### Nhóm 3: Tài nguyên Kiểm định, Schemas & Báo cáo Audit (Evaluation Assets — 18 tệp)
*Tài nguyên phục vụ benchmark, kiểm thử hồi quy offline và lưu trữ lịch sử; KHÔNG nạp vào generation context:*
- **Test Suites & Schemas (8 tệp):**
  19. `references/eval-suite.json`: Bộ đề kiểm thử ca khúc đa thể loại
  20. `references/eval-grader-schema.json`: Schema chấm điểm bài hát
  21. `references/cross-genre-full-song-suite.json`: Bộ test trọn bài đa thể loại
  22. `references/full-song-scope-a-schema.json`: Schema kiểm định Scope A toàn bài
  23. `references/semantic-movement-suite.json`: Bộ test chuyển động ngữ nghĩa
  24. `references/semantic-movement-grader-schema.json`: Schema chấm điểm chuyển động ngữ nghĩa
  25. `references/writer-realization-suite.json`: Bộ test hiện thực hóa ca từ người viết
  26. `references/writer-realization-grader-schema.json`: Schema chấm điểm Writer Realization
- **Báo cáo Audit Lịch sử & Phương pháp (10 tệp):**
  27. `references/audit-and-evaluation.md`: Phương pháp tự chấm điểm và đánh giá ca khúc offline
  28. `references/audit-process-audit-2026-07-18.md`: Báo cáo audit quy trình sáng tác
  29. `references/b6-baseline-audit-2026-07-18.md`: Báo cáo audit baseline B6
  30. `references/cot-corpus-audit-2026-07-18.md`: Báo cáo audit corpus suy luận chuỗi
  31. `references/emotional-field-audit-2026-07-22.md`: Báo cáo audit trường cảm xúc
  32. `references/expert-process-audit-2026-07-18.md`: Báo cáo audit quy trình chuyên gia
  33. `references/legacy-reference-audit-2026-07-18.md`: Báo cáo audit tài liệu di sản
  34. `references/line-corpus-audit-2026-07-18.md`: Báo cáo audit ngữ liệu dòng ca từ
  35. `references/sound-rhyme-prosody-audit-2026-07-18.md`: Báo cáo audit âm - vần - thanh điệu tiếng Việt
  36. `references/tu-corpus-audit-2026-07-18.md`: Báo cáo audit kho Tứ ca khúc
