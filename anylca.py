__author__ = 'y.foliage'
# 从字符串中获取整数及操作的 Token
def tokenize(string):
    buffer = Buffer(string)
    tk_int = TokenInt()
    tk_op = TokenOperator()
    tokens = []

    while buffer.peek():
        token = None
        # 用两种类型的 Token 进行测试
        for tk in (tk_int, tk_op):
            token = tk.consume(buffer)
            if token:
                tokens.append(token)
                break
        # 如果不存在可以识别的 Token 表示输入错误
        if not token:
            raise ValueError("Error in syntax")

    return tokens


# 从字符串中获取整数及操作的 Token
def tokenize(string):
    buffer = Buffer(string)
    tk_int = TokenInt()
    tk_op = TokenOperator()
    tokens = []

    while buffer.peek():
        token = None
        # 用两种类型的 Token 进行测试
        for tk in (tk_int, tk_op):
            token = tk.consume(buffer)
            if token:
                tokens.append(token)
                break
        # 如果不存在可以识别的 Token 表示输入错误
        if not token:
            raise ValueError("Error in syntax")

    return tokens


# 从字符串中获取整数及操作的 Token
def tokenize(string):
    buffer = Buffer(string)
    tk_int = TokenInt()
    tk_op = TokenOperator()
    tokens = []

    while buffer.peek():
        token = None
        # 用两种类型的 Token 进行测试
        for tk in (tk_int, tk_op):
            token = tk.consume(buffer)
            if token:
                tokens.append(token)
                break
        # 如果不存在可以识别的 Token 表示输入错误
        if not token:
            raise ValueError("Error in syntax")

    return tokens
