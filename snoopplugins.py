#! /usr/bin/env python3
# Copyright (c) 2020 Snoop Project <snoopproject@protonmail.com>
"Плагины Snoop Project/Черновик"

import click
import csv
import itertools
import json
import locale
import os
import platform
import re
import random
import requests
import shutil
import socket
import sys
import threading
import time
import webbrowser
import snoopbanner

from collections import Counter
from colorama import Fore, Style, init
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from requests.adapters import HTTPAdapter
from requests_futures.sessions import FuturesSession
from rich.console import Console
from rich.progress import (track,BarColumn,TimeRemainingColumn,SpinnerColumn,TimeElapsedColumn,Progress)
from rich.table import Table
from rich.panel import Panel
from rich.style import Style as STL
from urllib.parse import urlparse

locale.setlocale(locale.LC_ALL, '')
# раскраска
init(autoreset=True)
console = Console()

head0 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
url = "https://freegeoip.app/json/"
time_data = time.localtime()

def ravno():
    console.rule(characters = '=', style="cyan bold")
def helpend():
    console.rule("[bold red]Конец справки")

wZ1bad=[] #отфильтрованные ip (не ip) или отфильтрованные данные Yandex, отфильтрованные 'геокоординаты'.
azS=[] #список результатов future request.
coord=[] #координаты многоцелевой список.

class ElapsedFuturesSession(FuturesSession):
    """test_metrica: API:: https://pypi.org/project/requests-futures/"""
    def request(self, method, url, *args, **kwargs):
        """test"""
        return super(ElapsedFuturesSession, self).request(method, url, *args, **kwargs)
my_session = requests.Session()
da = requests.adapters.HTTPAdapter(max_retries=4)
my_session.mount('https://', da)

dirresults = os.getcwd()
sessionY = ElapsedFuturesSession(executor=ThreadPoolExecutor(max_workers=10), session=my_session)
progressYa = Progress(TimeElapsedColumn(), "[progress.percentage]{task.percentage:>1.0f}%", auto_refresh=False)

def Erf(hvostfile):
    print(f"\n\033[31;1mНе могу найти_прочитать файл: '{hvostfile}'.\033[0m \033[36m " + \
           "\nПожалуйста, укажите текстовый файл в кодировке —\033[0m \033[36;1mutf-8.\033[0m\n")
    print("\033[36mПо умолчанию, например, блокнот в OS Windows сохраняет текст в кодировке — ANSI.\033[0m")
    print("\033[36mОткройте ваш список пользователей и измените кодировку [файл ---> сохранить как ---> utf-8].")
    print("\033[36mИли удалите из файла нечитаемые спецсимволы.")
    

## Модуль Yandex_parser
def module3():
    while True:
        listlogin = []
        dicYa = {}

        def parsingYa(login):
# Запись в txt
            if Ya == '4':
                file_txt = open(dirresults + "/results/plugins/Yandex_parser/" + str(hvostfile) + '_' + \
                time.strftime("%d_%m_%Y_%H_%M_%S", time_data) + ".txt", "w", encoding="utf-8")
            #raise Exception("")
            else:
                file_txt = open(dirresults + "/results/plugins/Yandex_parser/" + str(login) + ".txt", "w", encoding="utf-8")

# Парсинг
            for login in listlogin:
                urlYa = f'https://yandex.ru/collections/api/users/{login}/'
                try:
                    r = sessionY.get(urlYa, headers = head0, timeout=3)
                    azS.append(r)
                except:
                    print(Fore.RED + "\nОшибка" + Style.RESET_ALL)
                    if Ya != '4':
                        ravno()
                    continue

            with progressYa:
                if Ya == '4':
                    task = progressYa.add_task("", total=len(listlogin))

                for reqY, login in zip(azS, listlogin):
                    if Ya == '4':
                        progressYa.refresh()
                        progressYa.update(task, advance=1)
                    rY=reqY.result()
