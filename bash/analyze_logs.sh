#!/bin/bash

# Генерация log файла
cat <<EOL > access.log
192.168.1.1 - - [28/Jul/2024:12:34:56 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.2 - - [28/Jul/2024:12:35:56 +0000] "POST /login HTTP/1.1" 200 567
192.168.1.3 - - [28/Jul/2024:12:36:56 +0000] "GET /home HTTP/1.1" 404 890
192.168.1.1 - - [28/Jul/2024:12:37:56 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.4 - - [28/Jul/2024:12:38:56 +0000] "GET /about HTTP/1.1" 200 432
192.168.1.2 - - [28/Jul/2024:12:39:56 +0000] "GET /index.html HTTP/1.1" 200 1234
EOL

# Инициализация отчета
report_file="report.txt"
echo "Отчет о логе веб-сервера" > $report_file
echo "========================" >> $report_file

# Подсчет общего количества запросов
total_requests=$(wc -l < access.log)
echo -e "Общее количество запросов:\t$total_requests" >> $report_file

# Подсчет количества уникальных IP-адресов с использованием awk
unique_ips=$(awk '{print $1}' access.log | sort | uniq | wc -l)
echo -e "Количество уникальных IP-адресов:\t$unique_ips" >> $report_file

# Подсчет количества запросов по методам с использованием awk
echo "Количество запросов по методам:" >> $report_file
awk '{print $6}' access.log | tr -d '"' | sort | uniq -c | sort -nr >> $report_file

# Поиск самого популярного URL с использованием awk
most_popular_url=$(awk '{print $7}' access.log | sort | uniq -c | sort -nr | head -n 1)
echo "Самый популярный URL:" >> $report_file
echo "$most_popular_url" >> $report_file

# Уведомление пользователя о создании отчета
echo "Отчет сохранен в файл $report_file"