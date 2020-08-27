# social_links
Демонстрация работы https://www.youtube.com/watch?v=Ulr2EC4z69g
#запуск виртуального окружения python3
d:\Python\social_links\env\Scripts\activate
#запуск позитивных тестов
pytest -v --tb=line -m positive ваш каталог копирования\social_links\  
#запуск негативных тестов
pytest -v --tb=line -m negative ваш каталог копирования\social_links\  
#запуск параллельных тестов
pytest  -v --tb=line ваш каталог копирования\social_links\ -n 3
