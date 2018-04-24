

def evaluation():
    relevance_dict = dict()
    for line in open(r'cacm.rel.txt'):
        r_list = line.split()
        q_id = r_list[0]
        if q_id not in relevance_dict:
            relevance_dict[q_id] = [r_list[2]]
        else:
            relevance_dict[q_id].append(r_list[2])

    print (relevance_dict)


if __name__ == "__main__":
    evaluation()