def fact(n):
    if n == 1:
        return 1;
    return n *fact(n-1);
print(fact(5))

#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式