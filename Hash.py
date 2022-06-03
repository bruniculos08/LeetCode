# Exemplo de tabela hash com python
nums = [1, 2, 3, 4]
prevMap = {}
target = 8

for i, n in enumerate(nums):
    prevMap[target - n] = n
print(prevMap)
print(prevMap[7])