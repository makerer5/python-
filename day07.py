def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '',' ':''})
    translated_card_number = card_number.translate(card_translation)
    print(translated_card_number)
main()
# str.maketrans功能可以让你替换字符中的任何变量



# 切片 适用于字符串，列表，元组
''' 在 Python 中，字符串可以使用切片（slice）来获取子字符串。
切片操作的一般形式为 my_string[start:stop:step]，其中：
start 是切片开始的位置，如果省略，默认从序列的开始处（索引 0）。
stop 是切片结束的位置，但不包括此位置的元素。如果省略，默认直到序列的结束。
step 是步长，表示取值的间隔。如果省略，默认为 1，即不跳过任何元素。，当步长为负数时，序列从后向前被遍历
'''

# 学习Luhn AIgorithm算法 
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1] # 反转信用卡，从最后一位开始
    # 从反转后的卡号中取出每个奇数位置的数字。由于字符串索引从0开始，奇数位置的索引在这里表现为偶数（例如，第一个字符的索引是0，但它实际上是第1位）。
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()