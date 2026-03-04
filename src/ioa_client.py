import os
import json
import requests
from dotenv import load_dotenv
import time
from datetime import datetime, timedelta

load_dotenv()

class IOAClient:
    """Client especializado para a API do Diário Oficial do Amazonas (IOA)"""
    
    def __init__(self, config_path="config.json"):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        contact = os.getenv("CONTACT_EMAIL", "contato_nao_configurado")
        prefix = self.config['crawler']['user_agent_prefix']
        
        self.headers = {
            "User-Agent": f"{prefix} ({contact})",
            "Accept": "application/json"
        }
        
        self.base_url = self.config['endpoints']['ioa_base_url']
        self.timeout = self.config['crawler']['timeout']

    def _get(self, endpoint: str):
        """função interna para requisições GET"""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição [{url}]: {e}")
            return None

    def get_by_date(self, date_str: str):
        """Busca edição pelo formato YYYY-MM-DD"""
        return self._get(f"edicoes_from_data/{date_str}.json")

    def get_latest(self):
        """Busca as últimas edições listadas"""
        return self._get("ultimas_edicoes.json")

if __name__ == "__main__":
    # test rapido
    client = IOAClient()
    print(f"Iniciado com User-Agent: {client.headers['User-Agent']}")
    
    resultado = client.get_latest()
    if resultado and not resultado.get('erro'):
        print(f"Conexão estabelecida. Último ID: {resultado['itens'][0]['id']}")

    # varias coletas pra ver noq q da
    dias_para_varrer = 60
    intervalo = client.config['crawler']['crawl_delay']
    data_fim = datetime.now()

    print(f"Iniciando coleta dos últimos {dias_para_varrer} dias...")

    coletas_sucesso = 0

    for i in range(dias_para_varrer):
        data_alvo = (data_fim - timedelta(days=i)).strftime("%Y-%m-%d")
        print(f" -> Verificando {data_alvo}...", end="\r")
        resultado = client.get_by_date(data_alvo)
        if resultado and not resultado.get('erro'):
            edicao = resultado['itens'][0]
            coletas_sucesso += 1
            print(f"Achado: ID {edicao['id']} | Edição {edicao['numero']} ({edicao['paginas']} pág.)")

        else:
            # sem edicao no dia, fim de semana ou feriado
            pass

        time.sleep(intervalo)

    print(f"\n Coletados {coletas_sucesso} edições com sucesso.")