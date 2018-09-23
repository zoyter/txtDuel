# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:24:58 2016

@author: Oleg Lyash
"""
# Импортируем модуль для енерации случайных чисел
import random

# Это функция для вывода картинки врага по имени "Дарт Вейдер"
def print_dart():
    print("                   @@@                  ")
    print("                @@@ S@@@                ")
    print("            @@@@@@@ S@@@@@@@            ")
    print("          @@@,B@B@@ S@@B@B,@@@          ")
    print("         @@h@H@B@@@ S@@@B@H@,G@         ")
    print("        @@.HH@B@B@@ S@@B@B@H@Gi@        ")
    print("        @hHH@H@B@@@ S@@@B@HHGGG@        ")
    print("       @@.@HH@B@B@@ S@@B@B@H.@.@@       ")
    print("       @hh H@H@B@@@ S@@@B@H@G@GG@       ")
    print("      @@.H@@H@B@B@@ S@@B@B@H.@G.@@      ")
    print("      @.hH @@H@B@@@ S@@@B@H,@,@G @      ")
    print("      @..@, H@B@B@@ S@@B@B@H  B..@      ")
    print("      @.@  @@@@@@@@ S@@@@@@@@.@B.@      ")
    print("      @.h.@@&92r@@@@@@@@r29&@@.@.@      ")
    print("     @@.@@HX@@@@@X2sr:,@@@@@2A@@.@@     ")
    print("     @.h@H2@&&HBM@@@@@@MBH&&@2A@@.@     ")
    print("     @.@H2@ h&&HBM@A,@MBH&&h @2A@.@     ")
    print("     @@H2@ r&iX&&HB@@BH&&Xr&r @2A@@     ")
    print("    @@H2@h hrXXHBBMA,MBBHXXrh h@2H@@    ")
    print("    @ @@B@h h&HBBM@@@@MBBH&h h@B@H @    ")
    print("    @@h@:B@&&@@@@@@G,@@@@@@&&@B,@M@@    ")
    print("    @H@@@:B@@@B@@@@@@@@@@B@@@B,@@@M@    ")
    print("   @ HM@@A:BABABABA@@ABABABAB,A@@BH @   ")
    print("   @HM@B@@A:B:B,B,B@@B,B,B,B,A@@B@Mh@   ")
    print("   @MHM@B@AAAAAAAA@..@AAAAAAAA@B@BHM@   ")
    print("  @ hM@M@@BAAAAAA@@@@@@AAAAAA@@@B@Mh @  ")
    print("  @HMHM@H@@ABABA@B BB B@ABABA@@B@BHMH@  ")
    print(" @ MhM@M@B@BABA@ B BB B @ABAB@B@B@MhM @ ")
    print(" @HhMHM@H@@@BB@B.B BB B.B@BB@@@B@MHMhH@ ")
    print("@@hMhM@M@B@@@@@B.B BB B.B@@@@@B@B@MhMh@@")
    print("@ MhMHM@H@B@@S@@.B BB.B.@@S@@B@B@MHMhMH@")
    print("@M MH@@@@@@@@.2@@@@@@@@@@2.@@@@@@@@hMhM@")
    print("@#Mh@@@@    @@@@M@M@M@M@@@@@  @@@@@@hM#@")
    print("@@@@@@@@    @@@H@H@H@H@H@H@@     @@@@@@@")
    print("@##Mh@@     @@@@s@H@H@H@s@@@        hMM@")
    print("@          @@@@@@s@s@s@s@@@@@          @")
    print("          @@@@@@@@@@@@@@@@@@@@          ")
    print("      @@@@@B@B@B@B@@@@B@B@B@B@@@@@      ")
    print("   @@@@@B@B@@@B@@@B@@B@@@B@@@B@B@@@@@   ")
    print(" @@@3@3@@@33@3@3@3@33@3@3@3@33@@@B@B@@@ ")
    print("                                        ")

# 			Иницаилизируем переменные
#	Типы оружия	
weapon_types = ["кулак","нога","палка","нож","меч"]
#	Сила удара для каждого типа оружия
weapon_power = [1,2,3,4,5]
#	Имена врагов
enemy_names = ["Человек","Зомби", "Гарпия", "Медуза", "Волк", "Оборотень", "Дарт Вейдер"]
#	Сила удара для каждого из врагов
enemy_power = [1,2,3,4,5,6]
#	Признак окончания игры
flag = True
#	Переменная для хранения случайного числа
dice = 0
#	Уровень
level = 1

# Начало игры и вывод заставки на экран
print("###########################################")
print("#                                         #")
print("#           ╔══╗─╔╗╔╗╔═══╗╔╗              #")
print("#           ║╔╗╚╗║║║║║╔══╝║║              #")
print("#           ║║╚╗║║║║║║╚══╗║║              #")
print("#           ║║─║║║║║║║╔══╝║║              #")
print("#           ║╚═╝║║╚╝║║╚══╗║╚═╗            #")
print("#           ╚═══╝╚══╝╚═══╝╚══╝            #")
print("#                                         #")
print("###########################################")
print()
print("Д О Б Р О П О Ж А Л О В А Т Ь")
#	Задаем стартовые параметры для игрока
hero = {"name":"NoName Hero", "weapon":0, "hp":100,"force":10, "luck":0.1}
#	Просим ввести имя персонажа
hero["name"] = input("Назови свое имя герой: ")
#	Приветствуем игрока с использованием введенного им имени
print("Приветствую тебя %s"%(hero["name"]))
#	Описываем куда попал игрок и какие тут правила
print('Ты попал(а) в текстовую игру "ДУЭЛЬ"')
print('Правила игры: ')
print('')
#	Начинаем игру, т.е. запускаем основной цикл игры
print("Начинаем игру")
while flag: # Это начало основного цикла игры
    # Генерируем противника с использованием случайных чисел
    enemy = {"name":"NoName Hero", "hp":100,"force":10, "luck":0.1} 
    enemy["name"] =enemy_names[ random.randrange(len(enemy_names)) ]
    enemy["hp"] = random.randrange(99)+1
    enemy["force"] = random.randrange(9)+1
    enemy["weapon"] = random.randrange(len(weapon_types))
    # Запускаем раунд игры № N (типа уровень)
    print("#########################################")
    print("          Раунд №%s"%(level))
    print("%s (%s) против %s (%s)"%(hero["name"],hero["hp"], enemy["name"], enemy["hp"]))
    if enemy["name"] =="Дарт Вейдер":
        print_dart()
    
    isDuel = False
    buf = input("Вызвать на дуэль '%s'? (y/n): "%(hero["name"]))
    if buf == "y":
        isDuel = True
    while isDuel:
        # Ваш удар Определяем его успешность
        print("    ход игрока")
        dice = random.randrange(0,6)
        print(    "%s ударил(а) %s используя %s"%(hero["name"], enemy["name"], weapon_types[hero["weapon"]]))
        if dice + hero["luck"]-enemy["luck"] <3:
            print("    .... и попал(а), отняв %s энергии"%(hero["force"]+weapon_power[hero["weapon"]]))
            enemy["hp"] -= hero["force"]+weapon_power[hero["weapon"]]
        else:
            print("    .....и промазал(а)")
        
        # ход противника
        print("    ход противника")
        dice = random.randrange(0,6)
        print("    %s ударил(а) %s используя %s"%(enemy["name"], hero["name"], weapon_types[hero["weapon"]]))
        if dice + hero["luck"]-enemy["luck"] <3:
            print("    .... и попал(а), отняв %s энергии"%(hero["force"]+weapon_power[hero["weapon"]]))
            hero["hp"] -= enemy["force"]+weapon_power[enemy["weapon"]]
        else:
            print("    .....и промазал(а)")
        
        if hero["hp"]<=0 or enemy["hp"]<=0:
            isDuel = False
            if hero["hp"]<=0:
                print("Вы умерли :-(")
            if enemy["hp"]<=0:
                print("Враг повержен :-(")
                
            break
        
        print("%s (%s) vs %s (%s)"%(hero["name"],hero["hp"], enemy["name"], enemy["hp"]))
        
    print("          Раунд №%s завершен"%(level))
    print("#########################################")    
    isEscape = False
    buf = input("Завршить ?")
    if buf == "y":
        flag = False
    level += 1

