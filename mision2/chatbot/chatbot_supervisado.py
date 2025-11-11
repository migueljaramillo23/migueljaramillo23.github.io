from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def build_and_train_model(train_pairs):
    questions = [q for q, _ in train_pairs]
    answers = [a for _, a in train_pairs]

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(questions)

    unique_answers = sorted(set(answers))
    answers_to_label = {a: i for i, a in enumerate(unique_answers)}
    y = [answers_to_label[a] for a in answers]

    model = MultinomialNB()
    model.fit(X, y)
    return model, vectorizer, unique_answers

def predict_answer(model, vectorizer, unique_answers, user_text):
    x = vectorizer.transform([user_text])
    label = model.predict(x)[0]
    return unique_answers[label]

if __name__ == "__main__":
    training_data = [
        ("hola", "¡Hola! ¿En qué puedo ayudarte?"),
        ("buenos días", "¡Buenos días!"),
        ("cómo estás", "Estoy bien, gracias por preguntar."),
        ("adiós", "¡Hasta luego!"),
        ("tu nombre", "Soy un chatbot de ejemplo."),
        ("qué puedes hacer", "Puedo responder preguntas simples basadas en ejemplos."),
        ("quién eres", "Soy un asistente virtual programado para ayudarte."),
        ("qué puedes hacer", "Puedo responder preguntas simples, saludar y dar información básica."),
        ("qué haces", "Estoy aquí para ayudarte a resolver tus dudas."),
        ("dónde estás", "Estoy en la nube, listo para ayudarte desde cualquier lugar."),
        ("qué hora es", "No tengo un reloj, pero puedes verla en tu dispositivo."),
        ("qué día es hoy", "Puedes verificar el calendario en tu dispositivo, pero puedo ayudarte con fechas si me las das."),
        ("me puedes ayudar", "¡Claro que sí! Dime en qué necesitas ayuda."),
        ("ayúdame", "Por supuesto, dime con qué necesitas ayuda."),
        ("gracias", "¡De nada! Siempre estoy para ayudar."),
        ("muchas gracias", "No hay de qué, es un placer ayudarte."),
        ("ok", "Perfecto "),
        ("vale", "¡Genial!"),
        ("sí", "De acuerdo."),
        ("no", "Entendido."),
        ("qué tal", "Todo bien, gracias por preguntar."),
        ("qué haces ahora", "Estoy esperando tus preguntas."),
        ("cómo te llamas", "Me llamo Chatbot de ejemplo."),
        ("cuántos años tienes", "No tengo edad, soy un programa."),
    ]

    model, vectorizer, unique_answers = build_and_train_model(training_data)
    print("Chatbot supervisado listo. Escribe 'salir' para terminar.\n")

    while True:
        user = input("Tú: ").strip()
        if user.lower() in {"salir", "exit", "quit"}:
            print("Bot: ¡Hasta pronto!")
            break

        response = predict_answer(model, vectorizer, unique_answers, user)  
        print("Bot:", response)