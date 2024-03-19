# str 字符串一旦定义后就不允许更改，但可以重新赋值一个相同名字的字符串
# 两个相同名字的str， python只会引用最后一个
text = 'hello world'
text = '你好，世界'
print(text)

# Comparison operators 比较运算符
'''
比较运算符允许您根据两个对象的值对它们进行比较。将比较运算符放在要比较的对象之间，就可以使用比较运算符。
比较运算符会根据表达式的真假返回一个布尔值，即 True 或 False。
'''
# Python has the following comparison operators:
'''
Operator	Meaning
==	Equal
!=	Not equal
>	Greater than
<	Less than
>=	Greater than or equal to
<=	Less than or equal to
'''
# 加密与解密
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]  # 通过取key_index对密钥长度的模，确保当消息长度超过密钥长度时，密钥循环使用。
            key_index += 1
            
            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            # 计算新字符的索引。加密时（direction=1），字符索引向前移动offset个位置；解密时（direction=-1），向后移动offset个位置。模len(alphabet)确保索引值不超出字母表范围
            new_index = (index + offset*direction) % len(alphabet)  
            final_message += alphabet[new_index]

    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')