#idea:HungTuan
#Code:HungTuan
while True:
    import calendar


    from random import randint
# list là những con số :>>
    list = []

# k là số con lô
    print("+-----------------------------------------------------------------+")
    print("lưu ý cái trò này chỉ là dự đoán thoii, nếu mà thiêng thì biết đâu ăn đc thì sao :>>")
    k = int(input("nay bà ở đầu ngõ có mấy con lô, type vào đây :"))
    
    for i in range(k):
        list.append(int(input()))
    print("+-----------------------------------------------------------------+")
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


    print("+-----------------------------------------------------------------+")
    from datetime import date
    today = str(date.today())
    print("Hôm nay là ngày " + today)  
    print("Bạn vừa nhập : " + str(you))
    print("Kết quả là : " + str(computer))

    if you == computer:
        print(a)
    if you != computer:
        print(b)


    # main program
    while True:
        answer = str(input('Gỡ lại không :) y là chạy lại/ n là out :>> '))
        if answer in ('y', 'n'):
            break
        print("Nhập lại đi (y/n)")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break