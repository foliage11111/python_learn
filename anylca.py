__author__ = 'y.foliage'
# ���ַ����л�ȡ������������ Token
def tokenize(string):
    buffer = Buffer(string)
    tk_int = TokenInt()
    tk_op = TokenOperator()
    tokens = []

    while buffer.peek():
        token = None
        # ���������͵� Token ���в���
        for tk in (tk_int, tk_op):
            token = tk.consume(buffer)
            if token:
                tokens.append(token)
                break
        # ��������ڿ���ʶ��� Token ��ʾ�������
        if not token:
            raise ValueError("Error in syntax")

    return tokens


# ���ַ����л�ȡ������������ Token
def tokenize(string):
    buffer = Buffer(string)
    tk_int = TokenInt()
    tk_op = TokenOperator()
    tokens = []

    while buffer.peek():
        token = None
        # ���������͵� Token ���в���
        for tk in (tk_int, tk_op):
            token = tk.consume(buffer)
            if token:
                tokens.append(token)
                break
        # ��������ڿ���ʶ��� Token ��ʾ�������
        if not token:
            raise ValueError("Error in syntax")

    return tokens


# ���ַ����л�ȡ������������ Token
def tokenize(string):
    buffer = Buffer(string)
    tk_int = TokenInt()
    tk_op = TokenOperator()
    tokens = []

    while buffer.peek():
        token = None
        # ���������͵� Token ���в���
        for tk in (tk_int, tk_op):
            token = tk.consume(buffer)
            if token:
                tokens.append(token)
                break
        # ��������ڿ���ʶ��� Token ��ʾ�������
        if not token:
            raise ValueError("Error in syntax")

    return tokens
