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

### GitHub Repositories

- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [Sara](https://github.com/tanko-r/AI-Associate) - A specialized Claude Code plugin that operates as a senior AI law associate capable of handling complex legal work.  Intended to work across multiple practice areas, but currently focused on US real estate transactions. Sara generates original legal documents and delegates research tasks to junior associate subagents, designed for solo practitioners and small law firms.
- [Ambrose](https://github.com/tanko-r/Ambrose) - An AI-powered contract review and redlining platform combining Claude Opus for risk analysis with Gemini Flash for revision generation. Built with Flask backend and Next.js frontend, engineered for in-house counsel and deal teams managing high volumes of contracts rapidly.
- [Lawvable](https://github.com/lawvable/awesome-legal-skills) - Curated AI skills for legal.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [LexNLP](https://github.com/LexPredict/lexpredict-lexnlp) - Open source Python library for natural language processing and information extraction from legal and regulatory texts. Extracts structured data like dates, monetary amounts, regulations, and citations with pre-trained models for document and clause classification.
- [LawBotics](https://github.com/hasnaintypes/lawbotics) - AI-powered legal contract analysis platform combining fine-tuned LLaMA models with modern web technologies to automate document review and clause extraction from PDFs and text. Identifies 41+ types of legal clauses and integrates with the CUAD dataset.
- <img src="https://flagcdn.com/w20/br.png" width="20" height="15" alt="BR"> <sub><i>[LegalNLP](https://github.com/felipemaiapolo/legalnlp) - Natural language processing methods and pre-trained models (BERT, Word2Vec, Doc2Vec, FastText) specifically designed for the Brazilian legal language, enabling legal document classification and semantic analysis. (Last updated: 2023-06)</i></sub>
- <img src="https://flagcdn.com/w20/in.png" width="20" height="15" alt="IN"> [MILDSum](https://github.com/Law-AI/mildsum) - Benchmark dataset and tools for multilingual legal document summarization, featuring 3,122 Indian court judgments with English and Hindi summaries drafted by legal practitioners, supporting legal NLP research.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [OLAW](https://github.com/harvard-lil/olaw) - Open Legal AI Workbench from Harvard Law School Library for building retrieval-augmented generation (RAG) applications in legal research. Provides customizable chatbot framework that integrates legal APIs and documents.
- <img src="https://flagcdn.com/w20/in.png" width="20" height="15" alt="IN"> [LawGlance](https://github.com/lawglance/lawglance) - Free, open-source RAG-based AI legal assistant for document analysis and legal question answering, enabling users to query their legal documents using natural language.
- [Legal ML Datasets](https://github.com/neelguha/legal-ml-datasets) - Curated collection of datasets and machine learning tasks for legal text processing, including contract understanding, clause classification, and legal document analysis benchmarks.
- <sub><i>[Awesome LegalAI Resources](https://github.com/CSHaitao/Awesome-LegalAI-Resources) - Comprehensive collection of legal AI datasets, tools, websites, and resources to facilitate development of intelligent legal technology systems. (Last updated: 2023-07)</i></sub>
- <i>[Legal Document Analysis using NLP](https://github.com/Team-NLP-Legal-Document/Legal_Document_Analysis_and_Classification_Using_NLP_and_Deep_Learning) - Deep learning pipeline for legal document classification and analysis using BERT embeddings and neural networks to automate document categorization and information extraction. (Last updated: 2023-12)</i>
- [LexReviewer](https://github.com/LexStack-AI/LexReviewer) - AI legal document review engine that ingests PDFs, uses RAG with hybrid retrieval, and provides grounded chat with citations and bounding-box references for verifiable answers from source text.
- [Ally Legal Assistant](https://github.com/Azure-Samples/ally-legal-assistant) - Microsoft Word plugin using Azure OpenAI for contract analysis, real-time Q&A, and auto-markup to help legal professionals save time during document reviews.

### Free Online Tools

- [Lawvable](https://lawvable.com) - Curated legal AI skills.
- [FreeLawChat.ai](https://freelawchat.ai/) - Free AI chatbot that answers legal questions across multiple jurisdictions with geographic-specific guidance. Users can ask unlimited questions on family law, employment, contracts, and other areas.
- [LexiAI](https://lexiai.org/) - Free multilingual AI legal chatbot available 24/7 that provides legal information in your chosen language using GPT technology.
- [CompareX Free Contract Analyser](https://compare-x.ai/free-contract-analyser) - Analyzes contracts in 60 seconds, identifying missing clauses, high-risk terms, and compliance gaps with plain-English explanations. Completely free with no credit card required.
- [Legitt AI Contract Review](https://legittai.com/contract-review) - Provides instant contract summaries, clause-by-clause risk analysis, and obligation tracking for PDFs and Word documents.
- [LogicBalls Legal Document Generator](https://logicballs.com/tools/legal-document-drafting-generator) - Free AI tool that generates NDAs, contracts, agreements, and legal memos in minutes without signup.
- [Galaxy.ai Legal Letter Generator](https://galaxy.ai/ai-legal-letter-generator) - Free legal letter generator requiring no login that creates various types of legal correspondence using AI entirely in your browser.
- [AI Lawyer](https://ailawyer.pro/) - Free AI legal assistant offering contract drafting, legal research, agreement comparison, translation, and summarization features.

## Law-Focused LLMs & Fine-Tuned Models

Foundation models and fine-tunes purpose-built for the legal domain, from general-purpose legal LLMs to specialized encoder models and retrieval systems.

### General-Purpose Legal LLMs

- <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> [LaWGPT](https://github.com/pengxiao-song/LaWGPT) - A series of open-source large language models based on Chinese-LLaMA, enhanced with expanded legal vocabulary and large-scale Chinese legal corpus pre-training plus instruction fine-tuning on judicial examination data.
- <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> [Lawyer-LLaMA](https://github.com/AndrewZhe/lawyer-llama) - A Chinese legal domain LLM built on LLaMA via continual pre-training on legal corpora and instruction fine-tuning with ChatGPT-generated legal Q&A, covering civil, criminal, and administrative law.
- <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> [Fuzi-Mingcha](https://github.com/irlab-sdu/fuzi.mingcha) - A Chinese judicial large language model jointly developed by Shandong University, Inspur Cloud, and China University of Political Science and Law, built on ChatGLM with capabilities for legal statute retrieval, case analysis, and judgment prediction.
- <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> [LexiLaw](https://github.com/CSHaitao/LexiLaw) - A fine-tuned Chinese legal language model based on ChatGLM-6B that provides legal consultation services using LoRA, P-tuning-v2, and full fine-tuning approaches trained on legal Q&A, statutes, and court documents.
- <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> [wisdomInterrogatory](https://github.com/zhihaiLLM/wisdomInterrogatory) - A legal-focused large language model developed by Zhejiang University and Alibaba DAMO Academy, built on Baichuan-7B with 40GB of legal domain data and six knowledge base types for intelligent legal consultation.
- <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> <sub><i>[HanFei](https://github.com/siat-nlp/HanFei) - A 7-billion-parameter fully fine-tuned Chinese legal large language model trained on approximately 60GB of legal domain data, supporting legal Q&A, multi-turn conversations, and article writing. (Last updated: 2023-10)</i></sub>
- <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> [InternLM-Law](https://github.com/InternLM/InternLM-Law) - An open-source Chinese legal LLM with 7B parameters and 32K-token context length that outperforms GPT-4 on the LawBench evaluation benchmark, presented at COLING 2025.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [Law_LLM](https://github.com/Tizzzzy/Law_LLM) - A multi-task legal LLM for the US legal system built on Gemma-7B, capable of similar case retrieval, precedent case recommendation, and legal judgment prediction.

### Legal BERT & Encoder Models

- <sub><i>[legalBERT](https://github.com/nonameemnlp2020/legalBERT) - The official code repository for the LEGAL-BERT paper, providing multiple pre-trained BERT variants optimized for different legal sub-domains including US contracts, ECHR cases, and EU legislation. (Last updated: 2020-06)</i></sub>
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> <sub><i>[CaseHOLD](https://github.com/reglab/casehold) - Stanford RegLab repository containing Legal-BERT and Custom Legal-BERT models pre-trained on 37GB of Harvard Law case corpus (3.4M+ legal decisions), plus the CaseHOLD benchmark of 53,000+ legal holdings. (Last updated: 2023-03)</i></sub>
- <img src="https://flagcdn.com/w20/in.png" width="20" height="15" alt="IN"> <sub><i>[InLegalBERT](https://github.com/Law-AI/pretraining-bert) - Code from IIT Kharagpur for pre-training BERT models on Indian legal text using dynamic MLM and NSP, producing InLegalBERT and InCaseLawBERT models trained on 5.4 million Indian legal documents spanning 1950-2019. (Last updated: 2023-06)</i></sub>

### Legal Embedding & Retrieval Models

- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> <sub><i>[fastlaw](https://github.com/jbesomi/fastlaw) - Law-specific word embeddings built with Apache Spark and FastText, trained on data from the Caselaw Access Project to replace generic word embeddings for supervised ML tasks on legal texts. (Last updated: 2019-06)</i></sub>
- [LRAGE](https://github.com/hoorangyee/LRAGE) - An open-source Legal Retrieval Augmented Generation Evaluation toolkit for assessing LLMs in RAG settings within the legal domain, with pre-compiled indexes and support for legal datasets.

## Legal Research

Platforms and tools for legal research, case law discovery, and statutory information.

### GitHub Repositories

- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [CourtListener](https://github.com/freelawproject/courtlistener) - Fully-searchable archive of US court opinions, orders, and judge data with coverage spanning decades of American case law. Used by legal professionals, researchers, and the general public for comprehensive case law research.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [Juriscraper](https://github.com/freelawproject/juriscraper) - Automated API for scraping American court websites to extract case metadata and opinions. Enables developers and legal research tools to collect court data programmatically from multiple jurisdictions.
- [LawLens](https://github.com/Ranjith00005/LawLens) - AI-powered legal research assistant that provides legal advisory, case outcome prediction, and automated report generation by analyzing PDF documents. Designed for law firms and individual practitioners.
- <img src="https://flagcdn.com/w20/gb.png" width="20" height="15" alt="UK"> [Lex](https://github.com/i-dot-ai/lex) - UK legal API providing access to legislation and case law specifically designed for AI agents and legal researchers. Built by the UK government's AI lab.
- [CC Legal Database](https://github.com/cc-archive/legaldb) - Curated repository of case law and legal scholarship from around the world housed in a Django-based platform.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [Law XML](https://github.com/DCCouncil/law-xml) - DC Law statutes and regulatory code published in structured XML format for programmatic access.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [Reporters DB](https://github.com/freelawproject/reporters-db) - Comprehensive database of court reporters with metadata and citation information for American courts.
- <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> [OpenArchiver](https://github.com/LogicLabs-OU/OpenArchiver) - Open-source platform for legally compliant email archiving and eDiscovery with GDPR-aware data retention.
- [AuthoritySpoke](https://github.com/mscarey/AuthoritySpoke) - Python library for modeling legal rules as structured data, enabling machine-readable representation and comparison of holdings from court opinions.

### Free Online Tools

- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [Google Scholar](https://scholar.google.com/scholar_courts) - Free case law search engine covering all 50 states and federal courts with opinions dating back to 1791, featuring customizable court selection and advanced search filters.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [CourtListener](https://www.courtlistener.com/) - Nonprofit-operated legal database with over 10 million case opinions from federal and state courts, plus 17.3 million PACER documents with advanced semantic search.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [Legal Information Institute (LII)](https://www.law.cornell.edu/) - Cornell Law School's nonprofit platform providing free access to U.S. Code, federal regulations, state statutes, court decisions, and legal encyclopedia.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [FindLaw](https://caselaw.findlaw.com/) - Comprehensive free resource for searching state and federal court opinions, statutes, regulations, and U.S. Code.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [GovInfo](https://www.govinfo.gov/help/cfr) - Official Government Publishing Office database offering authenticated federal regulations, Code of Federal Regulations, and federal register documents.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [Justia](https://law.justia.com/) - Free legal research platform featuring case law, statutes, regulations, and legal articles for federal and state resources.

## Contract Management

Tools for drafting, reviewing, negotiating, and managing legal contracts.

### GitHub Repositories

- [OCA Contract](https://github.com/OCA/contract) - Odoo module that manages contract creation, recurring invoicing, and lifecycle workflows with portal visibility.
- [Accord Project - Cicero](https://github.com/accordproject/cicero-template-library) - Open ecosystem for smart legal contracts providing a template library and execution engine. Allows drafting natural language templates bound to data models.
- [Contract Analyzer](https://github.com/ahmetkumass/contract-analyzer) - Open-source RAG-based system for extracting and analyzing key information from legal contracts using advanced language models.
- [OpenContracts](https://github.com/Open-Source-Legal/OpenContracts) - Enterprise-grade document analysis workspace combining LLM capabilities with annotation, collaboration, and structured data extraction.
- [DocuSeal](https://github.com/docusealco/docuseal) - Open-source DocuSign alternative for creating, filling, and signing digital documents with mobile-optimized forms and SDKs.
- [Contract Lifecycle Management Dashboard](https://github.com/cyberkunju/contract-management) - Frontend-based CLM platform built with React and TypeScript for designing reusable contract blueprints and managing workflows.
- <sub><i>[Contract Builder](https://github.com/blopa/Contract-Builder) - Free, open-source tool for easily building and maintaining any type of contract using spreadsheet-style interface. (Last updated: 2017-10)</i></sub>
- [Microsoft Agent for Contract Processing](https://github.com/microsoft/Agent-for-Contract-Processing-Solution-Accelerator) - Solution accelerator demonstrating AI agent deployment for streamlined NDA creation and management.

### Free Online Tools

- [CompareX Free Contract Analyser](https://compare-x.ai/free-contract-analyser) - Contract analyzer identifying missing clauses, high-risk terms, and compliance gaps in 60 seconds.
- [Legitt AI Contract Review](https://legittai.com/contract-review) - Instant contract summaries, clause-by-clause risk analysis, and obligation tracking for PDFs and Word documents.
- [LogicBalls Legal Document Generator](https://logicballs.com/tools/legal-document-drafting-generator) - Generates NDAs, contracts, agreements, and legal memos without signup.

## Practice Management

Software for law firms and legal departments to manage cases, clients, time, and billing.

### GitHub Repositories

- [Legal-Ease](https://github.com/sujal-pawar/Legal-Ease) - AI-driven legal case management platform enabling courts, law firms, and litigants to manage cases and schedule virtual hearings.
- [CaseAce](https://github.com/derekgan08/CaseAce-law-firm-management-system-backend) - Node.js and Express-based case management system for law firms offering CRM, document storage, task tracking, and appointment scheduling.
- [Kimai](https://github.com/kimai/kimai) - Leading open-source time-tracking application enabling lawyers to manage timesheets, generate invoices, and create reports with support for 30+ languages.
- [IDURAR ERP CRM](https://github.com/idurar/idurar-erp-crm) - Comprehensive open-source ERP and CRM system on MERN stack handling invoicing, quotes, payments, and accounting.
- [InvoiceShelf](https://github.com/InvoiceShelf/InvoiceShelf) - Laravel and Vue.js invoicing solution for tracking expenses, creating invoices and estimates, and managing recurring billing.
- [SolidInvoice](https://github.com/SolidInvoice/SolidInvoice) - PHP-based invoicing platform with client management, quote generation, and online payment processing.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> <sub><i>[Open Case Management (OCM)](https://github.com/aworley/ocm) - PHP-based case management system specifically designed for nonprofit legal services organizations. (Last updated: 2022-08)</i></sub>
- [Law Firm Management System](https://github.com/leon019i/Law_Firm_Management_system_Django) - Django-powered practice management platform with client management, case tracking, and mobile-friendly design.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [DAWSON - U.S. Tax Court ef-cms](https://github.com/ustaxcourt/ef-cms) - TypeScript-based electronic filing and case management system used by the U.S. Tax Court.
- <img src="https://flagcdn.com/w20/de.png" width="20" height="15" alt="DE"> [j-lawyer.org](https://github.com/jlawyerorg/j-lawyer-org) - Open-source Java-based legal case and document management system supporting case organization, document handling, invoicing, and fax integration for law offices on Windows, macOS, and Linux.

### Free Online Tools

- [OpenSign](https://www.opensignlabs.com/) - Free, unlimited, open-source e-signature tool.
- [SignWell](https://www.signwell.com) - Simple, free e-signature tool designed for small businesses and legal professionals.
- [Dropbox Sign](https://sign.dropbox.com) - Free document signing service integrating with Dropbox for contract management and legally enforceable document handling.
- [PandaDoc](https://www.pandadoc.com) - Document management and e-signature platform with free tier offering templates for contracts and legal agreements.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [Nolo](https://www.nolo.com) - Offers free legal information, document templates, and self-help resources for common legal issues and agreements.

## Document Management

Systems for storing, organizing, and retrieving legal documents securely.

### GitHub Repositories

- [Docassemble](https://github.com/jhpyle/docassemble) - Open-source expert system for guided interviews and document assembly built on Python, YAML, and Markdown. Automates legal form completion and helps self-represented litigants.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [docassemble-AssemblyLine](https://github.com/SuffolkLITLab/docassemble-AssemblyLine) - Rapid deployment framework by Suffolk Legal Innovation & Technology Lab that converts paper court forms into interactive web applications.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [docassemble-ALWeaver](https://github.com/SuffolkLITLab/docassemble-ALWeaver) - Code generation tool that automatically generates draft docassemble interviews from existing legal documents (PDF or DOCX).
- [DocuSeal](https://github.com/docusealco/docuseal) - Open-source alternative to DocuSign for creating, filling, and digitally signing documents.
- [OpenSign](https://github.com/OpenSignLabs/OpenSign) - Free and open-source DocuSign alternative providing e-signature capabilities for legal documents.
- [Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) - Document management system that scans, indexes, and archives physical documents with OCR and full-text search.
- [Papermerge](https://github.com/ciur/papermerge) - Open-source document management system optimized for digital archives and scanned documents with OCR capabilities.
- <sub><i>[Mayan EDMS](https://github.com/mayan-edms/Mayan-EDMS) - Free and open-source enterprise document management system supporting workflows, versioning, and audit trails. (Last updated: 2024-02)</i></sub>
- [PyMuPDF](https://github.com/pymupdf/PyMuPDF) - High-performance Python library for extracting, analyzing, and manipulating PDF document data for automated legal document processing.
- [Documenso](https://github.com/documenso/documenso) - Open-source DocuSign alternative built with Next.js and PostgreSQL, supporting self-hosting and PAdES-standard digital signatures for legally binding document workflows.

### Free Online Tools

- [PandaDoc](https://www.pandadoc.com) - Document management and e-signature platform with templates for legal agreements.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [LawDepot](https://www.lawdepot.com) - Provides free legal document templates and forms customizable for various needs.
- [JotForm](https://www.jotform.com) - Free form builder with legal document templates and signature collection capabilities.
- [Template.net](https://www.template.net) - Extensive library of free legal document templates including contracts, NDAs, and employment agreements.
- [GetDoc](https://www.getdoc.com) - Free document collaboration and e-signature platform with secure version control.
- [DocHub](https://www.dochub.com) - Free online document editor with e-signature capabilities for editing, signing, and managing documents directly in browser.

## Backend Utilities & Libraries

Programming libraries, SDKs, and utilities for building legal tech applications.

### Document Processing Libraries

- [python-docx](https://github.com/python-openxml/python-docx) - Python library for creating, reading, and modifying Microsoft Word documents programmatically with full support for paragraphs, tables, styles, and document structure.
- [pdfplumber](https://github.com/jsvine/pdfplumber) - Specialized PDF extraction tool providing detailed access to text, characters, rectangles, and lines for precise coordinate-based data extraction and table identification.
- [PyPDF](https://pypi.org/project/pypdf/) - Pure-Python library for splitting, merging, cropping, and transforming PDF pages while extracting text from electronically-generated documents.
- [python-docx-template](https://github.com/elapouya/python-docx-template) - Document generation library that injects Jinja2 templating into .docx files for dynamic content insertion and automated legal document assembly.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [x-ray](https://github.com/freelawproject/x-ray) - Python library from the Free Law Project that detects improperly redacted text in PDF documents by scanning for text hidden beneath rectangles or solid shapes.

### Legal NLP & Text Processing

- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [LexNLP](https://github.com/LexPredict/lexpredict-lexnlp) - Specialized Python library for natural language processing and information extraction from legal and regulatory texts with pre-trained models.
- [spaCy](https://spacy.io/) - Industrial-strength NLP library with pre-trained models for named entity recognition in contracts and legal documents.
- <img src="https://flagcdn.com/w20/gb.png" width="20" height="15" alt="UK"> [Blackstone](https://github.com/ICLRandD/Blackstone) - spaCy-based natural language processing model trained on English case law that detects legal entities and classifies sentences by legal purpose.
- [ContextGem](https://github.com/shcherbak-ai/contextgem) - Open-source Python LLM framework for extracting structured data and insights from documents with minimal code. Supports multi-level extraction workflows with paragraph-level source references, reasoning justifications, and multilingual support across multiple LLM providers.


### Document Services & Integration

- [Apache Tika](https://tika.apache.org/) - Enterprise-grade content detection and analysis framework that extracts metadata and text from 1000+ file types including PDFs and Office documents.
- [Office-Word-MCP-Server](https://github.com/GongRzhe/Office-Word-MCP-Server) - Model Context Protocol (MCP) server enabling AI assistants to create, read, and manipulate Word documents with rich formatting preservation.

### Smart Contract & Templating

- [Accord Project](https://accordproject.org/) - Open-source ecosystem for smart legal contracts with the Cicero templating system for creating structured, reusable contract templates.
- [Docassemble](https://docassemble.org/) - Full-stack expert system for guided legal interviews and document automation built in Python/YAML/Markdown with support for complex workflows.
- [Legalis](https://github.com/cool-japan/legalis) - Rust framework for parsing, analyzing, and simulating legal statutes, transforming natural language legal documents into structured, machine-verifiable code.

## Access to Justice

Tools and platforms designed to improve access to legal services and justice.

### GitHub Repositories

- [Docassemble](https://github.com/jhpyle/docassemble) - Expert system for guided interviews and document assembly that helps self-represented litigants generate court documents and legal forms.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [docassemble-AssemblyLine](https://github.com/SuffolkLITLab/docassemble-AssemblyLine) - Rapid deployment framework converting paper court forms into interactive web applications for legal aid organizations.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> <sub><i>[A2J Author](https://github.com/CCALI/a2j-author) - Open-source tool for creating guided interviews that help people complete legal forms and court documents. (Last updated: archived/removed)</i></sub>
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [Namesake](https://github.com/namesakefyi/namesake) - Web app guiding users through the legal name and gender marker change process in the United States, tracking requirements across jurisdictions.

### Free Online Tools

- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [Upsolve](https://www.upsolve.org) - Free online bankruptcy filing tool designed to help individuals file Chapter 7 bankruptcy without expensive attorney fees.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [LawDepot](https://www.lawdepot.com) - Provides free legal document templates and forms for self-represented litigants and small business owners.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [Nolo](https://www.nolo.com) - Offers free legal information, document templates, and self-help resources for common legal issues and agreements accessible to non-lawyers.

## Legal NLP & Datasets

Academic datasets, models, and tools for legal natural language processing research.

### GitHub Repositories

- [Legal ML Datasets](https://github.com/neelguha/legal-ml-datasets) - Curated collection of datasets and machine learning tasks for legal text processing, including contract understanding and clause classification.
- [Awesome Legal NLP](https://github.com/maastrichtlawtech/awesome-legal-nlp) - Curated collection aggregating 180+ legal NLP datasets, models, research papers, and implementation guidance.
- <img src="https://flagcdn.com/w20/gb.png" width="20" height="15" alt="UK"> [Blackstone](https://github.com/ICLRandD/Blackstone) - spaCy-based natural language processing model trained on English case law for detecting legal entities and clause classification.
- <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> [ChatLaw](https://github.com/PKU-YuanGroup/ChatLaw) - Large language model trained on Chinese legal documents and court data, achieving higher accuracy than GPT-4 on Chinese legal benchmarks.
- <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> [DISC-LawLLM](https://github.com/FudanDISC/DISC-LawLLM) - Intelligent legal system with LLM fine-tuned with 300K legal task examples, ranking highly on legal AI benchmarks.
- <img src="https://flagcdn.com/w20/cn.png" width="20" height="15" alt="CN"> <sub><i>[LawBench](https://github.com/open-compass/LawBench) - Comprehensive evaluation benchmark for assessing language models' legal knowledge across 20 tasks covering Chinese law. (Last updated: 2023-11)</i></sub>
- <img src="https://flagcdn.com/w20/in.png" width="20" height="15" alt="IN"> [MILDSum](https://github.com/Law-AI/mildsum) - Benchmark dataset and tools for multilingual legal document summarization with Indian court judgments.
- <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> [LexGLUE](https://github.com/coastalcph/lex-glue) - Benchmark combining seven legal NLP datasets for evaluating language models on tasks spanning European Court of Human Rights cases, US Supreme Court decisions, EU legislation, and contract analysis.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [LegalBench-RAG](https://github.com/zeroentropy-ai/legalbenchrag) - Information retrieval benchmark for evaluating RAG systems on complex legal contract questions, aggregating ground-truth snippets from ContractNLI, CUAD, MAUD, and PrivacyQA datasets.
- [Canadian Legal Data](https://github.com/a2aj-ca/canadian-legal-data) - Repository for accessing bulk Canadian legal data maintained by Access to Artificial Justice, providing structured datasets for legal text processing and research.

### Free Online Tools

- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [Descrybe Legal Research](https://descrybe.ai/) - Free case law research tool with no login required that searches U.S. federal and state court decisions using plain English queries with AI-generated summaries.

## Compliance & Regulatory Technology

Tools for regulatory compliance, sanctions screening, policy monitoring, and automated regulatory reporting.

### GitHub Repositories

- [OpenSanctions](https://github.com/opensanctions/opensanctions) - An open database of international sanctions data, persons of interest, and politically exposed persons (PEPs) for KYC/AML compliance screening.
- [Watchman](https://github.com/moov-io/watchman) - A high-performance AML/CTF/KYC sanctions screening tool written in Go that searches against OFAC and other global watchlists via an HTTP API.
- <sub><i>[Comply](https://github.com/strongdm/comply) - A compliance automation framework focused on SOC2 that generates auditor-friendly policy documents from Markdown and integrates with ticketing systems. (Last updated: 2022-07)</i></sub>
- [Comp](https://github.com/trycompai/comp) - An AI-native open-source compliance platform covering SOC 2, ISO 27001, HIPAA, and GDPR frameworks as an alternative to Vanta and Drata.
- [Marble](https://github.com/checkmarble/marble) - An open-source real-time decision engine for fraud detection and AML compliance, providing transaction monitoring, sanctions screening, and investigation case management.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [GovReady-Q](https://github.com/GovReady/govready-q) - An open-source GRC (Governance, Risk, and Compliance) platform that automates security assessments and compliance documentation for DevSecOps workflows.
- [FIRE Data Standard](https://github.com/SuadeLabs/fire) - The Financial Regulation Data Standard defining a common open specification for the transmission of granular data between regulatory systems in finance.
- [Compliance-to-Policy](https://github.com/oscal-compass/compliance-to-policy) - A framework bridging compliance-as-code (OSCAL) and policy-as-code engines like Kyverno for automated compliance verification.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [RegTech Data Validator](https://github.com/cfpb/regtech-data-validator) - Python-based tool by the Consumer Financial Protection Bureau for parsing and validating regulatory data submissions using Pandera schemas.
- [Legal Guard](https://github.com/nathangtg/legal-guard-regtech) - AI-powered regulatory analysis tool that transforms complex documents into plain English, assesses risks, and checks against regulations like GDPR and PDPA.

## eDiscovery & Litigation Support

Software for electronically stored information (ESI) collection, processing, review, and production.

### GitHub Repositories

- [FreeEed](https://github.com/shmsoft/FreeEed) - An open-source, AI-enabled eDiscovery platform that processes over 1,400 file types including PST, MS Office, and images with OCR for document review, search, and production.
- [Autopsy](https://github.com/sleuthkit/autopsy) - A widely-used digital forensics platform with a graphical interface to The Sleuth Kit, used by law enforcement, military, and corporate examiners to investigate computers and recover evidence for legal proceedings.
- [Mattermost Legal Hold](https://github.com/mattermost/mattermost-plugin-legal-hold) - A Mattermost plugin enabling administrators to place users on legal hold for a defined time period, with daily data collection and export capabilities for litigation compliance.
- <sub><i>[Open-Source-eDiscovery](https://github.com/dillonupgradeit/Open-Source-eDiscovery) - A Python-based eDiscovery application for creating and searching litigation productions from PDFs, emails, Office documents, images, and video files. (Last updated: 2020-11)</i></sub>
- [enigma](https://github.com/McFlip/enigma) - A Go-based eDiscovery tool for bulk decryption of emails in PST files and loose .eml files, designed for forensic and legal discovery workflows requiring legitimate certificate-based decryption.
- [ICIJ Extract](https://github.com/ICIJ/extract) - Cross-platform command-line tool for parallelized content extraction and analysis of documents, used by the International Consortium of Investigative Journalists for large-scale document investigations.

## Legal Analytics & Prediction

Platforms for litigation outcome prediction, judge analytics, legal data visualization, and data-driven legal insights.

### GitHub Repositories

- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> <sub><i>[scotus-predict-v2](https://github.com/mjbommar/scotus-predict-v2) - A random-forest-based model that predicts U.S. Supreme Court case outcomes and individual justice votes across nearly two centuries of decisions (1816-2014), achieving 70.2% case-level accuracy. (Last updated: 2017-04)</i></sub>
- <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> <sub><i>[legal-case-prediction](https://github.com/conorosully/legal-case-prediction) - An MSc project using NLP and machine learning including custom word embeddings to predict judicial decisions of the European Court of Human Rights. (Last updated: 2021-01)</i></sub>
- <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> <sub><i>[ECHR-OD_predictions](https://github.com/echr-od/ECHR-OD_predictions) - Implements a complete experimental framework for predicting European Court of Human Rights outcomes using binary, multiclass, and multilabel classification with multiple ML algorithms. (Last updated: 2022-12)</i></sub>
- <img src="https://flagcdn.com/w20/in.png" width="20" height="15" alt="IN"> [Realistic_LJP](https://github.com/ShubhamKumarNigam/Realistic_LJP) - Evaluates transformer models (InLegalBERT, BERT, XLNet) and LLMs for realistic legal judgment prediction on Indian court cases, presented at the NLLP Workshop at EMNLP 2024.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> <sub><i>[recidivism-predictions](https://github.com/stanford-policylab/recidivism-predictions) - Stanford Policy Lab replication code for the Science Advances paper comparing human vs. algorithmic accuracy in predicting criminal reoffending. (Last updated: 2020-05)</i></sub>
- [Legal-Text-Analytics](https://github.com/Liquid-Legal-Institute/Legal-Text-Analytics) - A comprehensive curated list of resources, methods, and tools for legal text analytics covering NER, case outcome prediction, argument mining, summarization, and datasets from multiple jurisdictions.
- <img src="https://flagcdn.com/w20/nl.png" width="20" height="15" alt="NL"> [Case Explorer](https://github.com/maastrichtlawtech/case-explorer-ui) - Network analysis platform for visualizing and exploring citation networks in Dutch and European court decisions, developed by Maastricht Law & Tech Lab.

## IP & Patent Technology

Tools for patent search, trademark monitoring, IP portfolio management, prior art analysis, and patent classification.

### GitHub Repositories

- [PatZilla](https://github.com/ip-tools/patzilla) - A modular patent information research platform and data integration toolkit with a modern UI and access to multiple data sources including the European Patent Office.
- <sub><i>[PatentInspector](https://github.com/KonstantinosPetrakis/PatentInspector) - An open-source patent analyzing web application built with Django and Vue 3, allowing users to search, filter, and export patent data. (Last updated: 2023-12)</i></sub>
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> <sub><i>[pypatent](https://github.com/daneads/pypatent) - A Python package for searching and scraping US Patent and Trademark Office patent data, outputting results as DataFrames or lists. (Last updated: 2020-06)</i></sub>
- [patents-public-data](https://github.com/google/patents-public-data) - Google's official collection of BigQuery datasets and Jupyter notebooks for conducting large-scale statistical analysis of patent data.
- [PatentSBERTa](https://github.com/AI-Growth-Lab/PatentSBERTa) - A deep NLP hybrid model combining Sentence-BERT and KNN for patent distance measurement and classification, trained on 1.5M+ patents.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> <sub><i>[hupd](https://github.com/suzgunmirac/hupd) - The Harvard USPTO Patent Dataset containing 4.5 million utility patent applications (2004-2018) with NLP models for patent acceptance prediction, classification, and summarization. (Last updated: 2023-12)</i></sub>
- [phpip](https://github.com/jjdejong/phpip) - A web-based patent and IP rights portfolio manager and docketing system built on Laravel/PHP with features for document merging, renewal management, and patent database integration.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [Patent MCP Server](https://github.com/riemannzeta/patent_mcp_server) - FastMCP server providing AI assistants with access to USPTO patent data through multiple APIs including Patent Public Search, Open Data Portal, PTAB, PatentsView, and Office Action APIs.

## Privacy & Data Protection

Specialized tools for privacy impact assessments, consent management, DSAR automation, and privacy policy generation.

### GitHub Repositories

- [Fides](https://github.com/ethyca/fides) - An open-source privacy engineering platform for managing data privacy requests (DSAR orchestration) and enforcing GDPR/CCPA/LGPD regulations in code with privacy-as-code workflows.
- <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> [Klaro](https://github.com/kiprotect/klaro) - An open-source, lightweight consent management platform that helps websites be transparent about third-party applications with GDPR/ePrivacy-compliant consent flows and support for 17+ languages.
- <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> [cookieconsent](https://github.com/orestbida/cookieconsent) - A lightweight, cross-browser, GDPR-compliant cookie consent plugin written in vanilla JavaScript with extensive customization options.
- [app-privacy-policy-generator](https://github.com/nisrulz/app-privacy-policy-generator) - A free, open-source web app that generates customized, GDPR-compliant privacy policies and terms of use documents for mobile applications.
- [CISO Assistant](https://github.com/intuitem/ciso-assistant-community) - A comprehensive open-source GRC platform supporting 100+ frameworks including GDPR, HIPAA, ISO 27001, and NIS2, with built-in risk assessment and compliance auditing.
- [ML Privacy Meter](https://github.com/privacytrustlab/ml_privacy_meter) - An open-source Python library for auditing data privacy in machine learning models through membership inference attacks, supporting GDPR-mandated data protection impact assessments.

## Legal Workflow Automation

Platforms and tools for automating legal processes, document lifecycles, and contract analytics.

### GitHub Repositories

- <sub><i>[ContraxSuite](https://github.com/LexPredict/lexpredict-contraxsuite) - An open-source contract analytics and legal document exploration platform using NLP and machine learning to extract clauses, entities, and structured data from unstructured legal text. (Last updated: 2023-02)</i></sub>
- [Wraft](https://github.com/wraft/wraft) - An open-source Document Lifecycle Management platform built with Elixir and React that helps businesses create, manage, approve, and sign documents from official letters to contracts.
- [CommonAccord](https://github.com/CommonAccord/Cmacc-Org) - An initiative to create global codes of legal transacting by codifying and automating legal documents as composable, interoperable objects.

## Court & Government Filing Systems

E-filing platforms, court management systems, government legal portals, and legal data standards.

### GitHub Repositories

- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [Open Case Filing System](https://github.com/federal-courts-software-factory/open-case-filing-system) - A public-domain platform by the Federal Courts Software Factory designed as a modern replacement for the federal CM/ECF system, built with Rust and PostgreSQL.
- <img src="https://flagcdn.com/w20/za.png" width="20" height="15" alt="ZA"> [Indigo](https://github.com/laws-africa/indigo) - A Django-based legislation publishing platform by Laws.Africa for managing, consolidating, and publishing legislation in the Akoma Ntoso XML standard, with export to HTML, PDF, and ePUB.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [Courts-DB](https://github.com/freelawproject/courts-db) - A comprehensive open-source database of current and historical courts maintained by Free Law Project, containing metadata from over 16 million data points.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> <sub><i>[LegalXML Court Filing 5.0](https://github.com/oasis-tcs/legalxml-courtfiling-5.0-spec) - The OASIS LegalXML Electronic Court Filing TC repository containing the ECF 5.0 specification, schemas, and examples for interoperable electronic court filing systems. (Last updated: 2019-05)</i></sub>
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [NIEM Model](https://github.com/niemopen/niem-model) - The National Information Exchange Model reference data model, an OASIS Open Project providing a common vocabulary with domain namespaces including Justice for government information exchange.
- <img src="https://flagcdn.com/w20/de.png" width="20" height="15" alt="DE"> [Open Legal Data Platform (OLDP)](https://github.com/openlegaldata/oldp) - A Django-based open data platform for processing and publishing legal documents with search and API access to court decisions and laws.

## Legal Ontologies & Knowledge Graphs

Structured legal knowledge representations, ontologies, and tools for building legal knowledge graphs and reasoning systems.

### GitHub Repositories

- [LKIF Core](https://github.com/RinkeHoekstra/lkif-core) - The LKIF Core legal ontology library consisting of 15 OWL modules covering fundamental legal and commonsense concepts across abstract, basic, and legal layers.
- <sub><i>[LegalRuleML](https://github.com/oasis-tcs/legalruleml) - The official OASIS LegalRuleML Technical Committee repository for developing examples and sharing knowledge about the correct application of the LegalRuleML standard for representing legal norms in markup. (Last updated: 2020-07)</i></sub>
- <sub><i>[LegalDocML Akoma Ntoso](https://github.com/oasis-open/legaldocml-akomantoso) - The official OASIS TC Open Repository containing schema files, examples, implementations, and libraries for the Akoma Ntoso legal document XML standard. (Last updated: 2022-06)</i></sub>
- <img src="https://flagcdn.com/w20/za.png" width="20" height="15" alt="ZA"> [Bluebell](https://github.com/laws-africa/bluebell) - A generic Akoma Ntoso 3 parser in Python supporting all hierarchical elements and multiple legal document types including acts, bills, debates, and judgments.
- [FOLIO](https://github.com/alea-institute/FOLIO) - The Federated Open Legal Information Ontology providing over 18,000 standardized legal concepts with unique identifiers and multilingual support for data interoperability in the legal industry.
- [Legal-Ontologies](https://github.com/Liquid-Legal-Institute/Legal-Ontologies) - A curated collection of resources, methods, and tools dedicated to legal ontologies, data schemes, and knowledge graphs maintained by the Liquid Legal Institute.
- <img src="https://flagcdn.com/w20/eu.png" width="20" height="15" alt="EU"> [DaPreCo KB](https://github.com/dapreco/daprecokb) - The largest freely available LegalRuleML knowledge base containing deontic rules formalized in Input/Output logic for GDPR and ISO 27018 compliance mapping.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> <sub><i>[SEC Knowledge Graph](https://github.com/AnjaneyaTripathi/knowledge_graph) - A knowledge graph construction tool for SEC litigation releases that classifies legal documents into crime categories and extracts violators, violations, actions, and fines. (Last updated: 2022-02)</i></sub>

## MCP Servers & AI Agent Tools for Law

Model Context Protocol servers, AI agent frameworks, and tooling specifically designed for legal AI workflows.

### GitHub Repositories

- [legal-mcp](https://github.com/agentic-ops/legal-mcp) - A comprehensive Model Context Protocol server for legal workflows designed to bridge AI assistants with legal databases, case management systems, and research tools.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [courtlistener-mcp](https://github.com/blakeox/courtlistener-mcp) - An MCP server bridging Claude and other LLMs with the CourtListener API, exposing legal research tools for accessing opinions, dockets, and court records with built-in observability.
- [mcp-cerebra-legal-server](https://github.com/yoda-digital/mcp-cerebra-legal-server) - An enterprise-grade MCP server for structured legal reasoning and analysis with automatic legal domain detection and citation formatting.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [us-legal-mcp](https://github.com/JamesANZ/us-legal-mcp) - An MCP server providing comprehensive US legislation access by searching Congress bills, Federal Register documents, court opinions, and committees from within AI coding environments.
- [LegalBench](https://github.com/HazyResearch/legalbench) - An open science benchmark of 162 collaboratively curated tasks from 40 contributors for evaluating legal reasoning capabilities in large language models.
- [Pasal](https://github.com/ilhamfp/pasal) - AI-native Indonesian legal platform combining an MCP server with a web app to give Claude grounded access to Indonesian laws and regulations.
- <img src="https://flagcdn.com/w20/de.png" width="20" height="15" alt="DE"> [Ayunis Legal MCP](https://github.com/ayunis-core/ayunis-legal-mcp) - MCP server for German legal codes with vector-based semantic search, comprising a store API, CLI tool, web scraper, and XML parser for comprehensive legal text analysis.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [Congress.gov MCP Server](https://github.com/bsmi021/mcp-congress_gov_server) - MCP server providing access to the official Congress.gov API for searching US bills, amendments, committee reports, and legislative data from within AI assistants.

## Legal Education & Communities

Newsletters, courses, conferences, and communities for legal technology learning and professional development.

- [Legal Quants](https://legalquants.com) - Community of lawyer-builders designing, building and implementing bleeding edge AI tools for lawyers. 
- <img src="https://flagcdn.com/w20/nl.png" width="20" height="15" alt="NL"> [Maastricht Law & Tech Lab](https://www.maastrichtuniversity.nl/research/maastricht-law-and-tech-lab) - Academic research center focused on legal NLP and technology with publicly available datasets and resources.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [Stanford Legal AI Lab](https://hazyresearch.stanford.edu/) - Research lab producing legal benchmarks, datasets, and models for advancing legal AI research.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [Harvard Law School Library Innovation Lab](https://law.harvard.edu/library/innovation/) - Develops tools and resources for legal research innovation and open legal data access.

## Advanced Legal Tools & Citation Systems

Specialized tools for citation analysis, contract comparison, and legal research infrastructure.

- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [eyecite](https://github.com/freelawproject/eyecite) - Open-source Python library extracting legal citations from court documents and automatically linking them to free legal databases.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [eyecite-ts](https://github.com/medelman17/eyecite-ts) - TypeScript port of eyecite for client-side citation extraction and annotation with 7KB gzipped footprint.
- <img src="https://flagcdn.com/w20/us.png" width="20" height="15" alt="US"> [CiteURL](https://github.com/raindrum/citeurl) - Parses legal citations and generates hyperlinks to free online legal sources supporting 130+ sources of U.S. law.
- [vibecode-law](https://github.com/vibecode-law/vibecode-law) - Open-source platform showcasing AI-built legal tech projects. Built with Laravel 12, React 19, TypeScript.
- [Redlines](https://github.com/houfu/redlines) - Python library producing Track Changes-style text comparison output in multiple formats; featured in DeepLearning.AI with 170K+ monthly downloads.
- [RedlineNow](https://github.com/jamietso/RedlineNow) - AI-powered document comparison tool providing side-by-side text editing with visual redline highlighting and AI-generated change summaries.
- [Tabular_Review](https://github.com/jamietso/Tabular_Review) - AI-powered document analysis tool transforming unstructured PDFs and Word documents into searchable, structured datasets for bulk contract reviews.
- [Contract Playbook AI](https://github.com/yuch85/contract-playbook-ai) - Generates contract review playbooks in minutes by extracting negotiation rules from reference contracts with rich-text editing and Track Changes compatibility.
- [ChartAI](https://github.com/jamietso/ChartAI) - Automatically extracts and visualizes corporate structures from legal documents using computer vision and React Flow interactive diagrams.
- <img src="https://flagcdn.com/w20/sg.png" width="20" height="15" alt="SG"> [sgcite](https://github.com/yuch85/sgcite) - Command-line tool verifying Singapore case law citations and detecting hallucinated authorities by cross-referencing official eLitigation database.
- [prompt-engineering-lawyers](https://github.com/houfu/prompt-engineering-lawyers) - Open-source Streamlit course teaching prompt engineering techniques for legal professionals with ChatGPT, Claude, and other LLMs.
- [Adeu](https://github.com/dealfluence/adeu) - Agentic DOCX redlining engine that enables AI agents and LLMs to inject native Track Changes and comments into Word documents without corrupting formatting, with a Model Context Protocol server and Python SDK.

## Meta-Resources

Other awesome lists and curated collections in the legal technology space.

- [awesome-legal](https://github.com/ankane/awesome-legal) - Curated collection of free legal documents, templates, and resources for companies and legal professionals.
- [awesome-legal-nlp](https://github.com/maastrichtlawtech/awesome-legal-nlp) - Comprehensive curated list of natural language processing resources, research papers, and datasets specifically for the legal domain, maintained by Maastricht Law & Tech Lab.
- [awesome-legal-data](https://github.com/openlegaldata/awesome-legal-data) - Collection of datasets, corpora, benchmarks, and tools for legal text processing and NLP research across multiple jurisdictions and languages.
- [awesome-legal-skills](https://github.com/lawvable/awesome-legal-skills) - Curated list of AI agent skills and automation tools designed to streamline and assist with legal workflows and document analysis.
- <sub><i>[Awesome-LegalAI-Resources](https://github.com/CSHaitao/Awesome-LegalAI-Resources) - Comprehensive collection of datasets, models, research papers, and tools focused on AI and machine learning applications in the legal domain. (Last updated: 2023-07)</i></sub>
- <sub><i>[awesome-lawtech](https://github.com/officeanddragons/awesome-lawtech) - Community-curated list of legal technology software, tools, and learning resources for legal professionals, designers, and developers. (Last updated: 2019-10)</i></sub>
- [legaltechlist](https://github.com/digitallawyer/legaltechlist) - Curated directory of legal technology tools and services organized by category for legal professionals and technologists.
- [LawAgent](https://github.com/AI-Hub-Admin/LawAgent) - Catalog of law-related AI agent tools and resources providing a common interface for developing legal AI workflows, with references to major commercial and open-source legal AI tools.

## Contributing

Please read our [contributing guidelines](contributing.md) before making a contribution. All contributions are welcome, but we maintain strict quality standards for inclusion.

## Code of Conduct

This project and everyone participating in it are governed by our [Code of Conduct](code-of-conduct.md). By participating, you are expected to uphold this code.

## License

This project is licensed under the [CC0 1.0 Universal](license) (public domain).
