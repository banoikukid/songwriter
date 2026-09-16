# Stage Validation Loop — đối chiếu xuyên tầng

## Mục tiêu

Định vị tầng sớm nhất sinh lỗi mà không biến sáng tác thành một chuỗi biểu mẫu. Grade artifact/outcome trước; diagnostic chỉ mở sau khi có triệu chứng.

## Artifact và cổng PASS

| Tầng | Artifact tối thiểu | PASS khi | Fail quay về |
|---|---|---|---|
| GOAL/BRIEF | goal · người hát/nghe · relation/topic · mood/register/genre · constraint thật · expression target nếu user đã nêu | lời hứa cảm xúc, target biểu đạt và điều không được đánh đổi đủ rõ | Goal/brief |
| ENTRY/SEED | entry mode · user material · provenance · music constraint nếu có | đúng cửa vào; không bịa material; artifact có sẵn đã thành constraint | Entry hoặc brief |
| INTENT/TỨ/HOOK | central intent · engine · Tứ · working hook; với đề mỏng hoặc Tứ chưa khóa: các motif skeleton đã khử trùng và arm sống đã được phát triển đủ để thấy movement/payoff; ambition arm cards chỉ khi mode được bật | có lực cảm xúc, đúng brief, sinh được section và fit music frame; Tứ thắng theo ngưỡng tuyệt đối trước khi thắng tương đối; nếu liên tưởng gánh bài, nguồn kết dính có căn cứ và không phải chuỗi từ/công năng; freshness không giết độ ấm | Intent/Tứ |
| SONG SYSTEM/CỐT | form · section jobs · behavior/payoff · music frame; image-role note chỉ khi Tứ phụ thuộc hình tượng; transformation trace chỉ khi ambition arm thay song system | section có việc khác nhau, payoff được chuẩn bị và lời–nhạc không kéo ngược nhau; hình tượng được giữ có việc nghe được thay vì thành kho ảnh; phá cách hình thức có việc nghĩa nghe được | Song system hoặc Tứ |
| ROUGH LYRIC | lyric sheet · voice/POV · phrase map sơ bộ · carrier ngoại hiện nếu brief yêu cầu | PASS **ROUGH-LYRIC SEMANTIC GATE** bên dưới | Đúng section/line; quay Cốt/Tứ nếu lỗi lan toàn bài |
| ROUGH DEMO | melody contour/range · stress/phrase · harmony/groove · section contrast | artifact nghe được xác nhận stress, breath/range, hook recall, contrast và payoff lyric–music | Music frame, prosody hoặc lyric section |
| REWRITE | baseline diff · diagnostic đã gọi · semantic recheck · re-demo status | triệu chứng gốc hết; toàn section qua **REWRITE CLOSURE**; không có hard fail mới hoặc symptom substitution; phần bị đổi đã được nghe lại | Pass gây thua |
| FINAL/EXPORT | lyric sheet · demo/render nếu claim Scope B · human verdict | ROUGH LYRIC PASS trước Scope A; Scope A trước prototype; Scope B trước prosody/music-fit; trạng thái gắn đúng | Tầng gốc của failure |

Fingerprint mặc định phải ngắn:

`entry=<mode>; intent=<tứ+engine>; cot=<form+behavior+payoff>; hook=<type>; voice=<register>; sound=<Scope>; music=<artifact/status>; base=<version+verdict>`

Chỉ thêm `diagnostic=<symptom+earliest-stage+patch>` khi có failure. Không ghi toàn bộ lyric, worksheet pressure/cost hay danh sách ảnh vào fingerprint.

### MOTIF-DIVERSITY — cổng tại INTENT/TỨ

Với input mỏng, hình ảnh hoặc khi ca gần đây lặp gốc phát triển, PASS chỉ khi:

