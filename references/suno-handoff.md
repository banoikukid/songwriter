# Handoff sang Suno

Trước khi handoff, xác định render là **prototype** hay **production candidate**. Lần gen đầu mặc định là prototype để kiểm song system và prosody; âm thanh đầy không đồng nghĩa bài đã qua rewrite/feedback gate. Đọc `music-sketch-and-demo.md` khi user yêu cầu ca khúc đầy đủ.

Lyrics-first chỉ được handoff với nhãn `[SUNO PROTOTYPE-READY — Scope A PASS; music-fit UNKNOWN]` sau `SCOPE-A RELEASE GATE` ở `vietnamese-line-and-sound.md`. Không ghi `Suno-ready` trần. Chỉ dùng `[PRODUCTION CANDIDATE]` sau khi đã nghe render/demo có lời và pass Scope B + performance + feedback.

Đây là nguồn vận hành duy nhất trong skill cho handoff Suno. Không tải playbook AI-music cũ vào generation; các marker hoặc setting chưa được tài liệu chính thức xác nhận chỉ được nêu như giả thuyết A/B, không làm mặc định.

## Xuất cơ bản

- Dùng tag section chuẩn: `[Verse]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Outro]`.
- Viết đầy đủ mọi section lặp; không ghi “lặp Chorus”.
- Dấu ngắt đặt ở biên từ; không xẻ từ ghép/láy.
- Style prompt mô tả genre, mood, energy curve, vocal, instrumentation, groove và production; không nhắc nghệ sĩ.
- Chỉ thêm một cue riêng ở đầu section khi thật sự cần. Không chèn cue giữa câu mặc định.

## Giới hạn kiểm soát

Lyrics và tag không buộc Suno tạo đúng melody, nốt, key, BPM hoặc meter. Density shift chỉ là bias yếu.

Nếu bản gen đều:

1. Đổi/lai genre có groove phù hợp.
2. Dùng section behavior đã được nguồn xác nhận như half-time/double-time/breakdown.
3. Dùng style descriptor về groove/tempo/phrasing.
4. Điều chỉnh settings trong phạm vi nguồn và re-roll.
5. Cần melody chính xác thì dùng audio/hum/composer/DAW.

Không coi `[Beat switch]` hoặc marker community là lever đáng tin nếu nguồn hiện hành chưa xác nhận.

## Reverse extract

Recognition không đồng nghĩa controllability. Khi Suno mô tả audio upload:

- Chỉ mine section, instrument + action, dynamics, vocal và FX.
- Xóa toàn bộ lời, đạo cụ và skeleton nội dung.
- Không dùng format reverse làm seed Tứ, Cốt hoặc Câu.
- A/B basic tags với section cues trước khi tin.

## Scope và phát âm

- Lyrics-first là Scope A: dọn biên từ, cụm phụ âm, checked-coda và viết đủ chữ.
- Có melody/demo là Scope B: kiểm tone–note, syllable–note và phát âm.
- Hát sai dấu: xác định đúng từ/cụm trên render, thử đổi sang cách nói tự nhiên tương đương rồi re-render; chỉ thử phiên âm cục bộ khi user nghe xác nhận lỗi phát âm lặp lại. Không trông chờ Style sửa dấu.

## Sau gen

Nghe rồi chẩn đúng triệu chứng:

- Phẳng do lời: quay Cốt/Hook/section role.
- Phẳng do engine: đổi genre/groove/settings/re-roll.
- Sai dấu: dọn lyric.
- Quá ngắn: kiểm đã viết đủ section lặp.
- Sai vocal: dùng Vocal Gender/control chuyên dụng và vocal descriptor.

Cập nhật verdict vào `case-log.md`.

Nếu render là prototype, quay về bước Rewrite: sửa đúng tầng rồi re-render. Chỉ gọi production candidate sau khi lyric–melody–harmony–rhythm và performance đã được nghe, không chỉ đọc.
