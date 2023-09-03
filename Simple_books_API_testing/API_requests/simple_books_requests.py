import requests
import random


class SimpleBooksRequests:
    _BASE_URL = "https://simple-books-api.glitch.me"

    def __init__(self):
        self.token = self._generate_token()

    def _generate_token(self):
        url = f'{self._BASE_URL}/api-clients'
        random_nr = random.randint(1, 99999999999999)
        body = {
            "clientName": "Laurentia",
            "clientEmail": f"laurentia034{random_nr}@gmail.com"
        }
        resp = requests.post(url=url, json=body)
        return resp.json()["accessToken"]

    def get_status(self):
        url = f'{self._BASE_URL}/status'
        response = requests.get(url=url)
        return response

    def get_all_books(self, limit=None, type=None):
        url = f'{self._BASE_URL}/books'
        request_params = {}
        if limit is not None:
            request_params.update({"limit": limit})
        if type is not None:
            request_params.update({"type": type})
        resp = requests.get(url=url, params=request_params)
        return resp

    def get_book_by_id(self, book_id):
        url = f'{self._BASE_URL}/books/{book_id}'
        resp = requests.get(url=url)
        return resp

    def submit_order(self, book_id, customer_name):
        url = f'{self._BASE_URL}/orders'
        request_body = {
            "bookId": book_id,
            "customerName": customer_name
        }
        resp = requests.post(url=url, json=request_body, headers={"Authorization": self.token})
        return resp

    def get_all_orders(self):
        url = f'{self._BASE_URL}/orders'
        resp = requests.get(url=url, headers={'Authorization': self.token})
        return resp

    def get_order_by_id(self, order_id):
        url = f'{self._BASE_URL}/orders/{order_id}'
        resp = requests.get(url=url, headers={'Authorization': self.token})
        return resp

    def update_order(self, order_id, customer_name):
        url = f'{self._BASE_URL}/orders/{order_id}'
        request_body = {
            "customerName": customer_name
            }
        resp = requests.patch(url=url, json=request_body, headers={'Authorization': self.token})
        return resp

    def delete_order(self, order_id):
        url = f'{self._BASE_URL}/orders/{order_id}'
        resp = requests.delete(url=url, headers={'Authorization': self.token})
        return resp


# first_object = SimpleBooksRequests()
# print(first_object.get_status())
# response = first_object.get_status()
# print(response.status_code)
# print(response.json())
#
# # get al books
# response2 = first_object.get_all_books()
# print(response2.status_code)
# print(response2.json())
#
# response3 = first_object.submit_order(3, "Laurentia")
# print(response3.json())
# print(response3.status_code)