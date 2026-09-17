# Khung nhạc, demo thô và vòng rewrite

## Mục lục

1. Khi nào đọc
2. Song System Card
3. Tạo demo thô
4. Audit prosody tích hợp
5. Rewrite và feedback
6. Gate production

## 1. Khi nào đọc

Đọc khi user yêu cầu sáng tác **ca khúc đầy đủ**, có/đòi melody, chord, groove, track, demo, Suno render hoặc đánh giá bản nghe. Nếu chỉ yêu cầu lời, giữ card âm nhạc ở mức giả định và gắn nhãn `LYRIC DRAFT — music-fit chưa xác nhận`.

## 2. Song System Card

Nén trước khi viết bản đầu:

- **Goal:** personal, artist release, commercial pop, sync, live, cộng đồng hay demo thử.
- **Central intent:** một câu; mỗi section ổn định/bất ổn ở mức nào.
- **Entry seed:** title/lyric, melody, groove/track, chord/harmony, brief/story hoặc co-write.
- **Hook stack:** lyric/title, melodic, rhythmic, instrumental hoặc production; chọn một hook chính và tối đa một hook phụ.
- **Form + section jobs:** mỗi section làm gì ở lời và năng lượng.
- **Phrase behavior + melody-reuse policy:** section đi bằng cân/điệp, ngắn–dài, nén→mở hay call–response; section tương ứng chọn `REUSE`, `VARIATION` hoặc `NEW BEHAVIOR`.
- **Tempo/meter/groove feel:** mô tả cảm giác; không hứa con số nếu engine không nghe/đo được.
- **Harmony map:** home/tension/release hoặc chord loop khi user cần; harmony phải cùng hướng với intent.
- **Melody map:** contour, register, phrase density, điểm lặp và chỗ lift; chưa có audio thì chỉ là direction.
- **Voice/range:** người hát, tessitura tương đối, diction và điểm lấy hơi; khi performance contrast là một phần của hook, ghi thêm vocal-direction map theo section job thay vì gán register theo tên section.
- **Production fingerprint:** nhạc cụ/texture/arrangement nào gánh hook hoặc contrast.

Không cần điền mọi ô bằng thuật ngữ. Card phải đủ để các quyết định không đánh nhau.

`REUSE` ưu tiên cùng số phrase, biên phrase, hơi và slot nhấn; không đồng nghĩa các dòng phải bằng số tiếng. `VARIATION` giữ một hình nhận ra được nhưng có một chỗ thay đổi chủ ý. `NEW BEHAVIOR` chỉ dùng khi vai section hoặc groove đổi thật. Với lyrics-first, đây vẫn là hướng thiết kế; audio mới xác nhận melody đã được tái dùng.

## 3. Tạo demo thô

Dùng bản rẻ nhất đủ nghe được **lời + melody + harmony/tonal center**:

- Voice memo hát mộc.
- Hum/nonsense syllable trên chord hoặc track.
- Guitar-vocal/piano-vocal.
- MIDI hoặc loop tối giản.
- Suno/AI render đầu như **prototype xác suất**, không gọi final.

Demo thô nhằm phát hiện lỗi bài, không khoe phối khí. Ghi lại seed ngay khi xuất hiện. Nếu melody-first, dùng âm vô nghĩa để ổn contour/range trước rồi mới ép lời vào.

Không đầu tư full arrangement khi hook, section contrast, prosody hoặc payoff chưa ổn.

## 4. Audit prosody tích hợp

Nghe demo và kiểm theo thứ tự:

1. **Intent:** lời, melody, harmony và rhythm có cùng biểu đạt stable/unstable, căng/thả và mood không?
2. **Natural speech:** trọng âm từ/cụm và phát âm tiếng Việt có bị melody bẻ sai không?
3. **Phrase fit:** số âm tiết, điểm lấy hơi, biên từ và nốt giữ có tự nhiên không?
4. **Hook recall:** sau một lượt, người nghe nhắc lại được lyric, melodic hoặc rhythmic hook chính không?
5. **Section contrast:** Verse/Chorus/Bridge khác vai ở ít nhất một tầng thật: register, contour, rhythm, harmony, density hoặc arrangement.
6. **Range/performance:** người hát mục tiêu có hát được và truyền đúng sắc thái không?
7. **Payoff:** peak lời có trùng hoặc được music trao lực không?

Lyrics-first chưa có demo chỉ chạy được Scope A. Không tuyên bố `music-fit PASS` khi chưa nghe artifact.

Phân biệt trạng thái artifact:

- `LYRIC DRAFT — Scope A chưa qua; music-fit UNKNOWN`: chưa đủ sạch để handoff.
- `SUNO PROTOTYPE-READY — Scope A PASS; music-fit UNKNOWN`: đủ để thử gen; không phải xác nhận prosody âm nhạc.
- `PROSODY PASS — Scope B`: đã nghe melody-demo có lời và pass stress/phrase/breath/range.
- `PRODUCTION CANDIDATE`: đã qua Scope B, performance và feedback gate.

