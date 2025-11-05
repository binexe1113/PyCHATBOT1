from flask import Flask, render_template, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()
    return chatbot_response(user_message)


def chatbot_response(user_message: str):
    user_message = user_message.lower().strip()  # normalize input
    brasilia_tz = pytz.timezone("America/Sao_Paulo")
    current_time = datetime.now(brasilia_tz).strftime("%H horas, %M minutos e %S segundos")

    # === RESPOSTAS BASEADAS EM REGRAS ===
    match True: 
        case _ if "oi" in user_message or "olá"  in user_message or "ola" in user_message and "hora" in user_message or "agora" in user_message:
            return jsonify({"response": f"Oi! Tudo bem? Agora são {current_time} de acordo com o horário oficial de brasilia ⏰"})
        case _ if "oi" in user_message or "olá"  in user_message or "ola" in user_message:
            return jsonify({"response": "Oi! Tudo bem? 😊"})
        case _ if "hora" in user_message or "agora" in user_message:
            return jsonify({"response": f"Agora são {current_time} de acordo com o horário oficial de brasilia ⏰"})
        case _ if "obrigado" in user_message:
            return jsonify({"response": "De nada! 😊"})
        case _ if "sair" in user_message:
            return jsonify({"response": "Tchau! 👋"})
        case _:
            return jsonify({"response": "Ainda não tenho as capacidades para responder essa pergunta :C"})


if __name__ == "__main__":
    app.run(debug=True)
