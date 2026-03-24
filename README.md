# Sentinel-DO

O Sentinel-DO é um sistema de monitoramento automatizado para os atos oficiais do Estado do Amazonas e seus municípios. O software realiza a varredura, ingestão e indexação de publicações governamentais para identificar eventos específicos, como aberturas de licitações, editais de concursos e convocações de servidores.

O sistema atua na conversão de dados brutos, provenientes tanto de APIs quanto de arquivos PDF não estruturados, em registros processáveis, permitindo o rastreamento de palavras-chave e a geração de notificações em tempo real.

## Alvos iniciais
- [x] Diário Oficial do Estado do Amazonas
- [ ] Diário Oficial do Município de Manaus

## Objetivos do Projeto
O Sentinel-DO é orientado pela entrega de autonomia e agilidade no acesso a dados governamentais, focando nos seguintes pilares de valor:

- **Antecipação de Prazos:** Reduzir o intervalo entre a publicação oficial e a tomada de decisão, garantindo que o usuário identifique editais de licitação, convocações de concursos e prazos recursais no momento exato de sua disponibilidade.

- **Filtragem de Ruído Informacional:** Isolar termos críticos (ex: "Tomada de Preços", "Contratação", "Retificação") em meio ao volume massivo de páginas diárias, convertendo arquivos densos em alertas diretos e objetivos.

- **Consolidação de Fontes Fragmentadas:** Centralizar o monitoramento de múltiplas esferas em uma interface única, eliminando a necessidade de conferência manual em portais com padrões de entrega distintos.

- **Integridade e Rastreabilidade:** Manter um histórico persistente de edições processadas, assegurando que nenhuma publicação seja ignorada por falhas de rede, servindo como uma base de auditoria retroativa.

- **Independência de Verificação:** Prover uma ferramenta técnica capaz de extrair dados de documentos não estruturados (PDF), garantindo acesso à informação mesmo em municípios que não possuem infraestrutura de dados moderna.

## Como usar

Recomendamos o uso de um ambiente virtual para isolar as dependências:
```bash
    git clone https://github.com/AndreKaled/sentinel-do.git
    cd sentinel-do
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    # ou: venv\Scripts\activate (Windows)
    pip install -r requirements.txt
```

O sistema busca credenciais e níveis de log via variáveis de ambiente. Crie um arquivo `.env`:
```bash
cp .env.example .env
```
Edite o .env com seu e-mail (necessário para o User-Agent amigável) e o caminho do banco SQLite.

O ioa_client.py atua como o motor de busca (provisório) para o Diário Oficial do Amazonas. Executa a coleta das edições recentes do Diário Oficial:
```bash
python3 src/ioa_client.py
```
A saída gerada provavelmente será algo como:

```plaintext
Iniciado com User-Agent: Sentinel-DO/0.1 (meuemail@email.com)
Conexão estabelecida com a API IOA.
-> Verificando 2026-03-24... Achado: ID 12345 | Edição 35000 (120 pág.)
-> Verificando 2026-03-23... [Fim de Semana/Sem Edição]
```

## Status atual

O projeto encontra-se em fase inicial, com foco na coleta e validação de dados do Diário Oficial do Amazonas.

Funcionalidades implementadas:
- Coleta automatizada de edições via API
- Varredura histórica por data
- Controle de taxa de requisição

Próximas etapas:
- Download de PDFs e Docs
- Extração de conteúdo (PDF parsing)
- Busca por palavras-chave
- Sistema de notificações