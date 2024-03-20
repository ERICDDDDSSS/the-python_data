# 튜플 
# : () 기호 여러 개의 변경할 수 없는 자료를 저장하는 컬렉션

t1 = ( 10, 12.45, 'hello' )
t2 = ( 20, 22.45, 'bye' )
t3 = t1 + t2

print('t1 : ', t1)
print('t2 : ', t2)
print('t3 : ', t3)

# 튜플도 인덱싱, 슬라이싱 가능

# 주의
# : 요소를 하나만 저장하는 경우
# , 기호를 같이 작성해야 튜플로 인식된다.
t4 = (10)                    # 튜플아님
print( type(t4) )

t5 = (10,)                   # 튜플
print( type(t5) )