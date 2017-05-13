def cheeseShop(kind, *agrs, **keyss):
    print("-- Do you have any", kind,"?");
    print("-- I'm sorry, we're all out of", kind);
    for arg in agrs:
        print(arg);
    print("-"*40);
    keys = sorted(keyss.keys());
    for kw in keys:
        print (kw,":",keyss[kw]);


# *agrs 接受元祖,包含所有没有出现在形式参数列表中的参数值
# **keyss 接受字典,包含所有未出现在形式参数列表的关键字参数
# *agrs 必须在**keyss之前
#cheeseShop("Lim","It's very runy",
#               "It's reallly Very Runny",
#              shopkeeper="MP",
#               client="JC",
#               sketch="CSS");



