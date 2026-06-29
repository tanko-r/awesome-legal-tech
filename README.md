# Awesome Legal Apps

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of awesome legal technology tools, apps, AI models, and resources for legal professionals and technologists where quality of curation beats quantity of links.
> This repo is automatically updated weekly based on /sync-and-update skill in ~/.claude/skills/.

## Jurisdiction Flags

Entries marked with a flag icon are designed for or specific to that jurisdiction's legal system. Entries without flags are globally applicable or jurisdiction-agnostic.

| Flag | Jurisdiction |
|------|-------------|
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> | United States |
| <img src="https://flagcdn.com/w20/gb.png" width="20" height="15" alt="UK"> | United Kingdom |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> | European Union |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> | China |
| <img src="https://flagcdn.com/w20/in.png" width="20" height="15" alt="IN"> | India |
| <img src="https://flagcdn.com/w20/br.png" width="20" height="15" alt="BR"> | Brazil |
| <img src="https://flagcdn.com/w20/de.png" width="20" height="15" alt="DE"> | Germany |
| <img src="https://flagcdn.com/w20/sg.png" width="20" height="15" alt="SG"> | Singapore |
| <img src="https://flagcdn.com/w20/za.png" width="20" height="15" alt="ZA"> | South Africa |
| <img src="https://flagcdn.com/w20/nl.png" width="20" height="15" alt="NL"> | Netherlands |
| <img src="https://flagcdn.com/w20/es.png" width="20" height="15" alt="ES"> | Spain |
| <img src="https://flagcdn.com/w20/kr.png" width="20" height="15" alt="KR"> | South Korea |
| <img src="https://flagcdn.com/w20/ch.png" width="20" height="15" alt="CH"> | Switzerland |
| <img src="https://flagcdn.com/w20/ar.png" width="20" height="15" alt="AR"> | Argentina |
| <img src="https://flagcdn.com/w20/at.png" width="20" height="15" alt="AT"> | Austria |
| <img src="https://flagcdn.com/w20/tw.png" width="20" height="15" alt="TW"> | Taiwan |
| <img src="https://flagcdn.com/w20/fr.png" width="20" height="15" alt="FR"> | France |
| <img src="https://flagcdn.com/w20/no.png" width="20" height="15" alt="NO"> | Norway |
| <img src="https://flagcdn.com/w20/pl.png" width="20" height="15" alt="PL"> | Poland |
| <img src="https://flagcdn.com/w20/jp.png" width="20" height="15" alt="JP"> | Japan |

## Contents

