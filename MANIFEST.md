# MANIFEST — songwriting-min

> Single source of truth cho version và cấu trúc skill `songwriting-min` (Songwriter).

---

## Thông Tin Phiên Bản

```yaml
skill: songwriting-min
version: 1.1.0
release_date: 2026-08-11
last_updated: 2026-09-16
purpose: "Writer-First Vietnamese Songwriting Skill with Adaptive Discovery Flow & Pilot Proofing"
repository: "https://github.com/banoikukid/songwriter"
source_canonical: "TearusVN/songwriting-studio/plugins/songwriting-studio/skills/songwriting-min"
```

---

## Danh Mục Tệp Tin (File Registry - Pure Agent Skill)

| Tệp tin | Vai trò | Trạng thái |
| :--- | :--- | :--- |
| `LICENSE` | Giấy phép mã nguồn mở MIT License | ✅ Active |
| `README.md` | Giới thiệu tổng quan & hướng dẫn nạp vào Agent | ✅ Active |
| `SKILL.md` | Bộ não điều khiển, Flow khám phá thích nghi, Pilot Proofing, Gates & Checklists (v1.1.0) | ✅ Active |
| `MANIFEST.md` | Bảng kê khai tài nguyên và phiên bản | ✅ Active |
| `agents/openai.yaml` | Cấu hình interface cho agent | ✅ Active |

> **Lưu ý:** Đây là bản **Pure Agent Skill** (100% Markdown & JSON Knowledge Base), hoàn toàn không chứa mã thực thi runtime, script Python hay dependency bên ngoài; attack surface tối thiểu và có tính portable cao trên mọi hệ thống Agent (Hermes, OpenClaw, Claude Code, Antigravity, Codex).

### Danh Mục References (30 tệp)

1. `references/idea-and-structure.md`: Khung ý tưởng, Tứ, Form, Hook, Material Affordance Audition, Chế độ phá cách
2. `references/vietnamese-line-and-sound.md`: Âm thanh, thanh điệu tiếng Việt, nhịp điệu, tông vật liệu & vần
3. `references/lyric-refinement.md`: Quy chuẩn tinh lọc ca từ (Lyric Craft, Language Realization, Sonic Realization)
4. `references/stage-validation-loop.md`: Cổng kiểm định ngữ nghĩa (Semantic Gate & Scope-A)
5. `references/suno-handoff.md`: Quy chuẩn đóng gói prompt, structure tags & handoff Suno AI
6. `references/music-sketch-and-demo.md`: Hướng dẫn dựng demo và kiểm tra nhạc-lời
7. `references/genre-and-lyric-routing.md`: Định tuyến ca từ theo thể loại âm nhạc
8. `references/folk-prosody.md`: Thơ dân gian, lục bát và biến thể vào ca khúc
9. `references/poem-to-song.md`: Phương pháp phổ thơ thành ca khúc
10. `references/style-mining.md`: Khai thác phong cách tác giả & bản sắc riêng
11. `references/dominant-analysis.md`: Phân tích hợp âm, hòa thanh & trục cảm xúc
12. `references/case-log-protocol.md`: Giao thức ghi nhớ ngắn hạn trong phiên làm việc (Session Memory Protocol)
13. `references/audit-and-evaluation.md`: Phương pháp tự chấm điểm và đánh giá ca khúc
14. `references/eval-suite.json`: Bộ đề kiểm thử ca khúc đa thể loại
15. `references/eval-grader-schema.json`: Schema chấm điểm bài hát
16. `references/cross-genre-full-song-suite.json`: Bộ test trọn bài đa thể loại
17. `references/full-song-scope-a-schema.json`: Schema kiểm định Scope A toàn bài
18. `references/semantic-movement-suite.json`: Bộ test chuyển động ngữ nghĩa
19. `references/semantic-movement-grader-schema.json`: Schema chấm điểm chuyển động ngữ nghĩa
20. `references/writer-realization-suite.json`: Bộ test hiện thực hóa ca từ người viết
21. `references/writer-realization-grader-schema.json`: Schema chấm điểm Writer Realization
22. `references/audit-process-audit-2026-07-18.md`: Báo cáo audit quy trình sáng tác
23. `references/b6-baseline-audit-2026-07-18.md`: Báo cáo audit baseline B6
24. `references/cot-corpus-audit-2026-07-18.md`: Báo cáo audit corpus suy luận chuỗi
25. `references/emotional-field-audit-2026-07-22.md`: Báo cáo audit trường cảm xúc
26. `references/expert-process-audit-2026-07-18.md`: Báo cáo audit quy trình chuyên gia
27. `references/legacy-reference-audit-2026-07-18.md`: Báo cáo audit tài liệu di sản
28. `references/line-corpus-audit-2026-07-18.md`: Báo cáo audit ngữ liệu dòng ca từ
29. `references/sound-rhyme-prosody-audit-2026-07-18.md`: Báo cáo audit âm - vần - thanh điệu tiếng Việt
30. `references/tu-corpus-audit-2026-07-18.md`: Báo cáo audit kho Tứ ca khúc
