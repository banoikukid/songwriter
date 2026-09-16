# Ý tưởng và cấu trúc

## Mục lục

1. Brief sáng tác
2. Chọn cửa vào
3. Sinh và chọn Tứ
4. Kiến trúc liên tưởng
5. Chọn engine phát triển
6. Hook đi cùng Form
7. Dựng Cốt
8. Chế độ tham vọng phá cách

## 1. Brief sáng tác

Chốt tối thiểu các tín hiệu cần cho bài; không biến danh sách này thành worksheet bắt buộc:

- **Goal + người thể hiện/nghe:** personal, artist release, commercial, sync, live/cộng đồng hay demo; giọng/range/POV nào nếu biết.
- **Chủ đề + người nói/người nghe:** ai nói với ai, ở giai đoạn hay quy mô nào.
- **Material/provenance:** chỉ khóa khoảnh khắc, hành vi, câu nói, quan hệ hoặc dữ kiện khi user chủ động cấp. Không yêu cầu nguồn đời tư của tác giả; nếu không có material, được dựng persona/tình huống hư cấu đúng brief và không trình nó như sự thật của user.
- **Mood/năng lượng:** buồn, man mác, ấm, vui, sôi động, chiêm nghiệm, hùng tráng.
- **Mục tiêu nghĩa:** tight-meaning, mood-with-turn hay pure mood-wash.
- **Register:** hit đại chúng, literary/indie hay tham vọng.
- **Music genre/production:** nếu user/audio/reference đã xác nhận, dùng để định form, density, groove space, diction và prior vần; nếu chưa có thì giữ `UNKNOWN`, không suy mood hoặc domain từ genre tưởng tượng.
- **Lyric tradition + expression lane:** chốt từ brief, register, seed và artist voice; bảng genre provisional không được tự chọn thay các bằng chứng này.

Tình yêu nhạc trẻ cần biết giai đoạn: crush, mập mờ, đang yêu, rạn vỡ hoặc hậu chia tay. Quê hương cần biết quy mô và địa phương hay toàn quốc. Thiếu dữ kiện nhưng user yêu cầu làm ngay thì nêu giả định ngắn, không lặng lẽ tự lấp.

### Generation-packet hygiene

Phân biệt **material** với **câu minh họa**. Câu thoại, thói quen, mốc giờ, đạo cụ hoặc vi cảnh do model tự đặt để giải thích một brief không tự trở thành lyric seed. Trước writer-pass:

1. Giữ nguyên chữ chỉ với material user cấp hoặc motif user cho phép sáng tạo và khóa lại.
2. Với ví dụ do model tự thêm, xóa bề mặt câu và nén về chức năng quan hệ, như `né tránh đối thoại`, `lời nói mất độ gần`, `một bên mời gọi — một bên chưa hồi đáp`.
3. Chỉ chuyển chức năng này qua `section job → immediate utterance → phrase → từ`; không paraphrase ví dụ, đổi đại từ hoặc dựng cặp đối xứng từ nó.

Nếu bỏ câu minh họa mà Tứ/Cốt không còn sinh được section, hướng đó chưa đủ Generate. Đào lại trục thay vì cho ví dụ làm nạng. Quy tắc này không xóa material cụ thể có provenance và không cấm model sáng tạo cảnh mới trong rough pass.

### DOMAIN-SENSE — khóa nghĩa trước khi sinh Tứ

Khi input chỉ là title/cụm ngắn và có thể chỉ nhiều miền, fan-out **cách hiểu** trước khi fan-out ý tưởng. Tách tối đa hai hoặc ba sense thực sự khác ở người nói–người nghe và quy mô quan hệ, chẳng hạn đôi lứa, thân hữu/nghĩa khí, gia đình/cộng đồng hoặc nhân tình thế thái. Đây chưa phải ba Tứ; mỗi sense có thể sinh nhiều Tứ sau đó.

Chọn sense bằng toàn cụm từ, sắc thái văn hóa, register, genre đã được user/audio/reference xác nhận, lyric tradition, lời user và prior đã được kiểm chứng. Không suy genre từ title rồi dùng chính genre đó để chứng minh sense; không lấy một từ khóa riêng làm proxy cho domain. Các từ chỉ tình cảm, duyên phận, nghĩa hoặc đời có thể đổi nghĩa theo tổ hợp.

Nếu hai sense còn ngang nhau và dẫn tới người nói–người nghe, stakes hoặc quy mô bài khác hẳn, đây là **blocking ambiguity** cho full lyric: trình hai lựa chọn bằng một dòng/sense và lấy lựa chọn trước khi viết. Không bắt user chọn khi khác biệt chỉ là sắc độ hoặc có thể cùng tồn tại trong một Tứ. Khi user yêu cầu draft ngay/một lượt, được tự chọn một sense nhưng phải ghi rõ giả định; có thể đưa hai seed ngắn thay vì giả vờ title đã tự quyết định.

Khi reference hoặc phản hồi sau đó cho thấy bài đã viết đúng kỹ thuật nhưng sai miền nghĩa, gắn `DOMAIN-SENSE FAIL` và quay về Brief. Không cứu bằng đổi danh từ, thêm một Verse hoặc polish hook; phải reseed Tứ/Cốt trong sense đúng.

Khóa **domain contract** trước khi fan-out. Không tự nhập một vấn đề ngoại miền như khí hậu, chiến tranh, công nghệ hoặc bệnh tật chỉ để làm chủ đề khó, thời sự hay mới hơn. Chỉ mở miền phụ khi user/seed đã gọi nó, hoặc khi cả ba điều cùng đúng: có cầu nhân quả/văn hóa rõ; nó làm sâu đúng cảm xúc đích; bỏ nó đi sẽ làm mất central intent chứ không làm bài trở lại tự nhiên hơn. Nếu miền phụ trở thành thứ bài đang thật sự bàn, quay lại Brief.

Prior cảm xúc không phải từ điển bắt buộc. Chẳng hạn, quê hương phổ thông thường hút về ký ức, thuộc về, cội nguồn, nhớ thương hoặc trở về; sông, lũy tre, câu hò, mùa màng hay tiếng biển chỉ có giá trị khi được ký ức hóa hoặc mang quan hệ văn hóa. Không rải chúng như danh mục cảnh vật, và không chuyển sang khí hậu/địa chính trị nếu brief không chủ ý đi vào mất quê, thiên tai hay lưu vong.

Nén brief theo một trong hai lane:

> **Utterance-led:** Trong [tình thế], [ai] nói với [ai], cảm xúc/nhận thức đi từ [A] đến [B], để người nghe [nhận/cảm điều gì].

> **Field-led:** Từ [hạt nhân], cảm xúc lan qua [thời gian/không gian/hệ hình] theo [chuyển động], để người nghe ở trong [trạng thái].

Lane hỗn hợp được phép: nhân vật mở cửa, emotional field khuếch đại, rồi hook đưa tai về người hát. Không dùng `field-led` để né quan hệ hoặc biến bài thành phong cảnh.

### SEED-BEHAVIOR AUDITION — title cần được trả lời hay được ngân rộng?

Với title/hình tượng mở, thử ngắn hai khả năng trước khi khóa Tứ: material đang chứa một câu hỏi, thay đổi hoặc nghịch lý cần **resolution/transform**; hay đang mở một trạng thái cần **resonance/sustain** qua nhiều lần trở lại. Đây không phải hai form bắt buộc và không mặc định phải xuất hai phương án. Chỉ giữ song song tới pilot khi cả hai có bằng chứng từ brief/material và sẽ tạo lyric behavior khác hẳn.

Đừng dùng độ dễ tóm tắt làm tiêu chí thắng. Hướng resonance vẫn Generate khi trường cảm xúc có lực hút rõ, mỗi lần trở lại mở thêm mặt khác của trạng thái và form/music đủ gánh biến thiên; nó không cần một cú nhận ra cuối bài. Ngược lại, title giàu hình ảnh không tự chứng minh field-led: khi người hát thật sự cần tỏ tình, hỏi, kể hoặc lựa chọn, utterance-led được quyền thắng.

Với resonance/constellation, giữ central intent như la bàn hậu trường. Không biến nó thành câu định nghĩa title, bảng ánh xạ từng ảnh/màu với một cảm xúc, hay kết luận đạo lý. Chọn bằng pilot của chính behavior ấy, không chấm nó bằng tiêu chí Chorus trả lời rõ như declaration.

