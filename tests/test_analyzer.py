from modules.url_analyzer import analisar_url
from modules.domain_analyzer import analisar_dominio


# TESTES DO ANALISADOR DE URL

def test_https():
    resultado = analisar_url("https://example.com")
    assert resultado == []


def test_http():
    resultado = analisar_url("http://example.com")
    assert "URL não utiliza HTTPS" in resultado


def test_ip():
    resultado = analisar_url("http://192.168.1.1")
    assert "Domínio utiliza endereço IP" in resultado


def test_url_longa():
    url = "https://example.com/" + ("a" * 110)
    resultado = analisar_url(url)
    assert "URL excessivamente longa" in resultado


# TESTES DO ANALISADOR DE DOMÍNIOS

def test_instagram_legitimo():
    resultado = analisar_dominio(
        "https://www.instagram.com"
    )
    assert resultado == []


def test_instagram_falso():
    resultado = analisar_dominio(
        "https://instagrarn.com"
    )
    assert len(resultado) > 0


def test_subdominio_enganoso():
    resultado = analisar_dominio(
        "https://instagram.com.exemplo.net"
    )
    assert len(resultado) > 0
def test_punycode():
    resultado = analisar_dominio(
        "https://xn--pple-43d.com"
    )

    assert any(
        "Punycode" in alerta
        for alerta in resultado
    )
