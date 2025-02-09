(matrices)=
# Матрицы

## Определение

Матрица -- это математический объект, представляющий собой прямоугольную таблицу чисел.

У каждой матрицы есть размер, который характеризуется двумя числами -- количеством строк и количеством столбцов. Матрицу, состоящую из $n$ строк $m$ столбцов будем называть матрицей размера $n \times m$. Пространство вещественных матриц $n \times m$ обозначается $\mathbf{R}^{n \times m}$. Мы будем рассматривать матрицу либо как набор $n$ вектор-строк, либо как набор $m$ вектор-столбцов.

**Замечание**: Вектор-строку из $n$ элементов можно рассматривать как матрицу размера $1 \times n$, а аналогичного размера вектор-столбец -- как матрицу размера $n \times 1$.

Рассмотрим произвольную матрицу $\mathbf{A}$:

$$
\mathbf{A} = \begin{pmatrix} a_{11} & a_{12} & ... & a_{1m} \\ a_{21} & a_{22} & ... & a_{2m} \\ ... & ... & ... & ... \\ a_{n1} & a_{n2} & ... & a_{nm} \end{pmatrix}
$$

Элемент матрицы $\mathbf{A}$, стоящий на пересечение строки $i$ и столбца $j$ будем обозначать $a_{ij}$.

В машинном обучении часто приходится иметь дело с матрицей объекты-признаки. Объекты, как и признаки -- это набор числовых характеристик (точки в многомерном пространстве), которые обычно рассматриваются как векторы.

## Операции с матрицами

Аналогично векторным операциям, для матриц определены операции **сложения** и **умножения на число**:

- сложение:

$$
\mathbf{A} + \mathbf{B} = \begin{pmatrix} a_{11} & a_{12} & ... & a_{1m} \\ a_{21} & a_{22} & ... & a_{2m} \\ ... & ... & ... & ... \\ a_{n1} & a_{n2} & ... & a_{nm} \end{pmatrix} + \begin{pmatrix} b_{11} & b_{12} & ... & b_{1m} \\ b_{21} & b_{22} & ... & b_{2m} \\ ... & ... & ... & ... \\ b_{n1} & b_{n2} & ... & b_{nm} \end{pmatrix} = \begin{pmatrix} a_{11} + b_{11} & a_{12} + b_{12} & ... & a_{1m} + b_{1m} \\ a_{21} + b_{21} & a_{22} + b_{22} & ... & a_{2m} + b_{2m} \\ ... & ... & ... & ... \\ a_{n1} + b_{n1} & a_{n2} + b_{n2} & ... & a_{nm} + b_{nm} \end{pmatrix}
$$

- умножения матрицы на число (скаляр):

$$
\lambda \cdot \mathbf{A} = \lambda \cdot \begin{pmatrix} a_{11} & a_{12} & ... & a_{1m} \\ a_{21} & a_{22} & ... & a_{2m} \\ ... & ... & ... & ... \\ a_{n1} & a_{n2} & ... & a_{nm} \end{pmatrix} = \begin{pmatrix} \lambda \cdot a_{11} & \lambda \cdot a_{12} & ... & \lambda \cdot a_{1m} \\ \lambda \cdot a_{21} & \lambda \cdot a_{22} & ... & \lambda \cdot a_{2m} \\ ... & ... & ... & ... \\ \lambda \cdot a_{n1} & \lambda \cdot a_{n2} & ... & \lambda \cdot a_{nm} \end{pmatrix}
$$

- транспонирование (строки и столбцы меняются местами):

$$
\mathbf{A} = \begin{pmatrix} a_{11} & a_{12} & ... & a_{1m} \\ a_{21} & a_{22} & ... & a_{2m} \\ ... & ... & ... & ... \\ a_{n1} & a_{n2} & ... & a_{nm} \end{pmatrix} \rightarrow \mathbf{A}^{T} = \begin{pmatrix} a_{11} & a_{21} & ... & a_{m1} \\ a_{12} & a_{22} & ... & a_{m2} \\ ... & ... & ... & ... \\ a_{1n} & a_{2n} & ... & a_{mn} \end{pmatrix}
$$

Но наибольший интерес представляет операция умножения матриц, которая определяется не самым интуитивным способом.

Рассмотрим операцию скалярного произведения как умножение матрицы размера $1 \times n$ (вектор-строка) на матрицу размера $n \times 1$ (вектор-столбец). Результатом данной операции получается матрица размера $1 \times 1$ (скаляр).

Таким образом для получения значения $c_{11}$ результирующей матрицы $\mathbf{С}$ мы скалярно умножили 1-ю строку $\mathbf{a_{1:}}$ матрицы $\mathbf{A}$ (вектор) на 1-й столбец $\mathbf{b_{:1}}$ матрицы $\mathbf{B}$ (вектор).

