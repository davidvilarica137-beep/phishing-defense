from modules.dns_analyzer import analisar_dns


class FakeRecord:
    def __init__(self, valor):
        self.valor = valor

    def to_text(self):
        return self.valor


def test_consulta_dns(monkeypatch):

    registros = {
        "A": ["203.0.113.10"],
        "AAAA": ["2001:db8::1"],
        "MX": ["10 mail.example.com."],
        "NS": ["ns1.example.com."]
    }

    def fake_resolve(dominio, tipo, lifetime):
        return [
            FakeRecord(valor)
            for valor in registros[tipo]
        ]

    monkeypatch.setattr(
        "modules.dns_analyzer.dns.resolver.resolve",
        fake_resolve
    )

    resultado = analisar_dns("example.com")

    assert resultado["A"] == ["203.0.113.10"]
    assert resultado["AAAA"] == ["2001:db8::1"]
    assert resultado["MX"] == ["10 mail.example.com."]
    assert resultado["NS"] == ["ns1.example.com."]


def test_dominio_invalido():

    resultado = analisar_dns(
        "https://example.com"
    )

    assert "ERRO" in resultado
