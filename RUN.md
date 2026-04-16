---
install: pip install -r requirements.txt
start: python -m uvicorn app:app --host 0.0.0.0 --port 4706
port: 4706
---
