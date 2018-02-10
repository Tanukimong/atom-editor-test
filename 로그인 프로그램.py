input_id = input("아이디를 입력해주세요.\n")
members = ['egoing','k8805','leezche']
for member in members:
    if input_id == member:
        print("Hello!, "+member)
        import sys
        sys.exit()
print('who are you?')