- các phương án đã được rút về skeleton `nguyên nhân → chuyển động → payoff`;
- còn ít nhất hai cơ chế cảm xúc thực sự khác nhau để đối chiếu;
- phương án thắng bám material/provenance, không lén suy một câu chuyện quen từ mood, dáng người, phong cảnh hoặc title;
- arm còn sống đã được mở vừa đủ để chứng minh nhiều vai đoạn hoặc một behavior sustain/declaration có biến thiên; không chọn từ các pitch một tầng;
- phương án thắng tự qua emotional credibility, Generate, material necessity và music/brief fit trước khi so freshness; không lấy “ít yếu nhất” làm Tứ;
- khi liên tưởng gánh bài, các nhánh fan-out là quan hệ/sức căng khác nhau và hội tụ ở một nguồn kết dính có căn cứ. Chuỗi `khái niệm → động tác vật lý → đồ vật` hoặc liên tưởng từ điển/công năng không được tính là chiều sâu;
- mặc định thử một trục chính. Trục phụ chỉ ở lại khi có chức năng riêng và deletion-test cho thấy bỏ nó làm movement/payoff nghèo đi;
- nhãn `đại chúng/tươi/tham vọng`, đổi POV, genre, đạo cụ hay trường từ không được tính là motif diversity.
- với output nhiều Tứ, không để từ ba hướng trở lên phụ thuộc trung tâm vào cùng cú phủ định/đảo nghĩa (`tưởng A → hóa ra B`, `không phải A → mà là B`, `từng A → giờ B` hoặc tương đương). Tương phản phụ hay sự xuất hiện của từ `nhưng/không/mà` không đủ để kết luận; phải rút skeleton và xem payoff có mất lực nếu bỏ cú lật hay không.

Nếu mọi hướng cùng skeleton, trả `FAIL: INTENT/TỨ · MOTIF-COLLAPSE`; nếu một bộ nhiều Tứ có từ ba hướng trở lên cùng sống nhờ phép lật nghĩa trung tâm, trả subcase `FAIL: INTENT/TỨ · MOTIF-COLLAPSE/REFRAME-COLLAPSE`, gộp họ đó và reseed các arm dư. Nếu người thắng chỉ là một nhận xét kéo dài hoặc chỉ tốt tương đối, trả `FAIL: INTENT/TỨ · Ý-CHUNG`. Nếu liên tưởng thắng nhờ cầu từ điển/công năng nhưng không truy được về sức căng hay material, trả `FAIL: INTENT/TỨ · ASSOCIATION-MECHANICAL`. Nếu arm quen tự thắng dù seed không làm nó cần thiết, trả `FAIL: INTENT/TỨ · BASELINE-AUTOPILOT`. Negative controls: khi user đã cho rõ một mô-típ quen hoặc yêu cầu cú nhận ra, mô-típ/reframe ấy vẫn được chọn nếu qua hard criteria; chỉ các arm dư lặp cùng phép lật mới phải reseed. Khi user khóa toàn bộ set vào các biến thể reframe, chấm diversity trong scope ấy thay vì áp ngưỡng cấp bộ. Khi declaration, tự sự hoặc hook trực tiếp đã đủ Generate **và brief không khóa `EXTERNALIZED/FIELD-DOMINANT`**, không bắt bài sinh hình tượng, trục phụ hay semantic turn chỉ để qua gate. Nếu direct arm thắng bằng độ trôi chảy nhưng làm mất expression target đã giữ trong phiên, trả `FAIL: INTENT/TỨ · EXPRESSION-TARGET-DROP`.

### LYRIC-YIELD — cổng audition trước khi khóa Cốt

Artifact là các vi đoạn viết mù tên cơ chế từ những arm đã qua MOTIF-DIVERSITY, không phải lời giải thích về tiềm năng. PASS khi arm thắng tạo được nhiều ý phát ngôn/biểu hiện có chức năng khác nhau, giữ register và emotional credibility, đồng thời còn movement hoặc payoff cho section kế. Một đoạn đẹp đơn lẻ chưa đủ.

Trả `FAIL: INTENT/TỨ · LOW-LYRIC-YIELD` khi vi đoạn chủ yếu là pitch được xuống dòng, ngụ ngôn, storyboard `ai làm gì ở đâu`, danh sách ảnh thay thế tùy ý, hoặc cùng một mệnh đề đổi chủ thể/danh từ. Trả `FAIL: INTENT/TỨ · MATERIAL-SURFACE-LOCK` khi chức năng cảm xúc có thể sống bằng carrier tốt hơn nhưng bản thử vẫn bám vật thô chỉ vì seed nhắc tới nó; material user khóa được giữ trong scope nhưng có thể chuyển `REGISTER-SHIFT/BACKSTAGE-ONLY`.

Sau mỗi section, đối chiếu harvest state với Cốt. Chỉ `ADJUST CỐT` khi central intent còn sinh lực; `PIVOT/RESEED` khi nhiều câu phải giải thích hoặc lặp mới giữ được hướng. Đây là gate điều phối, không được chấm vần, số âm tiết hay vẻ thơ ở cấp từ.

