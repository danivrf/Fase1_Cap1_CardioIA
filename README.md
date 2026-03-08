# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="asset/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto

## Nome do grupo

## 👨‍🎓 Integrantes:

- <a href="#">Felipe Livino dos Santos (RM 563187)</a>
- <a href="#">Daniel Veiga Rodrigues de Faria (RM 561410)</a>
- <a href="#">Tomas Haru Sakugawa Becker (RM 564147)</a>
- <a href="#">Daniel Tavares de Lima Freitas (RM 562625)</a>
- <a href="#">Gabriel Konno Carrozza (RM 564468)</a>

## 👩‍🏫 Professores:

### Tutor(a)

- <a href="#">Caique Nonato da Silva Bezerra</a>

### Coordenador(a)

- <a href="https://www.linkedin.com/company/inova-fusca">ANDRÉ GODOI CHIOVATO</a>

## 📜 Descrição

# CardioIA: Fase 1 - Batimentos de Dados 🫀🤖

Nest fase — focada inteiramente na engenharia de dados, curadoria e **Governança de Dados** —, nós assumimos o papel de Cientistas de Dados Hospitalares. O objetivo central foi catalogar, preparar e justificar a importância clínica de três fontes heterogêneas de dados estruturados e não-estruturados: Sinais Vitais Numéricos (IoT), Literatura Médica (NLP) e Exames de Imagem (Visão Computacional). Esses insumos abastecerão os motores de inferência diagnóstica nas próximas etapas.

---

## 🛠️ Estrutura do Repositório

```text
/
├── asset/                                  # Diretório contendo os ativos não estruturados
│   ├── abnormal_heartbeat_ecg_images/      # Imagens de ECG (Arritmia) (fazer download Google Drive)
│   ├── myocardial_infarction_ecg_images/   # Imagens de ECG (Infarto) (fazer download Google Drive)
│   ├── normal_ecg_images/                  # Imagens de ECG (Normais) (fazer download Google Drive)
│   ├── post_mi_history_ecg_images/         # Imagens de ECG (Pós-Infarto) (fazer download Google Drive)
│   ├── artigo_arritmia_cardiaca.txt        # Texto Científico: Arritmia
│   ├── artigo_infarto_miocardio.txt        # Texto Científico: Infarto do Miocárdio
│   ├── artigo_pos_infarto.txt              # Texto Científico: Pós-Infarto
│   └── artigo_coracao_normal.txt           # Texto Científico: Coração Normal
├── doencas_cardiacas.csv                   # Base Numérica unificada gerada a partir das imagens
├── exploracao_dados.ipynb                  # Notebook de exploração de dados
├── generate_cardiac_csv.py                 # Script Python gerador dos dados simulados e rotulação
└── README.md                               # Documentação principal e governança do projeto
```

> **Atenção:** Os repositórios de imagens puros originais são extensos (mais de 900 arquivos). Para fins desta entrega avaliativa, _você precisará acessar o link público ao fim deste documento_ para visualizar o volume completo consolidado em nuvem.

O repositório com os dados de ECG, foram extraidos de https://www.kaggle.com/datasets/evilspirit05/ecg-analysis?select=ecg_data_new_version

O repositório consolidado em nuvem pode ser acessado pelo link:
https://drive.google.com/drive/folders/1K2ljBezD008VaQa56zjJIHgxNI_4Tzn-?usp=sharing

---

## 📊 Parte 1: Dados Numéricos (IoT e Sensores)

### A Origem dos Dados

A base de dados tabulares estruturada, localizada em `doencas_cardiacas.csv`, foi **simulada computacionalmente** com alto rigor clínico utilizando o script `generate_cardiac_csv.py` (desenvolvido exclusivamente para esta fase).

A abordagem de simulação sintética de dados foi essencial para cumprir com as rígidas políticas de **Governança de Dados e Privacidade (LGPD/HIPAA)**, evitando a exposição de dados reais, ao mesmo tempo que criamos uma distribuição estatística coerente de parâmetros vitais fiel à realidade dos quadros patológicos atrelados aos exames de Eletrocardiograma (ECG) correspondentes (as imagens).

Possuímos **928 imagens** de ECG que foram extraidas de https://www.kaggle.com/datasets/evilspirit05/ecg-analysis?select=ecg_data_new_version,categorizadas em quatro anomalias cardíacas: Arritmia Cardíaca, Infarto do Miocárdio, Coração Normal e Pós-Infarto.

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

Agrupamos **928 exames visíveis de ECG** com morfologia real particionados em pastas (`normal`, `abnormal_heartbeat`, `myocardial_infarction`, `post_mi_history`). Estes arquivos foram mapeados de forma tabular pelo script.

Link do Google Drive: https://drive.google.com/drive/folders/1K2ljBezD008VaQa56zjJIHgxNI_4Tzn-?usp=sharing

### Aplicação da IA no Auxílio Diagnóstico

Esses rastreios não estruturados representam o ápice do valor agregado pelo CardioIA:

1. **Detecção de Anomalias com CNNs:** Modelos de Redes Neurais Convolucionais (_Convolutional Neural Networks_) treinarão seus filtros (_kernels_) utilizando as ondas e complexos QRS destas imagens 2D para extrair _features_ imperceptíveis ao olho do médico cansaço no último turno de 12 horas.
2. **Identificação de Padrões Temporais Fatais:** A Visão Computacional extrairá coordenadas específicas em exames que não contêm o laudo (Supradesnivelamento do segmento ST em ocorrências de IAMCSST, por exemplo), atuando de fato como um segundo cardiologista na triagem de emergência (_Triage AI_), mitigando significativamente os vieses cognitivos de exaustão e aumentando a especificidade e precisão no auxílio diagnóstico.

---

## 🔗 Entregáveis: Links de Acesso Público Cloud

Abaixo estão os links para o diretório virtual na nuvem contendo **o dataset CSV preenchido e as mais de 900+ imagens de exames**, garantindo as práticas de versionamento unificado do projeto para correção.

- **📂 Link do google drive**
  https://drive.google.com/drive/folders/1K2ljBezD008VaQa56zjJIHgxNI_4Tzn-?usp=sharing

> **Importante para o avaliador:** Caso enfrente lentidão no download do pacote completo via link acima na nuvem devido ao volume das pastas de imagem, todos os elementos estruturais textuais e tubulares (.csv) estão localmente registrados nas pastas deste exato repositório GitHub para inspeção imediata.

---

## 🔧 Como executar o código

Para replicar a criação do arquivo CSV deve-se

- Fazer o download dos arquivos do Google Drive e adicionar a pasta asset do projeto.
- Executar o script generate_cardiac_csv.py
- O arquivo CSV será gerado na pasta do projeto.

Para executar o notebook de exploração de dados deve-se

- Fazer o download dos arquivos do Google Drive e adicionar a pasta asset do projeto.
- Executar o notebook cardioia_exploracao_dados.ipynb
- O notebook será executado na pasta do projeto.

## 🗃 Histórico de lançamentos

- ## 0.2.0 - 08/03/2026 - Desenvolvimento dos algoritmos e notebook
- ## 0.1.0 - 07/03/2026 - Pesquisa e desenvolvimento do artivo

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
