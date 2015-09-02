
#일반 출력,,
#한글쓰려면 고급저장옵션에서 utf-8로 설정
#print("I 가지고있따 {0:3d} cats".format(6))

#형변환
#salary = input("Please enter your slalry: ")
#bonus = input("Pleas enter your bonus: ")
#payCheck = float(salary) + float(bonus)
#print(payCheck)

#형변환2
#salary = float(input("Please enter your slalry: "))
#bonus = float(input("Pleas enter your bonus: "))
#payCheck = salary + bonus
#print(payCheck)
# ctrl+k+c 주석  ctrl+k+u 주석해제

#data=float(1.3412)
#round(data, 2)

name="greenjoa"
print(name[0])
print(name[-1])
print(name[-2])
print(name[0:3]) #0,1,2 문자열 위치 가져옴

info="201312346greenjoa"
sid=info[:9]
sname=info[9:]
print(sid+" " +sname)

a="I eat %-10s apples."%"five"
print(a)
# %출력하고시픙ㄹ땐 %%


answer = input("종료할까요?").lower()
print(answer)
