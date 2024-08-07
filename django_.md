
```python
class Attr(models.Model):  
    name = models.CharField(max_length=50)  
  
    def __str__(self):  
        return self.name  
  
  
class ProductAttr(models.Model):  
    attr = models.ForeignKey("Attr", on_delete=models.CASCADE)  
    product = models.ForeignKey("Product", on_delete=models.CASCADE)  
    value = models.CharField(max_length=100)  
  
  
class Product(models.Model):  
    name = models.CharField(max_length=100)  
    attrs = models.ManyToManyField("Attr", through="ProductAttr")  
  
    def __str__(self):  
        return self.name

class UniqueProduct(models.Model):
	product = models.CustomForeignKey(Product, on_delete=models.PROTECT) 
	attr = models.ForeignKey(ProductAttr, on_delete=models.PROTECT)
```

Продукт имеет уникальные продукты. Уникальные продукты создаются на основе атрибутов продукта.
Задача: 
Написать кастомный ForeignKey, который обеспечивает интерфейс взаимодействия Product instance с UniqueProduct instances (по сути создаёт дополнительную абстракцию для reverse_many_to_one_manager).
Интерфейс должен иметь 2 метода: all, generate.
Метод all проксирует метод all ReverseManyToOne менеджера.
Метод generate создаёт UniqueProduct для данного Product instance (правила генерации не имеют значения).
Подсказка: Обратите внимание на атрибут related_accessor_class класса ForeignKey или его bases.