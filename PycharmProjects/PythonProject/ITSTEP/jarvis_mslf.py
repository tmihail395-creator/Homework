import os
import sys
import webbrowser
import speech_recognition as sr


r = sr.Recognizer()
print("Джарвис запущен и слушает...")

while True:
    with sr.Microphone() as src:
        try:
            cmd = r.recognize_google(r.listen(src), language='ru-RU').lower()
            print(f"Вы сказали: {cmd}")
            if "google" in cmd:
                webbrowser.open("https://google.com")
            # elif "подрочить бы" in cmd:
            #     webbrowser.open("https://rt.pornhub.com/model/miulio")
            elif "джарвис включи музыку" in cmd:
                import time
                import keyboard
                webbrowser.open("spotify:album:2sLw919CrljXgUn2fpOOrl")
                time.sleep(2)
                keyboard.send("play/pause media")
            elif "хватит" in cmd:
                print("Джарвис отключается.")
                break
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Ошибка: Проверьте подключение к интернету для распознавания голоса.")
        except Exception as e:
            pass

