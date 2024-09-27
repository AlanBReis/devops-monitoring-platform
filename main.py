from app import create_app

# Cria a aplicação Flask
app = create_app()

if __name__ == "__main__":
    # Roda o servidor na porta 5000
    app.run(host='0.0.0.0', port=5000)
