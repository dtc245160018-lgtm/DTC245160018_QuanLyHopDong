# Đề 34: Hệ thống Quản lý Hợp đồng (Contract Management System)

## Thành phần hệ thống
- **Web App**: Flask / Python
- **Database**: PostgreSQL + pgAdmin
- **Reverse Proxy**: Nginx
- **Monitoring**: Prometheus + Grafana + cAdvisor
- **Logging**: Loki + Promtail

## Hướng dẫn triển khai hệ thống

1. **Khởi động toàn bộ dịch vụ:**
   ```bash
   docker compose up -d --build


---

### Phase 2: Thực hiện tạo 3 mốc Commit theo đúng yêu cầu đề bài

Đề bài yêu cầu có **ít nhất 03 commit có ý nghĩa** ứng với các giai đoạn triển khai[span_3](start_span)[span_3](end_span)[span_4](start_span)[span_4](end_span):

<Steps>
  <Step title="Mốc 1: Commit cho Nginx Reverse Proxy (Commit 1)">
    Gõ các lệnh sau trong Terminal WSL[span_5](start_span)[span_5](end_span):
    ```bash
    git add docker-compose.yml nginx/
    git commit -m "feat: setup Nginx reverse proxy for contract system (Commit 1)"
    ```
  </Step>

  <Step title="Mốc 2: Commit cho Prometheus + Grafana + cAdvisor (Commit 2)">
    Gõ các lệnh sau trong Terminal WSL[span_6](start_span)[span_6](end_span):
    ```bash
    git add prometheus/ grafana/ docker-compose.yml
    git commit -m "feat: integrate Prometheus and Grafana for metrics monitoring (Commit 2)"
    ```
  </Step>

  <Step title="Mốc 3: Commit cho Loki + Promtail + README (Commit 3)">
    Gõ các lệnh sau trong Terminal WSL[span_7](start_span)[span_7](end_span):
    ```bash
    git add loki/ promtail/ README.md docker-compose.yml
    git commit -m "feat: integrate Loki and Promtail for centralized logging (Commit 3)"
    ```
  </Step>
</Steps>

---

### Phase 3: Đẩy (Push) mã nguồn lên GitHub

1. **Tạo Repository mới trên GitHub:**
   - Đặt tên Repo theo đúng mã số sinh viên / tên đề tài theo quy định[span_8](start_span)[span_8](end_span) (Ví dụ: `Contract-Management-System-SystemAdmin`).
   - Để chế độ **Public**.

2. **Liên kết và Đẩy code lên GitHub:**
   Gõ các lệnh sau trong Terminal WSL (thay URL bằng link Repo của Tuấn):
   ```bash
   git branch -M main
   git remote add origin https://github.com/<tai-khoan-github-cua-tuan>/<ten-repo>.git
   git push -u origin main
