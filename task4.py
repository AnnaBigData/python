# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 22:01:24 2021

@author: Anna Ku
"""

# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#  А также методы: go, stop, turn(direction), которые должны сообщать, 
#  что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую
#  скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
#  выводиться сообщение о превышении скорости.


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color 
        self.is_police = is_police
                
    def show_speed (self):
       # print (self.speed) 
       print(f"{self.name}: Скорость автомобиля - {self.speed}")
            
    def go(self):
        print (f"{self.name}: Go")
    
    def turn_right(self):
        print (f"{self.name}: Moving right")
        
    def stop(self):
        print (f"{self.name}: Stop")
  
#ограничение скорости не работает. Пыталась вытащить из примера решения 
#домашнего задания и nам при перемене дочерних классов показания скорости
# никак не влияют на картину        
  
class Sedan(Car):
        "City car"
        
        # def show_speed(self):
        #     if self.speed > 60:
        #         print ("Limit exceeded")
        #     else: 
        #         print (self.speed) 
        def show_speed(self):
            return f"{self.name}: Скорость автомобиля - {self.speed} - ПРЕВЫШЕНИЕ СКОРОСТИ!!!" \
            if self.speed > 60 else f"{self.name}: Скорость автомобиля - {self.speed}" # super().show_speed()
                
class Truck(Car):
        "Work"
        
        def show_speed(self):
         
        #     if self.speed > 60:
        #         print ("Limit exceeded")
        #     else: 
        #         print (self.speed) 
            return f"{self.name}: Скорость автомобиля - {self.speed} - ПРЕВЫШЕНИЕ СКОРОСТИ!!!" \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля - {self.speed}" # super().show_speed()  
                
a = Truck("Volvo", "White", 80)  
a.show_speed()