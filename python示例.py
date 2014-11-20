打印
	# 字符串 %s  整数 %d  浮点 %f  原样打印 %r
	print('字符串: %s 整数: %d 浮点: %f 原样打印: %r' % ('aa',2,1.0,'r'))
	#不换行打印
	print('abc',end=' ')

输入
	#返回字符串;python3 中raw_input已废弃，
	input("input:")
	#将输入的字符串，转换为数字
	int(raw_input("input:"))

注释
	# #符号标识注释
	#文档字符串，在模块，类和函数的起始部分，添加一个字符串，起到文档功能
	def hello():
		'''this is a doc string'''
		return True

操作符
	算术运算符
		+ - * / // % **

	比较运算符
		== != > < >= <=

	赋值运算符
		=

	逻辑运算符
		and or not

	成员运算符
		in not in

	身份运算符
		is is not

变量
	#Python大小写敏感
	case  Case
	# 输出时原型打印
	r=r'\n'
	# 布尔运算赋值,a值为True既不处理后面,a值为2.  None、字符串''、空元组()、空列表[],空字典{}、0、空字符串都是false
	a = 0 or 2 or 1
	# 全局变量
	global x
	# 所有局部变量组成的字典
	locals()

赋值
	增量赋值
		Eg：+=

	链式赋值
		x=y=z=1

	序列解包
		x,y,z=1,2,3
		x,y=y,x

判断

	if a == b:
	    print('==')
	elif a < b:
	    print(b)
	else:
	    print(a)

	#三目运算
	5 if a=3 else 4

循环
	#while
    while a<10:
    	print("<")
    	a+=1

    #for
    for i in range(1, 5):
    	print(i)	

数字
	#数字类型 int float
	type(1)
	type(1.0)

	#bool类型 True False
	type(True)

	#bool类型的父类是int
	type(True).__bases__

	#True被当作1，False被当作0
	a=True+1
	b=False+1

序列
	name="sunchp"
	shoplist = ['apple', 'mango', 'carrot', 'banana']
	zoo = ('wolf', 'elephant', 'penguin')

	#索引
	print(name[1])

	print(shoplist[1])
	
	print(zoo[1])

	#分片
	name[::-1]    # 倒着打印 对字符翻转串有效
    name[2::3]    # 从第二个开始每隔三个打印
    name[:-1]     # 排除最后一个

	shoplist[::-1]    # 倒着打印 对字符翻转串有效
    shoplist[2::3]    # 从第二个开始每隔三个打印
    shoplist[:-1]     # 排除最后一个

    zoo[::-1]    # 倒着打印 对字符翻转串有效
    zoo[2::3]    # 从第二个开始每隔三个打印
    zoo[:-1]     # 排除最后一个

	#加
	name=name+"wnc"

	shoplist=shoplist+['orange',]

	zoo=zoo+('pig',)

	#乘
	name=name*2

	shoplist=shoplist*2

	zoo=zoo*2

	#in
	'u' in name

	'mango' in shoplist

	'wolf' in zoo

	字符串 str
		' ' " " ''' '''
		help(str)
		#str类
		str()
		#常用函数

	列表 list
		[v,]
		help(list)
		#list类
		list()
		#元素赋值
		shoplist[1]='orange'
		#元素删除
		del shoplist[1]
		#分片赋值
		shoplist[1:3]=['orange','wnc']
		# 在位置1前面插入列表中一个值
		shoplist[1:1]=['orange']
		# 将字符串当表达式求值,得到列表
		eval("['1','a']") 
		#常用函数

	列表解析
		[x**2 for x in range(8)]
		[x**2 for x in range(8) if not x%2]

	元组 tuple
		(v,)
		help(tuple)
		#tuple类
		tuple()

集合
	{v,}
	help(set)
	#set类 无序，无重复
	set()
	#in
	'u' in set('sunchp')
	# 将列表通过集合去重复
	list(set(['qwe', 'as', '123', '123']))   
	#交集
	a=t|s
	#并集
	a=t&s
	#差集
	a=t-s
	#对称差集
	a=t^s

字典
	{k=v,}
	help(dict)
	#dict
	dict()
	#in
	'name' in {'name':'sunchp','age':24}
	# 添加字典元素
	ab['c'] = 80
	# 删除字典元素   
    del ab['Larry']   

文件
	fi=open("D:\sun.txt",'r')
	
	for l in fi:
		print(l)
	
	fi.close()
    	
异常
	try:
		fi=open("D:\sun.txt",'r')
		
		for l in fi:
			print(l)

	except IOError:
		print("Error")

	else:
		print("success")

	finally:
		fi.close()
		print("finally")