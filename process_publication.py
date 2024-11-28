import sys

block = [] 
with open(sys.argv[1], 'r') as f:
    for line in f:
        if line.strip().startswith('@'):
            if len(block) == 0:
                block.append(line)
            else:
                flag = False
                # print(block)
                for x in block:
                    if 'year=' in x:
                        flag = True

                if flag:
                    print(''.join(block))
                block = [line]
        else:
            block.append(line)
