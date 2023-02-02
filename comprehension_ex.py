# List Comprehention 은 반복되거나 조건을 만족하는 리스트를 보다 쉽게 만들기 위한방법
# 리스트나 여타 이터러블을 다른 리스트로 변환하기 쉬운 방법이다. 이경우 for 루프를 대체.
list = ['A', 'b', 'C', 'd']

[i.lower() for i in list]

[i for i in list]

[i * 3 for i in range(10)]

[i + 2 for i in range(10)]

# 조건문을 사용한 comprehention
[i for i in range(30) if i%2 == 0]

[i * 10 for i in range(20) if i%3 == 0]

# 먼저 반복문 적어주고, 그 인자들이 조건문에 해당하는지 확인하여 그 인자를 리스트의 요소로 가짐

# 두 개의 반복문 사용하기(개별x and o)

a = ['a', 'b', 'c', 'd', 'e']
b = ['1', '2', '3', '4', '5']
[i + j for i in a for j in b]

new_list = []
for i in a:
    for j in b:
        new_list.append(i+j)

new_list

# 두 개의 조건문 사용하기.
[i for i in range(50) if i%2 == 0 if i%3 == 0]

# 조건문에서 else 사용하기 (elif는 불가)
['even' if i%2 == 0 else 'odd' for i in range(10)]
# ['even' for i in range(10) if i%2 == 0 else 'odd']
