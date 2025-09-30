# Demonstrates an insecure pattern (eval on user input)


def insecure_eval(expr: str):
# intentional insecure pattern for scanning (SAST should flag this)
 return eval(expr)