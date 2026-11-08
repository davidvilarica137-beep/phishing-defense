from urllib.parse import urlparse
import ipaddress


def analisar_url(url):

    alertas = []

    dados = urlparse(url)

    # Verificar protocolo
    if dados.scheme != "https":
        alertas.append("URL não utiliza HTTPS")

    # Verificar endereço vazio
    if not dados.hostname:
        alertas.append("Endereço inválido")

        return alertas

    # Verificar tamanho
    if len(url) > 100:
        alertas.append("URL excessivamente longa")

    # Verificar caractere @
    if "@" in dados.netloc:
        alertas.append("Possível disfarce de endereço")

    # Verificar se o domínio é um IP
    try:
        ipaddress.ip_address(dados.hostname)
        alertas.append("Domínio utiliza endereço IP")

    except ValueError:
        pass

    return alertas
