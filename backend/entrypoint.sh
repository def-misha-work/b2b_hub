#!/bin/sh

if [ "$DATABASE" = "b2b_test_hub_db" ]
then
    echo "Waiting for postgres..."

    while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
      sleep 0.1
    done
fi
    echo "PostgreSQL started"

if alembic current; then
    # Если изменения обнаружены, то выполняем миграцию и обновляем базу данных
    alembic revision --autogenerate -m "New migration"
    alembic upgrade head
else
    # Если изменений нет, выводим сообщение об этом
    echo "No changes to the database, skipping migration"
fi

# shellcheck disable=SC1083
#uvicorn project.web.main:web --reload --host=0.0.0.0 --port="$PORT 8000"

# alembic revision --autogenerate -m "Initianal migration"
# alembic upgrade head

uvicorn main:app --reload --host=0.0.0.0 --port=8000

exec "$@"