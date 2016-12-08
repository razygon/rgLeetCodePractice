'''
12. Integer to Roman   
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

'''

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0 or num > 3999:
            return None
        romdict={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        rlist = [1000,500,100,50,10,5,1]
        rom = []
        for l in rlist:
            d = num/l
            if d == 0:
                rom.append('')
                continue
            if d<4:
                while(d):
                    rom.append(romdict[l])
                    d = d-1
            else:
                c = rom.pop(len(rom)-1)
                rom.append(romdict[l])
                if c == '':
                    rom.append(romdict[rlist[rlist.index(l)-1]])
                else:
                    rom.append(romdict[rlist[rlist.index(l)-2]])
            num = num%l
        return ''.join(rom)
