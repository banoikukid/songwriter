# MANIFEST — songwriting-min

> Single source of truth cho version và cấu trúc skill `songwriting-min` (Songwriter).

---

## Thông Tin Phiên Bản

```yaml
skill: songwriting-min
version: 1.0.0
last_updated: 2026-09-16
purpose: "Writer-First Vietnamese Songwriting Skill for AI & Human Cowriting"
repository: "https://github.com/banoikukid/songwriter"
```

---

## Danh Mục Tệp Tin (File Registry)

| Tệp tin | Vai trò | Trạng thái |
| :--- | :--- | :--- |
| `README.md` | Giới thiệu tổng quan & hướng dẫn sử dụng nhanh | ✅ Active |
| `SKILL.md` | Bộ não điều khiển, 8 bước sáng tác, lane chọn, gates & checklist | ✅ Active |
| `MANIFEST.md` | Bảng kê khai tài nguyên và phiên bản | ✅ Active |
| `.gitignore` | Cấu hình loại trừ git cho Python và hệ điều hành | ✅ Active |
| `scripts/lyric_static_check.py` | Kiểm tra tĩnh ca từ (độ dài dòng, trùng từ cuối, dòng lặp) | ✅ Active |
| `scripts/clean_context_eval.py` | Bộ test context và đánh giá ca khúc | ✅ Active |

### Danh Mục References (25 tệp)

1. `references/idea-and-structure.md`: Khung ý tưởng, Tứ, Form, Hook, Chế độ phá cách
2. `references/vietnamese-line-and-sound.md`: Âm thanh, thanh điệu tiếng Việt, nhịp điệu & vần
3. `references/stage-validation-loop.md`: Cổng kiểm định ngữ nghĩa (Semantic Gate)
4. `references/suno-handoff.md`: Quy chuẩn đóng gói prompt & tag cho Suno AI
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
17. `references/audit-process-audit-2026-07-18.md`: Báo cáo audit quy trình sáng tác
18. `references/b6-baseline-audit-2026-07-18.md`: Báo cáo audit baseline B6
19. `references/cot-corpus-audit-2026-07-18.md`: Báo cáo audit corpus suy luận chuỗi
20. `references/emotional-field-audit-2026-07-22.md`: Báo cáo audit trường cảm xúc
21. `references/expert-process-audit-2026-07-18.md`: Báo cáo audit quy trình chuyên gia
22. `references/legacy-reference-audit-2026-07-18.md`: Báo cáo audit tài liệu di sản
23. `references/line-corpus-audit-2026-07-18.md`: Báo cáo audit ngữ liệu dòng ca từ
24. `references/sound-rhyme-prosody-audit-2026-07-18.md`: Báo cáo audit âm - vần - luật thơ
25. `references/tu-corpus-audit-2026-07-18.md`: Báo cáo audit kho Tứ ca khúc
