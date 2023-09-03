import unittest

from API_requests.simple_books_requests import SimpleBooksRequests


class TestGetOrders(unittest.TestCase):
    """
    Testam ruta GET /orders
    """

    def setUp(self) -> None:
        self.request_handler = SimpleBooksRequests()

    def test_get_all_orders(self):
        """
        Verificam:
        - status code este 200
        - ca obtinem in response orderId plasat
        """
        place_order = self.request_handler.submit_order(1, 'Laurentia')
        order_id = place_order.json()['orderId']
        response = self.request_handler.get_all_orders()
        expected_status_code = 200
        expected_order_id = order_id
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_order_id, response.json()[0]['id'])


