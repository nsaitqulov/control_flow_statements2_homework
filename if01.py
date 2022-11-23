def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    w=a

    if a>w:
        w=a

    if b>w:
        w=b 

    if c>w:
        w=c
    return w
print(main(123, -12356, 258))