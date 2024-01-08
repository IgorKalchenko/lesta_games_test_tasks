# Тестовое задание для Lesta Games

## Задание №1

<details>
  <summary>Условие</summary>
  На языке Python написать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций. 
  
  Пример: 
  
  def isEven(value):
  
        return value % 2 == 0
</details>

В качестве альтернативного подхода мы можем использовать битовые операторы: они позволят проверить, какой бит на конце у числа:
если 0 -> чётное, если 1 -> нечетное.
В данной реализации используем оператор &.
Функция вернёт True, если число чётное и False, если нечётное.

Плюсы подхода:
- скорость, битовые операции будут выполняться быстрее, чем классическое деление
Минусы:
- для отрицательных чисел не будет работать в случае применения метода вычисления обратный код (one's complement)
- метод взятия остатка от деления на 2 (%) более понятен на начальном уровне

Код: [ссылка](https://github.com/IgorKalchenko/lesta_games_test_tasks/blob/main/task_1_lesta.py)

## Задание №2

<details>
  <summary>Условие</summary>
  На языке Python написать минимум 2 класса, реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.
  
  Оценивается:
  
  - Полнота и качество реализации
  - Оформление кода
  - Наличие сравнения и пояснения по быстродействию
</details>

## Задание №3

<details>
  <summary>Условие</summary>
  На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить, почему вы считаете, что функция соответствует заданным критериям.
</details>