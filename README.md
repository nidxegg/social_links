# social_links
#запуск позитивных тестов
pytest -v --tb=line -m positive ваш каталог копирования\social_links\  
#запуск негативных тестов
pytest -v --tb=line -m negative ваш каталог копирования\social_links\  
#запуск параллельных тестов
pytest  -v --tb=line ваш каталог копирования\social_links\ -n 3
