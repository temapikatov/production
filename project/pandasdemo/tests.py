from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APITestCase
# from htmltext import find_text, format_html, gettext


# Create your tests here.
class ViewsTestCase(TestCase):
    def test_index_loads_properly_1(self):
        response = self.client.get('lolo')
        self.assertEqual(response.status_code, 404)

    def test_index_loads_properly_2(self):
        url1 = reverse('home')
        response = self.client.get(url1)
        self.assertEqual(response.status_code, 200)

 # error content
    def test_index_loads_properly_3(self):
        url1 = reverse('home')
        response = self.client.get(url1)
        self.assertNotEqual(response.content, '<!DOCTYPE html>\n<html lang="en">\n<head>\n')

    def test_index_loads_properly_4(self):
        response = self.client.get('https:django/127')
        self.assertEqual(response.status_code, 404)
# error response
    def test_index_loads_properly_5(self):
        response = self.client.get('https:django/127')
        self.assertNotEqual(response, '<HttpResponseNotFound status_code=404, "text/html; charset=utf-8">')

class CharacterApiTest(APITestCase):
    def test_response_correct_1(self):
        url = reverse('main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_response_correct_2(self):
        url2 = reverse('main')
        response = self.client.get(url2)
        print(response.data)
        self.assertEqual(response.data, {'Unnamed: 0': {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6},
                                         'id': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7},
                                         'name': {0: 'aaaa', 1: 'ssssss', 2: 'ssassa', 3: 's', 4: '', 5: 'aaa', 6: ''},
                                         'gender': {0: '', 1: '', 2: '', 3: '', 4: '', 5: 'False', 6: 'True'},
                                         'percent': 50.0}
)
        # error id !=number
    def test_response_correct_3(self):
        url2 = reverse('main')
        response = self.client.get(url2)
        print(response.data)
        self.assertNotEqual(response.data, {"id":{"0":1,"1":2,"2":3,"3":4,"4":5,"5":6,"6":7},
                                         "name":{"0":"null","1":"null","2":"ssassa","3":"null","4":"null","5":"null","6":"null"},
                                         "gender":{"0":"null","1":"null","2":"null","3":"null","4":"null","5":"null","6":"null"},
                                         "percent":50.0})
        # error Wisdm
    def test_response_correct_4(self):
        url2 = reverse('main')
        response = self.client.get(url2)
        print(response.data)
        self.assertNotEqual(response.data, {"id":{"0":1,"1":2,"2":3,"3":4,"4":5,"5":6,"6":7},
                                         "name":{"0":"aaaa","1":"ssssss","2":"ssassa","3":"s","4":"a","5":"aaa","6":"a"},
                                         "gender":{"0":"true","1":"true","2":"true","3":"true","4":"true","5":"false","6":"true"},
                                         "percent":0.0})

# error zero
    def test_response_correct_5(self):
        url2 = reverse('main')
        response = self.client.get(url2)
        print(response.data)
        self.assertNotEqual(response.data, {"id":{"0":1,"1":2,"2":3,"3":4,"4":5,"5":6,"6":7},
                                         "name":{"0":"null","1":"null","2":"null","3":"null","4":"null","5":"null","6":"null"},
                                         "gender":{"0":"null","1":"null","2":"null","3":"null","4":"null","5":"null","6":"null"},
                                         "percent":100.0})