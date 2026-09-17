# Vietnamese Spoken Form & Prosody: Khẩu Ký Ca Từ & Ngữ Âm Khi Hát

> **Triết lý cốt lõi:**  
> **LYRIC WRITTEN FORM (Dạng chữ viết)** và **LYRIC SPOKEN/SUNG FORM (Dạng phát âm khi hát)** là hai tầng biểu diễn khác nhau.  
> *Nguyên tắc tối thượng:* **Spoken Form là công cụ chẩn đoán (Diagnostic), KHÔNG PHẢI công cụ tự động viết lại (Rewrite mặc định).**  
> Tuyệt đối không xóa bản sắc ca từ hay từ ngữ riêng của tác giả chỉ để thỏa mãn quy tắc ngữ âm máy móc.

---

## 1. Bản Chất Hai Tầng Biểu Diễn (Written vs. Spoken Realization)

Trong ca từ tiếng Việt hiện đại và nhạc AI (Suno / Udio / Vocal synth), văn bản ca từ thường chứa:
- Từ mượn tiếng Anh / tiếng nước ngoài;
- Chữ số, ngày tháng, mốc thời gian;
- Viết tắt, ký tự đặc biệt, tên riêng;
- Khẩu ngữ và phương ngữ.

```text
VĂN BẢN NGHỆ THUẬT (Written Form)
(Lưu giữ tính thẩm mỹ, thị giác và ý đồ tác giả)
            │
            ▼
    [BỘ LỌC CHẨN ĐOÁN / SPOKEN-FORM DIAGNOSTIC]
    (Kiểm tra rủi ro phát âm, nhịp thở, độ nuốt chữ của engine/ca sĩ)
            │
            ▼
CƠ CHẾ PHÁT ÂM KHI HÁT (Spoken / Sung Realization)
(Chỉ chú thích phát âm khi có nguy cơ đọc sai, không làm bẩn bản lời gốc)
```

### Nguyên tắc can thiệp (Intervention Guardrails):
1. **Giữ nguyên Written Form làm gốc:** Nếu tác giả/người dùng viết *"2026"* hoặc *"AI"*, giữ nguyên *"2026"* và *"AI"* trong bản lyric chính thức.
2. **Không tự động ép phiên âm tiếng Việt:** Không tự ý đổi mọi chữ tiếng Anh sang phiên âm ngô nghê (*running $\rightarrow$ răn ninh*, *game $\rightarrow$ gêm*) trong bản lyric xuất bản trừ khi người dùng chủ động yêu cầu hoặc dùng làm prompt phonetic riêng cho AI engine.
3. **Chỉ can thiệp khi có nguy cơ cao (High Pronunciation Risk):** Khi phát hiện engine AI hoặc ca sĩ có khả năng đọc sai gây lệch hẳn nghĩa hoặc phá vỡ nhịp thở bài hát.

---

## 2. Bảng Nhận Diện & Xử Lý Dạng Đọc (Spoken Normalization Patterns)

