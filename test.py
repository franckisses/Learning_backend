while 1:
    try:
        s = input().split(" ")
############################### reset
        if len(s) == 1 and s[0] != " "*len(s[0]):
            if s[0] == "reset"[:len(s[0])]:
                print("reset what")
            else: 
                print("unknown command")
############################# 2 words
        elif len(s) == 2:
            if s[0] == "reset"[:len(s[0])]:
                print("board fault")
            elif s[0] == "board"[:len(s[0])] and s[1] == "add"[:len(s[1])]:
                print("where to add")
            elif s[0] == "board"[:len(s[0])] and s[1] == "delete"[:len(s[1])]:
                print("no board at all")
            elif s[0] == "reboot"[:len(s[0])]:
                print("impossible")
            elif s[0] == "backplane "[:len(s[0])]:
                print("install first")
            else:
                print("unknown command")
    except:
        break

