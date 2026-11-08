import dns.resolver
import dns.exception


def analisar_dns(dominio):

    dominio = dominio.strip().lower().rstrip(".")

    if not dominio or "://" in dominio or "/" in dominio:
        return {"ERRO": "Informe somente o nome do domínio"}

    resultados = {}

    tipos = ["A", "AAAA", "MX", "NS"]

    for tipo in tipos:

        try:
            resposta = dns.resolver.resolve(
                dominio,
                tipo,
                lifetime=4
            )

            resultados[tipo] = [
                registro.to_text()
                for registro in resposta
            ]

        except dns.resolver.NXDOMAIN:
            resultados[tipo] = ["Domínio não encontrado"]
            break

        except dns.resolver.NoAnswer:
            resultados[tipo] = ["Nenhum registro encontrado"]

        except dns.exception.Timeout:
            resultados[tipo] = ["Tempo limite excedido"]

        except dns.resolver.NoNameservers:
            resultados[tipo] = ["Servidores DNS indisponíveis"]

        except Exception as erro:
            resultados[tipo] = [f"Erro: {erro}"]

    return resultados
