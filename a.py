
#gửi những thg lol click vào link bố gửi trên mess này
#dưới đây là Code của bố, không ăn cắp ăn trộm ở đâu nhé
#Đọc không hiểu j thì install Python 3.10.4 về nhé
#Đêm nay con Vong Hồn add mày trên fb ấy, acp nó nhé!!!!!!!!
#         ----NTH---- 

from random import randint
# list là những con số :>>
list = []

# k là số con lô
k = int(input())

for i in range(k):
    list.append(int(input()))
print("Bảng vừa nhập nè")
print(list)

you = int(input('nhập con lô '))

ran = randint(1,2,)
a = "Chúc mừng bạn nhé, bạn đã trúng, truy cập https://www.youtube.com/watch?v=OXDRWWzESww để nhận thưởng "
b = "Hazzzz không trúng, nhưng mà ksao cả, còn thở là còn gỡ, chạy lại chương trình đi !!!"
c = 0

while c < k:
    c+= 1
    if ran==c:
        computer=list[c-1]
print("Bạn vừa nhập : " + str(you))
print("Kết quả là : " + str(computer))

if you == computer:
    print(a)
if you != computer:
    print(b)