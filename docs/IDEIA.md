# Sentinel-DO
## Visão geral
O Sentinel-DO é uma plataforma de monitoramento automatizado de Diários Oficiais voltada inicialmente ao Estado do Amazonas e seus municípios.

O objetivo é transformar documentos extensos, não estruturados e difíceis de navegar em informações claras, pesquisáveis e estruturadas.

A proposta é reduzir o tempo entre a publicação de um ato oficial e a tomada de decisão do usuário (sem depender da leitura manual de 99.999 páginas)

## Problema
Órgãos públicos publicam diariamente uma grande quantidade de informações em Diários Oficiais. Essas publicações costumam estar distribuídas em diferentes portais, formatos, padrões de acesso e informações importantes escondidas em meio a conteúdos administrativos pouco relevantes para o usuário

Na prática isso gera alguns problemas como:
- PDFs extensos com centenas de páginas
- Conteúdo pouco estruturado
- Dificuldade em localizar palavras-chaves importantes
- Falta de padronização entre municípios
- Perda de prazos por atraso na leitura ou na avalanche de conteúdo para ler
- Dependência de conferência diária em N sites

Para empresas, advogados, jornalistas, concurseiros e cidadãos em geral que desejam acompanhar, acompanhar essas publicações manualmente é cansativo, demorado e sujeito a falhas.

## Solução
O Sentinel-DO automatiza a coleta, processamento e análise de publicações oficiais

O sistema realiza:
  * Coleta automática de edições
  * Download de PDFs e documentos
  * Extração de texto
  * Indexação e armazenamento
  * Busca por palavras-chave
  * Classificação automática de atos
  * Geração de alertas
  * Criação de histórico e trilha de auditoria

Assim o usuário deixa de depender da leitura manual de centenas de páginas e passa a receber apenas os conteúdos relevantes para seu interesse

## Fontes iniciais
As primeiras integrações planejadas são:
  * Diário Oficial do Estado do Amazonas
  * Diário Oficial do Município de Manaus

No futuro o sistema poderá expandir para:
  * Diários de outros municípios do Amazonas
  * Portais de transparência
  * Tribunais
  * Assembléias legislativas
  * Câmaras municipais
  * Diários de outros Estados (sonho rsrs)

# Diferenciais
Não depender exclusivamente de APIs ou bases estruturadas, mesmo quando o dado estiver disponível apenas em PDF, imagem escaneada ou documento mal formatado, o sistema deve ser capaz de extrair informação por meio do OCR, parsing e processamento textual.

Principais diferenciais:
- Independência de infraestrutura governamental
- Centralização de múltiplas fontes
- Busca unificada
- Histórico persistente
- Alertas personalizados
- Foco regional
- Possibilidade de uso por pessoas sem conhecimento técnico

# Insights
- Disponibilizar uma API gratuita ou com limites maiores para uso acadêmico
- Criar planos diferentes para concurseiros, empresas, escritórios de advocacia, jornalistas
- Prever janelas de oportunidade (tendencia de abertura de editais) com base no comportamento histórico (analise de sazonalidade)
- Pode se tornar uma ferramenta de apoio para jornalismo investigativo e fiscalização pública
- Pode denunciar comportamentos estranhos como uma empresa concorrendo sozinha em uma licitação, uma empresa que vence repetitivamente, licitação aberta com prazo curto e critérios duvidosos
- Pode também existir uma feature que identifica empresas vencedoras recorrentes e sugere melhorias de preços ou serviços para quem deseja competir

# Hipóteses
- Usar OCR para leitura de PDFs e imagens
- Um classificador pode ser usado para separar automaticamente trechos relevantes de conteúdos pouco relevantes
- Um modelo de IA poderia resumir publicações em poucas linhas
- Técnicas de NLP podem ser usadas para identificar entidades como nomes, valores, datas, órgãos e CNPJ.
- Pode ser possível prever padrões de publicação, como épocas do ano com maior incidência de concursos ou licitações
- Treinar um modelo preditivo para avisar antecipadamente sobre publicações, com base no histórico já existente
