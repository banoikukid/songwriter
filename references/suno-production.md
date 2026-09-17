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
│ 3. CONTROL PARAMETERS (Model version, Style/Audio Influence) │
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
- **Model Version:** Khuyến nghị Suno v3.5 hoặc v4 cho tiếng Việt tự nhiên nhất.
- **Generation Parameters:** Ghi chú rõ các tham số nếu platform hỗ trợ (Style Influence, Weirdness, Audio Extend timestamp).

---

## 2. Ngân Sách Ký Tự & Hồ Sơ Nền Tảng (Prompt Budget & Platform Profile)

Ngân sách ký tự là ràng buộc kỹ thuật của nền tảng bên ngoài (external constraint), được quản lý dưới dạng **Platform Profile** cấu hình linh hoạt:

```yaml
platform: suno
current_profile: "v3.5_v4_production"
fields:
  style_prompt:
    hard_limit: 1000        # Giới hạn kỹ thuật tối đa của giao diện Suno
    recommended_budget: 150 # Khoảng tối ưu để prompt cô đọng, tránh loãng attention
    guideline: "Ưu tiên từ khóa âm nhạc đắt giá; bỏ liên từ rườm rà."
  lyrics_sheet:
    hard_limit: 3000        # Giới hạn hiển thị và render an toàn
    recommended_budget: 1800 # Độ dài bài chuẩn (2 Verses, 1-2 Pre, 2-3 Choruses, Bridge, Outro)
    guideline: "Viết đầy đủ các section lặp; đảm bảo cấu trúc bài hoàn chỉnh."
  section_cue:
    hard_limit: 60          # Ký tự tối đa trong 1 cặp ngoặc vuông
    recommended_budget: 35
    guideline: "Tối đa 1 cue ở đầu section; cấm chèn cue giữa dòng lyric."
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

### 3.2. Kiểm Tra Tính Lặp Lại: Stochastic Variation vs Repeatable Pattern

Suno là một hệ thống khuếch tán âm thanh có tính ngẫu nhiên cao (stochastic model). Cùng một prompt có thể sinh ra các bản render rất khác nhau:

- **Single-Output Anomaly (Bất thường đơn lẻ 1 lần):**  
  *Ví dụ:* 3 lần gen đều là giọng nữ đúng yêu cầu, nhưng 1 lần đột nhiên nhảy sang giọng nam; hoặc 1 lần bị trượt nhịp ngẫu nhiên.  
  $\rightarrow$ **Giải pháp:** **RE-ROLL** (tạo lại lượt mới với đúng prompt đó). **Tuyệt đối không can thiệp sửa prompt/lyric khi chưa xác nhận lỗi có tính lặp lại.**
- **Repeatable Pattern (Lỗi có tính quy luật lặp lại):**  
  *Ví dụ:* $3/3$ lần gen đều bị ngọng cùng một từ; hoặc tất cả các bản render đều bị bẹt năng lượng ở Chorus.  
  $\rightarrow$ **Giải pháp:** Đã có bằng chứng xác đáng (evidence). Kích hoạt **Targeted Layer Patching**.

---

### 3.3. Ma Trận Vá Lỗi Theo Tầng (Targeted Layer Patching Matrix)

```
             QUAN SÁT THỰC TẾ (USER_REPORT / AUDIO)
                               │
                               ▼
        KIỂM TRA TÍNH LẶP LẠI (Repeatability Check)
         ├─ Lỗi đơn lẻ 1 lần ──► RE-ROLL (Giữ nguyên prompt)
         └─ Lỗi lặp lại nhiều lần
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
| **Giọng hát bị đổi giới tính (nam $\leftrightarrow$ nữ)** | `STYLE / VOCAL IDENTITY` | Thêm từ khóa nhấn mạnh vào Style: `solo female vocal throughout` (hoặc `male vocal only`). | Không sửa lời bài hát; không đụng vào melody. |
| **Dồn chữ, nuốt chữ ở cuối câu** | `LYRICS / ONE-BREATH` | Dòng đó quá dài ($>12$ âm tiết); cắt bớt 2–3 chữ thừa/hư từ để phrase có chỗ thở. | Không sửa các câu xung quanh; không đổi cấu trúc đoạn. |
| **Ngân chữ cuối quá dài, kéo lê thê** | `LYRICS / LINE LANDING` | Từ cuối dòng rơi vào nguyên âm quá mở hoặc thiếu điểm dừng; đổi từ kết dòng thành âm có điểm rơi gọn, hoặc thêm dấu phẩy ngắt nhịp. | Không viết lại cả Chorus. |
| **Section bị phẳng lì, không có cao trào** | `CONTROLS / ARRANGEMENT CUE` | Thêm cue năng lượng ở đầu đoạn: `[Chorus: Powerful beat drop, soaring vocal]` hoặc nén nhịp ca từ ngắn lại. | Không thay đổi cốt truyện hay Tứ của bài. |
| **Hát luôn cả thẻ tag vào lời** | `LYRICS / METATAG BLEED` | Tag quá phức tạp hoặc đặt sai chỗ; lược bỏ các từ rườm rà trong ngoặc vuông, đưa hướng dẫn nhạc cụ về Style Prompt. | Không đổi lời ca. |
| **Lạc sang thể loại khác (Genre Drift)** | `STYLE / PROMPT CONFLICT` | Style prompt chứa các thể loại triệt tiêu nhau (ví dụ: `acoustic folk` đi cùng `heavy synthesizer`); tinh lọc lại danh mục nhạc cụ. | Không đụng vào ca từ. |

---

## 4. Quy Trình Vòng Lặp Sản Xuất (Production Loop)

1. **Pass 1 — Prototype Test:**
   - Handoff với nhãn `[SUNO PROTOTYPE-READY — Scope A PASS; music-fit UNKNOWN]`.
   - Sinh $1 - 2$ biến thể để kiểm tra: (a) Giọng hát có đúng tính cách không; (b) Phát âm tiếng Việt có rõ dấu không; (c) Nhịp điệu và năng lượng có nâng đỡ ca từ không.
2. **Pass 2 — Targeted Patching:**
   - Chỉ khi phát hiện lỗi lặp lại qua quan sát thực tế (User report / Audio), áp dụng Targeted Patch ở Mục 3.
   - Sửa cục bộ đúng dòng/từ hoặc tham số bị lỗi.
3. **Pass 3 — Production Candidate:**
   - Chỉ gắn nhãn `[PRODUCTION CANDIDATE]` khi cả 3 yếu tố: **Ý nghĩa lời – Ngữ âm phát âm – Hòa âm phối khí** đều hòa quyện và được tai người xác nhận.
