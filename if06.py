def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a=n%10
    n//=10

    b=n%10
    n//=10

    c=n%10
    n//=10

    d=n%10
    n//=10

    e=n%10

    if a>b and a>c and a>d and a>e:
        return len(str(a))
    
    elif b>a and b>c and b>d and b>e:
        return len(str(b*10+a))
    
    elif c>a and c>b and c>d and c>e:
        return len(str(c*100+b*10+a))
    
    elif d>a and d>b and d>c and d>e:
        return len(str(d*1000+c*100+b*10+a))
    
    elif e>a and e>b and e>c and e>d:
        return len(str(e*10000+d*1000+c*100+b*10+a))

print(main(54694))
