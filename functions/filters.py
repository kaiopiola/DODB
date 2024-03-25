# Função para aplicar filtros aos dados
def apply_filters(data, filters):
    filtered_data = []
    for record in data:
        # Verifica se todas as condições do filtro são atendidas para o registro
        if all(apply_single_filter(record, f['key'], f['operator'], f['value']) for f in filters):
            filtered_data.append(record)
    return filtered_data

# Função para aplicar um único filtro a um registro
def apply_single_filter(record, key, operator, value):
    # Verifica se a chave existe no registro
    if key not in record:
        return False
    
    # Aplica a operação de filtragem com base no operador
    if operator == '=':
        return record[key] == value
    elif operator == '<':
        return record[key] < value
    elif operator == '>':
        return record[key] > value
    elif operator == '<=':
        return record[key] <= value
    elif operator == '>=':
        return record[key] >= value
    elif operator == 'LIKE':
        return value in record[key]
    elif operator == '<>':
        return record[key] != value
    else:
        # Padrão para igualdade se nenhum operador for especificado
        return record[key] == value
