stack = []
class error(Exception): pass

def push(obj):
    global stack
    stack = [obj] + stack

def pop():
    global stack
    if not stack:
        raise error('Stack underflow')
    top, *stack = stack
    return top

def top():
    if not stack:
        raise error('Stack underflow')
    return stack[0]

def empty(): return not stack                #判断栈是否为空
def member(obj): return obj in stack         #判断元素是否存在
def item(offset): return stack[offset]       #根据位置返回栈中元素
def length(): return len(stack)              #返回栈长度
def dump(): print('<Stack:%s>' % stack)
