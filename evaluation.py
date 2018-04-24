

def precision_cal(rel_ret_count,retrieved_count):
    return rel_ret_count/retrieved_count

def recall_cal(rel_ret_count,relevant_count):
    return rel_ret_count/relevant_count

def avg_precision_cal(precision_table, relevant_docs, rel_ret_count):
    if rel_ret_count == 0:
        return 0
    sum = 0
    for docID in precision_table:
        if docID in relevant_docs:
            sum += precision_table[docID]
    return sum/rel_ret_count

def evaluation():
    relevance_dict = dict()
    file_contents = open("queryRelevance.txt", 'r', encoding='utf-8')
    relevance_dict = eval(file_contents.read())
    file_contents.close()
    top_100_dict = dict()
    file_contents = open("bm25_Ranking_TOP100_retrieved.txt", 'r', encoding='utf-8')
    top_100_dict = eval(file_contents.read())
    file_contents.close()
    num_of_queries = len(relevance_dict)

    # precision_table = dict()
    # recall_table = dict()
    newFile = open('bm25_precision_recall_table.txt', 'w', encoding='utf-8')
    MAP_numerator = 0
    MRR_numerator = 0

    for q_id in top_100_dict:
        if q_id in relevance_dict.keys():
            precision_table = dict()
            recall_table = dict()
            rel_docs_ranks_RR = []
            newFile.write("Query ID: "+str(q_id) + "\n")
            newFile.write("Rank   Relevance   Precision       Recall\n")
            rel_ret_count = 0
            retrieved_count = 0
            retrieved_docs = top_100_dict[q_id]
            for docID in retrieved_docs:
                relevance = "N"
                retrieved_count += 1
                if docID in relevance_dict[q_id]:
                    rel_ret_count += 1
                    relevance = "R"
                    rel_docs_ranks_RR.append(retrieved_count)
                precision = precision_cal(rel_ret_count, retrieved_count)
                recall = recall_cal(rel_ret_count, len(relevance_dict[q_id]))
                # precision_table[(q_id, docID)] = precision
                # recall_table[(q_id, docID)] = recall
                precision_table[docID] = precision
                recall_table[docID] = recall
                if retrieved_count == 5:
                    P_at_5 = precision
                if retrieved_count == 20:
                    P_at_20 = precision
                newFile.write(str(retrieved_count) + "         ")
                newFile.write(relevance + "         ")
                newFile.write(str(format(precision, '.4f')) + "         ")
                newFile.write(str(format(recall, '.4f')))
                newFile.write("\n")
            newFile.write("\n")
            MAP_numerator += avg_precision_cal(precision_table, relevance_dict[q_id], rel_ret_count)
            if rel_docs_ranks_RR:
                RR = 1/rel_docs_ranks_RR[0]
                MRR_numerator += RR

            newFile.write("P@5: " + str(P_at_5) + "\n")
            newFile.write("P@20: " + str(P_at_20) + "\n")
            newFile.write("\n")
            newFile.write("******************* End of query "+str(q_id)+" ***************************")
            newFile.write("\n")
            newFile.write("\n")

    MAP = MAP_numerator/num_of_queries
    MRR = MRR_numerator/num_of_queries

    newFile.write("MAP: " + str(MAP) + "\n")
    newFile.write("MRR: " + str(MRR) + "\n")
    newFile.write("*******************************************************************")
    newFile.close()




if __name__ == "__main__":
    evaluation()