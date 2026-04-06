# Ngày 1 — Bài Tập & Phản Ánh
## Nền Tảng LLM API | Phiếu Thực Hành

**Thời lượng:** 1:30 giờ  
**Cấu trúc:** Lập trình cốt lõi (60 phút) → Bài tập mở rộng (30 phút)

---

## Phần 1 — Lập Trình Cốt Lõi (0:00–1:00)

Chạy các ví dụ trong Google Colab tại: https://colab.research.google.com/drive/172zCiXpLr1FEXMRCAbmZoqTrKiSkUERm?usp=sharing

Triển khai tất cả TODO trong `template.py`. Chạy `pytest tests/` để kiểm tra tiến độ.

**Điểm kiểm tra:** Sau khi hoàn thành 4 nhiệm vụ, chạy:
```bash
python template.py
```
Bạn sẽ thấy output so sánh phản hồi của GPT-4o và GPT-4o-mini.

---

## Phần 2 — Bài Tập Mở Rộng (1:00–1:30)

### Bài tập 2.1 — Độ Nhạy Của Temperature
Gọi `call_openai` với các giá trị temperature 0.0, 0.5, 1.0 và 1.5 sử dụng prompt **"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> Khi temperature tăng từ 0.0 lên 1.5, các phản hồi trở nên đa dạng và sáng tạo hơn nhưng cũng kém ổn định hơn. Ở mức 0.0, câu trả lời mang tính xác định và tập trung vào các sự thật phổ biến nhất; ở mức 1.5, nội dung bắt đầu trở nên lộn xộn và có thể xuất hiện các từ ngữ hoặc cấu trúc câu không tự nhiên.

**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Tôi sẽ đặt temperature ở mức thấp, từ 0.0 đến 0.2. Điều này đảm bảo chatbot đưa ra các phản hồi chính xác, nhất quán và đáng tin cậy, tránh việc "sáng tạo" quá mức dẫn đến cung cấp thông tin sai lệch cho khách hàng.

---

### Bài tập 2.2 — Đánh Đổi Chi Phí
Xem xét kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người thực hiện 3 lần gọi API, mỗi lần trung bình ~350 token.

**Ước tính xem GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này:**
> GPT-4o đắt hơn GPT-4o-mini khoảng 16.7 lần (dựa trên đơn giá $0.010 so với $0.0006 cho mỗi 1K output tokens).

**Mô tả một trường hợp mà chi phí cao hơn của GPT-4o là xứng đáng, và một trường hợp GPT-4o-mini là lựa chọn tốt hơn:**
> GPT-4o xứng đáng khi cần xử lý các tác vụ phức tạp đòi hỏi khả năng suy luận logic cao hoặc phân tích dữ liệu chuyên sâu. GPT-4o-mini là lựa chọn tốt hơn cho các tác vụ đơn giản như phân loại ý định người dùng (intent classification) hoặc tóm tắt các đoạn văn bản ngắn với khối lượng yêu cầu lớn.

---

### Bài tập 2.3 — Trải Nghiệm Người Dùng với Streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi khi nào thì non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming quan trọng nhất trong các ứng dụng chatbot hội thoại trực tiếp vì nó giúp giảm "độ trễ cảm nhận" (perceived latency), tạo cảm giác phản hồi tức thì cho người dùng. Ngược lại, non-streaming phù hợp hơn cho các tác vụ xử lý dữ liệu ngầm (background processing), hoặc khi cần kết quả ở dạng cấu trúc (như JSON) để thực hiện các bước xử lý logic tiếp theo trước khi hiển thị cho người dùng.


## Danh Sách Kiểm Tra Nộp Bài
- [x] Tất cả tests pass: `pytest tests/ -v`
- [x] `call_openai` đã triển khai và kiểm thử
- [x] `call_openai_mini` đã triển khai và kiểm thử
- [x] `compare_models` đã triển khai và kiểm thử
- [x] `streaming_chatbot` đã triển khai và kiểm thử
- [x] `retry_with_backoff` đã triển khai và kiểm thử
- [x] `batch_compare` đã triển khai và kiểm thử
- [x] `format_comparison_table` đã triển khai và kiểm thử
- [x] `exercises.md` đã điền đầy đủ
- [x] Sao chép bài làm vào folder `solution` và đặt tên theo quy định 
