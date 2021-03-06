# Лабораторная работа №1.
**Решение систем линейных алгебраических уравнений. Метод Гаусса**

*Требования:*
- Размерность n<=20 (задается из файла или с клавиатуры - по выбору конечного пользователя)
- Должно быть предусмотрено чтение исходных данных как из файла, так и ввод с клавиатуры.
- Должна быть реализована возможность ввода коэффициентов матрицы как с клавиатуры, так и из файла. Также предусмотреть случайные коэффициенты.

*Реализация:*
1. Вычисление определителя
2. Вывод треугольной  матрицы (включая преобразованный столбец В)
3. Столбец неизвестных
4. Столбец невязок

# Лабораторная работа №2
**1. Решение нелинейных уравнений. Метод хорд. Метод простой итерации**
**2. Решение систем нелинейных уравнений. Метод Ньютона**

*Требования:*
- Уравнения и системы задаются пользователем
- Графики решений нелинейных уравнений
- Одно уравнение решается разными методами одновременно. Вместе с этим демонстрируется разница в решениях (сравнение методов)
- График решения системы уравнений заданным методом

# Лабораторная работа №3. 
**Интегрирование. Метод прямоугольников**

*Требования:*
- Пользователь выбирает функцию, интеграл которой он хочет вычислить (3-5 функций), из тех, которые предлагает программа.
- В численный метод должен быть передан параметр-агрегат на подпрограмму вычисления значения функции в точке x.
- Пользователь задает пределы интегрирования и точность. 
- Для оценки погрешности использовать оценку Рунге.

**NOTE! Если нижний предел интегрирования >= верхнего предела - интеграл должен считаться корректно!**

*Реализация:*
1. Значение интеграла
2. Количество разбиений, на которое пришлось разбить
3. Полученную погрешность 

# Лабораторная работа №4
**Интерполирование кубическими сплайнами**

Для интерполяции необходимо подготовить 3-4 набора данных (в зависимости от функции).

Исходные данные должны быть подготовлены следующим образом:
1. Берем функцию
2. Берем точки x (точки необязательно упорядочены)
3. значение y получаем на основе данных выбранной функции

*Например: берем sin(x)*

* берем 3-4 точки на интервале 0 по 2π(шаг более или менее большой)
* берем 8-10 точек на интервале 0 по 2π (уменьшаем шаг)
* точки с предыдущего примера, только для одной точки изменяем значение y, например было 0.8, делаем -5, смотрим как ведет себя интерполяция.
* берем 8-10 точек на интервале 0 по 50π
* В итоге должны получить график, на котором одним цветом исходная функция (sin(x)), а другим цветом полученный график в результате интерполяции, и на графике должны быть отмечены сами точки (узлы) интерполяции.

*Требования:*
* Интерполяционный график должен пройти через исходные эти точки.
* Программа должна позволять найти значение y (отдельное поле) для любого введенного x
(рассчитывается на основе построенного интерполяционного многочлена).

# Лабораторная работа №5
**Решение обыкновенных дифференциальных уравнений. Метод Эйлера**

* Задается обыкновенное дифференциальное уравнение вида y’ + f(x,y) = 0 , пользователь задает начальные условия (x0, y0), конец отрезка и точность.
* Программа сама вычисляет шаг в зависимости от точности для нахождения массива значений x и y.
* Используется интерполирование кубическими сплайнами. 

# Лабораторная работа №6
**Интегрирование по прямоугольной области**

1. Метод ячеек
2. Приведение двойного интеграла к повторному интегралу:
    *  вычисление определенного интеграла методом трапеций
    *  вычисление определенного интеграла методом левых прямоугольников
    *  вычисление определенного интеграла методом средних прямоугольников
    *  вычисление определенного интеграла методом правых прямоугольников
