import unittest

from API_requests.simple_books_requests import SimpleBooksRequests


class TestUpdateOrder(unittest.TestCase):
    """
    Testam ruta UPDATE /orders/{order_id}
    """
    def setUp(self) -> None:
        self.request_handler = SimpleBooksRequests()

    def test_update_order_that_exists_in_db(self):
        """
        Verificam:
        - status code este 204
        - customer_name dupa update este cel asteptat
        """
        self.request_handler.submit_order(book_id=1, customer_name='Laurentia')
        all_orders = self.request_handler.get_all_orders()
        order_id = all_orders.json()[0]['id']
        customer_name = 'Alexandru'
        response = self.request_handler.update_order(order_id=order_id, customer_name=customer_name)
        expected_status_code = 204
        expected_customer_name = customer_name
        actual_customer_name = self.request_handler.get_order_by_id(order_id=order_id)
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_customer_name, actual_customer_name.json()['customerName'])

    def test_update_order_that_not_exists_in_db(self):
        """
        Verificam:
        - status code este 404
        - mesajul de eroare este cel asteptat
        """
        order_id = 'aaaaaaaaaaaaaaa'
        response = self.request_handler.update_order(order_id=order_id, customer_name='Laurentia')
        expected_status_code = 404
        expected_error_msg = f'No order with id {order_id}.'
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_error_msg, response.json()['error'])