| Đối tượng (Written) | Khả năng đọc sai (Engine Risk) | Dạng phát âm chuẩn (Spoken Target) | Khuyến nghị xử lý (Recommendation) |
|---|---|---|---|
| **Từ tiếng Anh thông dụng**<br>*(baby, love, say hi, bye, game...)* | Đọc ngọng ngữ điệu Việt, nuốt âm đuôi hoặc phát âm kiểu robot thô. | Giữ nguyên trọng âm gốc hoặc Việt hóa tự nhiên (`bây-bi`, `bai`). | Giữ nguyên written form; nếu Suno vấp, thêm phonetic cue trong style prompt hoặc chú thích riêng. |
| **Từ tiếng Anh đa âm tiết**<br>*(joker, running, memories...)* | Engine đọc thừa âm tiết, ngắt quãng nhịp điệu (*run-ning* thành 2 phách rời rạc). | Đếm đúng số slot nốt nhạc (`giốc-cơ` = 2 nốt; `mém-mờ-ri` = 3 nốt). | Cảnh báo `FOREIGN-PRONUNCIATION-RISK`. Khuyên tác giả kiểm tra số nốt giai điệu tương ứng. |
| **Mốc giờ & thời gian**<br>*(0h, 2h sáng, 12pm...)* | Đọc là "không hắt", "hai hắt", hoặc đọc tiếng Anh "zero hour". | `0h` $\rightarrow$ *"không giờ"*<br>`2h` $\rightarrow$ *"hai giờ sáng"* | Trong lyric viết: có thể để `0h` hoặc `không giờ`. Nếu hát Suno: khuyến nghị viết chữ *"không giờ"* để tránh lỗi đọc chữ cái. |
| **Chữ số & năm tháng**<br>*(2026, 100%, số 1...)* | Đọc rời rạc từng số: "hai không hai sáu" thay vì "hai nghìn không trăm...". | `2026` $\rightarrow$ *"hai nghìn không trăm hai mươi sáu"* (7 âm) hoặc *"hai không hai sáu"* (4 âm). | Cảnh báo `NUMBER-READING-RISK`: Số âm tiết chênh lệch lớn (4 âm vs 7 âm) sẽ phá vỡ giai điệu nếu engine chọn sai cách đọc. Viết rõ bằng chữ nếu cần cố định số âm tiết. |
| **Từ viết tắt & ký hiệu**<br>*(AI, FB, DM, VIP, cafe...)* | Đọc theo bảng chữ cái tiếng Việt "a-i", "ép-bê", hoặc bỏ qua ký hiệu. | `AI` $\rightarrow$ *"ây-ai"*<br>`VIP` $\rightarrow$ *"víp"*<br>`&` $\rightarrow$ *"và"*<br>`%` $\rightarrow$ *"phần trăm"* | Ký hiệu đặc biệt (`&`, `%`, `/`, `@`) **bắt buộc đổi thành chữ** (`và`, `phần trăm`, `trên`) trong lyric để đảm bảo singability. |
| **Tên riêng nước ngoài**<br>*(Paris, New York, Tokyo...)* | Lạc tông dấu thanh tiếng Việt. | `Pa-ri`, `Niu Oóc`. | Giữ tên chuẩn quốc tế trong lyric viết; ghi chú phonetic nếu engine phát âm sai. |

---

## 3. Khẩu Độ & Nhịp Thở Ca Từ (Vietnamese Prosody & Singability)

### Quy tắc cơ bản:
- **Tiếng Việt là ngôn ngữ đơn lập có thanh điệu (Tonal Language):** Mỗi âm tiết mang một dấu thanh (ngang, huyền, sắc, hỏi, ngã, nặng) gắn liền với độ cao tự nhiên của giọng nói.
- **Không áp đặt luật số âm tiết cố định (No Hard Syllable Meter):** Không ép mọi dòng phải đúng 7 hoặc 8 chữ. Thay vào đó, kiểm tra **khẩu độ miệng (mouth-feel)** và **nhịp thở tự nhiên (breath phrasing)**.

### Thẩm định prosody theo điều kiện dữ liệu:

```text
KHI CHƯA CÓ AUDIO (Lyrics-Only):
→ Chỉ cảnh báo nguy cơ khả dĩ (POTENTIAL PROSODY RISK).
→ Tuyệt đối KHÔNG tuyên bố câu hát chắc chắn mượt hay chắc chắn cấn.

KHI ĐÃ CÓ AUDIO / RENDER:
→ Đối chiếu chính xác: vocal timing, điểm lấy hơi, dấu thanh bị bẻ cong, từ bị nuốt.
```

---

## 4. Danh Mục Các Lăng Kính Chẩn Đoán Prosody (Prosody Risk Lenses)

Các mã chẩn đoán dưới đây là **cảnh báo tham vấn (Advisory)**; không block ngòi bút của Writer:

### 1. `MOUTHFUL-LINE` (Câu dồn chữ / Nghẽn khẩu hình)
- **Triệu chứng:** Một dòng chứa quá nhiều âm tiết phụ âm tắc/khép (`t, p, c, k, ch`) hoặc quá nhiều từ ghép liền nhau trong một tiết tấu nhanh, khiến người hát không kịp nhả chữ hoặc ca sĩ ảo bị líu lưỡi.
- **Dấu hiệu:** Đọc to câu văn với tốc độ bình thường mà cảm giác phải gồng cơ miệng hoặc hụt hơi trước khi đến từ cuối.
- **Cách xử lý:** Cắt bỏ các từ hư từ, từ nối thừa (`thực sự là`, `cho nên rằng`, `bởi vì thế mà`); tạo khoảng trống cho nguyên âm vang.

