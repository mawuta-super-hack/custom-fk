from django.test import TestCase

from .models import Attr, Product, ProductAttr, UniqueProduct


class CustomFKTestCase(TestCase):
    """Тестирование новых методов all() и generate()"""

    def setUp(self) -> None:
        self.attr1 = Attr.objects.create(name='Attr1')
        self.attr2 = Attr.objects.create(name='Attr2')
        self.product = Product.objects.create(name='Product1')
        self.product_attr1 = ProductAttr.objects.create(product=self.product,
                                                        attr=self.attr1,
                                                        value='Value1')
        self.product_attr2 = ProductAttr.objects.create(product=self.product,
                                                        attr=self.attr2,
                                                        value='Value2')

    def test_custom_fk_generate(self):

        unique_product = self.product.uniq.generate()

        self.assertIsNotNone(unique_product)
        self.assertIsInstance(unique_product, UniqueProduct)
        self.assertEqual(unique_product.product.id, self.product.id)

    def test_custom_fk_all(self):

        self.product.uniq.generate()
        self.product.uniq.generate()

        unique_products = self.product.uniq.all()

        self.assertIsNotNone(unique_products)
        self.assertEqual(len(unique_products), 2)
