#!/bin/bash

# Script برای راه‌اندازی PostgreSQL برای پروژه ToDoList Django

echo "🚀 شروع راه‌اندازی PostgreSQL..."

# بررسی وجود Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker نصب نشده است. لطفاً ابتدا Docker را نصب کنید."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose نصب نشده است. لطفاً ابتدا Docker Compose را نصب کنید."
    exit 1
fi

# ایجاد فایل .env اگر وجود نداشته باشد
if [ ! -f .env ]; then
    echo "📝 ایجاد فایل .env..."
    cat > .env << EOF
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
EOF
    echo "✅ فایل .env ایجاد شد"
else
    echo "ℹ️  فایل .env قبلاً موجود است"
fi

# نصب dependencies
echo "📦 نصب Python dependencies..."
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
    echo "✅ Virtual environment فعال شد"
else
    echo "⚠️  Virtual environment یافت نشد. در حال نصب در محیط فعلی..."
fi

pip install -r requirements.txt

# راه‌اندازی PostgreSQL با Docker
echo "🐘 راه‌اندازی PostgreSQL با Docker..."
docker-compose up -d postgres

# انتظار برای آماده شدن PostgreSQL
echo "⏳ انتظار برای آماده شدن PostgreSQL..."
sleep 10

# بررسی وضعیت PostgreSQL
if docker-compose ps postgres | grep -q "Up"; then
    echo "✅ PostgreSQL با موفقیت راه‌اندازی شد"
else
    echo "❌ خطا در راه‌اندازی PostgreSQL"
    docker-compose logs postgres
    exit 1
fi

# اجرای migrations
echo "🔄 اجرای Django migrations..."
python manage.py makemigrations
python manage.py migrate

echo ""
echo "🎉 راه‌اندازی کامل شد!"
echo ""
echo "📋 دستورات مفید:"
echo "   • اجرای سرور: python manage.py runserver"
echo "   • ایجاد superuser: python manage.py createsuperuser"
echo "   • توقف PostgreSQL: docker-compose down"
echo "   • مشاهده logs: docker-compose logs postgres"
echo ""
echo "🌐 پس از اجرای سرور، برنامه در آدرس http://127.0.0.1:8000 در دسترس خواهد بود" 