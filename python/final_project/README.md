#### Программа для подсчета тегов на выбранной web-странице
Программа подсчитывает количество html-тегов(как общее кол-во, так и кол-во по каждому тегу) на выбранной странице, выводит результат в консоль, а также осуществляет запись в лог файл и помещает лог-файл в S3-бакет AWS

Как использовать:

Программа принимает три аргумента в следующем формате:
 - Веб страница, например https://google.com
 - Имя лога
 - Имя S3-бакета в AWS для сохранения лога
```buildoutcfg
python tagcount.py https://google.com log1.log testbucket
```
