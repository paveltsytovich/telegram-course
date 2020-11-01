#
#
# Текст программы из статьи https://habr.com/ru/post/349860/ 
import re 
print(re.findall(r'\d+', '12 + ٦٧')) 
# -> ['12', '٦٧'] 
print(re.findall(r'\w+', 'Hello, мир!')) 
# -> ['Hello', 'мир'] 
print(re.findall(r'\d+', '12 + ٦٧', flags=re.ASCII)) 
# -> ['12'] 
print(re.findall(r'\w+', 'Hello, мир!', flags=re.ASCII)) 
# -> ['Hello'] 
print(re.findall(r'[уеыаоэяию]+', 'ОООО ааааа ррррр ЫЫЫЫ яяяя')) 
# -> ['ааааа', 'яяяя'] 
print(re.findall(r'[уеыаоэяию]+', 'ОООО ааааа ррррр ЫЫЫЫ яяяя', flags=re.IGNORECASE)) 
# -> ['ОООО', 'ааааа', 'ЫЫЫЫ', 'яяяя'] 

text = r""" 
Торт 
с вишней1 
вишней2 
""" 
print(re.findall(r'Торт.с', text)) 
# -> [] 
print(re.findall(r'Торт.с', text, flags=re.DOTALL)) 
# -> ['Торт\nс'] 
print(re.findall(r'виш\w+', text, flags=re.MULTILINE)) 
# -> ['вишней1', 'вишней2'] 
print(re.findall(r'^виш\w+', text, flags=re.MULTILINE)) 
# -> ['вишней2'] 