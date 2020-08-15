# 学习笔记

## 1.数据类型按可变和不可变
   * 可变数据类型:
     * 列表 list
     * 字典 dict
   * 不可变数据类型:
     * 整型int
     * 浮点型 float
     * 字符串型 string
     * 元组 tuple
## 2.另一种分类方式
   * 可变序列 list、bytearray、array.array、collections.deque 和 memoryview。
   * 不可变序列 tuple、str 和 bytes。

## 3.序列分类
   * 容器序列:list、tuple、collections.deque 等，能存放不同类型的数据 容器序列可以存 放不同类型的数据。
   * 扁平序列:str、bytes、bytearray、memoryview (内存视图)、array.array 等，存放的 是相同类型的数据 扁平序列只能容纳一种类型。
   * 容器序列存在深拷贝、浅拷贝问题
   * 非容器(数字、字符串、元组)类型没有拷贝问题
 ```
import copy 
copy.copy(object) 
copy.deepcopy(object)
```
## 4.Python 作用域遵循 LEGB 规则。
```
LEGB 含义解释:
• L-Local(function);函数内的名字空间
• E-Enclosing function locals;外部嵌套函数的名字空间(例如closure) • G-Global(module);函数定义所在模块(文件)的名字空间
• B-Builtin(Python);Python 内置模块的名字空间
```
## 5.参数分类
   * 必选参数
   * 默认参数
   * 可变参数
   * 关键字参数
   * 命名关键字参数

## 6. 函数的可变⻓参数
```
一般可变长参数定义如下:
def func(*args, **kargs): 
    pass
kargs 获取关键字参数 args 获取其他参数
示例:
def func(*args, **kargs): 
    print(f'args: {args}’) 
    print(f'kargs:{kargs}’)
func(123, 'xyz', name='xvalue' )
```

## 7. Lambda 表达式
Lambda 只是表达式，不是所有的函数逻辑都能封装进去

k = lambda x:x+1 print(k(1))

Lambda 表达式后面只能有一个表达式
   * 实现简单函数的时候可以使用 Lambda 表达式替代
   * 使用高阶函数的时候一般使用 Lambda 表达式
   
## 8. 偏函数
functools.partial:返回一个可调用的 partial 对象
使用方法:partial(func,*args,**kw)
注意:
   * func 是必须参数
   * 至少需要一个 args 或 kw 参数
   
##9. 返回值
   * 返回的关键字 • return
   * yield
 * 返回的对象
   * 可调用对象--闭包(装饰器)
   
## 10. 高阶函数
* 高阶:参数是函数、返回值是函数 
* 常见的高阶函数:map、reduce、filter、apply
* apply 在 Python2.3 被移除，reduce 被放在 functools 包中 
* 推导式和生成器表达式可以替代 map 和 filter 函数
* map (函数， 序列) 将序列中每个值传入函数，处理完成返回为 map 对象
* filter (函数，序列)将序列中每个值传入函数，符合函数条件的返回为 filter 对象

## 11.增强而不改变原有函数
装饰器强调函数的定义态而不是运行态

装饰器语法糖的展开:
```
@decorate def target():
    print('do something')

def target():
    print('do something')
target = decorate(target)

target 表示函数
target() 表示函数执行
new = func 体现“一切皆对象”，函数也可以被当做对象进行赋值
```
## 12. 被装饰函数
* 被修饰函数带参数
* 被修饰函数带不定长参数
* 被修饰函数带返回值