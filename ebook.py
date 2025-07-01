
# eBook
import pypdf
from gtts import gTTS

pdf_path = "C:\\Ramya\\New folder\\python_intro.pdf"

with open(pdf_path, "rb") as file:
    reader = pypdf.PdfReader(file)
    full_text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            full_text += page_text

start_marker = "Python Intro"
end_marker = "What is Coding?" 

start_index = full_text.find(start_marker)
end_index = full_text.find(end_marker)

if start_index != -1 and end_index != -1:
    selected_text = full_text[start_index:end_index].strip()
else:
    selected_text = "Requested section not found in the PDF."

with open("selected_text.txt", "w", encoding="utf-8") as f:
    f.write(selected_text)


tts = gTTS(selected_text, lang='en')
tts.save("python_intro_audio.mp3")
print("Audio saved as python_intro_audio.mp3")