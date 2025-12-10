```python
from flask import Flask, render_template, request, jsonify
from app.knowledge_base import KnowledgeBase
from app.agent import ZoologyAgent

app = Flask(__name__)
kb = KnowledgeBase()
agent = ZoologyAgent(kb)

@app.route("/")
def index():
    animal_classes = kb.list_classes()
    return render_template("index.html", animal_classes=animal_classes)

@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.json
    user_query = data.get("query", "")
    animal_class = data.get("animal_class")
    answer = agent
