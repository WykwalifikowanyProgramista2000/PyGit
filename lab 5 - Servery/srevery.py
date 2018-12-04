from abc import ABC, abstractmethod
from typing import List, Dict


class Product:

    product_id: str
    product_price: float

    def __init__(self, product_id: str, product_price: float) -> None:
        self.product_id = product_id
        self.product_price = product_price


class Server(ABC):

    limit_of_found_products = 3

    def __init__(self) -> None:
        super().__init__()
        pass


    @abstractmethod
    def find_products(self, letters_in_product_ID: int):
        pass


class ListServer(Server):

    product_list: List[List[str, float]]

    def __init__(self, list_of_products: List[Product]) -> None:
        self.product_list = []
        for single_product in list_of_products:
            self.product_list.append([single_product.product_id, single_product.product_price])
        super().__init__()


    def find_products(self, letters_in_product_ID: int) -> List[List[str, float]]:
        for single_product in self.product_list:



class DictServer(Server):

    product_dict: Dict[str, float]

    def __init__(self, list_of_products: List[Product]) -> None:
        self.product_dict = {}
        for single_product in list_of_products:
            self.product_dict += {single_product.product_id: single_product.product_price}
        super().__init__()


    def find_products(self, letters_in_product_ID: int) -> List[List[str, float]]:


