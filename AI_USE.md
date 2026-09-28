# AI_USE.md

AI tool(s) used: Claude, via the web interface.

## Log

| Field | Required entry |
|---|---|
| Week / Date | W05 / 2026-09-23 |
| Learning question | Bài tập lớn này yêu cầu làm những gì? |
| Pre-AI evidence | N/A — reading comprehension of the brief, not a Depth A item |
| Prompt purpose | Summarise the 15-section specification |
| Hint received | A structured summary: four parallel work streams (code, experiments, weekly posts, written-exam drills), two-state commit rule, Part I/Part II split |
| Verified against | Re-read §1, §4, §8, §10, §11 of the specification directly |
| What changed | Understood the deliverable structure before planning |
| Reconstructed without AI | Yes — I can now state the four work streams and the grading criteria from memory |

| Field | Required entry |
|---|---|
| Week / Date | W05 / 2026-09-26 |
| Learning question | Lập lịch thực hiện Part I trong 18 ngày |
| Pre-AI evidence | N/A — work organisation |
| Prompt purpose | Draft a schedule with per-task deadlines |
| Hint received | A 7-phase plan, ~42 hours, target submission 13/10 instead of the 14/10 deadline |
| Verified against | Checked the workload against §8, §10 and my own timetable |
| What changed | Adopted the schedule; added a reduced-scope fallback in case of load from other courses |
| Reconstructed without AI | Yes |

| Field | Required entry |
|---|---|
| Week / Date | W05 / 2026-09-27 |
| Learning question | Các lệnh Git và venv để dựng repo trên Windows |
| Pre-AI evidence | N/A — environment setup |
| Prompt purpose | Fix paste errors in directory creation; set up a virtual environment on PowerShell |
| Hint received | Diagnosis: line-continuation backslashes had split directory names; advice to create the venv inside the repository root |
| Verified against | Ran `find`, `git status` and `python -c "import sys; print(sys.prefix)"` to confirm each fix myself |
| What changed | Repaired the directory structure; moved `.venv` inside the repository |
| Reconstructed without AI | Yes — I can rebuild the structure from scratch |

| Field | Required entry |
|---|---|
| Week / Date | W05 / 2026-09-27 |
| Learning question | Trong phần về các độ đo phân lớp, tôi định nghĩa FP là "a bounding box NO matching ground-truth object exists in that location", và FN là "miss or fail to generate a valid bounding box although the real object exists, and this FN is infinite.". Đừng cho tôi định nghĩa đúng. Hãy hỏi tôi một câu duy nhất giúp tôi tự nhận ra định nghĩa này có phù hợp với bài toán tôi đang làm hay không. Chờ tôi trả lời rồi mới hỏi tiếp. |
| Pre-AI evidence | a4710ec |
| Prompt purpose | Socratic question |
| Hint received | The questions and examples that help me to understand definitions and can distinguish from TP, FP, TN and FN |
| Verified against | ML-Introduction.pdf, page 33-34 |
| What changed | Rewrite the definition of FP and FN, add examples to understand TP and TN |
| Reconstructed without AI | Yes |

| Field | Required entry |
|---|---|
| Week / Date | W05 / 2026-09-27 |
| Learning question | Ngưỡng tau trong pre-pruning được xác định dựa trên cái gì? |
| Pre-AI evidence | a4710ec |
| Prompt purpose | Socratic question |
| Hint received | The way to evaluate the model and the set to decide which 'tau' should be used. |
| Verified against | N/A - The slides does not supply the way to determine this 'tau' threshold |
| What changed | Update the knowledge at the pre-pruning part of C4.5 Algorithm. |
| Reconstructed without AI | Yes |