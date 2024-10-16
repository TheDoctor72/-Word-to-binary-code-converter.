def text_to_binary(text):
    binary_result=''.join(format(ord(char),'08b')for char in text)
    return binary_result
text="Hello World"
binary= text_to_binary(text)
print(f'Original text: {text}')
print(f'Binary code:{binary}')