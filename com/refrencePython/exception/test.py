while True:
    try:
        x = int(input(("please enter a num:")))
        break
        #  有异常,且匹配则走异常分支,完了继续转到try.
        # 如果未匹配到,则直接退出
    except ValueError:
        print("Oops! That was no valud num. try again...")