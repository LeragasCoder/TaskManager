# راه‌اندازی PostgreSQL برای پروژه ToDoList

## مرحله 1: ایجاد فایل .env

یک فایل با نام `.env` در ریشه پروژه بسازید و محتوای زیر را در آن قرار دهید:

```
# Database Configuration
DB_ENGINE=django.db.backends.postgresql
DB_NAME=todolist_db
DB_USER=todolist_user
DB_PASSWORD=todolist_password
DB_HOST=localhost
DB_PORT=5432

# Django Settings
DEBUG=True
SECRET_KEY=django-insecure-2lxo&-t)+n85y(#c(^6iho^pj_p91a6a+-t@in#f%p%vzvi6_=
```

## مرحله 2: نصب dependencies

```bash
pip install -r requirements.txt
```

## مرحله 3: راه‌اندازی PostgreSQL با Docker

### شروع PostgreSQL:
```bash
docker-compose up -d postgres
```

### بررسی وضعیت:
```bash
docker-compose ps
```

### مشاهده logs:
```bash
docker-compose logs postgres
```

## مرحله 4: اجرای migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## مرحله 5: ایجاد superuser (اختیاری)

```bash
python manage.py createsuperuser
```

## مرحله 6: اجرای سرور

```bash
python manage.py runserver
```

## دستورات مفید Docker

### توقف PostgreSQL:
```bash
docker-compose down
```

### توقف و حذف volumes:
```bash
docker-compose down -v
```

### اتصال مستقیم به PostgreSQL:
```bash
docker exec -it todolist_postgres psql -U todolist_user -d todolist_db
```

### Backup دیتابیس:
```bash
docker exec -t todolist_postgres pg_dump -U todolist_user todolist_db > backup.sql
```

### Restore دیتابیس:
```bash
docker exec -i todolist_postgres psql -U todolist_user -d todolist_db < backup.sql
```

## تنظیمات Production

برای محیط production:

1. فایل `.env.production` بسازید
2. `DEBUG=False` قرار دهید  
3. `SECRET_KEY` جدید تولید کنید
4. `ALLOWED_HOSTS` را تنظیم کنید
5. از PostgreSQL خارجی استفاده کنید (نه Docker)

## عیب‌یابی

### خطای اتصال به دیتابیس:
- مطمئن شوید Docker در حال اجرا است
- پورت 5432 آزاد باشد
- تنظیمات .env صحیح باشد

### خطای permission:
```bash
sudo chown -R $USER:$USER .
```

### پاک کردن کامل Docker volumes:
```bash
docker-compose down -v
docker volume prune
``` 