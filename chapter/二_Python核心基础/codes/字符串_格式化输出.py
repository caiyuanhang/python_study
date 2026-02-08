name = '张三'
gender = "男"

# + 拼接方式
infor = '我叫' + name + ', 我是' + gender + '的'
print('infor==', infor)

# 占位符方式
weight = 127.8
age = 18
level = 12
infor2 = '我叫%s' % name
print('占位符-单个==', infor2)
infor3 = '我叫%s，%s的，体重是%f，年龄是%i，今年读%d年级' % (name, gender, weight, age, level)
print('占位符-多个==', infor3)
infor4 = '我叫%s，%s的，体重是%s，年龄是%s，今年读%s年级' % (name, gender, weight, age, level)
print('占位符-全用%s==', infor4)
infor5 = '我叫%s，%s的，体重是%i，年龄是%i，今年读%i年级' % (name, gender, weight, age, level)
print('占位符-数值全用%i==', infor5)
infor6 = '我叫%s，%s的，体重是%d，年龄是%d，今年读%d年级' % (name, gender, weight, age, level)
print('占位符-数值全用%d==', infor6)
infor7 = '我叫%s，%s的，体重是%f，年龄是%f，今年读%f年级' % (name, gender, weight, age, level)
print('占位符-数值全用%f==', infor7)

# f-string
infor8 = f'我叫{name}，{gender}的，体重是{weight}，年龄是{age}，今年读{level}年级'
print('f-string 单引号==,', infor8)
infor9 = f"我叫{name}，{gender}的，体重是{weight}，年龄是{age}，今年读{level}年级"
print('f-string 双引号==,', infor9)
infor10 = f'''我叫{name}，{gender}的，体重是{weight}，年龄是{age}，今年读{level}年级'''
print('f-string 三对单引号==,', infor10)
infor11 = f"""我叫{name}，{gender}的，体重是{weight}，年龄是{age}，今年读{level}年级"""
print('f-string 三对双引号==,', infor11)
