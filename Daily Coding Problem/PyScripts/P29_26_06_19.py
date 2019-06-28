'''
This problem was asked by Amazon.
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

Created on 28-Jun-2019

@author: Lenovo
'''
def run_length(inp,choice):
    if choice=='encode':
        if any(char.isdigit() for char in inp):
            raise Exception('Input String must have only Alphabet for encoding')
        else:
            inpl=list(inp)
            mat=inpl[0]
            count=0
            ret=[]
            while True:
                if len(inpl)==0:
                    ret.append(f'{count}{mat}')
                    break
                char=inpl[0]
                if char==mat: 
                    char=inpl.pop(0)                      
                    count+=1
                else:
                    ret.append(f'{count}{mat}')
                    count=0
                    mat=inpl[0]
            return ''.join(ret)
    if choice=='decode':
        inpl=list(inp)
        ret=[]
        while True:
            if len(inpl)==0:
                break
            count=inpl.pop(0)
            mat=inpl.pop(0)
            ret.append(f'{mat*int(count)}')
        return ''.join(ret)

def main():
    assert run_length("AAAABBBCCDAA",'encode')=='4A3B2C1D2A'
    assert run_length("4A3B2C1D2A",'decode')=='AAAABBBCCDAA'
    
if __name__=='__main__':
    main()