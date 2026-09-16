# Session Memory Protocol (Giao thức ghi nhớ phiên làm việc)

> **Nguyên tắc cốt lõi:** Package skill là tài nguyên tĩnh bất biến (immutable). Agent **tuyệt đối không ghi trực tiếp** hay sửa đổi file trong package skill khi đang chạy.

Nếu môi trường host (Hermes, OpenClaw, Claude Code, Codex, Antigravity) hỗ trợ session memory, context log hoặc workspace state, agent chỉ lưu tối đa 10 fingerprint gần nhất trong state/bộ nhớ tạm của phiên làm việc hiện tại để tránh lặp cơ chế giữa các bài liên tiếp.

---

## 1. Quy tắc lưu vết trong Session State

- **Dung lượng tối đa:** Chỉ giữ tối đa 10 fingerprint gần nhất trong cùng một phiên làm việc;
- **Nội dung cấm:** Không lưu toàn bộ lyric, câu ví dụ, danh sách hình ảnh, title nổi tiếng hay nhận xét cảm tính dài;
- **Mục đích duy nhất:** Fingerprint chỉ mô tả cấu trúc tối thiểu (entry, engine, form, phrase, style, diagnostic) nhằm phục vụ việc khử trùng lặp (decontamination) giữa các bài trong cùng phiên;
- **Cấm làm seed:** Tuyệt đối không dùng fingerprint của bài cũ làm seed câu hoặc Tứ cho ca mới;
- **Vòng đời:** Khi kết thúc phiên làm việc hoặc người dùng yêu cầu làm bài hoàn toàn mới, reset session state về rỗng.

---

## 2. Cấu trúc Fingerprint mẫu (Ví dụ tham chiếu)

| Case | Fingerprint tránh lặp trong phiên |
|---|---|
| phrase-behavior | `entry=BRIEF; engine=DECLARATION; form=V-PC-C-V-PC-C-B-FC; phrase=short-long+call-response; expression=DIRECT; style=pop-funk-4/4` |
| scale-camera | `entry=TITLE; engine=DECLARATION/REFRAME; form=V-PC-C-V-PC-C-B-FC; phrase=open-verse+title-call; expression=MIXED; style=cinematic-6/8` |
| direct-control | `entry=TITLE; engine=DECLARATION/TRANSFORM; form=V-PC-C-V-PC-C-B-FC; phrase=short-long+call-response; expression=DIRECT/PERSONAL; style=pop-funk-4/4` |
| image-routing | `entry=TITLE/BRIEF; artifact=route+Tứ-Cốt checks; expression=DIRECT+MIXED+FIELD; image-route=literal+emblematic; diagnostic=owner-separation` |
