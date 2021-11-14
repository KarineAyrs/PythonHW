

class Tester:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, suite, allowed=[]):
        ex_num = 0
        allwd = False
        for els in suite:
            try:
                self.fun(*els)
            except Exception as ex:

                for al in allowed:
                    if isinstance(ex, al):
                        allwd = True

                if allwd:
                    ex_num = -1
                else:
                    ex_num = 1
                allwd = False

        return ex_num




