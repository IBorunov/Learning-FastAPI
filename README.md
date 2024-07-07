# Pet-проект для изучения возможностей FastAPI
## FastAPI-сервер со следующей логикой:

* Роут, который принимает схему schemas.Schema
* Указанный роут получает input_start равный "2023-12-20T22:39:40.000"
* Фильтруем записи в БД: получаем все записи из endpoint_state где state_start >= input_start и endpoint_id = 139
* Отсортировываем данные по state_start desc.
* Из полученнных данных ищем все записи, где id строки кратен числу 3
* В ответ роут в формате json возвращает: “filtered_count” – количество полученных записей, "client_info" – поле info из связанной модели clients_info у третьей записи из полученного списка, "state_id" - state_id у третьей записи.

<p align="center">
<img src=https://github.com/IBorunov/Learning-FastAPI/blob/main/%D0%A0%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%20(%D0%9A%D0%BE%D0%BD%D1%81%D0%BE%D0%BB%D1%8C).png>
</p>
<p align="center"><i>Результат в консоли </i></p>


<p align="center">
<img src=https://github.com/IBorunov/Learning-FastAPI/blob/main/%D0%A0%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%20%D0%B2%20Postman.png>
</p>
<p align="center"><i>Результат в Postman </i></p>
