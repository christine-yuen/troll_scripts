import sys

if __name__=='__main__':
    text = sys.argv[1]
    lw = [len(word) for word in text.split()]
    p = [c.lower() if (i%2==0) else c.upper() for i, c in enumerate(''.join(text.split()))]
    print(' '.join([''.join(p[max(sum(lw[:i-1]),0):sum(lw[:i])]) for i in range(len(lw)+1)]))
    