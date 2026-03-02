# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto

## Nome do grupo

## 👨‍🎓 Integrantes:

- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 1</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 2</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 3</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 4</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 5</a>

## 👩‍🏫 Professores:

### Tutor(a)

- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Tutor</a>

### Coordenador(a)

- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Coordenador</a>

## 📜 Descrição

_Descreva seu projeto com base no texto do PBL (até 600 palavras)_

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

_Acrescentar as informações necessárias sobre pré-requisitos (IDEs, serviços, bibliotecas etc.) e instalação básica do projeto, descrevendo eventuais versões utilizadas. Colocar um passo a passo de como o leitor pode baixar o seu código e executá-lo a partir de sua máquina ou seu repositório. Considere a explicação organizada em fase._

## 🗃 Histórico de lançamentos

- 0.5.0 - XX/XX/2024
  -
- 0.4.0 - XX/XX/2024
  -
- 0.3.0 - XX/XX/2024
  -
- 0.2.0 - XX/XX/2024
  -
- 0.1.0 - XX/XX/2024
  -

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

# CardioIA: Fase 1 - Batimentos de Dados 🫀🤖

Bem-vindo ao repositório da **Fase 1 do projeto CardioIA**. Este projeto representa a etapa fundamental na construção de uma plataforma digital avançada idealizada para revolucionar o ecossistema de uma cardiologia moderna através da Inteligência Artificial.

Nesta fase — focada inteiramente na engenharia de dados, curadoria e **Governança de Dados** —, nós assumimos o papel de Cientistas de Dados Hospitalares. O nosso objetivo central foi catalogar, preparar e justificar a importância clínica de três fontes heterogêneas de dados estruturados e não-estruturados: Sinais Vitais Numéricos (IoT), Literatura Médica (NLP) e Exames de Imagem (Visão Computacional). Esses insumos abastecerão os motores de inferência diagnóstica nas próximas etapas do curso.

---

## 🛠️ Estrutura do Repositório

```text
/
├── asset/                          # Diretório contendo os ativos não estruturados
│   ├── abnormal_heartbeat_ecg_images/ # Imagens de ECG (Arritmia)
│   ├── myocardial_infarction_ecg_images/ # Imagens de ECG (Infarto)
│   ├── normal_ecg_images/             # Imagens de ECG (Normais)
│   ├── post_mi_history_ecg_images/    # Imagens de ECG (Pós-Infarto)
│   ├── artigo_arritmia_cardiaca.txt   # Texto Científico: Arritmia
│   ├── artigo_infarto_miocardio.txt   # Texto Científico: Infarto do Miocárdio
│   ├── artigo_pos_infarto.txt         # Texto Científico: Pós-Infarto
│   └── artigo_coracao_normal.txt      # Texto Científico: Coração Normal
├── doencas_cardiacas.csv           # Base Numérica unificada gerada a partir das imagens
├── generate_cardiac_csv.py         # Script Python gerador dos dados simulados e rotulação
└── README.md                       # Documentação principal e governança do projeto
```

> **Atenção:** Os repositórios de imagens puros originais são extensos (mais de 900 arquivos). Para fins desta entrega avaliativa, _você precisará acessar o link público ao fim deste documento_ para visualizar o volume completo consolidado em nuvem.

---

## 📊 Parte 1: Dados Numéricos (IoT e Sensores)

### A Origem dos Dados

A base de dados tabulares estruturada, localizada em `doencas_cardiacas.csv`, foi **simulada computacionalmente** com alto rigor clínico utilizando o script `generate_cardiac_csv.py` (desenvolvido exclusivamente para esta fase).

A abordagem de simulação sintética de dados foi essencial para cumprir com as rígidas políticas de **Governança de Dados e Privacidade (LGPD/HIPAA)**, evitando a exposição de PHI (_Protected Health Information_) real, ao mesmo tempo que criamos uma distribuição estatística coerente de parâmetros vitais fiel à realidade dos quadros patológicos atrelados aos exames de Eletrocardiograma (ECG) correspondentes (as imagens).

Possuímos **928 instâncias** sintéticas geradas, muito acima do mínimo exigido de 100 linhas, categorizadas em quatro anomalias cardíacas.

### Variáveis e Relevância Clínica (Feature Engineering Context)

As colunas do CSV foram criteriosamente definidas pensando em modelos descritivos e preditivos:

1. **`Idade` e `Oxigenação` (SpO2):** São inputs cruciais para modelos preditivos, visto que o envelhecimento natural do corpo e as quedas na saturação denotam fragilidade prognóstica para um AVC isquêmico proveniente de FA.
2. **`Pressão arterial` (Sistólica/Diastólica):** A hipertensão é a espinha dorsal de um IA preventiva. Em modelos de machine learning, essa métrica atua como o principal fator de peso sináptico indicativo de estresse endotelial.
3. **`Nivel de colesterol` e `Nivel de glicemia`:** Representam marcadores metabólicos de alto risco para o Infarto Agudo do Miocárdio. Identificar padrões de agrupamento (Clustering/KNN) desses valores em pacientes rotulados como normais permitirá que a IA atue em _diagnóstico precoce_.
4. **`Nivel de creatinina`:** Fundamental em projetos reais hospitalares para indicar se o paciente suportaria a carga de contraste necessário em intervenções coronarianas (hemodinâmica).