Với tình ca pop/mainstream **đã được brief/reference xác nhận** và mang title thời tiết, mùa, cảnh vật hoặc biểu tượng, có thể thử **MIXED** như một arm đầu tiên: title thường là bộ khuếch đại cảm xúc, hoàn cảnh hoặc refrain, chưa chắc là chủ thể kể chuyện. Đây là fan-out prior, không phải gate. Khi brief khóa `EXTERNALIZED` hoặc material/reference cho thấy cả một trường hình tượng đang gánh cảm xúc, audition song song `FIELD-DOMINANT`; không để thứ tự thử biến thành verdict.

Không nén được thì chưa polish. Seed vẫn được phép thu/phác để khỏi mất ý.

## 2. Chọn cửa vào

Không có một thứ tự sáng tác duy nhất. Chọn entry theo artifact mạnh nhất:

| Entry | Bắt đầu bằng | Constraint đầu tiên |
|---|---|---|
| TITLE/LYRIC | title, câu, Tứ, story | central intent, semantic emphasis, section function |
| MELODY | hum, motif, topline, demo | contour, phrase, range, melodic stress |
| GROOVE/TRACK | beat, bass, loop, production hook | pocket, subdivision, density, phrase grid |
| CHORD/HARMONY | loop/progression, tonal tension | stable/unstable, harmonic rhythm, cadence |
| BRIEF/STORY | artist/sync/scene/audience brief | goal, POV, facts, emotional turn |
| COWRITE | seed của nhiều người | role, authorship, shared intent, version control |

Ghi seed ngay bằng chữ, hum/voice memo hoặc sketch rẻ. Với melody-first có thể giữ nonsense syllable tới khi contour và range ổn rồi mới đặt lời. Với reference/market brief, chỉ mine function, energy, form và production space; không lấy lyric, hook, đạo cụ hoặc skeleton.

Mọi entry hội tụ ở central intent và prosody; không buộc title phải có trước melody hoặc ngược lại.

## 3. Sinh và chọn Tứ

Tứ là **trục sinh bài**, không phải khẩu hiệu “yêu, nhớ, đau”. Nó phải tạo được chuyển động hoặc hệ liên tưởng đủ kéo nhiều section.

### MOTIF DISCOVERY — khám phá động trước khi chọn

Chạy khi user chưa khóa Tứ, input mỏng/hình ảnh hoặc bản vừa sinh rơi lại một mô-típ quen. Đây là bước suy luận từ material, không phải chọn trong danh mục mô-típ có sẵn.

1. **Giữ biên chứng cứ:** tách material có provenance, cảm giác/quan hệ user yêu cầu và phần model mới suy ra. Một người đứng một mình, sắc trời buồn hay một con đường không tự chứng minh chia xa, chờ đợi hoặc mong gặp lại.
2. **Đọc khả năng nghĩa:** hỏi material đang chứa sức căng nào; điều gì đổi mà điều gì còn; chi tiết nào có thể đảo nghĩa; chuyển động, nghịch lý, chu kỳ hoặc ngưỡng nào có thể trở thành lực sinh bài. Đây là câu hỏi khám phá, không phải các ô phải điền hay các họ mô-típ cố định.
3. **Sinh bốn đến sáu giả thuyết:** nén mỗi hướng thành `material/pressure → cơ chế cảm xúc → turn/payoff`. Các hướng phải khác ở điều khiến cảm xúc vận động, nhận thức được đổi hoặc lựa chọn được đặt ra; đổi POV, đạo cụ, phong cảnh hay genre chưa đủ. Đừng để cả bộ chỉ là nhiều câu trả lời hoặc nhiều cách diễn đạt cho cùng một nhận xét về đề tài. Khi sinh một bộ nhiều Tứ, audition cả hướng không cần lật nghĩa—chẳng hạn tích lũy lớp nghĩa, duy trì/khuếch đại trạng thái, tuần hoàn đào sâu, tuyên ngôn, tự sự hoặc trường cảm xúc—nếu material thật sự cho phép; đây là phép mở tìm kiếm, không phải quota bắt mọi bài dùng đủ engine.
4. **Khử trùng skeleton:** bỏ tên người, danh từ, đạo cụ và mỹ từ; rút mỗi hướng về `nguyên nhân → chuyển động → payoff`. Hai hướng còn cùng quan hệ nhân quả là một mô-típ. Kiểm thêm **REFRAME-COLLAPSE** ở cấp bộ: nếu từ ba hướng trở lên chỉ khác tiền đề/hình ảnh nhưng đều sống nhờ cùng cú `tin/tưởng A → nhận ra B`, `không phải A → mà là B`, `từng A → giờ B` hoặc một phép phủ định–đảo nghĩa tương đương, gộp chúng như một họ rồi reseed từ khả năng nghĩa chưa dùng. Chấm cơ chế trung tâm, không đếm từ `nhưng/không/mà`; một câu có tương phản phụ không tự biến cả Tứ thành REFRAME.
5. **Phát triển trước khi chọn:** giữ lại một vài skeleton khác gốc và mở mỗi hướng vừa đủ thành `nguồn sức căng/kết dính → chuyển động qua form phù hợp → lần trở lại/payoff`. Đây là arm card nhỏ, không phải lyric hay kho ảnh. Thường giữ một hoặc hai ứng viên qua vài vòng; không khóa nhánh chỉ vì câu pitch đầu nghe thuận.
6. **Đối chiếu tuyệt đối rồi mới đối chiếu cặp:** một hướng chỉ sống khi tự nó đủ emotional credibility, Generate, material necessity và music/brief fit. Sau đó mới chọn tương đối giữa các hướng còn sống. Nếu có thể thay toàn bộ seed bằng bất kỳ ảnh/title cùng mood nào mà Tứ không đổi, hoặc arm thắng vẫn chỉ là một nhận xét kéo dài, reseed; “tốt nhất trong nhóm” không đồng nghĩa “đủ tốt để viết”.
7. **Đóng bộ trước khi xuất nhiều Tứ:** rút lại skeleton của toàn bộ set sau vòng chọn, không tin vào nhãn engine model vừa đặt. Đánh dấu một hướng là reframe chỉ khi cú đổi nghĩa/đối cực là thứ làm payoff có lực; nếu bỏ cú lật mà hướng vẫn phát triển bằng tích lũy, duy trì, tuần hoàn, tuyên ngôn, tự sự hay field thì không đánh dấu. Nếu có từ ba hướng được đánh dấu, giữ tối đa hai hướng mạnh và reseed phần dư từ khả năng nghĩa chưa dùng; chạy lại closure cho tới khi còn dưới ba. Bỏ qua ngưỡng này chỉ khi user khóa toàn set vào reframe. Đây là kiểm hậu trường; không xuất bảng đếm hay lời tự chấm cho user.

Chỉ sau khi đã có các skeleton khác gốc mới gắn nhãn chiến lược nếu cần:

- **Đại chúng:** cửa vào rộng, hiểu ngay.
- **Tươi:** đổi nguyên nhân, nhận thức hoặc lựa chọn; không chỉ đổi đạo cụ.
- **Tham vọng:** chỉ khi user gọi rõ; có sức nặng và universal lift.

Các nhãn này là mức tiếp cận/rủi ro, không phải ba Tứ và không chứng minh motif diversity. Các kỹ thuật như ẩn dụ kéo dài, image/place-anchor, tình huống, tương phản, nhân vật/điển tích, definition/litany, chiêm nghiệm hoặc tự sự chỉ là phương tiện triển khai **sau khi chọn cơ chế**; không dùng chúng làm menu để thay thế suy luận.

`REFRAME` vẫn là engine hợp lệ và có thể thắng khi seed/brief làm cú nhận ra cần thiết. Nếu user yêu cầu rõ cú lật hoặc cấu trúc đối lập, giữ ít nhất một arm đáp ứng; chỉ tránh để các arm còn lại giả đa dạng bằng cách lặp cùng phép lật. Nếu user yêu cầu mọi phương án đều khảo sát những biến thể reframe, coi đó là scope chủ ý và chấm diversity bên trong scope ấy thay vì áp ngưỡng cấp bộ.

Chọn bằng sáu câu hỏi, không biến chúng thành worksheet bắt buộc phải xuất ra:

1. **Emotional credibility:** tình thế, phản ứng và giọng kể có logic cảm xúc đủ rõ để muốn nghe tiếp không, bất kể là tự sự thật hay persona hư cấu?
2. **Generate:** có sinh được nhiều vai đoạn hoặc một behavior sustain/declaration đủ biến thiên, hay chỉ là một câu nhận xét kéo dài?
3. **Music/brief fit:** có đúng lời hứa của đề và tạo được điểm rơi trong genre/seed âm nhạc không?
4. **Material necessity:** title, hình, câu hoặc artifact này có tham gia vào cơ chế, hay chỉ trang trí cho một bài có thể viết từ bất kỳ seed nào?
5. **Return/progression:** lần trở lại có thể thêm lực, đổi nghĩa hoặc mở quy mô, hay Verse–Chorus–Bridge chỉ nhắc lại cùng một luận điểm?
6. **Freshness:** giữa các phương án đã qua năm câu trên, hướng nào ít lặp ca gần đây hơn ở nguyên nhân, lựa chọn, hook hoặc cách phát ngôn?

