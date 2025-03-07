from typing import List, Tuple

# We assume that all lists passed to functions are the same length N

# Match big O complexities with the code snippets below

# answers 
# 1 - log n
def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n



# 2 - n^2
def question3(first_list: List[int], second_list: List[int])-> List[int]:
   temp: List[int] = first_list[:]
   for el_second_list in second_list:
      flag = False
      for check in temp:
         if el_second_list == check:
            flag = True
            break
      if not flag:
         temp.append(second_list)
   return temp


# 3 - n
def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res





# 4 - n^2
def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res


# 5 - 1
def question2(n: int) -> int:
	for _ in range(10):
		n **= 3
	return n



# 6 - n

def question4(input_list: List[int]) -> int:
  res: int = 0
  for el in input_list:
    if el > res:
      res = el
  return res













