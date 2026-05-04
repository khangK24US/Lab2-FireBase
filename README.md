# Lab2-FireBase
# Chatbot Page Assignment

Dự án mẫu cho bài lab gồm 2 phần:

- `frontend/`: Streamlit giao diện đăng nhập, chat và gọi backend.
- `backend/`: FastAPI backend xử lý xác thực Firebase, Google login và lưu chat vào Firestore.
- `.streamlit/secrets.toml`: chứa cấu hình Firebase và Google login.
- `requirements.txt`: thư viện cần cài.

## Hướng dẫn cài đặt environment

1. Cài Python (phiên bản 3.11 hoặc 3.12 được khuyến nghị).
2. Tạo và kích hoạt virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Cài các gói cần thiết:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Tạo file cấu hình secrets:

- Tạo file `.streamlit/secrets.toml`.
- Điền cấu hình `firebase_client`, `firebase_admin` và `google-login`.

## Hướng dẫn chạy backend

1. Kích hoạt virtual environment nếu chưa kích hoạt:

```bash
source .venv/bin/activate
```

2. Chạy backend FastAPI:

```bash
uvicorn backend.app.main:app --reload --port 8000
```

3. Kiểm tra backend hoạt động bằng cách truy cập:

```bash
http://localhost:8000/health
```

## Hướng dẫn chạy frontend

1. Kích hoạt virtual environment nếu chưa kích hoạt:

```bash
source .venv/bin/activate
```

2. Chạy Streamlit frontend:

```bash
streamlit run frontend/app.py
```

3. Mở trình duyệt và truy cập:

```bash
http://localhost:8501
```

## Lưu ý

- Không đẩy file `.streamlit/secrets.toml` lên GitHub.
- Nếu không cần Google login, vẫn có thể dùng Email/Password.
- Backend dùng Firebase Auth và Firestore để lưu lịch sử cuộc hội thoại.

https://github.com/user-attachments/assets/fd948b18-ce9e-4450-a6ec-e7b7c786c1e4
