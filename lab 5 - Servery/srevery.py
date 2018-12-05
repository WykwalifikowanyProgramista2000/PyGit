from abc import ABC, abstractmethod
from typing import List, Dict
import re

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
    def get_list_from_server(self):
        pass


    def find_products(self, letters_in_product_ID: int) -> List[Product]:
        product_list = self.get_list_from_server()
        products_with_n_letter_id = []
        for single_product in self.product_list:
            r = re.compile('([a-zA-Z]+)([0-9]+)')
            splitted_id = r.match(single_product.product_id)
            if(len(splitted_id.group(1)) == letters_in_product_ID and 1 < len(splitted_id.group(2)) < 4):
                products_with_n_letter_id.append(single_product)
        return products_with_n_letter_id


class ListServer(Server):

    product_list: List[Product]

    def __init__(self, list_of_products: List[Product]) -> None:
        self.product_list = []
        for single_product in list_of_products:
            self.product_list.append(single_product)
        super().__init__()


    def get_list_from_server(self):
        return self.product_list


    def find_products(self, letters_in_product_ID: int) -> List[Product]:
        products_with_n_letter_id = []
        for single_product in self.product_list:
            r = re.compile('([a-zA-Z]+)([0-9]+)')
            splitted_id = r.match(single_product.product_id)
            if(len(splitted_id.group(1)) == letters_in_product_ID):
                products_with_n_letter_id.append(single_product)
        return products_with_n_letter_id




class DictServer(Server):

    product_dict: Dict[str, float]

    def __init__(self, list_of_products: List[Product]) -> None:
        self.product_dict = {}
        for single_product in list_of_products:
            self.product_dict += {single_product.product_id: single_product.product_price}
        super().__init__()


    def find_products(self, letters_in_product_ID: int) -> List[List[str, float]]:


