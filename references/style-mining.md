# Style prompt và hướng phối thử

Đọc khi user cần Style prompt, mô tả phối khí hoặc một prototype Suno. Đây là tầng production direction, không được dùng để quyết định nghĩa title, Tứ, lyric tradition hay expression lane.

## Thứ tự bằng chứng

1. Audio/track/reference mà user đã cấp và cho phép phân tích.
2. Mô tả trực tiếp của user về genre, groove, thời kỳ, giọng và nhạc cụ.
3. Song System Card hiện tại.
4. Giả định production trung tính, phải ghi rõ khi thiếu dữ kiện.

Mood không tự thắng genre và genre không tự cấp cốt, vật liệu hay vần. Khi các trục xung đột, giữ constraint được user/audio xác nhận; hỏi lại nếu lựa chọn sẽ làm đổi hẳn sản phẩm.

## Khai thác phong cách từ bài mẫu (Pattern Extraction, Not Paraphrase — nwp)

Khi user cung cấp nghệ sĩ, ca khúc tham chiếu hoặc bài mẫu:
- **Được phép trích xuất (Extract Patterns):** Section pattern, line density, xu hướng số âm tiết/nhịp thở, hành vi gieo vần, chiến lược ẩn dụ, emotional arc, cách đặt hook, và mức độ khẩu ngữ/trực diện (conversational register).
- **Tuyệt đối KHÔNG trích xuất (Never Copy):** Không sao chép câu hát đặc trưng, cụm từ riêng biệt, cốt truyện cụ thể, hình ảnh độc quyền hoặc từ ngữ ca từ của bài mẫu.
- **Quy trình chuẩn hóa:**
  $$\text{REFERENCE} \rightarrow \text{PATTERN EXTRACTION} \rightarrow \text{STYLE DNA} \rightarrow \text{ORIGINAL CONCEPT} \rightarrow \text{ORIGINAL LYRIC}$$
  *(Tuyệt đối không chạy quy trình: REFERENCE → PARAPHRASE).*

## STYLE-SPEC tối thiểu

Nén thành các trường cần thiết, không bắt điền đủ khi bằng chứng thiếu:

- genre/subgenre và era nếu biết;
- tempo/groove feel;
- vocal type, register và delivery;
- lead instrument, supporting texture và rhythm section;
- energy/dynamics arc giữa các section;
- production character: dry/intimate, live/organic, polished, lo-fi, cinematic hoặc spacious;
- điều cần tránh khi user đã nêu.

Mỗi nhạc cụ phải có vai nghe được; không liệt kê kho nhạc cụ. Không suy key, BPM, meter, range hoặc kỹ thuật giọng cụ thể khi chưa có audio/brief đủ rõ.

## Xuất Style

- Viết mô tả descriptive-only; không dùng tên nghệ sĩ hoặc tên bài làm style target.
- Ưu tiên một câu hoặc cụm câu rõ về genre, groove, vocal, instrumentation, dynamics và production.
- Có thể dùng prose hoặc cụm từ ngắn; không tuyên bố một cú pháp luôn thắng mọi model/version.
- Kết bằng `All lyrics in Vietnamese.` khi handoff tiếng Việt.
- Chỉ thêm tối đa một cue riêng ở đầu section nếu cue giúp A/B arrangement; không chèn cue giữa câu mặc định.

## Guard Suno

- Style, lyrics và section tags là tín hiệu xác suất, không khóa melody, key, BPM, meter hay arrangement chính xác.
- Không dùng mật độ âm tiết hoặc số chữ như núm ép tempo/melody. Phrase density chỉ là một constraint phrasing cần nghe lại.
- Không hứa CAPS, dấu chấm, dấu gạch, slash hoặc tag mở rộng sẽ tạo cao độ/trường độ chính xác.
- Cần melody riêng: dùng hum/audio upload, composer hoặc DAW; text-only giữ `music-fit UNKNOWN`.
- Sau render, chẩn lyric, performance, arrangement và engine variance riêng; sửa đúng tầng rồi re-render.

Thông tin tính năng có thể đổi theo thời gian. Khi user hỏi tên model, giới hạn, slider, quyền sử dụng hoặc thao tác UI hiện hành, kiểm tài liệu Suno chính thức trước khi trả lời.

## Preset: NOSTALGIC-ROMANTIC-RNB-SYNTHPOP

Dùng khi user gọi `nostalgic romantic R&B synth-pop`, `R&B synth-pop hoài niệm` hoặc yêu cầu dùng lại mẫu đã lưu. Đây là production preset descriptive-only; không mang title, lyric, hook, melody hoặc tên nghệ sĩ/bài tham chiếu vào generation.

### Biến mood

- `WARM-HOPEFUL`: tình yêu đang sống, dịu dàng, lãng mạn về đêm.
- `BITTERSWEET`: mong manh, hồi tưởng, buồn thanh lịch nhưng không bi lụy.

Mặc định chọn theo lyric/brief; không để preset đổi central intent. Nếu bài sáng như `WARM-HOPEFUL`, bỏ các descriptor `tragic`, `dark heartbreak` và `despair`.

### Style core

