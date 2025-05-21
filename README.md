# CD_NNLT_CK
Bài tập lớn cuối kỳ môn CD_NNLT (data crawling, search thông tin từ website có sẵn). Sử dụng Python FastAPi, MySQL và Docker.
## Run local:
- Connection trong `mysql_api/database.py`:
    ```python
    MYSQL_USER = os.getenv("MYSQL_USER", "root") #username
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "") #password
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost") #host
    MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "glasses_db")
- Tạo database `glasses_db` trong MySQL (dùng file `init.sql`)
1. Chạy Data crawling để lấy dữ liệu từ web https://www.glasses.com/ vào file json:
- Chạy lệnh: `uvicorn crawl_data.crawl_api:app --host 0.0.0.0 --port 8001`
- Vào địa chỉ: http://127.0.0.1:8001/docs
- Chạy API 'GET /crawl' để crawl dữ liệu về
2. Chạy ingestion lưu data từ file json vào MySQL:
- Chạy lệnh: `uvicorn mysql_api.sql_api:app --host 0.0.0.0 --port 8000`
- Chạy lệnh: `python ingestion/ingest.py` để lưu dữ liệu vào MySQL
3. Chạy API search, filter sản phẩm:
- Chạy lệnh: `uvicorn mysql_api.sql_api:app --host 0.0.0.0 --port 8000`
- Vào địa chỉ: http://127.0.0.1:8000/docs
## Run docker:
- Chạy lệnh: `docker compose up --build`
- API data crawling: http://127.0.0.1:9001/docs
- API db: http://127.0.0.1:9000/docs
- UI: http://localhost:9080/filter.html
## 📁 Project Structure

```
DataCrawlProject/
├── app_main/
│   ├── front_end/
│   │   ├── ...
│   │   ├── about_us.html
│   │   ├── filter.html
│   │   └── index.html
│   └── Dockerfile
├── crawl_data/
│   ├── config.json
│   ├── crawl_api.py
│   ├── crawl.py
│   └── Dockerfile
├── data_crawl/
│   └── data.json
├── ingestion/
│   ├── ingest.py
│   └── Dockerfile
├── mysql_api/
│   ├── data_access.py
│   ├── database.py
│   ├── models.py
│   ├── schema.py
│   ├── sql_api.py
│   └── Dockerfile
├── mysql_db/
│   ├── init_db/
│   │   └── init.sql
│   ├── mysql_data/
│   │   └── ...
│   └── Dockerfile
├── docker-compose.yml
└── requirements.txt
```