Freshness là tiêu chí chọn sau khi đã có cảm xúc, không phải hard gate đứng trên độ ấm. `Pressure/cost` chỉ là diagnostic khi rough lyric nghe lạnh, lý giải hoặc thiếu lý do cất lời; không bắt mọi Tứ và mọi section phải khai báo hai trường này.

Một mô-típ quen được giữ làm arm đối chứng và vẫn có thể thắng khi brief/provenance thực sự đòi nó. Sự quen thuộc tự nó không phải điểm cộng; cũng không cấm chia xa, gặp lại hay hồi tưởng khi đó chính là quan hệ user đã cho.

Gắn nhãn đúng:

- Fail Generate → **Ý-CHUNG**, đào lại.
- Các phương án khác chữ nhưng rút về cùng nguyên nhân–chuyển động–payoff → **MOTIF-COLLAPSE**, quay bước đọc khả năng nghĩa.
- Arm quen thắng chỉ vì dễ hình dung dù material không chứng minh → **BASELINE-AUTOPILOT**, reseed; không chữa bằng đổi đạo cụ.
- Qua Generate nhưng model/case-log/corpus cùng hội tụ → **BASELINE-TROPE**. Mainstream vẫn được dùng nhưng không gọi là lợi thế sáng tạo.
- Chỉ quanh việc hai người ở lại với nhau, không có ý nghĩa rộng hơn trong mode tham vọng → **DYAD-CLOSED/COMPETENT**.

### ASSOCIATION-ENGINE DISCOVERY — chỉ khi liên tưởng phải sinh bài

Chạy khi arm còn là khẩu hiệu/nhận xét, khi material có nhiều khả năng nghĩa cần tìm nguồn kết dính, khi reference được dùng để học **cơ chế** liên tưởng, hoặc khi expression target đã khóa `EXTERNALIZED/FIELD-DOMINANT`. Chỉ bỏ qua nếu một tình thế trực tiếp, declaration, groove/hook hay tự sự đã đủ sinh bài **và** brief không yêu cầu field/carrier gánh cảm xúc; không coi mạng hình tượng là chuẩn cao hơn, cũng không dùng negative control để hạ target user đã khóa.

Tách **khám phá ứng viên** khỏi **chọn carrier**. Liên tưởng từ vựng, công năng, giác quan, thành ngữ, biểu tượng văn hóa và cả nối ngẫu nhiên đều hợp lệ ở fan-out: chúng mở không gian tìm kiếm nhưng không tự có trọng lượng chứng cứ. Firewall chỉ đặt ở hội tụ—không ứng viên nào được thắng chỉ vì tên của nó gần từ cảm xúc, công năng của nó giống một động tác vật lý hoặc nó chung một thuộc tính bề mặt.

1. **Đặt câu hỏi sinh nghĩa:** hỏi điều gì đang mâu thuẫn, điều gì đổi mà điều gì còn, một hành động có thể đổi nghĩa ra sao, hoặc vì sao giọng hát phải cất lên lúc này. Không bắt đầu bằng “danh từ nào đẹp?”.
2. **Fan-out quan hệ:** mở các sức căng, hệ quả, thế đối, vai xã hội, cộng hưởng văn hóa, chuyển thời gian, đổi quy mô hoặc khả năng đảo nghĩa thật sự có cầu từ seed. Liên tưởng từ vựng/công năng được phép vào đây như đầu mối ứng viên, không phải kết luận. Nếu tìm kiếm cứ quay về cùng một trường thị giác, tạm khóa giác quan đang thống trị rồi dò âm thanh, xúc giác, nhịp thân thể, khoảng cách không gian hoặc một kênh khác hợp seed. Đây là các phép dò, không phải quota hay menu phải dùng đủ.
3. **Tìm nguồn kết dính:** xem nghĩa đang được sinh bởi một tình thế hội tụ, vật/hình tượng chịu tải, động từ/lời gọi mở tầng, chuỗi ảnh tiến nghĩa, constellation cùng lực hút, place-anchor, declaration khuếch đại, cú pháp/refrain biến đổi hay một cơ chế khác. Tên dạng chỉ dùng để nhận ra sau khi đã thấy quan hệ; không chọn nhãn trước rồi điền ảnh.
4. **Fan-out rồi hội tụ:** phát triển hai hoặc ba cụm quan hệ thêm một tầng; tìm tình thế, hành động, cấu trúc hoặc hình tượng nằm ở giao điểm của các nhánh tương thích. Chuỗi công năng/từ điển kiểu `khái niệm → động tác vật lý → đồ vật nhận tác động` được phép đề cử ứng viên nhưng không được tự chọn nó. Với mỗi ứng viên cụ thể còn sống, tách ba đến năm hành vi, quy luật, chu kỳ, nghịch lý hoặc biến đổi có thật; chỉ giữ khi ít nhất một cơ chế có cầu với hạt nhân cảm xúc và sinh được chuyển động qua section. Độ sâu đến từ cơ chế và nhiều quan hệ có căn cứ cùng hội tụ, không từ khoảng cách từ vựng.
5. **Thử main-only trước:** chọn một trục chính và phát triển nó qua các section. Chỉ thêm một trục phụ khi nó bổ sung một chức năng thiếu—sức ép, bằng chứng, chuyển nghĩa, độ mở hoặc hook—và deletion-test cho thấy bỏ nó làm bài yếu đi. Trục phụ không được mở một bài cạnh tranh.
6. **Kiểm lần trở lại:** xác định điều gì xuất hiện hoặc được gọi lại ở Verse/Chorus/Bridge/Final và mỗi lần thêm nghĩa gì. STATE/SUSTAIN có thể tăng lực hoặc dư vang thay vì plot; DIRECT/DECLARATION có thể khuếch đại bằng nhiều chứng thực mà không cần hệ ảnh.
7. **Dừng hoặc reseed:** PASS khi nguồn kết dính làm material cần thiết, sinh được form phù hợp và không cần giải thích cơ chế trong lyric. Loại ứng viên chỉ chung mood, một thuộc tính bề mặt hoặc một lối tắt biểu tượng quen nếu các bước sau không đào ra được cơ chế mạnh hơn. Nếu mọi arm chỉ khác bề mặt, hình tượng thay thế tùy ý hoặc người thắng chỉ tốt tương đối, quay câu hỏi sinh nghĩa.

### MATERIAL AFFORDANCE AUDITION — tuyển nguyên liệu trước khi sinh Tứ

Chạy route này khi user yêu cầu ngân hàng nguyên liệu/liên tưởng đa tầng; khi fan-out còn nhiều carrier cụ thể ngang nhau; hoặc khi expression lane đã chọn chỉ sống nếu một vật, âm thanh, không gian hay hình tượng gánh được cảm xúc. Ghi `N/A` khi declaration/direct speech đã đủ lực, tự sự đã có material provenance rõ, hoặc lý do duy nhất là làm lời “thơ hơn”.

1. **Chốt việc cảm xúc trước vật:** material cần chứng minh quan hệ, giữ dấu vết, tạo chuyển độ, mở không gian, mang âm hình hay làm hook? Đừng bắt đầu bằng danh sách vật đẹp.
2. **Mở ứng viên khác loại:** vật thể, tình thế, âm thanh, thời gian, quan hệ, chuyển động và cả phương án `DIRECT/NO-OBJECT`. Không đặt quota và không bắt mọi miền phải có đại diện.
3. **Audition theo ngữ cảnh:** so tương đối bằng sáu khả năng: hành vi/chuyển động tự nhiên; điện tích cảm xúc đã có trong văn hóa hoặc tình thế; relation anchor; độ mở liên tưởng; khả năng thành phrase/âm hình; và mức gượng phải trả để dùng nó. Không chấm số, không đòi một ứng viên thắng cả sáu.
4. **Probe nhỏ rồi xóa chữ thử:** chỉ khi cần, thử một vai section, một chuyển động hoặc micro-phrase để nghe affordance. Probe là dụng cụ tuyển chọn, không phải seed lời; sau verdict chỉ giữ `vai → hành vi tự nhiên → relation anchor`.
5. **Hội tụ thành shortlist đa dạng:** giữ ít ứng viên thật sự khác chức năng. Khi user cần chọn, gắn `LOCKED · PREFERRED · AVAILABLE · REJECTED` và provenance `USER MATERIAL · MODEL CANDIDATE`; không biến mọi mục còn lại thành vật liệu bắt buộc của bài.
6. **Tôn trọng provenance:** material user khóa không bị loại chỉ vì đời thường, kỹ thuật hoặc mạnh âm. Tìm chức năng, genre, ký ức hay cadence làm nó cần thiết; nếu vẫn xung đột brief thì nêu xung đột và xin đổi, không lặng lẽ thay bằng một vật “mềm” hơn.

