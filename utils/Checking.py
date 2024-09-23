"""Методы для проверки ответов запросов"""
import json

from requests import Response


class Checking():

    """Метод для проверки статус кодов всех методов"""
    @staticmethod
    def check_status_code(response: Response, expected_status_code):
        # Проверка на ожидаемый статус код
        assert expected_status_code == response.status_code
        print("Ожидаемый статус код " + str(expected_status_code), "получен " + str(response.status_code))

        """Словарь кодов ошибок"""
        status_messages = {
            200: "Тест пройден! Статус код = 200 (OK)",
            201: "Тест пройден! Статус код = 201 (Created)",
            204: "Тест пройден! Статус код = 204 (No Content)",
            400: "Тест не пройден! Статус код = 400 (Bad Request)",
            401: "Тест не пройден! Статус код = 401 (Unauthorized)",
            403: "Тест не пройден! Статус код = 403 (Forbidden)",
            404: "Тест не пройден! Статус код = 404 (Not Found)",
            500: "Тест не пройден! Статус код = 500 (Internal Server Error)"
        }

        # Получение сообщения для текущего статус-кода
        message = status_messages.get(response.status_code, "Статус код не распознан: " + str(response.status_code))
        print(message)

    """Метод проверки наличия обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)      #функция json.loads() преобразует строку в формат json для работы с ней. Response.text - ответ в формате text. В дсон нам надо перевести е едля работы с полями ответа
        assert  list(token) == expected_value  # ожидаем что в списке(list) ответов из переменной token мы получим все параметры и будем сравниванть с теми параметрами что пришли нам в ответе по факту
        print("Все поля есть!")

    """Метод проверки значения обязательных полей в ответе запроса"""

    @staticmethod
    def check_response_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " верно!")

    """Метод проверки  обязательных полей в ответе запроса по заданному слову"""
    def check_response_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
           print("Слово " + search_word + " присутствует!")
        else:
            print("Слово " +  search_word + " не найдено!")