from django.test import TestCase, Client
import json
from .models import dish,orders

class DishAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_add_dish(self):
        response = self.client.post(
            "/adddish/",
            json.dumps({"name": "New Dish", "price": "10.99", "availability": True}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(dish.objects.count(), 1)

    def test_updatedish(self):
        test_dish = dish.objects.create(name="Test Dish", price="15.99", availability=True)
        response = self.client.put(
            f"/updatedish/{test_dish.id}/",
            json.dumps({"availability": False}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        test_dish.refresh_from_db()
        self.assertFalse(test_dish.availability)

    def test_Get_data(self):
        response = self.client.get("/getdish/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)

    def test_Delete_data(self):
        test_dish = dish.objects.create(name="Delete Me", price="5.99", availability=True)
        response = self.client.delete(f"/deletedish/{test_dish.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(dish.objects.count(), 0)

    def test_add_order(self):
        response = self.client.post(
            "/addorder/",
            {"name": "Customer", "dish": "Dish Name", "status": "Pending"},
            content_type="application/x-www-form-urlencoded",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(orders.objects.count(), 1)

    def test_update_order(self):
        test_order = orders.objects.create(
            CostumerName="Customer", dish="Dish Name", status="Pending"
        )
        response = self.client.put(
            f"/updateorder/{test_order.id}/",
            {"status": "Completed"},
            content_type="application/x-www-form-urlencoded",
        )
        self.assertEqual(response.status_code, 200)
        test_order.refresh_from_db()
        self.assertEqual(test_order.status, "Completed")

    def test_fetch_orders(self):
        response = self.client.get("/fetchorder/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