### AMBITION-TRANSFORMATION — chỉ khi mode được bật

Gate này chỉ sở hữu **tính thật của phép biến đổi và quan hệ giữa arm với song system**; `MOTIF-DIVERSITY`, `IMAGE-ROLE`, `SCALE-CONTINUITY`, semantic gate và Scope A/B vẫn sở hữu miền của chúng.

PASS khi:

- có baseline mạch lạc và các arm mạo hiểm khác ở trục sâu, không chỉ khác genre, POV, đạo cụ, trường từ, device hay section tag;
- mọi arm giữ domain/provenance, expression target và constraint thật của brief;
- mỗi biến đổi truy được về sức căng trong seed và làm thay đổi cơ chế phát triển, section job, payoff hoặc behavior nghe được;
- nếu form, phrase, hook stack hay music frame bị bẻ, sự thay đổi đó cần cho central intent và có artifact phù hợp để kiểm;
- arm thắng đã qua các hard gate hiện hành; độ mới chỉ phân thắng giữa những hướng còn giàu cảm xúc và hát được.

Nếu khác biệt biến mất khi bỏ bề mặt lạ, trả `FAIL: INTENT/TỨ · AMBITION-SURFACE` và reseed arm. Nếu form/phrase/production lạ có thể tháo ra mà Tứ/Cốt không mất gì, trả `FAIL: SONG SYSTEM/CỐT · AMBITION-DECOUPLED`; trả về behavior phù hợp hoặc làm rõ transformation trace. Gate này kết thúc ở arm card; sau khi chọn phải decompile trace thành section behavior trước writer-pass. Không dùng gate này để ép mọi bài tham vọng phải rộng quy mô, field-dominant hay phá form.

### IMAGE-ROLE FIT — chỉ khi Tứ phụ thuộc hình tượng

Chạy sau khi chọn Tứ và trước khi khóa Cốt; các bài còn lại ghi `N/A`.

- Cách tồn tại đã được route đúng: `LITERAL/EVENT · EMBLEMATIC · EMOTIONAL-FIELD/CONSTELLATION · HOOK-ONLY`. Chỉ nhánh `EMBLEMATIC` cần mapping một-một `đích → tương đồng → chuyển động chung`; không ép emotional field về phép định nghĩa ấy.
- Hình tượng chính có một vai nghe được trong cơ chế, section turn, payoff hoặc hook; không chỉ làm nhãn mood.
- Chuyển động hay lần trở lại của nó làm nghĩa tiến. Một neo duy nhất vẫn PASS nếu đã đủ.
- Không có quota ảnh. Mỗi ảnh được giữ có section job và semantic contribution riêng; với constellation, chúng cùng lực hút cảm xúc nhưng không làm cùng một việc.
- Với lane `MIXED`, quan hệ người, lời gọi, hành động hoặc hệ quả vẫn nghe rõ. Với `FIELD-DOMINANT`, referent và lực cảm xúc vẫn nghe được dù con người không giữ phần lớn chủ ngữ. Với `DIRECT/UTTERANCE`, không ép sinh hệ ảnh.

Nếu ở Tứ/Cốt, ảnh phụ chỉ tạo một danh sách đúng chủ đề hoặc thay thế tùy ý mà Cốt/payoff không đổi, trả `FAIL: SONG SYSTEM/CỐT · IMAGE-INVENTORY`; bỏ ảnh thừa hoặc giữ một neo. Nếu chức năng đã khác nhau nhưng rough lyric làm quan hệ hoặc trình tự giữa ảnh nghe rời/thô, để `ASSOCIATION-CARRIER` sở hữu lần sửa câu. Nếu phân bố chủ thể/vị ngữ làm người và quan hệ biến mất dù hệ ảnh đúng, để `SCENERY-LOCK` sở hữu lần sửa agency.

Chỉ ở route `EMBLEMATIC`, nếu hình tượng chưa có provenance vật thật lại tự sinh người tác động, đạo cụ hoặc biến cố vật lý, trả `FAIL: INTENT/TỨ→SONG SYSTEM/CỐT · IMAGE-LITERALIZATION`. Động từ vật lý không tự fail khi nó còn phục vụ phép tương đồng; fail nằm ở việc nó chiếm quyền sinh Cốt. Không dùng diagnostic này cho hành động có provenance của `LITERAL/EVENT` hoặc chuyển động tự nhiên của `EMOTIONAL-FIELD`.

