Snoop Project for Termux
========================

## Snoop Project один из самых перспективных OSINT-инструментов по поиску никнеймов.
- [X] This is the most powerful software taking into account the CIS location.

<img src="https://raw.githubusercontent.com/snooppr/snoop/master/images/snoopandroid.png" />  

Is your life slideshow? Ask Snoop.  
Snoop project is developed without taking into account the opinions of the NSA and their friends,  
that is, it is available to the average user.
............................................................................  

**Самостоятельная сборка ПО из исходно кода**  
**Self-build software from source**

## Snoop for Android/Demo  
<img src="https://raw.githubusercontent.com/snooppr/snoop/master/images/Snoop_termux.plugins.png" />  

**Native Installation**  

Установить [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=en "Google Play")  
```
# Примечание: установка Snoop на Termux продолжительная по времени
# Войти в домашнюю папку Termux (т.е. просто открыть Termux)
$ termux-setup-storage
$ ls #/data/data/com.termux/files/home # дефолтный/домашний каталог

# Установить python3 и зависимости
$ apt update && pkg upgrade && pkg install python libcrypt libxml2 libxslt git
$ pip install --upgrade pip

# Клонировать репозиторий
$ git clone https://github.com/snooppr/snoop -b snoop_termux
# (Если флешкa FAT (ни ext4), в таком случае,
# клонировать репозиторий только в ДОМАШНЮЮ директорию Termux)

# Войти в рабочий каталог Snoop
$ cd ~/snoop
# Установить зависимости 'requirements'
$ python3 -m pip install -r requirements.txt


# Дополнение для устаревших гаджетов (Android 6)
# Примечание на современных гаджетах пакеты уже предустановлены и настроены
# добавьте любое 'рандомное' имя и почту [^1]:
$ git config --global user.email "you@example.com"
$ git config --global user.name "username"
# Установите coreutils
$ pkg install coreutils
```
## Using
**English version — of Snoop see release (available 'Snoop EN version').**
```
$ python snoop.py --help

optional arguments:
  -h, --help           show this help message and exit

service arguments:
  --version, -V        About: вывод на печать версий:: OS; Snoop;
                       Python и Лицензии
  --list all           Вывести на печать детальную информацию о базе
                       данных Snoop
  --donate y, -d y     Пожертвовать на развитие Snoop Project-а,
                       получить/приобрести Snoop Full Version
  --autoclean y, -a y  Удалить все отчеты, очистить место
  --update y           Обновить Snoop

plugins arguments:
  --module y, -m y     OSINT поиск: задействовать различные плагины
                       Snoop:: IP/GEO/YANDEX (список плагинов будет
                       пополняться)

search arguments:
  nickname             Никнейм разыскиваемого пользователя.
                       Поддерживается поиск одновременно нескольких имён. Ник,
                       содеражащий в своем имени пробел, заключается в кавычки
  --verbose, -v        Во время поиска 'username' выводить на печать
                       подробную вербализацию
  --base , -b <path>   Указать для поиска 'username' другую БД
                       (Локально)/В demo version функция отключена
  --web-base, -w       Подключиться для поиска 'username' к
                       обновляемой web_БД (Online)/ В demo version функция
                       отключена
  --site , -s chess    Указать имя сайта из БД '--list all'. Поиск
                       'username' на одном указанном ресурсе
  --time-out , -t 9    Установить выделение макс.времени на ожидание
                       ответа от сервера (секунды). Влияет на
                       продолжительность поиска. Влияет на 'Timeout
                       ошибки:'Вкл. эту опцию необходимо при медленном
                       интернет соединении, чтобы избежать длительных
                       зависаний при неполадках в сети (по умолчанию значение
                       выставлено 5с)
  --found-print, -f    Выводить на печать только найденные аккаунты
  --no-func, -n        ✓Монохромный терминал, не использовать цвета в
                       url ✓Отключить звук ✓Запретить открытие web browser-а
                       ✓Отключить вывод на печать флагов стран ✓Отключить
                       индикацию и статус прогресса. Экономит ресурсы системы
                       и ускоряет поиск
  --userload , -u      Указать файл со списком user-ов. Пример_Linux:
                       'python3 snoop.py -u ~/listusers.txt start'.
                       Пример_Windows: 'python snoop.py -u
                       c:\snoop\listusers.txt start'
  --country, -c        Сортировка 'вывода на
                       печать/запись_результатов' по странам, а не по алфавиту
  --save-page, -S      Сохранять найденные странички пользователей в
                       локальные файлы
  --cert-off, -C       Выкл проверку сертификатов на серверах. По
                       умолчанию проверка сертификатов на серверах включена на
                       Snoop for Android, что повышает скорость поиска, но
                       дает больший percent ложных срабатываний
  --normal, -N         Переключатель режимов: SNOOPninja > нормальный
                       режим > SNOOPninja. По_умолчанию (GNU/Linux Full
                       Version) вкл 'режим SNOOPninja': ускорение поиска
                       ~25pct, экономия ОЗУ ~50pct, повторное 'гибкое'
                       соединение на сбойных ресурсах. Режим SNOOPninja
                       эффективен только для Snoop for GNU/Linux Full Version.
                       По_умолчанию (Windows) вкл 'нормальный режим'. В Demo
                       Version переключатель режимов деактивирован
```

**Example**
```
# Для поиска только одного пользователя:
$ python3 snoop.py username1
# Или, например, кириллица поддерживается:
$ python3 snoop.py олеся
# Для поиска имени, содержащего пробел:
$ python3 snoop.py "ivan ivanov"
$ python3 snoop.py ivan_ivanov
$ python3 snoop.py ivan-ivanov

# Для поиска одного и более юзеров:
$ python3 snoop.py username1 username2 username3 username4

# Поиск множества юзеров — сортировка вывода результатов по странам;
# избежание длительных зависаний на сайтах (чаще 'мёртвая зона' зависит от вашего ip-адреса);
# выводить на печать только найденные аккаунты; сохранять странички найденных
# аккаунтов локально; указать файл со списком разыскиваемых аккаунтов;
# подключиться для поиска к расширяемой и обновляемой web-base Snoop:
$ python3 snoop.py -с -t 6 -f -S -u ~/file.txt -w start

# 'ctrl-c/z' — прервать поиск
```
Найденные учетные записи будут храниться в ~/snoop/results/*/username.{txt.csv.html}.  
Для доступа браузера к результатам поиска на платформе Android требуются рут права.  
csv открывать в *office в кодировке **utf-8**, разделитель полей **запятая**.  

Уничтожить **все** результаты поиска — удалить каталог '~/snoop/results'.  
или ```python snoop.py --autoclean y```

```
# Обновляйте Snoop для тестирования новых функций в ПО:
$ python3 snoop.py --update y #Требуется установка Git.
```

**An example of searching Phone**  
<img src="https://raw.githubusercontent.com/snooppr/snoop/master/images/Android%20snoop_run.png" />
