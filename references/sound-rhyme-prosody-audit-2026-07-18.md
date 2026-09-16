# Audit bước sinh ÂM–VẦN–ĐIỆU (2026-07-18)

## Phạm vi và phương pháp

Đối chiếu B5 với cùng corpus 22 bài/6 lane, đọc kỹ hai dependency cũ `../../songwriting/references/vietnamese-prosody.md` và `../../songwriting/references/rhyming-playbook.md`, rồi kiểm các phản-ví-dụ đại diện ở lời/section. Đây là purposive falsification, không phải thống kê thị trường hay phân tích nốt toàn corpus. **Tone↔melody không thể kết luận từ chữ:** chỉ dùng nghiên cứu Kirby–Ladd để sửa đúng phạm vi; muốn chấm từng câu phải có melody/audio.

## Phản-chứng theo lane

| Lane / ca đại diện | Quan sát âm–vần–điệu | Rule cũ bị bác |
|---|---|---|
| Vpop buồn — `Mất Kết Nối` | cụm vần/assonance đổi theo section; dòng ngắn xen dòng dài; nhiều kết thúc mũi/đóng vẫn hoạt động | mọi bài cần AABB/ABAB; mọi cuối dòng phải mở+bằng |
| Nhạc vui/dance — `See Tình` | hook sống bằng chuỗi âm, điệp và wordplay gần mono-sound; semantic rhyme thứ yếu | AAAA luôn thành vè; lặp từ-cuối là lỗi; hook phải siết vần nghĩa |
| Indie — `Nàng Thơ`, `Một Đêm Say` | rhyme-pair rõ xen các dòng không khớp; phrasing/voice gánh; câu rất ngắn có thể là payoff chứ không template | cuối dòng “ngẫu nhiên” là lỗi; exact scheme bắt buộc |
| Mainstream ấm — `Có Em Chờ` | câu kể dài, vần nội/lặp/cadence đan nhau; không cần đồng nhất số chữ toàn đoạn | V1/V2 phải cùng con số; pop luôn strict end-rhyme |
| Bolero — `Duyên Phận` | câu dài nhiều vế và cadence vocal quan trọng; độ đều là thẩm mỹ lane, không phải monotony tự động | bắt câu ngắn phá mét; mọi section cần chênh density |
| Folk/anthemic — `Việt Nam Quê Hương Tôi`, `Hạt Gạo Làng Ta` | parallel/refrain và chuỗi âm cộng đồng tạo nhạc tính; repetition là kiến trúc | lặp frame/mono-sound mặc định nghèo; lục-bát là nguồn Việt duy nhất |

## Bảy lỗi phạm vi trong B5 cũ

1. **Genre bị dùng như khóa cả bài.** Rhyme mode thực tế đổi theo section-role: verse kể lỏng, hook/refrain lặp hoặc khít, bridge có thể đổi vùng âm.
2. **“Có sơ đồ AABB/ABAB” bị coi là bắt buộc.** Nội-vần, assonance, phonetic repetition và cadence cũng tạo coherence.
3. **Mono-rhyme bị cấm blanket.** Nó chỉ gây vè khi vần+cú pháp+meter+ý cùng lặp vô thức; ở dance, rap, folk, anthemic nó có thể là groove/hook.
4. **Vần gần và bão-hòa dùng ngưỡng máy móc.** `>½` không có cơ sở; chỉ sửa khi nghĩa bị ép hoặc âm không còn chức năng.
5. **Valence bị gán cho nguyên âm.** Không có cơ sở để coi `-a/-o` luôn vui và `-i/-ơi/-ương` luôn buồn.
6. **“Cuối dòng mở/bằng” bị áp lên mọi dòng.** Chỉ slot ngân cần ưu tiên âm tiết mở/sonorant; nasal vẫn ngân, checked-coda khó giữ dài. Thanh bằng/trắc phụ thuộc melody, không phải khẩu hình.
7. **Nghiên cứu tone–melody bị đảo thành tone-order cố định.** Kirby–Ladd đo hướng chuyển thanh **so với hướng nốt**; không có melody thì không thể gọi cặp `nặng→sắc` là sai.

## Kiến trúc B5 mới

1. **HARD:** giữ nghĩa; không ép vần; không xẻ từ ghép/láy; đọc không vấp; checked-coda không nằm ở sustain-slot nếu có lựa chọn tốt.
2. **ROLE:** chọn coherence theo lane+section bằng vần chân/nội, assonance, điệp hoặc cadence. Kiểm meter/biên phrase chỉ ở các đoạn reuse melody.
3. **MELODY:** Scope B so tone-motion với note-motion và nghe phát âm. Scope A không tự chấm tone-order; chờ render/tai người.

## Phạm vi hai reference cũ sau audit

- `../../songwriting/references/vietnamese-prosody.md`: chỉ là nguồn audit lịch sử; runtime hiện dùng `folk-prosody.md` khi user chủ ý giữ form.
- `../../songwriting/references/rhyming-playbook.md`: nguồn audit lịch sử; §II tone–melody chỉ có ý nghĩa ở Scope B. Các ngoại suy strictness theo genre và stable/unstable không phải nguồn vận hành của bản min; fixed tone-order/vowel-valence từng phát sinh trong `../SKILL.md` đã bị loại.

## Nguồn đối chiếu

- Kirby & Ladd, corpus 20 bài và dữ liệu: https://datashare.ed.ac.uk/items/772c3636-046d-4933-9000-917fa0fdd577
- University of Edinburgh research record: https://www.research.ed.ac.uk/en/publications/tone-melody-correspondence-in-vietnamese-popular-song
- `See Tình`: https://www.shazam.com/song/1637486483/see-t%C3%ACnh
- `Mất Kết Nối`: https://lyricvn.com/loi-bai-hat-mat-ket-noi-duong-domic/
- `Nàng Thơ`: https://lyricsvn.com/lyric/nang-tho/
- `Có Em Chờ`: https://lyricsvn.com/lyric/co-em-cho/
- `Một Đêm Say` (kênh tác giả): https://m.soundcloud.com/thinhsuy/mds
- `Việt Nam Quê Hương Tôi`: https://hopamviet.vn/chord/song/viet-nam-que-huong-toi/W8IUIOZO.html

## Trạng thái

Lõi HARD được giữ từ rule đã A/B; routing theo section-role, scope A/B và corpus lane là **PROVISIONAL**. Test tiếp theo: cùng một tứ+cốt, so arm cũ (scheme+open/bằng+tone-order) với arm mới (role-based+scope-correct), rồi nghe render và chấm phát âm/hát xuôi/tự nhiên.
