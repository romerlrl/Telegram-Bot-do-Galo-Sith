def identity(input_msg, output_msg, author = None):
    return output_msg.format(author = author)

def function_sabio(input_msg, output_msg, author = None):
    expr = input_msg.split(' ', 3)
    if len(expr)!=3:
        return ''
    suffix = expr[1][-1]
    if suffix == 's':
        suffix = expr[1][-2:]
    print("!", suffix)
    output_msg = f"Você já ouviu a história de Darth {expr[2]}, {suffix} {expr[1]}"
    return output_msg

functions = {
    'function_sabio': function_sabio
    
}

