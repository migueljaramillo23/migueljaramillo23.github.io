from chatbot.data import training_data
from chatbot.model import build_and_train_model, predict_answer, load_model

def chat(model,vectorizer,unique_answers):
    """inicia el modelo de conversacion"""
    print("\n 💬 chat iniciando. escribe salir para terminar \n")
    while True:
        user = input("Tú: ").strip()
        if user.lower() in {"salir", "exit", "quit"}:
            print("Bot: ¡Hasta pronto!")
            break
        response = predict_answer(model, vectorizer,unique_answers, user)  
        print("Bot:", response)
    
   
def main():
    #intenta cargar el modelo
    model, vectorizer, unique_answers = load_model()
    #menu principal
    while True:
        print("\n=== 🤖 MENU PRINCIPAL DEL CHATBOT ===")
        print("  1️⃣  chatea con el modelo")
        print("  2️⃣  reentrar el modelo")
        print(" 3️⃣  salir")
        opcion= input("\n elige una opcion (1-3): ").strip()
        if opcion == "1":
            if model is None:
                print("\n🩻 no hay modelo entrenado. entrenalo primero")
            else:
                chat( model, vectorizer, unique_answers)
                
        elif  opcion == "2":
            print("\n ♻️ reentrenando el modelo con los nuevos datos...")
            model, vectorizer, unique_answers=build_and_train_model(training_data)
            print("🆗 modelo actualizado correctamente")
        elif opcion== "3":
            print("\n 👍 !hasta luego¡")
            break
        else:
            print("\n ✖️ opcion no valida. intenta nuevamente")
        
        
                   
                   
if __name__ == "__main__":
    main()
