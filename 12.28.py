# # names = ["봄", "여름", "가을", "겨울"]


# # for i in range(4):
# #     print(i + 1, "번: ", names[i])


# # for i in range(4):
# #     name = names[i]
# #     print("{}번 : {}".format(i + 1, name))


# names = ["봄", "여름", "가을", "겨울", "봄봄"]
# # for i in range(len(names)):
# #     name = names[i]
# #     print("{}번 : {}".format(i + 1, name))


# # enumerate() : 인덱스 번호, 리스트 요소값을 한번에 처리할 수 있게 해줌 / 변수 두개를 받는 반복문을 만들어 낼 수 있어 편리하다
# # for i, name in enumerate(names):
# #     print("{}번 {}".format(i + 1, name))


# # 딕셔너리
# # - 리스트와 마찬가지로 다른 값을 여러 개 담을 수 있는 자료형
# # game = {"가위": "보", "바위": "가위", "보": "바위"}

# # print(game["보"])

# # 딕셔너리에서 key는 유일, value는 여러 값 가능
# # 키에 중복 입력해도 에러가 나오지 않지만 마지막 값만 인정됨
# # 키값에 리스트형식은 불가능
# # dict1 = {"key": [1, 2, 3, 4], "key": [5, 6, 7, 8]}

# # print(dict1["key"])
# # print(dict1[1])

# # 딕셔너리 수정
# dict2 = {"one": 1, "two": 2, "three": 3}
# dict2["two"] = 22
# # print(dict2)

# # 딕셔너리 추가
# dict2["four"] = 4
# # print(dict2)

# # 딕셔너리 삭제
# del dict2["one"]
# # print(dict2)

# dict2.pop("two")
# # print(dict2)


# # key, value 각각 호출
# scores = {"p": 10, "n": 20, "pan": 30}
# # for key in scores.keys():
# #     print(key)

# # for val in scores.values():
# #     print(val)

# # key, value 동시 호출
# # for key in scores.keys():
# #     print(key, scores[key])

# # for key, val in scores.items():
# #     print(key, val)

# # 딕셔너리 데이터 출력 시 출력 순서가 원본 순서와 다를 수 있다
# # 리스트와 달리 딕셔너리는 순서를 무조건 지키지 않는다 -> key로 찾기 때문에 순서를 지킬 필요 없음
# # 순서가 중요한 데이터라면 딕셔너리 자료형은 어울리지 않는다


# # 튜플
# tup2 = 1, 2, 3, 4, 5
# # print(tup2, type(tup2))

# var1 = 1
# var2 = (1,)  # ()안써도 튜플로 인식됨
# # print(type(var1), type(var2))

# # print(tup2[2])

# # 두 변수의 값을 맞바꿀 때 사용
# # 여러 값을 한 번에 전달하고 싶을 때 사용
# # 딕셔너리는 key에 따라 value를 찾아오므로 key가 매번 바뀌면 곤란하므로 key에 여러값을 넣으려고 할때 사용
# # 패킹

# c = (3, 4)
# d, e = c
# f = d, e

# # print(d, e)
# # print(f)


# # [실습] 데이터 맞바꾸기
# x = 5
# y = 10
# # print(x, y)

# # z = y, x
# # print(z)

# # x, y = z

# x, y = y, x
# # print(x, y)


# # 집합 연산
# s1 = set({1, 2, 3, 4, 5})
# s2 = set([4, 5, 6, 7, 8])
# # # 교집합
# # print(s1 & s2)
# # print(s1.intersection(s2))

# # # 합집합
# # print(s1 | s2)
# # print(s1.union(s2))

# # # 차집합 # 방향 주의
# # print(s1 - s2)
# # print(s1.difference(s2))


"""
score 에는 국어, 영어, 수학 점수가 들어있다
총점과 평균을 게산해서 배열에 담은 후 모든 학생의 국어, 영어, 수학, 총점, 평균을 출력하시오
* score에는 국어, 영어, 수학 점수만 들어있다.
"""
score = [
    [80, 80, 80, 0, 0],
    [60, 50, 80, 0, 0],
    [50, 90, 90, 0, 0],
    [40, 50, 60, 0, 0],
    [90, 90, 95, 0, 0],
    [85, 95, 100, 0, 0],
]

for i in range(len(score)):
    score[i][3] = sum(score[i][:3])
    score[i][4] = sum(score[i][:3]) / 3

# print(score)


"""
데이터 정렬 코드
- 퀵 정렬
- 나머지
"""
data = [100, 20, 5, 2, 3, 34, 65, 23, 66, 200]

# print(sorted(data))


"""
퀵 정렬
- 다른 원소와의 비교만으로 정렬을 수행
- O(n^2)
- 분할 정복 방법으로 리스트 정렬
"""

# for i in range(len(data)):
#     while i < len(data) / 2:
#         if data[i] > data[-i]:
#             data[i] = data[-i]
#         else:
#             continue

# print(data)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


sorted_data = quick_sort(data)
print(sorted_data)