Không có whitelist/blacklist vật thể. Một `bờ vai` có thể thắng vì nghiêng/tựa, khoảng cách thân mật, khả năng mở sang không gian và âm hình; một `mái tôn` cũng có thể thắng khi tiếng mưa, căn nhà hoặc ký ức có provenance làm nó không thể thay. Nếu không carrier nào thắng phương án trực tiếp, viết trực tiếp. Audition này tuyển **khả năng sinh nghĩa và sinh câu**, không chọn mỹ từ; Tứ và LLM vẫn quyết định cách biến material thành bài.

Khi học từ reference, chỉ trích `hạt nhân → nguồn kết dính → cầu giữa các miền → cách trở lại/biến nghĩa → payoff/scale`. Sau đó đóng reference và bỏ toàn bộ lyric, hook, đạo cụ, danh từ, tình tiết đặc trưng cùng skeleton riêng khỏi generation packet. Một reference thuộc dạng mới phải được phép cho thấy một engine mới; không ép nó vào các tên dạng đã biết.

### Chống rập khuôn

Khi đang viết một chuỗi ca trong cùng phiên, đọc fingerprint gần nhất trong `case-log.md`; một ca độc lập không phải tải lịch sử lỗi vào seed packet mặc định.

Mọi ví dụ trong skill, reference và case-log chỉ giải thích luật, không làm seed. Chạy test bỏ danh từ: nếu “pha hai ly”, “gọi hai phần”, “mua hai vé” cùng rút về một quan hệ nhân quả thì đó là một tứ, không phải ba.

Corpus chỉ được mở khi audit hoặc user yêu cầu đối chiếu thị trường. Học phân bố, độ rộng và music-fit; đóng corpus trước khi generation. Không dùng tên bài, câu hook, đạo cụ hay một skeleton cụ thể làm seed.

### SESSION-DECONTAMINATION — chống nhiễm có điều kiện trong chuỗi bài

Dùng khi phiên hiện tại đã sinh ít nhất một lyric khác **và** có tín hiệu trùng cụ thể: user nghe ra lặp; seed/Tứ mới hội tụ về skeleton, payoff hoặc hook grammar cũ; hay rough pass lặp một cụm trường từ/cadence nhận ra được. Việc bài cũ còn trong context chỉ là rủi ro, chưa tự kích hoạt fingerprint.

Trước khi fan-out Tứ, nén các bài trong phiên thành **session-negative fingerprint**, chỉ giữ:

- semantic skeleton và payoff;
- engine + speech-act progression;
- hook grammar/title placement;
- trường từ nội dung và thế đối lặp;
- cadence/độ dài câu nổi trội nếu chúng đang tạo cùng một giọng.

Không đưa toàn văn bài cũ, câu hay hoặc danh sách phương án sửa vào generation packet. Khi đã có overlap evidence, packet sạch chỉ mang **phần fingerprint đang trùng** cùng brief mới, seed có provenance, music constraint và motif được user chủ ý cho phép tái diễn; không truyền toàn bộ fingerprint đề phòng. Chưa có overlap evidence thì generation packet không mang fingerprint.

Chọn lại Tứ nếu topic mới nhưng vẫn chạy cùng quan hệ nhân quả, cùng payoff và cùng cách Chorus tuyên bố. Chọn carrier hoặc behavior khác khi chính chúng đang gây hội tụ. Không bắt mọi tầng đều khác: form Vpop, đại từ, từ chủ đề thiết yếu và ngữ pháp tự nhiên có thể trùng; điều cần tránh là **cụm nhiều tầng cùng hội tụ** khiến người nghe nhận ra bài cũ dưới tên mới.

Kết quả:

- **PASS:** khác ở gốc phát triển; bề mặt chưa tạo cụm lặp đáng chú ý.
- **RESEED:** trùng skeleton/payoff/hook grammar; quay Tứ/Cốt.
- **REWRITE:** gốc khác nhưng section dùng lại kho câu/cadence; đổi speech act hoặc cách dựng câu ở section đó.
- **ALLOW:** sự lặp là motif album/series, reprise hoặc yêu cầu rõ của user; ghi phạm vi được phép.

Không giải quyết bằng blacklist từ đơn hay thay đồng nghĩa máy móc. Cách đó thường làm ca từ gượng mà logic cũ vẫn còn. Decontamination chỉ chống lặp cấu trúc; nó không được ép bài xa khỏi trường cảm xúc tự nhiên hoặc làm bản mới lạnh hơn baseline.

### Ẩn dụ kéo dài

Sustain không đồng nghĩa saturation:

- Chạy **STRIP-CONCEIT**: bỏ từ miền ẩn dụ; mỗi section vẫn phải còn hành động, stakes hoặc nhận thức khác.
- Khóa **MODE**: nghĩa bóng không được bỗng biến thành đạo cụ thật ở Bridge nếu cảnh thật chưa được dựng.
- Với mainstream, giữ conceit ở hook và vài điểm trở lại; quan hệ người thật gánh thân bài.

## 4. Kiến trúc liên tưởng

Đây chủ yếu là **lăng kính sửa bài**, không phải sơ đồ ảnh bắt buộc trước khi viết. Khâu khám phá nguồn kết dính nằm ở `ASSOCIATION-ENGINE DISCOVERY` của mục 3; nếu Tứ đã qua bằng lời trực tiếp, declaration hay tự sự, không mở mục này chỉ để làm bài “thơ hơn”. Chỉ dùng các lens dưới đây khi Tứ đã chọn thật sự phụ thuộc hình tượng/trường nghĩa, hoặc rough lyric bộc lộ chuỗi ảnh rời, thô, thay thế tùy ý hay phải giảng vì sao ẩn dụ đúng.

Hai mode hữu ích khi chẩn đoán:

- **PROGRESSIVE CHAIN:** ảnh kế tiếp làm nghĩa tiến, đổi quy mô hoặc lật nhận thức. Hợp với bài chuyển hóa/reframe.
- **AFFECTIVE CONSTELLATION:** các miền ảnh có thể xa nhau nhưng cùng một lực cảm xúc và lần lượt mở thêm mặt của trạng thái. Hợp với lament, mood, lời gọi, litany và sustain.

Với constellation, progression có thể là `đào sâu · mở rộng · đổi giác quan · đổi khoảng cách · vọng lại` thay vì `nguyên nhân → kết luận`. Không gán mỗi ảnh vào một nhãn cảm xúc cố định để chứng minh coherence; coherence nằm ở lực hút chung và phần việc khác nhau của từng ảnh. Một bài direct/declaration nói rõ thesis không fail chỉ vì nó không vận hành theo mode này.

Chỉ hỏi ba câu:

1. Các ảnh còn quay về cùng hạt nhân cảm xúc không?
2. Ảnh mới có đào sâu, mở rộng, biến nghĩa hoặc tạo dư vang, hay chỉ thay danh từ cho đẹp?
3. Lời có đang giải thích cơ chế ẩn dụ thay vì để hình ảnh, cú pháp và âm thanh làm việc không?

### IMAGE-ROLE AUDITION — tùy chọn trước Cốt

Chỉ chạy khi Tứ đã chọn cần một hình tượng hoặc hệ ảnh để sinh chuyển động, payoff hay hook. Không kích hoạt chỉ vì title là cảnh vật, vì genre thường giàu hình ảnh hoặc vì muốn lời “thơ hơn”. Với `DIRECT/UTTERANCE`, bài kể đã có một neo đủ mạnh hoặc hình tượng chỉ là tên gọi ở hook, mặc định bỏ qua.

