# Quy Chuẩn Sản Xuất Suno AI (Suno Production & Diagnosis Protocol)

> **Lưu ý kiến trúc quan trọng:**  
> Khối định dạng `STYLE PROMPT` – `LYRICS BLOCK` – `CONTROLS / SETTINGS` chỉ là **hợp đồng định dạng xuất ra (Output Contract)** của **Suno Adapter**.  
> Đây **tuyệt đối KHÔNG phải mô hình tư duy nội tại (internal cognitive model)** của người viết ca khúc. Quá trình sáng tác của Songwriter luôn bắt đầu từ:  
> `Tứ → Central Intent → Hook → Image System → Form → Lyric`.  
> Chỉ khi người dùng yêu cầu đóng gói sang Suno, Suno Adapter mới ánh xạ kết quả vào 3 khối này.

---

## 1. Mô Hình Xuất 3 Khối Của Suno Adapter (Output Contract)

```text
┌──────────────────────────────────────────────────────────────┐
│ 1. STYLE PROMPT (Genre, Instruments, Groove, Vocal Identity) │
├──────────────────────────────────────────────────────────────┤
│ 2. LYRICS & CUES (Structure tags, Vocal Direction, Lyrics)   │
├──────────────────────────────────────────────────────────────┤
│ 3. CONTROL PARAMETERS (Model Selection, Vocal Gender, Params)│
└──────────────────────────────────────────────────────────────┘
```

### Khối 1: STYLE PROMPT
- **Nội dung:** Thể loại (Genre), Nhịp điệu (Groove/Tempo), Nhạc cụ chủ đạo (Instrumentation), Không gian âm thanh (Mood/Production) và **Vocal Identity** (Bản sắc giọng cốt lõi: giới tính, âm sắc).
- **Quy tắc vàng:** Không nhắc tên nghệ sĩ thương mại cụ thể; dùng đặc trưng âm thanh và Style DNA trừu tượng để định hình.
- *Ví dụ:* `Vietnamese indie folk pop, acoustic guitar, warm upright bass, gentle shaker, intimate breathy female vocal, melancholy, warm analog sound`

### Khối 2: LYRICS & CUES
- **Section Tags chuẩn:** `[Verse]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Outro]`.
- **Combined-bracket cues (Tối giản):** Có thể kèm định hướng biểu diễn ngắn gọn ở đầu section: `[Chorus: Soaring vocal, full band entrance]` hoặc `[Verse 1: Soft acoustic fingerpicking]`.
- **Cảnh báo Metatag Bleed:** Không chèn cues dày đặc giữa các dòng thơ; Suno có thể hiểu nhầm và hát luôn cả tag vào ca từ.
- **Viết đủ các lượt lặp:** Viết trọn vẹn mọi lần xuất hiện của Chorus, không dùng ghi chú `"Lặp lại Chorus 2 lần"`.

### Khối 3: CONTROL PARAMETERS
- **Model Profile & Selection:** Sử dụng model production hiện hành (`v6` flagship / default production model) làm mặc định về tính biểu cảm, linh hoạt và độ kiểm soát; dùng `v6-wild` khi muốn thể nghiệm âm thanh và lai tạo phong cách (genre-blending); dùng `v6-mini` khi cần lặp nhanh prototype.
- **Vocal Controls & Platform Capabilities:**
  - `Vocal Gender`: Chọn Male / Female toggle trong Advanced Options ở Custom Mode (thay vì chỉ trông chờ vào Style prompt).
  - `VOICE_PROFILE` (Voices / Personas): Lớp cá nhân hóa giọng hát (Voice Personalization) giúp giữ màu giọng và âm sắc nhất quán giữa các bài/lần gen.
  - `CUSTOM_MODEL`: Mô hình riêng biệt được huấn luyện/tạo từ các track của người dùng (tài khoản hỗ trợ).
  - `REMASTER`: Tái xử lý âm thanh giữ nguyên cấu trúc/lyrics/performance tương đối ổn định để cải thiện độ nét (clarity), chi tiết mix/texture và độ rõ phát âm.
  - `Generation Parameters`: Tinh chỉnh Style Influence, Weirdness slider, Audio Extend timestamp tùy nhu cầu bản phối.

