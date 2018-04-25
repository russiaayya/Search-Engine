
# function to compute precision
def precision_cal(rel_ret_count, retrieved_count):
    return rel_ret_count / retrieved_count

# function to compute recall
def recall_cal(rel_ret_count, relevant_count):
    return rel_ret_count / relevant_count

# function to compute average precision for a query
def avg_precision_cal(precision_table, relevant_docs, rel_ret_count):
    if rel_ret_count == 0:
        return 0
    sum = 0
    for docID in precision_table:
        if docID in relevant_docs:
            sum += precision_table[docID]
    return sum / rel_ret_count

# function to compute precision, recall, MAP, MRR and P@K
def evaluation(queryRelevanceFile, top100file, recallTableFile):

    # dictionary to hold query and its list of relevant documents
    relevance_dict = dict()
    file_contents = open(queryRelevanceFile, 'r', encoding='utf-8')
    relevance_dict = eval(file_contents.read())
    file_contents.close()

    # dictionary to hold query and its list of top 100 documents
    # from one of the retrieval systems
    top_100_dict = dict()
    file_contents = open(top100file, 'r', encoding='utf-8')
    top_100_dict = eval(file_contents.read())
    file_contents.close()

    # number of queries with relevance judgement
    num_of_queries = len(relevance_dict)

    # file that displays the evaluation results
    newFile = open(recallTableFile, 'w', encoding='utf-8')

    # holds the cumulative sum of average precision for each query
    MAP_numerator = 0
    # holds the cumulative sum of reciprocal rank for each query
    MRR_numerator = 0

    for q_id in top_100_dict:
        # process only if query has relevance judgement
        if q_id in relevance_dict.keys():
            # dictionary to hold the doc IDs and their precision values
            precision_table = dict()
            # dictionary to hold the doc IDs and their recall values
            recall_table = dict()
            # list to hold the relevant retrieved documents
            rel_docs_ranks_RR = []
            newFile.write("Query ID: " + str(q_id) + "\n")
            newFile.write("Rank      DocID       Relevance    Precision       Recall\n")
            # counter to keep track of the relevant retrieved documents
            rel_ret_count = 0
            # counter to keep track of the rank of the documents
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
                precision_table[docID] = precision
                recall_table[docID] = recall
                if retrieved_count == 5:
                    P_at_5 = precision
                if retrieved_count == 20:
                    P_at_20 = precision
                newFile.write(str(retrieved_count) + "       ")
                newFile.write(str(docID) + "         ")
                newFile.write(relevance + "         ")
                newFile.write(str(format(precision, '.4f')) + "         ")
                newFile.write(str(format(recall, '.4f')))
                newFile.write("\n")
            newFile.write("\n")
            MAP_numerator += avg_precision_cal(precision_table, relevance_dict[q_id], rel_ret_count)
            if rel_docs_ranks_RR:
                RR = 1 / rel_docs_ranks_RR[0]
                MRR_numerator += RR

            newFile.write("P@5: " + str(P_at_5) + "\n")
            newFile.write("P@20: " + str(P_at_20) + "\n")
            newFile.write("\n")
            newFile.write("******************* End of query " + str(q_id) + " ***************************")
            newFile.write("\n")
            newFile.write("\n")

    MAP = MAP_numerator / num_of_queries
    MRR = MRR_numerator / num_of_queries

    newFile.write("MAP: " + str(MAP) + "\n")
    newFile.write("MRR: " + str(MRR) + "\n")
    newFile.write("*******************************************************************")
    newFile.close()


if __name__ == "__main__":
    evaluation("queryRelevance.txt", "bm25_Ranking_TOP100_retrieved.txt", "bm25_Evaluation_table.txt")
    evaluation("queryRelevance.txt", "QLM_Ranking_TOP100_retrieved.txt", "QLM_Evaluation_table.txt")
    evaluation("queryRelevance.txt", "tfidf_TOP100_retrieved.txt", "tfidf_Evaluation_table.txt")
    evaluation("queryRelevance.txt", "lucene_TOP100_retrieved.txt", "lucene_Evaluation_table.txt")
    evaluation("queryRelevance.txt", "QueryEnriched_TOP100_retrieved.txt", "QueryEnriched_Evaluation_table.txt")
    evaluation("queryRelevance.txt", "BM25_task3_TOP100_retrieved.txt", "BM25_task3_Evaluation_table.txt")
    evaluation("queryRelevance.txt", "QLM_task3_TOP100_retrieved.txt", "QLM_task3_Evaluation_table.txt")
    evaluation("queryRelevance.txt", "tfidf_task3_TOP100_retrieved.txt", "tfidf_task3_Evaluation_table.txt")
    # evaluation("queryRelevance.txt", "bm25_Ranking_PRF.txt", "bm25_PRF_Evaluation_table.txt")

