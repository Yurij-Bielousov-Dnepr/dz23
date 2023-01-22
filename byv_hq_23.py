# Написать приложение с двумя потоками
# Поток №1
# Отображается меню в консоли и ожидается ввод от пользователя. 
# После ввода отображается подменю или выводится информация из файла. 
# Для команд управления использовать Event для второго потока

# Меню:
# 1. Температура/Влажность
#     1.1 Текущая # последняя запись в файле
#     1.2 Средняя # среднее 6 последних записей
# 2. Счетчики
#     2.1 Электроенергия # показания счетчика, текущий расход
#     2.2 Газ # показания счетчика, текущий расход
#     2.3 Вода # показания счетчика, текущий расход
# 3. Котел
#     3.1 Состояние # Включен/Выключен, температура, давление
#     3.2 Включить # Команда на включение
#     3.3 Выключить # Команда на выключение
# 4. Журнал # все записи из файла

# Поток №2
# Каждые 5 секунд отправляются GET запросы на сервер (ссылка позже на GitHub) и принимается ответ 
# в видt JSON (формат в файле example.json).
# Полученные данные с добавленным дата/время сохраняются в файле (любой формат файла). 
# При возникновении Event отправляет запросы на сервер (ссылка позже на GitHub) 
import datetime
import  datatime, time
import threading, requests
import json, pickle

ev1 = threading.Event()

boiler_condition="ON"
obj=None
lock1 = threading.Lock()
def menu():
    answer=input('''       Меню:
1. Температура/Влажность
    1.1 Текущая 
    1.2 Средняя 
2. Счетчики
    2.1 Электроенергия # показания счетчика, текущий расход
    2.2 Газ # показания счетчика, текущий расход
    2.3 Вода # показания счетчика, текущий расход
3. Котел
    3.1 Состояние 
    3.2 Включить 
    3.3 Выключить 
4. Журнал  
Введите 1-4 для выбора или Q для выхода''')
    while answer=="q" or answer== "Q":
        match answer:
            case "1":
                print("""Вы находитесь в меню Температура, уточните свой выбор
                            1.1 Текущая 
                            1.2 Средняя """)
            case "1.1":
                lock1.acquire()
                 # последняя запись в файле
                # открыть файл, прочитать последнюю запись выделить параметр
                temp = data["temperature"]

                humidity = data["humidity"]

                print(f"Текущая температура: {temp} ℃, текущая влажность: {humidity}")
                lock1.release()
            case "1.2":
                ... # среднее 6 последних записей
                # открыть файл, прочитать 6 записей найти среднее параметра
                with open('condition.log', 'r') as file:
                    list_range=[]
                    for i in range(5):
                        file.readline()
                        # list_range.append() 
            case "2":
                print(""" Вы находитесь в меню Счетчики, уточните свой выбор
                            2.1 Электроенергия:  показания счетчика & текущий расход
                            2.2 Газ: показания счетчик & текущий расход
                            2.3 Вода: показания счетчика & текущий расход""")
            case "2.1":
                ... #Электроенергия показания счетчика, текущий расход
            # открыть файл, прочитать последнюю запись, выделить параметры
                lock1.acquire()
                electricity = reqwest()["meter"]["electricity"]["consumption"]
                print(f"споживання електроенергії: {electricity} Кв")
                lock1.release()
            case "2.2":
                ...# Газ показания счетчика, текущий расход
            # открыть файл, прочитать последнюю запись, выделить параметры
                lock1.acquire()
                gas = reqwest()["meter"]["gas"]["consumption"]
                print(f"споживання електроенергії: {gas} ㎥")
                lock1.release()
            case "2.3":
                ...#Вода показания счетчика, текущий расход
            # открыть файл, прочитать последнюю запись, выделить параметры
                lock1.acquire()
                water = reqwest()["meter"]["water"]["consumption"]
                print(f"споживання електроенергії: {water} ㎥")
                lock1.release()
            case "3":
                print("""Вы находитесь в меню Котел, уточните свой выбор
                            3.1 Состояние: Включен/Выключен, температура, давление
                            3.2 Включить 
                            3.3 Выключить """)
            case "3.1":
                ...#Котел Состояние
            # открыть файл, прочитать последнюю запись, выделить параметр
                lock1.acquire()
                if reqwest()['boiler']['isRun'] == False:
                    print("Болер off!")
                if reqwest()['boiler']['isRun'] = True:
                    print("Болер включён!")
                lock1.release()
                ev1.set()
                ev1.wait()
                ev1.clear()
                if ev1.wait(0):
                    reqwest()
                with open('condition.json', 'r') as file:
                    file.readline('t2 '+ str(i) + '\n')
                print(" ",boiler_condition)
                with open('condition.json', 'r') as file:
                    file.readline('t2 '+ str(i) + '\n')
            case "3.2":
                ...#Включить
            # открыть файл, прочитать последнюю запись, выделить параметр
            # проверить состояние изменить если было выключено
                lock1.acquire()
                
                        if reqwest()['boiler']['isRun'] == False:
                            reqwest()['boiler']['isRun'] = True
                            print("Болер выключен!")
                lock1.release()
            case "3.3":
            # открыть файл, прочитать последнюю запись, выделить параметр
            # проверить состояние изменить если было включено
                lock1.acquire()
                if reqwest()['boiler']['isRun'] == True:
                    reqwest()['boiler']['isRun'] = False
                    print("Болер выключен!")
                lock1.release()
            case "4":
                ...# все записи из файла
                lock1.acquire()
                with open('condition.log', 'r') as file:
                    file.readline('t2 '+ str(i) + '\n')
            # открыть файл, прочитать все записи и раскодировать их через формат
                time = str(datetime.datetime.now())
                
                lock1.release()
# ev1.set()
# ev1.wait()
# ev1.clear()
# if ev1.wait(0):

#     f = open("img.png", 'wb')
#     f.write(resp.content)
#     f.close()

def reqwest():
    #  Каждые 5 секунд отправляются GET запросы на сервер (ссылка позже на GitHub) и принимается ответ 
# в видt JSON (формат в файле example.json).
# Полученные данные с добавленным дата/время сохраняются в файле (любой формат файла). 
# При возникновении Event отправляет запросы на сервер (ссылка позже на GitHub) 
    while True:
        global data
        resp = requests.get("http://localhost:8000/cgi-bin/index.py")
        if resp.status_code == 200:
            lock1.acquire()
            data=json.loads(resp.text) 
            time=str(datetime.datetime.now())
            with open('condition.log', 'w') as file:
                    file.write(time + '\n' + str(data) )
            lock1.release()
        time.sleep(5)
        if ev1.wait(3):
            ev1.wait()
            ev1.clear()

    resp = requests.get(request)
    if response.status_code == 200:
        data = json.loads(response.text)
        datarPickle = pickle.dumps(weather)

        temp= int(data["temperature"] ,["humidity"])
    return data


th1 = threading.Thread(target=menu) # создаем первый поток
th2 = threading.Thread(target=reqwest, daemon=True) # создаем второй поток

th1.start() # старт первого потока
th2.start() # старт второго потока


th1.join() # ожидание завершения первого потока
th2.join() # ожидание завершения второго потока