---

## 2. Ngân Sách Ký Tự & Hồ Sơ Nền Tảng (Prompt Budget & Platform Profile)

Để phân định rạch ròi giữa **giới hạn kỹ thuật của nền tảng (Platform Limits)** và **kinh nghiệm tối ưu nội bộ (Recommended Heuristics)**:

```yaml
platform: suno
model_profile:
  family: current
  preferred: "v6"                # Current flagship / default production model
  experimental: "v6-wild"        # Cho phép unexpected choices, genre-blending, thử nghiệm âm thanh
  fast_iteration: "v6-mini"      # Model nhẹ, nhanh cho prototype
  voice_profiles: "supported"    # Tách biệt: Voices / Personas (cá nhân hóa âm sắc giọng hát)
  custom_models: "supported"     # Tách biệt: Custom Models (model riêng tạo từ tracks)
  remaster: "supported"          # Tái xử lý âm thanh giữ cấu trúc/lời để nâng clarity & mix
  verify_official_docs: true     # Luôn đối chiếu tài liệu và giao diện thực tế tại thời điểm chạy

budget_policy:
  style_prompt:
    platform_limit:
      value: PLATFORM_DEPENDENT   # Ràng buộc UI/API của platform tại thời điểm thực tế
      source: OFFICIAL_UI_OR_DOCS
    recommended_budget:
      value: 120-180 ký tự
      type: INTERNAL_HEURISTIC   # Tránh làm loãng attention của mô hình AI; tập trung từ khóa âm nhạc đắt
      guideline: "Ưu tiên từ khóa âm nhạc trọng tâm; bỏ liên từ và giải thích rườm rà."

  lyrics_sheet:
    platform_limit:
      value: PLATFORM_DEPENDENT   # Giới hạn ô nhập lời của giao diện
      source: OFFICIAL_UI_OR_DOCS
    recommended_budget:
      value: 1200-2500 ký tự
      type: INTERNAL_HEURISTIC   # Độ dài tiêu chuẩn cho ca khúc hoàn chỉnh có đầy đủ section lặp
      guideline: "Viết đầy đủ các section lặp; đảm bảo tính toàn vẹn của cấu trúc bài."

  section_cue:
    platform_limit:
      value: PLATFORM_DEPENDENT
      source: OFFICIAL_UI_OR_DOCS
    recommended_budget:
      value: <= 40 ký tự
      type: INTERNAL_HEURISTIC   # Tối giản để triệt tiêu nguy cơ metatag bleed
      guideline: "Tối đa 1 cue ở đầu section; tuyệt đối cấm chèn cue giữa dòng lyric."
```

---

## 3. Ma Trận Chẩn Đoán Lỗi Suno & Vá Lỗi Đúng Tầng (Failure Diagnosis & Targeted Patching)

### 3.1. Phân Loại Nguồn Quan Sát (Observation Source & Confidence)

Trước khi kết luận bất kỳ lỗi nào trên bản render, agent phải phân định rõ nguồn thông tin:

| Nguồn quan sát | Độ tin cậy (Confidence) | Hành vi của Agent |
|---|---|---|
| **USER_REPORT** | **High** | Người dùng nghe trực tiếp và phản hồi cụ thể (ví dụ: *"chữ 'cũ' bị ngọng", "giọng nam bị nhảy sang nữ"*). $\rightarrow$ Kích hoạt quy trình chẩn đoán ngay. |
| **AUDIO_OBSERVATION** | **High / Medium** | Phân tích trực tiếp từ file audio demo (nếu hệ thống hỗ trợ multi-modal input). $\rightarrow$ Kích hoạt chẩn đoán theo bằng chứng nghe được. |
| **MODEL_INFERENCE** | **Low (Giả thuyết tạm thời)** | Agent tự suy đoán (ví dụ: *"có vẻ Suno sẽ gặp khó với từ này"*). $\rightarrow$ **CẤM tự ý sửa prompt/lyric.** Chỉ ghi chú như một rủi ro tiềm ẩn cần người dùng nghe kiểm tra. |

