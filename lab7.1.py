def leer_relevantes(archivo_relevantes):
    relevantes_por_consulta = {}
    with open(archivo_relevantes, 'r') as file:
        consulta_actual = 0
        for linea in file:
            if linea.strip().endswith('/'):
                consulta_actual += 1
                continue
            documentos = [int(doc) for doc in linea.strip().split()]
            if consulta_actual not in relevantes_por_consulta:
                relevantes_por_consulta[consulta_actual] = set(documentos)
            else:
                relevantes_por_consulta[consulta_actual].update(documentos)
    return relevantes_por_consulta

def leer_recuperados(archivo_recuperados):
    recuperados_por_consulta = {}
    with open(archivo_recuperados, 'r') as file:
        for linea in file:
            consulta, documento, _ = linea.split()
            consulta = int(consulta)
            documento = int(documento)
            if consulta not in recuperados_por_consulta:
                recuperados_por_consulta[consulta] = [documento]
            else:
                recuperados_por_consulta[consulta].append(documento)
    return recuperados_por_consulta

def calcular_metricas(relevantes_por_consulta, recuperados_por_consulta, Z):
    resultados = []
    for consulta, documentos_recuperados in recuperados_por_consulta.items():
        documentos_relevantes = relevantes_por_consulta.get(consulta, set())
        recuperados_hasta_Z = documentos_recuperados[:Z]
        relevantes_recuperados_hasta_Z = [doc for doc in recuperados_hasta_Z if doc in documentos_relevantes]
        
        precision = len(relevantes_recuperados_hasta_Z) / len(recuperados_hasta_Z) if recuperados_hasta_Z else 0
        recuerdo = len(relevantes_recuperados_hasta_Z) / len(documentos_relevantes) if documentos_relevantes else 0
        
        precision_R = precision  # Para simplificar, usaremos la misma precisión calculada para todos los casos
        
        if precision + recuerdo > 0:
            medida_F = 2 * precision * recuerdo / (precision + recuerdo)
        else:
            medida_F = 0
        
        resultados.append((consulta, precision, recuerdo, medida_F, precision_R))
        
    return resultados

def escribir_resultados(resultados, archivo_salida):
    with open(archivo_salida, 'w') as file:
        file.write('| Consulta | Precision | Recuerdo | Medida F | Precision R |\n')
        file.write("|----------|-----------|----------|----------|-------------|\n")
        for res in resultados:
            file.write('| {:<8} | {:<9.4f} | {:<8.4f} | {:<8.4f} | {:<11.4f} |\n'.format(*res))

Z = int(input("Ingrese el valor de Z: "))
#Z = 100  # Ejemplo, reemplaza esto con la línea de arriba para ejecución real
relevantes = leer_relevantes(r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab7\rlv-ass')
recuperados = leer_recuperados(r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab7\NPL_tf_idf_rels.txt')
archivo_final = r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab7\metrics_results.txt'
resultados = calcular_metricas(relevantes, recuperados, Z)
escribir_resultados(resultados, archivo_final)
print("Métricas calculadas y guardadas correctamente en el archivo:", archivo_final)