0. **Route cách tồn tại trước khi phát triển:**
   - `LITERAL/EVENT`: brief hoặc provenance cấp vật/sự kiện thật; nó được phép tạo hành động và hệ quả vật lý.
   - `EMBLEMATIC`: một hình tượng kết tinh hoặc so sánh cho một đích trừu tượng. Nén backstage `đích cảm xúc → phép tương đồng → chuyển động chung`; mapping này không được rò thành câu định nghĩa.
   - `EMOTIONAL-FIELD/CONSTELLATION`: nhiều ảnh cùng chịu một lực cảm xúc và mỗi ảnh làm thêm một việc. Không ép cả trường về một đích ánh xạ một-một.
   - `HOOK-ONLY`: hình tượng chỉ là tên gọi, âm hình hoặc refrain; không mở rộng nếu thân bài không cần.

   Khi hai route đều có provenance và sinh Cốt khác hẳn, fan-out hai arm rồi chọn bằng brief/material necessity. Không lai route chỉ để có nhiều ảnh hơn.

1. **Định vai và vị trí:** nhận ra hình tượng đang làm biến cố, bằng chứng, bản lề, đối sánh, cô đọng hook, refrain, place-anchor hay tâm của một constellation. Đây là chức năng đã có trong Tứ, không phải menu kỹ thuật.
2. **Thử chuyển động:** hỏi hình tượng xuất hiện, đổi trạng thái/ý nghĩa hoặc trở lại ra sao qua các section. Không bắt nó trải một vòng đời vật lý; một lần đúng điểm rơi vẫn đủ.
3. **Audition theo chức năng, không theo số lượng:** mỗi ảnh được giữ phải làm quan hệ hoặc semantic tension tiến bằng đào sâu, mở rộng, biến nghĩa hay dư vang. Với constellation, kiểm lực hút chung và phần đóng góp khác nhau của từng ảnh; ảnh không có section job nghe được thì loại.
4. **Giữ đúng lane:** ở `MIXED`, premise, lời gọi, hành động quan hệ hoặc hệ quả vẫn phải nghe rõ. Ở `FIELD-DOMINANT`, con người có thể lùi khỏi vị trí chủ ngữ nhưng lực cảm xúc và referent không được biến mất.
5. **Dừng sớm:** nếu hình tượng chính đã mang đủ bài, lyric trực tiếp mạnh hơn hoặc ảnh mới chỉ thay danh từ cho đẹp, sang Cốt.

Fail `IMAGE-INVENTORY` tại Tứ/Cốt khi các ảnh đúng chủ đề nhưng không có chức năng phân biệt, có thể đổi chỗ/thay thế mà section job, tension và payoff không đổi. Khi đó bỏ ảnh thừa hoặc quay lại vai của hình tượng chính; không chữa bằng thêm cầu giải thích. Kết quả audition chỉ là một ghi chú nén về `route → vai → chuyển động → vị trí`, không được rò thành lời phân tích trong lyric.

Chỉ dùng `IMAGE-LITERALIZATION` cho route `EMBLEMATIC`: fail khi hình tượng biểu trưng tự sinh người tác động, đạo cụ, hành động hay biến cố vật lý ngoài provenance, khiến phép so sánh thành cảnh thật. Không dùng diagnostic này để cấm chuyển động tự nhiên của `LITERAL/EVENT` hoặc agency giàu cảm xúc của `EMOTIONAL-FIELD`. Các động từ như `tàn`, `rụng`, `trôi`, `phai` vẫn hợp khi giữ đúng phép tương đồng; sửa bằng cách trả hình tượng về vai so sánh/kết tinh, không xóa sạch hình ảnh.

### Ngoại hiện cảm xúc — emotional field

Đây là một mode có bằng chứng ở nhiều tình khúc thành công, không phải chuẩn cao hơn lời trực tiếp. Dùng khi Tứ cần nỗi nhớ/mất mát lan rộng nhưng rough lyric cứ quy mọi chuyển động về `người hát nhớ, nghĩ, biết, nhận ra`.

Phân biệt hai thời điểm: trước rough pass chỉ **chọn thử lane** theo brief/seed; sau rough pass mới chạy diagnostic để phân bố lại agency khi đã nghe thấy lỗi. Không lấy một prior genre hoặc image-title làm bằng chứng rằng output đang lỗi.

Ngoại hiện không phải thêm mưa, mây, đường, đêm. Nó xuất hiện khi các yếu tố đã có **agency cảm xúc**: thời gian xóa hoặc kéo dài; không gian khép/mở/lạc hướng; mùa, ánh sáng, âm thanh hay biểu tượng mang cùng chuyển động của hạt nhân. Nhân vật vẫn có thể xuất hiện nhưng không độc quyền mọi động từ.

Ngoại hiện là **chức năng**, không phải mức độ cụ thể. Một mốc giờ, vị trí, vật thể hoặc hành động chỉ đặt camera chưa phải carrier; nó phải làm quan hệ, ký ức, thế đối hoặc sức ép cảm xúc nghe được. Sau rewrite ngoại hiện, chạy REWRITE CLOSURE để tránh đổi độc thoại phân tích thành staging văn xuôi.

Chọn theo brief:

- **DIRECT/UTTERANCE:** tỏ tình, tuyên ngôn, đối thoại và hook sing-along có thể giữ người hát ở trung tâm.
- **MIXED:** prior đầu cho tình ca đại chúng có image-title; nhân vật dẫn premise và giữ quan hệ/lời gọi, field mở quy mô ở Pre/Chorus/Bridge hoặc làm refrain.
- **FIELD-DOMINANT:** lament, chiêm nghiệm, folk/kinh điển hoặc image-system đã có thi pháp đủ mạnh có thể để thế giới hình tượng gánh phần lớn cảm xúc. `Image-title` một mình chưa đủ bằng chứng.

Không đếm đại từ như quota và không personify tùy ý: ở tầng thiết kế, chỉ cần lane đã chọn có một carrier hợp seed và còn giữ đúng quan hệ/referent. Sau rough pass, nếu cụm nội tâm lặp làm scale hẹp đi hoặc cảnh vật chiếm chuỗi chủ thể khiến con người biến mất, chuyển toàn quyền chẩn và sửa sang **AGENCY-BALANCE** tại `vietnamese-line-and-sound.md`; không chạy một subject-sequence diagnostic thứ hai tại đây.

Title/seed có thể là mệnh đề cần phát triển hoặc chỉ là neo cảm xúc cần được ngân rộng. Không ép loại thứ hai thành luận đề nhân quả hay cú reframe thông minh. TRANSFORM có thể đổi nghĩa ở lần trở lại; STATE/SUSTAIN có thể quay lại cùng anchor với lực, độ rộng hoặc dư vang lớn hơn.

Vật cụ thể không tự nhiên “thô”, và trăng/hoa/mùa/sông/tuổi thơ không tự nhiên “sáo”. Giá trị nằm ở quan hệ cảm xúc, vị trí, chuyển động và âm hình trong bài. Không sao chép bộ vật liệu của ca tham chiếu; học cách các ảnh cùng lực hút và phát triển.

### Giữ quy mô liên tưởng — personal gravity

Một Tứ có thể mở ở `PERSONAL`, `MIXED`, `FIELD`, `COMMUNAL` hoặc `PHILOSOPHICAL`. Trước khi viết, chỉ cần nhận ra bài có thật sự hứa một quy mô rộng hơn chuyện riêng hay không. Nếu không, giữ `PERSONAL`; không nâng giả bằng từ lớn.

Trước khi viết câu, ghi một scale arc rất ngắn cho các section cần thiết, chẳng hạn `FIELD → MIXED → PERSONAL HOOK → FIELD`. Chỉ định rõ điểm co về lời riêng và điểm mở lại. Với một section thực hiện chuyển độ, ghi thêm **camera arc** cho cụm hai đến bốn câu, chẳng hạn `PHILOSOPHICAL → FIELD → MIXED → PERSONAL`: câu nào giữ toàn cảnh, câu nào làm bản lề và câu nào được phép thu vào quan hệ riêng. Không cần ghi khi bài DIRECT/DECLARATION chủ ý sống tốt ở quy mô cá nhân.

Không cho Tứ hoặc Cốt sinh thẳng từ bề mặt. Đi qua chuỗi ngắn `section job → scale role → immediate utterance/ý phát ngôn → phrase → từ`. `Immediate utterance` phải là điều giọng kể có thể cất lên trong khoảnh khắc, không phải bản diễn xuôi của Tứ/Cốt; nó không phải một worksheet mới và không bắt buộc xuất cho user.

Không thu hẹp `immediate utterance` thành đối thoại. Tùy lane, nó có thể là lời gọi/hỏi, một khẳng định, thế đối, chuyển động của emotional field, biến nghĩa hình tượng, nhịp cú pháp hoặc khoảng lặng. Chọn bằng section job và tai nghe; không chọn động từ giao tiếp chỉ để chứng minh rằng section có speech act.