---

### 3.2. Đánh Giá Bằng Chứng Lặp Lại (Evidence-Based Repeatability)

Suno có tính ngẫu nhiên và tạo sinh (stochastic / generative), kết quả có thể biến thiên giữa các lần tạo (outputs vary across generations). Không suy đoán kiến trúc mô hình nội bộ và không dùng ngưỡng cứng nhắc (như máy móc đếm đủ 3 lần), mà đánh giá dựa trên **bằng chứng lặp lại (Repeatable Evidence)**:

- **Single-Output Anomaly (Bất thường ngẫu nhiên đơn lẻ):**  
  *Ví dụ:* Lần đầu gen đúng giọng nữ, lần hai đột nhiên nhảy sang giọng nam; hoặc một nốt bị trượt nhịp ngẫu nhiên 1 lần.  
  $\rightarrow$ **Giải pháp:** **RE-ROLL** (tạo lại lượt mới với cùng prompt). **Không can thiệp sửa prompt/lyric khi lỗi chỉ là ngẫu nhiên đơn lẻ.**
- **Repeatable Evidence (Bằng chứng có tính quy luật):**  
  Xác định khi hội đủ các tín hiệu:
  - **Frequency & Specificity:** Lỗi xuất hiện lặp lại (ví dụ 2 lần liên tiếp người dùng đều nghe thấy cùng một từ bị ngọng).
  - **Same Location & Symptom:** Cùng rơi vào đúng từ/câu/vị trí section cụ thể (chữ kết dòng Chorus, nốt cao Bridge).
  - **Same Generation Setup:** Xảy ra trên cùng một model profile và cùng cấu hình tham số.  
  $\rightarrow$ **Giải pháp:** Đã có bằng chứng xác đáng. Kích hoạt **Targeted Layer Patching**.

---

### 3.3. Đánh Giá Độ Tin Cậy Của Nguyên Nhân (Cause Confidence Assessment)

Trước khi quyết định vá tầng nào, agent phải đánh giá xem nguyên nhân gây ra lỗi đến từ đâu, tránh vội vã sửa ca từ khi lỗi bắt nguồn từ mô hình hoặc biểu diễn:

> **BẤT BIẾN CHẨN ĐOÁN (EVIDENCE-FIRST INVARIANT):**  
> **Heuristic chỉ có quyền tăng mức độ nghi vấn (Suspicion ↑), tuyệt đối không có quyền biến giả thuyết (hypothesis) thành quan sát thực tế (observation).**  
> *Ví dụ:* Từ kết dòng là nguyên âm mở $\rightarrow$ `Suspicion ↑`, **chứ không phải** `Cause = Lyric`. Chỉ khi người dùng nghe bản render xác nhận chữ đó bị ngân lê thê lặp lại trên cùng setup, thì mới có căn cứ xem xét `LYRIC_INDUCED`. Nếu chưa có bằng chứng audio/người nghe, mọi phán đoán âm học chỉ dừng ở mức *giả thuyết tạm thời* (`MODEL_INFERENCE` — Confidence Low).
> 
> **Phân biệt Causal Plausibility vs Failure Evidence:**
> - *Causal Plausibility (Khả năng nguyên nhân hợp lý):* Ví dụ khi giọng hát bị trôi giới tính và kiểm tra thấy prompt chưa chỉ định toggle $\rightarrow$ Khả năng do prompt thiếu chỉ định là có cơ sở (`Plausibility = Medium/High`).
> - *Failure Evidence (Bằng chứng xác thực lỗi):* Để kích hoạt vá tầng, bắt buộc phải có bằng chứng quan sát thực tế (User report hoặc Audio demo) xác nhận lỗi lặp lại. Heuristic hay Plausibility chỉ tăng mức nghi vấn, không phải bằng chứng lỗi (*Heuristic increases suspicion; Heuristic ≠ proof of failure*).