Из примере выше мы можем прийти к следующим заключениям:
- для умножения матриц необходимо, чтобы количество столбцов первой матрицы было равно количеству строк второй, иначе нельзя посчитать скалярное произведение
- операция умножения матриц не является коммутативной, то есть $\mathbf{A} \mathbf{B} \not = \mathbf{B} \mathbf{A}$

Развивая логику примера выше мы можем перейти к определению операции умножения матриц. Рассмотрим матрицы $\mathbf{A} \in \mathbf{R}^{n \times p}$ и $\mathbf{B} \in \mathbf{R}^{p \times m}$. Результатом произведения этих матриц будем матрица $\mathbf{A} \mathbf{B} = \mathbf{C} \in \mathbf{R}^{n \times m}$, где значение $c_{ij}$ получится путем скалярного произведения $i$-й строки $\mathbf{a_{i:}}$ матрицы $\mathbf{A}$ (вектор) на $j$-й столбец $\mathbf{b_{:j}}$ матрицы $\mathbf{B}$ (вектор):

$$
c_{ij} = \mathbf{a_{i:}} \cdot \mathbf{b_{:j}} = a_{i1}  b_{1j} + a_{i2}  b_{2j} + ... + a_{ip} b_{pj}
$$

**Замечание 1**: В результате умножения квадратных матриц размера $n \times n$ получается квадратная матрица того же размера.

**Замечание 2**: Частными случаями матричного умножения являются операции умножения вектор-строки на матрицу и матрицы на вектор-столбец, в результате которых получаются вектор-строка и вектор-столбец соответственно.

Рассмотрим пример, почему удобно представлять операцию умножения матриц именно таким образом. Пусть имеется система линейных уравнений:

$$
\begin{cases}
    a_{11} x_{1} + a_{12} x_{2} + ... + a_{1m} x_{m} = b_{1} \\
    a_{21} x_{1} + a_{22} x_{2} + ... + a_{2m} x_{m} = b_{2} \\
    ... \\
    a_{n1} x_{1} + a_{n2} x_{2} + ... + a_{nm} x_{m} = b_{n}
\end{cases}
$$

Представим данную систему в матричном виде:

$$
\mathbf{A} \mathbf{x} = \mathbf{b} \rightarrow \begin{pmatrix} a_{11} & a_{12} & ... & a_{1m} \\ a_{21} & a_{22} & ... & a_{2m} \\ ... & ... & ... & ... \\ a_{n1} & a_{n2} & ... & a_{nm} \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ ... \\ x_{m} \end{pmatrix} = \begin{pmatrix} b_{1} \\ b_{2} \\ ... \\ b_{n} \end{pmatrix}
$$

## Норма матрицы

Понятие матричной нормы несколько сложнее, чем векторной. Обычно принято рассматривать так называемые **операторные нормы**. Такая норма показывает насколько максимально растягивается произвольный вектор $\mathbf{x}$ при отображении $y = \mathbf{Ax}$. Формально операторная норма определяется следующим образом:

$$
\lVert \mathbf{A} \rVert_{p} = \sup_{\mathbf{x} \neq 0}\frac{\lVert \mathbf{Ax} \rVert_{p}}{\lVert \mathbf{x} \rVert_{p}}
$$

Существует множество матричных норм, но наиболее полезной является **спектральная норма**. Опуская математические выкладки, можно показать, что спектральная норма равна максимальному собственному числу матрицы $\mathbf{A}^T\mathbf{A}$:

$$
\lVert \mathbf{A} \rVert_{2} =\sqrt{\lambda_{max}(\mathbf{A}^T\mathbf{A})}
$$

Про собственные числа поговорим позже, а пока вернемся к нормам. Иногда также рассматривают **поэлементные нормы** матриц. Такая норма определяется тем же образом, что и для векторов. Наиболее распространенной из данного вида является **Евклидова норма**, она же **норма Фробениуса**:

$$
\lVert \mathbf{A} \rVert_{F} = \sqrt{\sum_{i}\sum_{j}a_{ij}^2}
$$

## Ранг матрицы

Вспомним, что матрицу можно рассматривать либо как набор вектор-строк, либо как набор вектор-столбцов, а для набор векторов определенно понятие линейной независимости.

Таким образом мы приходим двум следующим понятиям:
- **строчный ранг** матрицы -- это максимальное число линейно независимых строк (вектор-строк)
- **столбцовый ранг** матрицы -- это максимальное число линейно независимых столбцов (вектор-столбцов)

Тут мы можем задаться вопрос о том, равны ли эти ранги между собой, и если равны, то при каких условиях, и на помощь нам приходит **фундаментальная теорема «о ранге матрицы»**, которая говорит, что ранг, посчитанный по строкам всегда равен рангу, посчитанному по столбцам. Поэтому обычно говорят просто о ранге матрицы.

