#!/bin/bash
# Подсчёт строк с уровнем ERROR по всем файлам журналов

total=0
max=0
max_file=""

for f in data/*.log; do
    count=$(grep -c "ERROR" "$f")
    echo "$f: $count"
    total=$((total + count))
    if [ "$count" -gt "$max" ]; then
        max=$count
        max_file="$f"
    fi
done

echo "-----"
echo "Всего ERROR: $total"
echo "Больше всего ошибок в файле: $max_file ($max)"
