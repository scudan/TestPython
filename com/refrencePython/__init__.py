def cheeseShop(kindm, *agrs, **keyss):
    print("-- Do you have any", kind,"?");
    print("-- I'm sorry, we're all out of", kind);
    for arg in agrs:
        print(arg);
    print("-"*40);
    keys = sorted(keyss.keys());
    for kw in keys:
        print (kw,":",keyss[kw]);



    cheeseShop("Lim","It's very runy",
               "It's reallly Very Runny",
               shopkeeper="MP",
               client="JC",
               sketch="CSS");