import io
import os
import tkinter
from flask import Flask, jsonify
from tkinter import filedialog
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import TextConverter
from collections import Counter
import pprint
from flask_cors import CORS
import google.generativeai as palm
from dotenv import load_dotenv
import os
load_dotenv()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service.json'
palm.configure(api_key=os.getenv("PALM_API_KEY"))
print(os.getenv("PALM_API_KEY"))
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
root = tkinter.Tk()

# Hide unnecessary GUI element
root.withdraw()
filename = filedialog.askopenfilename()
print(filename)
print('Processing file...')

# Edit keyword_num to set the number of keywords
keyword_num = 20

resource_manager = PDFResourceManager()
fake_file_handle = io.StringIO()
converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
page_interpreter = PDFPageInterpreter(resource_manager, converter)

with open(filename, 'rb') as file:
    for page in PDFPage.get_pages(file, caching=True, check_extractable=True):
        page_interpreter.process_page(page)

    text = fake_file_handle.getvalue()

converter.close()
fake_file_handle.close()

words = text.lower().replace('\n', ' ').split(' ')

words = list(filter(''.__ne__, words))
stopwords = set(open(str(os.path.dirname(os.path.abspath(__file__))) + '/stopwords_english', 'r').read().splitlines())
filtered_words = []

# filtering words such that they don't repeat
def filter_function(x):
    if x not in stopwords:
        filtered_words.append(x)

list(map(filter_function, words))
word_frequency = Counter(filtered_words)
keywords = [word for word, _ in word_frequency.most_common(keyword_num)]

# Store keywords in a new array
new_array = keywords

print(new_array)


# ret(new_array)



# def text_to_wav(text: str, title, dest, voice_name = "en-IN-Wavenet-A"):
#     language_code = "-".join(voice_name.split("-")[:2])
#     text_input = tts.SynthesisInput(text=text)
#     voice_params = tts.VoiceSelectionParams(
#         language_code=language_code, name=voice_name
#     )
#     audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16,
#                                    speaking_rate=0.8)

#     client = tts.TextToSpeechClient()
#     response = client.synthesize_speech(
#         input=text_input,
#         voice=voice_params,
#         audio_config=audio_config,
#     )
    
#     filename = f"{dest + '/' + 'test_audio'}.wav"
#     with open(filename, "wb") as out:
#         out.write(response.audio_content)
#         print(f'Generated speech saved to "{filename}"')

#     return filename



def generate_summary(keywords: list) -> str:
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name

    # Create a prompt using the provided keywords
    prompt = f"Generate a comprehensive summary on the topic related to {', '.join(keywords)} that helps students for last-minute revision. Provide information about key concepts, applications, and significance"

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0.7,
        top_p=0.95,
        top_k=40,
        max_output_tokens=1024,
    )

    content = completion.result
    content = content.encode().decode('unicode_escape')
    summary = content[content.find('\n'):]
    summary = summary.lstrip()
    # audio_file = text_to_wav(summary, 'test_audio', "./audios")
    

    return summary



@app.route('/get_summary',methods=['GET'])
def return_summary():
    summary=generate_summary(new_array)
    print(summary)
    return jsonify({"result": summary})

# print(f"Summary: {summary}\n")

if __name__ == '__main__':
    app.run(port=5001)