import nltk

try:
    nltk.download('punkt')
    print("NLTK punkt descargado correctamente")
except Exception as e:
    print("error durante la descarga",e)
        