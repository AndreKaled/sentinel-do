# Sentinel-DO

O Sentinel-DO é um sistema de monitoramento automatizado para os atos oficiais do Estado do Amazonas e seus municípios. O software realiza a varredura, ingestão e indexação de publicações governamentais para identificar eventos específicos, como aberturas de licitações, editais de concursos e convocações de servidores.

O sistema atua na conversão de dados brutos, provenientes tanto de APIs quanto de arquivos PDF não estruturados, em registros processáveis, permitindo o rastreamento de palavras-chave e a geração de notificações em tempo real.

## Alvos iniciais
- [x] Diário Oficial do Estado do Amazonas
- [ ] Diário Oficial do Município de Manaus

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

## Funcionalidades atuais
- Coleta automatizada de edições via API
- Varredura histórica por data
- Controle de taxa de requisição

## Próximas etapas:
- Download de PDFs e documentos
- Extração de conteúdo (PDF parsing)
- Busca por palavras-chave
- Sistema de notificações
- OCR para documentos escaneados
- Modelagem de banco de dados 
- Estruturação e persistência de dados
- Estruturação de JSON para API

## Status atual
O projeto encontra-se em fase inicial, com foco na coleta e validação de dados do Diário Oficial do Amazonas.

## Documentação adicional

- [IDEIA.md](docs/IDEIA.md): visão geral, problema, solução e diferenciais
- [AI_CONTEXT.md](docs/AI_CONTEXT.md): contexto técnico e organizacional para uso de Agentes de IA
- [DEV_NOTES.md](docs/DEV_NOTES.md): dúvidas e anotações internas e pessoais
- [CONTRIBUTING.md](docs/CONTRIBUTING.md): guia para contribuições (FUTURO)
- [USER_STORIES.md](docs/USER_STORIES.md): histórias de usuários (FUTURO)
- [USER_CASES.md](docs/USER_CASES.md): atores, fluxos e cenários de uso (FUTURO)
- [REQUISITOS.md](docs/REQUISITOS.md): requisitos funcionais e não funcionais (FUTURO)