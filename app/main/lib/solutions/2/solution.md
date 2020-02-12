Solution:

1. Easy to notice and to prove that every third Fibonacci number is even:
1 1 **2** 3 5 **8** 13 21 **34** 55 89 **144** ...
2. If we only write the even numbers: 2 8 34 144...
it seems that they obey the following recursive relation: *E(n)=4E(n-1)+E(n-2)*.
If we can prove that for the Fibonacci numbers the formula *F(n)=4F(n-3)+F(n-6)* holds we
have proven this recursion.
3. *F(n) = F(n-1) + F(n-2) = F(n-2)+F(n-3)+F(n-2)=2F(n-2) + F(n-3)
= 2(F(n-3)+F(n-4))+F(n-3) = 3F(n-3) + 2F(n-4) = 3F(n-3) + F(n-4) + F(n-4)
= 3F(n-3) + F(n-4) + F(n-5) + F(n-6)
= 4F(n-3) + F(n-6)*