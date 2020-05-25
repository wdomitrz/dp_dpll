---
title: Artificial Intelligence in Theorem Proving Homework 1
author: Witalis Domitrz <witekdomitrz@gmail.com>
header-includes:
- \usepackage{amsmath}
- \usepackage{fullpage}
---

# Transformacja Tseytina

## Przypomnienie

$$(a \iff \neg b) \iff (b \lor a) \land (\neg a \lor \neg b)$$
$$(a \iff (b \land c)) \iff (\neg b \lor \neg c \lor a) \land (\neg a \lor b) \land (\neg a \lor c)$$
$$(a \iff (b \lor c)) \iff (\neg b \lor a) \land (\neg c \lor a) \land (\neg a \lor b \lor c)$$
$$(a \iff (b \implies c)) \iff (b \lor a) \land (\neg c \lor a) \land (\neg a \lor \neg b \lor c)$$
$$(a \iff (b \iff c)) \iff (\neg b \lor \neg c \lor a) \land (b \lor c \lor a) \land (\neg c \lor b \lor \neg a) \land (\neg b \lor c \lor \neg a)$$

## 1.

$$(x \land \neg y) \iff (x \implies (y \land \neg z))$$

Wprowadzam nowe zmienne tak, że

* $a_1 \iff \neg y$
* $a_2 \iff (x \land a_1)$
* $a_3 \iff \neg z$
* $a_4 \iff (y \land a_3)$
* $a_5 \iff (x \implies a_4)$
* $a_6 \iff (a_2 \iff a_5)$

Teraz formuła z treści jest spełnialna wtedy i tylko wtedy, gdy spełnialna jest formuła:

\begin{equation}
\begin{split}
(a_1 \iff \neg y) \land \\
(a_2 \iff (x \land a_1)) \land \\
(a_3 \iff \neg z) \land \\
(a_4 \iff (y \land a_3)) \land \\
(a_5 \iff (x \implies a_4)) \land \\
(a_6 \iff (a_2 \iff a_5)) \land \\
a_6
\end{split}
\end{equation}

Co po przekształceniu jak z [przypomnienia](#przypomnienie) jest w CNF-ie:

\begin{equation}
\begin{split}
(y \lor a_1) \land (\neg a_1 \lor \neg y) \land \\
(\neg x \lor \neg a_1 \lor a_2) \land (\neg a_2 \lor x) \land (\neg a_2 \lor a_1) \land \\
(z \lor a_3) \land (\neg a_3 \lor \neg z) \land \\
(\neg y \lor \neg a_3 \lor a_4) \land (\neg a_4 \lor y) \land (\neg a_4 \lor a_3) \land \\
(x \lor a_5) \land (\neg a_4 \lor a_5) \land (\neg a_5 \lor \neg x \lor a_4) \land \\
(\neg a_2 \lor \neg a_5 \lor a_6) \land (a_2 \lor a_5 \lor a_6) \land (\neg a_5 \lor a_2 \lor \neg a_6) \land (\neg a_2 \lor a_5 \lor \neg a_6) \land \\
a_6
\end{split}
\end{equation}

## 2.

$(y \land (x \iff \bot)) \iff (\neg x \lor y)$

Wprowadzam nowe zmienne:

* $a_1 \iff (x \iff \bot)$
* $a_2 \iff (y \land a_1)$
* $a_3 \iff \neg x$
* $a_4 \iff (a_3 \lor y)$
* $a_5 \iff (a_2 \iff a_4)$

Teraz formuła z zadania jest spełnialna wtedy i tylko wtedy, gdy spełnialna jest formuła:

\begin{equation}
\begin{split}
(a_1 \iff (x \iff \bot)) \land \\
(a_2 \iff (y \land a_1)) \land \\
(a_3 \iff \neg x) \land \\
(a_4 \iff (a_3 \lor y)) \land \\
(a_5 \iff (a_2 \iff a_4)) \land \\
a_5
\end{split}
\end{equation}

Co po przekształceniu jak z [przypomnienia](#przypomnienie) jest już prawie w CNF-ie:

\begin{equation}
\begin{split}
(\neg x \lor \neg \bot \lor a_1) \land (x \lor \bot \lor a_1) \land (\neg \bot \lor x \lor \neg a_1) \land (\neg x \lor \bot \lor \neg a_1) \land \\
(\neg y \lor \neg a_1 \lor a_2) \land (\neg a_2 \lor y) \land (\neg a_2 \lor a_1) \land \\
(x \lor a_3) \land (\neg a_3 \lor \neg x) \land \\
(\neg a_3 \lor a_4) \land (\neg y \lor a_4) \land (\neg a_4 \lor a_3 \lor y) \land \\
(\neg a_2 \lor \neg a_4 \lor a_5) \land (a_2 \lor a_4 \lor a_5) \land (\neg a_4 \lor a_2 \lor \neg a_5) \land (\neg a_2 \lor a_4 \lor \neg a_5) \land \\
a_5
\end{split}
\end{equation}

A po wyeliminowaniu symbolu $\bot$ i $\neg \bot$ jest w CNF-ie.

\begin{equation}
\begin{split}
(x \lor a_1) \land (\neg x \lor \neg a_1) \land \\
(\neg y \lor \neg a_1 \lor a_2) \land (\neg a_2 \lor y) \land (\neg a_2 \lor a_1) \land \\
(x \lor a_3) \land (\neg a_3 \lor \neg x) \land \\
(\neg a_3 \lor a_4) \land (\neg y \lor a_4) \land (\neg a_4 \lor a_3 \lor y) \land \\
(\neg a_2 \lor \neg a_4 \lor a_5) \land (a_2 \lor a_4 \lor a_5) \land (\neg a_4 \lor a_2 \lor \neg a_5) \land (\neg a_2 \lor a_4 \lor \neg a_5) \land \\
a_5
\end{split}
\end{equation}

Warto zauważyć, że można by też wyelimnować $\bot$ na początku (bo $(x \iff \bot) \iff \neg x$) i wtedy mamy

\begin{equation}
\begin{split}
(a_1 \iff \neg x)) \land \\
(a_2 \iff (y \land a_1)) \land \\
(a_4 \iff (a_1 \lor y)) \land \\
(a_5 \iff (a_2 \iff a_4)) \land \\
a_5
\end{split}
\end{equation}

co się sprowadza do:

\begin{equation}
\begin{split}
(x \lor a_1) \land (\neg x \lor \neg a_1) \land \\
(\neg y \lor \neg a_1 \lor a_2) \land (\neg a_2 \lor y) \land (\neg a_2 \lor a_1) \land \\
(\neg a_1 \lor a_4) \land (\neg y \lor a_4) \land (\neg a_4 \lor a_1 \lor y) \land \\
(\neg a_2 \lor \neg a_4 \lor a_5) \land (a_2 \lor a_4 \lor a_5) \land (\neg a_4 \lor a_2 \lor \neg a_5) \land (\neg a_2 \lor a_4 \lor \neg a_5) \land \\
a_5
\end{split}
\end{equation}

