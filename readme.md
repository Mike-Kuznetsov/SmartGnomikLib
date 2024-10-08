# SmartGnomikLib
[English readme](https://github.com/Mike-Kuznetsov/SmartGnomikLib/blob/main/english_readme.md)
### Smart Home Controller

Библиотека для голосового управления умными устройствами.      
В качестве устройства-контроллера можно использовать Orange Pi или Raspberry Pi.
Вы можете также сами переделать свои не-умные устройства в умные с помощью ESP8266/ESP32, мои видео вам помогут.

[Видео про библиотеку](https://www.youtube.com/watch?v=b9HwBJCooCI)      
[Канал Заметки ESPшника](https://www.youtube.com/@ESPdev)      
[Канал MautozTech](https://www.youtube.com/c/MautozTech)      

### Библиотека позволяет управлять:
- Любыми устройствами управляемыми с помощью GET-запросов      
  (например самодельными устройствами на ESP8266/ESP32)
- Устройствами совместимыми с платформой Tuya
- Компьютером

Образ настроенной ОС с настроенной программой для Orange Pi PC2 (и совместимых с ней плат): [Google Drive](https://drive.google.com/file/d/128jVv7pF3YjIEn2ycC7YM1Svyow9LUSr)      
Хочу отметить, что предустановленная программа может быть не последней версии.      

Бесплатные инвестиционные лайфхаки: https://pomoex.ru      
Телеграм канал: https://t.me/tech_pub      

### Преимущества библиотеки:
- Ваши данные не покидают вашу домашнюю сеть
- Высокая скорость работы
- Неограниченная возможность кастомизации, простота кастомизации

### Как собрать/настроить устройства (YouTube):
- [Умная люстра своими руками](https://www.youtube.com/watch?v=LqcxTVnJerQ)
- [Голосовое управление кондиционером](https://www.youtube.com/watch?v=OrqkeDkkqKg)
- [Голосовое управление компьютером](https://www.youtube.com/watch?v=hH3e1tUTVxI)
- [Умная батарея своими руками](https://www.youtube.com/watch?v=1qQIQP5o4bY)
- [Голосовое управление умными устройствами своими руками (+ про Tuya)](https://www.youtube.com/watch?v=Uk_LlI7Qcqw)
- [Мигание светодиодом](https://www.youtube.com/watch?v=lKjLFaw47dM)

### Установка и подготовка ОС:
1. <details> 
      <summary>Скачивание дистрибутива Armbian или другой ОС</summary>
  
      ```
      Голая Armbian 20.08 как у меня: https://drive.google.com/file/d/1FFzEcmnzOcK9rwSuBZPOyZdQ0BdvRMhi
      ```
   </details>
2. <details> 
      <summary>При необходимости: настройка частоты процессора</summary>
  
      ```
      Введите команду "armbian-config", выберите System >> CPU Frequency.
      У меня минимальная 480 МГц и максимальная 1200 МГц с настройкой "On demand", максимальную можно ставить и выше.
      ```
   </details> 
3. <details> 
      <summary>При необходимости: установка графической оболочки</summary>

      ```
      Если скачали ОС без графической оболочки, то для удобства можете её установить, прописав команды:
      "apt update"
      "apt install lubuntu-desktop -y"
      ```
   </details> 
4. <details> 
      <summary>Включение микрофона</summary>

      ```
      Если не работает микрофон на OrangePi, то пропишите "alsamixer", нажмите F4, стрелками выберите микрофон и нажмите пробел чтобы его включить.
      Если там есть два микрофона, можете включить оба. Потом нажимаете CTRL+S чтобы сохранить настройки и CTRL+C чтобы закрыть программу.
      ```
   </details>
5. <details> 
      <summary>Проверка микрофона</summary>
  
      ```
      Для проверки микрофона можете подключить наушники к OrangePi и ввести в терминал "arecord | aplay",
      звук с микрофона будет проигрываться в наушниках.
      ```
   </details>
6. <details> 
      <summary>Включение автоматического входа в ОС без ввода пароля</summary>
      - Решение для Lubuntu: Создать файл /etc/sddm.conf со следующим содержимым:
  
      ```
      [Autologin]      
      User=[ВАШЕ ИМЯ ПОЛЬЗОВАТЕЛЯ]      
      Session=Lubuntu.desktop      
      Relogin=true      
      ```
   </details>
   
### Скачивание и настройка программы:
1. Скачивание библиотеки, распаковка архива
2. Запуск файла setup.sh
3. <details> 
      <summary>Скачивание голосовой модели</summary>
      
      ```
      Модель слишком тяжелая для загрузки на Github, 40 мб. Поэтому надо скачивать самостоятельно.
      Папку с моделью надо поместить в папку с программой (например с example.py)
      Ссылка: https://alphacephei.com/vosk/models
      Название необходимой модели: "vosk-model-small-ru-0.22" (или новее если будет)
      ```
    </details>   
5. Написание кода или редактирование example.py
6. <details> 
      <summary>Настройка автозапуска программы</summary>
      - В Lubuntu это делается в Session Settings, там необходимо добавить следующую команду в автозапуск. Если у вас другой путь к папке, измените.
  
      ```
      cd /home/orangepi/Desktop/SmartGnomik && python3 example.py
      ```
   </details>
7. <details> 
      <summary>Настройка мигания светодиода</summary>
  
      ```
      Работает только на Orange Pi, потому что у меня нет Raspberry Pi для написания кода/тестирования.
      Если у вас Raspberry Pi и вы хотите чтобы светодиод мигал после выполнения команды, вы можете отредактировать код библиотеки.
      
      Для управления GPIO контактами (и мигания светодиодом) программа должна иметь root-доступ.
      Поэтому по-хорошему нужно:
      1. Сделать root владельцем всей папки (chown -R root [НАЗВАНИЕ ПАПКИ])
      2. Установить параметры доступа (chmod -R 755 [НАЗВАНИЕ ПАПКИ])
      3. Написать скрипт который будет запускать программу (например example.py)
         и поместить этот скрипт в директорию /usr/bin (sg_autostart.sh - пример скрипта)
      4. Добавить этот скрипт в автозапуск (В Lubuntu это делается в "Session settings").
         Команда, которая должна исполняться - "sudo sg_autostart.sh"
      5. Написать команду "visudo" и прописать внизу
         "[ИМЯ ПОЛЬЗОВАТЕЛЯ] ALL=(ALL:ALL) NOPASSWD:/usr/bin/sg_autostart.sh"
      ```
   </details>
### Пример программы:
```
from smart_gnomik import SmartGnomik

model_name = "vosk-model-small-ru-0.22" # Название модели, папка с моделью должна быть там же где и программа
activation_words = ['гном'] # Слово (слова) при произнесении которого активируется распознавание (типа "Окей гугл")

sg = SmartGnomik(model_name, activation_words)

# Можно поменять слова-активаторы
# sg.set_activation_words(activation_words)

# Можно поменять путь к библиотеке Tuya и другим библиотекам если они у вас не в папке "libs".
# sg.set_dir(r'/home/orangepi/Desktop/SmartGnomik/libs')

# Мигание после выполнения команды работает только на Orange Pi
# Модели: PC2, ZERO, ZEROPLUS2H5, ZEROPLUS2H3, PCPCPLUS, PRIME
# Если вашей модели нет в списке, то можете попробовать мигать встроенным светодиодом
# Для этого необходимо вызвать функцию без передачи названия модели и пина
sg.set_orangepi_LED(model="PC2", pin=7) 

ip = "192.168.0.1"
device_names = ["комп"] # КОМПьютер
mac_addr = "AA:BB:CC:DD:EE:FF"
username = "Username"
password = "top_secret_password"
pc = sg.set_pc(ip, device_names, mac_addr, username, password, port=22)
pc.add_command(action_words=["вкл"], command = 'turn_on')
pc.add_command(action_words=["выкл"], command = 'turn_off')
pc.add_command(action_words=["резаг"], command = 'reboot') #пеРЕЗАГрузи

ip = "192.168.0.2"
device_names = ["розет"] # РОЗЕТка
local_key = "Local_Key"
device_ID = "Device_ID"
tuya1 = sg.set_tuya_device(ip, device_names, local_key, device_ID)
tuya1.add_command(action_words=["вкл"], command = 'turn_on')
tuya1.add_command(action_words=["выкл"], command = 'turn_off')

esp1 = sg.set_web_device(ip="192.168.0.3", device_names=["ламп", "свет", "люст"]) #ЛЮСтра 1.128
esp1.add_command(action_words=["вкл"], web_request = 'turn_on')
esp1.add_command(action_words=["выкл"], web_request = 'turn_off')

esp2 = sg.set_ac(ip="192.168.0.4", device_names=["конд"]) # КОНДиционер
esp2.add_command(action_words=["вкл"], web_request = 'turn_on')
esp2.add_command(action_words=["выкл"], web_request = 'turn_off')

sg.start()
```

### Планы на будущее:
1. <details> 
      <summary>Добавить библиотеку в pip</summary>
  
      ```
      Это не было сделано сразу потому что есть зависимости которые необходимо устанавливать через apt.
      Pip не может это делать автоматически и я посчитал что пользователям будет проще загружать библиотеку
      напрямую с Github и запускать скрипт setup.sh который сам всё сделает.
      ```
2. Упростить написание сложных скриптов
3. Добавить возможность управлять устройствами из интернета

### Дополнительно:
- Перед запуском Bash-скриптов (.sh) необходимо давать им права на выполнение командой      
"chmod +x [НАЗВАНИЕ СКРИПТА]"
- Поддержать разработчика / Бесплатные инвестиционные лайфхаки: https://pomoex.ru
- Связаться со мной: mikesprogramms@gmail.com

### Проект использует:
[Vosk](https://github.com/alphacep/vosk-api) - для распознавания голоса      
[TuyaNet](https://github.com/ClusterM/tuyanet) - для взаимодействия с устройствами Tuya      
[PyWakeOnLAN](https://github.com/remcohaszing/pywakeonlan) и [Paramiko](https://github.com/paramiko/paramiko) - для управления компьютером      
Остальные зависимости можно посмотреть в файле setup.sh      
