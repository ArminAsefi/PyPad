import os
import sys
import random

class DroxyFireV1:

    MyStr = ""

    def __init__(self,mstr):
        self.MyStr = mstr

    def FindAscii(self):
        asci = []
        for i in range(0,len(self.MyStr)):
            asci.append(str(ord(self.MyStr[i])))
        return asci

    def IndexOf(self,myChar):
        index = 0
        found = False

        try:
            while (found == False):
                if (self.MyStr[index] == myChar):
                    found = True
                    break
                else:
                    index += 1

            if (found):
                return index
        except:
            return -1

    def EditByIndex(self,index,newData):
        try:
            dat = []
            for i in range(0,len(self.MyStr)):
                dat.append(self.MyStr[i])
            dat[index] = newData
            return self.UnArray(dat,False,"")
        except:
            return -1

    def EditByChar(self,myChar,newData):
        if (myChar in self.MyStr):
            self.MyStr = self.MyStr.replace(myChar,newData)
            return self.MyStr
        else:
            return -1
    
    def Reverse(self):
        asci = []
        for i in range(0,len(self.MyStr)):
            asci.append(str(self.MyStr[i]))
        asci.reverse()
        dataReved = ""
        for i in range(0,len(asci)):
            dataReved += asci[i]
        return dataReved

    def AddAscii(self,addNum):
        asci = []
        for i in range(0,len(self.MyStr)):
            asci.append(str(ord(self.MyStr[i]) + addNum))
        return asci

    def GetStr(self):
        return self.MyStr

    def CutStr(self,fromIndex,toIndex):
        try:
            return self.GetStr()[fromIndex:toIndex]
        except:
            return -1

    def SetStr(self,newStr):
        self.MyStr = newStr

    def ExtractNums(self):
        findedNums = []
        nums = [0,1,2,3,4,5,6,7,8,9]
        for i in range(0,len(self.MyStr)):
            for c in range(0,len(nums)):
                if (self.MyStr[i] == str(c)):
                    findedNums.append(self.MyStr[i])
        return findedNums

    def ExtractLetters(self):
        findedLetters = []
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(0,len(self.MyStr)):
            for c in range(0,len(letters)):
                if (self.MyStr[i] == str(letters[c])):
                    findedLetters.append(letters[c])
        return findedLetters

    def RandomInt(self,IsLimit,min,max):
        if (IsLimit):
            i = random.randint(min,max)
            return i
        else:
            LNums = [0,1,2,3,4,5,6,7,8,9]
            MLNums = [-1,-2,-3,-4,-5,-6,-7,-8,-9]
            lenn = random.randint(0,len(LNums) - 1)
            mlenn = random.randint(0,len(MLNums) - 1)
            i = random.randint(mlenn * 10,lenn * (1000000 * 1000000))
            return i

    def RandomStr(self,Length,IsLimit,LimitChars):
        if (IsLimit):
            chrs = LimitChars
            data = ""
            for i in range(0,Length):
                data += chrs[random.randint(0,len(chrs) - 1)]
            return data
        else:
            chrs = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456"789`~!@#$%^&*()-_=+{[]}\|';:/?.>,<"""
            data = ""
            for i in range(0,Length):
                data += chrs[random.randint(0,len(chrs) - 1)]
            return data


    def ExtractSymbols(self):
        findedChrs = []
        symbs = """`~!@#$%^&*()_-+={[]}\|'";:/?.>,<"""
        for i in range(0,len(self.MyStr)):
            for c in range(0,len(symbs)):
                if (self.MyStr[i] == str(symbs[c])):
                    findedChrs.append(self.MyStr[i])
        return findedChrs

    def DoesIn(self,search):
        if (search in self.GetStr()):
            return 1
        else:
            return -1

    def FindWordCount(self,search):
        return self.GetStr().count(search)

    def HashStr(self,salt):
        x = self.FindAscii()
        v = self.AddAscii(len(self.GetStr()) * round((salt + (salt - 1))))
        for i in range(0,len(self.GetStr())):
            if (i % 2 == 0):
                val = int(v[i]) + salt * (int(x[i]) + 2)
                v[i] = str(val)
            else:
                val = int(v[i]) + salt + (int(x[i]) + 2)
                v[i] = str(val)
        return self.ExtractFromAscii(v)

    def ExtractFromAscii(self,aArray):
        c = ''
        for i in range(0,len(aArray)):
            c += c.join(chr(int(aArray[i])))
        return c

    def DelStr(self,fromIndex,toIndex):
        try:
            c = self.GetStr()[fromIndex:toIndex]
            self.SetStr(self.GetStr().replace(c,""))
            return self.GetStr()
        except:
            return -1

    def UnArray(self,Array,IsSplit,Split):
        if (IsSplit):
            dat = ''
            for i in range(0,len(Array)):
                if (dat == ''):
                    dat += Array[i]
                else:
                    dat += ',' + Array[i]
            return dat
        else:
            dat = ''
            for i in range(0,len(Array)):
                dat += Array[i]
            return dat

if (__name__ == "__main__"):
    print("####################################")
    print("#                                  #")
    print("#            DroxyFireV1           #")
    print("#       Coded By Armin Asefi       #")
    print("#    E-mail : krossyx@gmail.com    #")
    print("#                                  #")
    print("####################################")