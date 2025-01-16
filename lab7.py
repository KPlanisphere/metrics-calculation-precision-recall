#C:\Users\mini_\AppData\Local\Programs\Python\Python312\python.exe "C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab7\lab7.py"

def read_relevance_file(file_path):
    relevance_dict = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        query = None
        relevant_docs = []
        for line in lines:
            if line.strip() == '/':
                relevance_dict[query] = relevant_docs
                query = None
                relevant_docs = []
            else:
                if query is None:
                    query = int(line.strip())
                else:
                    relevant_docs.extend(map(int, line.split()))
    return relevance_dict

def read_retrieval_file(file_path):
    retrieval_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            query, doc, cosine = line.split()
            query = int(query)
            doc = int(doc)
            cosine = float(cosine)
            if query not in retrieval_dict:
                retrieval_dict[query] = []
            retrieval_dict[query].append((doc, cosine))
    return retrieval_dict

def calculate_metrics(relevance_dict, retrieval_dict, z):
    results = []
    for query, relevant_docs in relevance_dict.items():
        retrieved_docs = sorted(retrieval_dict.get(query, []), key=lambda x: x[1], reverse=True)[:z]
        relevant_count = len(relevant_docs)
        retrieved_relevant_count = sum(1 for doc, _ in retrieved_docs if doc in relevant_docs)
        precision = retrieved_relevant_count / z if z != 0 else 0
        recall = retrieved_relevant_count / relevant_count if relevant_count != 0 else 0
        precision_r = 0 if relevant_count == 0 else sum(1 for doc, _ in retrieved_docs[:relevant_count] if doc in relevant_docs) / relevant_count
        f_measure = (2 * precision * recall) / (precision + recall) if (precision + recall) != 0 else 0
        results.append((query, precision, recall, f_measure, precision_r))
    return results


def write_results(results, output_file):
    with open(output_file, 'w') as file:
        file.write("| Consulta | Precision | Recuerdo | Medida F | Precision R |\n")
        file.write("|----------|-----------|----------|----------|-------------|\n")
        for query, precision, recall, f_measure, precision_r in results:
            file.write(f"| {query:<8} | {precision:.4f}    | {recall:.4f}   | {f_measure:.4f}   | {precision_r:.4f}      |\n")

def main():
    # DOCUMENTOS RELEVANTES
    relevance_file = r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab7\rlv-ass'
    # TF IDF
    retrieval_file = r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab7\NPL_tf_idf_rels.txt'
    # ARCHIVO DE SALIDA
    output_file = r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab7\metrics_results.txt'
    z = int(input("Ingrese el valor de Z (número de documentos): "))
    relevance_dict = read_relevance_file(relevance_file)
    retrieval_dict = read_retrieval_file(retrieval_file)
    results = calculate_metrics(relevance_dict, retrieval_dict, z)
    write_results(results, output_file)
    print("Métricas calculadas y guardadas correctamente en el archivo:", output_file)

if __name__ == "__main__":
    main()
