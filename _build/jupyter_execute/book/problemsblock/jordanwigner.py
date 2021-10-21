#!/usr/bin/env python
# coding: utf-8

# (quantchembasic)=
# 
# # Преобразование Жордана-Вигнера
# 
# ## Описание лекции
# 
# 
# ## Введение
#  Для того чтобы просимулировать квантовую систему на квантовом же компьютере, нам необходимо закодировать 
#  состояние системы и операторы которые могут на нее действовать (добавить fig. 1 из https://arxiv.org/pdf/1208.5986.pdf
#  или что-то похожее).
# ## Спины, фермионы и бозоны
# 
# ## Вторичное квантование
# 
# В квантовой механике мы [можем описать](../qcblock/gates.html#id11) состояние нескольких частиц как тензорное произведение состояний каждой из частиц.
# Например, если у нас есть две частицы, и их квантовое состояние описывается положением частицы в пространстве, $r_i$, 
# мы можем записать состояние частиц как
# 
# $$
# | \psi \rangle = | r_1 \rangle \otimes |r_2 \rangle. 
# $$
# 
# У этого подхода есть два главных недостатка -- во первых, работать с системами в которых разное количество частиц, или где
# это количество может меняться, не очень удобно. Во-вторых, не учитывается неразличимость квантовых частиц. 
# 
# Обе эти проблемы решаются вторичным квантованием, где вместо использования состояния каждой частицы мы описываем систему 
# количеством частиц в каждом из возможных состояний. Так как частицы неразличимы, такое описание достаточно для полного 
# описания системы. Вместо Гильбертова пространства фиксированной размерности наши состояния теперь являются элементами 
# пространства Фока (суммы Гильбертовых пространств для всех возможных значений количества частиц). Основное состояние,
# или вакуум, теперь это состояние с 0 частиц. 
# 
# Мы так же можем определить операторы, которые добавляют или убирают частицу в определенном состоянии из системы. На языке первой квантизации:
# 
# $$
# b^\dagger_\alpha | \Psi \rangle =\frac{1}{\sqrt{N+1}} | \psi_\alpha \rangle  \otimes | \Psi \rangle
# $$
# 
# $$
# b_\alpha | \psi_\alpha \rangle  \otimes | \Psi \rangle=\frac{1}{\sqrt{N}}| \Psi \rangle. 
# $$
# 
# $b^\dagger_\alpha$ называется оператором создания (creation), а $b_\alpha$ -- уничтожения (annihilation). Заметим, что 
# эти операторы не эрмитовы, т.е., $b^\dagger_\alpha \neq b_\alpha$. Нормализация операторов выбрана таким образом, что
# собственные значения (эрмитова) оператора $b^\dagger_\alpha b_\alpha$ -- количество частиц в состоянии $\alpha$.
# 
# Если в системе нет ни одной частицы в состоянии $\alpha$, то оператор уничтожения уничтожает состояние:
# 
# $$
# b_\alpha | \Psi \rangle=0.  
# $$
# 
# В зависимости от типа частиц, операторы создания и уничтожения подчиняются определенным отношениям. В случае бозонов, 
# разные операторы коммутируют:
# 
# $$
# [b^\dagger_i, b_j ] = \delta_{ij}  
# $$
# 
# $$
# [b^\dagger_i, b^\dagger_j ] = [b_i, b_j ] =0.  
# $$
# 
# В случае фермионов, операторы антикоммутируют:
# 
# $$
# \{с^\dagger_i, с_j \} = \delta_{ij} 
# $$
# 
# $$
# \{c^\dagger_i, c^\dagger_j \} = \{c_i, c_j \} =0.  
# $$
# 
# В частности, 
# 
# $$
# \{c^\dagger_j, c^\dagger_j \} = 2\left(c^\dagger_j\right)^2 = 0,
# $$
# 
# и, следовательно, в системе не может быть больше одного фермиона в одном состоянии.
# 
# ## Переход от спинов к фермионам
# 
# Мы можем попробовать сопоставить спину фермион сказав что спин вниз значит что фермион есть, а спин вверх -- что его нет.
# Другими словами, используя оператор количества частиц $\hat{n}_i = c^\dagger_i c_i$, где $c^\dagger_i$ и $c_i$ это операторы
# создания и разрушения  соответсвенно, мы хотели бы сопоставить
# 
# $$
# \hat{\sigma}_i^z = 1 - 2\hat{n}_i
# $$
# 
# Тогда лестничные (ladder) операторы $\sigma^- = (\hat{\sigma}_i^x-i\hat{\sigma}_i^y)/2$ и 
# $\sigma^+= (\hat{\sigma}_i^x+i\hat{\sigma}_i^y)/2$ соответствуют операторам создания и разрушения. 
# Действительно, на одной вершине эти операторы выполняют фермионное антикоммутационное отношение
# 
# $$ 
# \{ \sigma^+_j, \sigma^-_j \} = 1. 
# $$
# 
# К сожалению, на разных вершинах эти операторы коммутируют, а не антикоммутируют. Чтобы это исправить, мы "прикрепляем"
# к каждому фермиону "нить" (string):
# 
# $$
# \sigma^+_i = \left[ \prod_{j< i} (1-2c^\dagger_j c_j) \right] c_i
# $$
# 
# $$
# \sigma^-_i = \left[ \prod_{j< i} (1-2c^\dagger_j c_j) \right] c^\dagger_i
# $$
# 
# Oператор $\prod_{j_i} (1-2c^\dagger_j c_j)$ равен $\pm 1$ в зависимости от четности количества фермионов слева от вершины $i$.
# 
# Заметим, что  $c_k$ антикоммутирует с  $(1-2c^\dagger_k c_k)$:
# 
# $$ 
# \{ c_j, (1-2c^\dagger_j c_j) \} = c_j (1-2c^\dagger_j c_j) +  c_j (1-2c^\dagger_j c_j)c_j  =
# c_j  -2c_jc^\dagger_j c_j +  c_j -2c^\dagger_j c_jc_j = c_j  -2c_j+  c_j  = 0,
# $$
# 
# и, следовательно с нитью $\prod_{j_i} (1-2c^\dagger_j c_j) $ (интуивно, если сначала разрушить фермион, то четность изменится).
# 
# Пусть, без ограничения общности, $\ell>k$:
# 
# $$
# \sigma^+_k \sigma^-_\ell = \left[ \prod_{j<k} (1-2c^\dagger_j c_j) \right] c_k \left[ \prod_{m< \ell} (1-2c^\dagger_m c_m) \right] c^\dagger_\ell 
# $$
# 
# Если мы перенесем $c_k$ вправо, то выражение умножится на -1 дважды (один раз из-за изменения четности $\ell$-нити, 
# и один раз из-за обмена с $c^\dagger_\ell$) $i$-нить коммутирует со всем, поэтому ее мы можем перенести вправо без изменений:
# 
# $$
# \sigma^+_k \sigma^-_\ell 
# = \left[ \prod_{j<k} (1-2c^\dagger_j c_j) \right] c_k \left[ \prod_{m< \ell} (1-2c^\dagger_m c_m) \right] c^\dagger_\ell
# =  \left[ \prod_{m< \ell} (1-2c^\dagger_m c_m) \right] c^\dagger_\ell \left[ \prod_{j<k} (1-2c^\dagger_j c_j) \right] c_k =
# = \sigma^-_\ell  \sigma^+_k, 
# $$
# 
# как и требовалось. Мы так же можем записать обратное отношение:
# 
# $$
# c_i = \left[ \prod_{j< i} \sigma^z_j \right] \sigma^+_i
# $$
# 
# $$
# c^\dagger_i = \left[ \prod_{j< i} \sigma^z_j \right] \sigma^+_j.
# $$
# Проверка антикоммутаторов оставляется читателю в качестве упражнения.
# 
# Таким образом мы установили соответсвие между фермионной и спиновой системами, но операторы в обоих случаях очень нелокальны.
# В частности, один фермионный оператор соответветсвует произведению $\mathcal{O}(N)$ спиновых операторов (и наоборот).
# 
# ### Пример
# Какой-нибудь Hubbard model?
