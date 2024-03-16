from deep_translator import GoogleTranslator
import os
# Ruta del directorio actual
ruta_directorio = os.getcwd()

def translator(texto):
    traductor = GoogleTranslator(source='en', target='es')
    resultado = traductor.translate(texto)
    return resultado

def read_original_docs(files_to_translate):
    for index, file_name in enumerate(files_to_translate):
        print('\nComenzando a traducir')
        print(f"Traduciendo archivos...\nArchivo {index+1} de {len(files_to_translate)}\n")
        traduccion = []
        with open(file_name, "r") as archivo:
            # Lee el contenido del archivo
            for linea in archivo:
                # Imprime la línea actual
                linea = linea.strip()
                resultado = translator(linea)
                traduccion.append(resultado)
            save_translate_docs(traduccion, file_name)


def save_translate_docs(translate_doc, files_names):
    nombre, extension = files_names.split(".")
    nombre_sin_traducir = nombre.replace("traducir", "")
    nuevo_nombre_archivo = f"{nombre_sin_traducir}_traducido.{extension}"
    with open(nuevo_nombre_archivo, "w") as archivo_salida:
        # Itera sobre cada línea en la lista
        for linea in translate_doc:
            archivo_salida.write(linea + "\n")

def search_tranlator_docs():
    archivos_a_traducir = []
    apto = False
    for nombre_archivo in os.listdir(ruta_directorio):
        if 'traducir' in nombre_archivo.lower() and nombre_archivo.lower().endswith('.txt'):
            archivos_a_traducir.append(nombre_archivo)
            apto = True

    if apto:  
        print(f'\nSe han encontrado {len(archivos_a_traducir)} archivos para ser traducidos\n\n')
        read_original_docs(archivos_a_traducir)
        
    if apto == False:
        print("\nNo hay archivos txt que contengan 'traducir' en el nombre\n")
    
       
if __name__ == "__main__":
    path = "Documentation/readme.txt"
    search_tranlator_docs()

    