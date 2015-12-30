# input polynormial
def input_polynormial():
    seq_input = input('Enter your sequence:')
    seq = [int(i) for i in seq_input.split()]
    return [seq[0], seq[1::2], seq[2::2]]


# polynormial add
def polynormial_add(seq1, seq2):
    coef1 = seq1[1][:]
    coef2 = seq2[1][:]
    expon1 = seq1[2][:]
    expon2 = seq2[2][:]
    seq_add = []
    while (expon1 != []) & (expon2 != []):
        if expon1[0] == expon2[0]:
            seq_add.append(coef1.pop(0)+coef2.pop(0))
            seq_add.append(expon1.pop(0))
            del expon2[0]
        elif expon1[0] > expon2[0]:
            seq_add.append(coef1.pop(0))
            seq_add.append(expon1.pop(0))
        elif expon2[0] > expon1[0]:
            seq_add.append(coef2.pop(0))
            seq_add.append(expon2.pop(0))
    while expon1 != []:
        seq_add.append(coef1.pop(0))
        seq_add.append(expon1.pop(0))
    while expon2 != []:
        seq_add.append(coef2.pop(0))
        seq_add.append(expon2.pop(0))
    return seq_add


def polynormial_mul(seq1, seq2):
    coef1 = seq1[1][:]
    coef2 = seq2[1][:]
    expon1 = seq1[2][:]
    expon2 = seq2[2][:]
    coef_mul = []
    expon_mul = []

    for i in range(len(expon2)):  # 序列1第一项与序列2所有项相乘形成原始数组
        coef_mul.append(coef1[0] * coef2[i])
        expon_mul.append(expon1[0] + expon2[i])

    for i in range(1, len(expon1)):
        for j in range(len(expon2)):
            coef_node = coef1[i] * coef2[j]
            expon_node = expon1[i] + expon2[j]
            expon_mul, n_index = seq_insert(expon_mul, expon_node)
            coef_mul.insert(n_index, coef_node)

    seq_mul = []
    for i in range(len(expon_mul)):
        seq_mul.append(coef_mul[i])
        seq_mul.append(expon_mul[i])

    return seq_mul


def seq_insert(insert_list, node):  # 序列中插入节点
    nodeindex=0
    for i in range(len(insert_list)):
        if node >= insert_list[i]:
            insert_list.insert(i, node)
            nodeindex = i
            break
    if node < insert_list[-1]:
        insert_list.append(node)
        nodeindex = len(insert_list)
    return insert_list, nodeindex


polynormial_1 = input_polynormial()
polynormial_2 = input_polynormial()
print(polynormial_mul(polynormial_1, polynormial_2))
print(polynormial_add(polynormial_1, polynormial_2))
