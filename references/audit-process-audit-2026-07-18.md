# Audit quy trình audit/fix skill — 2026-07-18

## Câu hỏi audit

Apparatus cũ có đủ để kết luận một thay đổi làm `songwriting-min` tốt hơn và tổng quát hơn, hay mới chỉ giúp sửa ca vừa thấy?

## Nguồn chính thức dùng đối chiếu

1. [OpenAI — Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices): eval-driven development; task-specific/real-distribution tests; log và continuous evaluation; tránh vibe-based eval; dùng held-out data, edge/adversarial cases, pairwise/pass-fail và hiệu chỉnh judge với người.
2. [OpenAI — Working with evals](https://developers.openai.com/api/docs/guides/evals): eval có schema dữ liệu và grader rõ để chạy so sánh các version/model/parameter.
3. [Anthropic — Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents): tách capability khỏi regression; task/trial/grader/trace/outcome; nhiều trial vì nondeterminism; cân bằng positive/negative; môi trường sạch; deterministic + model + human graders; đọc trace để kiểm grader và dùng production incidents làm test.
4. Hướng dẫn `skill-creator` cục bộ: forward-test ở fresh context, chỉ truyền raw artifact/task-local context; không truyền suspected bug, intended fix, expected answer hoặc prior conclusion.

Các nguyên tắc trên được ánh xạ sang songwriting như eval một hệ thống sinh mở. Chúng không phải lý thuyết về cái đẹp và không thay tai người.

## Gap matrix trước khi sửa

| Thành phần | Trạng thái cũ | Rủi ro |
|---|---|---|
| Mục tiêu eval | Có brief/cùng material | Chưa freeze artifact, success criteria và version trước khi xem output |
| Dataset | Corpus + case-log + “nhiều ca” | Trộn incident, recent-memory và validation; dễ học thuộc ca vừa sửa |
| Holdout | Chỉ nói arm độc lập | Không có sealed set; chẩn đoán có thể rò vào generation |
| Capability/regression | Baseline non-regression chung | Chưa tách bài khó để leo năng lực khỏi bài ổn định để chống backslide |
| Negative cases | Có false positive note | Chưa bắt buộc ca rule phải bắn và ca không được bắn; dễ overtrigger |
| Nondeterminism | Một forward-test/case phổ biến | Một bản thắng có thể chỉ là variance |
| Graders | Người chọn + vài hard gate | Chưa có grader stack, `UNKNOWN`, calibration hoặc position-bias control |
| Artifact scope | Có lyric/card/demo/render | Stage loop cũ vẫn dùng B2–B6, thiếu Goal/Entry/Music/Performance |
| Trace | Fingerprint cuối | Chưa phân biệt outcome grading với trace diagnosis và grader bug |
| Promotion/revert | Validated/Provisional/Quarantined | Chưa có candidate, release gate, contamination status và điều kiện revert |
| Metric | Verdict 1–5; ngưỡng theo khoảng 10 ca | Điểm tổng dễ che hard fail; ngưỡng nhỏ giả chính xác |

## Quy trình sau sửa

1. **Freeze objective/baseline:** version, lane, artifact, hard invariants và câu hỏi so sánh.
2. **Triage incident:** raw artifact → symptom → earliest stage; case này vào development/capability, không vào holdout.
3. **Build balanced suite:** capability, regression, sealed holdout; cả trigger và non-trigger; phủ input route và artifact type theo pairwise coverage thay vì mọi tổ hợp.
4. **Run isolated trials:** fresh context, production-like skill, chỉ runner brief; đóng corpus và hidden rubric. Generative reliability dùng nhiều trial.
5. **Grade layered:** deterministic hard gates → rubric một trục → blind pairwise → human/audio. Model judge có `UNKNOWN`, đảo thứ tự và calibration.
6. **Inspect failures:** chấm outcome trước rồi mới đọc trace; phân biệt skill fail, route fail, model/audio variance, case ambiguity và grader bug.
7. **Patch lowest sufficient layer:** route/clarification trước blanket rule; một change hypothesis mỗi A/B.
8. **Release gate:** candidate thắng capability, pass sealed holdout, không hard-regress, scope rõ; claim âm nhạc phải có artifact nghe được.
9. **Monitor/revert:** production/user failure nhập incident queue; hard regression mới hoặc thắng chỉ khi leaked context thì thu hẹp/revert.

## Coverage tối thiểu cho songwriting-min

Không chạy full Cartesian. Chọn case để mỗi cặp quan trọng xuất hiện ít nhất một lần:

- Entry: title/lyric · melody · groove/track · chord/harmony · brief/story · draft-revision.
- Goal/lane: mainstream rõ nghĩa · ambition/high-ceiling · mood-wash · narrative · declaration · groove-led.
- Register/genre: Vpop trẻ · indie · bolero/tự sự · quê-folk · quê-anthemic; lane mới chỉ thêm khi có nhu cầu thật.
- Artifact: Tứ/scaffold · lyric sheet · rough demo · Suno render · audit-only.
- Failure family: trope/skeleton convergence · unearned payoff · referent/collocation · rhyme-led material · body/prop provenance · conceit literalization · prosody · hook recall · overclaim Suno control.

## Registry tối thiểu

Mỗi trial lưu:

`case_id · split(capability/regression/holdout) · brief_version · skill_version · model/harness · artifact · trial_id · contamination(clean/suspect) · deterministic_result · rubric_axes · pairwise_result · human_audio_verdict · earliest_failure_stage · notes`

Không lưu hidden expected answer cạnh runner brief nếu cùng agent có thể đọc cả hai. Holdout phải có người/evaluator riêng giữ rubric; generation arm chỉ nhận task.

## Những thay đổi đã thực hiện

- Viết lại `audit-and-evaluation.md` thành release protocol thay vì ghi chú A/B ngắn.
- Cập nhật `stage-validation-loop.md` từ B2–B6 sang tám tầng runtime và thêm artifact/music/performance gates.
- Tách case-log khỏi eval suite; thêm capability/regression/sealed holdout và contamination status.
- Thêm grader stack, multi-trial, balanced trigger/non-trigger, grader-bug path và revert condition.
- Giữ audit references ngoài runtime để không tăng cognitive load lúc viết bài.

## Tier bằng chứng

- Cấu trúc eval/release: **VALIDATED AS PROCESS PRIOR** qua hướng dẫn chính thức OpenAI, Anthropic và skill-creator.
- Cách ánh xạ cụ thể sang đánh giá songwriting: **PROVISIONAL**, cần chạy suite thật và hiệu chỉnh bằng verdict người nghe/audio.
- Không có eval protocol nào biến chất lượng nghệ thuật thành khách quan tuyệt đối hoặc bảo đảm hit.
