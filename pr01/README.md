# Практическая работа №1. Установка Linux и знакомство с терминалом (вариант A)

## Цель работы
Развернуть рабочее окружение и научиться выполнять команды в терминале Linux.

## Запуск
Все команды выполнены в Ubuntu (WSL2). Установка пакетов:

    sudo apt update && sudo apt install -y git python3 build-essential

## Результат
Вывод команд whoami, pwd, uname -a, lsb_release -a:

$ whoami
akmat

$ pwd
/home/akmat/ubuntu-practice/pr01

$ uname -a
Linux akm 6.18.33.2-microsoft-standard-WSL2 #1 SMP PREEMPT_DYNAMIC Thu Jun 18 21:54:43 UTC 2026 x86_64 GNU/Linux

$ lsb_release -a
Distributor ID:	Ubuntu
Description:	Ubuntu 26.04.1 LTS
Release:	26.04
Codename:	resolute

Файл about.txt создан командой echo, вторая строка добавлена через >>. Содержимое (cat):

Первая строка файла about.txt
Вторая строка, добавлена через >>

Вывод ls -la about.txt:

-rw-r--r-- 1 akmat akmat 107 Oct 29 16:28 about.txt

## Столбцы ls -la
1. Тип файла и права (первый символ: - файл, d каталог; дальше права владельца, группы, остальных: r чтение, w запись, x запуск).
2. Число жёстких ссылок на файл.
3. Владелец файла.
4. Группа файла.
5. Размер в байтах.
6. Дата и время последнего изменения.
7. Имя файла.

## Выводы
Я развернул Ubuntu, освоил базовые команды, перенаправление вывода (> и >>) и сдачу работ через git.
