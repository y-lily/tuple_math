This package provides implementation of basic math operations for tuples.

## Quickstart

```Python
from tuple_math import add

add((1, 3), (2, 4))         # (3, 7)
add((1, 3), (2, 4, 6))      # (3, 7, 6)
add((1, 3), (2, 4), (5, 7)) # (8, 14)


from tuple_math import sub

sub((1, 3), (2, 4))         # (-1, -1)
sub((1, 3, 5), (2, 4))      # (-1, -1, 5)
sub((1, 3), (2, 4, 6))      # (-1, -1, -6)


from tuple_math import mult

# The factors for mult operation are expected to be of equal length.
# As of version 1.1.0, if factors of unequal length are given, the returned tuple's length will be the lowest of the two.
# This behavior may change in later versions.
mult((1, 3), (2, 4))        # (2, 12)

```

## round_down_mod

NB: The `round_down_mod` operation does NOT take mod and rounds it down. Instead, it rounds the first argument down to the closest factor of the second argument.

```Python
from tuple_math import round_down_mod

round_down_mod((6, 8, 9), (4, 3, 3))    # (4, 6, 9)
```

This operation can be understood as "How many whole second numbers does first number include".
