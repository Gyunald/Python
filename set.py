# 집합 
# 중복 안됨, 순서가 없음
my_set = {1,2,3,4,5,5,5}
print(my_set)

java = {"a", "b", "c"}
python = {"a", "d", "e"}

# 교집합 (java and python)
print(java & python)
print(java.intersection(python))

# 합집합 (java or python)
print(java | python)
print(java.union(python))

# 차집합 (java not python)
print(java - python)
print(java.difference(python))

# 추가
python.add("f")
print(python)

# 삭제
java.remove("a")
print(java)