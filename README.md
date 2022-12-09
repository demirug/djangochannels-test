Django channels test project

---
Setup .env file
```
SECRET_KEY=your secret key
DEBUG=1
ALLOWED_HOSTS=*
REDIS_HOST=127.0.0.1
REDIS_PORT=6379
```

To start test_channel handler use `manage.py runworker test_channel`