# Wojciech Dziuba 292639

from abc import ABC, abstractmethod
from typing import List, Dict
import re
import unittest


class Product:

    def __init__(self, product_id: str, product_price: float) -> None:
        self.product_id = product_id
        self.product_price = product_price


class Server(ABC):
    n_max_returned_entries = 3

    def __init__(self) -> None:
        super().__init__()
        pass


    @abstractmethod
    def get_list_from_server(self):
        pass


    def find_products(self, letters_in_product_id: int) -> List[Product]:
        product_list = self.get_list_from_server()
        products_with_n_letter_id = []
        for single_product in product_list:
            r = re.compile('([a-zA-Z]+)([0-9]+)')
            splitted_id = r.match(single_product.product_id)
            if(len(splitted_id.group(1)) == letters_in_product_id and 1 < len(splitted_id.group(2)) < 4):
                products_with_n_letter_id.append(single_product)
        if len(products_with_n_letter_id) > self.n_max_returned_entries:
            raise TooManyProductsFoundError
        return sorted(products_with_n_letter_id, key=lambda product: product.product_price)


class ListServer(Server):

    def __init__(self, list_of_products: List[Product]) -> None:
        super().__init__()
        self.product_list = list_of_products

    def get_list_from_server(self) -> List[Product]:
        return self.product_list


class DictServer(Server):

    def __init__(self, list_of_products: List[Product]) -> None:
        super().__init__()
        self.product_dict: Dict[str, Product] = {}
        for single_product in list_of_products:
            self.product_dict[single_product.product_id] = single_product


    def get_list_from_server(self) -> List[Product]:
        temp_list = []
        for value in self.product_dict.values():
            temp_list.append(value)
        return temp_list


class Client:

    def __init__(self, server: Server):
        self.current_server = server

    def sum_products_price(self, letters_in_product_id: int) -> float:
        summed_price = 0
        try:
            found_products = self.current_server.find_products(letters_in_product_id)
            for product in found_products:
                summed_price += product.product_price
            return summed_price
        except TooManyProductsFoundError:
            return 0


class TooManyProductsFoundError(Exception):

    def __init__(self, msg=None):
        if msg is None:
            msg = "Found products limit exceeded"
        super().__init__(msg)


test_product_list = [Product("bbbb111", 10),
                     Product("aaa11", 3),
                     Product("bbbb11", 20),
                     Product("aaa11", 2),
                     Product("aaa111", 1),
                     Product("ccc2222", 300),
                     Product("bbbb11", 30),
                     Product("bbbb11", 40)
                     ]
new_server = ListServer(test_product_list)
new_client = Client(new_server)


class TestServerMethods(unittest.TestCase):

    def test_list_sorting(self):
        self.assertEqual(new_server.find_products(3), [test_product_list[4], test_product_list[3], test_product_list[1]])

    def test_error_thrown(self):
        with self.assertRaises(TooManyProductsFoundError):
            new_server.find_products(4)

    def test_sum_prices_error(self):
        self.assertEqual(new_client.sum_products_price(4), 0)


if __name__ == '__main__':
    unittest.main()

# Wojciech Dziuba 292639
