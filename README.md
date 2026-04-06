# Awesome Legal Apps

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of awesome legal technology tools, apps, AI models, and resources for legal professionals and technologists where quality of curation beats quantity of links.

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

## Contents

- [AI Tools](#ai-tools)
- [Law-Focused LLMs & Fine-Tuned Models](#law-focused-llms--fine-tuned-models)
- [Legal Research](#legal-research)
- [Contract Management](#contract-management)
- [Practice Management](#practice-management)
- [Document Management](#document-management)
- [Backend Utilities & Libraries](#backend-utilities--libraries)
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
- [Meta-Resources](#meta-resources)

## AI Tools

Tools and models that use AI to assist with legal work, from contract analysis to legal research and document generation.

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Sara](https://github.com/tanko-r/AI-Associate)** | A specialized Claude Code plugin that operates as a senior AI law associate capable of handling complex legal work across multiple practice areas, currently focused on US real estate transactions, generating original legal documents and delegating research tasks to junior associate subagents. | Python | 2026-03-02 |
| **[Ambrose](https://github.com/tanko-r/Ambrose)** | An AI-powered contract review and redlining platform combining Claude Opus for risk analysis with Gemini Flash for revision generation, engineered for in-house counsel and deal teams managing high volumes of contracts. | Python, Flask, TypeScript, Next.js | 2026-03-02 |
| **[Lawvable](https://github.com/lawvable/awesome-legal-skills)** | Curated AI skills for legal workflows and document analysis. | | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[LexNLP](https://github.com/LexPredict/lexpredict-lexnlp)** | Open source Python library for natural language processing and information extraction from legal and regulatory texts, extracting structured data like dates, monetary amounts, regulations, and citations with pre-trained models. | Python | 2026-03-02 |
| **[LawBotics](https://github.com/hasnaintypes/lawbotics)** | AI-powered legal contract analysis platform combining fine-tuned LLaMA models with modern web technologies to automate document review and clause extraction, identifying 41+ types of legal clauses and integrating with the CUAD dataset. | Python, PyTorch | 2026-03-02 |
| *<img src="https://flagcdn.com/w20/br.png" width="20" height="15" alt="BR"> **[LegalNLP](https://github.com/felipemaiapolo/legalnlp)*** | *Natural language processing methods and pre-trained models (BERT, Word2Vec, Doc2Vec, FastText) specifically designed for the Brazilian legal language, enabling legal document classification and semantic analysis. ⚠️ Stale (2023-06)* | *Python, PyTorch* | *2026-03-02* |
| <img src="https://flagcdn.com/w20/in.png" width="20" height="15" alt="IN"> **[MILDSum](https://github.com/Law-AI/mildsum)** | Benchmark dataset and tools for multilingual legal document summarization, featuring 3,122 Indian court judgments with English and Hindi summaries drafted by legal practitioners. | Python | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[OLAW](https://github.com/harvard-lil/olaw)** | Open Legal AI Workbench from Harvard Law School Library for building retrieval-augmented generation (RAG) applications in legal research, providing a customizable chatbot framework that integrates legal APIs and documents. | Python | 2026-03-02 |
| <img src="https://flagcdn.com/w20/in.png" width="20" height="15" alt="IN"> **[LawGlance](https://github.com/lawglance/lawglance)** | Free, open-source RAG-based AI legal assistant for document analysis and legal question answering, enabling users to query their legal documents using natural language. | Python | 2026-03-02 |
| **[Legal ML Datasets](https://github.com/neelguha/legal-ml-datasets)** | Curated collection of datasets and machine learning tasks for legal text processing, including contract understanding, clause classification, and legal document analysis benchmarks. | | 2026-03-02 |
| ***[Awesome LegalAI Resources](https://github.com/CSHaitao/Awesome-LegalAI-Resources)*** | *Comprehensive collection of legal AI datasets, tools, websites, and resources to facilitate development of intelligent legal technology systems. ⚠️ Stale (2023-07)* | | *2026-03-02* |
| ***[Legal Document Analysis using NLP](https://github.com/Team-NLP-Legal-Document/Legal_Document_Analysis_and_Classification_Using_NLP_and_Deep_Learning)*** | *Deep learning pipeline for legal document classification and analysis using BERT embeddings and neural networks to automate document categorization and information extraction. ⚠️ Stale (2023-12)* | *Python, PyTorch* | *2026-03-02* |
| **[LexReviewer](https://github.com/LexStack-AI/LexReviewer)** | AI legal document review engine that ingests PDFs, uses RAG with hybrid retrieval, and provides grounded chat with citations and bounding-box references for verifiable answers from source text. | Python | 2026-03-03 |
| **[Ally Legal Assistant](https://github.com/Azure-Samples/ally-legal-assistant)** | Microsoft Word plugin using Azure OpenAI for contract analysis, real-time Q&A, and auto-markup to help legal professionals save time during document reviews. | TypeScript, Office.js | 2026-03-03 |
| **[Claude Cowork Legal Plugin](https://github.com/anthropics/knowledge-work-plugins)** | Open-source legal plugin for Claude Cowork automating contract review, NDA triage, and compliance workflows for in-house legal teams, part of Anthropic's knowledge-work plugin ecosystem. | Python | 2026-03-25 |
| **[Claude Legal Skill](https://github.com/evolsb/claude-legal-skill)** | AI-powered contract review skill with CUAD risk detection, market benchmarks, and lawyer-ready redlines, compatible with Claude Code, Codex, Cursor, and 26+ AI coding tools. | Python | 2026-03-25 |
| **[Contract Review Agent](https://github.com/kipeum86/contract-review-agent)** | Local-first AI contract review agent that turns legal templates and counterparty drafts into clause-level analysis and tracked-change DOCX redlines. | Python | 2026-03-25 |
| <img src="https://flagcdn.com/w20/in.png" width="20" height="15" alt="IN"> **[LegalOS](https://github.com/paidinesh7/LegalOS)** | AI-powered legal document analyzer designed for Indian startup founders to review and understand legal agreements. | Python | 2026-03-25 |
| <img src="https://flagcdn.com/w20/br.png" width="20" height="15" alt="BR"> **[Lex Intelligentia Skills](https://github.com/fbmoulin/lex-intelligentia-skills)** | Agent skills ecosystem with 17 specialized skills for Brazilian law professionals including magistrates, lawyers, and legal researchers. | Python | 2026-03-25 |
| **[AI Legal Claude](https://github.com/zubair-trabzada/ai-legal-claude)** | Claude Code skill suite providing 14 specialized legal AI skills including contract review, risk analysis, NDA generation, compliance auditing, and negotiation strategy, orchestrated by 5 parallel agents. | Python | 2026-04-06 |
| **[BS Detector](https://github.com/JuanVazTor/lh-ai-fs)** | AI pipeline that audits legal briefs for false or misrepresented case citations, verifying whether cited authority says what the brief claims it says. | Python | 2026-04-06 |
| **[Hallucination Auditor](https://github.com/jamescockburn47/hallucinationauditor)** | Local tool for auditing AI hallucinations in legal authority citations, verifying whether cited cases exist and whether quoted passages accurately reflect the source, producing audit-grade reports. | Python | 2026-04-06 |
| **[Lawvable](https://lawvable.com)** | Curated legal AI skills platform. | | 2026-03-02 |
| **[FreeLawChat.ai](https://freelawchat.ai/)** | Free AI chatbot that answers legal questions across multiple jurisdictions with geographic-specific guidance on family law, employment, contracts, and other areas. | | 2026-03-02 |
| **[LexiAI](https://lexiai.org/)** | Free multilingual AI legal chatbot available 24/7 that provides legal information in your chosen language using GPT technology. | | 2026-03-02 |
| **[CompareX Free Contract Analyser](https://compare-x.ai/free-contract-analyser)** | Analyzes contracts in 60 seconds, identifying missing clauses, high-risk terms, and compliance gaps with plain-English explanations, completely free with no credit card required. | | 2026-03-02 |
| **[Legitt AI Contract Review](https://legittai.com/contract-review)** | Provides instant contract summaries, clause-by-clause risk analysis, and obligation tracking for PDFs and Word documents. | | 2026-03-02 |
| **[LogicBalls Legal Document Generator](https://logicballs.com/tools/legal-document-drafting-generator)** | Free AI tool that generates NDAs, contracts, agreements, and legal memos in minutes without signup. | | 2026-03-02 |
| **[Galaxy.ai Legal Letter Generator](https://galaxy.ai/ai-legal-letter-generator)** | Free legal letter generator requiring no login that creates various types of legal correspondence using AI entirely in your browser. | | 2026-03-02 |
| **[AI Lawyer](https://ailawyer.pro/)** | Free AI legal assistant offering contract drafting, legal research, agreement comparison, translation, and summarization features. | | 2026-03-02 |

## Law-Focused LLMs & Fine-Tuned Models

Foundation models and fine-tunes purpose-built for the legal domain, from general-purpose legal LLMs to specialized encoder models and retrieval systems.

### General-Purpose Legal LLMs

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[LaWGPT](https://github.com/pengxiao-song/LaWGPT)** | A series of open-source large language models based on Chinese-LLaMA, enhanced with expanded legal vocabulary and large-scale Chinese legal corpus pre-training plus instruction fine-tuning on judicial examination data. | Python, PyTorch | 2026-03-02 |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[Lawyer-LLaMA](https://github.com/AndrewZhe/lawyer-llama)** | A Chinese legal domain LLM built on LLaMA via continual pre-training on legal corpora and instruction fine-tuning with ChatGPT-generated legal Q&A, covering civil, criminal, and administrative law. | Python, PyTorch | 2026-03-02 |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[Fuzi-Mingcha](https://github.com/irlab-sdu/fuzi.mingcha)** | A Chinese judicial large language model jointly developed by Shandong University, Inspur Cloud, and China University of Political Science and Law, built on ChatGLM with capabilities for legal statute retrieval, case analysis, and judgment prediction. | Python, PyTorch | 2026-03-02 |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[LexiLaw](https://github.com/CSHaitao/LexiLaw)** | A fine-tuned Chinese legal language model based on ChatGLM-6B that provides legal consultation services using LoRA, P-tuning-v2, and full fine-tuning approaches trained on legal Q&A, statutes, and court documents. | Python, PyTorch | 2026-03-02 |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[wisdomInterrogatory](https://github.com/zhihaiLLM/wisdomInterrogatory)** | A legal-focused large language model developed by Zhejiang University and Alibaba DAMO Academy, built on Baichuan-7B with 40GB of legal domain data and six knowledge base types for intelligent legal consultation. | Python, PyTorch | 2026-03-02 |
| *<img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[HanFei](https://github.com/siat-nlp/HanFei)*** | *A 7-billion-parameter fully fine-tuned Chinese legal large language model trained on approximately 60GB of legal domain data, supporting legal Q&A, multi-turn conversations, and article writing. ⚠️ Stale (2023-10)* | *Python, PyTorch* | *2026-03-02* |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[InternLM-Law](https://github.com/InternLM/InternLM-Law)** | An open-source Chinese legal LLM with 7B parameters and 32K-token context length that outperforms GPT-4 on the LawBench evaluation benchmark, presented at COLING 2025. | Python, PyTorch | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Law_LLM](https://github.com/Tizzzzy/Law_LLM)** | A multi-task legal LLM for the US legal system built on Gemma-7B, capable of similar case retrieval, precedent case recommendation, and legal judgment prediction. | Python, PyTorch | 2026-03-02 |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[LegalOne](https://github.com/CSHaitao/LegalOne)** | A family of Chinese legal-domain foundation models (1.7B, 4B, 8B parameters) trained via a three-phase pipeline with agentic chain-of-thought distillation and curriculum reinforcement learning for reliable legal reasoning. | Python, PyTorch | 2026-03-25 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[PrinzBench](https://github.com/prinz-ai/prinzbench)** | A benchmark ranking frontier LLMs on their ability to conduct legal research, analysis, and locate obscure publicly available legal information across US law. | | 2026-03-25 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[LEXam](https://github.com/LEXam-Benchmark/LEXam)** | A comprehensive legal reasoning benchmark evaluating LLMs on 4,886 law exam questions from 340 exams spanning Swiss, EU, and international law, accepted at ICLR 2026. | | 2026-03-25 |
| **[Legal-LLM (LawMate Romania)](https://github.com/DorobantuDiana/Legal-LLM)** | Romanian legal domain LLM built by fine-tuning Saul-7B-Instruct-v1 on the Romanian Constitution and Education Law, with the resulting model published on Hugging Face. | Python, PyTorch | 2026-04-06 |

### Legal BERT & Encoder Models

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| ***[legalBERT](https://github.com/nonameemnlp2020/legalBERT)*** | *The official code repository for the LEGAL-BERT paper, providing multiple pre-trained BERT variants optimized for different legal sub-domains including US contracts, ECHR cases, and EU legislation. ⚠️ Stale (2020-06)* | *Python, PyTorch* | *2026-03-02* |
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[CaseHOLD](https://github.com/reglab/casehold)*** | *Stanford RegLab repository containing Legal-BERT and Custom Legal-BERT models pre-trained on 37GB of Harvard Law case corpus (3.4M+ legal decisions), plus the CaseHOLD benchmark of 53,000+ legal holdings. ⚠️ Stale (2023-03)* | *Python, PyTorch* | *2026-03-02* |
| *<img src="https://flagcdn.com/w20/in.png" width="20" height="15" alt="IN"> **[InLegalBERT](https://github.com/Law-AI/pretraining-bert)*** | *Code from IIT Kharagpur for pre-training BERT models on Indian legal text using dynamic MLM and NSP, producing InLegalBERT and InCaseLawBERT models trained on 5.4 million Indian legal documents spanning 1950-2019. ⚠️ Stale (2023-06)* | *Python, PyTorch* | *2026-03-02* |

### Legal Embedding & Retrieval Models

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[fastlaw](https://github.com/jbesomi/fastlaw)*** | *Law-specific word embeddings built with Apache Spark and FastText, trained on data from the Caselaw Access Project to replace generic word embeddings for supervised ML tasks on legal texts. ⚠️ Stale (2019-06)* | *Python* | *2026-03-02* |
| **[LRAGE](https://github.com/hoorangyee/LRAGE)** | An open-source Legal Retrieval Augmented Generation Evaluation toolkit for assessing LLMs in RAG settings within the legal domain, with pre-compiled indexes and support for legal datasets. | Python | 2026-03-03 |
| **[Inception](https://github.com/freelawproject/inception)** | FastAPI microservice from the Free Law Project generating legal-text embeddings via fine-tuned ModernBERT, optimized for court opinions with GPU acceleration and batch processing. | Python | 2026-03-25 |

## Legal Research

Platforms and tools for legal research, case law discovery, and statutory information.

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[CourtListener](https://github.com/freelawproject/courtlistener)** | Fully-searchable archive of US court opinions, orders, and judge data with coverage spanning decades of American case law, used by legal professionals, researchers, and the general public. | Python, Django | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Juriscraper](https://github.com/freelawproject/juriscraper)** | Automated API for scraping American court websites to extract case metadata and opinions, enabling developers and legal research tools to collect court data programmatically from multiple jurisdictions. | Python | 2026-03-02 |
| **[LawLens](https://github.com/Ranjith00005/LawLens)** | AI-powered legal research assistant that provides legal advisory, case outcome prediction, and automated report generation by analyzing PDF documents, designed for law firms and individual practitioners. | Python | 2026-03-02 |
| <img src="https://flagcdn.com/w20/gb.png" width="20" height="15" alt="UK"> **[Lex](https://github.com/i-dot-ai/lex)** | UK legal API providing access to legislation and case law specifically designed for AI agents and legal researchers, built by the UK government's AI lab. | Python | 2026-03-02 |
| **[CC Legal Database](https://github.com/cc-archive/legaldb)** | Curated repository of case law and legal scholarship from around the world housed in a Django-based platform. | Python, Django | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Law XML](https://github.com/DCCouncil/law-xml)** | DC Law statutes and regulatory code published in structured XML format for programmatic access. | | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Reporters DB](https://github.com/freelawproject/reporters-db)** | Comprehensive database of court reporters with metadata and citation information for American courts. | Python | 2026-03-02 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[OpenArchiver](https://github.com/LogicLabs-OU/OpenArchiver)** | Open-source platform for legally compliant email archiving and eDiscovery with GDPR-aware data retention. | | 2026-03-03 |
| **[AuthoritySpoke](https://github.com/mscarey/AuthoritySpoke)** | Python library for modeling legal rules as structured data, enabling machine-readable representation and comparison of holdings from court opinions. | Python | 2026-03-03 |
| **[Legal Sources](https://github.com/worldwidelaw/legal-sources)** | Open-source collection scripts for legal data from 50+ countries written autonomously by an AI agent, with community-contributed government data sources. | | 2026-03-25 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[US Code Tools](https://github.com/nickvido/us-code-tools)** | TypeScript ingestion engine and sync tooling for the US Code corpus, providing structured programmatic access to United States federal statutes. | TypeScript | 2026-04-06 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Google Scholar](https://scholar.google.com/scholar_courts)** | Free case law search engine covering all 50 states and federal courts with opinions dating back to 1791, featuring customizable court selection and advanced search filters. | | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[CourtListener](https://www.courtlistener.com/)** | Nonprofit-operated legal database with over 10 million case opinions from federal and state courts, plus 17.3 million PACER documents with advanced semantic search. | | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Legal Information Institute (LII)](https://www.law.cornell.edu/)** | Cornell Law School's nonprofit platform providing free access to U.S. Code, federal regulations, state statutes, court decisions, and legal encyclopedia. | | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[FindLaw](https://caselaw.findlaw.com/)** | Comprehensive free resource for searching state and federal court opinions, statutes, regulations, and U.S. Code. | | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[GovInfo](https://www.govinfo.gov/help/cfr)** | Official Government Publishing Office database offering authenticated federal regulations, Code of Federal Regulations, and federal register documents. | | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Justia](https://law.justia.com/)** | Free legal research platform featuring case law, statutes, regulations, and legal articles for federal and state resources. | | 2026-03-02 |

## Contract Management

Tools for drafting, reviewing, negotiating, and managing legal contracts.

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| **[OCA Contract](https://github.com/OCA/contract)** | Odoo module that manages contract creation, recurring invoicing, and lifecycle workflows with portal visibility. | Python | 2026-03-02 |
| **[Accord Project - Cicero](https://github.com/accordproject/cicero-template-library)** | Open ecosystem for smart legal contracts providing a template library and execution engine, allowing drafting of natural language templates bound to data models. | | 2026-03-02 |
| **[Contract Analyzer](https://github.com/ahmetkumass/contract-analyzer)** | Open-source RAG-based system for extracting and analyzing key information from legal contracts using advanced language models. | Python | 2026-03-02 |
| **[OpenContracts](https://github.com/Open-Source-Legal/OpenContracts)** | Enterprise-grade document analysis workspace combining LLM capabilities with annotation, collaboration, and structured data extraction. | Python | 2026-03-02 |
| **[DocuSeal](https://github.com/docusealco/docuseal)** | Open-source DocuSign alternative for creating, filling, and signing digital documents with mobile-optimized forms and SDKs. | | 2026-03-02 |
| **[Contract Lifecycle Management Dashboard](https://github.com/cyberkunju/contract-management)** | Frontend-based CLM platform built with React and TypeScript for designing reusable contract blueprints and managing workflows. | TypeScript, React | 2026-03-02 |
| ***[Contract Builder](https://github.com/blopa/Contract-Builder)*** | *Free, open-source tool for easily building and maintaining any type of contract using a spreadsheet-style interface. ⚠️ Stale (2017-10)* | | *2026-03-02* |
| **[Microsoft Agent for Contract Processing](https://github.com/microsoft/Agent-for-Contract-Processing-Solution-Accelerator)** | Solution accelerator demonstrating AI agent deployment for streamlined NDA creation and management. | Python | 2026-03-03 |
| **[Legal Redline Tools](https://github.com/evolsb/legal-redline-tools)** | Generates tracked-changes Word documents and redline PDFs from AI-powered contract reviews, producing the actual deliverables lawyers send. | Python | 2026-03-25 |
| **[Restated AI](https://github.com/Flosters/Restated-AI)** | AI tool for generating amended and restated versions of legal agreements, automating the redrafting of contract amendments. | TypeScript | 2026-04-06 |
| **[Indemnification Architect](https://github.com/Tucuxi-Inc/IndemnificationArchitect)** | Parametric drafting and analysis tool for indemnification clauses that uses visual sliders to adjust clause components and generates production-quality legal text from each configuration. | TypeScript | 2026-04-06 |
| **[CompareX Free Contract Analyser](https://compare-x.ai/free-contract-analyser)** | Contract analyzer identifying missing clauses, high-risk terms, and compliance gaps in 60 seconds. | | 2026-03-02 |
| **[Legitt AI Contract Review](https://legittai.com/contract-review)** | Instant contract summaries, clause-by-clause risk analysis, and obligation tracking for PDFs and Word documents. | | 2026-03-02 |
| **[LogicBalls Legal Document Generator](https://logicballs.com/tools/legal-document-drafting-generator)** | Generates NDAs, contracts, agreements, and legal memos without signup. | | 2026-03-02 |

## Practice Management

Software for law firms and legal departments to manage cases, clients, time, and billing.

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| **[Legal-Ease](https://github.com/sujal-pawar/Legal-Ease)** | AI-driven legal case management platform enabling courts, law firms, and litigants to manage cases and schedule virtual hearings. | | 2026-03-02 |
| **[CaseAce](https://github.com/derekgan08/CaseAce-law-firm-management-system-backend)** | Node.js and Express-based case management system for law firms offering CRM, document storage, task tracking, and appointment scheduling. | | 2026-03-02 |
| **[Kimai](https://github.com/kimai/kimai)** | Leading open-source time-tracking application enabling lawyers to manage timesheets, generate invoices, and create reports with support for 30+ languages. | | 2026-03-02 |
| **[IDURAR ERP CRM](https://github.com/idurar/idurar-erp-crm)** | Comprehensive open-source ERP and CRM system on MERN stack handling invoicing, quotes, payments, and accounting. | | 2026-03-02 |
| **[InvoiceShelf](https://github.com/InvoiceShelf/InvoiceShelf)** | Laravel and Vue.js invoicing solution for tracking expenses, creating invoices and estimates, and managing recurring billing. | PHP, Laravel | 2026-03-02 |
| **[SolidInvoice](https://github.com/SolidInvoice/SolidInvoice)** | PHP-based invoicing platform with client management, quote generation, and online payment processing. | PHP | 2026-03-02 |
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Open Case Management (OCM)](https://github.com/aworley/ocm)*** | *PHP-based case management system specifically designed for nonprofit legal services organizations. ⚠️ Stale (2022-08)* | *PHP* | *2026-03-02* |
| ***[Law Firm Management System](https://github.com/leon019i/Law_Firm_Management_system_Django)*** | *Django-powered practice management platform with client management, case tracking, and mobile-friendly design. ⚠️ Stale (2024-03)* | *Python, Django* | *2026-03-02* |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[DAWSON - U.S. Tax Court ef-cms](https://github.com/ustaxcourt/ef-cms)** | TypeScript-based electronic filing and case management system used by the U.S. Tax Court. | TypeScript | 2026-03-02 |
| <img src="https://flagcdn.com/w20/de.png" width="20" height="15" alt="DE"> **[j-lawyer.org](https://github.com/jlawyerorg/j-lawyer-org)** | Open-source Java-based legal case and document management system supporting case organization, document handling, invoicing, and fax integration for law offices on Windows, macOS, and Linux. | Java | 2026-03-02 |
| **[LPM Skills](https://github.com/legalopsconsulting/lpm-skills)** | AI skills encoding legal project management methodology for Claude, covering matter management, budgeting, task workflows, and deadline tracking. | Python | 2026-03-25 |
| **[TimeBrief](https://github.com/jamescockburn47/voice-time)** | Voice-powered time tracking app for lawyers with fully local AI, enabling hands-free timesheet entry without sending data to external servers. | Python | 2026-04-06 |
| **[CounselScope](https://github.com/Tucuxi-Inc/PublicCounselScope)** | AI-powered legal query optimization platform that transforms vague legal requests into precisely-scoped instructions by building on internal organizational legal knowledge. | Python | 2026-04-06 |
| **[OpenSign](https://www.opensignlabs.com/)** | Free, unlimited, open-source e-signature tool. | | 2026-03-02 |
| **[SignWell](https://www.signwell.com)** | Simple, free e-signature tool designed for small businesses and legal professionals. | | 2026-03-02 |
| **[Dropbox Sign](https://sign.dropbox.com)** | Free document signing service integrating with Dropbox for contract management and legally enforceable document handling. | | 2026-03-02 |
| **[PandaDoc](https://www.pandadoc.com)** | Document management and e-signature platform with free tier offering templates for contracts and legal agreements. | | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Nolo](https://www.nolo.com)** | Offers free legal information, document templates, and self-help resources for common legal issues and agreements. | | 2026-03-02 |

## Document Management

Systems for storing, organizing, and retrieving legal documents securely.

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| **[Docassemble](https://github.com/jhpyle/docassemble)** | Open-source expert system for guided interviews and document assembly built on Python, YAML, and Markdown, automating legal form completion and helping self-represented litigants. | Python, YAML | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[docassemble-AssemblyLine](https://github.com/SuffolkLITLab/docassemble-AssemblyLine)** | Rapid deployment framework by Suffolk Legal Innovation & Technology Lab that converts paper court forms into interactive web applications. | Python, YAML | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[docassemble-ALWeaver](https://github.com/SuffolkLITLab/docassemble-ALWeaver)** | Code generation tool that automatically generates draft docassemble interviews from existing legal documents in PDF or DOCX format. | Python, YAML | 2026-03-02 |
| **[DocuSeal](https://github.com/docusealco/docuseal)** | Open-source alternative to DocuSign for creating, filling, and digitally signing documents. | | 2026-03-02 |
| **[OpenSign](https://github.com/OpenSignLabs/OpenSign)** | Free and open-source DocuSign alternative providing e-signature capabilities for legal documents. | | 2026-03-02 |
| **[Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx)** | Document management system that scans, indexes, and archives physical documents with OCR and full-text search. | Python | 2026-03-02 |
| **[Papermerge](https://github.com/ciur/papermerge)** | Open-source document management system optimized for digital archives and scanned documents with OCR capabilities. | Python | 2026-03-02 |
| ***[Mayan EDMS](https://github.com/mayan-edms/Mayan-EDMS)*** | *Free and open-source enterprise document management system supporting workflows, versioning, and audit trails. ⚠️ Stale (2024-02)* | *Python* | *2026-03-02* |
| **[PyMuPDF](https://github.com/pymupdf/PyMuPDF)** | High-performance Python library for extracting, analyzing, and manipulating PDF document data for automated legal document processing. | Python | 2026-03-02 |
| **[Documenso](https://github.com/documenso/documenso)** | Open-source DocuSign alternative built with Next.js and PostgreSQL, supporting self-hosting and PAdES-standard digital signatures for legally binding document workflows. | TypeScript, Next.js | 2026-03-02 |
| **[Word AI Redliner](https://github.com/yuch85/word-ai-redliner)** | Microsoft Word add-in that applies AI edits as tracked-change redlines with prompt management, connecting to Ollama or other LLMs for structure-aware legal document editing. | TypeScript, Office.js | 2026-03-25 |
| **[SuperDoc Redlines](https://github.com/yuch85/superdoc-redlines)** | CLI tool for applying tracked changes and comments to DOCX files using SuperDoc headless mode, enabling automated document markup in legal workflows. | TypeScript | 2026-03-25 |
| **[SignaturePacketIDE](https://github.com/jamietso/SignaturePacketIDE)** | AI-powered legal signature page extractor and packet generator that automates creation of wet-ink signature packs for M&A and financing transactions. | Python | 2026-03-25 |
| **[open-agreements](https://github.com/open-agreements/open-agreements)** | CLI tool that fills 25 standard legal agreement templates (NDAs, cloud terms, SAFEs, employment agreements, NVCA financing documents) and produces signable DOCX files. | TypeScript | 2026-04-06 |
| **[CoQuill](https://github.com/houfu/coquill)** | Conversational document assembly tool for Claude that fills DOCX templates through natural-language interview, supporting Jinja2 conditionals and loops without a server or scripting language. | Python | 2026-04-06 |
| **[SuperDoc VS Code Extension](https://github.com/mattConnHarbour/superdoc-vscode-extension)** | VS Code extension for editing and viewing DOCX files via SuperDoc, with live reload for AI-modified documents and auto-save for side-by-side code and document workflows. | JavaScript | 2026-04-06 |
| **[PandaDoc](https://www.pandadoc.com)** | Document management and e-signature platform with templates for legal agreements. | | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[LawDepot](https://www.lawdepot.com)** | Provides free legal document templates and forms customizable for various needs. | | 2026-03-02 |
| **[JotForm](https://www.jotform.com)** | Free form builder with legal document templates and signature collection capabilities. | | 2026-03-02 |
| **[Template.net](https://www.template.net)** | Extensive library of free legal document templates including contracts, NDAs, and employment agreements. | | 2026-03-02 |
| **[GetDoc](https://www.getdoc.com)** | Free document collaboration and e-signature platform with secure version control. | | 2026-03-02 |
| **[DocHub](https://www.dochub.com)** | Free online document editor with e-signature capabilities for editing, signing, and managing documents directly in browser. | | 2026-03-02 |

## Backend Utilities & Libraries

Programming libraries, SDKs, and utilities for building legal tech applications.

### Document Processing Libraries

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| **[python-docx](https://github.com/python-openxml/python-docx)** | Python library for creating, reading, and modifying Microsoft Word documents programmatically with full support for paragraphs, tables, styles, and document structure. | Python | 2026-03-02 |
| **[pdfplumber](https://github.com/jsvine/pdfplumber)** | Specialized PDF extraction tool providing detailed access to text, characters, rectangles, and lines for precise coordinate-based data extraction and table identification. | Python | 2026-03-02 |
| **[PyPDF](https://pypi.org/project/pypdf/)** | Pure-Python library for splitting, merging, cropping, and transforming PDF pages while extracting text from electronically-generated documents. | Python | 2026-03-02 |
| **[python-docx-template](https://github.com/elapouya/python-docx-template)** | Document generation library that injects Jinja2 templating into .docx files for dynamic content insertion and automated legal document assembly. | Python | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[x-ray](https://github.com/freelawproject/x-ray)** | Python library from the Free Law Project that detects improperly redacted text in PDF documents by scanning for text hidden beneath rectangles or solid shapes. | Python | 2026-03-02 |
| **[EdgeParse](https://github.com/raphaelmansuy/edgeparse)** | High-accuracy Rust-based PDF converter that deterministically transforms digital PDFs into Markdown, JSON with bounding boxes, HTML, or plain text without requiring a JVM or GPU. | Rust | 2026-03-25 |
| **[Python-Redlines](https://github.com/JSv4/Python-Redlines)** | Python library for generating docx tracked-change redlines, enabling programmatic creation of legal document comparisons with native Word Track Changes formatting. | Python | 2026-03-25 |
| **[office-word-diff](https://github.com/yuch85/office-word-diff)** | Library for applying word-level text diffs to Microsoft Word via Office.js API, preserving formatting with cascading fallback strategies for AI text editing and grammar checking in Word add-ins. | TypeScript, Office.js | 2026-03-25 |
| **[Docxodus](https://github.com/JSv4/Docxodus)** | Office XML redline engine built on the OpenXML SDK that generates tracked-change DOCX comparisons, providing C# support for programmatic legal document redlining. | C# | 2026-04-06 |

### Legal NLP & Text Processing

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[LexNLP](https://github.com/LexPredict/lexpredict-lexnlp)** | Specialized Python library for natural language processing and information extraction from legal and regulatory texts with pre-trained models. | Python | 2026-03-02 |
| **[spaCy](https://spacy.io/)** | Industrial-strength NLP library with pre-trained models for named entity recognition in contracts and legal documents. | Python, spaCy | 2026-03-02 |
| <img src="https://flagcdn.com/w20/gb.png" width="20" height="15" alt="UK"> **[Blackstone](https://github.com/ICLRandD/Blackstone)** | spaCy-based natural language processing model trained on English case law that detects legal entities and classifies sentences by legal purpose. | Python, spaCy | 2026-03-02 |
| **[ContextGem](https://github.com/shcherbak-ai/contextgem)** | Open-source Python LLM framework for extracting structured data and insights from documents with minimal code, supporting multi-level extraction workflows with paragraph-level source references, reasoning justifications, and multilingual support across multiple LLM providers. | Python | 2026-03-03 |

### Document Services & Integration

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| **[Apache Tika](https://tika.apache.org/)** | Enterprise-grade content detection and analysis framework that extracts metadata and text from 1000+ file types including PDFs and Office documents. | Java | 2026-03-02 |
| **[Office-Word-MCP-Server](https://github.com/GongRzhe/Office-Word-MCP-Server)** | Model Context Protocol (MCP) server enabling AI assistants to create, read, and manipulate Word documents with rich formatting preservation. | TypeScript | 2026-03-02 |

### Smart Contract & Templating

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| **[Accord Project](https://accordproject.org/)** | Open-source ecosystem for smart legal contracts with the Cicero templating system for creating structured, reusable contract templates. | | 2026-03-02 |
| **[Docassemble](https://docassemble.org/)** | Full-stack expert system for guided legal interviews and document automation built in Python/YAML/Markdown with support for complex workflows. | Python, YAML | 2026-03-02 |
| **[Legalis](https://github.com/cool-japan/legalis)** | Rust framework for parsing, analyzing, and simulating legal statutes, transforming natural language legal documents into structured, machine-verifiable code. | Rust | 2026-03-03 |

## Access to Justice

Tools and platforms designed to improve access to legal services and justice.

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| **[Docassemble](https://github.com/jhpyle/docassemble)** | Expert system for guided interviews and document assembly that helps self-represented litigants generate court documents and legal forms. | Python, YAML | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[docassemble-AssemblyLine](https://github.com/SuffolkLITLab/docassemble-AssemblyLine)** | Rapid deployment framework converting paper court forms into interactive web applications for legal aid organizations. | Python, YAML | 2026-03-02 |
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[A2J Author](https://github.com/CCALI/a2j-author)*** | *Open-source tool for creating guided interviews that help people complete legal forms and court documents. ⚠️ Stale (archived/removed)* | | *2026-03-02* |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Namesake](https://github.com/namesakefyi/namesake)** | Web app guiding users through the legal name and gender marker change process in the United States, tracking requirements across jurisdictions. | TypeScript, React | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Upsolve](https://www.upsolve.org)** | Free online bankruptcy filing tool designed to help individuals file Chapter 7 bankruptcy without expensive attorney fees. | | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[LawDepot](https://www.lawdepot.com)** | Provides free legal document templates and forms for self-represented litigants and small business owners. | | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Nolo](https://www.nolo.com)** | Offers free legal information, document templates, and self-help resources for common legal issues and agreements accessible to non-lawyers. | | 2026-03-02 |

## Legal NLP & Datasets

Academic datasets, models, and tools for legal natural language processing research.

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| **[Legal ML Datasets](https://github.com/neelguha/legal-ml-datasets)** | Curated collection of datasets and machine learning tasks for legal text processing, including contract understanding and clause classification. | | 2026-03-02 |
| **[Awesome Legal NLP](https://github.com/maastrichtlawtech/awesome-legal-nlp)** | Curated collection aggregating 180+ legal NLP datasets, models, research papers, and implementation guidance. | | 2026-03-02 |
| <img src="https://flagcdn.com/w20/gb.png" width="20" height="15" alt="UK"> **[Blackstone](https://github.com/ICLRandD/Blackstone)** | spaCy-based natural language processing model trained on English case law for detecting legal entities and clause classification. | Python, spaCy | 2026-03-02 |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[ChatLaw](https://github.com/PKU-YuanGroup/ChatLaw)** | Large language model trained on Chinese legal documents and court data, achieving higher accuracy than GPT-4 on Chinese legal benchmarks. | Python, PyTorch | 2026-03-02 |
| <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[DISC-LawLLM](https://github.com/FudanDISC/DISC-LawLLM)** | Intelligent legal system with LLM fine-tuned with 300K legal task examples, ranking highly on legal AI benchmarks. | Python, PyTorch | 2026-03-02 |
| *<img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> **[LawBench](https://github.com/open-compass/LawBench)*** | *Comprehensive evaluation benchmark for assessing language models' legal knowledge across 20 tasks covering Chinese law. ⚠️ Stale (2023-11)* | | *2026-03-02* |
| <img src="https://flagcdn.com/w20/in.png" width="20" height="15" alt="IN"> **[MILDSum](https://github.com/Law-AI/mildsum)** | Benchmark dataset and tools for multilingual legal document summarization with Indian court judgments. | Python | 2026-03-02 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[LexGLUE](https://github.com/coastalcph/lex-glue)** | Benchmark combining seven legal NLP datasets for evaluating language models on tasks spanning European Court of Human Rights cases, US Supreme Court decisions, EU legislation, and contract analysis. | Python | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[LegalBench-RAG](https://github.com/zeroentropy-ai/legalbenchrag)** | Information retrieval benchmark for evaluating RAG systems on complex legal contract questions, aggregating ground-truth snippets from ContractNLI, CUAD, MAUD, and PrivacyQA datasets. | Python | 2026-03-02 |
| **[Canadian Legal Data](https://github.com/a2aj-ca/canadian-legal-data)** | Repository for accessing bulk Canadian legal data maintained by Access to Artificial Justice, providing structured datasets for legal text processing and research. | | 2026-03-03 |
| **[LLM-and-Law](https://github.com/Jeryi-Sun/LLM-and-Law)** | Actively maintained curated paper list summarizing large language models applied to legal tasks including judgment prediction, document analysis, and legal reasoning research. | | 2026-03-25 |

### Public Datasets

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[The Atticus Project — CUAD & ACORD](https://www.atticusprojectai.org/datasets)** | Two annotated contract datasets from the same non-profit: CUAD covers 500+ commercial contracts across 41 clause types; ACORD provides 126,000+ expert-rated query-clause pairs for complex clauses like indemnification and limitation of liability. | | 2026-03-19 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[LEDGAR](https://huggingface.co/datasets/coastalcph/ledgar)** | 80,000 contract provisions extracted from SEC filings, covering clause types including confidentiality, governing law, and indemnification, available on HuggingFace. | | 2026-03-19 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[ContractNLI](https://stanfordnlp.github.io/contract-nli/)** | 607 annotated NDAs from Stanford NLP for natural language inference on legal contracts, released under Creative Commons. | | 2026-03-19 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Stanford Material Contracts Corpus (MCC)](https://mcc.law.stanford.edu)** | 1M+ real agreements filed with the SEC between 2000–2023, fully searchable by contract type and party; the largest open contract dataset available. | | 2026-03-19 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[LexGLUE](https://huggingface.co/datasets/coastalcph/lex_glue)** | Bundle of multiple legal NLP datasets in one place on HuggingFace, including LEDGAR and UNFAIR-ToS (terms of service annotations), for benchmarking language models on legal tasks. | | 2026-03-19 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[SEC EDGAR](https://www.sec.gov/cgi-bin/browse-edgar)** | Primary public source of millions of contracts filed by U.S. public companies, with free access to the raw filings behind many of the datasets above. | | 2026-03-19 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[TREC Legal Track](https://trec-legal.umiacs.umd.edu/corpora/trec/legal10/)** | Document corpora and relevance judgments from the TREC Legal Track competitions, designed for evaluating e-discovery and legal information retrieval systems. | | 2026-03-19 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Caselaw Access Project](https://case.law/)** | Harvard Law School's digitized archive of all official U.S. court decisions published in books from the 1600s to 2020, covering 40+ million pages of legal text. | | 2026-03-19 |
| **[ICC Case Transcripts](https://www.icc-cpi.int/case-transcripts)** | Official transcripts of proceedings before the International Criminal Court, freely available for legal NLP research on international criminal law. | | 2026-03-19 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Descrybe Legal Research](https://descrybe.ai/)** | Free case law research tool with no login required that searches U.S. federal and state court decisions using plain English queries with AI-generated summaries. | | 2026-03-19 |

## Compliance & Regulatory Technology

Tools for regulatory compliance, sanctions screening, policy monitoring, and automated regulatory reporting.

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| **[OpenSanctions](https://github.com/opensanctions/opensanctions)** | An open database of international sanctions data, persons of interest, and politically exposed persons (PEPs) for KYC/AML compliance screening. | Python | 2026-03-02 |
| **[Watchman](https://github.com/moov-io/watchman)** | A high-performance AML/CTF/KYC sanctions screening tool written in Go that searches against OFAC and other global watchlists via an HTTP API. | Go | 2026-03-02 |
| ***[Comply](https://github.com/strongdm/comply)*** | *A compliance automation framework focused on SOC2 that generates auditor-friendly policy documents from Markdown and integrates with ticketing systems. ⚠️ Stale (2022-07)* | *Go* | *2026-03-02* |
| **[Comp](https://github.com/trycompai/comp)** | An AI-native open-source compliance platform covering SOC 2, ISO 27001, HIPAA, and GDPR frameworks as an alternative to Vanta and Drata. | TypeScript, Next.js | 2026-03-02 |
| **[Marble](https://github.com/checkmarble/marble)** | An open-source real-time decision engine for fraud detection and AML compliance, providing transaction monitoring, sanctions screening, and investigation case management. | Go | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[GovReady-Q](https://github.com/GovReady/govready-q)** | An open-source GRC (Governance, Risk, and Compliance) platform that automates security assessments and compliance documentation for DevSecOps workflows. | Python, Django | 2026-03-02 |
| **[FIRE Data Standard](https://github.com/SuadeLabs/fire)** | The Financial Regulation Data Standard defining a common open specification for the transmission of granular data between regulatory systems in finance. | | 2026-03-02 |
| **[Compliance-to-Policy](https://github.com/oscal-compass/compliance-to-policy)** | A framework bridging compliance-as-code (OSCAL) and policy-as-code engines like Kyverno for automated compliance verification. | | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[RegTech Data Validator](https://github.com/cfpb/regtech-data-validator)** | Python-based tool by the Consumer Financial Protection Bureau for parsing and validating regulatory data submissions using Pandera schemas. | Python | 2026-03-02 |
| **[Legal Guard](https://github.com/nathangtg/legal-guard-regtech)** | AI-powered regulatory analysis tool that transforms complex documents into plain English, assesses risks, and checks against regulations like GDPR and PDPA. | Python | 2026-03-03 |
| **[Probo](https://github.com/getprobo/probo)** | Open-source compliance platform for startups supporting SOC 2, GDPR, ISO 27001, HIPAA, ISO 27701, and ISO 42001 as a self-hosted alternative to Vanta and Drata. | TypeScript, Next.js | 2026-04-06 |
| **[Regis](https://github.com/Flosters/Regis)** | AI-powered corporate ownership mapping and Ultimate Beneficial Owner (UBO) analysis tool that generates interactive ownership charts from natural language prompts or uploaded images, with a unified entity directory and automated syncing. | TypeScript | 2026-04-06 |
| **[TaxStructuringTool LITE](https://github.com/tech-taitan/TaxStructuringTool_LITE)** | Lightweight entity charting tool for tax professionals that visualizes corporate structures and ownership chains for tax structuring analysis. | TypeScript | 2026-04-06 |
| **[EasyBoard](https://github.com/SaifAlYounan/EasyBoard)** | Open-source board portal for managing corporate board meetings, materials, and governance workflows. | TypeScript | 2026-04-06 |


## eDiscovery & Litigation Support

Software for electronically stored information (ESI) collection, processing, review, and production.

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| **[FreeEed](https://github.com/shmsoft/FreeEed)** | An open-source, AI-enabled eDiscovery platform that processes over 1,400 file types including PST, MS Office, and images with OCR for document review, search, and production. | Java | 2026-03-02 |
| **[Autopsy](https://github.com/sleuthkit/autopsy)** | A widely-used digital forensics platform with a graphical interface to The Sleuth Kit, used by law enforcement, military, and corporate examiners to investigate computers and recover evidence for legal proceedings. | Java | 2026-03-02 |
| **[Mattermost Legal Hold](https://github.com/mattermost/mattermost-plugin-legal-hold)** | A Mattermost plugin enabling administrators to place users on legal hold for a defined time period, with daily data collection and export capabilities for litigation compliance. | Go | 2026-03-02 |
| ***[Open-Source-eDiscovery](https://github.com/dillonupgradeit/Open-Source-eDiscovery)*** | *A Python-based eDiscovery application for creating and searching litigation productions from PDFs, emails, Office documents, images, and video files. ⚠️ Stale (2020-11)* | *Python* | *2026-03-02* |
| **[enigma](https://github.com/McFlip/enigma)** | A Go-based eDiscovery tool for bulk decryption of emails in PST files and loose .eml files, designed for forensic and legal discovery workflows requiring legitimate certificate-based decryption. | Go | 2026-03-02 |
| **[ICIJ Extract](https://github.com/ICIJ/extract)** | Cross-platform command-line tool for parallelized content extraction and analysis of documents, used by the International Consortium of Investigative Journalists for large-scale document investigations. | Java | 2026-03-02 |
| **[ReelDiscovery](https://github.com/ghanderson77-ops/ReelDiscovery)** | AI-powered e-discovery email dataset generator from QuikData that creates realistic corporate email threads with authentic headers, attachments, and storyline-driven content for training, testing, and demonstration of e-discovery systems. | C# | 2026-04-06 |

## Legal Analytics & Prediction

Platforms for litigation outcome prediction, judge analytics, legal data visualization, and data-driven legal insights.

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[scotus-predict-v2](https://github.com/mjbommar/scotus-predict-v2)*** | *A random-forest-based model that predicts U.S. Supreme Court case outcomes and individual justice votes across nearly two centuries of decisions (1816-2014), achieving 70.2% case-level accuracy. ⚠️ Stale (2017-04)* | *Python* | *2026-03-02* |
| *<img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[legal-case-prediction](https://github.com/conorosully/legal-case-prediction)*** | *An MSc project using NLP and machine learning including custom word embeddings to predict judicial decisions of the European Court of Human Rights. ⚠️ Stale (2021-01)* | *Python* | *2026-03-02* |
| *<img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[ECHR-OD_predictions](https://github.com/echr-od/ECHR-OD_predictions)*** | *Implements a complete experimental framework for predicting European Court of Human Rights outcomes using binary, multiclass, and multilabel classification with multiple ML algorithms. ⚠️ Stale (2022-12)* | *Python* | *2026-03-02* |
| <img src="https://flagcdn.com/w20/in.png" width="20" height="15" alt="IN"> **[Realistic_LJP](https://github.com/ShubhamKumarNigam/Realistic_LJP)** | Evaluates transformer models (InLegalBERT, BERT, XLNet) and LLMs for realistic legal judgment prediction on Indian court cases, presented at the NLLP Workshop at EMNLP 2024. | Python, PyTorch | 2026-03-02 |
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[recidivism-predictions](https://github.com/stanford-policylab/recidivism-predictions)*** | *Stanford Policy Lab replication code for the Science Advances paper comparing human vs. algorithmic accuracy in predicting criminal reoffending. ⚠️ Stale (2020-05)* | *Python* | *2026-03-02* |
| **[Legal-Text-Analytics](https://github.com/Liquid-Legal-Institute/Legal-Text-Analytics)** | A comprehensive curated list of resources, methods, and tools for legal text analytics covering NER, case outcome prediction, argument mining, summarization, and datasets from multiple jurisdictions. | | 2026-03-02 |
| <img src="https://flagcdn.com/w20/nl.png" width="20" height="15" alt="NL"> **[Case Explorer](https://github.com/maastrichtlawtech/case-explorer-ui)** | Network analysis platform for visualizing and exploring citation networks in Dutch and European court decisions, developed by Maastricht Law & Tech Lab. | TypeScript, React | 2026-03-02 |

## IP & Patent Technology

Tools for patent search, trademark monitoring, IP portfolio management, prior art analysis, and patent classification.

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| **[PatZilla](https://github.com/ip-tools/patzilla)** | A modular patent information research platform and data integration toolkit with a modern UI and access to multiple data sources including the European Patent Office. | Python | 2026-03-02 |
| ***[PatentInspector](https://github.com/KonstantinosPetrakis/PatentInspector)*** | *An open-source patent analyzing web application built with Django and Vue 3, allowing users to search, filter, and export patent data. ⚠️ Stale (2023-12)* | *Python, Django* | *2026-03-02* |
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[pypatent](https://github.com/daneads/pypatent)*** | *A Python package for searching and scraping US Patent and Trademark Office patent data, outputting results as DataFrames or lists. ⚠️ Stale (2020-06)* | *Python* | *2026-03-02* |
| **[patents-public-data](https://github.com/google/patents-public-data)** | Google's official collection of BigQuery datasets and Jupyter notebooks for conducting large-scale statistical analysis of patent data. | Python | 2026-03-02 |
| **[PatentSBERTa](https://github.com/AI-Growth-Lab/PatentSBERTa)** | A deep NLP hybrid model combining Sentence-BERT and KNN for patent distance measurement and classification, trained on 1.5M+ patents. | Python, PyTorch | 2026-03-02 |
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[hupd](https://github.com/suzgunmirac/hupd)*** | *The Harvard USPTO Patent Dataset containing 4.5 million utility patent applications (2004-2018) with NLP models for patent acceptance prediction, classification, and summarization. ⚠️ Stale (2023-12)* | *Python, PyTorch* | *2026-03-02* |
| **[phpip](https://github.com/jjdejong/phpip)** | A web-based patent and IP rights portfolio manager and docketing system built on Laravel/PHP with features for document merging, renewal management, and patent database integration. | PHP, Laravel | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Patent MCP Server](https://github.com/riemannzeta/patent_mcp_server)** | FastMCP server providing AI assistants with access to USPTO patent data through multiple APIs including Patent Public Search, Open Data Portal, PTAB, PatentsView, and Office Action APIs. | Python | 2026-03-03 |
| **[Patent Prompts](https://github.com/arcprime-ip/patent-prompts)** | Curated AI prompts for patent workflows including claim drafting, prior art analysis, and continuation strategy based on real USPTO practice, installable as agent skills. | | 2026-03-25 |

## Privacy & Data Protection

Specialized tools for privacy impact assessments, consent management, DSAR automation, and privacy policy generation.

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| **[Fides](https://github.com/ethyca/fides)** | An open-source privacy engineering platform for managing data privacy requests (DSAR orchestration) and enforcing GDPR/CCPA/LGPD regulations in code with privacy-as-code workflows. | Python | 2026-03-02 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[Klaro](https://github.com/kiprotect/klaro)** | An open-source, lightweight consent management platform that helps websites be transparent about third-party applications with GDPR/ePrivacy-compliant consent flows and support for 17+ languages. | TypeScript | 2026-03-02 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[cookieconsent](https://github.com/orestbida/cookieconsent)** | A lightweight, cross-browser, GDPR-compliant cookie consent plugin written in vanilla JavaScript with extensive customization options. | TypeScript | 2026-03-02 |
| **[app-privacy-policy-generator](https://github.com/nisrulz/app-privacy-policy-generator)** | A free, open-source web app that generates customized, GDPR-compliant privacy policies and terms of use documents for mobile applications. | | 2026-03-02 |
| **[CISO Assistant](https://github.com/intuitem/ciso-assistant-community)** | A comprehensive open-source GRC platform supporting 100+ frameworks including GDPR, HIPAA, ISO 27001, and NIS2, with built-in risk assessment and compliance auditing. | Python | 2026-03-02 |
| **[ML Privacy Meter](https://github.com/privacytrustlab/ml_privacy_meter)** | An open-source Python library for auditing data privacy in machine learning models through membership inference attacks, supporting GDPR-mandated data protection impact assessments. | Python | 2026-03-02 |
| **[Databunker](https://github.com/securitybunker/databunker)** | Self-hosted secure vault for storing and managing customer PII, PHI, PCI, and KYC records with built-in tokenization and encryption to support GDPR, HIPAA, and SOC 2 compliance. | Go | 2026-04-06 |

## Legal Workflow Automation

Platforms and tools for automating legal processes, document lifecycles, and contract analytics.

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| ***[ContraxSuite](https://github.com/LexPredict/lexpredict-contraxsuite)*** | *An open-source contract analytics and legal document exploration platform using NLP and machine learning to extract clauses, entities, and structured data from unstructured legal text. ⚠️ Stale (2023-02)* | *Python* | *2026-03-02* |
| **[Wraft](https://github.com/wraft/wraft)** | An open-source Document Lifecycle Management platform built with Elixir and React that helps businesses create, manage, approve, and sign documents from official letters to contracts. | | 2026-03-02 |
| **[CommonAccord](https://github.com/CommonAccord/Cmacc-Org)** | An initiative to create global codes of legal transacting by codifying and automating legal documents as composable, interoperable objects. | | 2026-03-02 |

## Court & Government Filing Systems

E-filing platforms, court management systems, government legal portals, and legal data standards.

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Open Case Filing System](https://github.com/federal-courts-software-factory/open-case-filing-system)** | A public-domain platform by the Federal Courts Software Factory designed as a modern replacement for the federal CM/ECF system, built with Rust and PostgreSQL. | Rust | 2026-03-02 |
| <img src="https://flagcdn.com/w20/za.png" width="20" height="15" alt="ZA"> **[Indigo](https://github.com/laws-africa/indigo)** | A Django-based legislation publishing platform by Laws.Africa for managing, consolidating, and publishing legislation in the Akoma Ntoso XML standard, with export to HTML, PDF, and ePUB. | Python, Django | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Courts-DB](https://github.com/freelawproject/courts-db)** | A comprehensive open-source database of current and historical courts maintained by Free Law Project, containing metadata from over 16 million data points. | Python | 2026-03-02 |
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[LegalXML Court Filing 5.0](https://github.com/oasis-tcs/legalxml-courtfiling-5.0-spec)*** | *The OASIS LegalXML Electronic Court Filing TC repository containing the ECF 5.0 specification, schemas, and examples for interoperable electronic court filing systems. ⚠️ Stale (2019-05)* | | *2026-03-02* |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[NIEM Model](https://github.com/niemopen/niem-model)** | The National Information Exchange Model reference data model, an OASIS Open Project providing a common vocabulary with domain namespaces including Justice for government information exchange. | | 2026-03-02 |
| <img src="https://flagcdn.com/w20/de.png" width="20" height="15" alt="DE"> **[Open Legal Data Platform (OLDP)](https://github.com/openlegaldata/oldp)** | A Django-based open data platform for processing and publishing legal documents with search and API access to court decisions and laws. | Python, Django | 2026-03-02 |
| <img src="https://flagcdn.com/w20/de.png" width="20" height="15" alt="DE"> **[RIS Caselaw](https://github.com/digitalservicebund/ris-backend-service)** | Backend service for the German federal caselaw platform that manages, stores, and provides API access to judicial decisions across German courts. | Java, TypeScript | 2026-04-06 |
| <img src="https://flagcdn.com/w20/gb.png" width="20" height="15" alt="UK"> **[Find Case Law — Data Enrichment Service](https://github.com/nationalarchives/ds-caselaw-data-enrichment-service)** | Service used by The National Archives to automatically annotate UK judicial decisions with references to cited cases and relevant legislation for the Find Case Law platform. | Python | 2026-04-06 |

## Legal Ontologies & Knowledge Graphs

Structured legal knowledge representations, ontologies, and tools for building legal knowledge graphs and reasoning systems.

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| **[LKIF Core](https://github.com/RinkeHoekstra/lkif-core)** | The LKIF Core legal ontology library consisting of 15 OWL modules covering fundamental legal and commonsense concepts across abstract, basic, and legal layers. | | 2026-03-02 |
| ***[LegalRuleML](https://github.com/oasis-tcs/legalruleml)*** | *The official OASIS LegalRuleML Technical Committee repository for developing examples and sharing knowledge about the correct application of the LegalRuleML standard for representing legal norms in markup. ⚠️ Stale (2020-07)* | | *2026-03-02* |
| ***[LegalDocML Akoma Ntoso](https://github.com/oasis-open/legaldocml-akomantoso)*** | *The official OASIS TC Open Repository containing schema files, examples, implementations, and libraries for the Akoma Ntoso legal document XML standard. ⚠️ Stale (2022-06)* | | *2026-03-02* |
| <img src="https://flagcdn.com/w20/za.png" width="20" height="15" alt="ZA"> **[Bluebell](https://github.com/laws-africa/bluebell)** | A generic Akoma Ntoso 3 parser in Python supporting all hierarchical elements and multiple legal document types including acts, bills, debates, and judgments. | Python | 2026-03-02 |
| **[FOLIO](https://github.com/alea-institute/FOLIO)** | The Federated Open Legal Information Ontology providing over 18,000 standardized legal concepts with unique identifiers and multilingual support for data interoperability in the legal industry. | | 2026-03-02 |
| ***[Legal-Ontologies](https://github.com/Liquid-Legal-Institute/Legal-Ontologies)*** | *A curated collection of resources, methods, and tools dedicated to legal ontologies, data schemes, and knowledge graphs maintained by the Liquid Legal Institute. ⚠️ Stale (2024-03)* | | *2026-03-02* |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[DaPreCo KB](https://github.com/dapreco/daprecokb)** | The largest freely available LegalRuleML knowledge base containing deontic rules formalized in Input/Output logic for GDPR and ISO 27018 compliance mapping. | | 2026-03-02 |
| *<img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[SEC Knowledge Graph](https://github.com/AnjaneyaTripathi/knowledge_graph)*** | *A knowledge graph construction tool for SEC litigation releases that classifies legal documents into crime categories and extracts violators, violations, actions, and fines. ⚠️ Stale (2022-02)* | *Python* | *2026-03-02* |

## MCP Servers & AI Agent Tools for Law

Model Context Protocol servers, AI agent frameworks, and tooling specifically designed for legal AI workflows.

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| **[legal-mcp](https://github.com/agentic-ops/legal-mcp)** | A comprehensive Model Context Protocol server for legal workflows designed to bridge AI assistants with legal databases, case management systems, and research tools. | Python | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[courtlistener-mcp](https://github.com/blakeox/courtlistener-mcp)** | An MCP server bridging Claude and other LLMs with the CourtListener API, exposing legal research tools for accessing opinions, dockets, and court records with built-in observability. | Python | 2026-03-02 |
| **[mcp-cerebra-legal-server](https://github.com/yoda-digital/mcp-cerebra-legal-server)** | An enterprise-grade MCP server for structured legal reasoning and analysis with automatic legal domain detection and citation formatting. | Python | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[us-legal-mcp](https://github.com/JamesANZ/us-legal-mcp)** | An MCP server providing comprehensive US legislation access by searching Congress bills, Federal Register documents, court opinions, and committees from within AI coding environments. | Python | 2026-03-02 |
| **[LegalBench](https://github.com/HazyResearch/legalbench)** | An open science benchmark of 162 collaboratively curated tasks from 40 contributors for evaluating legal reasoning capabilities in large language models. | Python | 2026-03-02 |
| **[Pasal](https://github.com/ilhamfp/pasal)** | AI-native Indonesian legal platform combining an MCP server with a web app to give Claude grounded access to Indonesian laws and regulations. | Python | 2026-03-03 |
| <img src="https://flagcdn.com/w20/de.png" width="20" height="15" alt="DE"> **[Ayunis Legal MCP](https://github.com/ayunis-core/ayunis-legal-mcp)** | MCP server for German legal codes with vector-based semantic search, comprising a store API, CLI tool, web scraper, and XML parser for comprehensive legal text analysis. | Python | 2026-03-03 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Congress.gov MCP Server](https://github.com/bsmi021/mcp-congress_gov_server)** | MCP server providing access to the official Congress.gov API for searching US bills, amendments, committee reports, and legislative data from within AI assistants. | Python | 2026-03-03 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[EU Compliance MCP](https://github.com/Ansvar-Systems/EU_compliance_MCP)** | EU-focused compliance MCP server making EU regulations searchable, cross-referenceable, and AI-readable, part of Ansvar's suite covering 10+ European jurisdictions. | Python | 2026-03-25 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[US Compliance MCP](https://github.com/Ansvar-Systems/US_Compliance_MCP)** | MCP server for US cybersecurity and privacy regulations including HIPAA, CCPA, GLBA, FERPA, and COPPA. | Python | 2026-03-25 |
| <img src="https://flagcdn.com/w20/de.png" width="20" height="15" alt="DE"> **[German Law MCP](https://github.com/Ansvar-Systems/German-law-mcp)** | MCP server for querying 6,870 German statutes from gesetze-im-internet.de directly from AI assistants. | Python | 2026-03-25 |
| <img src="https://flagcdn.com/w20/nl.png" width="20" height="15" alt="NL"> **[Dutch Law MCP](https://github.com/Ansvar-Systems/Dutch-law-mcp)** | MCP server for Dutch legislation covering 46 key statutes with 13,815 provisions and EU law cross-references, sourced from wetten.overheid.nl. | Python | 2026-03-25 |
| <img src="https://flagcdn.com/w20/es.png" width="20" height="15" alt="ES"> **[Spanish Law MCP](https://github.com/Ansvar-Systems/spanish-law-mcp)** | MCP server for Spanish law covering data protection (LOPDGDD), national security framework (ENS), cybercrime, e-commerce (LSSI), and NIS2 transposition. | Python | 2026-03-25 |
| <img src="https://flagcdn.com/w20/gb.png" width="20" height="15" alt="UK"> **[UK Case Law MCP](https://github.com/georgejeffers/uk-case-law-mcp-server)** | MCP server enabling LLMs to search, retrieve, and cite UK legal judgments via The National Archives API. | Python | 2026-03-25 |
| **[CanLII MCP](https://github.com/Alhwyn/canlii-mcp)** | MCP server for searching and retrieving Canadian legal information including court decisions, legislation, and citations via the CanLII API. | Python | 2026-03-25 |
| <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> **[EU AI Act MCP](https://github.com/SonnyLabs/EU_AI_ACT_MCP)** | MCP server helping AI agents comply with the EU AI Act with tools for risk classification, prohibited practice checks, transparency disclosures, and deepfake labeling. | Python | 2026-03-25 |
| **[DOCX Redline MCP](https://github.com/AnsonLai/docx-redline-mcp)** | MCP server for inspecting and editing .docx files with support for real Word tracked changes and comments, purpose-built for legal contract review pipelines. | Python | 2026-03-25 |
| **[Law7 MCP](https://github.com/mikhashev/law7)** | Open up-to-date legal database for AI assistants via MCP server and core engine. | Python | 2026-03-25 |
| **[Korean Law MCP](https://github.com/chrisryugj/korean-law-mcp)** | MCP server and CLI providing 89 tools for Korean law covering statutes, precedents, ordinances, and legal interpretations, installable via npm. | TypeScript | 2026-04-06 |
| **[Greek Law MCP](https://github.com/Ansvar-Systems/Greek-law-mcp)** | MCP server providing a comprehensive Greek legal database with 21,119 statutes and 7,793 provisions for cybersecurity compliance queries, part of the Ansvar multi-jurisdiction suite. | Python | 2026-04-06 |
| **[Danish Law MCP](https://github.com/Ansvar-Systems/Danish-law-mcp)** | MCP server providing access to 62,764 Danish laws sourced from Retsinformation for use in AI assistants and compliance workflows. | Python | 2026-04-06 |
| **[FOLIO MCP](https://github.com/alea-institute/folio-mcp)** | MCP server exposing the FOLIO legal ontology (18,000+ standardized legal concepts) to AI assistants for semantic legal classification and knowledge retrieval. | Python | 2026-04-06 |

## Legal Education & Communities

Newsletters, courses, conferences, and communities for legal technology learning and professional development.

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| **[Legal Quants](https://legalquants.com)** | Community of lawyer-builders designing, building, and implementing bleeding edge AI tools for lawyers. | | 2026-03-02 |
| <img src="https://flagcdn.com/w20/nl.png" width="20" height="15" alt="NL"> **[Maastricht Law & Tech Lab](https://www.maastrichtuniversity.nl/research/maastricht-law-and-tech-lab)** | Academic research center focused on legal NLP and technology with publicly available datasets and resources. | | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Stanford Legal AI Lab](https://hazyresearch.stanford.edu/)** | Research lab producing legal benchmarks, datasets, and models for advancing legal AI research. | | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[Harvard Law School Library Innovation Lab](https://law.harvard.edu/library/innovation/)** | Develops tools and resources for legal research innovation and open legal data access. | | 2026-03-02 |

## Advanced Legal Tools & Citation Systems

Specialized tools for citation analysis, contract comparison, and legal research infrastructure.

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[eyecite](https://github.com/freelawproject/eyecite)** | Open-source Python library extracting legal citations from court documents and automatically linking them to free legal databases. | Python | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[eyecite-ts](https://github.com/medelman17/eyecite-ts)** | TypeScript port of eyecite for client-side citation extraction and annotation with 7KB gzipped footprint. | TypeScript | 2026-03-02 |
| <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> **[CiteURL](https://github.com/raindrum/citeurl)** | Parses legal citations and generates hyperlinks to free online legal sources supporting 130+ sources of U.S. law. | Python | 2026-03-02 |
| **[vibecode-law](https://github.com/vibecode-law/vibecode-law)** | Open-source platform showcasing AI-built legal tech projects, built with Laravel 12, React 19, and TypeScript. | PHP, Laravel, TypeScript, React | 2026-03-02 |
| **[Redlines](https://github.com/houfu/redlines)** | Python library producing Track Changes-style text comparison output in multiple formats, featured in DeepLearning.AI with 170K+ monthly downloads. | Python | 2026-03-02 |
| **[RedlineNow](https://github.com/jamietso/RedlineNow)** | AI-powered document comparison tool providing side-by-side text editing with visual redline highlighting and AI-generated change summaries. | Python | 2026-03-03 |
| **[Tabular_Review](https://github.com/jamietso/Tabular_Review)** | AI-powered document analysis tool transforming unstructured PDFs and Word documents into searchable, structured datasets for bulk contract reviews. | Python | 2026-03-03 |
| **[Contract Playbook AI](https://github.com/yuch85/contract-playbook-ai)** | Generates contract review playbooks in minutes by extracting negotiation rules from reference contracts with rich-text editing and Track Changes compatibility. | TypeScript | 2026-03-03 |
| **[ChartAI](https://github.com/jamietso/ChartAI)** | Automatically extracts and visualizes corporate structures from legal documents using computer vision and React Flow interactive diagrams. | Python, TypeScript, React | 2026-03-03 |
| <img src="https://flagcdn.com/w20/sg.png" width="20" height="15" alt="SG"> **[sgcite](https://github.com/yuch85/sgcite)** | Command-line tool verifying Singapore case law citations and detecting hallucinated authorities by cross-referencing the official eLitigation database. | Python | 2026-03-03 |
| **[prompt-engineering-lawyers](https://github.com/houfu/prompt-engineering-lawyers)** | Open-source Streamlit course teaching prompt engineering techniques for legal professionals with ChatGPT, Claude, and other LLMs. | Python | 2026-03-03 |
| **[Adeu](https://github.com/dealfluence/adeu)** | Agentic DOCX redlining engine that enables AI agents and LLMs to inject native Track Changes and comments into Word documents without corrupting formatting, with a Model Context Protocol server and Python SDK. | Python | 2026-03-25 |

## Meta-Resources

Other awesome lists and curated collections in the legal technology space.

| Name | Description | Tech Stack | Date Added |
|------|-------------|------------|------------|
| ***[awesome-legal](https://github.com/ankane/awesome-legal)*** | *Curated collection of free legal documents, templates, and resources for companies and legal professionals. ⚠️ Stale (2024-03)* | | *2026-03-02* |
| **[awesome-legal-nlp](https://github.com/maastrichtlawtech/awesome-legal-nlp)** | Comprehensive curated list of natural language processing resources, research papers, and datasets specifically for the legal domain, maintained by Maastricht Law & Tech Lab. | | 2026-03-02 |
| **[awesome-legal-data](https://github.com/openlegaldata/awesome-legal-data)** | Collection of datasets, corpora, benchmarks, and tools for legal text processing and NLP research across multiple jurisdictions and languages. | | 2026-03-02 |
| **[awesome-legal-skills](https://github.com/lawvable/awesome-legal-skills)** | Curated list of AI agent skills and automation tools designed to streamline and assist with legal workflows and document analysis. | | 2026-03-02 |
| ***[Awesome-LegalAI-Resources](https://github.com/CSHaitao/Awesome-LegalAI-Resources)*** | *Comprehensive collection of datasets, models, research papers, and tools focused on AI and machine learning applications in the legal domain. ⚠️ Stale (2023-07)* | | *2026-03-02* |
| ***[awesome-lawtech](https://github.com/officeanddragons/awesome-lawtech)*** | *Community-curated list of legal technology software, tools, and learning resources for legal professionals, designers, and developers. ⚠️ Stale (2019-10)* | | *2026-03-02* |
| **[legaltechlist](https://github.com/digitallawyer/legaltechlist) ([web](https://legaltech.herokuapp.com/))** | Curated directory of legal technology tools and services organized by category for legal professionals and technologists. | | 2026-03-02 |
| **[LawAgent](https://github.com/AI-Hub-Admin/LawAgent)** | Catalog of law-related AI agent tools and resources providing a common interface for developing legal AI workflows, with references to major commercial and open-source legal AI tools. | | 2026-03-02 |
| **[Awesome-Legal (ishandutta2007)](https://github.com/ishandutta2007/Awesome-Legal)** | Curated list of SaaS products and open-source projects focused on AI agents for legal workflows. | | 2026-03-25 |
| **[awesome-legaltech (Vaquill-AI)](https://github.com/Vaquill-AI/awesome-legaltech)** | Curated list of legaltech resources spanning open-source platforms, AI models, MCP servers, companies, datasets, and tools for the global legal ecosystem. | | 2026-04-06 |

## Contributing

Please read our [contributing guidelines](contributing.md) before making a contribution. All contributions are welcome, but we maintain strict quality standards for inclusion.

## Code of Conduct

This project and everyone participating in it are governed by our [Code of Conduct](code-of-conduct.md). By participating, you are expected to uphold this code.

## License

This project is licensed under the [CC0 1.0 Universal](license) (public domain).
