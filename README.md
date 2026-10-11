# Những mảnh suy nghĩ — Streamlit

Một trang nhật ký tương tác: người đọc nhấn nút để mở từng câu ngắn theo từng giai đoạn.

## Chạy trên máy tính

1. Cài Python 3.10 trở lên.
2. Giải nén thư mục dự án.
3. Mở Terminal / CMD trong thư mục dự án và chạy:

```bash
pip install -r requirements.txt
streamlit run app.py
```

4. Trình duyệt sẽ mở trang web cục bộ.

## Sửa nội dung câu chuyện

Mở `timeline_data.json` bằng VS Code hoặc Notepad.
- `title`: tiêu đề trang.
- `subtitle`: lời mở đầu.
- `chapters`: các giai đoạn.
- `fragments`: từng câu sẽ hiện ra khi nhấn nút.

Bạn nên sửa từng câu để phản ánh chính xác trải nghiệm của mình. Nội dung mẫu chỉ là khung khởi đầu; hãy bỏ mọi câu không đúng với sự thật của bạn.

## Đẩy lên GitHub

Tạo một repository mới trên GitHub, rồi tải các tệp trong thư mục này lên repository. Nếu dùng Git trên máy:

```bash
git init
git add .
git commit -m "Tạo trang nhật ký tương tác"
git branch -M main
git remote add origin https://github.com/TEN-TAI-KHOAN/TEN-REPO.git
git push -u origin main
```

Thay `TEN-TAI-KHOAN` và `TEN-REPO` bằng thông tin repository của bạn.

## Triển khai lên Streamlit Community Cloud

1. Đẩy dự án lên GitHub.
2. Đăng nhập Streamlit Community Cloud bằng tài khoản GitHub.
3. Chọn **Create app**, chọn repository, branch `main`, và file chính `app.py`.
4. Nhấn **Deploy**.

## Lưu ý riêng tư

Nếu định gửi trang này cho một người cụ thể, hãy cân nhắc nội dung nào bạn thật sự muốn chia sẻ. Đừng đưa thông tin riêng tư của người khác lên trang công khai nếu chưa có sự đồng ý. Có thể đặt repository ở chế độ private khi viết và chỉnh sửa; khi triển khai, hãy kiểm tra cài đặt quyền truy cập của ứng dụng.