## Линейные преобразования

В рамках школьной программы все знакомы с понятием функции. Функция -- это соответствием между элементами двух множеств.

Например, линейная функция вида $y = f(x) = kx + b$ отображает элементы множества вещественных чисел $x \in \mathbf{R}$ в себя $y \in \mathbf{R}$ :

$$
f: \mathbf{R} \rightarrow \mathbf{R}
$$

Парабола $y = f(x) = x^2$ отображает элементы множества вещественных чисел $x \in \mathbf{R}$ во множество неотрицательных вещественных чисел $y \in \mathbf{R}^{+} \cup \{0\}$ :

$$
f: \mathbf{R} \rightarrow \mathbf{R}^{+} \cup \{0\}
$$

Среди всего множества функций есть определенный класс функций, называемых линейными. Этот класс является самым простым среди множества всех функций. Основным свойством линейных функций является пропорциональность $x$ и $y$: изменение значения функции $y$ пропорционально изменению значения аргумента $x$. Графиком линейной функции является прямая.

Обобщая идею линейных функций на матрицы и вектора мы можем прийти к понятиям **линейных отображений** и **линейных преобразований**.

Линейное отображение -- это обобщение линейной функции, которое принимает на вход вектор и возвращает вектор. Вектор может быть как той же размерности, так и другой.

Формально, линейное отображение -- это отображение множества элементов одного векторного пространства $V$ в другое $W$

