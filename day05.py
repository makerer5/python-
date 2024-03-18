# try except
'''
Python中的try和except块是异常处理的关键部分，用于捕获和处理程序运行中出现的错误，以避免程序因错误而完全停止。
使用try和except可以使程序更加健壮和用户友好。下面是基本的用法：
'''
'''
try:
    # 尝试执行的代码
    # 可能会引发异常的操作
except SomeException:
    # 如果在try块中发生了SomeException类型的异常，则执行这里的代码
'''

# 访问异常信息
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(risk)
except Exception as e:
    print(f"发生错误：{e}")

# finally块是一个可选的代码块，无论是否发生异常，它都会被执行。这对于执行清理工作，如关闭文件或释放资源等操作非常有用：
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(risk)
except SomeException:
    print("failed")
finally:
    # 无论是否发生异常，都会执行的代码
    print('failed')

# calss 构建新类
# 在Python中，类（class）是对象的蓝图或模板，你可以使用它来创建具有特定属性和方法的对象。
# 类定义了对象的状态（通过属性）和行为（通过方法）。创建新对象的过程通常称为实例化。
class MyFirstClass:
    def __init__(self, name):
        self.name = name  # 属性

    def greet(self):
        # 方法
        return f"Hello, {self.name}!"

# 创建MyFirstClass的一个实例
my_object = MyFirstClass("Alice")
print(my_object.greet())  # 输出: Hello, Alice!
'''
'class MyFirstClass:'：这行定义了一个名为MyFirstClass的新类。
'def __init__(self, name):'：这是一个特殊的方法，称为类的构造器或初始化方法。当创建类的新实例时，Python会自动调用它。self参数是对当前对象实例的引用，而name是一个传递给类实例化过程的参数。
'self.name = name'：这行代码将传递给构造器的name参数值赋给self.name属性。这样，每个类实例都会有自己的name属性。
'def greet(self):'：这是类的一个方法，用于定义对象的行为。greet方法使用对象的name属性来返回一个问候语。
'''

'''
'my_object = MyFirstClass("Alice")'：这行代码创建了MyFirstClass类的一个新实例，并将字符串"Alice"作为参数传递给__init__方法。然后，这个新创建的对象被赋值给变量my_object。
使用类和对象是面向对象编程（OOP）的核心概念。在面向对象编程中，类提供了一种将数据（属性）和功能（方法）封装到一起的方式，使得创建复杂程序时更加有条不紊，易于管理和维护。
'''

class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        return f"Hi!, {self.name}, where are you going"

person_talk = Person("Alice")
print(person_talk.talk())


# inheritance 继承
'''
在Python中，继承是面向对象编程（OOP）的一个核心概念，它允许我们定义一个类（称为子类或派生类）来继承另一个类（称为父类或基类）的属性和方法。
这种机制有助于代码的重用，可以让我们建立一个层次化的类结构。
'''
class Parent:
    def __init__(self):
        self.value = "Inside Parent"

    def show(self):
        print(self.value)

class Child(Parent):
    def __init__(self):
        # 调用父类的__init__方法
        super().__init__()
        self.value = "side Child"

    def display(self):
        print(self.value)

# 创建Parent类的实例
p= Parent()
p.show
c = Child()
c.display

# super()函数是一个内置函数，用于调用父类的方法。它非常有用，尤其是在覆盖父类方法的时候，因为它允许你在子类中调用父类的实现。
# 在上面的例子中，Child类通过调用super().__init__()来确保父类Parent的__init__方法被执行，这样Child实例就继承了父类的所有属性，然后我们可以根据需要对其进行修改或扩展。

# Overriding 方法重写
# 在子类中，你可以修改继承自父类的行为，这称为方法重写。在上面的例子中，Child类通过定义自己的__init__方法并设置self.value的值为"Inside Child"来重写Parent类的__init__方法。

# 多重继承
# Python还支持多重继承，允许子类同时继承多个父类的属性和方法。
class Base1:
    def method(self):
        print("Inside Base1")

class Base2:
    def method(self):
        print("Inside Base2")

class MultiDerived(Base1, Base2):
    pass

md = MultiDerived()
md.method()  # 输出将依赖于方法解析顺序（MRO），在这个例子中是Base1

'''
方法解析顺序（Method Resolution Order，简称MRO）是一个非常重要的概念，
在Python的面向对象编程中用于确定类继承体系中方法调用的顺序。
Python 2.3之后的版本采用了C3线性化算法来计算MRO，它保证了在任何情况下，类的继承都是明确和一致的。
MRO决定了当你调用一个方法时，Python会首先在哪个类中寻找这个方法。这个顺序尤其在多重继承的场景下非常关键，因为不同的父类可能含有相同名称的方法。

C3线性化算法
C3线性化算法是一种用于计算类继承中方法解析顺序的算法。
其目标是保持继承的直观性并保持局部优先级（子类优先于父类，多重继承中按定义顺序优先）的同时，也满足一致性（如果类X在类Y之前，那么在整个MRO中，X都应该在Y之前）。

如何查看MRO
你可以通过两种方式查看Python类的MRO：

使用类的__mro__属性。
使用内置的mro()方法。
'''
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# 查看类D的MRO
print(D.__mro__)

# 在这个例子中，类D继承自B和C，而B和C都继承自A。
# 根据C3线性化算法，D的MRO将会是D-B-C-A。这意味着，如果这些类中有同名的方法，Python会首先在D中查找，
# 如果没有找到，然后是B，接着是C，最后是A。


