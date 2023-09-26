
import os
file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'prostitution.txt')

with open(file_name, 'r', encoding='utf-8') as f:
    text = f.read()
    print(text)