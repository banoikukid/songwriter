# Recent case fingerprints

Đây là bộ nhớ ngắn cho **chuỗi bài trong cùng phiên** và regression, không phải kho câu mẫu hay eval suite. Ca độc lập không tải file này vào generation packet.

Quy tắc:

- Chỉ giữ tối đa 10 fingerprint gần nhất; khi thêm dòng thứ 11, chuyển dòng cũ nhất sang backup/eval registry ngoài skill.
- Không lưu lyric đầy đủ, câu ví dụ, danh sách hình ảnh, title nổi tiếng hay verdict cảm tính dài.
- Fingerprint chỉ mô tả cấu trúc đã dùng để tránh lặp; không được làm seed cho ca mới.
- Khi hết chuỗi bài hoặc đổi phiên, được phép xóa toàn bộ bảng và giữ header.

| Ngày | Case | Fingerprint tránh lặp | Verdict |
|---|---|---|---|
| 2026-07-24 | phrase-behavior | `entry=BRIEF; engine=DECLARATION; form=V-PC-C-V-PC-C-B-FC; phrase=short-long+call-response; expression=DIRECT; style=pop-funk-4/4; diagnostic=8-grid` | single-trial PASS lyric-sheet; music-fit UNKNOWN |
| 2026-07-24 | scale-camera | `entry=TITLE; engine=DECLARATION/REFRAME; form=V-PC-C-V-PC-C-B-FC; phrase=open-verse+title-call; expression=MIXED; scale=PHILOSOPHICAL>MIXED>PERSONAL>PHILOSOPHICAL; style=cinematic-co-phong-6/8; diagnostic=scale-collapse` | single-trial PASS semantic gate; music-fit UNKNOWN |
| 2026-07-24 | direct-negative-control | `entry=TITLE; engine=DECLARATION/TRANSFORM; form=V-PC-C-V-PC-C-B-FC; phrase=short-long+call-response+dialogue-bridge; expression=DIRECT/PERSONAL; scale=N/A; style=pop-funk-4/4; diagnostic=over-widening` | single-trial PASS; scale gate correctly skipped; music-fit UNKNOWN |
| 2026-07-27 | image-role-smoke | `entry=TITLE; engine=DECLARATION/REFRAME; form=V-PC-C-V-PC-C-B-FC-O; phrase=short-long+title-call; expression=MIXED; image-role=hook-compression; style=cinematic-pop-6/8; diagnostic=image-role-audition>literalization` | human FAIL at INTENT/TỨ→CỐT: emblematic image was turned into a physical object; static Scope A had passed but music-fit remains UNKNOWN |
| 2026-07-27 | emblematic-mapping | `entry=TITLE/BRIEF; engine=DECLARATION+STATE; artifact=Tứ-Cốt-hook; expression=MIXED+DIRECT-control; image-role=emblematic+literal-control; diagnostic=image-literalization` | candidate smoke PASS across emblematic, single-anchor, literal-provenance and direct controls; independent/human verdict pending |
| 2026-07-27 | image-routing-refactor | `entry=TITLE/BRIEF; artifact=route+Tứ-Cốt checks; expression=DIRECT+MIXED+FIELD; image-route=literal+emblematic+constellation+hook-only; diagnostic=owner-separation` | provisional same-context PASS on five branch/negative controls; human and music-fit verdict pending |
| 2026-07-28 | ambition-transformation | `entry=TITLE+BRIEF+MUSIC-controls; artifact=baseline+exploration+frontier arm cards; transformation=Tứ+lane/image+scale+song-system; diagnostic=ambition-surface+decoupled` | provisional same-context PASS on root-diversity, surface-negative and music-decoupling controls; independent/human/music-fit pending |
| 2026-07-28 | ambition-packet-decompile | `entry=TITLE+ambition; artifact=selected-arm>writer-packet>load-bearing-lines; transformation=call-response/form; diagnostic=analysis-leakage(mechanism)+core-word-audition` | human FAIL exposed mechanism vocabulary in a frontier lyric; patched same-context PASS on affected case, plain-direct negative and register-sensitive control; music-fit pending |
| 2026-07-28 | normal-writer-firewall | `entry=BRIEF; artifact=writer-packet>rough-section; expression=DIRECT+MIXED+FIELD; diagnostic=activation-burden+conditional-overlap` | provisional same-context PASS across three lane/negative controls; static check found no terminal repeat or duplicate; independent human and music-fit verdict pending |
| 2026-07-29 | ngay-thuong-co-em | `entry=BRIEF; engine=DECLARATION/AMPLIFY; form=I-V-PC-C-PC-V-PC-C-B-BUILD-FC-FPC-O; phrase=balanced+title-call; expression=DIRECT/MIXED; style=modern-youth-pop-4/4; handoff=section-tags+audible-section-cues; diagnostic=opposition-overuse+cue-format` | human PASS lyric + full Suno handoff; milestone PROVISIONAL for youth-pop love lane; render/Scope B/music-fit UNKNOWN; cross-genre validation required |
