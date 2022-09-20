def isNumber(s):
  try:
    float(s)

    if s.find("-") == 0:
        return print("Error")
    elif (s.find(".") != -1):
        print(int(round(float(s))))
    elif s.find("3" or "6" or "9"):
        s = s.replace('3', '짝')
        s = s.replace('6', '짝')
        s = s.replace('9', '짝')
        return print(s)

  except ValueError:
    return print("Please Insert Number")


a = input()
isNumber(a)
