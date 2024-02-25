def pallindrome_checker(n):
     a=str(n)[::-1]
     if a==str(n):
        print(f"{n} is a pallindrome")
     else:
         print(f"{n} is not pallindrome")
            

pallindrome_checker(12321)
pallindrome_checker(12345)
