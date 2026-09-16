# Audit và đánh giá skill

Tài liệu này là router audit, không phải runtime sáng tác. Chỉ mở khi user yêu cầu kiểm tra/tối ưu skill, có failure artifact rõ, cần A/B với baseline/model khác hoặc cần đối chiếu corpus/thị trường.

Dùng audit cycle và release discipline bên dưới khi thay rule, chạy forward-test hoặc quyết định promotion/revert. Đọc `stage-validation-loop.md` khi cần định vị lỗi xuyên tầng.

## 1. Nguyên tắc lõi

- Định nghĩa mục tiêu, artifact và tiêu chí thành công **trước** khi xem bản mới.
- Đánh giá đúng thứ user sẽ nhận: Tứ/card, lyric sheet, rough demo, Suno render hay full-production candidate.
- Chấm từng tầng bằng artifact của chính tầng đó. Một arm thắng ở Tứ/Cốt/Song System chưa được tính là thắng lyric; một writer-pass lỗi cũng chưa đủ bác bỏ kiến trúc định hướng nếu lỗi xuất hiện sau handoff. Khi cần so quy trình, ghi riêng `direction quality`, `writer realization` và `music/render realization` trước verdict tổng.
- Ưu tiên outcome; trace chỉ dùng để tìm tầng sinh lỗi. Không bắt một đường thao tác cứng nếu nhiều đường đều cho kết quả hợp lệ.
- Tách kiểm tra “có làm được điều khó mới không” khỏi “có làm hỏng điều từng làm được không”.
- Một case phát hiện lỗi được phép giúp sửa rule, nhưng không được tự làm bằng chứng rằng rule đã tổng quát hóa.
- Đo **activation burden**, không chỉ độ dài tài liệu: bao nhiêu gate, field và sweep được buộc chạy trước khi model được viết? Rule buộc đặt tên nhiều trường phân tích có thể rò chính giọng phân tích ấy vào lyric.
- Khi một chuỗi patch làm đầu ra ngày càng đúng checklist nhưng lạnh/gượng hơn, ưu tiên xóa, hạ cấp thành diagnostic hoặc định tuyến theo triệu chứng trước khi thêm rule mới.
- Không dùng điểm tổng hợp để che hard fail như sai nghĩa, payoff vô quyền, ép vần, đạo cụ không provenance hoặc music-fit chưa được nghe.
- Model không tự chứng nhận “chạm”, “tươi”, “hit” hay “siêu phẩm”. Tai người giữ quyền ở cảm xúc, tự nhiên, nhớ hook và nghe–hát.

## 2. Bốn nguồn bằng chứng tách biệt

1. **Incident/live:** raw artifact và verdict người dùng. Dùng phát hiện failure và tạo test candidate; không đủ để promotion.
2. **Capability suite:** ca khó hoặc hành vi mới đang cần nâng. Có thể còn tỷ lệ fail cao.
3. **Regression suite:** ca đã từng pass hoặc failure đã sửa; giữ ổn định để bắt backslide.
4. **Sealed holdout:** brief mới, không mở khi viết rule hay sinh arm; chỉ dùng ở release gate.

`case-log.md` là recent-memory và nguồn incident, **không phải** eval suite. Corpus nổi tiếng là nguồn prior/phản-ví-dụ, **không phải** đáp án mẫu.

## 3. Cấp độ bằng chứng

- **Quarantined:** insight có thể đúng nhưng cơ chế, công thức hoặc nguồn có nguy cơ gây học thuộc/gây hại.
- **Provisional:** bắt từ artifact thật và có failure hypothesis, nhưng mới pass case sửa lỗi.
- **Candidate:** thắng capability A/B trên nhiều ca độc lập, grader đủ rõ; chưa mở sealed holdout.
- **Validated:** pass sealed holdout, không gây regression đáng kể ở các lane liên quan và có xác nhận tai người cho trục chủ quan.

“Validated” luôn gắn với scope, artifact và lane; không có rule validated cho mọi thể loại chỉ vì thắng Vpop ballad.

