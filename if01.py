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
        W=b 

    if c>w:
        w=c
    return W
print(main(1, 5, 4))