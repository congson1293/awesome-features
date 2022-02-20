# Demo FastAPI

## Requirements
```
pip install -r requirements.txt
```

## Steps to create API
chỉ cần 6 bước để tạo 1 API

Bước 1: import fastapi
Bước 2: tạo 1 instance của class FastAPI
Bước 3: tạo đường dẫn, bắt đầu từ /
Bước 4: khai báo phương thức HTTP: post, get, put, delete hay options, head, patch, trace
Bước 5: khai báo hàm
Bước 6: trả về content với format dict, list, str, int, ...

## Run
```
uvicorn main:app --host 0.0.0.0 --port 8000
```

Or in dev
```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
## References
```
https://viblo.asia/p/huong-dan-co-ban-framework-fastapi-tu-a-z-phan-1-V3m5W0oyKO7#_cai-dat-2
```