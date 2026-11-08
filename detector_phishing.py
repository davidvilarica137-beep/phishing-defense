from urllib.parse import urlparse

SINAIS_SUSPEITOS = [
    "login",
    "verify",
    "account",
    "password",
    "secure",
    "free"
]

def analisar_url(url):

    resultado = []

    try:
        dados = urlparse(url)

        if dados.scheme != "https":
            resultado.append("URL sem HTTPS")

        if "@" in dados.netloc:
            resultado.append("Possível disfarce de endereço")

        if len(url) > 100:
            resultado.append("URL muito longa")

        for palavra in SINAIS_SUSPEITOS:
            if palavra in url.lower():
                resultado.append(
                    f"Palavra suspeita: {palavra}"
                )

        if resultado:
            print("\n[ALERTA] Características suspeitas:")
            for item in resultado:
                print("-", item)
        else:
            print("\nNenhum sinal simples encontrado.")

    except Exception as erro:
        print("Erro:", erro)


url = input("Digite uma URL para analisar: ")
analisar_url(url)
