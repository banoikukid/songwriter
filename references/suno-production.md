# Quy Chuẩn Sản Xuất Suno AI (Suno Production & Diagnosis Protocol)

> **Mục đích:** Cung cấp mô hình sản xuất 3 khối chuẩn mực, kiểm soát ngân sách ký tự, cú pháp metatags và ma trận chẩn đoán lỗi Suno để vá lỗi cục bộ đúng tầng mà không làm hỏng bài hát.

---

## 1. Mô Hình Sản Xuất Ba Khối (Style – Lyrics – Control)

Khi handoff sang Suno, đóng gói artifact thành 3 khối tách biệt:

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
- **Nội dung:** Thể loại (Genre), Nhịp điệu (Groove/Tempo), Nhạc cụ chủ đạo (Instrumentation), Âm hưởng không gian (Mood/Production) và **Vocal Identity** (Bản sắc giọng cốt lõi).
- **Quy tắc vàng:** Không nhắc tên nghệ sĩ thương mại cụ thể; dùng đặc trưng âm thanh để định hình.
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

## 2. Ngân Sách Ký Tự (Prompt & Character Budget)

Để tránh bị cắt cụt (truncation) hoặc làm loãng sự chú ý của mô hình AI:

| Hạng mục | Ngân sách ký tự khuyến nghị | Giới hạn an toàn | Lưu ý xử lý |
|---|---|---|---|
| **Style Prompt** | $120 - 180$ ký tự | Tối đa $200$ ký tự | Ưu tiên từ khóa âm nhạc đắt giá; bỏ liên từ rườm rà. |
| **Lyrics Sheet** | $1200 - 2500$ ký tự | Tối đa $3500 - 5000$ ký tự | Bài chuẩn gồm 2 Verses, 1-2 Pre, 2-3 Choruses, 1 Bridge, 1 Outro. |
| **Section Tag / Cue** | $\le 40$ ký tự / tag | Tối đa 1 cue / section | Không nhồi nhét cả câu văn vào trong dấu ngoặc vuông `[...]`. |

---

## 3. Ma Trận Chẩn Đoán Lỗi Suno & Vá Lỗi Đúng Tầng (Suno Failure Diagnosis & Targeted Patching)

Khi nghe bản render đầu tiên (prototype) và phát hiện lỗi, **tuyệt đối không đập đi viết lại toàn bài**. Hãy xác định chính xác tầng lỗi và chỉ vá duy nhất tầng đó:

```
                  BẢN RENDER SUNO CÓ LỖI
                             │
            ┌────────────────┴────────────────┐
            ▼                                 ▼
   XÁC ĐỊNH TRIỆU CHỨNG              PHÂN LOẠI TẦNG LỖI
            │                                 │
            └────────────────┬────────────────┘
                             ▼
                 VÁ ĐÚNG DUY NHẤT TẦNG ĐÓ
            (Giữ nguyên 100% các tầng khác)
```

| Triệu chứng lỗi trên audio | Tầng lỗi thực tế | Hành động vá lỗi (Targeted Patch) | Điều TUYỆT ĐỐI KHÔNG làm |
|---|---|---|---|
| **Hát lơ lớ, ngọng dấu thanh điệu** | `PHONETIC FIT` (Ngữ âm tiếng Việt) | Tìm đúng từ/cụm bị sai; thay bằng từ đồng nghĩa có thanh điệu tự nhiên hơn hoặc đổi sang nguyên âm mở. | Không viết lại Tứ; không sửa Style prompt. |
| **Giọng hát bị đổi giới tính (nam $\leftrightarrow$ nữ)** | `VOCAL IDENTITY` (Style Prompt) | Thêm từ khóa nhấn mạnh vào Style: `solo female vocal throughout` (hoặc `male vocal only`). | Không sửa lời bài hát; không đụng vào melody. |
| **Dồn chữ, nuốt chữ ở cuối câu** | `ONE-BREATH / PROSE-TO-LYRIC` | Dòng đó quá dài ($>12$ âm tiết); cắt bớt 2–3 chữ thừa/hư từ để phrase có chỗ thở. | Không sửa các câu xung quanh; không đổi cấu trúc đoạn. |
| **Ngân chữ cuối quá dài, kéo lê thê** | `LINE LANDING / CHECKED-CODA` | Từ cuối dòng rơi vào nguyên âm quá mở hoặc thiếu điểm dừng; đổi từ kết dòng thành âm có điểm rơi gọn, hoặc thêm dấu phẩy ngắt nhịp. | Không viết lại cả Chorus. |
| **Section bị phẳng lì, không có cao trào** | `ARRANGEMENT ARC / ENERGY` | Thêm cue năng lượng ở đầu đoạn: `[Chorus: Powerful beat drop, soaring vocal]` hoặc nén nhịp ca từ ngắn lại. | Không thay đổi cốt truyện hay Tứ của bài. |
| **Hát luôn cả thẻ tag vào lời** | `METATAG BLEED` | Tag quá phức tạp hoặc đặt sai chỗ; lược bỏ các từ rườm rà trong ngoặc vuông, đưa hướng dẫn nhạc cụ về Style Prompt. | Không đổi lời ca. |
| **Lạc sang thể loại khác (Genre Drift)** | `STYLE PROMPT CONFLICT` | Style prompt chứa các thể loại triệt tiêu nhau (ví dụ: `acoustic folk` đi cùng `heavy synthesizer`); tinh lọc lại danh mục nhạc cụ. | Không đụng vào ca từ. |

---

## 4. Quy Trình Vòng Lặp Sản Xuất (Production Loop)

1. **Pass 1 — Prototype Test:**
   - Handoff với nhãn `[SUNO PROTOTYPE-READY — Scope A PASS; music-fit UNKNOWN]`.
   - Sinh $1 - 2$ biến thể để kiểm tra: (a) Giọng hát có đúng tính cách không; (b) Phát âm tiếng Việt có rõ dấu không; (c) Nhịp điệu và năng lượng có nâng đỡ ca từ không.
2. **Pass 2 — Targeted Patching:**
   - Nghe và đối chiếu bảng chẩn đoán ở Mục 3.
   - Sửa cục bộ đúng dòng/từ hoặc tham số bị lỗi.
3. **Pass 3 — Production Candidate:**
   - Chỉ gắn nhãn `[PRODUCTION CANDIDATE]` khi cả 3 yếu tố: **Ý nghĩa lời – Ngữ âm phát âm – Hòa âm phối khí** đều hòa quyện và được tai người xác nhận.
