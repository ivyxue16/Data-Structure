def convertToBase7(num: int):
        s = []
        if num > 0:
            while num > 0:
                rem = num % 7
                s.append(rem)
                num = num // 7
            newstring = ""
            while len(s) > 0:
                newstring = newstring + str(s.pop())
        elif num < 0:
            num = abs(num)
            while num > 0:
                rem = num % 7
                s.append(rem)
                num = num // 7
            newstring = "-"
            while len(s) > 0:
                newstring = newstring + str(s.pop())
        else:
            return "0"
        return newstring


def convertToBaseN(num: int, base: int):
        s = [] # create a stack
        digit = '0123456789ABCDEF' # 16-digit converter
        if num > 0:
            while num > 0:
                rem = num % base 
                s.append(rem)
                num = num // base
            newstring = ""
            while len(s) > 0:
                newstring = newstring + digit[s.pop()]
        elif num < 0:
            num = abs(num)
            while num > 0:
                rem = num % base
                s.append(rem)
                num = num // base
            newstring = "-"
            while len(s) > 0:
                newstring = newstring + digit[s.pop()] 
        else:
            # num is 0
            return "0"
        return newstring

print(convertToBaseN(25,16))