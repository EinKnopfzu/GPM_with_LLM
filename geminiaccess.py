import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

from google.colab import userdata

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

GOOGLE_API_KEY=userdata.get('AIzaSyDKynoUJbO9zj6XzSBpSfQ3fa0Ls8PYjp0')
genai.configure(api_key=GOOGLE_API_KEY)

