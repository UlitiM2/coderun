queue = []

while True:
    cmd = input().split()
    if cmd[0] == 'push':
        queue.append(cmd[1])
        print('ok')
    elif cmd[0] == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print('error')
    elif cmd[0] == 'pop':
        if len(queue) != 0:
            print(queue[0])
            queue.pop(0)
        else:
            print('error')
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'clear':
        queue = []
        print('ok')
    elif cmd[0] == 'exit':
        print('bye')
        break