Immediate utterance không được chép hoặc đổi nhẹ câu minh họa đã bị loại khỏi generation packet. Nếu nó vẫn giữ cùng chủ thể, động từ và trật tự nhân quả của ví dụ, quay lại section job và tìm một speech act hoặc chuyển động hình tượng khác.

Giữ scale theo **cụm nghĩa**, không theo danh từ. Nếu hai vế của một câu đều mở toàn cảnh, cả hai nên cùng ở quy mô rộng cho tới khi có bản lề chủ ý; vế sau phải đáp, tạo quan hệ, chuyển động hoặc hệ quả chứ không chỉ thêm một chân lý quen. `Khái quát` vẫn có lực hút và làm nghĩa tiến; `chung chung` có thể thay bằng nhiều câu đời–người khác mà cốt không đổi. Được co/mở ngay giữa câu khi từ nối, cú pháp, lời gọi hoặc hình tượng làm chuyển độ nghe rõ.

Tài liệu này chỉ sở hữu **scaffold sinh ý**. Cổng PASS/FAIL của scale và camera arc nằm duy nhất tại `stage-validation-loop.md`. Nếu gate báo `SCALE-COLLAPSE`, sửa scale role và immediate utterance trước; không thay máy móc `ta/người` bằng mưa, trăng, đường hay mùa.

Các arc thường dùng:

- **Cổ phong/triết tình:** nhân thế hoặc duyên–kiếp mở trường → tương phùng hiện như một phần của trường → biệt ly vọng thành quy luật/dư âm, không chỉ sự kiện riêng.
- **Quê hương/cộng đồng:** ký ức cá nhân mở cửa → tiếng nói, phong tục, mùa màng hoặc lịch sử chung mở quy mô → lời riêng trở thành lời thuộc về.
- **Tình ca mixed:** quan hệ người đặt premise → hình tượng/thời gian khuếch đại → hook trả về lời gọi → final mở dư âm vượt khỏi đôi nhân vật khi Tứ đòi hỏi.

Khi sửa scale trên một lyric đã có melody hoặc bản Suno tốt, giữ số tiếng gần đúng, điểm ngắt, slot nhấn và chất âm cuối của câu cũ trước khi thử thay contour. Scale/ý nghĩa vẫn có quyền ưu tiên, nhưng thay đổi prosody phải được nghe lại ở Scope B.

## 5. Chọn engine phát triển

Chọn engine trước Hook+Form và Cốt:

- **NARRATIVE/TRANSFORM:** bài cần sự kiện, lựa chọn hoặc reframe làm tình thế đổi.
- **DECLARATION/AMPLIFY:** bài trả lời một câu hỏi cảm xúc bằng một mệnh đề rồi tăng độ lớn, độ chắc hoặc số chiều chứng minh.
- **STATE/SUSTAIN:** trạng thái ít đổi về bản chất; groove, lament hoặc mood được repetition, nhịp, giai điệu và độ tăng lực gánh.

Không dùng độ phức tạp của plot để xếp hạng ba engine. Corpus hiện có đã cho thấy declaration và sustain có thể đúng với nhạc trẻ đại chúng; đây là prior **PROVISIONAL**, tai người vẫn quyết.

### Engine tuyên ngôn cho hit đại chúng

Dùng khi mục tiêu là tỏ tình, xác nhận, mong muốn, lời hứa hoặc một cảm xúc có thể hiểu ngay. Dựng theo bốn nhịp:

1. Một câu hỏi, nhu cầu hoặc điều khó nói.
2. Một mệnh đề trung tâm đủ rõ để làm title/hook.
3. Hai đến bốn góc chứng minh hoặc khuếch đại không đổi thesis.
4. Trở lại hook với lực lớn hơn; không chốt thêm một bài học sống.

Chạy năm cửa:

- **Immediate:** nghe Chorus một lượt hiểu nhân vật đang cảm thấy gì.
- **Compression:** ưu tiên title 2–5 từ khi tự nhiên; cụm hook đầy đủ nói được trong một hơi. Đây không phải quota cứng.
- **Unity:** toàn Chorus paraphrase được bằng một mệnh đề.
- **Sing-along:** có frame cú pháp/cadence/điệp đủ rõ để người nghe đoán được lượt sau.
- **Projection:** người nghe có thể đặt mình hoặc người họ yêu vào bài mà không cần biết tiểu sử nhân vật.

Phổ quát ở engine này đến từ cửa vào rộng và cảm xúc trực tiếp, không bắt buộc SCOPE-EXPAND. Nếu Verse liên tục giải thích tâm lý còn Chorus chứa nhiều kết luận, quay lại mệnh đề trung tâm thay vì polish câu.

## 6. Hook đi cùng Form

Chọn **working Hook** và Form trong cùng một bước; cho phép đổi sau rough demo nếu lyric–music fit yếu. Trước khi sinh bề mặt câu, chọn phrase behavior và melody-reuse policy theo Song System ở `music-sketch-and-demo.md`; form không tự cấp một lưới số tiếng.

Hook có nhiều tầng:

- **Semantic:** title/reframe/payoff cô đọng.
- **Phonetic:** âm tiết, điệp, wordplay hoặc groove; nghĩa có thể đơn giản nếu nhạc vui/dance.
- **Melodic:** motif/contour/interval dễ nhận ra; cần artifact nghe được để xác nhận.
- **Rhythmic:** cadence, syncopation hoặc phrase pattern.
- **Instrumental/production:** riff, sound, texture hoặc drop gánh nhận diện.

Chọn một hook chính và tối đa một hook phụ trong rough pass. Lyric-only không tự chứng nhận melodic/rhythmic/production hook.

Form theo chức năng:

- Pop/Vpop/ballad: Verse–Pre–Chorus–Verse–Pre–Chorus–Bridge–Final Chorus khi cốt cần ramp.
- Indie/acoustic: Verse–Chorus hoặc refrain, lift theo mood.
- Bolero/tự sự: Verse + điệp khúc.
- Chiêm nghiệm/Trịnh: vòng tròn/refrain, không ép chorus bùng.
- Rap: flow + hook; bridge tùy cốt.
- Folk/anthemic: litany, refrain, panorama hoặc form truyền thống đã chọn.

Chorus của form V-C cần ba việc: khác vai với Verse, có câu đinh, neo đúng Tứ. Title placement có thể FRONT, BACK, BOOKEND hoặc REPEAT; chọn theo chức năng.

Với declaration mainstream, Verse đặt câu hỏi/khó nói hoặc một mặt của mệnh đề; Pre tạo lực; Chorus trả lời. Dùng parallelism và repetition có chủ đích. Không bắt Bridge xoay; Bridge có thể rút nhạc, thú nhận ngắn hoặc nâng độ chắc của cùng thesis.

Ghi section job bằng **chuyển động biểu đạt nghe được**: một speech act giữa người nói–người nghe, hoặc một thay đổi của thế đối, emotional field, hình tượng, nhịp cú pháp hay khoảng trống. `Gọi–hỏi–thú nhận–nhượng bộ` chỉ là một họ khả năng, không phải mặc định. Đặc biệt ở Bridge, không giao việc bằng một luận điểm giải thích ký ức, thời gian, tình yêu hay cơ chế tâm lý. Nếu job chỉ nén được thành `X nghĩa là/gây ra/giữ lại Y`, đó là ghi chú phân tích; chuyển nó thành khoảnh khắc nhận ra hoặc chuyển động biểu đạt trước khi sinh immediate utterance.

### HOOK DISTILLATION — chưng cất payoff, chống Chorus giải thích

Sau rough Chorus, tìm:
- 1 câu hoặc 1 cặp câu chứa payoff cảm xúc rõ nhất;
- câu nào người nghe có thể nhớ và ngân lại sau một lần nghe;
- câu nào trả lời trực diện tựa bài hoặc sức căng trung tâm (central tension) tốt nhất.

Nếu hook mạnh đang nằm giữa nhiều câu giải thích câu chuyện:
- cắt bớt các câu giải thích hoàn cảnh đã được Verse chuẩn bị;
- đưa hook gần đầu hoặc cuối Chorus để tạo điểm neo;
- cho các line còn lại phục vụ hook, không cạnh tranh hay chia nhỏ sự chú ý với hook.

Chorus không cần kể lại toàn bộ story. Nó cần kết tinh (crystallize) cảm xúc trung tâm.
*Heuristic:* Nếu bỏ 30–40% số chữ của Chorus mà payoff cảm xúc rõ ràng và vang hơn, Chorus đang bị over-explaining.

### FINAL CHORUS ≠ MORE WORDS — kết luận bằng biến nghĩa, không bằng nhồi chữ

