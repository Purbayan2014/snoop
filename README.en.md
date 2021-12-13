Snoop Project for Termux
========================

## Snoop Project is one of the most promising OSINT tools for finding nicknames.
- [X] This is the most powerful software taking into account the CIS location.

<p align="center">  
  <img src="https://raw.githubusercontent.com/snooppr/snoop/master/images/snoopandroid.png" />  
</p>  

Is your life slideshow? Ask Snoop.  
Snoop project is developed without taking into account the opinions of the NSA and their friends,  
that is, it is available to the average user.  

## Self-build software from source  
**Snoop for Android/Demo**  
<p align="center">  
  <img src="https://raw.githubusercontent.com/snooppr/snoop/master/images/Snoop_termux.plugins.png" width="90%" />  
</p>  

**Self-build software from source**  
**Native Installation**  

Install [Termux](https://f-droid.org/en/packages/com.termux/ "F-Droid")  
```
# Note: Installing Snoop on Termux is time consuming
# Enter Termux home folder (i.e. just open Termux)
$ termux-setup-storage
$ pwd #/data/data/com.termux/files/home # default/home directory

# Install python3 and dependencies
$ apt update && pkg upgrade && pkg install python libcrypt libxml2 libxslt git
$ pip install --upgrade pip

# Clone the repository
$ git clone https://github.com/snooppr/snoop -b snoop_termux
# (if the flash drive is FAT (not ext4), in this case,
# clone the repository only to the Termux HOME directory)

# Enter the Snoop working directory
$ cd ~/snoop
# Install the 'requirements' dependencies
$ python3 -m pip install -r requirements.txt

# To expand the terminal output in Termux (by default, 2k lines are displayed in the CLI),  
for example, displaying the entire database of the option '--list-all [1/2]'  
add the line 'terminal-transcript-rows=10000' to the file '~/.termux/termux.properties'  
(the feature is available in Termux v0.114+).  
Restart Termux. 

# The user can also launch the Snoop Project on the snoop command from anywhere in the cli by creating an alias.  
$ printf "alias snoop='cd && cd snoop && python snoop.py'" >> .bashrc  
# The user can also run a quick check on the database of the site he is interested in, without using the 'list-all' option, using the 'snoopcheck'command
$ alias snoopcheck='cd && cd snoop && printf 2 | python snoop.py --list-all | grep -i' >> .bashrc  
# restart Termux. 
```
<p align="center">  
  <img src="https://raw.githubusercontent.com/snooppr/snoop/master/images/snoop_alias.gif" width="40%" />  
</p>  


## Using
```
Help

optional arguments:
  -h, --help            show this help message and exit

service arguments:
  --version, -V         printing versions of :: OS; Snoop;
                        Python and Licenses
  --list-all, -l        Print detailed information about the 
                        Snoop database
  --donate, -d          Donate to the development of the Snoop Project,
                        get/buy Snoop Full Version
  --autoclean, -a       Delete all reports, clear space
  --update, -U          Обновить Snoop

plugins arguments:
  --module, -m          OSINT search: use various plugins Snoop ::
                        IP/GEO/YANDEX (the list of plugins will continue
                        to grow)

search arguments:
  nickname              The nickname of the wanted user.
                        Searching for several names at the same time is 
                        supported. Nicknames containing a space in their name
                        are enclosed in quotation marks
  --verbose, -v         When searching for 'username', print detailed
                        verbalization
  --base , -b <path>    Specify another database for search for 'username'
                        (Local)/In demo version the function is disabled
  --web-base, -w        Connect to search for 'username' to the updated web_DB
                        (Online)/In demo version the function is disabled
  --site , -s <site_name> 
                        Specify the name of the site from the database 
                        '--list-all'. Search for 'username' on one specified
                        resource, it is acceptable to use the '-s' option
                        multiple times
  --exclude , -e <country_code> 
                        Exclude the selected region from the search,
                        it is permissible to use the '-e' option several times,
                        for example, '-e RU -e WR' exclude Russia and World from search
  --one-level , -o <country code> 
                        Include only the selected region in the search,
                        it is permissible to use the '-o' option several times,
                        for example, '-o US -o UA' search for USA and Ukraine
  --country, -c         Sort 'print/record_results' by country,
                        not alphabetically
  --time-out , -t <digit> 
                        Set maximum time allocation for waiting for a response 
                        from the server (seconds). Affects the search duration.
                        Affects 'Timeout errors:' On. this option is necessary
                        with a slow Internet connection to avoid long freezes
                        in case of network problems
                        (by default, the value is set to 5s)
  --found-print, -f     Print only found accounts
  --no-func, -n         ✓Monochrome terminal, do not use colors in url 
                        ✓Disable sound ✓Disable opening web browser
                        ✓Disable printing of country flags 
                        ✓Disable indication and progress status. 
                        Saves system resources and speeds up searches
  --userlist , -u <path> 
                        Specify a file with a list of users.
                        Example: 'python snoop.py -u
                        /storage/emulated/0/Download/listusers.txt'
  --save-page, -S       Save found user pages to local files
  --cert-off, -C        Disable verification of certificates on servers. 
                        By default, server certificate checking is enabled on
                        Snoop for Android, which improves search speed, 
                        but may result in higher percentages of false positives
  --headers , -H <name> 
                        Set the user-agent manually, the agent is enclosed in 
                        quotes, by default a random or overridden user-agent
                        from the snoop database is set for each site.
                        https://юзерагент.рф/
  --normal-mode, -N     Mode switch: SNOOPninja> normal mode> SNOOPninja. 
                        By_default (GNU/Linux Full Version) on 
                        'SNOOPninja mode': search acceleration ~ 25pct,
                        RAM saving ~ 50pct, repeated 'flexible' connection on
                        failed resources. SNOOPninja mode is only effective for
                        Snoop for GNU/Linux Full Version. The default
                        (on Windows) is 'normal mode'. 
                        In Demo Version, the mode switch is deactivated
  --quick-mode , -q     Quiet search mode on. Intermediate
                        the results are not printed. Repeated flexible
                        connections on faulty resources without slowing down
                        the software. The most advanced search mode 
                        (in development - not use)
```

**Example**
```
# To search for just one user:
$ python3 snoop.py username1
# Or, for example, Cyrillic is supported:
$ python3 snoop.py олеся
# To search for a name containing a space:
$ python3 snoop.py "bob dylan"
$ python3 snoop.py bob_dylan
$ python3 snoop.py bob-dylan

# To search for one or more users:
$ python3 snoop.py username1 username2 username3 username4

# Search for multiple users - sorting the output of results by country;
# avoid long freezes on sites (more often the 'dead zone' depends on your ip-address);
# print only found accounts; save pages found
# of accounts locally; specify a file with a list of wanted accounts;
# connect to search for Snoop's extensible and updatable web-base:
$ python3 snoop.py -с -t 9 -f -S -u ~/file.txt -w

# 'ctrl-c' — abort search
```
Found accounts will be stored in '~/snoop/results/nicknames/*/username. {Txt.csv.html}'.  
To access the browser to search results on the Android platform, it is desirable to have root rights.  
csv open in *office, field separator **comma**.    

Destroy **all** search results - delete the directory '~/snoop/results'.
or ```python snoop.py --autoclean```

```
# Update Snoop to test new software features:
$ python3 snoop.py --update y #requires a Git installation.
```

**An example snoop for android**  
<p align="center">  
  <img src="https://raw.githubusercontent.com/snooppr/snoop/master/images/Android%20snoop_run.gif" width="40%" />  
</p>  
