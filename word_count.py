"""Taller evaluable"""


import os
import pandas as pd


# Directorio donde se encuentran los archivos de texto


def load_input(input_directory):
    """Load text files in 'input_directory/'"""
    # Lea los archivos de texto en la carpeta input/ y almacene el contenido en
    # un DataFrame de Pandas. Cada línea del archivo de texto debe ser una
    # entrada en el DataFrame

# Obtener la lista de archivos en la carpeta de entrada
    files = os.listdir(input_directory)

# Inicializar una lista para almacenar los datos de los archivos
    data = []


# Iterar sobre cada archivo en la carpeta de entrada
    for file_name in files:
    # Construir la ruta completa del archivo
       file_path = os.path.join(input_directory, file_name)
    # Verificar si es un archivo de texto
       if os.path.isfile(file_path) and file_name.endswith('.txt'):
        # Leer el contenido del archivo y dividirlo en líneas
            with open(file_path, 'r') as file:
                lines = file.readlines()
            # Agregar cada línea como una entrada en la lista de datos
                for line in lines:
                   data.append({'File': file_name, 'Content': line.strip()})

# Crear un DataFrame de Pandas a partir de los datos
    df = pd.DataFrame(data)

    return df

def clean_text(df):
    """Text cleaning"""
    #
    # Elimine la puntuación y convierta el texto a minúsculas.
    #
    # Definir una función para limpiar el texto
    def clean_text(text):
        # Eliminar puntuación y convertir a minúsculas
        cleaned_text = text.lower().strip()
        cleaned_text = ''.join(char for char in cleaned_text if char.isalnum() or char.isspace())
        return cleaned_text

    # Aplicar la función de limpieza a la columna 'Content' del DataFrame
    df['Content'] = df['Content'].apply(clean_text)
    return df

def word_count_dataframe(df):
    # Inicializar un diccionario para almacenar el recuento de palabras
    word_count = {}

    # Iterar sobre cada fila del DataFrame
    for index, row in df.iterrows():
        # Dividir el texto en palabras
        words = row['Content'].split()
        # Contar las palabras y actualizar el diccionario de recuento
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    # Convertir el diccionario de recuento en un DataFrame
    word_count_df = pd.DataFrame(word_count.items(), columns=['word', 'count'])
    return word_count_df

# Ejemplo de uso:
# Suponiendo que 'df' es el DataFrame con el texto limpio
# word_count_df = word_count_dataframe(df)



def save_output(dataframe, output_filename):
    """Save output to a file."""
    # Crear el nombre del archivo con extensión .txt si no está presente
    if not output_filename.endswith('.txt'):
        output_filename += '.txt'

    # Guardar el contenido en el archivo con formato adecuado
    with open(output_filename, 'w') as file:
        # Escribir cada fila del DataFrame en el archivo
        for index, row in dataframe.iterrows():
            file.write(f"{row['word']}\t{row['count']}\n")


#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    """Call all functions."""
    a=load_input(input_directory)
    b=clean_text(a)
    c=word_count_dataframe(b)
    d=save_output(c,output_filename)


if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
