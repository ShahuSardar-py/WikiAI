from flask import Flask, request
from wiki import search_and_fetch
from LLM import get_response

app = Flask(__name__)


