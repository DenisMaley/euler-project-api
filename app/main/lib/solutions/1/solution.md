Solution:

1. We know that multiples of 3 form an Arithmetic Progression(AP) and it's sum 
S<sub>3</sub> = 3 + 6 + 9 + 12 + 15 + 18 + 21 + …
2. And the multiples of 5 form an AP and it's sum S<sub>5</sub> = 5 + 10 + 15 + 20 + …
3. Now, Sum of them S<sub>3</sub> + S<sub>5</sub> i.e. 3 + 5 + 6 + 9 + 10 + 12 + 15 + 15 + 18 + 20 + …
4. From the previous step, 15 is repeated twice. In fact, all of the multiples of 15 (or 3*5) will be 
repeated as they are counted twice, once in the series S<sub>3</sub> and again in the series S<sub>3</sub>. 
So, the multiples of 15 need to be discarded from the result.
5. So, the final result will be S<sub>3</sub> + S<sub>5</sub> – S<sub>15</sub>
6. Generalizing, we can conclude that the sum of all the multiples of d1 or d1 below n
can be calculated as S<sub>d1</sub> + S<sub>d2</sub> – S<sub>(d1 * d2)</sub>
7. S<sub>d</sub>(n) = n(a<sub>1</sub> + a<sub>n</sub>)/2 = n(2a<sub>1</sub> + (n - 1)d)/2
8. Since a<sub>1</sub> = d, S<sub>d</sub>(n) = n(n + 1)d/2