- [AI Tools](#ai-tools)
- [Law-Focused LLMs & Fine-Tuned Models](#law-focused-llms--fine-tuned-models)
- [Legal Research](#legal-research)
- [Contract Management](#contract-management)
- [Practice Management](#practice-management)
- [Document Management](#document-management)
- [Backend Utilities & Libraries](#backend-utilities--libraries)
- [Legal Tech Developer Tools](#legal-tech-developer-tools)
- [Access to Justice](#access-to-justice)
- [Legal NLP & Datasets](#legal-nlp--datasets)
- [Compliance & Regulatory Technology](#compliance--regulatory-technology)
- [eDiscovery & Litigation Support](#ediscovery--litigation-support)
- [Legal Analytics & Prediction](#legal-analytics--prediction)
- [IP & Patent Technology](#ip--patent-technology)
- [Privacy & Data Protection](#privacy--data-protection)
- [Legal Workflow Automation](#legal-workflow-automation)
- [Court & Government Filing Systems](#court--government-filing-systems)
- [Legal Ontologies & Knowledge Graphs](#legal-ontologies--knowledge-graphs)
- [MCP Servers & AI Agent Tools for Law](#mcp-servers--ai-agent-tools-for-law)
- [Legal Education & Communities](#legal-education--communities)
- [Advanced Legal Tools & Citation Systems](#advanced-legal-tools--citation-systems)
- [Notable Proprietary Legal AI Tools](#notable-proprietary-legal-ai-tools)
- [Meta-Resources](#meta-resources)

## AI Tools

Tools and models that use AI to assist with legal work, from contract analysis to legal research and document generation.

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Sara](https://github.com/tanko-r/AI-Associate)*** | *A specialized Claude Code plugin that operates as a senior AI law associate capable of handling complex legal work across multiple practice areas, currently focused on US real estate transactions, generating original legal documents and delegating research tasks to junior associate subagents. ⚠️ Stale (archived/removed)* | *Python* | No license | *2026-03-02* |
| **[Ambrose](https://github.com/tanko-r/Ambrose)** | An AI-powered contract review and redlining platform combining Claude Opus for risk analysis with Gemini Flash for revision generation, engineered for in-house counsel and deal teams managing high volumes of contracts. | Python, Flask, TypeScript, Next.js | Other | 2026-03-02 |
| **[Lawvable](https://github.com/lawvable/awesome-legal-skills)** | Curated AI skills for legal workflows and document analysis. | | Other | 2026-03-02 |
| **[LiTiL AI](https://litil.ai/#/projects)** | A collection of legal AI tools developed by [@narcolepticchicken](https://github.com/narcolepticchicken). | | Other | 2026-06-26 |
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[LexNLP](https://github.com/LexPredict/lexpredict-lexnlp)*** | *Open source Python library for natural language processing and information extraction from legal and regulatory texts, extracting structured data like dates, monetary amounts, regulations, and citations with pre-trained models. ⚠️ Stale (2024-05)* | *Python* | AGPL-3.0 | *2026-03-02* |
| **[LawBotics](https://github.com/hasnaintypes/lawbotics)** | AI-powered legal contract analysis platform combining fine-tuned LLaMA models with modern web technologies to automate document review and clause extraction, identifying 41+ types of legal clauses and integrating with the CUAD dataset. | Python, PyTorch | No license | 2026-03-02 |
| *<img src="https://flagcdn.com/w20/br.png" width="20" height="15" alt="BR"> **[LegalNLP](https://github.com/felipemaiapolo/legalnlp)*** | *Natural language processing methods and pre-trained models (BERT, Word2Vec, Doc2Vec, FastText) specifically designed for the Brazilian legal language, enabling legal document classification and semantic analysis. ⚠️ Stale (2023-06)* | *Python, PyTorch* | MIT | *2026-03-02* |
| <img src="https://flagcdn.com/w20/in.png" width="20" height="15" alt="IN"> **[MILDSum](https://github.com/Law-AI/mildsum)** | Benchmark dataset and tools for multilingual legal document summarization, featuring 3,122 Indian court judgments with English and Hindi summaries drafted by legal practitioners. | Python | No license | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[OLAW](https://github.com/harvard-lil/olaw)** | Open Legal AI Workbench from Harvard Law School Library for building retrieval-augmented generation (RAG) applications in legal research, providing a customizable chatbot framework that integrates legal APIs and documents. | Python | MIT | 2026-03-02 |
| <img src="https://flagcdn.com/w20/in.png" width="20" height="15" alt="IN"> **[LawGlance](https://github.com/lawglance/lawglance)** | Free, open-source RAG-based AI legal assistant for document analysis and legal question answering, enabling users to query their legal documents using natural language. | Python | Apache-2.0 | 2026-03-02 |
| **[Legal ML Datasets](https://github.com/neelguha/legal-ml-datasets)** | Curated collection of datasets and machine learning tasks for legal text processing, including contract understanding, clause classification, and legal document analysis benchmarks. | | No license | 2026-03-02 |
| ***[Awesome LegalAI Resources](https://github.com/CSHaitao/Awesome-LegalAI-Resources)*** | *Comprehensive collection of legal AI datasets, tools, websites, and resources to facilitate development of intelligent legal technology systems. ⚠️ Stale (2023-07)* | | MIT | *2026-03-02* |
| ***[Legal Document Analysis using NLP](https://github.com/Team-NLP-Legal-Document/Legal_Document_Analysis_and_Classification_Using_NLP_and_Deep_Learning)*** | *Deep learning pipeline for legal document classification and analysis using BERT embeddings and neural networks to automate document categorization and information extraction. ⚠️ Stale (2023-12)* | *Python, PyTorch* | No license | *2026-03-02* |
| **[LexReviewer](https://github.com/LexStack-AI/LexReviewer)** | AI legal document review engine that ingests PDFs, uses RAG with hybrid retrieval, and provides grounded chat with citations and bounding-box references for verifiable answers from source text. | Python | No license | 2026-03-03 |
| **[Ally Legal Assistant](https://github.com/Azure-Samples/ally-legal-assistant)** | Microsoft Word plugin using Azure OpenAI for contract analysis, real-time Q&A, and auto-markup to help legal professionals save time during document reviews. | TypeScript, Office.js | No license | 2026-03-03 |
| **[Claude Cowork Legal Plugin](https://github.com/anthropics/knowledge-work-plugins)** | Open-source legal plugin for Claude Cowork automating contract review, NDA triage, and compliance workflows for in-house legal teams, part of Anthropic's knowledge-work plugin ecosystem. | Python | Apache-2.0 | 2026-03-25 |
| **[Claude Legal Skill](https://github.com/evolsb/claude-legal-skill)** | AI-powered contract review skill with CUAD risk detection, market benchmarks, and lawyer-ready redlines, compatible with Claude Code, Codex, Cursor, and 26+ AI coding tools. | Python | MIT | 2026-03-25 |
| **[Contract Review Agent](https://github.com/kipeum86/contract-review-agent)** | Local-first AI contract review agent that turns legal templates and counterparty drafts into clause-level analysis and tracked-change DOCX redlines. | Python | Apache-2.0 | 2026-03-25 |
| <img src="https://flagcdn.com/w20/in.png" width="20" height="15" alt="IN"> **[LegalOS](https://github.com/paidinesh7/LegalOS)** | AI-powered legal document analyzer designed for Indian startup founders to review and understand legal agreements. | Python | No license | 2026-03-25 |
| *<img src="https://flagcdn.com/w20/br.png" width="20" height="15" alt="BR"> **[Lex Intelligentia Skills](https://github.com/fbmoulin/lex-intelligentia-skills)*** | *Agent skills ecosystem with 17 specialized skills for Brazilian law professionals including magistrates, lawyers, and legal researchers. ⚠️ Stale (archived/removed)* | *Python* | — | *2026-03-25* |
| **[AI Legal Claude](https://github.com/zubair-trabzada/ai-legal-claude)** | Claude Code skill suite providing 14 specialized legal AI skills including contract review, risk analysis, NDA generation, compliance auditing, and negotiation strategy, orchestrated by 5 parallel agents. | Python | No license | 2026-04-06 |
| **[BS Detector](https://github.com/JuanVazTor/lh-ai-fs)** | AI pipeline that audits legal briefs for false or misrepresented case citations, verifying whether cited authority says what the brief claims it says. | Python | No license | 2026-04-06 |
| **[Hallucination Auditor](https://github.com/jamescockburn47/hallucinationauditor)** | Local tool for auditing AI hallucinations in legal authority citations, verifying whether cited cases exist and whether quoted passages accurately reflect the source, producing audit-grade reports. | Python | No license | 2026-04-06 |
| **[claude-for-legal](https://github.com/anthropics/claude-for-legal)** | Anthropic's official suite of plugins, reference agents, skills, and data connectors for legal workflows covering in-house commercial, privacy, employment, litigation, IP, AI governance, and regulatory practice areas. | Python | Apache-2.0 | 2026-06-11 |
| **[Lavern](https://github.com/AnttiHero/lavern)** | Open-source agentic law firm with 67 specialist AI agents that review documents through evidence-backed debate, mandatory human gate checkpoints, and a 10-pass verification loop to reduce hallucinations. | Python | Apache-2.0 | 2026-06-11 |
| <img src="https://flagcdn.com/w20/de.png" width="20" height="15" alt="DE"> **[Claude für deutsches Recht](https://github.com/Klotzkette/claude-fuer-deutsches-recht)** | Experimental skill collection for German legal practice spanning employment, corporate, insolvency, data protection, and procedural law, tested in daily practice. | Python | Apache-2.0 | 2026-06-11 |
| **[Due Diligence Agents](https://github.com/zoharbabin/due-diligence-agents)** | Open-source forensic M&A due diligence platform using 13 AI agents across 9 domains (Legal, Finance, Commercial, Tech, Cyber, HR, Tax, Regulatory, ESG) that cross-reference findings and trace every conclusion to an exact source page and quote. | Python | Apache-2.0 | 2026-06-11 |
| **[Master Claude for Legal](https://github.com/sboghossian/master-claude-for-legal)** | Master skill pack for legal teams using Claude, providing reference implementations, starter skills, and templates built from Anthropic's Claude for Legal Teams webinars. | Python | Other | 2026-06-11 |
| **[LQ.AI](https://github.com/LegalQuants/lq-ai)** | Self-hosted, open-source AI platform for legal teams with character-verifiable citations, a privacy-preserving anonymization layer for cloud inference, and reusable workflow skills, running against Anthropic, OpenAI, Azure, or local Ollama models with bring-your-own keys. | Python | Apache-2.0 | 2026-06-11 |
| **[Donna](https://github.com/LegalQuants/Donna)** | Document-forward SvelteKit frontend for the LQ.AI legal backend providing conversational legal work with character-verified citation pills, matter-scoped projects, knowledge bases, playbook redlines, and autonomous background runs with transparency receipts. | TypeScript, SvelteKit | Apache-2.0 | 2026-06-11 |
| **[Mike (local desktop edition)](https://github.com/LegalQuants/LQmikelocal)** | Local-first Electron desktop edition of the Mike AI legal platform that runs documents, database, and model calls entirely on your computer with no cloud dependencies, storing data in a local SQLite workspace. | TypeScript, Electron | AGPL-3.0 | 2026-06-11 |
| **[BigLaw](https://github.com/discover-legal/BigLaw)** | Open-source legal AI platform consolidating research, drafting, redlining, e-signatures, briefing, docketing, billing, and collaboration in a single stack, registering as an MCP server for agent integration. | Python | AGPL-3.0 | 2026-06-15 |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[Claude for Legal — ZH](https://github.com/CSlawyer1985/claude-for-legal-ZH)** | Chinese law adaptation of Anthropic's claude-for-legal, providing legal agents, skills, and MCP data connectors for Chinese legal practice scenarios including litigation, corporate, and regulatory work. | Python | Apache-2.0 | 2026-06-15 |
| <img src="https://flagcdn.com/w20/de.png" width="20" height="15" alt="DE"> **[AI Skills German Law](https://github.com/borghei/AI-Skills-German-Law)** | Collection of 48 plugins and 103 skills for German legal practice and EU compliance covering general law, specialist practice areas, regulated industries, IP, and frameworks including KI-VO, NIS2, HinSchG, LkSG, DORA, DSA/DMA, and CSRD, with citations linked to official sources. | | Other | 2026-06-15 |
| **[AiWorkdeck](https://github.com/zeweihan/aiworkdeck)** | AI-native IDE workspace for legal and document-heavy workflows providing file management, agent plugins, WPS document editing, OCR, and evidence chain tracking, positioned as VS Code for lawyers. | | AGPL-3.0 | 2026-06-15 |
| **[Judicex](https://github.com/JustVugg/judicex)** | Open-source legal AI workspace for evidence-grounded legal drafting, matter analysis, and verifiable answers with citation transparency. | | Apache-2.0 | 2026-06-15 |
| **[doc-haus](https://github.com/sure-scale/doc-haus)** | Open-source local-first legal AI agent that processes documents on your machine and delivers redlines directly into Word, forked from OpenCode with legal-specific document handling. | | Other | 2026-06-15 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Vera EB Suite](https://github.com/VeraSuperHub/vera-eb-suite)** | Open-source AI skills and plugins for US employment-based immigration petitions (EB-1 and EB-2 NIW) covering evidence organization, narrative drafting, RFE response, and adversarial pre-filing review across 19 modular skills. | Python | GPL-3.0 | 2026-06-22 |
| <img src="https://flagcdn.com/w20/pl.png" width="20" height="15" alt="PL"> **[Commercial Legal PL](https://github.com/apiotrowski-afk/commercial-legal-pl)** | Claude skill for drafting and analyzing B2B IT contracts and settlements under Polish commercial law, built from daily law-firm use with 12 editorial guidelines, 20 clause files, and 8 workflow templates. | | Apache-2.0 | 2026-06-22 |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[Contract Review Pro](https://github.com/CSlawyer1985/contract-review-pro)** | Professional contract review skill for Chinese legal practitioners built on a systematic methodology with a 7-step workflow, 5 gate checks, 15 risk labels, 124 risk templates, and 105 clause references covering 30 contract types across 7 business domains, producing annotated contracts, legal opinions, and analysis documents. | Python | No license | 2026-06-29 |

## Law-Focused LLMs & Fine-Tuned Models

Foundation models and fine-tunes purpose-built for the legal domain, from general-purpose legal LLMs to specialized encoder models and retrieval systems.

### General-Purpose Legal LLMs

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> ***[LaWGPT](https://github.com/pengxiao-song/LaWGPT)*** | *A series of open-source large language models based on Chinese-LLaMA, enhanced with expanded legal vocabulary and large-scale Chinese legal corpus pre-training plus instruction fine-tuning on judicial examination data. ⚠️ Stale (2024-06)* | *Python, PyTorch* | GPL-3.0 | *2026-03-02* |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[Lawyer-LLaMA](https://github.com/AndrewZhe/lawyer-llama)** | A Chinese legal domain LLM built on LLaMA via continual pre-training on legal corpora and instruction fine-tuning with ChatGPT-generated legal Q&A, covering civil, criminal, and administrative law. | Python, PyTorch | Apache-2.0 | 2026-03-02 |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[Fuzi-Mingcha](https://github.com/irlab-sdu/fuzi.mingcha)** | A Chinese judicial large language model jointly developed by Shandong University, Inspur Cloud, and China University of Political Science and Law, built on ChatGLM with capabilities for legal statute retrieval, case analysis, and judgment prediction. | Python, PyTorch | Apache-2.0 | 2026-03-02 |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[LexiLaw](https://github.com/CSHaitao/LexiLaw)** | A fine-tuned Chinese legal language model based on ChatGLM-6B that provides legal consultation services using LoRA, P-tuning-v2, and full fine-tuning approaches trained on legal Q&A, statutes, and court documents. | Python, PyTorch | MIT | 2026-03-02 |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[wisdomInterrogatory](https://github.com/zhihaiLLM/wisdomInterrogatory)** | A legal-focused large language model developed by Zhejiang University and Alibaba DAMO Academy, built on Baichuan-7B with 40GB of legal domain data and six knowledge base types for intelligent legal consultation. | Python, PyTorch | Apache-2.0 | 2026-03-02 |
| *<img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[HanFei](https://github.com/siat-nlp/HanFei)*** | *A 7-billion-parameter fully fine-tuned Chinese legal large language model trained on approximately 60GB of legal domain data, supporting legal Q&A, multi-turn conversations, and article writing. ⚠️ Stale (2023-10)* | *Python, PyTorch* | Apache-2.0 | *2026-03-02* |
| *<img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[InternLM-Law](https://github.com/InternLM/InternLM-Law)*** | *An open-source Chinese legal LLM with 7B parameters and 32K-token context length that outperforms GPT-4 on the LawBench evaluation benchmark, presented at COLING 2025. ⚠️ Stale (2024-05)* | *Python, PyTorch* | Apache-2.0 | *2026-03-02* |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Law_LLM](https://github.com/Tizzzzy/Law_LLM)** | A multi-task legal LLM for the US legal system built on Gemma-7B, capable of similar case retrieval, precedent case recommendation, and legal judgment prediction. | Python, PyTorch | No license | 2026-03-02 |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[LegalOne](https://github.com/CSHaitao/LegalOne)** | A family of Chinese legal-domain foundation models (1.7B, 4B, 8B parameters) trained via a three-phase pipeline with agentic chain-of-thought distillation and curriculum reinforcement learning for reliable legal reasoning. | Python, PyTorch | Apache-2.0 | 2026-03-25 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[PrinzBench](https://github.com/prinz-ai/prinzbench)** | A benchmark ranking frontier LLMs on their ability to conduct legal research, analysis, and locate obscure publicly available legal information across US law. | | No license | 2026-03-25 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[LEXam](https://github.com/LEXam-Benchmark/LEXam)** | A comprehensive legal reasoning benchmark evaluating LLMs on 4,886 law exam questions from 340 exams spanning Swiss, EU, and international law, accepted at ICLR 2026. | | Apache-2.0 | 2026-03-25 |
| **[Legal-LLM (LawMate Romania)](https://github.com/DorobantuDiana/Legal-LLM)** | Romanian legal domain LLM built by fine-tuning Saul-7B-Instruct-v1 on the Romanian Constitution and Education Law, with the resulting model published on Hugging Face. | Python, PyTorch | MIT | 2026-04-06 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Lawma](https://github.com/socialfoundations/lawma)** | Lightly fine-tuned Llama 3 models (8B and 70B) trained on 260 legal classification tasks derived from US Supreme Court and Court of Appeals databases, setting a new baseline for legal classification benchmarks. | Python, PyTorch | No license | 2026-06-11 |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[2N-Guardian](https://github.com/RayBagel/2N-Guardian)** | Legal LLM explainable reward engine using GRPO with a three-dimensional reward function (legal accuracy, citation support, logical coherence) to reduce hallucinations in legal text generation, with a Chinese legal dataset and training code. | Python | Apache-2.0 | 2026-06-22 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[@narcolepticchicken Models]([https://github.com/Tizzzzy/Law_LLM](https://huggingface.co/narcolepticchicken))** | A collection of fine-tuned and post-trained models by attorney Aaron Kelly focused on law and contracts. | Other |  | 2026-06-26 |

### Legal BERT & Encoder Models

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| ***[legalBERT](https://github.com/nonameemnlp2020/legalBERT)*** | *The official code repository for the LEGAL-BERT paper, providing multiple pre-trained BERT variants optimized for different legal sub-domains including US contracts, ECHR cases, and EU legislation. ⚠️ Stale (2020-06)* | *Python, PyTorch* | Apache-2.0 | *2026-03-02* |
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[CaseHOLD](https://github.com/reglab/casehold)*** | *Stanford RegLab repository containing Legal-BERT and Custom Legal-BERT models pre-trained on 37GB of Harvard Law case corpus (3.4M+ legal decisions), plus the CaseHOLD benchmark of 53,000+ legal holdings. ⚠️ Stale (2023-03)* | *Python, PyTorch* | Apache-2.0 | *2026-03-02* |
| *<img src="https://flagcdn.com/w20/in.png" width="20" height="15" alt="IN"> **[InLegalBERT](https://github.com/Law-AI/pretraining-bert)*** | *Code from IIT Kharagpur for pre-training BERT models on Indian legal text using dynamic MLM and NSP, producing InLegalBERT and InCaseLawBERT models trained on 5.4 million Indian legal documents spanning 1950-2019. ⚠️ Stale (2023-06)* | *Python, PyTorch* | MIT | *2026-03-02* |

### Legal Embedding & Retrieval Models

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[fastlaw](https://github.com/jbesomi/fastlaw)*** | *Law-specific word embeddings built with Apache Spark and FastText, trained on data from the Caselaw Access Project to replace generic word embeddings for supervised ML tasks on legal texts. ⚠️ Stale (2019-06)* | *Python* | No license | *2026-03-02* |
| **[LRAGE](https://github.com/hoorangyee/LRAGE)** | An open-source Legal Retrieval Augmented Generation Evaluation toolkit for assessing LLMs in RAG settings within the legal domain, with pre-compiled indexes and support for legal datasets. | Python | MIT | 2026-03-03 |
| **[Inception](https://github.com/freelawproject/inception)** | FastAPI microservice from the Free Law Project generating legal-text embeddings via fine-tuned ModernBERT, optimized for court opinions with GPU acceleration and batch processing. | Python | BSD-2-Clause | 2026-03-25 |

## Legal Research

Platforms and tools for legal research, case law discovery, and statutory information.

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[CourtListener](https://github.com/freelawproject/courtlistener)** | Fully-searchable archive of US court opinions, orders, and judge data with coverage spanning decades of American case law, used by legal professionals, researchers, and the general public. | Python, Django | Other | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Juriscraper](https://github.com/freelawproject/juriscraper)** | Automated API for scraping American court websites to extract case metadata and opinions, enabling developers and legal research tools to collect court data programmatically from multiple jurisdictions. | Python | BSD-2-Clause | 2026-03-02 |
| **[LawLens](https://github.com/Ranjith00005/LawLens)** | AI-powered legal research assistant that provides legal advisory, case outcome prediction, and automated report generation by analyzing PDF documents, designed for law firms and individual practitioners. | Python | MIT | 2026-03-02 |
| <img src="https://flagcdn.com/w20/gb.png" width="20" height="15" alt="UK"> **[Lex](https://github.com/i-dot-ai/lex)** | UK legal API providing access to legislation and case law specifically designed for AI agents and legal researchers, built by the UK government's AI lab. | Python | MIT | 2026-03-02 |
| **[CC Legal Database](https://github.com/cc-archive/legaldb)** | Curated repository of case law and legal scholarship from around the world housed in a Django-based platform. | Python, Django | MIT | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Law XML](https://github.com/DCCouncil/law-xml)** | DC Law statutes and regulatory code published in structured XML format for programmatic access. | | No license | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Reporters DB](https://github.com/freelawproject/reporters-db)** | Comprehensive database of court reporters with metadata and citation information for American courts. | Python | BSD-2-Clause | 2026-03-02 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[OpenArchiver](https://github.com/LogicLabs-OU/OpenArchiver)** | Open-source platform for legally compliant email archiving and eDiscovery with GDPR-aware data retention. | | AGPL-3.0 | 2026-03-03 |
| **[AuthoritySpoke](https://github.com/mscarey/AuthoritySpoke)** | Python library for modeling legal rules as structured data, enabling machine-readable representation and comparison of holdings from court opinions. | Python | Other | 2026-03-03 |
| **[Legal Sources](https://github.com/worldwidelaw/legal-sources)** | Open-source collection scripts for legal data from 50+ countries written autonomously by an AI agent, with community-contributed government data sources. | | AGPL-3.0 | 2026-03-25 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[US Code Tools](https://github.com/nickvido/us-code-tools)** | TypeScript ingestion engine and sync tooling for the US Code corpus, providing structured programmatic access to United States federal statutes. | TypeScript | No license | 2026-04-06 |
| **[MENA Legal Atlas](https://github.com/sboghossian/mena-legal-atlas)** | Open map of every legal data source across 25 MENA jurisdictions covering official gazettes, consolidated legislation, apex court decisions, and regulatory bodies. | | Other | 2026-06-11 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Google Scholar](https://scholar.google.com/scholar_courts)** | Free case law search engine covering all 50 states and federal courts with opinions dating back to 1791, featuring customizable court selection and advanced search filters. | | Not FOSS | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[CourtListener](https://www.courtlistener.com/)** | Nonprofit-operated legal database with over 10 million case opinions from federal and state courts, plus 17.3 million PACER documents with advanced semantic search. | | Not FOSS | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Legal Information Institute (LII)](https://www.law.cornell.edu/)** | Cornell Law School's nonprofit platform providing free access to U.S. Code, federal regulations, state statutes, court decisions, and legal encyclopedia. | | Not FOSS | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[FindLaw](https://caselaw.findlaw.com/)** | Comprehensive free resource for searching state and federal court opinions, statutes, regulations, and U.S. Code. | | Not FOSS | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[GovInfo](https://www.govinfo.gov/help/cfr)** | Official Government Publishing Office database offering authenticated federal regulations, Code of Federal Regulations, and federal register documents. | | Public domain | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Justia](https://law.justia.com/)** | Free legal research platform featuring case law, statutes, regulations, and legal articles for federal and state resources. | | Not FOSS | 2026-03-02 |

## Contract Management

Tools for drafting, reviewing, negotiating, and managing legal contracts.

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| **[OCA Contract](https://github.com/OCA/contract)** | Odoo module that manages contract creation, recurring invoicing, and lifecycle workflows with portal visibility. | Python | AGPL-3.0 | 2026-03-02 |
| **[Accord Project - Cicero](https://github.com/accordproject/cicero-template-library)** | Open ecosystem for smart legal contracts providing a template library and execution engine, allowing drafting of natural language templates bound to data models. | | Apache-2.0 | 2026-03-02 |
| **[Contract Analyzer](https://github.com/ahmetkumass/contract-analyzer)** | Open-source RAG-based system for extracting and analyzing key information from legal contracts using advanced language models. | Python | No license | 2026-03-02 |
| **[OpenContracts](https://github.com/Open-Source-Legal/OpenContracts)** | Enterprise-grade document analysis workspace combining LLM capabilities with annotation, collaboration, and structured data extraction. | Python | MIT | 2026-03-02 |
| **[DocuSeal](https://github.com/docusealco/docuseal)** | Open-source DocuSign alternative for creating, filling, and signing digital documents with mobile-optimized forms and SDKs. | | AGPL-3.0 | 2026-03-02 |
| **[Contract Lifecycle Management Dashboard](https://github.com/cyberkunju/contract-management)** | Frontend-based CLM platform built with React and TypeScript for designing reusable contract blueprints and managing workflows. | TypeScript, React | No license | 2026-03-02 |
| ***[Contract Builder](https://github.com/blopa/Contract-Builder)*** | *Free, open-source tool for easily building and maintaining any type of contract using a spreadsheet-style interface. ⚠️ Stale (2017-10)* | | MIT | *2026-03-02* |
| **[Microsoft Agent for Contract Processing](https://github.com/microsoft/Agent-for-Contract-Processing-Solution-Accelerator)** | Solution accelerator demonstrating AI agent deployment for streamlined NDA creation and management. | Python | MIT | 2026-03-03 |
| **[Legal Redline Tools](https://github.com/evolsb/legal-redline-tools)** | Generates tracked-changes Word documents and redline PDFs from AI-powered contract reviews, producing the actual deliverables lawyers send. | Python | MIT | 2026-03-25 |
| **[Restated AI](https://github.com/Flosters/Restated-AI)** | AI tool for generating amended and restated versions of legal agreements, automating the redrafting of contract amendments. | TypeScript | MIT | 2026-04-06 |
| **[Indemnification Architect](https://github.com/Tucuxi-Inc/IndemnificationArchitect)** | Parametric drafting and analysis tool for indemnification clauses that uses visual sliders to adjust clause components and generates production-quality legal text from each configuration. | TypeScript | MIT | 2026-04-06 |
| **[Whereas](https://github.com/zgbrenner/whereas)** | Open-source contract repository with built-in clause extraction, playbook deviation analysis, and embedded e-signature via DocuSeal integration. | TypeScript | GPL-3.0 | 2026-06-11 |
| **[Vaulytica](https://github.com/clay-good/vaulytica)** | Free deterministic linter for legal documents that flags structural issues, inconsistencies, and common drafting errors without relying on an LLM. | | MIT | 2026-06-11 |
| **[SignCraft](https://github.com/Steviewonders99/signcraft)** | Open-source AI contract review and e-signature platform providing a free alternative to DocuSign, Adobe Sign, and PandaDoc, with AI-powered clause analysis for drafting, reviewing, and signing legal contracts. | TypeScript | MIT | 2026-06-15 |
| **[draft-legal](https://github.com/AniketTati/draft-legal)** | Self-hosted, AI-native contract lifecycle management platform designed as an open-source alternative to Ironclad and Harvey, keeping contracts on your own servers. | | Other | 2026-06-15 |
| **[Hermes Legal](https://github.com/Lethe044/hermes-legal)** | Autonomous contract risk analysis tool that scores clauses, suggests negotiation language, issues SIGN/NEGOTIATE/REJECT verdicts, compares document versions, and watches folders for new contracts, supporting English and Turkish. | Python | MIT | 2026-06-15 |
| <img src="https://flagcdn.com/w20/kr.png" width="20" height="15" alt="KR"> **[Korean Contracts](https://github.com/kimlawtech/korean-contracts)** | Claude Code skill for automatically generating nine types of Korean employment and business contracts (employment, part-time, flexible, daily, freelance, outsourcing, amendment, and salary agreements) updated for 2026 minimum wage and Supreme Court precedents. | | Other | 2026-06-15 |
| **[ContractGuard](https://github.com/he-yufeng/ContractGuard)** | AI contract analysis agent that detects red flags, unfair terms, and missing protections in uploaded contracts in under 30 seconds, supporting PDF, DOCX, TXT, and RTF with batch processing and contract comparison. | Python | MIT | 2026-06-22 |
| **[ContractSpark](https://github.com/ICodingStack/ContractSpark)** | Client-side open-source contract generator for freelancers and small businesses providing eight professional agreement templates with AI-powered builder, real-time preview, and one-click PDF export — requires no backend. | | MIT | 2026-06-22 |

## Practice Management

Software for law firms and legal departments to manage cases, clients, time, and billing.

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| **[Legal-Ease](https://github.com/sujal-pawar/Legal-Ease)** | AI-driven legal case management platform enabling courts, law firms, and litigants to manage cases and schedule virtual hearings. | | No license | 2026-03-02 |
| **[CaseAce](https://github.com/derekgan08/CaseAce-law-firm-management-system-backend)** | Node.js and Express-based case management system for law firms offering CRM, document storage, task tracking, and appointment scheduling. | | Other | 2026-03-02 |
| **[Kimai](https://github.com/kimai/kimai)** | Leading open-source time-tracking application enabling lawyers to manage timesheets, generate invoices, and create reports with support for 30+ languages. | | AGPL-3.0 | 2026-03-02 |
| **[IDURAR ERP CRM](https://github.com/idurar/idurar-erp-crm)** | Comprehensive open-source ERP and CRM system on MERN stack handling invoicing, quotes, payments, and accounting. | | AGPL-3.0 | 2026-03-02 |
| **[InvoiceShelf](https://github.com/InvoiceShelf/InvoiceShelf)** | Laravel and Vue.js invoicing solution for tracking expenses, creating invoices and estimates, and managing recurring billing. | PHP, Laravel | AGPL-3.0 | 2026-03-02 |
| **[SolidInvoice](https://github.com/SolidInvoice/SolidInvoice)** | PHP-based invoicing platform with client management, quote generation, and online payment processing. | PHP | MIT | 2026-03-02 |
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Open Case Management (OCM)](https://github.com/aworley/ocm)*** | *PHP-based case management system specifically designed for nonprofit legal services organizations. ⚠️ Stale (2022-08)* | *PHP* | GPL-2.0 | *2026-03-02* |
| ***[Law Firm Management System](https://github.com/leon019i/Law_Firm_Management_system_Django)*** | *Django-powered practice management platform with client management, case tracking, and mobile-friendly design. ⚠️ Stale (2024-03)* | *Python, Django* | No license | *2026-03-02* |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[DAWSON - U.S. Tax Court ef-cms](https://github.com/ustaxcourt/ef-cms)** | TypeScript-based electronic filing and case management system used by the U.S. Tax Court. | TypeScript | Other | 2026-03-02 |
| <img src="https://flagcdn.com/w20/de.png" width="20" height="15" alt="DE"> **[j-lawyer.org](https://github.com/jlawyerorg/j-lawyer-org)** | Open-source Java-based legal case and document management system supporting case organization, document handling, invoicing, and fax integration for law offices on Windows, macOS, and Linux. | Java | AGPL-3.0 | 2026-03-02 |
| **[LPM Skills](https://github.com/legalopsconsulting/lpm-skills)** | AI skills encoding legal project management methodology for Claude, covering matter management, budgeting, task workflows, and deadline tracking. | Python | Apache-2.0 | 2026-03-25 |
| **[TimeBrief](https://github.com/jamescockburn47/voice-time)** | Voice-powered time tracking app for lawyers with fully local AI, enabling hands-free timesheet entry without sending data to external servers. | Python | MIT | 2026-04-06 |
| **[CounselScope](https://github.com/Tucuxi-Inc/PublicCounselScope)** | AI-powered legal query optimization platform that transforms vague legal requests into precisely-scoped instructions by building on internal organizational legal knowledge. | Python | Other | 2026-04-06 |
| **[stella](https://github.com/stella/stella)** | Open-source self-hostable legal workspace for law firms with matter and document management, AI-assisted drafting, a DOCX editor, citation and case-law tools, business-registry lookup, and multilingual anonymisation. | TypeScript | Apache-2.0 | 2026-05-31 |
| **[OpenSign](https://www.opensignlabs.com/)** | Free, unlimited, open-source e-signature tool. | | AGPL-3.0 | 2026-03-02 |
| **[OpenSpecter](https://github.com/akashshrx/OpenSpecter)** | Enterprise-grade self-hostable AI workspace for legal teams with matter management, document organization, and AI-assisted workflows. | | AGPL-3.0 | 2026-06-15 |

## Document Management

Systems for storing, organizing, and retrieving legal documents securely.

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| **[Docassemble](https://github.com/jhpyle/docassemble)** | Open-source expert system for guided interviews and document assembly built on Python, YAML, and Markdown, automating legal form completion and helping self-represented litigants. | Python, YAML | MIT | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[docassemble-AssemblyLine](https://github.com/SuffolkLITLab/docassemble-AssemblyLine)** | Rapid deployment framework by Suffolk Legal Innovation & Technology Lab that converts paper court forms into interactive web applications. | Python, YAML | MIT | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[docassemble-ALWeaver](https://github.com/SuffolkLITLab/docassemble-ALWeaver)** | Code generation tool that automatically generates draft docassemble interviews from existing legal documents in PDF or DOCX format. | Python, YAML | MIT | 2026-03-02 |
| **[DocuSeal](https://github.com/docusealco/docuseal)** | Open-source alternative to DocuSign for creating, filling, and digitally signing documents. | | AGPL-3.0 | 2026-03-02 |
| **[OpenSign](https://github.com/OpenSignLabs/OpenSign)** | Free and open-source DocuSign alternative providing e-signature capabilities for legal documents. | | Other | 2026-03-02 |
| **[Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx)** | Document management system that scans, indexes, and archives physical documents with OCR and full-text search. | Python | GPL-3.0 | 2026-03-02 |
| **[Papermerge](https://github.com/ciur/papermerge)** | Open-source document management system optimized for digital archives and scanned documents with OCR capabilities. | Python | Apache-2.0 | 2026-03-02 |
| **[Mayan EDMS](https://github.com/mayan-edms/Mayan-EDMS)** | Free and open-source enterprise document management system supporting workflows, versioning, and audit trails. | Python | Other | 2026-03-02 |
| **[PyMuPDF](https://github.com/pymupdf/PyMuPDF)** | High-performance Python library for extracting, analyzing, and manipulating PDF document data for automated legal document processing. | Python | AGPL-3.0 | 2026-03-02 |
| **[Documenso](https://github.com/documenso/documenso)** | Open-source DocuSign alternative built with Next.js and PostgreSQL, supporting self-hosting and PAdES-standard digital signatures for legally binding document workflows. | TypeScript, Next.js | AGPL-3.0 | 2026-03-02 |
| **[Word AI Redliner](https://github.com/yuch85/word-ai-redliner)** | Microsoft Word add-in that applies AI edits as tracked-change redlines with prompt management, connecting to Ollama or other LLMs for structure-aware legal document editing. | TypeScript, Office.js | MIT | 2026-03-25 |
| **[SuperDoc Redlines](https://github.com/yuch85/superdoc-redlines)** | CLI tool for applying tracked changes and comments to DOCX files using SuperDoc headless mode, enabling automated document markup in legal workflows. | TypeScript | Apache-2.0 | 2026-03-25 |
| **[SignaturePacketIDE](https://github.com/jamietso/SignaturePacketIDE)** | AI-powered legal signature page extractor and packet generator that automates creation of wet-ink signature packs for M&A and financing transactions. | Python | MIT | 2026-03-25 |
| **[open-agreements](https://github.com/open-agreements/open-agreements)** | CLI tool that fills 25 standard legal agreement templates (NDAs, cloud terms, SAFEs, employment agreements, NVCA financing documents) and produces signable DOCX files. | TypeScript | Apache-2.0 | 2026-04-06 |
| **[CoQuill](https://github.com/houfu/coquill)** | Conversational document assembly tool for Claude that fills DOCX templates through natural-language interview, supporting Jinja2 conditionals and loops without a server or scripting language. | Python | MIT | 2026-04-06 |
| **[SuperDoc VS Code Extension](https://github.com/mattConnHarbour/superdoc-vscode-extension)** | VS Code extension for editing and viewing DOCX files via SuperDoc, with live reload for AI-modified documents and auto-save for side-by-side code and document workflows. | JavaScript | AGPL-3.0 | 2026-04-06 |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[Legal Doc Redactor](https://github.com/moyupeng0422/legal-doc-redactor)** | Fully offline browser-based legal document redaction tool that identifies and masks 15 categories of sensitive information (names, IDs, financial data, addresses) with a paired restoration workflow for external review cycles, supporting batch processing and Windows/macOS context-menu integration. | | MIT | 2026-06-22 |

## Backend Utilities & Libraries

Programming libraries, SDKs, and utilities for building legal tech applications.

### Document Processing Libraries

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| **[python-docx](https://github.com/python-openxml/python-docx)** | Python library for creating, reading, and modifying Microsoft Word documents programmatically with full support for paragraphs, tables, styles, and document structure. | Python | MIT | 2026-03-02 |
| **[pdfplumber](https://github.com/jsvine/pdfplumber)** | Specialized PDF extraction tool providing detailed access to text, characters, rectangles, and lines for precise coordinate-based data extraction and table identification. | Python | MIT | 2026-03-02 |
| **[PyPDF](https://pypi.org/project/pypdf/)** | Pure-Python library for splitting, merging, cropping, and transforming PDF pages while extracting text from electronically-generated documents. | Python | BSD-3-Clause | 2026-03-02 |
| **[python-docx-template](https://github.com/elapouya/python-docx-template)** | Document generation library that injects Jinja2 templating into .docx files for dynamic content insertion and automated legal document assembly. | Python | LGPL-2.1 | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[x-ray](https://github.com/freelawproject/x-ray)** | Python library from the Free Law Project that detects improperly redacted text in PDF documents by scanning for text hidden beneath rectangles or solid shapes. | Python | BSD-2-Clause | 2026-03-02 |
| **[EdgeParse](https://github.com/raphaelmansuy/edgeparse)** | High-accuracy Rust-based PDF converter that deterministically transforms digital PDFs into Markdown, JSON with bounding boxes, HTML, or plain text without requiring a JVM or GPU. | Rust | Other | 2026-03-25 |
| **[Python-Redlines](https://github.com/JSv4/Python-Redlines)** | Python library for generating docx tracked-change redlines, enabling programmatic creation of legal document comparisons with native Word Track Changes formatting. | Python | MIT | 2026-03-25 |
| **[office-word-diff](https://github.com/yuch85/office-word-diff)** | Library for applying word-level text diffs to Microsoft Word via Office.js API, preserving formatting with cascading fallback strategies for AI text editing and grammar checking in Word add-ins. | TypeScript, Office.js | Apache-2.0 | 2026-03-25 |
| **[Docxodus](https://github.com/JSv4/Docxodus)** | Office XML redline engine built on the OpenXML SDK that generates tracked-change DOCX comparisons, providing C# support for programmatic legal document redlining. | C# | MIT | 2026-04-06 |

### Legal NLP & Text Processing

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[LexNLP](https://github.com/LexPredict/lexpredict-lexnlp)*** | *Specialized Python library for natural language processing and information extraction from legal and regulatory texts with pre-trained models. ⚠️ Stale (2024-05)* | *Python* | AGPL-3.0 | *2026-03-02* |
| **[spaCy](https://spacy.io/)** | Industrial-strength NLP library with pre-trained models for named entity recognition in contracts and legal documents. | Python, spaCy | MIT | 2026-03-02 |
| <img src="https://flagcdn.com/w20/gb.png" width="20" height="15" alt="UK"> **[Blackstone](https://github.com/ICLRandD/Blackstone)** | spaCy-based natural language processing model trained on English case law that detects legal entities and classifies sentences by legal purpose. | Python, spaCy | Apache-2.0 | 2026-03-02 |
| **[ContextGem](https://github.com/shcherbak-ai/contextgem)** | Open-source Python LLM framework for extracting structured data and insights from documents with minimal code, supporting multi-level extraction workflows with paragraph-level source references, reasoning justifications, and multilingual support across multiple LLM providers. | Python | Apache-2.0 | 2026-03-03 |
| <img src="https://flagcdn.com/w20/de.png" width="20" height="15" alt="DE"> **[bundesrecht](https://github.com/harshildarji/bundesrecht)** | Python package for parsing, normalising, and resolving German federal law references from legal texts, enabling programmatic access to citations from gesetze-im-internet.de. | Python | MIT | 2026-06-11 |

### Document Services & Integration

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| **[Apache Tika](https://tika.apache.org/)** | Enterprise-grade content detection and analysis framework that extracts metadata and text from 1000+ file types including PDFs and Office documents. | Java | Apache-2.0 | 2026-03-02 |
| **[Office-Word-MCP-Server](https://github.com/GongRzhe/Office-Word-MCP-Server)** | Model Context Protocol (MCP) server enabling AI assistants to create, read, and manipulate Word documents with rich formatting preservation. | TypeScript | MIT | 2026-03-02 |

### Smart Contract & Templating

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| **[Accord Project](https://accordproject.org/)** | Open-source ecosystem for smart legal contracts with the Cicero templating system for creating structured, reusable contract templates. | | Apache-2.0 | 2026-03-02 |
| **[Docassemble](https://docassemble.org/)** | Full-stack expert system for guided legal interviews and document automation built in Python/YAML/Markdown with support for complex workflows. | Python, YAML | MIT | 2026-03-02 |
| **[Legalis](https://github.com/cool-japan/legalis)** | Rust framework for parsing, analyzing, and simulating legal statutes, transforming natural language legal documents into structured, machine-verifiable code. | Rust | Apache-2.0 | 2026-03-03 |

## Legal Tech Developer Tools

General-purpose libraries and tools especially useful when building legal technology applications, from document ingestion pipelines to NLP workflows.

### Document Processing & OCR

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| **[MinerU](https://github.com/opendatalab/MinerU)** | High-accuracy document parser that transforms PDFs and Office files into LLM-ready Markdown, JSON with bounding boxes, or plain text, with layout analysis, formula extraction, and multi-column support. | Python | Other | 2026-04-06 |
| **[Scriberr](https://github.com/rishikanthc/Scriberr)** | Self-hosted AI audio transcription service with fully local processing, suitable for transcribing depositions, hearings, and client meetings without sending audio to external servers. | Go | MIT | 2026-04-06 |
| **[Docling](https://github.com/docling-project/docling)** | IBM's document conversion toolkit that transforms PDFs, Word, PowerPoint, and HTML into structured Markdown or JSON with layout preservation, table extraction, and reading order detection, designed for LLM ingestion pipelines. | Python | MIT | 2026-04-06 |
| **[Marker](https://github.com/datalab-to/marker)** | High-accuracy PDF to Markdown and JSON converter handling complex layouts including tables, equations, and multi-column text, optimized for speed in document ingestion pipelines. | Python | GPL-3.0 | 2026-04-06 |
| **[noroboto](https://github.com/LegalQuants/noroboto)** | Proof-of-concept tool that applies Unicode obfuscation to DOCX and PDF documents to deter automated scraping and machine extraction. | Python | MIT | 2026-06-11 |

### NLP & Named Entity Recognition

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| **[Hugging Face Transformers](https://github.com/huggingface/transformers)** | Leading open-source library for loading and fine-tuning transformer models; widely used to run legal BERT variants, clause classifiers, and contract information extractors. | Python | Apache-2.0 | 2026-04-06 |
| **[Stanza](https://github.com/stanfordnlp/stanza)** | Stanford NLP Python library with pre-trained pipelines for tokenization, POS tagging, NER, and dependency parsing across 60+ languages, applicable to multi-jurisdiction legal text processing. | Python | Other | 2026-04-06 |
| **[NLTK](https://github.com/nltk/nltk)** | Foundational Python toolkit for natural language processing providing tokenization, stemming, tagging, parsing, and corpus utilities; widely used as a baseline in legal text processing research. | Python | Apache-2.0 | 2026-04-06 |
| **[Flair](https://github.com/flairNLP/flair)** | NLP framework for sequence labeling, NER, and text classification with state-of-the-art contextual string embeddings; useful for training custom NER models on legal text corpora. | Python | Other | 2026-04-06 |

## Access to Justice

Tools and platforms designed to improve access to legal services and justice.

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| **[Docassemble](https://github.com/jhpyle/docassemble)** | Expert system for guided interviews and document assembly that helps self-represented litigants generate court documents and legal forms. | Python, YAML | MIT | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[docassemble-AssemblyLine](https://github.com/SuffolkLITLab/docassemble-AssemblyLine)** | Rapid deployment framework converting paper court forms into interactive web applications for legal aid organizations. | Python, YAML | MIT | 2026-03-02 |
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[A2J Author](https://github.com/CCALI/a2j-author)*** | *Open-source tool for creating guided interviews that help people complete legal forms and court documents. ⚠️ Stale (archived/removed)* | | — | *2026-03-02* |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Namesake](https://github.com/namesakefyi/namesake)** | Web app guiding users through the legal name and gender marker change process in the United States, tracking requirements across jurisdictions. | TypeScript, React | GPL-3.0 | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Upsolve](https://www.upsolve.org)** | Free online bankruptcy filing tool designed to help individuals file Chapter 7 bankruptcy without expensive attorney fees. | | Not FOSS | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[LawSage](https://github.com/tomwolfe/LawSage)** | AI-powered open-source platform that translates complex laws into actionable court-ready defenses for self-represented litigants regardless of income, converting voice or text descriptions of legal issues into precise filings and legal strategies. | TypeScript | MIT | 2026-06-29 |

## Legal NLP & Datasets

Academic datasets, models, and tools for legal natural language processing research.

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| **[Legal ML Datasets](https://github.com/neelguha/legal-ml-datasets)** | Curated collection of datasets and machine learning tasks for legal text processing, including contract understanding and clause classification. | | No license | 2026-03-02 |
| **[Awesome Legal NLP](https://github.com/maastrichtlawtech/awesome-legal-nlp)** | Curated collection aggregating 180+ legal NLP datasets, models, research papers, and implementation guidance. | | MIT | 2026-03-02 |
| <img src="https://flagcdn.com/w20/gb.png" width="20" height="15" alt="UK"> **[Blackstone](https://github.com/ICLRandD/Blackstone)** | spaCy-based natural language processing model trained on English case law for detecting legal entities and clause classification. | Python, spaCy | Apache-2.0 | 2026-03-02 |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[ChatLaw](https://github.com/PKU-YuanGroup/ChatLaw)** | Large language model trained on Chinese legal documents and court data, achieving higher accuracy than GPT-4 on Chinese legal benchmarks. | Python, PyTorch | AGPL-3.0 | 2026-03-02 |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[DISC-LawLLM](https://github.com/FudanDISC/DISC-LawLLM)** | Intelligent legal system with LLM fine-tuned with 300K legal task examples, ranking highly on legal AI benchmarks. | Python, PyTorch | Apache-2.0 | 2026-03-02 |
| *<img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[LawBench](https://github.com/open-compass/LawBench)*** | *Comprehensive evaluation benchmark for assessing language models' legal knowledge across 20 tasks covering Chinese law. ⚠️ Stale (2023-11)* | | Apache-2.0 | *2026-03-02* |
| <img src="https://flagcdn.com/w20/in.png" width="20" height="15" alt="IN"> **[MILDSum](https://github.com/Law-AI/mildsum)** | Benchmark dataset and tools for multilingual legal document summarization with Indian court judgments. | Python | No license | 2026-03-02 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[LexGLUE](https://github.com/coastalcph/lex-glue)** | Benchmark combining seven legal NLP datasets for evaluating language models on tasks spanning European Court of Human Rights cases, US Supreme Court decisions, EU legislation, and contract analysis. | Python | No license | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[LegalBench-RAG](https://github.com/zeroentropy-ai/legalbenchrag)** | Information retrieval benchmark for evaluating RAG systems on complex legal contract questions, aggregating ground-truth snippets from ContractNLI, CUAD, MAUD, and PrivacyQA datasets. | Python | MIT | 2026-03-02 |
| **[Canadian Legal Data](https://github.com/a2aj-ca/canadian-legal-data)** | Repository for accessing bulk Canadian legal data maintained by Access to Artificial Justice, providing structured datasets for legal text processing and research. | | No license | 2026-03-03 |
| **[LLM-and-Law](https://github.com/Jeryi-Sun/LLM-and-Law)** | Actively maintained curated paper list summarizing large language models applied to legal tasks including judgment prediction, document analysis, and legal reasoning research. | | No license | 2026-03-25 |
| **[AALawyer](https://github.com/theSleepyPig/AALawyer)** | ACL 2026 research system that mitigates legal hallucinations via symbolic constraints and analogical precedent retrieval, providing a framework for legally grounded LLM responses. | Python | No license | 2026-06-11 |
| <img src="https://flagcdn.com/w20/gb.png" width="20" height="15" alt="UK"> **[UK Statute Retrieval](https://github.com/alshehriamal1994/uk-statute-retrieval)** | Provision-level retrieval and neural reranking model for UK legislation with an open distilled ModernBERT reranker, from the Artificial Intelligence and Law (2026) paper, supporting precise statutory search at the provision level. | Python | MIT | 2026-06-15 |
| **[Urdu Legal NER Corpora](https://github.com/scheema286/-Urdu-Legal_ner_corpora)** | 117,500 annotated Urdu legal documents for named entity recognition research, presented at RANLP 2025, the first large-scale NER corpus for Urdu legal text. | | MIT | 2026-06-15 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[EU AI Act Dataset](https://github.com/jeroenherczeg/eu-ai-act-dataset)** | Reproducible pipeline transforming the official EU AI Act Formex XML into a structured, multilingual, retrieval-ready Hugging Face Parquet dataset covering 24 official EU languages with structural metadata, effective-date fields, and cross-references. | Python | Other | 2026-06-22 |

### Public Datasets

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[The Atticus Project — CUAD & ACORD](https://www.atticusprojectai.org/datasets)** | Two annotated contract datasets from the same non-profit: CUAD covers 500+ commercial contracts across 41 clause types; ACORD provides 126,000+ expert-rated query-clause pairs for complex clauses like indemnification and limitation of liability. | | CC-BY-4.0 | 2026-03-19 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[LEDGAR](https://huggingface.co/datasets/coastalcph/ledgar)** | 80,000 contract provisions extracted from SEC filings, covering clause types including confidentiality, governing law, and indemnification, available on HuggingFace. | | Other | 2026-03-19 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[ContractNLI](https://stanfordnlp.github.io/contract-nli/)** | 607 annotated NDAs from Stanford NLP for natural language inference on legal contracts, released under Creative Commons. | | CC-BY-4.0 | 2026-03-19 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Stanford Material Contracts Corpus (MCC)](https://mcc.law.stanford.edu)** | 1M+ real agreements filed with the SEC between 2000–2023, fully searchable by contract type and party; the largest open contract dataset available. | | Public domain | 2026-03-19 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[LexGLUE](https://huggingface.co/datasets/coastalcph/lex_glue)** | Bundle of multiple legal NLP datasets in one place on HuggingFace, including LEDGAR and UNFAIR-ToS (terms of service annotations), for benchmarking language models on legal tasks. | | Other | 2026-03-19 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[SEC EDGAR](https://www.sec.gov/cgi-bin/browse-edgar)** | Primary public source of millions of contracts filed by U.S. public companies, with free access to the raw filings behind many of the datasets above. | | Public domain | 2026-03-19 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[TREC Legal Track](https://trec-legal.umiacs.umd.edu/corpora/trec/legal10/)** | Document corpora and relevance judgments from the TREC Legal Track competitions, designed for evaluating e-discovery and legal information retrieval systems. | | Public domain | 2026-03-19 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Caselaw Access Project](https://case.law/)** | Harvard Law School's digitized archive of all official U.S. court decisions published in books from the 1600s to 2020, covering 40+ million pages of legal text. | | CC0-1.0 | 2026-03-19 |
| **[ICC Case Transcripts](https://www.icc-cpi.int/case-transcripts)** | Official transcripts of proceedings before the International Criminal Court, freely available for legal NLP research on international criminal law. | | Public domain | 2026-03-19 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Descrybe Legal Research](https://descrybe.ai/)** | Free case law research tool with no login required that searches U.S. federal and state court decisions using plain English queries with AI-generated summaries. | | Not FOSS | 2026-03-19 |

## Compliance & Regulatory Technology

Tools for regulatory compliance, sanctions screening, policy monitoring, and automated regulatory reporting.

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| **[OpenSanctions](https://github.com/opensanctions/opensanctions)** | An open database of international sanctions data, persons of interest, and politically exposed persons (PEPs) for KYC/AML compliance screening. | Python | MIT | 2026-03-02 |
| **[Watchman](https://github.com/moov-io/watchman)** | A high-performance AML/CTF/KYC sanctions screening tool written in Go that searches against OFAC and other global watchlists via an HTTP API. | Go | Apache-2.0 | 2026-03-02 |
| ***[Comply](https://github.com/strongdm/comply)*** | *A compliance automation framework focused on SOC2 that generates auditor-friendly policy documents from Markdown and integrates with ticketing systems. ⚠️ Stale (2022-07)* | *Go* | Apache-2.0 | *2026-03-02* |
| **[Comp](https://github.com/trycompai/comp)** | An AI-native open-source compliance platform covering SOC 2, ISO 27001, HIPAA, and GDPR frameworks as an alternative to Vanta and Drata. | TypeScript, Next.js | AGPL-3.0 | 2026-03-02 |
| **[Marble](https://github.com/checkmarble/marble)** | An open-source real-time decision engine for fraud detection and AML compliance, providing transaction monitoring, sanctions screening, and investigation case management. | Go | Other | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[GovReady-Q](https://github.com/GovReady/govready-q)** | An open-source GRC (Governance, Risk, and Compliance) platform that automates security assessments and compliance documentation for DevSecOps workflows. | Python, Django | Other | 2026-03-02 |
| **[FIRE Data Standard](https://github.com/SuadeLabs/fire)** | The Financial Regulation Data Standard defining a common open specification for the transmission of granular data between regulatory systems in finance. | | Apache-2.0 | 2026-03-02 |
| **[Compliance-to-Policy](https://github.com/oscal-compass/compliance-to-policy)** | A framework bridging compliance-as-code (OSCAL) and policy-as-code engines like Kyverno for automated compliance verification. | | Apache-2.0 | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[RegTech Data Validator](https://github.com/cfpb/regtech-data-validator)** | Python-based tool by the Consumer Financial Protection Bureau for parsing and validating regulatory data submissions using Pandera schemas. | Python | CC0-1.0 | 2026-03-02 |
| **[Legal Guard](https://github.com/nathangtg/legal-guard-regtech)** | AI-powered regulatory analysis tool that transforms complex documents into plain English, assesses risks, and checks against regulations like GDPR and PDPA. | Python | No license | 2026-03-03 |
| **[Probo](https://github.com/getprobo/probo)** | Open-source compliance platform for startups supporting SOC 2, GDPR, ISO 27001, HIPAA, ISO 27701, and ISO 42001 as a self-hosted alternative to Vanta and Drata. | TypeScript, Next.js | MIT | 2026-04-06 |
| **[Regis](https://github.com/Flosters/Regis)** | AI-powered corporate ownership mapping and Ultimate Beneficial Owner (UBO) analysis tool that generates interactive ownership charts from natural language prompts or uploaded images, with a unified entity directory and automated syncing. | TypeScript | MIT | 2026-04-06 |
| **[TaxStructuringTool LITE](https://github.com/tech-taitan/TaxStructuringTool_LITE)** | Lightweight entity charting tool for tax professionals that visualizes corporate structures and ownership chains for tax structuring analysis. | TypeScript | No license | 2026-04-06 |
| **[EasyBoard](https://github.com/SaifAlYounan/EasyBoard)** | Open-source board portal for managing corporate board meetings, materials, and governance workflows. | TypeScript | No license | 2026-04-06 |
| **[GRCX](https://github.com/grcx-dev/grcx)** | Open-source regulatory radar for financial services compliance teams that monitors publications from BoE, FCA, MAS, SEC, and ESMA, mapping them to six control frameworks with a cryptographic audit trail. | TypeScript | MIT | 2026-06-11 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[getregdata](https://github.com/Nolpak14/getregdata)** | Claude Code skills for querying European government registry data across multiple jurisdictions to support KYC, credit risk, property verification, compliance, and lead generation workflows. | | MIT | 2026-06-15 |
| **[GEPA Compliance Optimizer](https://github.com/anastasiosyal/dspy-gepa-optimizer)** | DSPy-based prompt optimization tool that mines compliance rubrics from labelled regulatory decisions using the GEPA algorithm, achieving 30% more violation detections starting from a single-line prompt. | Python | MIT | 2026-06-22 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[Regulus](https://github.com/neul-labs/regulus)** | Open-source compliance plane for Google ADK adding six BasePlugin extensions — policy enforcement, privacy controls, audit trails, kill switches, model risk assessment, and data residency — with ten regulation profiles including EU AI Act, GDPR, UK GDPR, DORA, NIS2, and FCA rules. | Java | MIT | 2026-06-29 |


## eDiscovery & Litigation Support

Software for electronically stored information (ESI) collection, processing, review, and production.

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| **[FreeEed](https://github.com/shmsoft/FreeEed)** | An open-source, AI-enabled eDiscovery platform that processes over 1,400 file types including PST, MS Office, and images with OCR for document review, search, and production. | Java | Apache-2.0 | 2026-03-02 |
| **[Autopsy](https://github.com/sleuthkit/autopsy)** | A widely-used digital forensics platform with a graphical interface to The Sleuth Kit, used by law enforcement, military, and corporate examiners to investigate computers and recover evidence for legal proceedings. | Java | No license | 2026-03-02 |
| **[Mattermost Legal Hold](https://github.com/mattermost/mattermost-plugin-legal-hold)** | A Mattermost plugin enabling administrators to place users on legal hold for a defined time period, with daily data collection and export capabilities for litigation compliance. | Go | Other | 2026-03-02 |
| ***[Open-Source-eDiscovery](https://github.com/dillonupgradeit/Open-Source-eDiscovery)*** | *A Python-based eDiscovery application for creating and searching litigation productions from PDFs, emails, Office documents, images, and video files. ⚠️ Stale (2020-11)* | *Python* | MIT | *2026-03-02* |
| **[enigma](https://github.com/McFlip/enigma)** | A Go-based eDiscovery tool for bulk decryption of emails in PST files and loose .eml files, designed for forensic and legal discovery workflows requiring legitimate certificate-based decryption. | Go | MIT | 2026-03-02 |
| **[ICIJ Extract](https://github.com/ICIJ/extract)** | Cross-platform command-line tool for parallelized content extraction and analysis of documents, used by the International Consortium of Investigative Journalists for large-scale document investigations. | Java | MIT | 2026-03-02 |
| **[ReelDiscovery](https://github.com/ghanderson77-ops/ReelDiscovery)** | AI-powered e-discovery email dataset generator from QuikData that creates realistic corporate email threads with authentic headers, attachments, and storyline-driven content for training, testing, and demonstration of e-discovery systems. | C# | GPL-3.0 | 2026-04-06 |
| ***[Bates Labeler](https://github.com/safnjnf/Bates-Labeler)*** | *Python tool for adding Bates numbers to PDF documents, simplifying document management and organization for legal discovery and production workflows. ⚠️ Stale (archived/removed)* | *Python* | MIT | *2026-06-15* |

## Legal Analytics & Prediction

Platforms for litigation outcome prediction, judge analytics, legal data visualization, and data-driven legal insights.

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[scotus-predict-v2](https://github.com/mjbommar/scotus-predict-v2)*** | *A random-forest-based model that predicts U.S. Supreme Court case outcomes and individual justice votes across nearly two centuries of decisions (1816-2014), achieving 70.2% case-level accuracy. ⚠️ Stale (2017-04)* | *Python* | No license | *2026-03-02* |
| *<img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[legal-case-prediction](https://github.com/conorosully/legal-case-prediction)*** | *An MSc project using NLP and machine learning including custom word embeddings to predict judicial decisions of the European Court of Human Rights. ⚠️ Stale (2021-01)* | *Python* | MIT | *2026-03-02* |
| *<img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[ECHR-OD_predictions](https://github.com/echr-od/ECHR-OD_predictions)*** | *Implements a complete experimental framework for predicting European Court of Human Rights outcomes using binary, multiclass, and multilabel classification with multiple ML algorithms. ⚠️ Stale (2022-12)* | *Python* | No license | *2026-03-02* |
| <img src="https://flagcdn.com/w20/in.png" width="20" height="15" alt="IN"> **[Realistic_LJP](https://github.com/ShubhamKumarNigam/Realistic_LJP)** | Evaluates transformer models (InLegalBERT, BERT, XLNet) and LLMs for realistic legal judgment prediction on Indian court cases, presented at the NLLP Workshop at EMNLP 2024. | Python, PyTorch | Apache-2.0 | 2026-03-02 |
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[recidivism-predictions](https://github.com/stanford-policylab/recidivism-predictions)*** | *Stanford Policy Lab replication code for the Science Advances paper comparing human vs. algorithmic accuracy in predicting criminal reoffending. ⚠️ Stale (2020-05)* | *Python* | No license | *2026-03-02* |
| **[Legal-Text-Analytics](https://github.com/Liquid-Legal-Institute/Legal-Text-Analytics)** | A comprehensive curated list of resources, methods, and tools for legal text analytics covering NER, case outcome prediction, argument mining, summarization, and datasets from multiple jurisdictions. | | CC-BY-SA-4.0 | 2026-03-02 |
| <img src="https://flagcdn.com/w20/nl.png" width="20" height="15" alt="NL"> **[Case Explorer](https://github.com/maastrichtlawtech/case-explorer-ui)** | Network analysis platform for visualizing and exploring citation networks in Dutch and European court decisions, developed by Maastricht Law & Tech Lab. | TypeScript, React | MIT | 2026-03-02 |

## IP & Patent Technology

Tools for patent search, trademark monitoring, IP portfolio management, prior art analysis, and patent classification.

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| **[PatZilla](https://github.com/ip-tools/patzilla)** | A modular patent information research platform and data integration toolkit with a modern UI and access to multiple data sources including the European Patent Office. | Python | AGPL-3.0 | 2026-03-02 |
| ***[PatentInspector](https://github.com/KonstantinosPetrakis/PatentInspector)*** | *An open-source patent analyzing web application built with Django and Vue 3, allowing users to search, filter, and export patent data. ⚠️ Stale (2023-12)* | *Python, Django* | GPL-3.0 | *2026-03-02* |
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[pypatent](https://github.com/daneads/pypatent)*** | *A Python package for searching and scraping US Patent and Trademark Office patent data, outputting results as DataFrames or lists. ⚠️ Stale (2020-06)* | *Python* | GPL-3.0 | *2026-03-02* |
| ***[patents-public-data](https://github.com/google/patents-public-data)*** | *Google's official collection of BigQuery datasets and Jupyter notebooks for conducting large-scale statistical analysis of patent data. ⚠️ Stale (2024-06)* | *Python* | Apache-2.0 | *2026-03-02* |
| **[PatentSBERTa](https://github.com/AI-Growth-Lab/PatentSBERTa)** | A deep NLP hybrid model combining Sentence-BERT and KNN for patent distance measurement and classification, trained on 1.5M+ patents. | Python, PyTorch | MIT | 2026-03-02 |
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[hupd](https://github.com/suzgunmirac/hupd)*** | *The Harvard USPTO Patent Dataset containing 4.5 million utility patent applications (2004-2018) with NLP models for patent acceptance prediction, classification, and summarization. ⚠️ Stale (2023-12)* | *Python, PyTorch* | MIT | *2026-03-02* |
| **[phpip](https://github.com/jjdejong/phpip)** | A web-based patent and IP rights portfolio manager and docketing system built on Laravel/PHP with features for document merging, renewal management, and patent database integration. | PHP, Laravel | GPL-3.0 | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Patent MCP Server](https://github.com/riemannzeta/patent_mcp_server)** | FastMCP server providing AI assistants with access to USPTO patent data through multiple APIs including Patent Public Search, Open Data Portal, PTAB, PatentsView, and Office Action APIs. | Python | MIT | 2026-03-03 |
| **[Patent Prompts](https://github.com/arcprime-ip/patent-prompts)** | Curated AI prompts for patent workflows including claim drafting, prior art analysis, and continuation strategy based on real USPTO practice, installable as agent skills. | | MIT | 2026-03-25 |
| **[PQAI](https://github.com/pqaidevteam/pqai)** | AI-powered prior-art search server that accepts plain-language invention descriptions and retrieves semantically similar patents and technical literature from global patent databases. | Python | MIT | 2026-06-11 |
| **[OPS Patent Search MCP](https://github.com/navisbio/OPS-patent-search-mcp)** | MCP server for searching and retrieving patents via the EPO Open Patent Services API, providing AI assistants with access to the full global patent corpus including EP, US, WO, JP, and CN filings. | Python | MIT | 2026-06-11 |
| **[iPatent](https://github.com/TIBHannover/iPatent)** | Interactive web-based patent search and analysis prototype supporting prior art search, cross-domain search, infringement detection, and freedom-to-operate analysis using multimodal patent image retrieval. | | MIT | 2026-06-15 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Superhighway Patent Research Agent](https://superhighway.walls.sh/guides/patent-research-agent)** | Python agent that maps patent landscapes, finds prior art (patents + academic publications), assesses freedom-to-operate risk, and tracks competitor patent filings using live web search. Generates structured patent intelligence briefs with key patent holders, key patents, FTO risk assessment, expiry landscape, and search gap disclosure. Pay-per-call, no signup. | Python | | 2026-06-16 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[USPTO ODP Go Client](https://github.com/patent-dev/uspto-odp)** | Complete Go client library for the USPTO Open Data Portal API wrapping 53 endpoints across Patent Application, Bulk Data, Petition, PTAB, Office Action, and TSDR services, with patent number normalization and automatic retry logic. | Go | MIT | 2026-06-22 |
| **[OpenPatent](https://github.com/erdalbektas/OpenPatent)** | Fully local, open-source patent suite using AI agents for patent searching, drafting, prosecution, consulting, litigation support, and portfolio management with BYOK or any model provider support, requiring no cloud dependency. | TypeScript | Other | 2026-06-29 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[PatentAI](https://github.com/yorkeccak/patents)** | Open-source conversational patent assistant that searches and analyzes the entire USPTO corpus using natural language, with prior art analysis, freedom-to-operate assessment, competitive intelligence, and technology trend visualization. | TypeScript | MIT | 2026-06-29 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Claude-Patent-Creator](https://github.com/RobThePCGuy/Claude-Patent-Creator)** | USPTO patent creation system combining an MCP server and Claude Code plugin with hybrid RAG search over MPEP/USC/CFR, BigQuery access to 76M+ patents, automated 35 USC 112 compliance checks, prior art search, and diagram generation. | Python | MIT | 2026-06-29 |

## Privacy & Data Protection

Specialized tools for privacy impact assessments, consent management, DSAR automation, and privacy policy generation.

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| **[Fides](https://github.com/ethyca/fides)** | An open-source privacy engineering platform for managing data privacy requests (DSAR orchestration) and enforcing GDPR/CCPA/LGPD regulations in code with privacy-as-code workflows. | Python | Apache-2.0 | 2026-03-02 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[Klaro](https://github.com/kiprotect/klaro)** | An open-source, lightweight consent management platform that helps websites be transparent about third-party applications with GDPR/ePrivacy-compliant consent flows and support for 17+ languages. | TypeScript | Other | 2026-03-02 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[cookieconsent](https://github.com/orestbida/cookieconsent)** | A lightweight, cross-browser, GDPR-compliant cookie consent plugin written in vanilla JavaScript with extensive customization options. | TypeScript | MIT | 2026-03-02 |
| **[app-privacy-policy-generator](https://github.com/nisrulz/app-privacy-policy-generator)** | A free, open-source web app that generates customized, GDPR-compliant privacy policies and terms of use documents for mobile applications. | | AGPL-3.0 | 2026-03-02 |
| **[CISO Assistant](https://github.com/intuitem/ciso-assistant-community)** | A comprehensive open-source GRC platform supporting 100+ frameworks including GDPR, HIPAA, ISO 27001, and NIS2, with built-in risk assessment and compliance auditing. | Python | Other | 2026-03-02 |
| **[ML Privacy Meter](https://github.com/privacytrustlab/ml_privacy_meter)** | An open-source Python library for auditing data privacy in machine learning models through membership inference attacks, supporting GDPR-mandated data protection impact assessments. | Python | MIT | 2026-03-02 |
| **[Databunker](https://github.com/securitybunker/databunker)** | Self-hosted secure vault for storing and managing customer PII, PHI, PCI, and KYC records with built-in tokenization and encryption to support GDPR, HIPAA, and SOC 2 compliance. | Go | MIT | 2026-04-06 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[PrivacyQuant](https://github.com/LegalQuants/privacyquant)** | Versioned statutory knowledge graph and MCP workflow layer for US state consumer privacy law, enabling applicability triage, gap analysis, DSAR routing, and conflict-of-laws synthesis across state privacy statutes. | TypeScript | MIT | 2026-06-11 |
| **[Pinpoint](https://github.com/zgbrenner/pinpoint)** | Privacy-first, no-account AI policy builder that runs entirely in the browser without retaining user data, generating and exporting a complete AI governance policy pack. | | MIT | 2026-06-15 |
| <img src="https://flagcdn.com/w20/kr.png" width="20" height="15" alt="KR"> **[Korean Privacy Terms](https://github.com/kimlawtech/korean-privacy-terms)** | Claude Code skill for auto-generating Korean privacy policies and terms of service compliant with the 2025.4.21 drafting guidelines and 2026 revised Korean privacy law. | | Apache-2.0 | 2026-06-15 |

## Legal Workflow Automation

Platforms and tools for automating legal processes, document lifecycles, and contract analytics.

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| ***[ContraxSuite](https://github.com/LexPredict/lexpredict-contraxsuite)*** | *An open-source contract analytics and legal document exploration platform using NLP and machine learning to extract clauses, entities, and structured data from unstructured legal text. ⚠️ Stale (2023-02)* | *Python* | AGPL-3.0 | *2026-03-02* |
| **[Wraft](https://github.com/wraft/wraft)** | An open-source Document Lifecycle Management platform built with Elixir and React that helps businesses create, manage, approve, and sign documents from official letters to contracts. | | AGPL-3.0 | 2026-03-02 |
| **[CommonAccord](https://github.com/CommonAccord/Cmacc-Org)** | An initiative to create global codes of legal transacting by codifying and automating legal documents as composable, interoperable objects. | | MIT | 2026-03-02 |
| **[Open Cap Format (OCF)](https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF)** | Open-source data standard for structuring and tracking capitalization table data for startups and private companies, enabling interoperability between cap table tools and legal systems. | | Other | 2026-06-11 |

## Court & Government Filing Systems

E-filing platforms, court management systems, government legal portals, and legal data standards.

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Open Case Filing System](https://github.com/federal-courts-software-factory/open-case-filing-system)*** | *A public-domain platform by the Federal Courts Software Factory designed as a modern replacement for the federal CM/ECF system, built with Rust and PostgreSQL. ⚠️ Stale (2024-05)* | *Rust* | CC0-1.0 | *2026-03-02* |
| <img src="https://flagcdn.com/w20/za.png" width="20" height="15" alt="ZA"> **[Indigo](https://github.com/laws-africa/indigo)** | A Django-based legislation publishing platform by Laws.Africa for managing, consolidating, and publishing legislation in the Akoma Ntoso XML standard, with export to HTML, PDF, and ePUB. | Python, Django | Other | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Courts-DB](https://github.com/freelawproject/courts-db)** | A comprehensive open-source database of current and historical courts maintained by Free Law Project, containing metadata from over 16 million data points. | Python | BSD-2-Clause | 2026-03-02 |
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[LegalXML Court Filing 5.0](https://github.com/oasis-tcs/legalxml-courtfiling-5.0-spec)*** | *The OASIS LegalXML Electronic Court Filing TC repository containing the ECF 5.0 specification, schemas, and examples for interoperable electronic court filing systems. ⚠️ Stale (2019-05)* | | Other | *2026-03-02* |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[NIEM Model](https://github.com/niemopen/niem-model)** | The National Information Exchange Model reference data model, an OASIS Open Project providing a common vocabulary with domain namespaces including Justice for government information exchange. | | Other | 2026-03-02 |
| <img src="https://flagcdn.com/w20/de.png" width="20" height="15" alt="DE"> **[Open Legal Data Platform (OLDP)](https://github.com/openlegaldata/oldp)** | A Django-based open data platform for processing and publishing legal documents with search and API access to court decisions and laws. | Python, Django | MIT | 2026-03-02 |
| <img src="https://flagcdn.com/w20/de.png" width="20" height="15" alt="DE"> **[RIS Caselaw](https://github.com/digitalservicebund/ris-backend-service)** | Backend service for the German federal caselaw platform that manages, stores, and provides API access to judicial decisions across German courts. | Java, TypeScript | GPL-3.0 | 2026-04-06 |
| <img src="https://flagcdn.com/w20/gb.png" width="20" height="15" alt="UK"> **[Find Case Law — Data Enrichment Service](https://github.com/nationalarchives/ds-caselaw-data-enrichment-service)** | Service used by The National Archives to automatically annotate UK judicial decisions with references to cited cases and relevant legislation for the Find Case Law platform. | Python | MIT | 2026-04-06 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[NYC Charter Laws & Rules MCP](https://github.com/BetaNYC/nyc-charter-laws-rules)** | MCP server providing AI assistants with access to the New York City Charter, Administrative Code, and Rules of the City of New York, kept current with the latest local laws. | TypeScript | MIT | 2026-06-11 |
| **[StateDecoded](https://github.com/statedecoded/statedecoded)** | Open-source platform for publishing legal codes as structured, human-readable web content with full-text search, permalinks, and API access, designed for state and municipal governments. | PHP | Other | 2026-06-11 |
| **[Tezca](https://github.com/madfam-org/tezca)** | Open legal intelligence platform for Mexico providing access to 30,000+ laws across federal, state, and municipal sources with 3.5M+ searchable articles, a trilingual interface, and an API for AI agent integration. | | AGPL-3.0 | 2026-06-11 |
| <img src="https://flagcdn.com/w20/jp.png" width="20" height="15" alt="JP"> **[gitlaw-jp](https://github.com/aluqas/gitlaw-jp)** | Converts Japanese legislation from the e-gov API into a Git repository where each amendment becomes a trackable commit, enabling diff-based comparison of legal changes across promulgation and enforcement branches. | Python | No license | 2026-06-22 |

## Legal Ontologies & Knowledge Graphs

Structured legal knowledge representations, ontologies, and tools for building legal knowledge graphs and reasoning systems.

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| **[LKIF Core](https://github.com/RinkeHoekstra/lkif-core)** | The LKIF Core legal ontology library consisting of 15 OWL modules covering fundamental legal and commonsense concepts across abstract, basic, and legal layers. | | No license | 2026-03-02 |
| ***[LegalRuleML](https://github.com/oasis-tcs/legalruleml)*** | *The official OASIS LegalRuleML Technical Committee repository for developing examples and sharing knowledge about the correct application of the LegalRuleML standard for representing legal norms in markup. ⚠️ Stale (2020-07)* | | Other | *2026-03-02* |
| ***[LegalDocML Akoma Ntoso](https://github.com/oasis-open/legaldocml-akomantoso)*** | *The official OASIS TC Open Repository containing schema files, examples, implementations, and libraries for the Akoma Ntoso legal document XML standard. ⚠️ Stale (2022-06)* | | Other | *2026-03-02* |
| <img src="https://flagcdn.com/w20/za.png" width="20" height="15" alt="ZA"> **[Bluebell](https://github.com/laws-africa/bluebell)** | A generic Akoma Ntoso 3 parser in Python supporting all hierarchical elements and multiple legal document types including acts, bills, debates, and judgments. | Python | GPL-3.0 | 2026-03-02 |
| **[FOLIO](https://github.com/alea-institute/FOLIO)** | The Federated Open Legal Information Ontology providing over 18,000 standardized legal concepts with unique identifiers and multilingual support for data interoperability in the legal industry. | | Other | 2026-03-02 |
| ***[Legal-Ontologies](https://github.com/Liquid-Legal-Institute/Legal-Ontologies)*** | *A curated collection of resources, methods, and tools dedicated to legal ontologies, data schemes, and knowledge graphs maintained by the Liquid Legal Institute. ⚠️ Stale (2024-03)* | | CC-BY-SA-4.0 | *2026-03-02* |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[DaPreCo KB](https://github.com/dapreco/daprecokb)** | The largest freely available LegalRuleML knowledge base containing deontic rules formalized in Input/Output logic for GDPR and ISO 27018 compliance mapping. | | No license | 2026-03-02 |
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[SEC Knowledge Graph](https://github.com/AnjaneyaTripathi/knowledge_graph)*** | *A knowledge graph construction tool for SEC litigation releases that classifies legal documents into crime categories and extracts violators, violations, actions, and fines. ⚠️ Stale (2022-02)* | *Python* | No license | *2026-03-02* |

## MCP Servers & AI Agent Tools for Law

Model Context Protocol servers, AI agent frameworks, and tooling specifically designed for legal AI workflows.

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| **[legal-mcp](https://github.com/agentic-ops/legal-mcp)** | A comprehensive Model Context Protocol server for legal workflows designed to bridge AI assistants with legal databases, case management systems, and research tools. | Python | No license | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[courtlistener-mcp](https://github.com/blakeox/courtlistener-mcp)** | An MCP server bridging Claude and other LLMs with the CourtListener API, exposing legal research tools for accessing opinions, dockets, and court records with built-in observability. | Python | MIT | 2026-03-02 |
| **[mcp-cerebra-legal-server](https://github.com/yoda-digital/mcp-cerebra-legal-server)** | An enterprise-grade MCP server for structured legal reasoning and analysis with automatic legal domain detection and citation formatting. | Python | No license | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[us-legal-mcp](https://github.com/JamesANZ/us-legal-mcp)** | An MCP server providing comprehensive US legislation access by searching Congress bills, Federal Register documents, court opinions, and committees from within AI coding environments. | Python | MIT | 2026-03-02 |
| **[LegalBench](https://github.com/HazyResearch/legalbench)** | An open science benchmark of 162 collaboratively curated tasks from 40 contributors for evaluating legal reasoning capabilities in large language models. | Python | No license | 2026-03-02 |
| **[Pasal](https://github.com/ilhamfp/pasal)** | AI-native Indonesian legal platform combining an MCP server with a web app to give Claude grounded access to Indonesian laws and regulations. | Python | AGPL-3.0 | 2026-03-03 |
| <img src="https://flagcdn.com/w20/de.png" width="20" height="15" alt="DE"> **[Ayunis Legal MCP](https://github.com/ayunis-core/ayunis-legal-mcp)** | MCP server for German legal codes with vector-based semantic search, comprising a store API, CLI tool, web scraper, and XML parser for comprehensive legal text analysis. | Python | MIT | 2026-03-03 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Congress.gov MCP Server](https://github.com/bsmi021/mcp-congress_gov_server)** | MCP server providing access to the official Congress.gov API for searching US bills, amendments, committee reports, and legislative data from within AI assistants. | Python | MIT | 2026-03-03 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[EU Compliance MCP](https://github.com/Ansvar-Systems/EU_compliance_MCP)** | EU-focused compliance MCP server making EU regulations searchable, cross-referenceable, and AI-readable, part of Ansvar's suite covering 10+ European jurisdictions. | Python | Apache-2.0 | 2026-03-25 |
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[US Compliance MCP](https://github.com/Ansvar-Systems/US_Compliance_MCP)*** | *MCP server for US cybersecurity and privacy regulations including HIPAA, CCPA, GLBA, FERPA, and COPPA. ⚠️ Stale (archived/removed)* | *Python* | — | *2026-03-25* |
| <img src="https://flagcdn.com/w20/de.png" width="20" height="15" alt="DE"> **[German Law MCP](https://github.com/Ansvar-Systems/German-law-mcp)** | MCP server for querying 6,870 German statutes from gesetze-im-internet.de directly from AI assistants. | Python | Apache-2.0 | 2026-03-25 |
| <img src="https://flagcdn.com/w20/nl.png" width="20" height="15" alt="NL"> **[Dutch Law MCP](https://github.com/Ansvar-Systems/Dutch-law-mcp)** | MCP server for Dutch legislation covering 46 key statutes with 13,815 provisions and EU law cross-references, sourced from wetten.overheid.nl. | Python | Apache-2.0 | 2026-03-25 |
| <img src="https://flagcdn.com/w20/es.png" width="20" height="15" alt="ES"> **[Spanish Law MCP](https://github.com/Ansvar-Systems/spanish-law-mcp)** | MCP server for Spanish law covering data protection (LOPDGDD), national security framework (ENS), cybercrime, e-commerce (LSSI), and NIS2 transposition. | Python | Other | 2026-03-25 |
| <img src="https://flagcdn.com/w20/gb.png" width="20" height="15" alt="UK"> **[UK Case Law MCP](https://github.com/georgejeffers/uk-case-law-mcp-server)** | MCP server enabling LLMs to search, retrieve, and cite UK legal judgments via The National Archives API. | Python | Other | 2026-03-25 |
| **[CanLII MCP](https://github.com/Alhwyn/canlii-mcp)** | MCP server for searching and retrieving Canadian legal information including court decisions, legislation, and citations via the CanLII API. | Python | MIT | 2026-03-25 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[EU AI Act MCP](https://github.com/SonnyLabs/EU_AI_ACT_MCP)** | MCP server helping AI agents comply with the EU AI Act with tools for risk classification, prohibited practice checks, transparency disclosures, and deepfake labeling. | Python | Apache-2.0 | 2026-03-25 |
| **[DOCX Redline MCP](https://github.com/AnsonLai/docx-redline-mcp)** | MCP server for inspecting and editing .docx files with support for real Word tracked changes and comments, purpose-built for legal contract review pipelines. | Python | MIT | 2026-03-25 |
| **[Law7 MCP](https://github.com/mikhashev/law7)** | Open up-to-date legal database for AI assistants via MCP server and core engine. | Python | Other | 2026-03-25 |
| **[Korean Law MCP](https://github.com/chrisryugj/korean-law-mcp)** | MCP server and CLI providing 89 tools for Korean law covering statutes, precedents, ordinances, and legal interpretations, installable via npm. | TypeScript | MIT | 2026-04-06 |
| **[Greek Law MCP](https://github.com/Ansvar-Systems/Greek-law-mcp)** | MCP server providing a comprehensive Greek legal database with 21,119 statutes and 7,793 provisions for cybersecurity compliance queries, part of the Ansvar multi-jurisdiction suite. | Python | Other | 2026-04-06 |
| **[Danish Law MCP](https://github.com/Ansvar-Systems/Danish-law-mcp)** | MCP server providing access to 62,764 Danish laws sourced from Retsinformation for use in AI assistants and compliance workflows. | Python | Apache-2.0 | 2026-04-06 |
| **[FOLIO MCP](https://github.com/alea-institute/folio-mcp)** | MCP server exposing the FOLIO legal ontology (18,000+ standardized legal concepts) to AI assistants for semantic legal classification and knowledge retrieval. | Python | MIT | 2026-04-06 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Vaquill MCP](https://github.com/Vaquill-AI/vaquill-mcp)** | MCP server for the Vaquill legal research API providing AI assistants with access to US federal law (USC, CFR), 50-state legislation, and CourtListener case law in a single interface. | TypeScript | MIT | 2026-06-11 |
| **[CourtListener MCP Server](https://github.com/cyanheads/courtlistener-mcp-server)** | MCP server exposing CourtListener's 9M+ opinion corpus to AI assistants with tools for searching opinions, federal dockets, judge records, citation networks, and oral arguments via STDIO or Streamable HTTP. | TypeScript | No license | 2026-06-11 |
| **[Legal Skills Open](https://github.com/ThomasMoreAI/legal-skills-open)** | Open library of 200+ legal AI skills installable via SKILL.md, covering 39 jurisdictions and designed for use with MCP-compatible agents under the Apache 2.0 license. | | Apache-2.0 | 2026-06-11 |
| <img src="https://flagcdn.com/w20/de.png" width="20" height="15" alt="DE"> **[German Legal MCP](https://github.com/metaneutrons/german-legal-mcp)** | Model Context Protocol server providing unified access to multiple German and EU legal databases for AI-assisted legal research across German federal law and European regulations. | TypeScript | GPL-3.0 | 2026-06-11 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[EU AI Act MCP](https://github.com/lexbeam-software/eu-ai-act-mcp)** | Open-source MCP server giving AI agents nine deterministic tools for EU AI Act (Regulation 2024/1689) compliance, including risk classification, prohibited practice checks, and transparency requirement lookups. | Python | MIT | 2026-06-11 |
| **[LQ Skills](https://github.com/LegalQuants/lq-skills)** | Curated, harness-agnostic collection of legal agent skills built by ~100 lawyer-builders across 17+ jurisdictions, installable across Claude Code, Codex, Gemini CLI, Cursor, and other tools. | Python | Apache-2.0 | 2026-06-11 |
| **[LegalQuants Plugin](https://github.com/LegalQuants/lq-plugin)** | Official LegalQuants Claude Code plugin providing terminal access to the community knowledge archive and curated synthesis vault via an MCP chat server, with member sign-in for a personalized experience. | Shell | No license | 2026-06-11 |
| <img src="https://flagcdn.com/w20/at.png" width="20" height="15" alt="AT"> **[Austria RIS MCP](https://github.com/mburgler/ris-marketplace-dev_version)** | Claude plugin and MCP connector for the Austrian Rechtsinformationssystem (RIS) providing search and citation over federal, state, and municipal law, gazettes, and case law from VfGH, VwGH, OGH, BVwG, LVwG, and DSB. | | Apache-2.0 | 2026-06-15 |
| <img src="https://flagcdn.com/w20/ch.png" width="20" height="15" alt="CH"> **[Fedlex MCP](https://github.com/malkreide/fedlex-mcp)** | MCP server for Swiss federal law (Fedlex) providing search over the SR (systematic compilation), legal change monitoring, and BBl/treaties queries for use in Claude Desktop and Claude.ai. | | MIT | 2026-06-15 |
| <img src="https://flagcdn.com/w20/ar.png" width="20" height="15" alt="AR"> **[Argentina Law MCP](https://github.com/guidobonomini/argentina-law-mcp-server)** | MCP server for Argentine law providing AI agents with document processing, case analysis, legal research, and practice management capabilities for Argentine legal professionals. | | MIT | 2026-06-15 |
| <img src="https://flagcdn.com/w20/tw.png" width="20" height="15" alt="TW"> **[Taiwan Legal DB MCP](https://github.com/lawchat-oss/mcp-taiwan-legal-db)** | MCP server providing AI agents with access to Taiwan Judicial Yuan court decisions and the National Laws and Regulations Database for legal research and analysis. | | MIT | 2026-06-15 |
| **[AgentCounsel](https://github.com/zgbrenner/agentcounsel)** | Open library of legal skills for AI-assisted legal teams, providing reusable skills across practice areas for use in MCP-compatible AI agents. | | MIT | 2026-06-15 |
| <img src="https://flagcdn.com/w20/fr.png" width="20" height="15" alt="FR"> **[French Law MCP](https://github.com/Ansvar-Systems/French-law-mcp)** | MCP server for French legislation providing AI assistants with access to 3,958 statutes and 193,793 articles (Code civil, Code pénal, Code du travail, and more) with EU directive cross-references and daily freshness checks from Légifrance. | Python | Apache-2.0 | 2026-06-22 |
| <img src="https://flagcdn.com/w20/no.png" width="20" height="15" alt="NO"> **[Norwegian Law MCP](https://github.com/ngu-tek/Norwegian-law-mcp)** | MCP server for Norwegian legislation providing 3,400 statutes, 33,521 provisions, and 25,301 legislative preparatory works (forarbeider) from Lovdata with EEA/EU cross-references and zero LLM-generated content. | | Apache-2.0 | 2026-06-22 |

## Legal Education & Communities

Newsletters, courses, conferences, and communities for legal technology learning and professional development.

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| **[Legal Quants](https://legalquants.com)** | Community of lawyer-builders designing, building, and implementing bleeding edge AI tools for lawyers. | | — | 2026-03-02 |
| <img src="https://flagcdn.com/w20/nl.png" width="20" height="15" alt="NL"> **[Maastricht Law & Tech Lab](https://www.maastrichtuniversity.nl/research/maastricht-law-and-tech-lab)** | Academic research center focused on legal NLP and technology with publicly available datasets and resources. | | — | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Stanford Legal AI Lab](https://hazyresearch.stanford.edu/)** | Research lab producing legal benchmarks, datasets, and models for advancing legal AI research. | | — | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Harvard Law School Library Innovation Lab](https://law.harvard.edu/library/innovation/)** | Develops tools and resources for legal research innovation and open legal data access. | | — | 2026-03-02 |

## Advanced Legal Tools & Citation Systems

Specialized tools for citation analysis, contract comparison, and legal research infrastructure.

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[eyecite](https://github.com/freelawproject/eyecite)** | Open-source Python library extracting legal citations from court documents and automatically linking them to free legal databases. | Python | BSD-2-Clause | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[eyecite-ts](https://github.com/medelman17/eyecite-ts)** | TypeScript port of eyecite for client-side citation extraction and annotation with 7KB gzipped footprint. | TypeScript | No license | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[CiteURL](https://github.com/raindrum/citeurl)** | Parses legal citations and generates hyperlinks to free online legal sources supporting 130+ sources of U.S. law. | Python | MIT | 2026-03-02 |
| **[vibecode-law](https://github.com/vibecode-law/vibecode-law)** | Open-source platform showcasing AI-built legal tech projects, built with Laravel 12, React 19, and TypeScript. | PHP, Laravel, TypeScript, React | MIT | 2026-03-02 |
| **[Redlines](https://github.com/houfu/redlines)** | Python library producing Track Changes-style text comparison output in multiple formats, featured in DeepLearning.AI with 170K+ monthly downloads. | Python | MIT | 2026-03-02 |
| **[RedlineNow](https://github.com/jamietso/RedlineNow)** | AI-powered document comparison tool providing side-by-side text editing with visual redline highlighting and AI-generated change summaries. | Python | MIT | 2026-03-03 |
| **[Tabular_Review](https://github.com/jamietso/Tabular_Review)** | AI-powered document analysis tool transforming unstructured PDFs and Word documents into searchable, structured datasets for bulk contract reviews. | Python | MIT | 2026-03-03 |
| **[Contract Playbook AI](https://github.com/yuch85/contract-playbook-ai)** | Generates contract review playbooks in minutes by extracting negotiation rules from reference contracts with rich-text editing and Track Changes compatibility. | TypeScript | Other | 2026-03-03 |
| **[ChartAI](https://github.com/jamietso/ChartAI)** | Automatically extracts and visualizes corporate structures from legal documents using computer vision and React Flow interactive diagrams. | Python, TypeScript, React | MIT | 2026-03-03 |
| <img src="https://flagcdn.com/w20/sg.png" width="20" height="15" alt="SG"> **[sgcite](https://github.com/yuch85/sgcite)** | Command-line tool verifying Singapore case law citations and detecting hallucinated authorities by cross-referencing the official eLitigation database. | Python | MIT | 2026-03-03 |
| **[prompt-engineering-lawyers](https://github.com/houfu/prompt-engineering-lawyers)** | Open-source Streamlit course teaching prompt engineering techniques for legal professionals with ChatGPT, Claude, and other LLMs. | Python | Other | 2026-03-03 |
| **[Adeu](https://github.com/dealfluence/adeu)** | Agentic DOCX redlining engine that enables AI agents and LLMs to inject native Track Changes and comments into Word documents without corrupting formatting, with a Model Context Protocol server and Python SDK. | Python | MIT | 2026-03-25 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[CiteBench](https://github.com/LawEngine/cite-bench)** | Blind benchmark for legal citation verification using four-label classification over Illinois and federal primary law, designed to evaluate AI systems for citation accuracy and hallucination detection. | Python | Apache-2.0 | 2026-06-11 |
| **[Circuitus](https://github.com/zgbrenner/circuitus)** | Browser-based legal research environment with a document reader, annotation system, and practice library using legal-grade typography, running entirely client-side with no server dependency. | | GPL-3.0 | 2026-06-15 |

## Notable Proprietary Legal AI Tools

> ⚠️ **Not FOSS, not endorsed.** The tools below are proprietary (closed-source) — some paid, some free-to-use — and are **not** open source. They are listed not as endorsements but because they are interesting or notable examples of legal AI that are not widely publicized. This section is curated **manually** and is **excluded from automated updates**.

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Prest0](https://prest0.ai)** | Enterprise legal AI platform that deploys a dedicated bilingual (English/Spanish) AI agent per law firm on an isolated VM, with persistent memory, Twilio voice + SMS intake, deep legal research, and legal-grade document drafting. Vertical-specialized for immigration (I-589 asylum, U-visa), California workers' comp (WCAB Pre-Hearing Statements under Rule 10563), and plaintiff-side employment law. Patent-pending Context-Based Semantic TreeSearch memory architecture. | TypeScript, Python, Node.js | Not FOSS | 2026-04-22 |
| **[PDF Mavericks](https://www.pdfmavericks.com)** | Browser-local PDF toolkit covering compress, merge, split, sign, watermark, and redact for contracts and case files. Files never leave the device — processing runs in JavaScript via PDF.js. No upload, no account, no tracking. | TypeScript, Next.js, PDF.js | Not FOSS | 2026-05-09 |
| **[Legitt AI Contract Review](https://legittai.com/contract-review)** | Provides instant contract summaries, clause-by-clause risk analysis, and obligation tracking for PDFs and Word documents. | | Not FOSS | 2026-03-02 |
| **[Lawvable](https://lawvable.com)** | Curated legal AI skills platform. | | Not FOSS | 2026-03-02 |
| **[AI Lawyer](https://ailawyer.pro/)** | Free AI legal assistant offering contract drafting, legal research, agreement comparison, translation, and summarization features. | | Not FOSS | 2026-03-02 |
| **[LexiAI](https://lexiai.org/)** | Free multilingual AI legal chatbot available 24/7 that provides legal information in your chosen language using GPT technology. | | Not FOSS | 2026-03-02 |
| **[FreeLawChat.ai](https://freelawchat.ai/)** | Free AI chatbot that answers legal questions across multiple jurisdictions with geographic-specific guidance on family law, employment, contracts, and other areas. | | Not FOSS | 2026-03-02 |
| **[CompareX Free Contract Analyser](https://compare-x.ai/free-contract-analyser)** | Analyzes contracts in 60 seconds, identifying missing clauses, high-risk terms, and compliance gaps with plain-English explanations, completely free with no credit card required. | | Not FOSS | 2026-03-02 |
| **[LogicBalls Legal Document Generator](https://logicballs.com/tools/legal-document-drafting-generator)** | Free AI tool that generates NDAs, contracts, agreements, and legal memos in minutes without signup. | | Not FOSS | 2026-03-02 |
| **[Galaxy.ai Legal Letter Generator](https://galaxy.ai/ai-legal-letter-generator)** | Free legal letter generator requiring no login that creates various types of legal correspondence using AI entirely in your browser. | | Not FOSS | 2026-03-02 |

## Meta-Resources

Other awesome lists and curated collections in the legal technology space.

| Name | Description | Tech Stack | License | Date Added |
|------|-------------|------------|---------|------------|
| ***[awesome-legal](https://github.com/ankane/awesome-legal)*** | *Curated collection of free legal documents, templates, and resources for companies and legal professionals. ⚠️ Stale (2024-03)* | | CC0-1.0 | *2026-03-02* |
| **[awesome-legal-nlp](https://github.com/maastrichtlawtech/awesome-legal-nlp)** | Comprehensive curated list of natural language processing resources, research papers, and datasets specifically for the legal domain, maintained by Maastricht Law & Tech Lab. | | MIT | 2026-03-02 |
| **[awesome-legal-data](https://github.com/openlegaldata/awesome-legal-data)** | Collection of datasets, corpora, benchmarks, and tools for legal text processing and NLP research across multiple jurisdictions and languages. | | No license | 2026-03-02 |
| **[awesome-legal-skills](https://github.com/lawvable/awesome-legal-skills)** | Curated list of AI agent skills and automation tools designed to streamline and assist with legal workflows and document analysis. | | Other | 2026-03-02 |
| ***[Awesome-LegalAI-Resources](https://github.com/CSHaitao/Awesome-LegalAI-Resources)*** | *Comprehensive collection of datasets, models, research papers, and tools focused on AI and machine learning applications in the legal domain. ⚠️ Stale (2023-07)* | | MIT | *2026-03-02* |
| ***[awesome-lawtech](https://github.com/officeanddragons/awesome-lawtech)*** | *Community-curated list of legal technology software, tools, and learning resources for legal professionals, designers, and developers. ⚠️ Stale (2019-10)* | | Other | *2026-03-02* |
| **[legaltechlist](https://github.com/digitallawyer/legaltechlist) ([web](https://legaltech.herokuapp.com/))** | Curated directory of legal technology tools and services organized by category for legal professionals and technologists. | | No license | 2026-03-02 |
| **[LawAgent](https://github.com/AI-Hub-Admin/LawAgent)** | Catalog of law-related AI agent tools and resources providing a common interface for developing legal AI workflows, with references to major commercial and open-source legal AI tools. | | No license | 2026-03-02 |
| **[Awesome-Legal (ishandutta2007)](https://github.com/ishandutta2007/Awesome-Legal)** | Curated list of SaaS products and open-source projects focused on AI agents for legal workflows. | | No license | 2026-03-25 |
| **[awesome-legaltech (Vaquill-AI)](https://github.com/Vaquill-AI/awesome-legaltech)** | Curated list of legaltech resources spanning open-source platforms, AI models, MCP servers, companies, datasets, and tools for the global legal ecosystem. | | No license | 2026-04-06 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[Awesome EU AI Act](https://github.com/GenAI-Gurus/awesome-eu-ai-act)** | Curated collection of tools, official sources, open-source projects, templates, and implementation guides for complying with the EU AI Act. | | CC0-1.0 | 2026-06-11 |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[Awesome Legal AI ZH](https://github.com/lilialla/awesome-legal-ai-zh)** | One-stop curated map of 238+ GitHub-verified open-source AI tools for Chinese lawyers and legal teams, organized by practice workflow with commercial-use annotations and weekly automated verification via the GitHub API. | | Other | 2026-06-29 |

## Contributing

Please read our [contributing guidelines](contributing.md) before making a contribution. All contributions are welcome, but we maintain strict quality standards for inclusion.

## Code of Conduct

This project and everyone participating in it are governed by our [Code of Conduct](code-of-conduct.md). By participating, you are expected to uphold this code.

## License

This project is licensed under the [CC0 1.0 Universal](license) (public domain).
