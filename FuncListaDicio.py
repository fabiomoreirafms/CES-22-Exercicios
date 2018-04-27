
def imprime_endereco(*args, **kwargs):
    def text_decorator(func):
        def wrapper(nome):
            return "{0} mora em {1}".format(nome, func(nome))
        return wrapper

    @text_decorator
    def get_adress(nome):
        return kwargs.get(nome, "nowhere")

    for arg in args:
        print (get_adress(arg))

imprime_endereco(*["a", "b", "c", "d"], **{"a": "A", "d":"D"})