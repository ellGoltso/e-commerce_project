from src.Product import Product


class Category:
    name: str
    description: str
    __products: list[Product]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        count: int = 0
        for product in self.__products:
            count += product.quantity
        return f"{self.name}, количество продуктов: {count} шт."

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        str_products: str = ""
        for product in self.__products:
            str_products += str(product)

        return str_products