#                    print(rY.text)
                    try:
                        rdict = json.loads(rY.text)
                        if rdict.get('title') == "404 Not Found":
                            raise Exception("")
                    except:
                        rdict = {}
                        rdict.update(public_id="Увы", display_name="-No-")

                    pub = rdict.get("public_id")
                    name = rdict.get("display_name")
                    email=str(login)+"@yandex.ru"
                    avatar = rdict.get("default_avatar_id")

                    if rdict.get("display_name") == "-No-":
                        if Ya != '4':
                            print(Style.BRIGHT + Fore.RED + "\nНе сработало")
                            console.rule(characters = '=', style="cyan bold\n")
                        else:
                            wZ1bad.append(str(login))
                            continue
                        continue
                    else:
                        table1 = Table(title = "\n" + Style.BRIGHT + Fore.RED + str(login) + Style.RESET_ALL, style="green")
                        table1.add_column("Имя", style="magenta", overflow="fold")
                        table1.add_column("Логин", style="cyan", overflow="fold")
                        table1.add_column("E-mail", style="cyan", overflow="fold")
                        if Ya == '3':
                            table1.add_row(name,"Пропуск","Пропуск")
                        else:
                            table1.add_row(name,login,email)
                        console.print(table1)

                        otzyv=f"https://reviews.yandex.ru/user/{pub}"
                        market=f"https://market.yandex.ru/user/{pub}/reviews"

                        if Ya == '3':
                            music=f"\033[33;1mПропуск\033[0m"
                        else:
                            music=f"https://music.yandex.ru/users/{login}/tracks"
                        dzen=f"https://zen.yandex.ru/user/{pub}"
                        qu=f"https://yandex.ru/q/profile/{pub}/"
                        avatar_html = f"https://avatars.mds.yandex.net/get-yapic/{avatar}/islands-retina-50"
                        avatar_cli = f"https://avatars.mds.yandex.net/get-yapic/{avatar}/islands-300"

                        print("\033[32;1mЯ.Отзывы:\033[0m", otzyv)
                        print("\033[32;1mЯ.Маркет:\033[0m", market)
                        print("\033[32;1mЯ.Музыка:\033[0m", music)
                        print("\033[32;1mЯ.Дзен:\033[0m", dzen)
                        print("\033[32;1mЯ.Кью:\033[0m", qu)
                        print("\033[32;1mAvatar:\033[0m", avatar_cli)

                        yalist=[avatar_html, otzyv, market, music, dzen, qu]

                        file_txt.write(f"{login} | {email} | {name}\n{avatar_cli}\n{otzyv}\n{market}\n{music}\n{dzen}\n{qu}\n\n")

                    for webopen in yalist:
                        if webopen == music and Ya == '3':
                            continue
                        else:
                            if "arm" in platform.platform(aliased=True, terse=0) or "aarch64" in platform.platform(aliased=True, terse=0):
                                pass
                            else: 
                                webbrowser.open(webopen)
            ravno()
            azS.clear()

# сохранение в html
            if Ya == '4':
# запись в txt концовка
                file_txt.write(f"\nНеобработанные данные из файла '{hvostfile}' ({len(wZ1bad)}):\n")
                for badsites in wZ1bad:
                    file_txt.write(f"{badsites}\n")
                file_txt.write(f"\nОбновлено: " + time.strftime("%d/%m/%Y_%H:%M:%S", time_data) + ".")
                file_txt.close()
    # Конец функции

        print(
"\n\033[36m[\033[0m\033[32;1m1\033[0m\033[36m] --> Указать логин пользователя\n\
[\033[0m\033[32;1m2\033[0m\033[36m] --> Указать публичную ссылку на Яндекс.Диск\n\
[\033[0m\033[32;1m3\033[0m\033[36m] --> Указать идентификатор пользователя\n\
[\033[0m\033[32;1m4\033[0m\033[36m] --> Указать файл с именами пользователей\n\
[\033[0m\033[32;1mhelp\033[0m\033[36m] --> Справка\n\
[\033[0m\033[31;1mq\033[0m\033[36m] --> Выход\n")

        Ya = input()

# Выход
        if Ya == "q":
            print(Style.BRIGHT + Fore.RED + "Выход")
            sys.exit()

# Help
        elif Ya == "help":
            snoopbanner.help_yandex_parser()
            helpend()

