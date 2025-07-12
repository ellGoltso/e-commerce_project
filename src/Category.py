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


    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1


    @property
    def products(self):
        str_products: str = ''
        for product in self.__products:
            str_products += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'

        return str_products
