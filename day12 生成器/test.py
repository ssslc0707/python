# def it():
#     print(1)
#     yield 'a'
#     print(2)
#     yield 'b'
#
#
# g = it()
#
# for i in g:
#     print(i)
#
#
# def wahaha(i):
#     i += 1
#     if i < 100000:
#         #wahaha(i)
#         yield '娃哈哈'%i
#
#
# generator = wahaha(0)
#
# for i in generator:
#     print(i)
#
def getFileInput():
    with open('file',mode='r+',encoding='utf-8') as f:
        while 1:
            readline = f.readline()

            if readline.strip():
                yield readline.strip()
# for i in getFileInput():
#     print(i)


 