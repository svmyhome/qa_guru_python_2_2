def only_print():
    print("Print")
only_print()

def print_with_arg(value):
    print(value)
print_with_arg(1)
print_with_arg("dfdgff")

def print_with_any_arg(*args):
    print(f"This is {args}")
    for i in args:
        print(i)
    print(f"This is one element", *args)
print_with_any_arg(3, 6)

def print_with_return(arg: str):
    return arg.title()
print(print_with_return("dsfddfdfs"))

def print_dict(**kwargs):
    print(kwargs)
    print(*kwargs)

print_dict(key=123, value=345)

def get_age_from_dict(d):
    return d["age"]

print(get_age_from_dict({"name": "Pety", "age":  11}))

users = [
    {"name": "Pety", "age":  17},
    {"name": "Pety", "age":  12},
    {"name": "Pety", "age":  13},
]

print(sorted(users, key=get_age_from_dict))
print(max(users, key=get_age_from_dict))
print(min(users, key=get_age_from_dict))