import inspect
from pprint import pprint


class Class1():
    at = 1

    def test(x):
        pass


def introspection_info(obj=None, **kwargs):
    info_dic: dict = {}
    try:
        print(f'\n\033[93mИсследуем объект {obj.__name__}\033[0m')
    except AttributeError:
        print(f'\n\033[93mИсследуем объект {obj}\033[0m')
    print('Тип объекта:', type(obj), sep='\n\t')
    info_dic['type'] = type(obj)
    print('Атрибуты объекта:', dir(obj), sep='\n\t')
    info_dic['attributes'] = dir(obj)
    method_list = []
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        print(f'Имя: {attr_name:<20} Тип: {str(type(attr)):<40} Исполняемый: {callable(attr)}')
        if callable(attr):
            method_list.append(attr_name)
    info_dic['methods'] = method_list
    print('Модуль, к которому объект принадлежит:', inspect.getmodule(obj), sep='\n\t')
    info_dic['module'] = inspect.getmodule(obj)
    if inspect.isfunction(obj):
        sign = inspect.signature(obj)
        print('Передаваемый в функцию параметры:', sign.parameters, sep='\n\t')
        param_list = []
        for p_name, param in sign.parameters.items():
            param_list.append([param.name, param.default])
        info_dic['signature'] = param_list
        print('-' * 50)
    return info_dic


info = introspection_info(42)
print()
pprint(info)

info = introspection_info(introspection_info)
print()
pprint(info)

info = introspection_info(Class1)
print()
pprint(info)