## ROUGH-LYRIC SEMANTIC GATE — chủ sở hữu chuẩn

Chạy sau rough pass và trước Scope A. Gate này chỉ xác nhận lyric đã đủ đúng về ý nghĩa để đáng kiểm tra âm–vần; nó không chứng minh prosody, melody-fit, hook recall hay chất lượng cảm xúc cuối cùng.

Không hồi tố mọi diagnostic vào writer-pass. Với mỗi section, chỉ gọi owner có triệu chứng nghe/đọc được và dẫn được tới dòng/cụm cụ thể; không có evidence thì ghi `N/A`. Nếu nhiều diagnostic cùng được kích hoạt chỉ vì chúng tồn tại trong reference, đó là activation burden của quy trình, không phải bằng chứng lyric fail.

**PASS** khi đồng thời:

1. Lyric giữ đúng brief, central intent, Tứ, voice/POV, expression target và việc của từng section.
2. Tiếng Việt rõ nghĩa, tự nhiên; không đổi nghĩa chỉ để lấy vần hoặc vẻ “thơ”.
3. Không có quãng dài thành lời phân tích, tư vấn, tóm tắt tâm lý hay biên bản dựng cảnh; không có cụm báo cáo đối xứng literal hóa câu minh họa brief rồi chen carrier trang trí. Lyric không lặp tên cơ chế, carrier hoặc thành phần song system chỉ để chứng minh kế hoạch. Ở Hook/Chorus/Bridge/Outro, một câu tải cao diễn xuôi ghi chú Tứ/Cốt hoặc literal hóa transformation trace cũng chạy `ANALYSIS-LEAKAGE`, dù chỉ một dòng.
4. Với `EXTERNALIZED` hoặc `MIXED`, carrier đã chọn thật sự làm nghĩa tiến; cảnh vật không chỉ thay đại từ làm chủ ngữ. Đối chiếu **CARRIER-RENDER**: ở `TRANSFIGURED`, một dòng đơn vẫn fail `ASSOCIATION-CARRIER/RAW-CARRIER REPORT` nếu chỉ trình diễn hành vi vật lý hậu trường, kể cả câu kề đã tạo nhân quả; ở `LITERAL`, giữ chi tiết có provenance, hệ quả EVENT, realist job hoặc groove/onomatopoeia riêng. `BEHAVIORAL-DEMO LEAKAGE/PARALLEL-TRANSLATION` vẫn fail khi câu kề phải dịch hộ toàn bộ quan hệ/cảm xúc. Áp đúng owner: chức năng ảnh ở Tứ/Cốt là `IMAGE-INVENTORY`, quan hệ ảnh trong rough lyric là `ASSOCIATION-CARRIER`, phân bố agency là `SCENERY-LOCK`, còn vật lý hóa ngoài provenance chỉ là `IMAGE-LITERALIZATION` ở route `EMBLEMATIC`.
5. Với Tứ quy mô rộng, scale/camera arc qua **SCALE-CONTINUITY** bên dưới. Với bài `DIRECT/PERSONAL` có chủ ý, mục này là `N/A`; không ép mở ra nhân thế, cảnh quan hay cộng đồng.
6. Phrase behavior và melody-reuse policy đủ nhất quán để chuyển sang Scope A; chưa cần bằng số tiếng.

Kết quả chỉ là `PASS` hoặc `FAIL: <earliest-stage> · <symptom>`. Nếu nhiều dòng cùng sai một miền nghĩa, expression target hoặc quy mô, quay `INTENT/TỨ` hay `SONG SYSTEM/CỐT`; không sửa đồng nghĩa từng câu. Nếu ý đã đúng nhưng một cụm còn cấn tự nhiên, quay đúng section/line.

## SCALE-CONTINUITY — chỉ khi Tứ hứa quy mô rộng

Đối chiếu lyric với scale arc của bài và camera arc của cụm hai đến bốn câu:

