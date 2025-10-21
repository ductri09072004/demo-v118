# Demo API - Python FastAPI

Đây là một API nhỏ được xây dựng bằng Python FastAPI để cung cấp data giả cho testing và demo.

## Tính năng

- **Users API**: Quản lý thông tin người dùng
- **Products API**: Quản lý sản phẩm
- **Posts API**: Quản lý bài viết
- **Random Data**: Lấy dữ liệu ngẫu nhiên
- **Health Check**: Kiểm tra trạng thái API

## Cài đặt

1. **Cài đặt dependencies:**
```bash
pip install -r requirements.txt
```

2. **Chạy API:**
```bash
python main.py
```

Hoặc sử dụng uvicorn trực tiếp:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

### Root
- `GET /` - Thông tin API và danh sách endpoints

### Users
- `GET /users` - Lấy danh sách tất cả users
- `GET /users/{user_id}` - Lấy thông tin user theo ID
- `GET /random-user` - Lấy một user ngẫu nhiên

### Products
- `GET /products` - Lấy danh sách tất cả products
- `GET /products/{product_id}` - Lấy thông tin product theo ID
- `GET /products/category/{category}` - Lấy products theo category
- `GET /random-product` - Lấy một product ngẫu nhiên

### Posts
- `GET /posts` - Lấy danh sách tất cả posts
- `GET /posts/{post_id}` - Lấy thông tin post theo ID
- `GET /posts/author/{author}` - Lấy posts theo tác giả

### Health Check
- `GET /health` - Kiểm tra trạng thái API

## Sử dụng

Sau khi chạy API, bạn có thể truy cập:

- **API Documentation**: http://localhost:8000/docs (Swagger UI)
- **ReDoc**: http://localhost:8000/redoc
- **API Root**: http://localhost:8000/

## Ví dụ sử dụng

```bash
# Lấy tất cả users
curl http://localhost:8000/users

# Lấy user theo ID
curl http://localhost:8000/users/1

# Lấy user ngẫu nhiên
curl http://localhost:8000/random-user

# Lấy products theo category
curl http://localhost:8000/products/category/Điện thoại

# Kiểm tra health
curl http://localhost:8000/health
```

## Cấu trúc dự án

```
demo-base-4/
├── main.py              # File chính chứa FastAPI app
├── requirements.txt     # Dependencies
└── README.md           # Hướng dẫn sử dụng
```

## Mở rộng

Bạn có thể dễ dàng mở rộng API bằng cách:
- Thêm endpoints mới
- Thêm models mới
- Kết nối database thật
- Thêm authentication
- Thêm validation
