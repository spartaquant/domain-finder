---
port: 4706
---

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY --from=clone /src/ .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 4706
CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "4706"]
```
