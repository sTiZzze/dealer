import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import random


@pytest.mark.django_db
class TestCars(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_superuser(username='testuser', password='12345')

    def setUp(self):
        self.client.login(username='testuser', password='12345')

    @pytest.mark.usefixtures()
    def test_get_cars_list(self):
        """GET запрос к списку машин."""
        url = reverse('cars-list')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.usefixtures()
    def test_post_cars_list(self):
        """POST запрос к списку машин."""
        url = reverse('cars-list')
        vin_number = random.randint(1000000, 9999999)
        data = {'model': 'BMW', 'color': 'RED', 'price': 1000.00, 'engine_volume': 5,
                'is_from_the_factory': True, 'vin_number': 'JN8AZ2NE5C' + str(vin_number),
                'amount_of_owners': 2, 'year': 2001}
        response = self.client.post(url, data=data, status='json')
        assert response.status_code == status.HTTP_201_CREATED
