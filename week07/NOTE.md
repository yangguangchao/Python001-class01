# 学习笔记

## 1.调用 property() 是构建数据描述器的简洁方式，该数据描述器在访问属性时触发函数调用
## 2.发起调用描述器
```
描述符可以通过其方法名称直接调用。例如， d.__get__(obj) 。

或者，更常见的是在属性访问时自动调用描述符。例如，在中 obj.d 会在 d 的字典中查找 obj 。如果 d 定义了方法 __get__() ，则 d.__get__(obj) 根据下面列出的优先级规则进行调用。

调用的细节取决于 obj 是对象还是类。

对于对象来说， object.__getattribute__() 中的机制是将 b.x 转换为 type(b).__dict__['x'].__get__(b, type(b)) 。 这个实现通过一个优先级链完成，该优先级链赋予数据描述器优先于实例变量的优先级，实例变量优先于非数据描述符的优先级，并如果 __getattr__() 方法存在，为其分配最低的优先级。 完整的C实现可在 Objects/object.c 中的 PyObject_GenericGetAttr() 找到。

对于类来说，机制是 type.__getattribute__() 中将 B.x 转换为 B.__dict__['x'].__get__(None, B) 。在纯Python中，它就像:

def __getattribute__(self, key):
    "Emulate type_getattro() in Objects/typeobject.c"
    v = object.__getattribute__(self, key)
    if hasattr(v, '__get__'):
        return v.__get__(None, self)
    return v
要记住的重要点是：

描述器由 __getattribute__() 方法调用

重写 __getattribute__() 会阻止描述器的自动调用

object.__getattribute__() 和 type.__getattribute__() 会用不同的方式调用 __get__().

数据描述符始终会覆盖实例字典。

非数据描述器会被实例字典覆盖。

super() 返回的对象还有一个自定义的 __getattribute__() 方法用来发起调用描述器。 调用 super(B, obj).m() 会搜索 obj.__class__.__mro__ 紧随 B 的基类 A，然后返回 A.__dict__['m'].__get__(obj, B)。 如果其不是描述器，则原样返回 m。 如果不在字典中，m 会转而使用 object.__getattribute__() 进行搜索。

这个实现的具体细节在 Objects/typeobject.c. 的 super_getattro() 中，并且你还可以在 Guido's Tutorial 中找到等价的纯Python实现。

以上展示的关于描述器机制的细节嵌入在 object ， type ， 和 super() 中的 __getattribute__() 。当类派生自类 object 或有提供类似功能的元类时，它们将继承此机制。同样，类可以通过重写 __getattribute__() 阻止描述器调用。

描述符示例
以下代码创建一个类，其对象是数据描述器，该描述器为每个 get 或 set 打印一条消息。覆盖 __getattribute__() 是可以对每个属性执行此操作的替代方法。但是，此描述器对于跟踪仅几个选定的属性很有用：

class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Updating', self.name)
        self.val = val

>>> class MyClass(object):
...     x = RevealAccess(10, 'var "x"')
...     y = 5
...
>>> m = MyClass()
>>> m.x
Retrieving var "x"
10
>>> m.x = 20
Updating var "x"
>>> m.x
Retrieving var "x"
20
>>> m.y
5
这个协议很简单，并提供了令人兴奋的可能性。有几种用例非常普遍，以至于它们被打包到单独的函数调用中。属性、绑定方法、静态方法和类方法均基于描述器协议。roperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)

```

## 3.类属性和对象属性的作用域
### 对于类：
    * 类可以直接访问类属性
    * 类不可以直接访问实例方法，必须通过实例化之后的对象来访问实例方法
    * 类不可以访问对象特有的属性（比如：def __init__中定义的属性）
    * 类可以直接访问类方法
    * 类可以直接访问静态方法
    * 所以存在：如果对象中的属性跟类中的属性相同，改变对象中的属性值，不会影响类中的属性值

### 对于对象：
    * 对象可以直接访问类的属性（实例化过程中，类已经将属性赋给对象）
    * 对象可以直接访问自己私有的属性
    * 对象可以直接访问类方法
    * 对象可以直接访问静态方法
    * 对象可以直接访问实例方法
    
## 4. classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
## 5.类方法
* 三种方法
  * 普通方法  至少一个self参数，表示该方法的对象
  * 类方法   至少一个cls参数，表示该方法的类
  * 静态方法  由类调用，无参数
* 三种方法在内存中都归属于类