Không suy từ `PROTOTYPE-READY` sang `music-fit`; render đầu là artifact để mở Scope B.

## 5. Rewrite và feedback

Luân phiên theo pass:

1. **Writer pass:** phát triển hoặc thay material, tránh micro-audit liên tục.
2. **Editor pass:** sửa đúng triệu chứng ở intent, form, melody/prosody, line hoặc arrangement.
3. **Re-demo:** nghe lại section bị sửa và toàn bài nếu sửa hook/form.

Không giới hạn hai vòng nếu cùng một lỗi lyric–music còn nghe thấy; dừng khi vòng mới không còn cải thiện rõ hoặc cần tai người.

Trước feedback, nói rõ mục tiêu bài và hỏi cụ thể:

- Chỗ nào mất tập trung hoặc không hiểu?
- Sau một lượt còn nhớ hook nào?
- Đoạn nào cảm xúc/nhạc không khớp hoặc khó hát?

Với bài quan trọng, lấy nhiều ý kiến độc lập. Coi một triệu chứng lặp lại là tín hiệu mạnh hơn một giải pháp đơn lẻ. Người viết quyết định cách sửa.

## 6. Gate production

Chỉ chuyển từ rough demo sang full demo/production khi:

- Central intent và hook đã ổn.
- Lyrics–melody–harmony–rhythm pass prosody ở artifact nghe được.
- Form và section contrast hoạt động.
- Người hát/range/phát âm phù hợp.
- Feedback không còn lỗi gốc lặp lại, hoặc user chủ động chấp nhận trade-off.

## 7. Music Blueprint & Arrangement Arc

> **Quy tắc kích hoạt (Activation Policy):**  
> - **Dormant (Ngủ yên):** Khi yêu cầu là sáng tác ca từ đơn thuần (Lyric-First) và người dùng không yêu cầu phối khí. Tuyệt đối không tự động sinh BPM, Key, Mode, hợp âm hay bảng năng lượng chi tiết khi người dùng chỉ cần một bài hát.  
> - **Active (Kích hoạt):** Chỉ kích hoạt khi người dùng yêu cầu dựng demo âm thanh, định hình bản phối khí hoàn chỉnh, hoặc lập kế hoạch sản xuất chuyên sâu.

Khi ở trạng thái Active, xây dựng **Arrangement Arc** mô tả chuyển động năng lượng qua từng section:

```text
SECTION → ENERGY (1-10) → INSTRUMENTATION → VOCAL DYNAMICS → TRANSITION
```

### Quy tắc Blueprint tương đối (Relative Specification)
- **Mô tả theo section, KHÔNG bịa timestamps giả:** Tuyệt đối không tự bịa mốc thời gian (như `0:00 - 0:30`) khi chưa có file audio thực tế được phân tích. Dùng vị trí section làm đơn vị đo lường.
- **Đường cong năng lượng mẫu:**
  - *Verse 1:* Năng lượng 3–4/10; nhạc cụ mộc/tối giản (acoustic guitar, piano mộc, bass mềm); giọng gần gũi, thủ thỉ.
  - *Pre-Chorus:* Năng lượng 5–6/10; trống/percussion bắt đầu vào nhịp; vocal đẩy cao dần, tạo lực căng (tension).
  - *Chorus 1:* Năng lượng 7–8/10; đầy đủ dàn nhạc (full drums, synth/strings nở rộng); giọng ngân vang, mở sáng.
  - *Verse 2:* Năng lượng 4–5/10; giữ nhịp groove của Chorus nhưng tiết chế bớt nhạc cụ hòa âm để tạo chỗ thở.
  - *Bridge:* Năng lượng đổi hướng (hoặc drop xuống 2–3/10 với nhạc cụ mộc, hoặc bùng nổ lên 9/10); đổi hòa thanh hoặc nhịp điệu.
  - *Final Chorus:* Năng lượng đỉnh cao (9–10/10); bè dày (stacked harmonies), nhạc cụ dày nhất, tạo cảm giác giải phóng trọn vẹn (resolution).
  - *Outro:* Năng lượng hạ dần; nhạc cụ thưa dần để lại dư ba.
- **Chuyển đoạn (Transitions):** Nêu rõ cách kết nối giữa các section (drum fill, silence/pause, reverse cymbal, vocal swell). Không ép bài hát đơn giản phải dùng beat switch phức tạp.

Không phải bài nào cũng cần full demo. Với Suno, render đầu là vòng thử; bản được chọn sau nghe, sửa và re-render mới là candidate để chốt.
