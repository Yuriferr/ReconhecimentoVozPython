import speech_recognition as sr

# Cria um objeto de reconhecimento de fala
r = sr.Recognizer()

# Captura o áudio do microfone
with sr.Microphone() as source:
    print("Fale algo...")
    audio = r.listen(source)

# Realiza a transcrição do áudio
try:
    text = r.recognize_google(audio, language="pt-BR")  # Transcrição em português

    # Imprime o texto transcritado
    print("Você disse: " + text)

except sr.UnknownValueError:
    print("Não foi possível transcrever o áudio")

except sr.RequestError:
    print("Erro na solicitação para a API")