Final Chorus không mặc định phải:
- dài hơn các Chorus trước;
- chứa nhiều chữ/nhiều thông tin mới hơn;
- hát cao hơn hay kịch tính hóa giả tạo.

Final Chorus cần tạo cảm giác kết luận (resolution), chuyển nghĩa hoặc dư ba.
Có thể làm điều đó bằng cách:
- thay đúng một line chốt;
- đổi một đại từ (pronoun) hoặc đổi ngôi quan sát;
- đổi một hình ảnh bản lề;
- rút bớt chữ để nén lại sự tĩnh lặng;
- giữ nguyên hook nhưng đổi ngữ cảnh của các câu dẫn;
- hoặc thậm chí hát nhỏ lại (pull back).

Nếu Final Chorus phải thêm một câu dài lê thê để giải thích bài học hay kết cục, ưu tiên sửa emotional arc ở các section trước thay vì nhồi chữ vào đoạn kết.

### Nhận ra dòng chảy tu từ trước khi viết câu

Form cho biết section đứng ở đâu; **speech act + rhetorical carrier** có thể cho biết lời đang chuyển động bằng cách nào. Nếu tình thế, declaration, tự sự hoặc emotional field đã có flow nghe được, để carrier `N/A` thay vì bắt bài chứng minh một device. Khi carrier thật sự gánh chuyển động, chọn một trội cho bài hoặc section và tối đa một phụ:

- Gọi/hỏi: vocative, rhetorical question, đối thoại tưởng tượng.
- Đối/lật: tương phản, nghịch lý, phủ định–khẳng định, nhượng bộ.
- Khuếch đại: anaphora, parallelism, enumeration, gradation.
- Hình hóa: metaphor, personification, comparison hoặc một image-system có tiến nghĩa.
- Âm hóa: phonetic refrain, call–response, wordplay hoặc nhịp cú pháp.
- Tự sự trữ tình: ellipsis, deixis, hồi cố và refrain; sự kiện chỉ giữ phần có lực cảm xúc.

Khi flow còn mơ hồ, có thể nén progression bằng các việc như `hỏi → đối → khẳng định → lật`; không bắt mọi section phải có một nhãn động từ phát ngôn. Chuỗi `mốc giờ → địa điểm → hành động → hành động` chỉ là staging; dùng khi NARRATIVE thật sự cần, không làm mặc định vì “cụ thể”.

Concrete là nguyên liệu, không phải thước đo lyricism. Một câu trực tiếp hoặc trừu tượng vẫn đúng nếu có giọng, tension, cadence hoặc quan hệ; một câu nhiều chi tiết vẫn là văn xuôi nếu chỉ đặt camera.

### Khi concept lộ ra như bản phân tích

Semantic skeleton là ghi chú hậu trường, không phải kho câu. Chỉ khi rough lyric có một quãng nghe như định nghĩa, tư vấn hoặc phân loại tâm lý, hỏi: **người này thực sự đang muốn nói gì với ai?** Sau đó viết lại bằng giọng trực tiếp, lời gọi/hỏi, nhịp cú pháp hoặc chuyển động biểu tượng phù hợp bài.

`Pressure`, `cost`, `speech act` và `withheld core` có thể giúp chẩn đúng một đoạn lạnh, nhưng không phải bốn ô bắt buộc cho mọi section. Không chữa bản lạnh bằng cách rải vật, body-part hoặc từ “thơ”; cũng không bắt mọi câu phải kịch tính. Câu bình thường vẫn có thể chạm nếu đúng giọng, đúng nhịp và đúng điểm rơi.

## 7. Dựng Cốt

Nén cốt thành skeleton không còn đạo cụ. Đổi quán thành sân ga nhưng vẫn “có → mất → vật gợi → buông” là chưa đổi cốt.

Chọn một hành vi phát triển chính:

- **EVENT:** sự kiện đổi tình thế.
- **INTENSIFY:** cùng sự thật nhưng lực/stakes tăng.
- **ACCUMULATE:** thêm các lớp không trùng.
- **REFRAME:** nhìn lại sự thật bằng một nghĩa khác.
- **SCOPE-EXPAND:** riêng/nhỏ mở tới nghĩa rộng hơn.
- **CYCLE-DEEPEN:** trở lại anchor với nghĩa sâu hơn.
- **DECLARE/AMPLIFY:** giữ một thesis, thêm chiều đo/chứng minh và tăng lực xác nhận.
- **SUSTAIN/GROOVE:** trạng thái giữ; hook/flow/âm gánh.

Dựng scaffold:

| Section | Việc phải làm |
|---|---|
| Verse 1 | Dựng shared premise hoặc tình thế |
| Pre-Chorus | Dồn câu hỏi, áp lực hoặc chuyển độ cao |
| Chorus | Kết tinh Tứ và hook |
| Verse 2 | Đổi vai, góc hoặc stakes; không kể lại Verse 1 |
| Bridge | Mở sâu, lựa chọn, lớp stakes cao nhất hoặc đổi flow đúng behavior |
| Final | Trả payoff đã được cốt trao quyền |

### EXTERNALIZATION CONTRACT — có điều kiện trước writer-pass

Chỉ chạy khi brief khóa `EXTERNALIZED`, Tứ đã chọn `MIXED/FIELD-DOMINANT`, hoặc scale arc thật sự rộng hơn chuyện riêng. Với `DIRECT/PERSONAL` sống tốt bằng lời gọi, đối thoại hay tuyên ngôn, ghi `N/A`; không mở contract chỉ để bài có vẻ thơ hoặc nhiều cảnh hơn.

Nén backstage thành một ghi chú ngắn: `carrier → chuyển động tự nhiên → relation anchor → phân bố/return qua section`. Carrier có thể là tình thế, thời gian–không gian, âm thanh, nghi lễ, nhịp sống chung hoặc hệ hình tượng đã được Tứ trao việc; nó không đồng nghĩa một danh sách vật thể hay chuỗi chủ ngữ phi nhân.

Chạy bốn probe:

1. **Independent movement:** ngoài việc minh họa người hát đang nhớ/nghĩ, carrier có quy luật, hệ quả hoặc thay đổi nào thật sự làm Cốt tiến không?
2. **Native behavior:** chuyển động có tự nhiên trong miền nghĩa ấy không, hay phải gán ý chí, nhân hóa hoặc động tác vật lý gượng để tạo vẻ ngoại hiện?
3. **Relational anchor:** con người, quan hệ, mất mát, thuộc về hoặc sức ép nào khiến chuyển động ấy có cảm xúc thay vì thành phong cảnh/tư liệu?
4. **Two-way deletion:** bỏ các câu tự thuật, carrier còn truyền được một phần tension; bỏ carrier, quan hệ hoặc payoff phải nghèo đi rõ. Nếu chỉ một phía phụ thuộc, contract đang trang trí hoặc đang nuốt mất con người.

Không bắt carrier giữ chủ ngữ ở mọi section. Chỉ gán cho section nơi nó thực sự đổi, mở, gây hệ quả hoặc trở lại; những đoạn khác được phép đi bằng lời trực tiếp. Nếu không có carrier nào qua cả bốn probe, thử `situational` hoặc `communal` thay cho phong cảnh. Brief không khóa expression target thì được hạ về `MIXED/DIRECT`; brief đã khóa `EXTERNALIZED/FIELD-DOMINANT` thì reseed Tứ, không rải ảnh để vá.

Trước writer-pass, decompile contract vào section jobs/immediate utterance bằng lời tự nhiên về điều đang xảy ra và điều đó làm quan hệ đổi thế nào. Không đưa tên contract, nhãn carrier, bảng agency, câu mẫu hoặc kho ảnh vào generation packet.

Chạy TỨ-FIT:

1. Payoff nói lại được bằng một formulation của Tứ/hook.
2. Không có anchor hoặc tầng nghĩa cạnh tranh.
3. Sức nặng Tứ khớp mood, form và arc.
4. **Payoff có quyền:** thay đổi quan hệ cần nhiều người thì phải có đủ phản hồi/hành động. Một người tỏ tình chỉ chứng minh “đã nói”, chưa chứng minh “đã thành đôi”.

Trình scaffold cho user duyệt trước khi viết lời, trừ draft-lane mà user yêu cầu một lượt.

Nếu làm ca khúc đầy đủ, ghép scaffold lời với Song System Card tại `music-sketch-and-demo.md`: stable/unstable, groove, harmony, melodic contour, voice/range và production fingerprint. Cốt lời pass nhưng các tầng nhạc đánh nhau vẫn chưa pass song system.

### Concept coupling và hiện thân hóa

Tách hai câu hỏi trước khi writer-pass:

