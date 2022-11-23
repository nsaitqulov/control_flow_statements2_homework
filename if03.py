def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>=b and b>=c:
        return(b)
    elif b>=a and a>=c:
        return(a)
    elif c>=a and c>=b:
        return(c)
print(main(123, 778, -2581))