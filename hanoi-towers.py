A=[]
B=[]
C=[]

for i in range(5,0,-1):
    A.append(i)

def printhanoi(source, target, helper):
    height = len(A)+len(B)+len(C)
    towers = []
    towers.append('--------')
    sa = 'S'if source == A else ('T'if target == A else 'H' )
    sb = 'S'if source == B else ('T'if target == B else 'H' )
    sc = 'S'if source == C else ('T'if target == C else 'H' )
    towers.append('  '.join([sa, sb, sc]))
    towers.append('--------')
    for i in range(height):
        sa = str(A[height-i-1]) if len(A) > height-i-1 else '|'
        sb = str(B[height-i-1]) if len(B) > height-i-1 else '|'
        sc = str(C[height-i-1]) if len(C) > height-i-1 else '|'
        towers.append('  '.join([sa, sb, sc]))
    towers.append('A--B--C-')
    towers.append('============')
    print('\n'.join(towers))
        
def hanoi(n, source, helper, target):
    
    if n > 0:
        printhanoi(source, target, helper)
        
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
       
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
        
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)

hanoi(len(A),A,B,C)
