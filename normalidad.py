import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def prueba_de_normalidad(column, column_name):
    column = column.dropna()  # Eliminar valores NaN

    # Verificar que quedan datos para el análisis
    if column.empty:
        print(f"La columna '{column_name}' quedó vacía después de filtrar NaN y/o ceros. No se puede realizar la prueba de normalidad.\n")
        return

    ks_statistic, p_value = stats.kstest(column, 'norm', args=(np.mean(column), np.std(column)))

    # Imprimir los resultados
    print(f"Estadístico de prueba (ks_statistic) = {ks_statistic:.20f}")
    print(f"p-value = {p_value:.20f}")

    alpha = 0.05
    if p_value < alpha:
        print(f"Se rechaza la hipótesis nula: los datos de '{column_name}' NO provienen de una distribución normal.\n")
    else:
        print(f"No se rechaza la hipótesis nula: los datos de '{column_name}' parecen provenir de una distribución normal.\n")
    
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
    # Graficar histograma
    axes[0].hist(column, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    axes[0].set_title(f'Histograma de {column_name}')
    axes[0].set_xlabel(column_name)
    axes[0].set_ylabel('Frecuencia')

    # Graficar boxplot
    axes[1].boxplot(column)
    axes[1].set_title(f'Boxplot de {column_name}')
    axes[1].set_ylabel(column_name)

    # Mostrar gráficos
    plt.tight_layout()
    plt.show()
    
def frecuencias(column, column_name):
    frecuencia = column.value_counts()

    # Graficar frecuencias
    plt.figure(figsize=(10, 6))
    frecuencia.plot(kind='bar', color='skyblue', edgecolor='black', alpha=0.7)

    plt.title(f'Gráfico de {column_name}')
    plt.xlabel('Categorías')  # Categorías en el eje X
    plt.ylabel('Frecuencia')   # Frecuencia en el eje Y
    plt.xticks(range(len(frecuencia)), frecuencia.index, rotation=45, ha='right')  # Etiquetas del eje X
    plt.tight_layout()
    plt.show()