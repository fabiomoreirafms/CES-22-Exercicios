
def decorador_padrao(func):
    def func_wrapper(nome, **kwargs):
        return "Decorador {0} Decorador".format(func(nome, **kwargs))
    return func_wrapper


@decorador_padrao
def get_adress (nome, **enderecos):
    return "{0} mora em {1}".format(nome, enderecos[nome])

print(get_adress("abc",**{"abc": "Alfabeto" }))