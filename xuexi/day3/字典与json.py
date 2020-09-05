import json
d1 = { "a": None,"b": False,"c": True,"d": "BAB2",
       "e": ["1", 12],
       "f": ("1n", 90),
       "g": {"h": 1,"i": "11","j": True}
       }

print(type(d1))
print(d1)       #输出格式为字典

d1_js = json.dumps(d1)     # 字典转jsonprint(type(d1_js))
print(type(d1_js))
print(d1_js)

js_d1 = json.loads(d1_js)  # json转字典print(type(js_d1))print(js_d1)


#{'a': None, 'b': False, 'c': True, 'd': 'BAB2', 'e': ['1', 12], 'f': ('1n', 90), 'g': {'h': 1, 'i': '11', 'j': True}} #s输出各式为字典
#{"a": null, "b": false, "c": true, "d": "BAB2", "e": ["1", 12], "f": ["1n", 90], "g": {"h": 1, "i": "11", "j": true}}    输出格式为json


a='{"a":True,"b":"bbb"}'
b='{"a":true,"b":"bb"}'
print(eval(a))           #eval可以将字符串转换为字典
print(b)
