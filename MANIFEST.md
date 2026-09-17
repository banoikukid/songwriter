# MANIFEST — songwriting-min

> Single source of truth cho version và cấu trúc skill `songwriting-min` (Songwriter).

---

## Thông Tin Phiên Bản

```yaml
skill: songwriting-min
version: 1.3.2
release_date: 2026-08-11
last_updated: 2026-09-17
purpose: "Writer-First Vietnamese Songwriting Skill: Return to Emotional Core, 8-Level Priority Hierarchy, Anti-Flatness & Pure Agent Architecture (v1.3.2)"
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
| `SKILL.md` | Hiến pháp sáng tác cốt lõi (Return to Roots), 4 Phanh Writer, Flow khám phá thích nghi & Điều kiện dừng (v1.3.1) | ✅ Active |
| `MANIFEST.md` | Bảng kê khai tài nguyên và phiên bản | ✅ Active |
| `agents/openai.yaml` | Cấu hình interface cho agent | ✅ Active |

> **Lưu ý:** Đây là bản **Pure Agent Skill** (100% Markdown & JSON Knowledge Base), hoàn toàn không chứa mã thực thi runtime, script Python hay dependency bên ngoài; attack surface tối thiểu và có tính portable cao trên mọi hệ thống Agent (Hermes, OpenClaw, Claude Code, Antigravity, Codex).

### Phân Tầng Tài Nguyên Tham Chiếu (3-Tier Reference Taxonomy — 33 tệp)

> **Nguyên tắc Context Budget:** 33 tệp trong thư mục `references/` **không phải** là 33 tài liệu runtime đồng thời nạp vào prompt. Agent tuân thủ chính sách ngữ cảnh tối thiểu: mỗi lượt sáng tác/hiệu chỉnh chỉ nạp $1 - 2$ tệp theo đúng lane đang kích hoạt. Tuyệt đối **không nạp Tier 3** vào generation context.

#### Nhóm 1: Tri thức Cốt lõi & Handoff Sản xuất (Runtime Knowledge — 13 tệp)
*Chỉ nạp tệp tương ứng khi lane nghiệp vụ cụ thể được kích hoạt:*
1. `references/idea-and-structure.md`: Khung ý tưởng, Tứ, Form, Hook, Material Affordance Audition, Chế độ phá cách
2. `references/vietnamese-line-and-sound.md`: Âm thanh, thanh điệu tiếng Việt, nhịp điệu, tông vật liệu, vần & Lexical Naturalness
3. `references/lyric-refinement.md`: Quy chuẩn tinh lọc ca từ (Lyric Craft, Compression, Subtext, Sonic Realization)
4. `references/vocal-realization.md`: Phân tầng vocal (Identity, Performance, Production), âm sắc & vocal prosody tiếng Việt
5. `references/suno-production.md`: Chuẩn sản xuất 3-block Suno (Style, Lyrics, Controls), Character Budgets & Cause Confidence Diagnosis
6. `references/stage-validation-loop.md`: Cổng kiểm định ngữ nghĩa (Semantic Gate & Scope-A release loop)
7. `references/suno-handoff.md`: Quy chuẩn đóng gói prompt, structure tags & handoff Suno AI
8. `references/music-sketch-and-demo.md`: Hướng dẫn dựng demo, Music Blueprint & kiểm tra nhạc-lời
9. `references/genre-and-lyric-routing.md`: Định tuyến ca từ theo thể loại âm nhạc
10. `references/folk-prosody.md`: Thơ dân gian, lục bát và biến thể vào ca khúc
11. `references/poem-to-song.md`: Phương pháp phổ thơ thành ca khúc
12. `references/style-mining.md`: Khai thác Style DNA, phong cách tác giả & bản sắc riêng
13. `references/dominant-analysis.md`: Phân tích hợp âm, hòa thanh & trục cảm xúc

#### Nhóm 2: Công cụ Thẩm định & Chẩn đoán (Diagnostic Sidecars — 2 tệp)
*Chỉ nạp khi người dùng yêu cầu review độc lập hoặc chẩn đoán ca từ có vấn đề:*
14. `references/lyric-quality-review.md`: Đánh giá chất lượng lời độc lập theo 6 lăng kính (CRITICAL, SUGGESTED, OPTIONAL)
15. `references/case-log-protocol.md`: Giao thức ghi nhớ phiên làm việc (Session Memory Protocol — CHỈ nạp khi host hỗ trợ session continuity hoặc cần truy vết bộ nhớ phiên; KHÔNG nạp mặc định khi sáng tác)

#### Nhóm 3: Tài nguyên Kiểm định, Schemas & Báo cáo Audit (Evaluation Assets — 18 tệp)
*Tài nguyên phục vụ benchmark, kiểm thử hồi quy offline và lưu trữ lịch sử; KHÔNG nạp vào generation context:*
- **Test Suites & Schemas (8 tệp):**
  16. `references/eval-suite.json`: Bộ đề kiểm thử ca khúc đa thể loại
  17. `references/eval-grader-schema.json`: Schema chấm điểm bài hát
  18. `references/cross-genre-full-song-suite.json`: Bộ test trọn bài đa thể loại
  19. `references/full-song-scope-a-schema.json`: Schema kiểm định Scope A toàn bài
  20. `references/semantic-movement-suite.json`: Bộ test chuyển động ngữ nghĩa
  21. `references/semantic-movement-grader-schema.json`: Schema chấm điểm chuyển động ngữ nghĩa
  22. `references/writer-realization-suite.json`: Bộ test hiện thực hóa ca từ người viết
  23. `references/writer-realization-grader-schema.json`: Schema chấm điểm Writer Realization
- **Báo cáo Audit Lịch sử & Phương pháp (10 tệp):**
  24. `references/audit-and-evaluation.md`: Phương pháp tự chấm điểm và đánh giá ca khúc offline
  25. `references/audit-process-audit-2026-07-18.md`: Báo cáo audit quy trình sáng tác
  26. `references/b6-baseline-audit-2026-07-18.md`: Báo cáo audit baseline B6
  27. `references/cot-corpus-audit-2026-07-18.md`: Báo cáo audit corpus suy luận chuỗi
  28. `references/emotional-field-audit-2026-07-22.md`: Báo cáo audit trường cảm xúc
  29. `references/expert-process-audit-2026-07-18.md`: Báo cáo audit quy trình chuyên gia
  30. `references/legacy-reference-audit-2026-07-18.md`: Báo cáo audit tài liệu di sản
  31. `references/line-corpus-audit-2026-07-18.md`: Báo cáo audit ngữ liệu dòng ca từ
  32. `references/sound-rhyme-prosody-audit-2026-07-18.md`: Báo cáo audit âm - vần - thanh điệu tiếng Việt
  33. `references/tu-corpus-audit-2026-07-18.md`: Báo cáo audit kho Tứ ca khúc
