#!/usr/bin/env python
# coding: utf-8

# (mll1)=
# 
# # Машинное обучение как пазл
# 
# ## Введение
# 
# Мы продолжаем вводную часть нашего курса и переходим к машинному обучению. Если тема для вас хорошо знакома, можете пропустить этот блок, при желании можно пройти  [этот тест](http://foo) для определения достаточности уровня знаний. Тест можно проигнорировать, если вы не знакомы с машинным обучением и для вас выглядят магией такие вещи как автоматическая детекция лиц на фото или определение тональности отзыва на товар.  
# 
# Про машинное обучение, конечно, уже много всего написано, есть и немало неплохих курсов, сочетающих как теорию, так и практику. Но все же теория в этой области еще не догоняет практику, мы пока не понимаем, "почему оно работает", а гарантии обобщающей способности алгоритмов (т.е. гарантии того, что модель машинного обучения будет работать на новых данных) в теории даются только для очень простых моделей. Таким образом, работа со сложными моделями остается своего рода искусством с примесью математики, инженерии и просто следования хорошим практикам, выработанным, как правило, в корпорациях или академическом сообществе.
# 
# В этой лекции мы примем сторону практики и расскажем про задачи машинного обучения как некоторый пазл (или лего, кому что ближе) -- меняя разные кусочки, мы будем получать разные прикладные задачи/сценарии/модели применения машинного обучения. Для иллюстрации такое описание мы сопроводим 3-мя примерами:
# 
#  - задача рекомендации контента и градиентный бустинг
#  - автоматическая оценка читаемости научной статьи и BERT
#  - детекция симптомов COVID-19 на рентгенограммах и YOLO
# 
# В этой лекции мы не опишем подробно, что это за модели машинного обучения (градиентный бустинг, BERT, YOLO), но зато покажем, что сценарии их применения в разных задачах (анализ табличных данных, текстов, изображений) похожи.
# 
# 
# ```{note}
# В этой лекции мы почти не будем говорить о математике. И изложенный взгляд на машинное обучение как ремесло, вполне вероятно, вызовет критику со стороны специалистов в области статистики, эконометрики и теории машинного/статического обучения. Мы осознаем эти риски и тем не менее рассказываем о машинном обучении именно как о ремесле. Акцент в курс делается на квантовые вычисления и квантовое машинное обучение, и в этой лекции мы опишем задачи "классического" машинного обучения на том уровне, чтоб просто было понятно, как это переносится на квантово-классические вариационные схемы и прочие алгоритмы, о которых пойдет речь далее в курсе. При этом строгость изложения материала тоже может немного пострадать.
# ```
# 
# 
# ## Составляющие части задачи машинного обучения
# 
# Выделим следующие компоненты ("пазлы"), которые просматриваются во многих разных задачах машинного обучения:
# 
# - Целевой признак
# - Модель
# - Данные
# - Функция потерь
# - Решатель
# - Схема валидации и метрика качества
# 
# По ходу изложения будем обсуждать упомянутые примеры задач машинного обучения.
# 
# ### Целевой признак
# 
# Есть задачи, в которых машинное обучение не нужно, а достаточно экспертных знаний. По закону Ома, известно что напряжение пропорционально силе тока и электрическому сопротивлению, и вряд ли захочется предсказывать напряжение в сети каким-то другим образом, кроме как применением закона Ома. То же самое можно сказать про многие другие физические явления.
# 
# Однако, для очень многих явлений вокруг нет хорошего теоретического объяснения или достаточных экспертных знаний. У нас нет "формулы", которая описала бы, как поставленный лайк к посту в соцсети, возврат кредита, клик по рекомендации товара или локализация заразы в конкретной части легких зависят от прочих факторов. В таких случаях мы можем приблизить такую неизвестную нам формулу с помощью машинного обучения.
# 
# В идеале с помощью машинного обучения мы хотели бы предсказывать какое-то событие, явление или процесс так, чтоб от этого была польза: прибыль компании/клиентов, если речь о бизнес-проекте, или новые знания, если это исследовательский проект. При этом напрямую это сделать вряд ли получится, и надо определить целевой признак, которая, как мы считаем, будет связана с целевым событием/явлением. Звучит абстрактно, и дать строгое определение таких событий, явлений или процессов вряд ли получится. Поэтому сразу перейдем к примерам.
# 
# ```{note}
# Перед этим только небольшое замечание, что потребовав наличие целевого признака, мы ограничилиcь рассмотрением задач обучения с учителем ([supervised learning](https://en.wikipedia.org/wiki/Supervised_learning)). Это все еще включает очень большой перечень типов задач машинного обучения, но не все.
# ```
# 
# **Пример 1. Рекомендация новостного контента**
# 
# Новостному порталу хочется понять, какой контент нравится пользователям и по каким ссылкам они будут кликать. Здесь _событием_ будет то, что пользователю нравится рекомендуемый контент.  
# 
# 
# ```{figure} /_static/mlblock/see_also.png
# :width: 600px
# :name: see_also
# 
# Блок "Читайте также" на новостном портале
# ```
# 
# Понятно, что нет возможности установить строгую зависимость такого события от прочих факторов. Поэтому мы определяем целевой признак: факт клика пользователя по показанной рекомендованной ссылке. Мы верим, что клик по ссылке связан с _событием_: если пользователю  нравится рекомендуемый контент, он/она перейдет по ссылке.
# 
# **Пример 2. Автоматическая оценка читаемости научной статьи**
# 
# Допустим, научному журналу хочется автоматически оценивать читаемость текста, чтобы знать, какие статьи можно сразу подавать на ревью, а какие лучше предварительно направить в сервис proofreading, где статья будет вычитана и поправлена носителем языка.
# 
# В идеале мы бы хотели предсказывать, "хорошо" ли написана статья или "плохо". Но это очень сложно определить формально, и потому есть много метрик читаемости текста, таких как [Automated readability index](https://en.wikipedia.org/wiki/Automated_readability_index) или [Flesch reading ease](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch_reading_ease), которые являются эвристиками и "приближают" то что мы имеем в виду под хорошо или плохо написанным текстом. Кстати, на момент написания это лекции на платформе Kagglе проходит [соревнование](https://www.kaggle.com/c/commonlitreadabilityprize/overview) по этой теме.
# 
# Небольшое лирическое отступление: во многом опыт спецалиста по машинному обучению сказывается в способности понять, когда это машинное обучение **не** требуется. Описанную задачу можно решить и без всякого машинного обучения. Можно замерить 5-10 метрик читаемости текста, разметить 100-200 статей вручную (желательно, чтоб это делали эксперты уровня редактора журнала, а еще и лучше бы иметь по 3 оценки на статью) и заключить, хорошо ли метрики читаемости коррелируют с оценками экспертов. Другой вариант -- попытаться малой ценой использоваться готовые решения, например, Grammarly.
# 
# Но если этого окажется недостаточно, придется подумать. Пока остановимся тут и еще раз подчеркнем, что определить читаемость текста напрямую -- невозможно, и мы это заменим на другой _Целевой признак_, например, на агрегированную метрику читаемости текста.
# 
# 
# **Пример 3. Детекция симптомов COVID-19 на рентгенограммах**
# 
# Последние пару лет мы видели бурное развитие методов глубокого обучение в приложениях к анализу медицинских данных, а в особенности это стало актуальным в симптомов COVID-эпоху.
# 
# Допустим, стоит задача определения аномалий на рентгенограммах грудной клетки. В идеале мы хотели мы сразу по таким изображениям обнаруживать симптомы симптомов COVID-19 у пациента. Но заголовок этого примера выдает желаемое за действительное, и, конечно, сразу по снимкам диагностировать не получится.  
# 
# ```{figure} /_static/mlblock/covid_detection_ct.png
# :width: 1000px
# :name: COVID_detection_ct
# 
# Пример данных [соревнования](https://www.kaggle.com/c/siim-COVID19-detection) по определению аномалий на рентгенограммах грудной клетки. [Источник](https://www.kaggle.com/andradaolteanu/siim-COVID-19-box-detect-dcm-metadata)
# ```
# 
# Поэтому в такой задаче надо аккуратно определить _Целевой признак_. В данном случае их несколько. Согласно [описанию источника данных](https://www.kaggle.com/c/siim-covid19-detection/data) соревнования, комитет врачей-радиологов проанализировал 6334 рентгенограмм и пометил их метками: 'Negative for Pneumonia' (нет пневмонии), 'Typical Appearance' (нормально), 'Indeterminate Appearance' (неразборчиво) и 'Atypical Appearance' (ненормально). Надо четко понимать, что возможности обученной модели будут ограничены имеющейся разметкой и поэтому заголовок "детекция симптомов COVID-19" слегка "желтоват", в реальности модель детекции сможет выделять участок изображения (bounding box) и помечать это вектором из 4-х значений, соответствующих описанным целевым признакам в обучающей выборке.
# 
# ```{figure} /_static/mlblock/covid_detection_prediction.png
# :width: 1000px
# :name: COVID_detection_prediction
# 
# Прогноз модели детекции, обученной на данных [соревнования](https://www.kaggle.com/c/siim-COVID19-detection) по определению аномалий на рентгенограммах грудной клетки. [Источник](https://www.kaggle.com/yujiariyasu/catch-up-on-positive-samples-plot-submission-csv)
# ```
# 
# ### Данные
# 
# Определение _Целевого признака_ неразрывно связано с имеющимися данными. Нет смысла определять целевой признак, который мы не можем измерить или по которому мы не можем собрать данные. Например, если новостной портал не логирует клики пользоватей, нет смысла задавать вопрос о том, нравятся ли пользователям показанные рекомендации -- для начала надо настроить сервисы для хранения кликов. Другой пример: вряд ли стоит пытаться предсказывать движения денежных активов в микросекундном диапазоне, если нет дорогостоящей инфраструкруты для сбора и обработки таких данных.
# 
# Но _Данные_ -- это, конечно, не только _Целевой признак_. Но и просто _признаки_, также в эконометрике называемые предикторами или независимыми переменными. С помощью _признаков_ как раз и получится предсказать _Целевой признак_, а хорошо или плохо -- об этом чуть далее.
# 
# Продумывание, сбор, и обработка  _признаков_ -- один из наиболее творческих аспектов работы специалистов по машинному обучению. Эта работа может включать в себя общение с представителями предметной области или бизнеса, клиентами, чтение научных статей, применение и более технических приемов, таких как порождение признаков из других признаков (feature engineering) или использование моделей для получения признаков (например, признаки изображения, полученные предобученной искусственной нейросетью).
# 
# **Пример 1. Рекомендация новостного контента**
# 
# В этой задаче, как правило, хорошо работают данные о поведении пользователей, попросту -- "клики". Обычно алгоритмы рекомендации хорошо работают при обучении на больших объемах данных, и поэтому большая часть проекта посвящена настройка хранилища данных и обработке потоковых событий (показ рекомендации, клик по рекомендации).
# 
# Если есть возможность собрать какие-то признаки пользователей (пол, возраст, указанные интересы) или рекомендуемого контента (темы новостей, представление текста новости "эмбеддингами"), эту информацию можно добавить в модель.
# 
# При достаточно хорошей подготовке данных задачу можно решить и без машинного обучения. Довольно сильным прототипом (baseline-решением), опять же, при достаточных объемах данных, моет быть просто сортировка контента по Click-through-Rate (CTR). Для каждой новости мы просто собираем статистику, сколько раз она была показана пользователю в качестве рекомендации и сколько раз по ней в итоге кликнули. Отношение кликов к показам и есть Click-through-Rate. Есть, конечно, детали -- что делать с "холодными" новостями, без накопленной стастистики для расчета CTR, что делать с clickbait-новостями, как фильтровать то, что нельзя показывать в качестве рекомендации. Но после решения этих проблем может оказаться, что просто сортировка по CTR -- уже неплохое решение.
# 
# **Пример 2. Автоматическая оценка читаемости научной статьи**
# 
# Допустим, научному журналу удалось договориться с сервисом proofreading и получить данные о том, какие статьи хорошо написаны и не требуют множества правок, а какие пришлось переписывать почти что с нуля. Эту информацию можно пытаться использовать для обучения модели, которая для заданного куска текста будет предсказывать, как сильно его нужно поправить.
# 
# Тут мы будем иметь дело с задачей из области NLP (Natural Language Processing) -- на входе будет просто текст (полный текст статьи или разбитый на параграфы) и по сути мы можем не придумывать _признаки_ вручную, а модель сама их извлечет, то есть выучит представление текста. _Целевым признаком_ при этом будет, например, какое-либо расстояние (скажем, Левенштейна) между оригинальным текстом и поправленным редактором. Таким образом, это будет задачей регрессии, в которой для текста предсказывается, как сильно его следует изменить.
# 
# Опять стоит отметить, что в такой задаче скорее всего нужно много  обучающих данных, чтобы описанный алгоритм хорошо заработал.
# 
# И еще стоит отметить, что задачи NLP зачастую пересекаются с лингвистикой, и это как раз такой пример. Вполне вероятно, что задачу можно решить без тоже машинного обучения и по-другому -- на основе правил-эвристик, разработанных в сотрудничестве с лингвистами. Эдакая версия Grammarly для работы с научными текстами.
# 
# 
# Но дальше в примере будем считать, что лингвистов в команде нет, простые метрики читаемости текста, описанные выше, работают плохо, и мы решаем задачу регрессии, то есть испольуем машинное обучение.
# 
# **Пример 3. Детекция симптомов COVID-19 на рентгенограммах**
# 
# В этой задаче ключевые данные для обучения модели -- это собственно изображение, рентгенограмма области грудной клетки и разметка, которая состоит из координат интересующей области изображения и типа области, в данном случае это одна из 4-х меток: 'Negative for Pneumonia' (нет пневмонии), 'Typical Appearance' (нормально), 'Indeterminate Appearance' (неразборчиво) и 'Atypical Appearance' (ненормально).
# 
# Конечно, у снимков есть разные метаданные, да и форматы медацинских данных обычно специфические, но нам для примера подойдет такое упрощение.
# 
# 
# 
# ### Модель
# 
# С моделированием знаком любой исследователь. Чтоб рассчитать минимальную толщину стекла вагона метро для защиты от птиц во время движения по открытым участкам, достаточно представить птицу цилиндром той же массы, и для данной задачи цилиндр будет подходящей моделью птицы.
# 
# Подобным же образом, в задачах машинного обучения с учителем _Модель_ приближает _Целевой признак_ и делает это с помощью _Данных_ и _Параметров_. (Параметры -- это неотъемлемая часть модели, и поэтому мы их не выносим как отдельный компонент задач машинного обучения).
# 
# Надо понимать, что предлагая модель, мы совершаем уже второе упрощение. Сначала, как мы говорили, _Целевой признак_ заменяет нам то, что мы реально хотим знать. А теперь, к тому же, мы заменяем целевой признак на его прогноз с помощью модели.
# 
# **Пример 1. Рекомендация новостного контента**
# 
# В задачах рекомендации есть классический алгоритм ALS (Alternative Least Squares), но можно задачу решить и как задачу ранжирования. Это может быть предпочтительно, поскольку можно использовать боевую лошадку машинного обучения на табличных данных -- градиентный бустинг.  Бустинг подходит для задач классификации, регрессии и ранжирования, и его можно использовать также и в описанной задаче.
# 
# Также, если бустинг уже используется в компании в других задачах, скорее всего получится безболезненно переиспользовать опыт подержки модели и соответствующей инфрастуктуры в "продакшене" вместо того, чтобы отдельно все это разрабатывать для ALS.
# 
# **Пример 2. Автоматическая оценка читаемости научной статьи**
# 
# Описанную задачу, опять же с оговорками про возможность альтернативного подхода без всякого машинного обучения, скорее всего хочется решать с помощью языковых моделей, основанных на трансформерах. В частности, в этой задаче имеет смысл использовать [SciBERT](https://github.com/allenai/scibert), предобученный как раз на научных текстах.
# 
# **Пример 3. Детекция симптомов COVID-19 на рентгенограммах**
# 
# Подходов к детекции объектов на изображениях немало, но по соотношению скорости и качества работы особенно хорошо себя зарекомендовала модель [YOLOv5](https://github.com/ultralytics/yolov5).
# 
# ### Функция потерь
# 
# Выбор функции потерь (loss function) зависит от конкретной задачи, и это вопрос, изучаемый в курсах машинного обучения. Функция потерь определена для объектов обучающей выборки и по сути говорит, насколько прогноз хорошо соответствует значению целевого признака.
# 
# Тут тонкий момент: примерно для того же нужны метрики качества, о которых речь пойдет ниже. Но функция потерь на практике чаще всего используется именно для того, чтоб задать цель обучения модели (для чего именно ей менять свои параметры) и также оценить, насколько хорошо модель обучилась, попросту, насколько хорошо она "сошлась".
# 
# В отличие от метрик качества, функции потерь вполне могут быть плохо интерпретируемыми, например как логистическая функция потерь (logloss), и на практике при разработке модели Data Scientist посмотрит на значение функции потерь всего несколько раз:
# 
# - при отладке модели стоит проверить, может ли она "переобучиться под мини-батч", то есть может ли она при обучении всего с парой десятком примеров добиться почти нулевого значения функции потерь. Это важно, чтоб понять, нет ли где-то ошибки в коде описания модели и хватает ли модели сложности (capacity), чтобы подстроиться под данные
# - чтобы избежать переобучения, стоит проверять (вручную или автоматически) значение функции потерь на отложенной выборке
# - еще значения функции потерь можно сравнивать для разных версий модели, чтоб понять, какая из них лучше обучилась
# 
# Заметим, что дизайн функции потерь под задачу, как и придумывание признаков -- порой интересный творческий процесс, а итоговая функции потерь, используемая для обучения модели может быть сложной, состоящей из нескольких более простых функций потерь.
# 
# Для примера, в задаче переноса стиля (style transfer), в классическом варианте задаются два изображения -- "контентное" и "стилевое" -- и генерируется третье изображение, которое похоже на в целом на "контентное" изображение, но по стилю -- на "стилевое." При этом функция потерь складывается из двух других:
# 
#  - одна -- content loss -- передает, насколько отличаются карты признаков (feature maps) генерируемого и "контентного" изображений
#  - вторая -- style loss -- соответственно передает, насколько похожи стили генерируемого и "стилевого" изображений. Делается это хитро, и за деталями лучше обратиться, например, к [лекции "Visualizing and Understanding"](https://www.youtube.com/watch?v=6wcs6szJWMY) стэнфордского курса cs231n.
# 
# ```{figure} /_static/mlblock/example_styletransfer.png
# :name: example_styletransfer.png
# :width: 800px
# 
# Пример решения задачи Neural Style Transfer из [задания 3](https://cs231n.github.io/assignments2020/assignment3/) стэнфордского курса cs231n.
# ```
# 
# Функция потерь может включать и много составляющих, больше двух, если мы хотим чтоб модель выучила разные аспекты задачи. К примеру, в [этой статье на Хабре](https://habr.com/ru/post/562064/) (уровень - продвинутый NLP) Давид Дале описывает дистилляцию нескольких больших NLP моделей для получения маленькой версии русскоязычной модели BERT. Маленький BERT по сути "учится" у больших моделей RuBERT, LaBSE, USE, и T5, и описание того, что маленькая модель должна уметь (предсказывать замаскированные токены по контексту, строить представления токенов подобно тому, как это делают большие модели, предсказывать правильный порядок токенов в предложении)-- это и есть составление сложной функции потерь.
# 
# 
# **Пример 1. Рекомендация новостного контента**
# 
# Задача свелась к задаче ранжирования на табличных данных, и тут можно использовать функцию потерь, которую можно оптимизировать с помощью градиентного бустинга (т.е. дифференцируемую, это важно), для задачи ранжирования. Например, [LambdaMART](https://www.microsoft.com/en-us/research/publication/from-ranknet-to-lambdarank-to-lambdamart-an-overview/).
# 
# **Пример 2. Автоматическая оценка читаемости научной статьи**
# 
# Тут задача свелась к задаче регрессии с текстовым входными данными, и можно использовать простую функцию потерь -- среднеквадратичную ошибку (Mean Squared Error).
# 
# **Пример 3. Детекция симптомов COVID-19 на рентгенограммах**
# 
# В задаче детекции объектов на изображениях, как правило, для каждого объекта модель выдает 4 числа – координаты окна (bounding box) и его длину и ширину, а также вектор с числами – оценки принадлежности данного региона к каждому из классов. Поэтому функция потерь, как правило, складывается из двух других:
# 
#  - Для сравнения предсказанного региона с реальным (согласно разметке в обучающей выборке) используется среднеквадратичная ошибка (Mean Squared Error).
#  - Для сравнения вектора оценок принадлежности региона к каждому из классов с реальным (согласно разметке в обучающей выборке) используется стандартная для задачи классификации функция потерь – кросс-энтропия.
# 
# 
# ```{figure} /_static/mlblock/object_detection_loss.png
# :name: object_detection_loss
# :width: 800px
# 
# Слайд стэнфордского курса cs231n про функцию потерь в задаче детекции объектов. [Источник](http://cs231n.stanford.edu/slides/2020/lecture_12.pdf).
# ```
# 
# ### Решатель
# 
# Когда мы определились с целевым признаком, обучающими данными, моделью и функцией потерь, мы наконец можем собственно обучать модель -- то есть менять ее параметры так, чтобы все лучше и лучше предсказывать целевой признак, что меряется с помощью функции потерь.
# 
# Наиболее часто используемых вариантов два:
# 
#  - явное решение (closed-form solution), в котором просто применится формула для получения оптимальных параметров модели. Тут _Решателем_ будет фреймворк, вычисляющий эту явно выписанную формулу, т.е. скорее всего производящий матричные умножения --  например, `NumPy`.
#  - оптимизация параметров модели градиентными методами оптимизации. Тут _Решателем_ будет алгоритм оптимизации и его конкретная реализация, например, в `PyTorch`
# 
# Самый известный пример первого варианта -- это явное решение задачи наименьших квадратов. Существует прямо конкретная формула, включающая в себя перемножение матриц и векторов и взятие обратной матрицы, и дающая оптимальный (по минимизации среднеквадратичной ошибки) вектор весов линейной модели при наличии, конечно, обучающей выборки. Получилась, что эта лекция вводная, без математических выкладок, поэтому не будем здесь приводить формулы без контекста, детали можно найти в любом классическом учебнике по статистике или машинному обучению или вкратце [в этой статье](https://habr.com/ru/company/ods/blog/322076/) на Хабре в разделе "Линейная регрессия".
# 
# Во всех трех примерах задач, которые мы попутно рассматриваем, и который сводятся к обучению градиентного бустинга, SciBERT и YOLO соответственно, нет явного решения, которое простой формулой выдало бы оптимальные параметры модели, и поэтому параметры подбираются с помощью методов оптимизации. В примере с градиентным бустингом "под капотом" -- алгоритм обучения деревьев решений, с ним можно познакомиться в [этой статье](https://habr.com/ru/company/ods/blog/322534/). А в двух других примерах обучаются искусственные нейронные сети, и сегодня это делается как правило с помощью оптимизаторов, реализованных во фреймворках (PyTorch/TensorFlow/etc), причем аппаратная реализация, в которой работает _Решатель_, -- это скорее видеокарта или TPU.
# 
# Ко второму из рассмотренных вариантов _Решателя_ можно также отнести и автоматическое дифференцирование. Чтобы оптимизировать параметры модели градиентными методами, нужно знать собственно градиенты функции потерь -- вектора частных производных функции потерь по параметрам. Попросту говоря, это ответ на вопрос, какие параметры модели стоит изменять и как это скажется на функции потерь, которую мы хотим минимизировать.
# 
# Иногда такие градиенты функции потерь можно найти аналитически, например, в случае линейной или логистической регрессии. Но как правило, в случае более сложных моделей с большим числом параметров аналитическое выражение для градиенты функции потерь выглядит слишком громоздко, а градиент лучше вычислять численно. Это задача методов автоматического дифференцирования. В частности, возможно, величайший алгоритм машинного обучения всех времен - алгоритм обратного распространения ошибки (backpropagation) -- не что иное как численный метод нахождения производных функции потерь по параметрам модели.
# 
# 
# 
# ### Схема валидации и метрика качества
# 
# Наконец, когда мы определились с целевым признаком, обучающими данными, моделью, функцией потерь, а также научились подбирать параметры модели так, чтоб функция потерь уменьшалась, остался последний шаг -- решить, как мы действительно поймем, что решаем задачу хорошо.
# 
# Выбор метрики качества напрямую связан с тем, чего мы хотим от модели машинного обучения в более широком контексте. Например, в бизнес-процессе могут быть ключевые показатели, которые мы _опосредованно_ можем улучшать с помощью машинного обучения. Ключевыми показателями могут быть такие вещи как дневная аудитория приложения, Life-Time Value, показатели, связанные с удержанием (retention) клиентов/сотрудников, удовлетворенность клиентов и т.д. Многие из этих показателей нельзя замерять напрямую и оптимизировать, и тогда искусство Data Scientist-а заключается в том, чтобы выбрать простую метрику качества, которая бы задавалась понятной формулой (например, доля верных ответов или полнота) и при этом неплохо "коррелировала" с тем показателем бизнес-процесса, который хочется оптимизировать и таким образом приносить деньги компании или уменьшать операционные расходы.
# 
# 
# Определение схемы валидации нужно, чтобы ответить на следующие вопросы:
# 
# - как понять, что модель сработает неплохо на новых, ранее не виденных данных
# - как понять, что мы улучшили решение, поменяв модель, ее гиперпараметры или добавив новые признаки
# - как понять, что одна модель лучше другой модели, один набор признаков лучше другого при фиксированной модели и т.д.
# 
# Во многом это связано с переобучением. Недостаточно просто замерить метрику качества на обучающей выборке. Надо хотя бы разбить выборку на 2 части: на одной обучать модель, на второй -- проверить метрику качества. И чаще всего при больших объемах данных и больших моделях ровно так и делают. Но в мире "малых данных" и легковесных моделей более предпочтительна кросс-валидация. В этой схеме выборка делится на несколько частей, а модель обучается столько же раз. При этом каждая из подвыборок один раз является тестовой частью, на которой измеряется качество прогнозов, а все остальные разы она участвует в обучении модели. Таким образом, кросс-валидация дает более надежную оценку того, как модель сработает на новых данных, в сравнении с простым разбиением обучающей выборки на две части.
# 
# 
# ```{figure} /_static/mlblock/k_fold_cross_validation.png
# :name: k_fold_cross_validation.png
# :width: 600px
# 
# Схема K-fold кросс-валидации.
# ```
# 
# Вы вряд ли ошибетесь, если на практике будете применять 5-кратную стратифицированную (такую что распределение целевого признака примерно одинаковое в каждой подвыборке) кросс-валидацию, но надо понимать, что кросс-валидация -- не панацея. И схема валидации, которую мы тут описываем, -- это больше, чем просто кросс-валидация.
# 
# Часто выделяют "офлайн" и "онлайн" режимы валидации. И метрики, полученные на кросс-валидации относятся к первому режиму, "офлайн". То есть мы один раз собрали обучающие данные, они больше не меняются, и вот с таким статическим срезом данных мы работаем, создаем признаки, обучаем модели, измеряем значения метрик на кросс-валидации. Но это не отвечает на вопрос, что получится, когда мы "выкатим модель в прод", какие значения метрик ожидать на новых данных. И тут, как правило, устраиваются A/B-тесты, которые позволяют понять, а действительно ли мы видим эффект от модели, лучше ли вообще с моделью, чем без нее, а если лучше с моделью, то какую модель выбрать. A/B-тестирование -- это очень обширная тема, выходящая за рамки данной статьи, и развивать ее тут мы не будем. Только отметим, что определение схемы валидации -- зачастую нетривиальный процесс и в зависимости от проекта может быть методологически сложным, в том числе и приводить к ошибкам.
# 
# Также заметим, что AutoML, о котором столь многие мечтают, решает некоторые вопросы, но далеко не все. В частности, алгоритмы AutoML не подберут вам правильную схему валидации. Они работают с уже имеющейся схемой валидации, и если валидация неверна, приводит к ошибкам, то тут и AutoML не поможет. Так что Data-Scientist-ов AutoML пока не вытеснит.
# 
# **Пример 1. Рекомендация новостного контента**
# 
# В этой задаче для выбора модели и ее гиперпараметров можно использовать обычную кросс-валидацию, но вот чтоб убедиться, что "в бою" модель также работает, лучше настроить A/B-тест (а точнее, для задач ранжирования намного лучше использовать [интерливинг](https://sease.io/2020/05/online-testing-for-learning-to-rank-interleaving.html)).  Пришло время сказать, что этот пример взят из практики автора этой лекции, Юрия Кашницкого, и в [выступлении на DataFest 2018](https://www.youtube.com/watch?v=uK4hPD12YmI) описывались сложности валидации модели в задаче рекомендации новостей. Вывод такой, что в задачах рекомендции (да и во многих других) надо устроить онлайн-проверку модели (A/B-тест, интерливинг) помимо офлайн-проверки (кросс-валдиации), только таким образом можно удостовериться, что модель действительно полезна, например, что использовать модель – лучше, чем просто показывать самый популярный контент.  
# 
# **Пример 2. Автоматическая оценка читаемости научной статьи**
# 
# Здесь тоже может использоваться обычная кросс-валидация, хотя на практике из-за объемов данных и размера модели кросс-валидацию проводить будет дороговато и придется удовлетвориться разбиением обучающей выборки на две части и проверкой модели на отложенной части.
# 
# Есть, конечно, детали. BERT не очень хорошо работает с длинными текстами, так что скорее всего мы разобьем полный текст статьи на параграфы и будем их подавать в модель по очереди. В таком случае лучше проводить [GroupKFold кросс-валидацию](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html) так, чтобы на каждом этапе кросс-валидации в обучающей и проверочной выборке были параграфы из разных статей. Мы вряд ли хотим обучаться на одной половине статьи и проверять модель на второй ее половине -- так бы мы получили слишком оптимистичную оценку качества модели.
# 
# Но даже при оговоренных тонкостях кросс-валидации самая большая сложность данной задачи -- убедиться, что метрика качества соответствует тому, что мы реально хотим получить в задаче. Это связано со сложностью определения "хорошо" и "плохо" написанного научного текста, о которой мы говорили выше. Поэтому в данной задаче, как и во многих других практических задачах машинного обучения, не обойтись без проверки результатов модели вручную. Такая проверка модели будет делаться уже после кросс-валидации, и в этом смысле она похожа на онлайн-оценку модели.
# 
# **Пример 3. Детекция симптомов COVID-19 на рентгенограммах**
# 
# Здесь схема проверки модели очень похожа на предыдущую. Сначала кросс-валидация или проверка модели на отложенной части, а потом – проверка предсказаний модели экспертами. Конечно, никто не будет по одной только кросс-валидации или результатам участников в соревновании Kaggle заключать, что модель прекрасно работает и ее можно нести врачам. В данном случае надо проверить модель на данных, приближенных к тем, которые будут использоваться врачами на практике. Чтобы не было [таких историй](https://www.technologyreview.com/2020/04/27/1000658/google-medical-ai-accurate-lab-real-life-clinic-covid-diabetes-retina-disease/), как у Google Health, когда Deep Learning модель достигала 90% верных ответов при определении диабетической ретинопатии по фото зрачка, но при обучении на качественных снимках высокого разрешения. А при работе с менее качественными снимками система просто слишком часто отказывалась выносить вердикт из-за того, что была недостаточно уверена в прогнозе.  
# 
# 
# ### Заключение
# 
# В этой лекции мы описали, из чего складывается постановка задачи машинного обучения и рассмотрели, как общие компоненты проглядываются в разных по своей природе задачах. При этом мы поговорили о моделях-рабочих лошадках в трех разных областях: градиентном бустинге для табличных данных, BERT для текстов и YOLO для детекции изображений.
# 
# Немного пожертвовав, возможно, строгостью определения таких понятий как целевой признак или решатель, мы, надеюсь, описали все "пазлы" достаточно абстрактно, чтоб сложилось общее представление о том, как машинное обучение применяется в разных задачах, а также какие подводные камни стоит ожидать при боевом применении машинного обучения. Надеемся, это позволит лучше осознать взаимосвязь разных компонентов в квантово-классических схемах обучения, о которых речь пойдет далее в курсе.
