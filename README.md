# python_infotecs

# requirments.txt - файл с зависимостями

# Метод findCityById
``` Метод принимает 1 аргумент - geonameid обьекта , если обьект не найдет , тогда возвращяется соотвествующее сообщение.```

# Метод Search
``` Метод принимает 1 аргумент - string типа str , после ищет входения данной подстроки в alternatenames всех записей , в случае совпадения выдаёт массив названий обьектов.```

# Метод getСitiesByNames
``` Метод принимает 2 аргумента - firstCity(название 1-го обьекта на русском языке) и secondCity(название 2-го обьекта на русском языке) , после ищет входения данных подстрок в alternatenames всех записей , в случае совпадения выдаёт массив найденных обьектов. В случаи соответсвия нескольких обьектов входящему названию ,выбирается обьект с большем населением . Дополнительно вычесляються 2 дополнительный параметра:  ***
*Какой обьект севернее.  
*Совпадает ли временная зона у обьектов.```