# Указать login
        elif Ya == '1':
            print("\033[36m└──Введите username/login разыскиваемого пользователя, например,\033[0m\033[32;1m bobbimonov\033[0m\n")
            login = input()
            listlogin.append(login)

            parsingYa(login)

# Указать ссылку на Я.Диск
        elif Ya == '2':
            print("\033[36m└──Введите публичную ссылку на Яндекс.Диск, например,\033[0m\033[32;1m https://yadi.sk/d/7C6Z9q_Ds1wXkw\033[0m\n")
            urlYD = input()

            try:
                r2 = my_session.get(urlYD, headers = head0, timeout=3)
            except:
                print(Fore.RED + "\nОшибка" + Style.RESET_ALL)
                console.rule(characters = '=', style="cyan bold\n")
                continue
            try:
                login = r2.text.split('displayName":"')[1].split('"')[0]
            except:
                login = "NoneStop"
                print(Style.BRIGHT + Fore.RED + "\nНе сработало")

            if login != "NoneStop":
                listlogin.append(login)
                parsingYa(login)

# Указать идентиффикатор Яндекс пользователя
        elif Ya == '3':
            print("\033[36m└──Введите идентификатор пользователя Яндекс, например,\033[0m\033[32;1m tr6r2c8ea4tvdt3xmpy5atuwg0\033[0m\n")
            login = input()
            listlogin.append(login)

            if len(login) != 26:
                print(Style.BRIGHT + Fore.RED + "└──Неверно указан идентификатор пользователя" + Style.RESET_ALL)
                ravno()
            else:
                parsingYa(login)

# Указать файл с логинами
        elif Ya == '4':
            print("\033[31;1m└──В Demo version этот метод плагина недоступен\033[0m\n")
            snoopbanner.donate()
        else:
            print(Style.BRIGHT + Fore.RED + "└──Неверный выбор" + Style.RESET_ALL)
            ravno()

## Модуль Reverse Vgeocoder
def module2():
    print(Style.BRIGHT + Fore.RED + "└──Плагин Reverse Vgeocoder 'сложен' и не поддерживается в Snoop_termux\n\nВыход\n" + Style.RESET_ALL)

## Модуль GEO_IP/domain
def module1():
# Домен > IPv4/v6
    def res46(dipp):
        try:
            res46 = socket.getaddrinfo(f"{dipp}", 80)
        except:
            pass
        try:
            res4 = res46[0][4][0]
        except:
            res4 = "-"
        try:
            if ":" not in res46[-1][4][0]:
                res6 = "-"
            else:
                res6 = res46[-1][4][0]
        except:
            res6 = "-"
        #print(res46)
        return res4, res6

# Запрос future request
    def reqZ():
        try:
            r=req.result()
            return r.text
        except requests.exceptions.ConnectionError:
            print(Fore.RED + "\nОшибка соединения\n" + Style.RESET_ALL)
        except requests.exceptions.Timeout:
            print(Fore.RED + "\nОшибка таймаут\n" + Style.RESET_ALL)
        except requests.exceptions.RequestException:
            print(Fore.RED + "\nОшибка не идентифицирована\n" + Style.RESET_ALL)
        except requests.exceptions.HTTPError:
            print(Fore.RED + "\nОшибка HTTPS\n" + Style.RESET_ALL)
        return "Err"

# Выбор поиска одиночный или '-f'
    ravno()
    print("\n\033[36mВведите домен (пример:\033[0m \033[32;1mexample.com\033[0m\033[36m), или IPv4/IPv6 (пример:\033[0m \033[32;1m8.8.8.8\033[0m\033[36m),\n\
или url (пример: \033[32;1mhttps://example.com/1/2/3/foo\033[0m\033[36m), \n\
или укажите файл_с данными, выбрав ключ (пример:\033[0m \033[32;1m--file\033[0m\033[36m или\033[0m \033[32;1m-f\033[0m\033[36m)\n\
[\033[0m\033[32;1m-f\033[0m\033[36m] --> обработатка файла данных\n\
[\033[0m\033[32;1menter\033[0m\033[36m] --> информация о своем GEO_IP\n\
[\033[0m\033[31;1mq\033[0m\033[36m] --> Выход")
    dip = input("\n")