---

## 📝 Parte 2: Dados Textuais (NLP)

Para instanciar as frentes de Natural Language Processing (NLP), adicionamos à subpasta `asset` quatro documentos nos moldes científicos exigidos pela academia, embasados em literatura clássica (ex: "Heart Disease in Middle and Advanced Age" via Project Gutenberg) abordando cada um dos diagnósticos correspondentes às pastas ECG:

- `artigo_arritmia_cardiaca.txt`
- `artigo_infarto_miocardio.txt`
- `artigo_pos_infarto.txt`
- `artigo_coracao_normal.txt`

### Aplicação da IA nos Textos (Justificativa GenAi/NLP)

A ingestão destes textos densos e técnicos pela máquina não é rudimentar. No CardioIA, esses textos justificam a existência de dois subsistemas:

1. **Reconhecimento de Entidade Nomeada (NER):** Algoritmos de NLP podem extrair entidades clínicas ("Betabloqueadores", "Trombolíticos", "Amiodarona") do texto sem esforço humano. Isso é relevante na saúde porque permite a criação de grafos de conhecimento que ligam o quadro de um paciente internado ao livro-texto apropriado automaticamente (Sistemas Especialistas).
2. **Classificação, Clusterização e QA Médico:** Através da vetorização densa destes textos (Embeddings), a IA poderá classificar novos protocolos médicos vindos do SUS automaticamente em pastas corretas, e até alimentar potentes RAGs (_Retrieval-Augmented Generation_) para responder a médicos plantonistas: _"Qual o medicamento listado nos documentos para controle de frequência nas Arritmias?"_ de maneira sub-segundo durante uma emergência.

---

## 👁️ Parte 3: Dados Visuais (Visão Computacional)

Na subpasta `asset/` (ou no link contido abaixo), agrupamos **928 exames visíveis de ECG** com morfologia real particionados em pastas (`normal`, `abnormal_heartbeat`, `myocardial_infarction`, `post_mi_history`). Estes arquivos foram mapeados de forma tabular pelo script.

### Aplicação da IA no Auxílio Diagnóstico

Esses rastreios não estruturados representam o ápice do valor agregado pelo CardioIA:

1. **Detecção de Anomalias com CNNs:** Modelos de Redes Neurais Convolucionais (_Convolutional Neural Networks_) treinarão seus filtros (_kernels_) utilizando as ondas e complexos QRS destas imagens 2D para extrair _features_ imperceptíveis ao olho do médico cansaço no último turno de 12 horas.
2. **Identificação de Padrões Temporais Fatais:** A Visão Computacional extrairá coordenadas específicas em exames que não contêm o laudo (Supradesnivelamento do segmento ST em ocorrências de IAMCSST, por exemplo), atuando de fato como um segundo cardiologista na triagem de emergência (_Triage AI_), mitigando significativamente os vieses cognitivos de exaustão e aumentando a especificidade e precisão no auxílio diagnóstico.

---

## 🔗 Entregáveis: Links de Acesso Público Cloud

Abaixo estão os links para o diretório virtual na nuvem contendo **o dataset CSV preenchido e as mais de 900+ imagens de exames**, garantindo as práticas de versionamento unificado do projeto para correção.

- **📂 [INSIRA O SEU LINK PUBLICO DO ONEDRIVE/GDRIVE AQUI]**

> **Importante para o avaliador:** Caso enfrente lentidão no download do pacote completo via link acima na nuvem devido ao volume das pastas de imagem, todos os elementos estruturais textuais e tubulares (.csv) estão localmente registrados nas pastas deste exato repositório GitHub para inspeção imediata.

---

_Construído como laboratório prático para a FIAP - PBL CardioIA / Fase 1._

# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto

## Nome do grupo

## 👨‍🎓 Integrantes:

- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 1</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 2</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 3</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 4</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 5</a>

## 👩‍🏫 Professores:

### Tutor(a)

- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Tutor</a>

### Coordenador(a)

- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Coordenador</a>

## 📜 Descrição

_Descreva seu projeto com base no texto do PBL (até 600 palavras)_

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

_Acrescentar as informações necessárias sobre pré-requisitos (IDEs, serviços, bibliotecas etc.) e instalação básica do projeto, descrevendo eventuais versões utilizadas. Colocar um passo a passo de como o leitor pode baixar o seu código e executá-lo a partir de sua máquina ou seu repositório. Considere a explicação organizada em fase._

## 🗃 Histórico de lançamentos

- 0.5.0 - XX/XX/2024
  -
- 0.4.0 - XX/XX/2024
  -
- 0.3.0 - XX/XX/2024
  -
- 0.2.0 - XX/XX/2024
  -
- 0.1.0 - XX/XX/2024
  -

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
