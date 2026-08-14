class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a, 2)
        num2 = int(b, 2)

        answer = num1 + num2

        return bin(answer)[2:]
              
        