# выход
    if dip == "q":
        print(Style.BRIGHT + Fore.RED + "Выход")
        sys.exit()

# проверка данных
    elif dip == '--file' or dip == '-f':
        while True:
            print("""\033[36m├──Выберите тип поиска
│
[\033[0m\033[32;1m1\033[0m\033[36m] --> Online (медленно)
[\033[0m\033[32;1m2\033[0m\033[36m] --> Offline (быстро)
[\033[0m\033[32;1m3\033[0m\033[36m] --> Offline_тихий (очень быстро)
[\033[0m\033[32;1mhelp\033[0m\033[36m] --> Справка\n\
[\033[31;1mq\033[0m\033[36m] --> Выход\033[0m""")

            dipbaza = input('\n')

# Выход
            if dipbaza == "q":
                print("\033[31;1mВыход\033[0m")
                sys.exit(0)
# Справка
            elif dipbaza == "help":
                snoopbanner.geo_ip_domain()
                helpend()

# Оффлайн поиск
# Открываем GeoCity
            elif dipbaza == "2" or dipbaza == "3":
                while True:
                    print("\033[31;1m└──В Demo version этот метод плагина недоступен\033[0m\n")
                    snoopbanner.donate()
                    break

                break

# Онлайн поиск
            elif dipbaza == "1":
                print("\033[31;1m└──В Demo version этот метод плагина недоступен\033[0m\n")
                snoopbanner.donate()
                break

# Неверный выбор ключа при оффлайн/онлайн поиске. Выход
            else:
                print(Style.BRIGHT + Fore.RED + "└──Неверный выбор" + Style.RESET_ALL)
                ravno()

# одиночный запрос
    else:
        if dip == "":
            pass
            uu3 = dip
        else:
            u = urlparse(dip).hostname
            uu3 = dip
            if bool(u) == False:
                dip=dip.split("/")[0].strip()
            else:
                dip=u.replace("www.", "").strip()
        session = requests.Session()
        url2 = 'https://freegeoip.app/json/{}'.format(dip)
        try:
            r=session.get(url=url2, headers = head0, timeout=3)
            dip1 = r.text
            dip_dic = json.loads(dip1)
            T1=dip_dic.get("country_code")
            T2=dip_dic.get("time_zone")
            T3=dip_dic.get("latitude")
            T4=dip_dic.get("longitude")
            T5=dip_dic.get("ip")
        except:
            T1="-"
            T2="-"
            T3="stop"
            T4="stop"
            T5="-"
            print("""\033[31;1m\n
|\ | _ ._  _
| \|(_)| |(/_\033[0m""")

# IP/Домен > Домен и IPv4v6
        try:
            resD1=socket.getfqdn(dip)
            res4, res6 = res46(resD1)
        except:
            resD1="-"
            print("err")

        table = Table(title = Style.BRIGHT + Fore.RED + str(uu3) + Style.RESET_ALL, style="green")
        table.add_column("Сountry", style="magenta")
        if dip == "":
            table.add_column("Your IP", style="cyan", overflow="fold")
        else:
            table.add_column("IPv4", style="cyan", overflow="fold")
            table.add_column("IPv6", style="cyan", overflow="fold")
        table.add_column("Domain", style="green", overflow="fold")
        table.add_column("Time_Zone", style="green", overflow="fold")
        if dip == "":
            table.add_row(T1,T5,resD1,T2)
        else:
            table.add_row(T1,res4,res6,resD1,T2)
        console.print(table)
        if T3 == "stop" and T4 =="stop":
            print("\n")
            URL_GEO = ""
        else:
            URL_GEO = f"https://www.openstreetmap.org/#map=13/{T3}/{T4}"
            URL_GEO2 = f"https://www.google.com/maps/@{T3},{T4},28m/data=!3m1!1e3"
            print(Style.BRIGHT + Fore.BLACK + f"{URL_GEO}" + Style.RESET_ALL)
            print(Style.BRIGHT + Fore.BLACK + f"{URL_GEO2}\n" + Style.RESET_ALL)

        module1()
if __name__ == "__main__":
    module1()
