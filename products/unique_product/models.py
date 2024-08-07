from functools import cached_property

from django.db import models
from django.db.models.fields.related_descriptors import (
    ReverseManyToOneDescriptor, create_reverse_many_to_one_manager)


class ProductManager(models.Manager):

    def all(self):
        return super().all()

    def generate(self):
        import random

        prodatr = ProductAttr.objects.filter(
            product=self.instance.id).values_list('id', flat=True)
        attr = random.choice(prodatr)

        uniq = UniqueProduct.objects.create(
            product=self.instance,
            attr=ProductAttr.objects.get(id=attr)
        )
        return uniq


class NewReverseManyToOneDescriptor(ReverseManyToOneDescriptor):

    @cached_property
    def related_manager_cls(self):
        related_model = self.rel.related_model
        setattr(
            self.rel.related_model._meta, 'default_manager', ProductManager()
        )
        return create_reverse_many_to_one_manager(
            related_model._default_manager.__class__,
            self.rel,
        )


class CustomForeignKey(models.ForeignKey):
    related_accessor_class = NewReverseManyToOneDescriptor


class Attr(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductAttr(models.Model):
    attr = models.ForeignKey("Attr", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    value = models.CharField(max_length=100, default=0)


class Product(models.Model):
    name = models.CharField(max_length=100)
    attrs = models.ManyToManyField("Attr", through="ProductAttr")

    def __str__(self):
        return self.name


class UniqueProduct(models.Model):
    product = CustomForeignKey(
        Product, on_delete=models.PROTECT, related_name='uniq')
    attr = models.ForeignKey(ProductAttr, on_delete=models.PROTECT)
