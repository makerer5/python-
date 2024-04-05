# 字典
'''
字典采用{}表示，其中包含用逗号分隔的键值对，每个键后跟着一个冒号：和值
'''

dictroy = {'list':2,'values':36,'amount':50.0}
print(dictroy['list']) #通过字典中的键来访问值，使用[]，并把键包含在[]之间

# 格式化字符串加字典联合使用
print(f'List: {dictroy["list"]}')
# 在上述例子中，我们引用字典中的键时使用了“”，这是为了避免与''起冲突。具体可见‘python中引号'这一节的解释

test = lambda x: x * 2
print(test(3))
# lambda函数可作为基础函数调用

'''
lambda 函数是一种快速定义单行函数的方法，常用于需要函数对象的地方，而又不想用 def 关键字显式地定义函数体的情况。lambda 函数的基本语法是：
'''
lambda arguments: expression

__name__ # 变量
'''
如果你想要一个文件即可以独立执行也可以作为模块被其他文件导入并使用其函数或类时。可以使用___name___
这样可以提供灵活性，使得代码既可以作为脚本运行，也可以作为库的一部分被重用。
'''
# 假设有一个名为 example.py 的文件：
def function():
    print("Function is called.")

if __name__ == "__main__":
    print("Script is running directly.")
    function()
else:
    print("Script is imported into another module.")

# 当你直接运行 example.py 时，输出会是：
'''
Script is running directly.
Function is called.
'''
# 这是因为 __name__ == "__main__" 这个条件被满足了，所以 if 语句块中的代码被执行。

# 然而，如果你有另一个 Python 文件，比如说 import_example.py，并且在里面写上 import example，当 import_example.py 被运行时，example.py 文件中的输出会是：
'''
Script is imported into another module.
'''

# 这是因为当 example.py 被导入时，__name__ 的值不再是 "__main__"，而是模块名 "example"，所以 if 语句块中的代码不会被执行，else 语句块中的代码会被执行。
# 通过这种方式，你可以控制哪些代码只在脚本作为主程序运行时执行，而在脚本被导入时不执行。这对于避免执行脚本中的某些操作，如单元测试或只有在脚本被直接执行时才有意义的操作，非常有用。


# 以下是一个 learn Lambda functions by building an expense tracker 项目
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            print('Exiting the program.')
            break

main()
if __name__ == '__main__':
    main()