## 4. Audit cycle tối thiểu

1. **Freeze:** ghi version baseline, mục tiêu user, artifact, lane và failure symptom bằng chữ trung tính.
2. **Locate:** tìm tầng sớm nhất gây lỗi; phân biệt rule thiếu, rule có nhưng route hụt, grader sai hay brief mơ hồ.
3. **Design:** chọn capability + regression + holdout phù hợp; có cả ca rule phải bắn và ca rule không được bắn.
4. **Run clean:** mỗi arm ở fresh context/trial; chỉ đưa brief và material task-local, không đưa corpus, chẩn đoán, expected answer hay intended fix.
5. **Grade:** chạy hard invariants trước; sau đó rubric từng trục, blind pairwise và nghe artifact nếu claim liên quan âm nhạc.
6. **Inspect:** đọc raw output/trace và false positive; sửa eval nếu task hoặc grader phạt một đáp án hợp lệ.
7. **Patch low:** sửa ở tầng thấp nhất đủ giải quyết lỗi; ưu tiên xóa/hạ cấp/route theo triệu chứng trước thêm blanket rule.
8. **Release:** promotion chỉ khi candidate thắng đúng trục, sealed holdout pass và regression không thua theo hard gate.

### Harness context sạch (Giao thức đánh giá độc lập)

Quy trình forward-test chuẩn cho nhà phát triển khi audit skill:

- mỗi case × trial mở một context/sandbox sạch hoàn toàn riêng biệt;
- generator chỉ thấy snapshot skill và brief của đúng case;
- raw output được ghi lại trước khi chấm;
- grader chạy ở sandbox khác, chỉ thấy raw output, user brief, rubric và output schema; không thấy skill, chẩn đoán hay intended fix;
- deterministic scan chỉ là diagnostic nhanh, không thay semantic grader;
- chạy ít nhất ba trial độc lập để loại trừ tính ngẫu nhiên của LLM.

Không dùng output sinh và verdict trong cùng một session để làm bằng chứng promotion. Không đưa tên failure đang điều tra vào generator prompt; tiêu chí đó chỉ thuộc grader rubric.

## 5. A/B và grader stack

### A/B hợp lệ

- Cùng brief, material, model/harness và budget; chỉ thay một cụm rule hoặc một stage.
- Randomize/ẩn nhãn A–B; nếu model judge, đảo thứ tự để dò position bias.
- So raw artifact, không kèm lời biện hộ của arm.
- Với sinh mở, chạy nhiều trial; claim về độ ổn định cần ít nhất ba lượt độc lập mỗi case, hoặc phải ghi rõ `single-trial`.
- Ghi win/loss/tie, hard fail, trade-off và độ chắc của verdict; không chỉ giữ ví dụ thắng.

### Grader theo thứ tự

1. **Deterministic/hard gate:** format, section thiếu, contradiction, provenance, referent, scope A/B, marker hứa quá khả năng.
2. **Rubric một trục:** đúng brief, central intent, arc/payoff, tự nhiên, hook recall, prosody/music-fit. Cho phép `UNKNOWN` khi artifact không đủ.
3. **Blind pairwise:** người nghe hoặc judge chọn trên đúng một câu hỏi; không hỏi chung “bài nào hay hơn” khi cần biết nguyên nhân.
4. **Human/audio gate:** bắt buộc cho cảm xúc, singability, phát âm, flow, hook recall và production-fit.

Model judge chỉ là proxy. Phải hiệu chỉnh định kỳ với verdict người thật; khi lệch, tin raw artifact + người nghe và sửa rubric.

## 6. Corpus protocol

- Chọn mẫu đúng genre × mood × register, báo cỡ mẫu và tín hiệu đại diện/thành công.
- Chẩn phân bố chức năng: semantic skeleton, breadth, arc behavior, line role, hook stack, rhyme/prosody mode và production behavior nếu có audio.
- Tìm phản-ví-dụ cho cả hai chiều: khi một thủ pháp xuất hiện và khi nó vắng mặt mà bài vẫn thành công.
- Không suy lyric từ cốt MV; không lấy hook, đạo cụ, câu, skeleton đơn lẻ hoặc trope nổi tiếng làm seed.
- Sau khi distill prior, đóng corpus rồi mới chạy generation trong fresh context.
- Sample nhỏ chỉ tạo hypothesis; corpus không chứng minh một rule gây ra thành công thương mại.

