from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import random
from datetime import datetime

app = FastAPI(title="Demo API", description="API nhỏ để get data giả", version="1.0.0")

# Models
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int
    city: str

class Product(BaseModel):
    id: int
    name: str
    price: float
    category: str
    in_stock: bool

class Post(BaseModel):
    id: int
    title: str
    content: str
    author: str
    created_at: str
    likes: int

# Fake data
fake_users = [
    User(id=1, name="Nguyễn Văn A", email="nguyenvana@email.com", age=25, city="Hà Nội"),
    User(id=2, name="Trần Thị B", email="tranthib@email.com", age=30, city="TP.HCM"),
    User(id=3, name="Lê Văn C", email="levanc@email.com", age=28, city="Đà Nẵng"),
    User(id=4, name="Phạm Thị D", email="phamthid@email.com", age=35, city="Cần Thơ"),
    User(id=5, name="Hoàng Văn E", email="hoangvane@email.com", age=22, city="Hải Phòng"),
]

fake_products = [
    Product(id=1, name="iPhone 15", price=25000000, category="Điện thoại", in_stock=True),
    Product(id=2, name="MacBook Pro", price=45000000, category="Laptop", in_stock=True),
    Product(id=3, name="Samsung Galaxy S24", price=22000000, category="Điện thoại", in_stock=False),
    Product(id=4, name="Dell XPS 13", price=35000000, category="Laptop", in_stock=True),
    Product(id=5, name="iPad Air", price=15000000, category="Tablet", in_stock=True),
]

fake_posts = [
    Post(id=1, title="Học Python cơ bản", content="Python là ngôn ngữ lập trình dễ học...", author="Nguyễn Văn A", created_at="2024-01-15", likes=25),
    Post(id=2, title="FastAPI Tutorial", content="FastAPI là framework hiện đại cho Python...", author="Trần Thị B", created_at="2024-01-16", likes=18),
    Post(id=3, title="Database Design", content="Thiết kế database là bước quan trọng...", author="Lê Văn C", created_at="2024-01-17", likes=32),
    Post(id=4, title="API Best Practices", content="Một số best practices khi thiết kế API...", author="Phạm Thị D", created_at="2024-01-18", likes=15),
    Post(id=5, title="Docker cho Developer", content="Docker giúp đóng gói ứng dụng...", author="Hoàng Văn E", created_at="2024-01-19", likes=28),
]

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Chào mừng đến với Demo API!",
        "version": "1.0.0",
        "endpoints": {
            "users": "/users",
            "products": "/products", 
            "posts": "/posts",
            "random_user": "/random-user",
            "random_product": "/random-product"
        }
    }

# Users endpoints
@app.get("/users", response_model=List[User])
async def get_users():
    """Lấy danh sách tất cả users"""
    return fake_users

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    """Lấy thông tin user theo ID"""
    user = next((user for user in fake_users if user.id == user_id), None)
    if not user:
        return {"error": "User không tồn tại"}
    return user

@app.get("/random-user", response_model=User)
async def get_random_user():
    """Lấy một user ngẫu nhiên"""
    return random.choice(fake_users)

# Products endpoints
@app.get("/products", response_model=List[Product])
async def get_products():
    """Lấy danh sách tất cả products"""
    return fake_products

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """Lấy thông tin product theo ID"""
    product = next((product for product in fake_products if product.id == product_id), None)
    if not product:
        return {"error": "Product không tồn tại"}
    return product

@app.get("/products/category/{category}")
async def get_products_by_category(category: str):
    """Lấy products theo category"""
    filtered_products = [p for p in fake_products if p.category.lower() == category.lower()]
    return filtered_products

@app.get("/random-product", response_model=Product)
async def get_random_product():
    """Lấy một product ngẫu nhiên"""
    return random.choice(fake_products)

# Posts endpoints
@app.get("/posts", response_model=List[Post])
async def get_posts():
    """Lấy danh sách tất cả posts"""
    return fake_posts

@app.get("/posts/{post_id}", response_model=Post)
async def get_post(post_id: int):
    """Lấy thông tin post theo ID"""
    post = next((post for post in fake_posts if post.id == post_id), None)
    if not post:
        return {"error": "Post không tồn tại"}
    return post

@app.get("/posts/author/{author}")
async def get_posts_by_author(author: str):
    """Lấy posts theo tác giả"""
    filtered_posts = [p for p in fake_posts if author.lower() in p.author.lower()]
    return filtered_posts

# Health check
@app.get("/health")
async def health_check():
    """Kiểm tra trạng thái API"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "message": "API đang hoạt động bình thường"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7000)
