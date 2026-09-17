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
- **Model Profile & Selection:** Sử dụng model production hiện hành (`v6` flagship) làm mặc định cho độ tự nhiên của ca từ tiếng Việt; dùng `v6-wild` khi muốn thể nghiệm âm thanh và lai tạo phong cách (genre-blending); dùng `v6-mini` khi cần lặp nhanh prototype.
- **Vocal Controls & Platform Capabilities:**
  - `Vocal Gender`: Chọn Male / Female toggle trong Advanced Options ở Custom Mode (thay vì chỉ trông chờ vào Style prompt).
  - `Voice Profile / Personas`: Gán Voice đã lưu hoặc Custom Model nếu tài khoản người dùng có sẵn.
  - `Generation Parameters`: Tinh chỉnh Style Influence, Weirdness slider, Audio Extend timestamp tùy nhu cầu bản phối.

---

## 2. Ngân Sách Ký Tự & Hồ Sơ Nền Tảng (Prompt Budget & Platform Profile)

Để phân định rạch ròi giữa **giới hạn kỹ thuật của nền tảng (Platform Limits)** và **kinh nghiệm tối ưu nội bộ (Recommended Heuristics)**:

```yaml
platform: suno
model_profile:
  family: current
  preferred: "v6"                # Model flagship / current production generation
  experimental: "v6-wild"        # Cho phép unexpected choices, genre-blending, thử nghiệm âm thanh
  fast_iteration: "v6-mini"      # Model nhẹ, nhanh cho prototype
  custom_models: "supported"     # Khai thác Custom Models / Personas nếu tài khoản hỗ trợ
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

Suno là hệ thống khuếch tán âm thanh có tính ngẫu nhiên (stochastic). Không dùng ngưỡng cứng nhắc (như máy móc đếm đủ 3 lần), mà đánh giá dựa trên **bằng chứng lặp lại (Repeatable Evidence)**:

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

### 3.3. Ma Trận Vá Lỗi Theo Tầng (Targeted Layer Patching Matrix)

```
             QUAN SÁT THỰC TẾ (USER_REPORT / AUDIO)
                               │
                               ▼
        KIỂM TRA TÍNH LẶP LẠI (Repeatable Evidence Check)
         ├─ Lỗi đơn lẻ ngẫu nhiên ──► RE-ROLL (Giữ nguyên prompt)
         └─ Có bằng chứng quy luật
                               │
                               ▼
                     XÁC ĐỊNH TẦNG BỊ LỖI
                               │
                               ▼
                    VÁ ĐÚNG DUY NHẤT TẦNG ĐÓ
             (Giữ nguyên 100% các tầng không liên quan)
```

| Triệu chứng lỗi lặp lại | Tầng lỗi thực tế | Hành động vá lỗi cục bộ (Targeted Patch) | Điều TUYỆT ĐỐI KHÔNG làm |
|---|---|---|---|
| **Hát lơ lớ, ngọng dấu thanh điệu** | `LYRICS / PHONETIC FIT` | Tìm đúng từ/cụm bị sai; thay bằng từ đồng nghĩa có thanh điệu tự nhiên hơn hoặc đổi sang nguyên âm mở. | Không viết lại Tứ; không sửa Style prompt. |
| **Giọng hát bị đổi giới tính (nam $\leftrightarrow$ nữ)** | `STYLE / VOCAL IDENTITY` | Dùng tùy chọn Vocal Gender chính thức trong Advanced Options nếu có; hoặc thêm từ khóa nhấn mạnh vào Style: `solo female vocal throughout` (hoặc `male vocal only`). | Không sửa lời bài hát; không đụng vào melody. |
| **Dồn chữ, nuốt chữ ở cuối câu** | `LYRICS / ONE-BREATH` | Dòng đó quá dài; bổ sung dấu phẩy ngắt nhịp hoặc cắt bớt 2–3 chữ thừa/hư từ để phrase có chỗ thở tự nhiên. | Không sửa các câu xung quanh; không đổi cấu trúc đoạn. |
| **Ngân chữ cuối quá dài, kéo lê thê** | `LYRICS / LINE LANDING` | Từ cuối dòng rơi vào nguyên âm quá mở hoặc thiếu điểm dừng; đổi từ kết dòng thành âm có điểm rơi gọn, hoặc thêm dấu phẩy ngắt nhịp. | Không viết lại cả Chorus. |
| **Section bị phẳng lì, không có cao trào** | `CONTROLS / ARRANGEMENT CUE` | Thêm cue năng lượng ở đầu đoạn: `[Chorus: Powerful beat drop, soaring vocal]` hoặc nén nhịp ca từ ngắn lại. | Không thay đổi cốt truyện hay Tứ của bài. |
| **Hát luôn cả thẻ tag vào lời** | `LYRICS / METATAG BLEED` | Tag quá phức tạp hoặc đặt sai chỗ; lược bỏ các từ rườm rà trong ngoặc vuông, đưa hướng dẫn nhạc cụ về Style Prompt. | Không đổi lời ca. |
| **Lệch / trôi thể loại (Genre Drift)** | `STYLE / GENRE TRIAGE` | Phân loại rõ: <br>1. `PROMPT_CONFLICT`: Thể loại triệt tiêu nhau $\rightarrow$ Tinh lọc lại danh mục nhạc cụ.<br>2. `MODEL_VARIANCE`: Model có độ biến thiên cao (nhánh wild) $\rightarrow$ Siết chặt từ khóa neo thể loại hoặc chọn model profile tiêu chuẩn.<br>3. `INTENTIONAL_FUSION`: Người dùng chủ ý lai tạo phong cách $\rightarrow$ Giữ nguyên, chỉ cân chỉnh tỉ trọng từ khóa. | Không đụng vào ca từ; không tự tiện xóa bỏ ý đồ lai tạo thể loại của người dùng. |

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