### 2. `FORCED-PUNCTUATION` / `AWKWARD-BREATH` (Ngắt nhịp xé nghĩa)
- **Triệu chứng:** Dòng ngắt hoặc điểm lấy hơi rơi vào giữa một từ ghép đẳng lập/chính phụ hoặc cụm từ cố định làm đứt gãy ý nghĩa.
  - *Ví dụ cấn:* `"Anh ngồi nhìn chiếc lá rụng rơi bên hiên / nhà vắng tanh"` $\rightarrow$ ngắt đôi cụm *"hiên nhà"*.
- **Cách xử lý:** Điều chỉnh vị trí ngắt dòng sao cho điểm lấy hơi trùng với ranh giới ngữ nghĩa tự nhiên của cụm từ.

### 3. `STRESS-MISMATCH` / `STRESS-RISK` (Cấn dấu thanh & Trọng âm giai điệu)
- **Triệu chứng:** Âm tiết mang thanh điệu trầm hoặc khép (dấu nặng `.`, huyền `\`) lại bị rơi vào nốt nhạc cao nhất của câu, hoặc âm mang thanh cao (sắc `/`, ngã `~`) bị ấn vào nốt trầm sâu nhất, tạo ra hiện tượng hát nghe như đổi dấu (ví dụ: *"hạnh phúc"* nghe thành *"hành phục"*).
- **Lưu ý:** Khi chưa có melody cố định, chỉ flag những trường hợp thanh điệu va đập quá gắt trong cụm từ liên tiếp.

### 4. `FOREIGN-PRONUNCIATION-RISK` (Rủi ro phát âm từ ngoại lai)
- **Triệu chứng:** Dùng từ tiếng Anh có phụ âm cuối phức tạp hoặc âm tiết không tồn tại trong ngữ âm tiếng Việt mà không có giải pháp giai điệu nâng đỡ.
- **Cách xử lý:** Đánh giá xem từ đó có phải là bản sắc không thể thay thế của câu hát không. Nếu có: giữ nguyên và chú thích cách ngắt nhịp; nếu là từ sáo rỗng: thay bằng từ tiếng Việt có sức nặng tương đương.

### 5. `NUMBER-READING-RISK` (Rủi ro đọc chữ số đa nghĩa)
- **Triệu chứng:** Xuất hiện số hoặc mốc năm trong câu ca từ mà cách đọc có thể dao động từ 1 đến 5 âm tiết.
- **Cách xử lý:** Khuyến nghị tác giả ghi rõ dạng chữ nếu nhịp điệu của đoạn nhạc đòi hỏi số lượng âm tiết tuyệt đối chính xác.

---

## 5. Quy Trình Chú Thích Phát Âm (Phonetic Annotation Workflow)

Khi chuẩn bị handoff cho Suno hoặc ca sĩ phòng thu:

1. **Bản Lyric Chính (Display Lyric):**  
   Giữ nguyên ngôn ngữ tự nhiên và thẩm mỹ chữ viết của tác giả:
   ```text
   [Chorus]
   Cuộc gọi lúc 0h chỉ để nghe em thở dài
   Trong trò chơi này, anh đâu phải một joker
   Chỉ muốn yêu em đến tận năm 2026 và mãi sau.
   ```

2. **Bản Chú Thích Hát / Engine Guidance (Chỉ khi cần hỗ trợ render):**
   ```text
   [Suno/Vocal Guidance Note]
   - "0h": phát âm là "không giờ" (2 âm tiết).
   - "joker": phát âm là "dô-cơ" hoặc "giốc-cơ" (2 âm tiết, nhịp đều).
   - "2026": khuyến nghị hát "hai nghìn không trăm hai sáu" hoặc "hai không hai sáu" tùy theo khuôn nhịp giai điệu.
   ```

3. **Bất biến tối cao:** Không bao giờ biến bản hiển thị chính thức thành một văn bản thô ráp đầy ký hiệu phiên âm làm mất đi vẻ đẹp thơ mộng của ca từ.
