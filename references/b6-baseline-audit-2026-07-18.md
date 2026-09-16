# Audit B6 — baseline non-regression (2026-07-18)

## Mục tiêu

Forward-test B6 trên một bài hoàn chỉnh để bắt tình trạng sửa cho “đúng kỹ thuật” nhưng làm lạnh, đổi register hoặc phá vai câu. Đây là bài tự sinh cho test nội bộ; không dùng câu/đạo cụ từ corpus. Verdict “chạm” vẫn chờ tai người.

## Brief cố định

- Lane: nhạc trẻ/Vpop ballad mainstream; tình yêu hậu chia tay; man mác, kìm nén; tight-meaning; hit-đại-chúng; Scope A.
- B1: hai người từng hiểu nhau gặp lại và từ thân thuộc thành khách sáo; ngỡ bình thản → nhận ra chính sự lịch sự đo khoảng cách đau nhất.
- Tứ: tương phản/reframe `thân thuộc → khách sáo`; độ rộng communal, không dựa thói-quen/đạo-cụ cá nhân.
- Cốt: gặp lại → trao những câu an toàn → nhớ độ hiểu nhau cũ → payoff “lịch sự mới là xa nhất”; `EVENT nhẹ + REFRAME`.
- Form: V1–Pre–Chorus–V2–Pre–Chorus–Bridge–Final Chorus. Hook semantic/title: **Lịch Sự Đến Đau Lòng**.

## Baseline coherent đầu tiên sau B5

### Lịch Sự Đến Đau Lòng

**[Verse 1]**  
Mình gặp nhau giữa con đường đông người  
Em mỉm cười như gặp một người quen  
Anh hỏi em dạo này công việc thế nào  
Em bảo mọi điều vẫn ổn như xưa

**[Pre-Chorus]**  
Không ai nhắc những ngày từng rất gần  
Không ai hỏi lòng còn đau hay không

**[Chorus]**  
Ta lịch sự đến đau lòng  
Từng biết nhau hơn cả chính mình  
Giờ mỗi câu đều vừa đủ  
Để chẳng ai phải lặng thinh  
Ta lịch sự đến đau lòng  
Chúc nhau yên vui rồi quay đi  
Hóa ra xa nhất không phải chia ly  
Mà là khi mình chẳng còn gì để hỏi

**[Verse 2]**  
Có một thời chỉ nghe một tiếng thở  
Đã biết người đang giấu chuyện gì  
Giờ em kể bằng vài câu ngắn  
Anh gật đầu như chuyện chẳng liên quan

**[Pre-Chorus 2]**  
Ta đã học cách không làm khó nhau  
Nên vô tình làm khó trái tim

**[Chorus]**  
Ta lịch sự đến đau lòng  
Từng biết nhau hơn cả chính mình  
Giờ mỗi câu đều vừa đủ  
Để chẳng ai phải lặng thinh  
Ta lịch sự đến đau lòng  
Chúc nhau yên vui rồi quay đi  
Hóa ra xa nhất không phải chia ly  
Mà là khi mình chẳng còn gì để hỏi

**[Bridge]**  
Nếu một ngày ta thôi cần giữ ý  
Liệu có còn điều gì để nói ra?  
Hay những lời mình chưa từng nói hết  
Đã theo lần từ biệt hôm qua

**[Final Chorus]**  
Ta lịch sự đến đau lòng  
Từng biết nhau hơn cả chính mình  
Giờ mỗi câu đều vừa đủ  
Để chẳng ai phải lặng thinh  
Ta lịch sự đến đau lòng  
Chúc nhau yên vui rồi quay đi  
Hóa ra xa nhất không phải chia ly  
Là nói rất nhiều mà chẳng chạm được nhau

## Sweep và đối chứng