```text
TRIỆU CHỨNG (ví dụ: Ngân chữ cuối quá dài)
   │
   ├── LYRIC-INDUCED (Confidence: Cao chỉ khi nghe audio/user report xác nhận từ kết âm mở không có điểm dừng)
   ├── VOCAL-PERFORMANCE-INDUCED (Confidence: Cao nếu có cue [Belt]/[Soaring] kéo dài)
   ├── MELODY-INDUCED (Do tiết tấu và beat drop tại cadence)
   ├── MODEL-VARIANCE (Do model ngẫu nhiên giữ note)
   └── UNKNOWN (Chưa đủ căn cứ → Re-roll trước)
```

- Nếu `Cause Confidence` vào tầng Lyric là cao $\rightarrow$ Vá tầng `Lyrics / Line Landing`.
- Nếu lỗi do model variance hoặc vocal cue $\rightarrow$ Tinh chỉnh cue hoặc re-roll, **tuyệt đối KHÔNG sửa ca từ**.

---

### 3.4. Ma Trận Vá Lỗi Theo Tầng (Targeted Layer Patching Matrix)

```
             QUAN SÁT THỰC TẾ (USER_REPORT / AUDIO)
                               │
                               ▼
        KIỂM TRA TÍNH LẶP LẠI (Repeatable Evidence Check)
         ├─ Lỗi đơn lẻ ngẫu nhiên ──► RE-ROLL (Giữ nguyên prompt)
         └─ Có bằng chứng quy luật
                               │
                               ▼
        ĐÁNH GIÁ NGUYÊN NHÂN (Cause Confidence Assessment)
                               │
                               ▼
                     XÁC ĐỊNH TẦNG BỊ LỖI
                               │
                               ▼
                    VÁ ĐÚNG DUY NHẤT TẦNG ĐÓ
             (Giữ nguyên 100% các tầng không liên quan)
```

