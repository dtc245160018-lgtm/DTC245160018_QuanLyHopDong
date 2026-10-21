# ĐỀ TÀI 34: HỆ THỐNG QUẢN LÝ HỢP ĐỒNG
**Môn:** Triển khai và Quản trị Hệ thống Phần mềm  
**Mã số Sinh viên:** DTC245160018 
**Họ và tên:** Nguyễn Tuấn Anh 

---

## 📌 Giới thiệu Hệ thống
Hệ thống Quản lý Hợp đồng được triển khai dạng Containerization sử dụng Docker và Docker Compose, bao gồm các thành phần chính:
- **Web Application:** Website Quản lý Hợp đồng sử dụng **Python (Django)**
- **Database:** PostgreSQL & pgAdmin
- **Web Server / Reverse Proxy:** Nginx (HTTPS tự ký + Security Headers)
- **Monitoring:** Prometheus + Grafana + cAdvisor
- **Logging:** Loki + Promtail (Truy vấn LogQL)

---

## 🚀 Hướng dẫn Chạy Hệ thống

### 1. Yêu cầu môi trường
- Docker & Docker Compose v2.x trở lên
- Git

### 2. Các bước khởi chạy
```bash
# Clone repository
git clone [https://github.com/dtc245160018-lctm/DTC245160018_QuanLyHopDong.git](https://github.com/dtc245160018-lctm/DTC245160018_QuanLyHopDong.git)

# Di chuyển vào thư mục dự án
cd DTC245160018_QuanLyHopDong

# Khởi chạy toàn bộ hệ thống bằng Docker Compose
docker compose up -d
