# 438. Find All Anagrams in a String

Anagrams:

1. when the appearence number of diffrent character of B string is euqal with those of A string, then B is an anagram of A string.

Keep two hash maps to track the charactor numbers of the current string and the string to be compared.

vector<int> av(26, 0);
vector<int> bv(26, 0);

for each charactor in A, ++av[a[i] - 'a'], ++bv[b[i] - 'a']

2. use sliding window to go through the whole target string.
