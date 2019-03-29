# Relations and Relation Schemes

A ***relation scheme*** $R$ is a finite set of ***attribute names*** $\{ A_1,
A_2, ..., A_n \}$. Corresponding to each attribute name $A_i$ is a set $D_i$,
$1 \leq i \leq n$, called the ***domain*** of $A_i$. Let $D = D_1 \cup D_2 \cup
... \cup D_n$. A ***relation*** $r$ on relation scheme $R$ is a finite set of
mappings $\{ t_1, t_2, ... t_p \}$ from $R$ to $D$ with the restriction that
for each mapping $t \in r, t(A_i)$ must be in $D_i, 1 \leq i \leq n$. The
mappings are called ***tuples***.

> An alternative definition of a relation that I learned in the undergraduate
> database course that I took is $r \subseteq dom(A_1) \times dom(A_2) \times
> ...  \times dom(A_n)$. The restriction stated in the book's definition is
> implicit in the definition of the Cartesian product.

A ***key*** of a relation $r(R)$ is a subset $K$ of $R$ such that for any
distinct tuples $t_1$ and $t_2$ in $r$, $t_1(K) \neq t_2(K)$ and no proper
subset $K'$ of $K$ shares this property. $K$ is a ***superkey*** of $r$ if $K$
contains a key of $r$.

> Others names for a key are ***minimal superkey*** and ***candidate key***.

Relations are supposed to abstract some portion of the world, and this portion
of the world may change with time. Relations are time-varying, so that tuples
may be added, deleted, or changed, but the relation scheme is time-invariant.

