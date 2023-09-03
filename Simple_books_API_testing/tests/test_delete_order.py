import unittest

from API_requests.simple_books_requests import SimpleBooksRequests


class TestDeleteOrder(unittest.TestCase):
    """
    Testam ruta DELETE /orders/{order_id}

    """
    def setUp(self) -> None:
        self.request_handler = SimpleBooksRequests()

    def test_delete_an_existing_order(self):
        """
        Verificam:
        - status code este 204
        - order_id nu se mai gaseste in baza de date
        """
        # Creez o comanda
        submit_order = self.request_handler.submit_order(book_id=1, customer_name='Laurentia')
        order_id = submit_order.json()['orderId']
        response = self.request_handler.delete_order(order_id=order_id)
        orders_list = self.request_handler.get_all_orders()
        expected_status_code = 204
        expected_list_length = 0
        actual_list_length = len(orders_list.json())
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_list_length, actual_list_length)

    def test_delete_an_order_that_not_exist(self):
        """
        Verificam:
        - status code este 404
        - mesajul de eroare este cel asteptat
        """
        order_id = 'sssssssssssss'
        response = self.request_handler.delete_order(order_id=order_id)
        expected_status_code = 404
        expected_error_msg = f'No order with id {order_id}.'
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_error_msg, response.json()['error'])
