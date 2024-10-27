while True:
    #입력
    word = input()
    if int(word) == 0:
        break

    # 문자 뒤집어서 비교
    if word == word[::-1]:
        print('yes')
    else:
        print('no')