| Slot | Option 0 — baseline | Candidate | Kết quả T1–T3 |
|---|---|---|---|
| V1.3 | Anh hỏi em dạo này công việc thế nào | Anh hỏi dạo này em sống thế nào | Candidate bớt văn xuôi, nối trực tiếp vào truth quan hệ; không đổi register → **T4 người chọn B**, `REPLACE` |
| V1.4 | Em bảo mọi điều vẫn ổn như xưa | “Mọi thứ vẫn bình thường” — em nói | Candidate tạo spoken-seam và kịch hóa không cần thiết; baseline đang gánh setup/plain-line → `KEEP-BASELINE` |
| C.4 | Để chẳng ai phải lặng thinh | Không câu nào đi quá xã giao | Candidate giải thích tứ quá lộ, dùng từ hành chính và lạnh hơn → `KEEP-BASELINE` |
| Pre2 | Ta đã học cách không làm khó nhau / Nên vô tình làm khó trái tim | Ta đã học cách nhìn nhau bình thản / Chỉ không ngờ bình thản cũng làm đau | Candidate qua T1–T3 nhưng **T4 người chọn A** → `KEEP-BASELINE`; kiểm kỹ thuật không được lấn át tai người |
| Bridge 3–4 | Hay những lời mình chưa từng nói hết / Đã theo lần từ biệt hôm qua | Hay mình chỉ còn câu chào rất khẽ / Để một người đi, một người nhìn theo | Candidate thêm cảnh chia tay mới, đổi cốt từ gặp-lại sang melodrama và cá nhân hóa → `KEEP-BASELINE` |

## Bản cuối sau T4

Verdict người ngày 2026-07-18: `1B · 2A`. Chỉ thay một vị trí:

- V1.3 → `Anh hỏi dạo này em sống thế nào`
- Pre-Chorus 2 → giữ baseline `Ta đã học cách không làm khó nhau / Nên vô tình làm khó trái tim`

Không thay bốn vị trí còn lại dù đã flag hoặc candidate qua T1–T3. Đây là bằng chứng trực tiếp rằng `flag ≠ phải sửa`, plain/setup line có thể thắng candidate nhiều craft hơn, và **model-pass ≠ human-pass**.

## Stage fingerprint

`[FP cot=gap-lai→safe-talk→remember-closeness→politeness-reframe+EVENT-light/REFRAME; line=direct-contrast+semantic-refrain; sound=verse-loose/chorus-refrain+Scope-A; base=PASS]`

- TỨ: PASS — một social-state broad, không anchor cạnh tranh.
- CỐT: PASS — payoff phát biểu lại đúng tứ; bridge không bắt twist mới.
- LINE: PASS — direct/plain làm hạ tầng, hook/reframe làm đòn bẩy.
- SOUND: PASS có điều kiện Scope A — đọc-to và biên từ ổn; chưa được tự chấm tone↔melody.
- BASELINE-NONREGRESSION: **PASS** — người chọn `1B · 2A`; bản cuối chỉ nhận sửa đổi thắng tai người. Đây là PASS ở tầng lời; phát âm/flow vẫn chờ render.

## Lỗi quy trình phát hiện và bản vá

1. `sửa TẤT CẢ câu đã flag` biến diagnostic thành án sửa, tái tạo over-polish → đổi thành ba verdict `KEEP/REPLACE/PENDING` và luôn giữ option 0.
2. Plain/setup line dễ bị coi là “ít craft” rồi sửa oan → buộc chấm vai cấu trúc trước line-level beauty.
3. `A→B` còn sót trong checklist dù B3 đã công nhận SUSTAIN/GROOVE/LITANY/CYCLE → đổi checklist sang arc-behavior.
4. Baseline có thể bị model tự ghi PASS trước verdict người → bắt buộc `PENDING-HUMAN` cho đến T4. Ca này xác nhận guardrail: Pre2 candidate qua T1–T3 nhưng người vẫn chọn baseline.

## Test kế tiếp

Render bản cuối để điền phát âm/flow. Chưa có render thì không thăng các rule provisional về âm/vần/điệu hoặc Suno handoff.
