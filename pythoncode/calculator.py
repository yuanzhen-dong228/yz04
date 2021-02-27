class Calculator:
    def add(self, a, b):
        return a + b

    def div(self, a, b):
        try:
            a / b
        except:
            print('分母不能为零')
        return a / b
