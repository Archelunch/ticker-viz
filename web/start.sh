#!/bin/sh

echo "Waiting for postgres..."

echo $POSTG_H $POSTG_P
while ! nc -z $POSTG_H $POSTG_P; do
    sleep 0.1
done

echo "PostgreSQL started"

cp -R ../db ./

exec "$@"