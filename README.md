# Задача
Реализуйте алгоритм перемешивания списка.

# Решение
В принципе у модуля `random` есть метод `shuffle`, который перемешивает список.

Но, как мне показалось, необходимо было создать свой метод перемешивания.

В ходе решения задачи было создано два метода.
+ метод создания и заполнения списка. Для дальнейшего удобства сравнения с изначальным списком заполнил просто рядом натуральных чисел от 0 до `num`
+ собственно метод перемешивания списка. Принцип работы: случайным образом выбираются два индекса и значения элементов с этими индексами меняются местами с помощью временной переменной `temporary`. Так как это только одна случаная замена, то этот код поместил в цикл, где количество итераций определяются переменной `depth_shuffle`. По сути это глубина перемешивания.

Код не исключает возможность замены элемента на самого себя, поэтому отдельная замена может не внести какие-либо изменения в список. Также необходимо учесть, что есть вероятность, что перенесенное значение элемента в определенный момент может вернуться на свое изначальное место.

У `depth_shuffle` есть верхняя граница значений, зависящая в первую очередь от количества элементов в списке, после которой не имеет смысла увеличивать значение этой переменной. К примеру для списка с 10 элементами нет разницы будет ли глубина перемешивания 100 или 1000, он будет одинаково хорошо перемешан.