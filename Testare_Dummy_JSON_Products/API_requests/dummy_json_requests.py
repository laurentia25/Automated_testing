import requests


class DummyJsonRequests:
    _BASE_URL = "https://dummyjson.com/products"

    def get_all_products(self, select=None):
        url = self._BASE_URL
        criteria = {}
        if select is not None:
            criteria.update({"select": select})
        resp = requests.get(url=url, params=criteria)
        return resp

    def get_a_single_product(self, prod_id):
        url = f'{self._BASE_URL}/{prod_id}'
        resp = requests.get(url=url)
        return resp

    def search_products(self, keyword=None):
        url = f'{self._BASE_URL}/search'
        criteria = {}
        if keyword is not None:
            criteria.update({"q": keyword})
        resp = requests.get(url=url, params=criteria)
        return resp

    def limit_skip_products(self, limit=None, skip=None):
        url = self._BASE_URL
        request_params = {}
        if limit is not None:
            request_params.update({"limit": limit})
        if skip is not None:
            request_params.update({"skip": skip})
        resp = requests.get(url=url, params=request_params)
        return resp

    def get_all_products_categories(self):
        url = f'{self._BASE_URL}/categories'
        resp = requests.get(url=url)
        return resp

    def get_products_of_category(self, category):
        url = f'{self._BASE_URL}/categories/{category}'
        resp = requests.get(url=url)
        return resp

    def add_product(self, title=None, stock=None, price=None):
        url = f'{self._BASE_URL}/add'
        product_details = {}
        if title is not None:
            product_details.update({"title": title})
        if stock is not None:
            product_details.update({"stock": stock})
        if price is not None:
            product_details.update({"price": price})
        resp = requests.post(url=url, json=product_details)
        return resp

    def update_product(self, product_id, title=None, price=None, stock=None, rating=None):
        url = f'{self._BASE_URL}/{product_id}'
        updated_details = {}
        if title is not None:
            updated_details.update({"title": title})
        if price is not None:
            updated_details.update({"price": price})
        if stock is not None:
            updated_details.update({"stock": stock})
        if rating is not None:
            updated_details.update({"rating":rating})
        resp = requests.patch(url=url, json=updated_details)
        return resp

    def delete_product(self, product_id):
        url = f'{self._BASE_URL}/{product_id}'
        resp = requests.delete(url=url)
        return resp

