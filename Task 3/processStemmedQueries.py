q_id = 0
query_dict = dict()
for q_line in open(r'Input\cacm_stem.query.txt'):
    q_id += 1
    query_dict[q_id] = q_line.split()
outputFile = open(r'queries_stemmed.txt', 'w', encoding='utf8')
outputFile.write(str(query_dict))
outputFile.close()