MNK_input=input('Enter M, N and k:')
MNK=[int(x) for x in MNK_input.split()]
M=MNK[0]
N=MNK[1]
K=MNK[2]

push_sequence=[i for i in range(1,N+1)]

def check_sequence(push_sequence, check_sequence):
    stack=[]
    for check in push_sequence:
        stack.append(check)
        for stack_check in range(len(stack)):
            if stack[-1]==check_sequence[0]:
                stack.pop()
                check_sequence.pop(0)
            elif stack[-1]!=check_sequence[0]:
                break
    if check_sequence==[]:
        return True
    else: return False


for i in range(K):
    sequence_origin=input('Enter sequence:')
    sequence=[int(x) for x in sequence_origin.split()]
    if check_sequence(push_sequence, sequence):
        print ('Yes')
    else:
        print('No')