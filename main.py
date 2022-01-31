from fastapi import FastAPI
import uvicorn
import requests
app = FastAPI()
data = []

# Читаем данные из файла и формируем список словарей (каждый словарь - 1 город)
with open('RU.txt', encoding='utf-8') as file:
    for i in file:
        temp = i.split('\t')
        data.append(
            {'geonameid': temp[0], 'name': temp[1], 'asciiname': temp[2], 'alternatenames': temp[3],
             'latitude': temp[4],
             'longitude': temp[5], 'feature class': temp[6], 'feature code': temp[7], 'country code': temp[8],
             'cc2': temp[9],
             'admin1 code': temp[10], 'admin2 code': temp[11], 'admin3 code': temp[12], 'admin4 code': temp[13],
             'population': temp[14],
             'elevation': temp[15], 'dem': temp[16], 'timezone': temp[17], 'modification date': temp[18]}
        )


# Метод принимает идентификатор geonameid и возвращает информацию о городе
@app.get("/city/{geonameid}")
def root(geonameid: int):
    response = {'status': 404, 'message': 'not found'}
    for i in data:
        if int(i['geonameid']) == geonameid:
            response = i
            break
    return response


# Метод принимает страницу и количество отображаемых на странице городов и возвращает список городов с их информацией
@app.get("/page/{geo_page}/countPerPage/{geo_count}")
def root(geo_page: int,geo_count: int):
    response = {'status': 404, 'message': 'not found'}
    if geo_count < 1: return  "incorrect data"
    if (geo_page < 1 or geo_page > int(len(data) / geo_count)):
        return "incorrect data"
    response = []
    for i in range(geo_page * geo_count - 1, geo_page * geo_count + (geo_count) - 1):
        response.append(data[i])
    return response


# Метод принимает названия двух городов (на русском языке) и получает информацию о найденных городах,
# а также дополнительно: какой из них расположен севернее и одинаковая ли у них временная зона
# (когда несколько городов имеют одно и то же название, разрешать неоднозначность выбирая город с большим населением; если население совпадает, брать первый попавшийся)
@app.get("/city/{firstCity}/{secondCity}")
def root(firstCity: str, secondCity: str):
    response = {'status': 404, 'message': 'not found'}
    firstCity_ = False
    secondCity_ = False
    for i in data:
        if i['alternatenames'].find(firstCity) != -1:
            if firstCity_:
                if firstCity_['population'] < i['population']: firstCity_ = i
            else: firstCity_ = i
        elif i['alternatenames'].find(secondCity) != -1:
            if secondCity_:
                if secondCity_['population'] < i['population']: secondCity_ = i
            else: secondCity_ = i

    if firstCity_ or secondCity_:
        north = 0
        equel_time_zone = False
        if firstCity_['timezone'] == secondCity_['timezone']: equel_time_zone = True
        if firstCity_['latitude'] > secondCity_['latitude']:
            north = firstCity_['name']
        else: north = secondCity_['name']
        response = {firstCity : firstCity_, secondCity : secondCity_, 'north': north, 'Equal time zone':equel_time_zone}
    return response


# Метод ищет вхождения заданной строки в названиях городов и возвращает список совпадений
@app.get("/search/{string}")
def root(string: str):
    response = {'status': 404, 'message': 'not found'}
    temp = []
    for i in data:
        if i['alternatenames'].find(string) != -1:
            temp.append(i['alternatenames'])
    if len(temp) > 0: response = temp
    return set(response)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
