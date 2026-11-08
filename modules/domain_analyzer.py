from urllib.parse import urlparse
from difflib import SequenceMatcher

MARCAS = {
    "instagram": "instagram.com",
    "facebook": "facebook.com",
    "google": "google.com"
}


def analisar_dominio(url):

    alertas = []

    try:
        dados = urlparse(url)
        dominio = dados.hostname

        if not dominio:
            return ["Domínio inválido"]

        dominio = dominio.lower().rstrip(".")

        # Detectar domínios internacionais codificados
        try:
            dominio = dominio.encode("idna").decode("ascii")
        except UnicodeError:
            return ["Domínio com codificação inválida"]

        partes = dominio.split(".")

        # Detectar Punycode
        if any(parte.startswith("xn--") for parte in partes):
            alertas.append(
                "Domínio contém caracteres internacionais codificados (Punycode)"
            )

        # Verificar imitação de marcas
        for marca, oficial in MARCAS.items():

            if dominio == oficial:
                continue

            if dominio.endswith("." + oficial):
                continue

            if marca in dominio:
                alertas.append(
                    f"Possível imitação da marca {marca}"
                )
                continue

            parte_principal = partes[0]

            similaridade = SequenceMatcher(
                None,
                parte_principal,
                marca
            ).ratio()

            if similaridade >= 0.80:
                alertas.append(
                    f"Possível domínio parecido com {marca}"
                )

        return alertas

    except Exception as erro:
        return [f"Erro na análise: {erro}"]
