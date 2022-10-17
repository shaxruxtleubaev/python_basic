
try:
    from lesson30 import Cars
except ImportError as ie:
    print('Данный модуль не существует')
finally:
    audi = Cars('Audi', 'White', 'Sport Car', 'Alibek')
    bmw = Cars('BMW', 'Black', 'Sport car', 'Ismail')
    with open('infos.txt', mode='a') as file:
        speed_of_car = audi.cars_speed()
        second_driver = bmw.cars_speed()
        #info_about_driver = audi,drivers_info()
        infos = list()
        infos.extend([speed_of_car])
        file.write(f'\n{infos}')
        file.write(f'\n{second_driver}')
        file.close()

























