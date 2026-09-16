# Audit bốn reference của `songwriting` cũ (2026-07-18)

## Mục tiêu

Lọc tri thức còn dùng được mà không phục hồi hệ thống 14-rule. Audit đối chiếu với corpus tứ/cốt/câu 22 bài, case-log và các field-test Suno mới hơn. Tài liệu cũ chỉ là **nguồn giả thuyết/negative evidence**, không làm seed câu.

## Kết luận theo file

| File cũ | Giữ | Không chuyển sang flow | Quyết định |
|---|---|---|---|
| `../../songwriting/references/line-craft.md` | register làm đổi cú pháp; direct/điệp đúng ở anthemic và melodramatic; câu nối có chức năng | “mỗi câu = vật/hình + một device”, cấm phát-biểu, bắt đổi thủ-pháp mỗi đoạn, bậc-thang vết, ví dụ vật-vắng dễ gây convergence | Legacy-quarantine; insight register đã được line-role/craft-budget hấp thu |
| `../../songwriting/references/hook-title.md` | title placement; phân biệt title/hook; hook-first cho commercial; earworm là một đường hợp lệ | `≤7` thành luật, title luôn phải là câu đáng nhớ nhất, bridge luôn mở góc mới, semantic-integrity áp vào phonetic hook, GREAT checklist thiên semantic | Chỉ port title-placement; giữ hai đường semantic/phonetic của bản min |
| `../../songwriting/references/song-anatomy.md` | ranh giới lyrics vs melody/production; không tự hứa hit/kiệt tác | “density lái melody mạnh”, mô hình 25 thành phần tạo false precision, “lời chủ yếu là hygiene” không universal theo lane | Không dùng vận hành; Suno-index mới là nguồn ranh giới hiện hành |
| `../../songwriting/references/genres-formulas.md` | chức năng Post-Chorus/Drop/Rap break; form phi tuyến; phân biệt lyrics-first với melody-first | template số chữ D–I, “4 dòng bằng chữ không bao giờ”, chênh 2–3 chữ, đuôi luôn ngắn nhất, density chữa đều, tag buộc engine đổi melody | Port block theo chức năng; bỏ toàn bộ công thức mét/claim deterministic |

## Phản-chứng chính

1. Corpus có mainstream/anthemic sống bằng phát-biểu và điệp, nên image/device không phải đơn vị bắt buộc của mọi câu.
2. Bolero, folk litany và anthemic parallel cho thấy dòng đều hoặc frame lặp có thể là kiến trúc, không mặc định là monotony.
3. Nhạc vui/dance có phonetic hook; hook không cần semantic twist/payoff trong mọi trường hợp.
4. Field-test mới của chính skill xác nhận lyric density/tag chỉ tạo bias yếu; không được nói Suno “buộc” đổi melody.
5. Bridge và V2 thay đổi theo arc-behavior; không universal phải reveal/góc mới.

## Các thay đổi đã áp dụng

- Đặt bốn file vào legacy-quarantine; không tăng dependency từ 5 lên 9.
- Port bốn kiểu title placement dưới dạng lựa chọn chức năng.
- Port Post-Chorus/Drop/Rap break theo chức năng, không port template số chữ.
- Sửa chorus thành conditional theo form+mood và sửa claim Suno deterministic thành probabilistic.
- Scope tiêu chí chống-thơ-hóa cho V-C/pop; miễn chorus-bùng với AAA/vòng-tròn/through-composed/phổ-thơ sát.

## Gate tái sử dụng về sau

Một insight từ skill cũ chỉ được quay lại khi: (1) diễn đạt được mà không cần ví dụ chữ; (2) có lane/scope rõ; (3) không mâu thuẫn corpus/field-test mới; (4) nếu biến thành rule sinh — phải A/B với baseline. Nếu chỉ giúp phân tích, giữ trong reference và không bật lúc viết.
