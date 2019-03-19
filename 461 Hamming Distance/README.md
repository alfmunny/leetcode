# 461. Hamming Distance

How to convert a integer N to binary

```
int n = N;
int a[32] = {0};

for ( size_t i = 0; n > 0; ++i)
{
    if (n%2) a[i] = 1;
    n = n/2;
}
```
