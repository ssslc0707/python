# def tail(filename):
#     f = open(filename,encoding='utf-8')
#     while True:
#         line = f.readline()
#         if line.strip():
#             yield line.strip()
#
# g = tail('file')
# for i in g:
#     if 'python' in i:
#         print('***',i)



def f1(*args):
    print('1',*args)
    print('2',args)
    def in2(args):
        print(args)
    in2(args)

f1(1)