| Triệu chứng lỗi lặp lại | Nguyên nhân khả dĩ & Độ tin cậy (Likely Cause) | Tầng lỗi thực tế | Hành động vá lỗi cục bộ (Targeted Patch) | Điều TUYỆT ĐỐI KHÔNG làm |
|---|---|---|---|---|
| **Hát lơ lớ, ngọng dấu thanh điệu** | `PHONETIC_FIT` (Confidence: High nếu lặp lại ở cùng một từ) | `LYRICS / PHONETIC FIT` | Tìm đúng từ/cụm bị sai; thay bằng từ đồng nghĩa có thanh điệu tự nhiên hơn hoặc đổi sang nguyên âm mở. | Không viết lại Tứ; không sửa Style prompt. |
| **Giọng hát bị đổi giới tính (nam $\leftrightarrow$ nữ)** | `GENDER_DRIFT` (Confidence: High nếu prompt thiếu chỉ định hoặc model bỏ qua prompt) | `CONTROLS / VOCAL GENDER` hoặc `STYLE / VOCAL IDENTITY` | Ưu tiên chọn Vocal Gender trong Advanced Options; nếu không có, thêm từ khóa nhấn mạnh vào Style: `solo female vocal throughout` (hoặc `male vocal only`). | Không sửa lời bài hát; không đụng vào melody. |
| **Dồn chữ, nuốt chữ ở cuối câu** | `BREATH_OVERLOAD` (Confidence: High chỉ khi audio/user report xác nhận hát bị dồn dập, hoặc câu vượt quá không gian phrase/hơi thở cho phép; số âm tiết chỉ là signal, không phải ngưỡng cứng) | `LYRICS / ONE-BREATH` | Bổ sung dấu phẩy ngắt nhịp hoặc cắt bớt 2–3 chữ thừa/hư từ để phrase có chỗ thở tự nhiên. | Không sửa các câu xung quanh; không đổi cấu trúc đoạn. |
| **Ngân chữ cuối quá dài, kéo lê thê** | 1. `LYRIC_INDUCED` (nguyên âm quá mở)<br>2. `CUE_INDUCED` (tag soaring/belt)<br>3. `MODEL_VARIANCE` | `LYRICS / LINE LANDING` (nếu lyric) hoặc `CONTROLS / CUE` (nếu do cue) | Nếu do lyric: đổi từ kết dòng sang âm có điểm rơi gọn hoặc thêm dấu phẩy ngắt nhịp. Nếu do cue: bỏ các tag [Soaring]/[Belt] ở cuối đoạn. Nếu do model variance: re-roll. | Không vội vã sửa ca từ khi lỗi do model variance hoặc cue; không viết lại cả Chorus. |
| **Section bị phẳng lì, không có cao trào** | `ENERGY_DEFICIT` (Confidence: High nếu thiếu dynamic contrast giữa các đoạn) | `CONTROLS / ARRANGEMENT CUE` | Thêm cue năng lượng ở đầu đoạn: `[Chorus: Powerful beat drop, soaring vocal]` hoặc nén nhịp ca từ ngắn lại. | Không thay đổi cốt truyện hay Tứ của bài. |
| **Hát luôn cả thẻ tag vào lời** | `METATAG_BLEED` (Confidence: High nếu tag phức tạp hoặc chèn giữa câu) | `LYRICS / METATAG BLEED` | Lược bỏ các từ rườm rà trong ngoặc vuông, đưa hướng dẫn nhạc cụ về Style Prompt. | Không đổi lời ca. |
| **Bản thu bị đục, thiếu độ nét mix/texture hoặc phát âm chưa sáng (trong khi cấu trúc, ca từ và diễn xuất vocal đã ưng ý)** | `PRODUCTION_TEXTURE / MIX_CLARITY` (Confidence: High khi cấu trúc bài, lyric và performance đã hoàn thành tốt) | `PRODUCTION / REMASTER` | Sử dụng tính năng **Remaster** của Suno để tinh chỉnh độ trong (clarity), chi tiết mix/texture hoặc phát âm mà vẫn giữ ổn định cấu trúc và bản diễn xuất; tinh chỉnh nhẹ Style prompt nếu cần. | Không viết lại ca từ; không xóa bản thu ưng ý để re-generate toàn bộ track từ đầu. |
| **Lệch / trôi thể loại (Genre Drift)** | 1. `PROMPT_CONFLICT`<br>2. `MODEL_VARIANCE`<br>3. `INTENTIONAL_FUSION` | `STYLE / GENRE TRIAGE` | Phân loại rõ: <br>1. Xung đột prompt $\rightarrow$ Tinh lọc danh mục nhạc cụ.<br>2. Biến thiên model $\rightarrow$ Siết chặt từ khóa neo thể loại hoặc chọn model profile tiêu chuẩn.<br>3. Ý đồ lai tạo $\rightarrow$ Giữ nguyên, chỉ cân chỉnh tỉ trọng từ khóa. | Không đụng vào ca từ; không tự tiện xóa bỏ ý đồ lai tạo thể loại của người dùng. |


---

## 4. Quy Trình Vòng Lặp Sản Xuất (Production Loop)

1. **Pass 1 — Prototype Test:**
   - Handoff với nhãn `[SUNO PROTOTYPE-READY — Scope A PASS; music-fit UNKNOWN]`.
   - Sinh $1 - 2$ biến thể để kiểm tra: (a) Giọng hát có đúng tính cách không; (b) Phát âm tiếng Việt có rõ dấu không; (c) Nhịp điệu và năng lượng có nâng đỡ ca từ không.
2. **Pass 2 — Targeted Patching:**
   - Chỉ khi phát hiện lỗi lặp lại có bằng chứng qua quan sát thực tế (User report / Audio), áp dụng Targeted Patch ở Mục 3.
   - Sửa cục bộ đúng dòng/từ hoặc tham số bị lỗi.
3. **Pass 3 — Production Candidate:**
   - Chỉ gắn nhãn `[PRODUCTION CANDIDATE]` khi cả 3 yếu tố: **Ý nghĩa lời – Ngữ âm phát âm – Hòa âm phối khí** đều hòa quyện và được tai người xác nhận.
