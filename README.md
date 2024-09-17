# SmartGnomikLib
### Smart Home Controller

Библиотека для голосового управления умными устройствами.      
В качестве устройства-контроллера можно использовать Orange Pi или Raspberry Pi.

### С её помощью можно управлять:
- Любыми устройствами управляемыми с помощью GET-запросов      
  (например самодельными устройствами на ESP8266/ESP32)
- Устройствами совместимыми с платформой Tuya
- Компьютером

Образ настроенной ОС с настроенной программой для Orange Pi PC2 (и совместимых с ней плат): https://drive.google.com/file/d/1bjumnH2Hv2xlWecRSoOOCXUW6J5NqSU4      
Хочу отметить, что предустановленная программа может быть не последней версии.

### Создание карты памяти и подготовка ОС:
1. <details> 
      <summary>Скачивание дистрибутива Armbian или другой ОС</summary>
      - Голая Armbian 20.08 как у меня: https://drive.google.com/file/d/1FFzEcmnzOcK9rwSuBZPOyZdQ0BdvRMhi
   </details>
2. <details> 
      <summary>При необходимости: установка графической оболочки</summary>
      - Если скачали ОС без графической оболочки, то для удобства можете её установить, прописав команды: "apt update" и "apt install lubuntu-desktop -y"
   </details> 
3. <details> 
      <summary>Включение микрофона</summary>
      - Если не работает микрофон на OrangePi, то пропишите "alsamixer", нажмите F4, стрелками выберите микрофон и нажмите пробел чтобы его включить.
      Если там есть два микрофона, можете включить оба. Потом нажимаете CTRL+S чтобы сохранить настройки и CTRL+C чтобы закрыть программу.
   </details>
4. <details> 
      <summary>Проверка микрофона</summary>
      - Для проверки микрофона можете подключить наушники к OrangePi и ввести в терминал "arecord | aplay", звук с микрофона будет проигрываться в наушниках.
   </details>
5. <details> 
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
1. <details> 
      <summary>Настройка мигания светодиода</summary>
  
      ```
      Для управления GPIO контактами (и мигания светодиодом) программа должна иметь root-доступ.
      Поэтому по-хорошему нужно:
      1. Сделать root владельцем всей папки (chown -R root [НАЗВАНИЕ ПАПКИ])
      2. Установить параметры доступа (chmod -R 755 [НАЗВАНИЕ ПАПКИ])
      3. Написать скрипт который будет запускать программу на Питоне и поместить этот скрипт в директорию /usr/bin (sg_autostart.sh - пример скрипта)
      4. Добавить этот скрипт в автозапуск (В Lubuntu это делается в "Session settings"). Команда, которая должна исполняться - "sudo sg_autostart.sh"
      5. Написать команду "visudo" и прописать внизу "[ИМЯ ПОЛЬЗОВАТЕЛЯ] ALL=(ALL:ALL) NOPASSWD:/usr/bin/sg_autostart.sh"
      ```
   </details>
   
2. 


