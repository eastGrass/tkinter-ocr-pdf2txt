import sys
# python test.py 55 44 88
if __name__=='__main__':
    n = int(sys.argv[1])#从命令行读取一个参数赋给n,是str类型所以需要转换成int型
    m = int(sys.argv[2])
    print("打印输出接收的参数:")
    print('\t类型:',type(sys.argv),'\n\t值:', sys.argv)
    print("$$$$$$$$$$")
    print(sys.argv[0])
    print(sys.argv[-1])
    print("##########")
    print(n+m)
    print("**********")
    for item in sys.argv:
        print(type(item))
# python test.py 11111 22222 88888

'''
"args": ["11111","22222","88888"]
'''
