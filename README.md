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
1. Chạy ingestion lưu data từ file json vào MySQL:
- Chạy lệnh: `uuvicorn mysql_api.sql_api:app --host 0.0.0.0 --port 8000`
- Chạy lệnh: `python ingestion/ingest.py`
- Thêm data vào `data_crawl/data.json`
2. Chạy API search, filter sản phẩm:
- Chạy lệnh: `uuvicorn mysql_api.sql_api:app --host 0.0.0.0 --port 8000`
- Vào địa chỉ: `http://127.0.0.1:8000/docs`
