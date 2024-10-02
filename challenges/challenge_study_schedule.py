def study_schedule(permanence_period, target_time):
    # Verificar se target_time é None
    if target_time is None:
        return None
    
    # Inicializar contador
    count = 0
    
    # Iterar sobre cada período de permanência
    for period in permanence_period:
        # Verificar se a tupla é válida
        if not isinstance(period, tuple) or len(period) != 2:
            return None
        start, end = period
        # Verificar se os elementos da tupla são inteiros
        if not isinstance(start, int) or not isinstance(end, int):
            return None
        # Verificar se o target_time está dentro do período
        if start <= target_time <= end:
            count += 1
    
    return count