from flask import Blueprint, render_template
import psutil

# Criação do blueprint para rotas
main = Blueprint('main', __name__)

@main.route("/")
def index():
    # Coleta as métricas do sistema usando a biblioteca psutil
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()

    # Passa as métricas para o template HTML
    return render_template("index.html", cpu_usage=cpu_usage, memory_info=memory_info)
