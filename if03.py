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
    if (a>=b and a<=c) or (a<=b and a>=c):
        return a
    elif (b>=a and b<=c) or (b<=a and b>=c):
        return b
    elif (c>=a and c<=b) or (c>=b and c<=a):
        return c


print(main(123, 778, -2581))