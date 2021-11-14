class DivStr(str):
    need_set = ['__getitem__', '__add__', '__mul__', ' __rmul__']

    def wrapper(fun, fun_name):
        def inner_fun(*args):
            ret_type = fun(*args)
            if isinstance(ret_type, str):
                return DivStr(ret_type)
            else:
                return ret_type

        inner_fun.__name__ = fun_name
        return inner_fun

    for func, obj in str.__dict__.items():
        if func == '__mul__':
            print()
        if callable(str.__getattribute__(str(str), func)) and (
                not func.startswith("__") or func in need_set or func == '__rmul__'):
            locals().update({func: wrapper(obj, func)})

    def __floordiv__(self, other):
        n = len(self)
        max_parts = n // other
        res = []
        i = 0
        if max_parts == 0:
            return [DivStr('')] * other

        while True:
            kusok = self[i * max_parts:(i + 1) * max_parts]
            if len(kusok) == max_parts:
                res.append(kusok)
                i += 1

            else:
                break

        return res

    def __mod__(self, other):
        n = len(self)
        rem = n % other
        return DivStr(self[n - rem:n])
