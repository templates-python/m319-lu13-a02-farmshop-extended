from dataclasses import dataclass


@dataclass
class Article:
    """
    an article in the farmshop
    """
    name: str
    price: float
    stock: int

    @property
    def article_value(self):
        return self.price * self.stock

if __name__ == '__main__':
    pass