Các audit chuyên biệt hiện có: `tu-corpus-audit-2026-07-18.md`, `cot-corpus-audit-2026-07-18.md`, `line-corpus-audit-2026-07-18.md`, `sound-rhyme-prosody-audit-2026-07-18.md`, `emotional-field-audit-2026-07-22.md`, `legacy-reference-audit-2026-07-18.md`, `b6-baseline-audit-2026-07-18.md`, `expert-process-audit-2026-07-18.md` và `audit-process-audit-2026-07-18.md`.

## 7. Audit động cơ liên tưởng từ bài mẫu

Chỉ chạy khi user yêu cầu học/đối chiếu reference hoặc failure cho thấy Tứ thắng nhưng nguồn liên tưởng nông. Chọn mẫu khác **cơ chế sinh nghĩa**, không gom nhiều bài cùng trope; luôn có negative control là một bài hay nhờ lời trực tiếp, declaration, groove/hook hoặc tự sự mà không cần hệ ảnh sâu.

Với mỗi mẫu, trích ở cấp chức năng:

`hạt nhân · nguồn sức căng · nguồn kết dính · cầu giữa các miền · cách nghĩa trở lại/biến đổi · scale/payoff · music/form implication`

Kiểm bằng bốn câu hỏi:

1. Điều gì thật sự giữ bài lại với nhau nếu bỏ danh từ/hình ảnh nổi bật?
2. Các liên tưởng xa được nối bằng quan hệ cảm xúc, văn hóa, nhân quả, cú pháp hay chỉ bằng từ gần nghĩa?
3. Một neo/refrain/tình thế trở lại có thêm nghĩa gì?
4. Sức mạnh nằm ở engine liên tưởng hay ở một lane khác mà skill không được ép thành hình tượng?

Chỉ rút quy trình tổng quát sau khi có ít nhất ba dạng đối chứng khác cơ chế. Đóng reference trước generation; không chuyển tên bài, lyric, hook, đạo cụ, tình tiết đặc trưng, bộ ảnh hoặc skeleton riêng sang arm mới. Forward-test phải dùng brief mới và kiểm cả hai chiều: route phải bắn khi liên tưởng cần sinh bài, và phải `N/A` khi direct/narrative đã đủ.

## 8. Case-log và release discipline

Chỉ đọc fingerprint gần nhất của `case-log.md` khi đang sinh một chuỗi ca, retest regression hoặc có dấu hiệu convergence. Một ca độc lập không tải lịch sử lỗi vào generation packet mặc định. Không đọc verdict/câu cũ để làm seed; không chép lại lyric đầy đủ.

Sau mỗi artifact, append: goal/entry · Tứ+skeleton · behavior · hook stack · demo status · session-overlap verdict · fingerprint `cot · line · sound · music · base` · verdict để trống. Sau nghe render, cập nhật phát âm, flow, hook recall, hard fail và verdict người nghe.

Trước khi đưa rule vào runtime:

1. Có failure hypothesis và stage owner.
2. Có ca positive lẫn negative; case sửa lỗi không nằm trong holdout.
3. Baseline/version được đóng băng; arm chỉ khác một biến hợp lý.
4. Capability tăng; regression không có hard fail mới.
5. Sealed holdout pass; claim âm nhạc có artifact nghe được.
6. Ghi scope, trade-off, bằng chứng và điều kiện revert.

Revert hoặc thu hẹp scope nếu rule tạo hard fail mới, bắn oan lặp lại, làm giảm tự nhiên/cảm xúc ở lane ngoài mục tiêu, hoặc chỉ thắng khi evaluator biết chẩn đoán.

Không khôi phục apparatus đã demote chỉ vì một ví dụ thắng.
