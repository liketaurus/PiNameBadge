# PiNameBadge
Простой скрипт на Python для масштабирования и отображения изображения бейджа на Raspberry в полноэкранном режиме (используется [pygame](https://ru.wikipedia.org/wiki/Pygame)).

## :clock4: Проверка работоспособности
Все, что вам нужно сделать - это создать бейдж в любом графическом редакторе, сохранить его под именем **Badge-Demo.PNG** (заменить [файл](https://github.com/liketaurus/PiNameBadge/blob/master/Badge-Demo.PNG) из репозитория) и выполнить команду ```./run.sh``` Все! Бейдж отобразится в полноэкранном режиме! Для выхода из него - просто нажмите <kbd>Esc</kbd>

Кстати, создать бейдж можно в моем [мастере бейджей](https://ppc-ntu-khpi.github.io/badge/).

## :rocket: Реальное использование
1. переходим в папку с установленным [LCD-show](https://github.com/goodtft/LCD-show):
```cd ../../Загрузки/LCD-show/```
2. переключаемся на LCD:
```sudo ./LC35-show```
3. переходим в папку, куда установлены файлы проекта:
```cd Документы/PiNameBadge```
4. запускаем отображение бейджа:
 ```./run.sh```
5. выход из отображения бейджа - все та же клавиша <kbd>Esc</kbd>
6. если надо переключиться обратно на экран, подключенный по HDMI:
```cd ../../Загрузки/LCD-show/```
```sudo ./LC35-hdmi```

Вернувшись к HDMI, возможно, после перезагрузки придется запустить в консоли ```raspi-config``` и [отключить оверскан](https://www.raspberrypi.org/documentation/configuration/raspi-config.md), чтобы картинка отображалась без полей.

При переключении на LCD у меня картинка отображалась одновременно на нем, и на HDMI-мониторе (правда, с тем же разрешением - 480х320 :disappointed:)

Кстати, поменять разрешение (размер картинки-бейджа) можно изменив значения констант ```WIDTH``` и ```HEIGHT``` в файле [**ShowBadge.py**](https://github.com/liketaurus/PiNameBadge/blob/master/ShowBadge.py). 

![](https://img.shields.io/badge/just%20a%20-sample-red.svg)  ![](https://img.shields.io/badge/made%20with-python-blue.svg) ![](https://img.shields.io/badge/made%20for%20-raspberry-brightgreen.svg)
