# custom-fk

Написан кастомный ForeignKey, который обеспечивает интерфейс взаимодействия между моделями Product и UniqueProduct.
Интерфейс имеет два метода:
1. All - получение всех объектов UniqueProduct для конкретного объекта Product.
```
product_object.uniq.all()
```

2. Generate - генерация уникального продукта (UniqueProduct) объекта Product.
```
product_object.uniq.generate()
```

### Запуск тестов:
```
cd ./products
python manage.py test
```

### Запуск cервера:
```
cd ./products
python manage.py migrate 
python manage.py runserver
```