$$
f: V \rightarrow W ,
$$
удовлетворяющее так называемым [условиям линейности](https://ru.wikipedia.org/wiki/Линейное_отображение#cite_note-_5e0d87b5e4a6def2-2).

Если $V$ и $W$ — это одно и то же векторное пространство, то $f$ называют не просто линейным отображением, а **линейным преобразованием**.

Отображения и преобразования удобно рассматривать как движение в векторном пространстве.

Ранее упоминалось, что при умножении вектора на матрицу мы получаем вектор, поэтому матрица задает преобразование, которое, если проверить условия линейности, является линейным. Соответственно, **матрица задает линейное отображение**.

Например, матрица $\mathbf{A} \in \mathbf{R}^{n \times m}$ задает преобразование из векторного пространства размерности $n$ в векторное пространство размерности $m$.

**Замечание 1**: Для того, чтобы матрица задавала линейное преобразование, она должна быть квадратной, т.к. в результате умножение вектора на квадратную матрицу его размерность не меняется. Таким образом вектор, как элемент векторного пространства, отображается в то же векторное пространство.

**Замечание 2**: Пусть имеются две матрицы $\mathbf{A} \in \mathbf{R}^{n \times p}$ и $\mathbf{B} \in \mathbf{R}^{p \times m}$. Умножив матрицу $\mathbf{A}$ на матрицу $\mathbf{B}$ мы получим матрицу $\mathbf{C} \in \mathbf{R}^{n \times m}$. Матрица $\mathbf{C}$ задает линейное отображение, равное последовательному применению отображений, задаваемых матрицами $\mathbf{A}$ и $\mathbf{B}$. Таким образом операция умножения матриц имеет простую интерпретацию - последовательное применение линейных отображений.

Рассмотрим некоторые примеры линейных преобразований на плоскости, задаваемых матрицами размера $2 \times 2$:

- Вращение / поворот:
    - на 90 градусов против часовой стрелки: $\mathbf{A} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$
    - на угол $\theta$ против часовой стрелки: $\mathbf{A} = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$
- Отражение:
    - относительно оси $x$: $ \mathbf{A} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$
    - относительно оси $y$: $\mathbf{A} = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$
    - относительно линии, образующей угол $\theta$ с началом координат: $\mathbf{A} = \begin{pmatrix} \cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta \end{pmatrix}$
- Масштабирование:
    - в 2 раза по всем направлениям: $\mathbf{A} = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$
- Проекция:
    - на ось $y$: $\mathbf{A} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$

## Обратная матрица

Рассмотрим особую матрицу линейного преобразования, которая переводит каждый вектор сам в себя, т.е. никак его не изменяет. Данное преобразование задается так называемой **единичной матрицей**:

$$
\mathbf{E} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
$$

Произведение любой матрицы / вектора и единичной матрицы подходящего размера равно самой матрице / вектору (аналог единицы для операции умножения чисел):

$$
\mathbf{A} \mathbf{E} = \mathbf{E} \mathbf{A} = \mathbf{A}
$$

Появление такого элемента в пространстве вещественных матриц наводит на мысль о том, что для каждой матрицы должен существовать обратный элемент:

$$
\mathbf{A} \mathbf{A}^{-1} = \mathbf{A}^{-1} \mathbf{A} = \mathbf{E}
$$

**Замечание**: Аналогично операции умножения чисел, если $a \cdot 1 = 1 \cdot a = a$, то существует $a^{-1}$, такой, что $a \cdot a^{-1} = a^{-1} \cdot a = 1$.

Теория линейной алгебры говорит о том, что обратная матрица существует только для **невырожденных квадратных матриц**, строки и столбцы которых линейно независимы.

Те линейные преобразования, которые были приведены в примерах выше задаются невырожденными квадратными матрицами, поэтому для них существуют обратные преобразования, которые тоже будут линейными.

Например, обратными к преобразованиям вращения / поворота, отражения и масштабирования являются эти же преобразования: вращение / поворот, отражение и масштабирование соответственно.

**Замечание**: Существуют разные алгоритмы нахождения обратной матрицы, которые не будут нами рассматриваться, но с ними можно ознакомиться [здесь](https://ru.wikipedia.org/wiki/Обратная_матрица).

Будем назвать линейное преобразование **вырожденным**, если оно задается вырожденной матрицей.

Соответственно, возникает вопрос, чем же так особенны вырожденные линейные преобразования, если для них не существует обратного преобразования?

Невырожденное линейное преобразование устанавливает взаимно-однозначное соответствие между входными и выходными векторами. Вырожденное преобразование этим свойством не обладает.

Это связано с тем, вырожденные линейные преобразования переводят некоторые ненулевые вектора в нулевые (для невырожденных линейных преобразований только нулевой вектор переходит в нулевой):

$$
\mathbf{A} \mathbf{x} = 0, \mathbf{x} \not ={\begin{pmatrix} 0 \\ 0 \\ ... \\ 0 \end{pmatrix}}
$$

В связи с этим одному выходному вектору (нулевому) соответствует несколько входных векторов, поэтому не существует обратного преобразования.

## Определитель

Введем еще одно из ключевых понятий линейной алгебры -- **определитель**.

Определитель -- это скалярный показатель (число) **квадратной матрицы** $f: \mathbf{R}^{n \times n} \rightarrow \mathbf{R}$, который позволяет охарактеризовать некоторые свойства этой матрицы и линейного преобразования, заданного этой матрицей.

Определитель матрицы $\mathbf{x}$ обозначается как: $\det(\mathbf{A}) = |\mathbf{A}| = \Delta(\mathbf{A})$

Формально понятие определителя может быть введено несколькими способами:
- через перестановки
- через свойства определителя
- геометрически

**Замечание**: В данной лекции не будет рассказано, как посчитать определитель. Ознакомиться с алгоритмом расчета и формальным выводом определителя можно по [ссылке](https://ru.wikipedia.org/wiki/Определитель).

Определитель обладает следующими важными свойствами -- он **равен нулю** тогда и только тогда, когда **строки (столбцы) матрицы линейно зависимы**.

Из этого можно сделать следующие выводы:
- матрица вырожденная тогда и только тогда, когда ее определитель равен 0
- линейное преобразование вырожденное тогда и только тогда, когда определитель матрицы, задающей данное преобразование, равен 0
- если определитель матрицы равен 0, то для данной матрицы не существует обратной

Существуют эффективные алгоритмы вычисления определителя квадратной матрицы, которые позволяют проверять, является матрица вырожденной.

## Собственные числа и векторы

Для некоторых линейных преобразований существуют такие векторы, которые после данного преобразования либо растягиваются, либо сжимаются (тот же вектор, умноженный на некоторое число). Такие векторы называются **собственными векторами** линейного преобразования, а числа, на которые данные векторы умножаются -- **собственными значениями**.

Рассмотрим произвольную матрицу линейного преобразования $\mathbf{A}$. Формально понятия собственных векторов и собственных значений вводятся через следующее равенство: $
\mathbf{A} \mathbf{x} = \lambda \mathbf{x}$

Векторы $\mathbf{x}$, удовлетворяющие данному равенству являются собственными векторами линейного преобразования $\mathbf{A}$, а соответствующие данным векторам значения $\lambda$ -- собственными числами.

Линейное преобразование может как не иметь собственных векторов (например, поворот в двумерном пространстве), или иметь $n$ собственных векторов с различными собственными значениями.

Собственные числа и собственные значения играют большую роль в линейной алгебре, так как многие соотношения, связанные с линейными преобразованиями, существенно упрощаются в системе координат, построенной на базисе из собственных векторов линейного преобразованиями.

Множество собственных значений линейного преобразованиями (**спектр оператора**) характеризует важные свойства оператора без привязки к какой-либо конкретной системе координат.

Также собственные векторы используются в Методе Главных Компонент, который предназначен для уменьшения размерности данных с потерей наименьшего количества информации.

## Что мы узнали?

 - Определение матрицы
 - Операции с матрицами
 - Норма матрицы
 - Ранг матрицы
 - Линейные преобразования
 - Обратная матрица
 - Определитель матрицы
 - Собственные числа и векторы матрицы
