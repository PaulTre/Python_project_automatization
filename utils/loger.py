import datetime
import os

from requests import Response


class Logger():
    file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log" # Создаем переменную, в которую заложили логику сохранения файла. logs/log_ название файла, будет храниться в папке логс, называться с названия log_. str(datetime...) Используем библиотеку, указываем что используем текущее время, указываем формат даты и время и указываем расширение файла

    @classmethod  #C помощью данного метода мы будем открывать файл и записывать в него данные
    def writer_log_file(cls, data: str):  # Записывание логов в файл, т.к classmethod(Для того чтобы обращаться к переменным нашего класса) cls - класс, data(данные) будут в формате строчном.
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file: # with open - Открываем файл, cls.file_name - обращаемся к переменой класса, 'a', 'encoding' - указываем кодировку файла.
            logger_file.write(data) #Просим записывать данные в этот файл

    @classmethod #С помощью этого метода мы получаем данные по Request
    def add_request(cls, url: str, method: str, data : str = None): # методы - cls. Туда будем помещать url в формате строки и название метода в формате строки
        test_name = os.environ.get('PYTEST_CURRENT_TEST') # в эту переменную будем помещать название теста который сейчас выполняется

        data_to_add = f"\n-----\n" # Строка необходима для того чтобы разделять логи. \n - обозначает что будет перенос с одной строки на другую
        data_to_add += f"Test:  {test_name}\n" # Помещаем название теста
        data_to_add += f"Test:  {str(datetime.datetime.now())}\n" # Помещаем время
        data_to_add += f"Request method:  {method}\n" # Помещаем запроса
        data_to_add += f"Request URL:  {url}\n" # Помещаем урлу
        data_to_add += "\n" # Чистая строка

        if data: # Проверяем, есть ли тело запроса
            data_to_add += f"Request Body:  {data}\n" # Записываем тело запроса
        else:
            data_to_add += f"Request Body:  None\n" # Если тела нет, указываем None

        cls.writer_log_file(data_to_add) #Для записи всех данных выше, обращаемся к классу, к методу и помещаем в него название переменной

    @classmethod # Метод который помещает в себя ответ
    def add_response(cls, result: Response): #Делаем функцию, метод тот же, но добавляем в него ответ библиотеки Requests
        cookies_as_dict = dict(result.cookies) #Обращаемся к кукам. Это нужно для того чтобы поместит в файл наши куки
        headers_as_dict = dict(result.headers) #Помещаем заголовки запроса

        data_to_add = f"Response code:  {result.status_code}\n" #Убираем плюс т.к это наша строка. Тут нужно просто обьявить переменную
        data_to_add += f"Response text:  {result.text}\n" #Добавляем текстовый ответ
        data_to_add += f"Response headers: {headers_as_dict}\n" #Добавляем хедеры
        data_to_add += f"Response cookies: {cookies_as_dict}\n" #Добавляем куки
        data_to_add = f"\n-----\n" # Разделение результатов строк

        cls.writer_log_file(data_to_add) #Записываем полученные данные в файл