1. **Kiến trúc nghĩa có sinh nhạc không?** Từ cơ chế trung tâm của Tứ, audition một hoặc hai hệ quả nghe được ở cadence, stable/unstable, phrase, form, vocal field hoặc production return. Chỉ giữ hệ quả có tính tất yếu tương đối: bỏ nó đi thì cảm giác hoặc payoff của Tứ yếu rõ. Một thủ pháp chỉ “hợp mood” nhưng gắn được cho hàng trăm bài khác là genre/arrangement choice, không phải concept coupling.
2. **Người nghe có sống trong kiến trúc ấy không?** Chuyển mỗi section job thành immediate utterance rồi tìm carrier phù hợp: quan hệ, hành động, âm thanh, không gian, cảm giác hoặc lời trực tiếp. Không ép mỗi section phải có đạo cụ hay cảnh đời thường. Concrete chỉ có giá trị khi mang quan hệ hoặc semantic tension; abstraction vẫn hát được khi có giọng, nhịp và điểm rơi.

Không dùng tỷ lệ như `70% cụ thể / 30% trừu tượng` làm luật. Mật độ phụ thuộc genre, voice, section và engine. Nếu Tứ thắng nhưng lyric nghe như lời giải thích, giữ Tứ và viết lại tầng hiện thân; nếu chi tiết sống động nhưng làm mất central intent, giữ phần có cảm xúc rồi dựng lại cầu nghĩa. Hybrid hai arm chỉ hợp lệ khi chúng cùng central intent: một arm có thể cung cấp kiến trúc, arm kia cung cấp register hoặc cách hiện thân; không ghép hai payoff cạnh tranh.

## 8. Chế độ tham vọng phá cách

Đây là một route tìm kiếm rộng hơn chạy **trên cùng runtime**, không phải bộ luật sáng tác thứ hai. Chỉ bật theo yêu cầu rõ. Không hứa “siêu phẩm”; tăng trần bằng phép biến đổi có nguồn từ seed, không bằng nhồi device.

### Fan-out ở gốc, chưa viết ba bài

Giữ cùng domain contract, provenance, người hát/nghe, expression target và constraint nhạc. Từ sức căng thật trong seed, dựng ba arm card:

- **BASELINE:** hướng mạch lạc, giàu cảm xúc và dễ kiểm chứng nhất; không cố làm lạ.
- **EXPLORATION:** giữ tâm cảm xúc nhưng biến đổi một trục sâu đủ làm cơ chế phát triển, section job hoặc payoff đổi.
- **FRONTIER:** kết hợp các biến đổi tương thích để nội dung và song system phụ thuộc lẫn nhau; rủi ro phải tập trung quanh một ý lớn, không rải đều khắp bài.

Mỗi card chỉ cần nén: `skeleton nguyên nhân→chuyển động→payoff · engine · expression lane/carrier · image route nếu cần · scale arc · hook/form/phrase behavior · music implication · rủi ro chính`. Không sinh câu mẫu, kho ảnh hoặc ba lyric đầy đủ ở bước này.

Các trục sâu có thể biến đổi:

- cơ chế Tứ, quan hệ nhân quả hoặc cách payoff được trao quyền;
- `DIRECT/MIXED/FIELD-DOMINANT` và carrier `situational/environmental/communal`;
- route hình tượng `LITERAL/EVENT · EMBLEMATIC · EMOTIONAL-FIELD/CONSTELLATION · HOOK-ONLY`;
- scale/camera movement;
- speech-act progression, hook stack, form và section contrast;
- phrase behavior, melody-reuse policy, groove/harmony/production behavior khi entry hoặc brief có bằng chứng nhạc.

Đổi genre, POV, đạo cụ, trường từ, hình ảnh hoặc section tag mà skeleton và payoff vẫn nguyên chỉ là thay bề mặt. Nếu bỏ form/phrase/production lạ mà Tứ vẫn kể y hệt, phần nhạc đó chưa tham gia phép biến đổi.

### Chọn và chuyển hóa

1. Chạy `MOTIF-DIVERSITY` để loại các arm cùng gốc; với arm dựa vào hình tượng, route qua `IMAGE-ROLE`; với quy mô rộng, khóa `SCALE-CONTINUITY`.
2. Loại arm vi phạm domain/provenance, expression target, emotional credibility, tiếng Việt tự nhiên, Generate, material necessity hoặc constraint nhạc. Không cho điểm “lạ” bù hard fail.
3. Giữa các arm còn sống, ưu tiên hướng tạo được một khám phá, mất mát không thể hoàn nguyên, lựa chọn có giá, hoặc dư âm phổ quát mà vẫn có immediate utterance để hát.
4. Chỉ viết full lyric cho arm thắng. Trước writer-pass, **decompile arm card**: đây là artifact chọn hướng, không phải prompt sinh từ. Dịch transformation trace thành section job, chuyển động tiêu cự và behavior nghe được; không chuyển nguyên nhãn kỹ thuật thành vốn từ của lyric.
5. Giữ baseline làm đối chứng. Chỉ hybrid khi hai arm thật sự bổ trợ cùng một central intent; chọn một phép biến đổi trội và để phần còn lại phục vụ nó.

Packet sau decompile chỉ mang material có provenance, tiền đề cảm xúc và quan hệ người hát–người nghe, central intent, expression target, section job ở dạng immediate utterance, scale/camera turn được phép và constraint phrase/nhạc thật sự nghe được. Chỉ mang phần fingerprint có overlap evidence theo `SESSION-DECONTAMINATION`. Bỏ tên arm, engine/lane/route/scale, diagnostic, câu mẫu, hai arm bị loại và mọi từ chỉ tồn tại để mô tả cơ chế.

**Mechanism ≠ vocabulary.** Call–response có thể sống bằng hai lượt phrase; lyric không cần thuật lại hành vi gọi–đáp. Một phép biến đổi dựa vào melody, nhịp, khoảng trống hoặc sự phai mờ có thể do form và production gánh; lyric không phải gọi tên các thành phần ấy. Nếu bỏ một danh từ kỹ thuật mà song system vẫn hoạt động, đừng ép nó trở lại bằng từ đồng nghĩa.

Sau rough pass trong mode tham vọng, nếu Hook, Bridge hoặc payoff đúng chức năng nhưng một từ tải chính nghe lạnh hoặc chỉ chứng minh arm card, dùng subcase **MECHANISM-LEAKAGE** tại `vietnamese-line-and-sound.md`; ba câu dưới đây chỉ là probe trong owner ấy, không phải một audition độc lập:

1. Từ ấy có gợi đúng cảm xúc và register của người hát, hay chỉ chứng minh arm card?
2. Nó có tự nhiên ở miệng hát và chịu được lặp lại không?
3. Bỏ nó đi, có thể giữ cơ chế bằng speech act, phrase, khoảng nghỉ hoặc hình tượng đang sống tốt hơn không?

Fail thì viết lại immediate utterance/cả lượt phrase, không thay đồng nghĩa từng chữ. Đây không phải blacklist: từ bình thường, từ trực tiếp hoặc từ chỉ âm nhạc vẫn hợp lệ khi chúng là giọng thật của bài và có lực cảm xúc riêng.

Ba câu hỏi nâng trần vẫn hữu ích:

1. Điều gì mất đi thì không thể hoàn nguyên?
2. Người kể phải trả giá hoặc thừa nhận sự thật nào?
3. Bỏ tên hai nhân vật, người ngoài câu chuyện vẫn nhận ra phần đời mình ở đâu?

Phổ quát không phải zoom-out giả sang xã hội; đó là chuyện riêng chạm thời gian, hữu hạn, căn tính, thuộc về, tự do, tha thứ hoặc điều không thể lấy lại. Tứ dạng lời khuyên “hãy hiểu/chọn/chăm nhau” thường đúng nhưng nguội; mệnh đề chỉ tổng kết sau khi Cốt khiến nó phải được nói.

### Phá cách phải sống trong nhạc

Form, phrase hoặc production phá cách chỉ ở lại khi nó biểu hiện đúng cơ chế: đứt đoạn vì ký ức đứt, vòng lặp vì trạng thái không thoát, section co/mở vì scale đổi, cadence bị trì hoãn vì payoff chưa đến. Không dùng tag, nhịp lạ hay câu dài bất thường để che Tứ yếu.

Sau rough pass, chạy semantic gate và Scope A như mọi bài khác. Có audio thì A/B baseline với arm tham vọng trên cùng brief; nghe hook recall, stress/phrase, section contrast, payoff và độ chạm. Chưa có audio chỉ được chọn **lyric candidate**, không tuyên bố music-fit hoặc ưu thế sản xuất.
