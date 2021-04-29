# vkspygamesVK Spy Games
![](https://camo.githubusercontent.com/3e67cbf9ad871339d5ab14a6bda8e6bdc76454f6d18eba7fe9b2888af85dfc28/687474703a2f2f7777772e6f6b6f2e62792f75706c6f6164732f706f7374732f323031382d30382f7468756d62732f313533343234323635355f322e6a7067)

**VK Spy Games** - программа, которая выводит список групп в ВК, в которых состоит пользователь, но не состоит никто из его друзей.

##Запуск программы

Для того чтобы скачать и запустить данную программу, выполните следующие шаги:

1. Если у Вас не установлен Git, установите его по [этой инструкции](https://github.com/netology-code/guides/tree/master/git);
1. Склонируйте с помощью Git данный репозиторий следующей командой:

    git clone https://github.com/Karina-I-F/vkspygames.git
    
1. Если у Вас не установлен Python, установите его по данным инструкциям:
        *[Инструкция по установке и настройке Python в Windows](https://github.com/netology-code/guides/blob/master/python/python_windows.md)
        *[Инструкция по установке и настройке Python в Mac](https://github.com/netology-code/guides/blob/master/python/python_mac.md)
        *[Инструкция по установке и настройке Python в Linux](https://github.com/netology-code/guides/blob/master/python/python_linux.md)

1. Для установки всех зависимостей запустите командную строку от имени администратора и выполните следующую команду:

    pip install -r 'путь до файла requirements.txt'

1. Запустите IDLE (Python), откройте файл diploma.py;

1. Запустите программу, нажав на клавишу F5;

1. Введите ID ВКонтакте.

###Выходные данные

Файл groups.json в папке с программой в формате:

[
    {
    “name”: “Название группы”, 
    “gid”: “идентификатор группы”, 
    “members_count”: количество_участников_сообщества
    ...
    },
    {
    …
    }
]
