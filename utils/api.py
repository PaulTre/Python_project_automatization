
from utils.http_method import Http_methods

"""Методы для тестирования API Google maps"""

base_url = "https://rahulshettyacademy.com"           #Базовая url которые мы используем везде
key = "key=qaclick123"                               #Параметр который мы используем во всех методах

class Google_maps_api():

    """Метод для создания новой локации"""

    @staticmethod
    def create_new_place():

        json_body_for_new_location = {
                "location": {
                    "lat": -38.383494,
                    "lng": 33.427362
                }, "accuracy": 50,
                "name": "Frontline house",
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": [
                    "shoe park",
                    "shop"
                ],
                "website": "http://google.com",
                "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json"           #Resource для метода POST
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = Http_methods.post(post_url, json_body_for_new_location)
        print(result_post.text)
        return result_post

    """Метод для проверки новой локации"""

    @staticmethod
    def get_new_place(place_id):

        get_resource = "/maps/api/place/get/json" #ресурс метода GET
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get