```text
Vietnamese nostalgic romantic R&B synth-pop, [WARM-HOPEFUL: warm and hopeful | BITTERSWEET: bittersweet and elegant], tender emotional vocal, slow mid-tempo half-time groove, smooth melodic phrasing, intimate breathy verses, warm electric piano, deep rounded sub bass, soft electronic drums, gentle snare and finger snaps, shimmering analog synth pads, delicate bell-like synth plucks, ambient clean electric guitar fills, subtle retro 1980s atmosphere, spacious vocal reverb, tasteful delay at phrase endings, rising pre-chorus tension, expansive melodic chorus with sustained emotional notes, memorable vocal hook, layered backing harmonies, polished nocturnal production. All lyrics in Vietnamese.
```

Chỉ thay token mood và vocal gender/register theo brief. Không tự khóa BPM/key/range khi chưa có audio.

### Exclude Styles

```text
acoustic piano ballad, bolero, folk, bright pop funk, fast city pop, heavy rock, orchestral power ballad, trap hi-hats, rap, EDM festival drop, aggressive belting, excessive vocal runs
```

Với biến `WARM-HOPEFUL`, thêm `tragic mood`; với `BITTERSWEET`, không loại nỗi buồn nhẹ.

### Section-cue palette

Chọn tối đa một cue phù hợp ở đầu mỗi section; không bắt dùng đủ:

```text
[Intro]
[shimmering synth pad, warm electric piano motif, distant vocal texture]

[Verse]
[intimate breathy vocal, sparse R&B beat, deep rounded sub bass]

[Pre-Chorus]
[rising synth chords, gentle finger snaps, vocal melody climbing]

[Chorus]
[wide romantic synths, full half-time groove, sustained emotional vocal]

[Post-Chorus]
[echoed vocal hook, bell-like synth response, ambient guitar]

[Bridge]
[drums drop out, exposed close vocal, electric piano and warm dark pad]

[Final Chorus]
[climactic wide synths, deep drums, higher sustained vocal, stacked harmonies]

[Outro]
[electric piano reprise, delayed vocal fragments, synth pad slowly fading]
```

Sau render, nghe lại Scope B. Preset này tăng xác suất ra texture/groove tương tự, không đảm bảo melody hoặc arrangement cố định.

---

## Style Research → Style DNA (Chiết xuất đặc trưng âm nhạc quan sát được)

> **Cảnh báo kiến trúc & bản quyền:**  
> `Style DNA` **tuyệt đối KHÔNG phải là công cụ mô phỏng cá nhân (Artist Imitation)** hay trích xuất dấu vân tay nghệ sĩ (*artist fingerprint extraction*).  
> Nó định nghĩa là: **tập hợp các đặc trưng âm nhạc thuần túy có thể quan sát và đo lường được (Observable Musical Characteristics)**, độc lập hoàn toàn với danh tính của bất kỳ nghệ sĩ cụ thể nào.  
> Cấm tuyệt đối các chỉ dẫn dạng: *"hãy hát như ca sĩ X"*, *"viết như nhạc sĩ Y"*, *"phỏng theo bài Z"*.

Khi người dùng yêu cầu nghiên cứu hoặc lấy cảm hứng từ một trường phái/tác phẩm, agent chỉ chiết xuất các thuộc tính âm nhạc khách quan:

```text
Nguồn cảm hứng / Thể loại
             ↓
Trừu tượng hóa thành đặc trưng âm nhạc khách quan
             ↓
STYLE DNA (Observable Characteristics)
             ↓
Tác phẩm nguyên bản mới hoàn toàn
```

### 8 Chiều Đặc Trưng Âm Nhạc Quan Sát Được (Observable Characteristics):
1. **Phrase Density:** Mật độ câu từ (dày đặc tự sự hội thoại hay thưa thoáng, giàu khoảng lặng ngắt nghỉ).
2. **Melodic Contour Tendency:** Xu hướng đường nét giai điệu (bước nhảy quãng rộng phóng khoáng hay di chuyển liền bậc êm đềm).
3. **Instrumentation & Texture:** Nhạc cụ thực tế cấu thành âm thanh (acoustic mộc, synthesizer analog cổ điển, hay bộ gõ tối giản).
4. **Rhythmic Feel & Groove:** Tính chất nhịp điệu (đảo phách/syncopation, laid-back trễ nhịp, swing, hay thẳng phách 4/4).
5. **Vocal Register & Stance:** Vùng giọng và thế phát ngôn (thủ thỉ kề cận micro, tự sự trung tính, hay phóng khoáng vang xa).
6. **Arrangement Density & Space:** Độ dày bản phối và khoảng trống âm thanh (minimalism chắt chiu hay wall of sound nhiều tầng bè).
7. **Emotional Pacing:** Nhịp biến chuyển cảm xúc (cháy âm ỉ tích lũy rồi bùng nổ hay duy trì một không gian chiêm nghiệm tĩnh lặng).
8. **Imagery Density:** Mật độ hình ảnh trong ca từ (ngôn ngữ đời thường trực diện hay biểu tượng trừu tượng mang tính điện ảnh).

### Rào cản phủ định nghiêm ngặt (Negative Guardrails):
- **CẤM sao chép ca từ & motif signature:** Tuyệt đối không mượn cụm từ đặc trưng, câu hook, cách ví von nhận diện thương hiệu hay chi tiết cá nhân từ tác phẩm tham chiếu.
- **CẤM đưa tên nghệ sĩ/tác phẩm vào Prompt:** Không đưa tên nghệ sĩ, ban nhạc hay bài hát vào Style prompt của Suno hoặc brief sáng tác.
- **Mục tiêu duy nhất:** Tạo ra một **bản đặc tả âm nhạc khách quan (Objective Musical Specification)** để sáng tác một ca khúc hoàn toàn mới, mang giá trị tự thân.
