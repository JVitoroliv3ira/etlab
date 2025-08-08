# etlab

**etlab** é uma biblioteca Python para criação e execução de pipelines **ETL (Extract → Transform → Load)** de forma **funcional** e **declarativa**.  
O projeto busca oferecer uma solução **leve**, **extensível** e **fácil de entender**, adequada tanto para fins acadêmicos quanto para aplicações reais de engenharia de dados.

---

## 🎯 Objetivos

- Fornecer um formato **declarativo** para definição de pipelines, utilizando YAML ou JSON.
- Aplicar **princípios funcionais** para garantir testabilidade e previsibilidade.
- Oferecer uma **arquitetura modular** com *extractors*, *loaders* e *transformers* plugáveis.
- Facilitar o aprendizado e a prototipagem de fluxos ELT, sem sacrificar boas práticas.
- Incluir ferramentas de **observabilidade** e **reprodutibilidade**.

---

## 🏗 Arquitetura Proposta

```
src/etlab/
├── pipeline.py       # Orquestração principal do ELT
├── extractors/       # Fontes de dados
├── loaders/          # Destinos de dados
├── transformers/     # Transformações puras
├── catalog/          # Metadados e schemas
├── cli.py            # Interface de linha de comando
└── utils.py          # Funções auxiliares
```

**Fluxo principal:**
```
Extract → Load (staging) → Transform(s) → Load (final)
```

---

## 📋 Roadmap

- [ ] Implementar CLI inicial (`init`, `run`, `validate`, `report`).
- [ ] Criar extractors para CSV e HTTP JSON.
- [ ] Criar loaders para CSV e SQLite.
- [ ] Adicionar transformações básicas (normalização, filtros, deduplicação).
- [ ] Suporte a parâmetros no YAML.
- [ ] Validação de schema com Pydantic.
- [ ] Geração de relatório HTML.
- [ ] Publicação no PyPI.

---

## 📄 Licença

Este projeto é licenciado sob a [GNU General Public License v3.0](LICENSE).

Você pode usar, modificar e distribuir este software, **desde que o código-fonte das modificações também seja disponibilizado sob a GPL-3.0**.

---

**etlab** — *pipelines declarativos, funcionais e extensíveis.*
