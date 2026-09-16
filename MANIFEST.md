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

## Danh Mục Tệp Tin (File Registry)

| Tệp tin | Vai trò | Trạng thái |
| :--- | :--- | :--- |
| `README.md` | Giới thiệu tổng quan & hướng dẫn sử dụng nhanh | ✅ Active |
| `SKILL.md` | Bộ não điều khiển, Flow khám phá thích nghi, Pilot Proofing, Gates & Checklists (v1.1.0) | ✅ Active |
| `MANIFEST.md` | Bảng kê khai tài nguyên và phiên bản | ✅ Active |
| `.gitignore` | Cấu hình loại trừ git cho Python và hệ điều hành | ✅ Active |
| `agents/openai.yaml` | Cấu hình interface cho agent | ✅ Active |
| `scripts/lyric_static_check.py` | Kiểm tra tĩnh ca từ (độ dài dòng, trùng từ cuối, dòng lặp) | ✅ Active |
| `scripts/clean_context_eval.py` | Bộ test context và đánh giá ca khúc | ✅ Active |

### Danh Mục References (29 tệp)

1. `references/idea-and-structure.md`: Khung ý tưởng, Tứ, Form, Hook, Material Affordance Audition, Chế độ phá cách
2. `references/vietnamese-line-and-sound.md`: Âm thanh, thanh điệu tiếng Việt, nhịp điệu, tông vật liệu & vần
3. `references/stage-validation-loop.md`: Cổng kiểm định ngữ nghĩa (Semantic Gate & Scope-A)
4. `references/suno-handoff.md`: Quy chuẩn đóng gói prompt, structure tags & handoff Suno AI
5. `references/music-sketch-and-demo.md`: Hướng dẫn dựng demo và kiểm tra nhạc-lời
6. `references/genre-and-lyric-routing.md`: Định tuyến ca từ theo thể loại âm nhạc
7. `references/folk-prosody.md`: Thơ dân gian, lục bát và biến thể vào ca khúc
8. `references/poem-to-song.md`: Phương pháp phổ thơ thành ca khúc
9. `references/style-mining.md`: Khai thác phong cách tác giả & bản sắc riêng
10. `references/dominant-analysis.md`: Phân tích hợp âm, hòa thanh & trục cảm xúc
11. `references/case-log.md`: Nhật ký các case thực chiến
12. `references/audit-and-evaluation.md`: Phương pháp tự chấm điểm và đánh giá ca khúc
13. `references/eval-suite.json`: Bộ đề kiểm thử ca khúc đa thể loại
14. `references/eval-grader-schema.json`: Schema chấm điểm bài hát
15. `references/cross-genre-full-song-suite.json`: Bộ test trọn bài đa thể loại
16. `references/full-song-scope-a-schema.json`: Schema kiểm định Scope A toàn bài
17. `references/semantic-movement-suite.json`: Bộ test chuyển động ngữ nghĩa
18. `references/semantic-movement-grader-schema.json`: Schema chấm điểm chuyển động ngữ nghĩa
19. `references/writer-realization-suite.json`: Bộ test hiện thực hóa ca từ người viết
20. `references/writer-realization-grader-schema.json`: Schema chấm điểm Writer Realization
21. `references/audit-process-audit-2026-07-18.md`: Báo cáo audit quy trình sáng tác
22. `references/b6-baseline-audit-2026-07-18.md`: Báo cáo audit baseline B6
23. `references/cot-corpus-audit-2026-07-18.md`: Báo cáo audit corpus suy luận chuỗi
24. `references/emotional-field-audit-2026-07-22.md`: Báo cáo audit trường cảm xúc
25. `references/expert-process-audit-2026-07-18.md`: Báo cáo audit quy trình chuyên gia
26. `references/legacy-reference-audit-2026-07-18.md`: Báo cáo audit tài liệu di sản
27. `references/line-corpus-audit-2026-07-18.md`: Báo cáo audit ngữ liệu dòng ca từ
28. `references/sound-rhyme-prosody-audit-2026-07-18.md`: Báo cáo audit âm - vần - luật thơ
29. `references/tu-corpus-audit-2026-07-18.md`: Báo cáo audit kho Tứ ca khúc