- **Trong câu/cặp câu:** các vế cùng quy mô phải đáp, đào sâu, tạo quan hệ hoặc hệ quả; không ghép hai chân lý rộng thay thế tùy ý. Nếu co/mở, bản lề phải nghe được qua cú pháp, từ nối, hình tượng, lời gọi hoặc section turn.
- **Trong cụm:** câu giữ rộng phải giữ trọn trường nghĩa; câu bản lề chuyển tiêu cự; câu gần chỉ xuất hiện ở vị trí đã chủ ý.
- **Trong section/toàn bài:** Verse, Chorus và Bridge thực hiện đúng vai `giữ · co · mở`; phần cá nhân là một tiêu điểm trong trường rộng, không âm thầm chiếm lại toàn bộ động từ.

`SCALE-COLLAPSE` thuộc `INTENT/TỨ`, `SONG SYSTEM/CỐT` hoặc section job. Sửa scale role và immediate utterance trước khi sửa chữ. Chỉ sau khi scale đã PASS mới mở `AGENCY-BALANCE` ở `vietnamese-line-and-sound.md` nếu cụm vẫn bị khóa trong chủ thể người hoặc cảnh vật.

Negative control: confession, dialogue hay declaration chủ ý ở `PERSONAL` không cần camera arc. Một lyric gần và thật không fail vì thiếu từ lớn hoặc thiếu phong cảnh.

## Baseline non-regression

1. Giữ bản coherent đầu tiên sau rough demo làm composition baseline. Chưa có audio thì chỉ là lyric baseline.
2. So diff trên: đúng brief/intent · nghĩa/tự nhiên · hook · phrase/music · cảm xúc tai người.
3. Hard fail mới thắng điểm cộng mềm; hoàn nguyên hoặc thử option khác.
4. Với rule provisional, A/B cùng brief, material, model/harness và budget.
5. Grade outcome trước, đọc trace sau.

### REWRITE CLOSURE — bắt buộc sau mọi diagnostic patch

Chạy theo thứ tự trên **toàn section đã đổi**, không chỉ câu vừa sửa:

1. Chạy lại ROUGH-LYRIC SEMANTIC GATE và diagnostic gốc.
2. Kiểm symptom substitution có xác suất cao: `phân tích → staging`, `protagonist-lock → scenery-lock`, `trừu tượng → vật thể thô`, `ép vần → sai nghĩa`, `câu đều → văn xuôi dài`.
3. So với baseline về nghĩa, độ ấm, register, phrase và section job. Bản mới chỉ PASS khi thắng hoặc giữ các trục cũ mà không sinh hard fail.
4. Sau semantic non-regression mới chạy Scope A; có audio thì re-demo Scope B phần bị đổi.

Một carrier ngoại hiện mới chỉ được tính là cải thiện khi hành động, âm thanh, tình thế hoặc trường hình tượng thật sự mang quan hệ/semantic tension. Chi tiết chỉ trả lời `ai đang ở đâu/làm gì` là staging, dù cụ thể và đúng ngữ pháp.

## Validation theo loại claim

| Claim | Artifact bắt buộc | Grader chính |
|---|---|---|
| Tứ/cốt rõ và sinh được bài | Tứ + section scaffold | rubric chức năng + phản-ví-dụ |
| Lời tự nhiên/rõ nghĩa | lyric sheet | hard gate + blind human pairwise |
| Hát xuôi/prosody tốt | melody-demo có lyric | nghe phrase/stress/breath; Scope B |
| Hook dễ nhớ | demo + recall sau khoảng nghỉ | unaided human recall |
| Phối/genre-fit | production sketch/render | blind listening theo target |
| Tốt hơn baseline | raw A/B cùng brief | multi-axis pairwise + hard non-regression |

## Failure trace

`symptom → artifact → earliest-stage → route/grader → evidence → patch → retest → regression → verdict`

- Rule có mà route không gọi: sửa routing, không chồng rule đồng nghĩa.
- Output hợp lệ nhưng grader fail: sửa grader.
- Lỗi chỉ ở render: không quy hết cho lyric/Tứ.
- Nhiều diagnostic cùng bật cho mọi draft: coi đó là lỗi activation burden và hạ cấp/xóa rule trước khi thêm gate.

## Log và promotion

`case-log.md` ghi artifact thật và fingerprint ngắn; registry eval riêng ghi `case-id · split · skill-version · model/harness · trial · graders · result · reviewer · contamination-status`.

Với mẫu nhỏ, báo số đếm và uncertainty. Promotion theo `audit-and-evaluation.md`: capability → candidate → sealed holdout + regression → validated theo scope.
