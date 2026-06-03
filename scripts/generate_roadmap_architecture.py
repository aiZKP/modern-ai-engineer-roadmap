from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
STAGES_DIR = DOCS / "stages"


def P(num: str, name: str, summary: str, build: str, measure: str, subparts: list[str]) -> dict:
    return {
        "num": num,
        "name": name,
        "summary": summary,
        "build": build,
        "measure": measure,
        "subparts": subparts,
    }


STAGES = [
    {
        "num": 0,
        "name": "Orientation",
        "tagline": "Build the map before choosing tools.",
        "goal": "Understand modern AI engineering as a discipline: product judgment, model behavior, system design, evaluation, and responsible deployment.",
        "artifact": "A learning log, environment checklist, use-case decision memo, and first roadmap plan.",
        "metrics": ["weekly learning cadence", "one documented use-case decision", "tooling installed and tested", "first project skeleton"],
        "exit": ["explain AI engineering versus ML engineering", "describe prompting, RAG, agents, fine-tuning, and serving", "choose a narrow first project", "maintain a decision log"],
        "parts": [
            P("0.1", "AI Engineering Mental Model", "Build a mental model of AI products as systems around foundation models, not as isolated prompts.", "Draw an AI application stack for a simple assistant.", "Check owners, inputs, outputs, failure modes, and evaluation points.", ["AI Engineering vs ML Engineering", "Foundation Model Product Stack", "Models as Probabilistic Components", "Adaptation Patterns"]),
            P("0.2", "Tooling and Learning Environment", "Create a reliable local workspace so every later project can be reproduced, debugged, and shared.", "Create the roadmap workspace with notes, projects, environment files, and a decision journal.", "Run one script, one test, and one documented setup command from a clean shell.", ["Developer Environment", "Python and Notebook Setup", "Git Terminal and Shell Workflow", "Secrets and Configuration"]),
            P("0.3", "Use Case Judgment", "Choose AI projects that have clear users, data, success criteria, and acceptable risk.", "Write a use-case brief for the first AI application you want to build.", "Score user value, data availability, evaluation difficulty, latency, privacy, cost, and risk.", ["Use Case Selection", "Feasibility and Risk", "Product Metrics and User Value"]),
            P("0.4", "Learning Operating System", "Turn the roadmap into a repeatable loop of learning, building, measuring, and reflection.", "Create a 30-day plan with weekly artifacts.", "Review scope, hours, measurements, weak spots, and exit criteria.", ["Stage Project Loop", "Evaluation First Habit", "Decision Journal and Failure Log", "Roadmap Navigation"]),
            P("0.5", "First Portfolio Skeleton", "Start documenting work from day one so every stage leaves behind usable evidence.", "Create a public or private portfolio skeleton.", "Check that every project has a problem, approach, run instructions, measurements, and next steps.", ["Portfolio Repository Layout", "README Quality Bar", "Evidence Over Certificates"]),
        ],
    },
    {
        "num": 1,
        "name": "Foundations",
        "tagline": "Become fluent with code, data, math, and systems basics.",
        "goal": "Build the programming, data, math, and software habits needed to learn AI without fighting basic tooling.",
        "artifact": "A tested Python data application with a CLI or API, setup notes, and a short data report.",
        "metrics": ["tests pass from clean checkout", "data quality report", "runtime measured", "CLI or API path documented"],
        "exit": ["use Python environments, packages, tests, and type hints", "clean and inspect a real dataset", "explain vectors, probability, gradients, and splits", "debug HTTP, JSON, SQL, Git, and shell workflows"],
        "parts": [
            P("1.1", "Python Software Craft", "Write Python that can grow from notebooks into maintainable AI project code.", "Refactor a notebook-style script into a small package with tests and a CLI.", "Track test count, runtime, config options, and reproducibility.", ["Python Project Structure", "Functions Classes and Modules", "Testing with Pytest", "Logging and Error Handling", "Configuration and Reproducibility"]),
            P("1.2", "Math for AI Engineers", "Learn the practical math that explains representations, uncertainty, optimization, and metrics.", "Build notebooks for vector similarity, probability simulation, and gradient descent.", "Validate at least one calculation by hand and one by code.", ["Linear Algebra for Representations", "Probability and Random Variables", "Statistics and Sampling", "Calculus and Gradient Intuition"]),
            P("1.3", "Data Handling", "Turn messy raw data into inspected, documented, and validated inputs.", "Profile, clean, and export a real dataset.", "Track missingness, duplicates, schema drift, outliers, and cleaning decisions.", ["CSV JSON and Parquet", "Pandas and NumPy Workflow", "Data Validation and Schemas", "Visualization for Debugging"]),
            P("1.4", "Databases and Storage", "Understand where application, training, retrieval, and observability data live.", "Load a cleaned dataset into SQLite and query it.", "Track query correctness, indexes, joins, and storage format decisions.", ["SQL Tables and Joins", "Indexes Transactions and Query Plans", "Document Stores and Object Storage", "Vector Database Preview"]),
            P("1.5", "Web and API Basics", "Learn the service contracts used by LLM APIs, agent tools, dashboards, and deployed products.", "Build a small JSON API or command-line API client.", "Measure request latency, error handling, input limits, and response schema validity.", ["HTTP Methods and Status Codes", "JSON Contracts and Validation", "REST APIs and Streaming", "Auth Headers and Rate Limits"]),
            P("1.6", "Systems Thinking Basics", "Build enough runtime intuition to reason about memory, concurrency, queues, containers, and deployment.", "Wrap a slow data task as a small service or background job.", "Measure runtime, memory, backpressure behavior, and failure recovery.", ["Complexity and Runtime Costs", "Processes Threads and Async IO", "Queues Caches and Background Jobs"]),
        ],
    },
    {
        "num": 2,
        "name": "Machine Learning",
        "tagline": "Learn how models learn from data and how evaluation can lie.",
        "goal": "Develop the ML habits that remain essential for deep learning, LLM applications, and agent systems: baselines, splits, metrics, leakage checks, and error analysis.",
        "artifact": "An ML baseline report comparing simple and stronger models with metrics, error slices, and a model card.",
        "metrics": ["baseline metric", "improved model metric", "train-validation gap", "three error slices", "leakage checklist"],
        "exit": ["frame supervised and unsupervised tasks", "choose and interpret metrics", "detect leakage and evaluation flaws", "write a concise model card and failure analysis"],
        "parts": [
            P("2.1", "Problem Framing", "Turn product goals into learnable tasks with clear targets, labels, features, and constraints.", "Create a task framing document.", "Report target definition, label source, feature availability, and prediction-time constraints.", ["Targets Labels and Features", "Prediction Time Availability", "Label Noise and Annotation Quality", "Baseline Definition"]),
            P("2.2", "Splits and Leakage", "Design evaluation splits that represent future use instead of memorized training data.", "Create and justify two split strategies.", "Track split sizes, group boundaries, time boundaries, duplicates, and leakage risks.", ["Train Validation and Test Sets", "Time and Group Splits", "Data Leakage Patterns", "Preprocessing Without Leakage"]),
            P("2.3", "Supervised Models", "Use simple and strong supervised models before neural complexity.", "Train linear, tree, and ensemble models for the same task.", "Compare lift, calibration, feature importance, speed, and interpretability.", ["Linear and Logistic Models", "Decision Trees and Random Forests", "Gradient Boosted Trees", "Model Pipelines and Hyperparameters", "Interpretability and Feature Importance"]),
            P("2.4", "Metrics and Error Analysis", "Understand model behavior through metrics, thresholds, slices, and concrete failures.", "Create an evaluation report with examples.", "Track confusion matrix, precision/recall tradeoffs, calibration, and slice performance.", ["Classification Metrics", "Regression and Ranking Metrics", "Calibration and Thresholds", "Slice Based Error Analysis"]),
            P("2.5", "Unsupervised Representations", "Prepare for embeddings, clustering, retrieval, and topic discovery.", "Cluster and visualize a dataset.", "Report nearest examples, cluster stability, projection limits, and usefulness.", ["Clustering and Similarity", "Dimensionality Reduction", "Embeddings as Representations"]),
        ],
    },
    {
        "num": 3,
        "name": "Deep Learning",
        "tagline": "Train, debug, and reason about neural networks.",
        "goal": "Understand neural networks deeply enough to work with transformers, fine-tuning, inference optimization, and modern model code.",
        "artifact": "A PyTorch training project with loops, validation curves, checkpoints, ablations, and debugging notes.",
        "metrics": ["training and validation curves", "final validation metric", "training time", "memory use", "ablation result"],
        "exit": ["implement a training loop", "explain autograd and optimizers", "debug a model that does not learn", "read and modify architecture code"],
        "parts": [
            P("3.1", "Neural Network Core", "Connect tensors, layers, losses, gradients, and optimizers to learning behavior.", "Train a tiny neural network and inspect its learning curve.", "Plot loss, accuracy, gradients, and one failed run.", ["Tensors and Shapes", "Layers Activations and Parameters", "Loss Functions", "Backpropagation and Autograd"]),
            P("3.2", "Training Loop Engineering", "Build training code that handles data, devices, checkpoints, validation, and experiment records.", "Create a reusable PyTorch training script.", "Track epoch time, curves, checkpoints, and reproducibility.", ["Datasets and Dataloaders", "Batching and Device Placement", "Training and Evaluation Modes", "Checkpoints and Resume Logic"]),
            P("3.3", "Optimization Dynamics", "Tune training behavior with optimizers, schedules, initialization, regularization, and ablations.", "Run learning-rate and regularization ablations.", "Compare convergence, overfitting, stability, and final metric.", ["SGD Adam and Weight Decay", "Learning Rate Schedules", "Initialization and Normalization", "Regularization and Data Augmentation"]),
            P("3.4", "Architectures and Modalities", "Read and adapt model structures for tabular, vision, text, sequence, and multimodal tasks.", "Train or adapt a small model architecture.", "Compare quality and speed across variants.", ["MLPs CNNs and Sequence Models", "Attention as a Bridge to Transformers", "Transfer Learning", "Multimodal Model Basics"]),
            P("3.5", "Debugging Neural Systems", "Diagnose the ordinary reasons neural networks fail before blaming the architecture.", "Apply a training debugging checklist.", "Record before-after curves, runtime, memory, and the fix.", ["Sanity Checks and Tiny Overfit Tests", "Gradient Problems", "Numerical Stability and Precision"]),
            P("3.6", "Hardware Aware Training Preview", "Understand the first layer of GPU utilization, memory pressure, and data bottlenecks.", "Profile a small training run.", "Track CPU/GPU utilization, dataloader time, batch size, and memory.", ["GPU Utilization Basics", "Memory Footprint", "Profiling Training Runs"]),
        ],
    },
    {
        "num": 4,
        "name": "LLMs",
        "tagline": "Understand tokens, transformers, generation, adaptation, and evaluation.",
        "goal": "Build a practical mental model of LLM behavior so you can choose models, control outputs, evaluate quality, and decide between prompting, RAG, tools, and fine-tuning.",
        "artifact": "An LLM fundamentals notebook comparing models, tokenization, structured outputs, embeddings, costs, and failure cases.",
        "metrics": ["token counts", "latency", "cost estimate", "structured output validity", "small task accuracy"],
        "exit": ["explain tokenization, embeddings, attention, context, and sampling", "choose models by constraints", "use structured outputs", "know when fine-tuning is premature"],
        "parts": [
            P("4.1", "Token and Context Mechanics", "Understand how language becomes tokens and why context is a scarce engineering resource.", "Create tokenization and context-budget demos.", "Report token counts, truncation risks, cost, and latency.", ["Tokenization and Subwords", "Context Windows and Truncation", "Prompt Packing and Context Efficiency", "Token Based Pricing"]),
            P("4.2", "Transformer Mental Model", "Learn the architecture concepts that explain modern LLM behavior.", "Annotate a transformer block and trace a simplified forward pass.", "Check tensor shapes, attention flow, and causal masking.", ["Embeddings and Positional Information", "Self Attention QKV", "MLP Blocks Residuals and Normalization", "Causal Masking"]),
            P("4.3", "Generation Controls", "Control probabilistic text generation and make outputs fit software contracts.", "Compare repeated generations across decoding settings.", "Track variation, validity, latency, and quality.", ["Logits and Softmax", "Temperature Top-p and Top-k", "Stop Sequences and Max Tokens", "Structured Outputs and JSON Schemas", "Frequency and Presence Penalties"]),
            P("4.4", "Model Landscape", "Choose among model families, sizes, licenses, providers, and hosting patterns.", "Create a private model leaderboard for one task.", "Report quality, latency, cost per success, privacy, license, and operations.", ["Closed API and Open Weight Models", "Base Instruct Reasoning and Multimodal Models", "Licenses and Data Policies", "Build Buy Host or Route"]),
            P("4.5", "Prompting and In-Context Learning", "Use instructions, examples, constraints, and decomposition before heavier adaptation.", "Build a prompt testing lab.", "Track prompt version, pass rate, output validity, and regression cases.", ["Prompt Anatomy", "Zero Shot Few Shot and Examples", "Task Decomposition", "Prompt Versioning and Tests"]),
            P("4.6", "Fine-Tuning and Dataset Engineering", "Know when model weights should change and how data quality drives the result.", "Prepare an instruction dataset and PEFT plan.", "Track data quality, coverage, held-out quality, memory, cost, and regressions.", ["When to Fine Tune", "Instruction and Preference Data", "PEFT LoRA and QLoRA", "Fine Tuning Evaluation"]),
            P("4.7", "LLM Evaluation Methodology", "Evaluate open-ended model behavior with exact checks, rubrics, judges, and comparative tests.", "Create a 30-case eval set.", "Track exact pass rate, rubric scores, judge agreement, and failure categories.", ["Exact and Functional Evaluation", "AI as Judge", "Comparative Evaluation"]),
        ],
    },
    {
        "num": 5,
        "name": "AI Applications",
        "tagline": "Build reliable AI products around models.",
        "goal": "Learn prompt systems, RAG, context engineering, user experience, guardrails, evaluation, feedback loops, and application architecture.",
        "artifact": "An evaluated RAG or AI workflow application with documents, prompts, tests, logs, latency, cost, and failure analysis.",
        "metrics": ["retrieval hit rate", "answer correctness", "hallucination rate", "latency", "token cost", "feedback captured"],
        "exit": ["version prompts and context", "build and evaluate RAG", "separate retrieval and generation failures", "add feedback, guardrails, logs, and release checks"],
        "parts": [
            P("5.1", "AI Product Interface", "Design user flows that expose uncertainty, citations, correction, and escalation clearly.", "Design a conversation flow and response policy.", "Track user-visible failures, clarification rate, and correction capture.", ["Conversation UX", "Uncertainty and Abstention", "Citations and Evidence", "Human Escalation"]),
            P("5.2", "Prompt System Engineering", "Treat prompts as versioned product assets with tests and release discipline.", "Create a prompt registry and test suite.", "Track prompt version, test pass rate, output validity, and rollback path.", ["System and User Prompts", "Examples Constraints and Formatting", "Prompt Regression Testing", "Prompt Security Basics"]),
            P("5.3", "RAG Ingestion", "Turn documents into clean, retrievable, inspectable knowledge assets.", "Build a document ingestion pipeline.", "Track parsed documents, rejected content, chunks, metadata, and freshness.", ["Document Parsing and Cleaning", "Chunk Size and Overlap", "Metadata and Filtering", "Deduplication and Freshness", "Multimodal RAG Preview"]),
            P("5.4", "Retrieval and Reranking", "Retrieve the right evidence before asking the model to answer.", "Compare BM25, vector, and hybrid retrieval.", "Track hit rate, recall, precision, latency, and reranker cost.", ["BM25 Term Retrieval", "Embeddings and Vector Search", "Hybrid Search", "Reranking and Query Rewriting"]),
            P("5.5", "Grounded Generation", "Assemble context so answers are faithful, cite evidence, and admit when evidence is missing.", "Build a cited answer generator.", "Track faithfulness, unsupported claims, unknown-answer behavior, and token use.", ["Context Assembly", "Citation Policy", "Conflict Handling"]),
            P("5.6", "Application Evaluation and Feedback", "Measure the whole application through golden sets, rubrics, judges, human review, and user feedback.", "Create a 50-question eval suite and feedback flow.", "Track pass rate, judge agreement, human review notes, and feedback categories.", ["Golden Sets and Rubrics", "Retrieval Evaluation", "Answer Evaluation", "Feedback Loops and Data Flywheels"]),
            P("5.7", "Guardrails and Release Architecture", "Wrap model calls with gateways, routers, validators, caches, monitoring, and incident response.", "Deploy a small AI app with release checks.", "Track p95 latency, cache hit rate, error rate, blocked unsafe requests, and cost.", ["Model Gateways Routers and Caches", "Input and Output Guardrails", "Monitoring Rollback and Incidents"]),
        ],
    },
    {
        "num": 6,
        "name": "AI Agents",
        "tagline": "Build controlled tool-using systems, not vague autonomy.",
        "goal": "Learn the agent loop, planning, tools, MCP, memory, multi-agent coordination, evaluation, observability, and security boundaries.",
        "artifact": "A tool-using agent with typed tools, memory, traces, task evals, prompt-injection tests, and an architecture README.",
        "metrics": ["task success rate", "tool error rate", "loop step count", "cost per successful task", "security test pass rate"],
        "exit": ["implement a manual agent loop", "design typed tools and permissions", "use memory intentionally", "trace, evaluate, and red-team runs"],
        "parts": [
            P("6.1", "Agent Loop Fundamentals", "Build the observe-think-act-observe-finish loop explicitly before using frameworks.", "Build a manual ReAct-style agent.", "Track steps, success, invalid actions, and stop reasons.", ["Agent State and Messages", "Observe Reason Act Observe", "Final Answer and Stop Rules", "Loop Budget and Cancellation"]),
            P("6.2", "Reasoning and Planning Patterns", "Use planning, decomposition, reflection, and routing only when the task needs them.", "Compare direct, ReAct, and planner-executor designs.", "Track quality, cost, latency, and debuggability.", ["ReAct Pattern", "Planner Executor", "Reflection and Self Critique", "Routing and Workflow Agents"]),
            P("6.3", "Tool Design", "Give agents safe, typed, observable interfaces to useful software capabilities.", "Create three typed tools.", "Track schema validity, tool success, retries, and permission blocks.", ["Tool Contracts and JSON Schema", "Function Calling", "Tool Errors Timeouts and Retries", "Idempotency and Side Effects"]),
            P("6.4", "MCP and Tool Ecosystems", "Use Model Context Protocol concepts to expose tools and resources with clear boundaries.", "Create one MCP-style tool server or documented equivalent.", "Track exposed resources, permissions, auth, and host integration.", ["MCP Hosts Clients and Servers", "Resources Tools and Prompts", "Local vs Remote MCP", "Authentication and Exposure Boundaries"]),
            P("6.5", "Memory and Agentic RAG", "Manage short-term state, long-term memory, retrieval, summarization, and forgetting.", "Build an agent with retrieval and selective memory.", "Track retrieval quality, memory precision, stale memory, and context size.", ["Working Memory", "Long Term Memory Types", "Retrieval as a Tool", "Summarization Compression and Forgetting"]),
            P("6.6", "Multi-Agent Systems", "Coordinate specialized agents only when the extra communication improves outcomes.", "Build a planner-researcher-writer-reviewer comparison.", "Track handoff success, conflicts, cost, latency, and quality lift.", ["Supervisor Worker", "Agents as Tools", "Handoffs and Shared State"]),
            P("6.7", "Agent Evaluation and Observability", "Make runs inspectable through task evals, tool tests, traces, metrics, and replay.", "Add evals and tracing to the agent.", "Track success, trace completeness, tool errors, cost, and latency.", ["Task Evals", "Tool Unit and Integration Tests", "Structured Tracing", "Replay and Failure Triage"]),
            P("6.8", "Agent Security and Safety", "Defend against prompt injection, tool abuse, secret leaks, and excessive agency.", "Red-team the agent and add mitigations.", "Track attack success before and after mitigation.", ["Prompt Injection Against Agents", "Least Privilege Tool Access", "Secret Handling and Sandboxing"]),
        ],
    },
    {
        "num": 7,
        "name": "Model Infrastructure",
        "tagline": "Operate AI systems as production software.",
        "goal": "Build the infrastructure layer for data pipelines, model adaptation pipelines, serving, deployment, observability, reliability, and cost control.",
        "artifact": "A deployed model-backed service with data or retrieval pipeline, registry metadata, eval checks, structured logs, and dashboards.",
        "metrics": ["p50 and p95 latency", "error rate", "eval pass rate", "cost per request", "throughput", "rollback time"],
        "exit": ["package AI services reproducibly", "run configured pipelines", "deploy model-backed APIs", "monitor quality, latency, cost, and errors"],
        "parts": [
            P("7.1", "Data Pipeline Architecture", "Move raw data through repeatable ingestion, cleaning, validation, and lineage steps.", "Create an ETL pipeline.", "Track records, rejected rows, schema versions, and lineage.", ["ETL and Scheduled Jobs", "Crawlers and Connectors", "Cleaning and Validation", "Lineage and Versioning"]),
            P("7.2", "RAG and Feature Infrastructure", "Operate embeddings, vector indexes, feature artifacts, and refresh jobs as production assets.", "Build a rebuildable vector index pipeline.", "Track chunks, embedding model, metadata, index version, and rollback.", ["Embedding Jobs", "Vector Store Operations", "Feature Stores and Artifacts", "Index Refresh and Rollback"]),
            P("7.3", "Training and Adaptation Pipelines", "Automate dataset generation, fine-tuning, evaluation, and artifact export.", "Create a generate-train-evaluate-export pipeline.", "Track dataset version, config, checkpoint, report, and promotion decision.", ["Pipeline Orchestration", "Dataset Generation Jobs", "Fine Tuning Jobs", "Model Registry and Release Gates"]),
            P("7.4", "Serving and Deployment", "Expose model behavior through reliable APIs, containers, streaming, batching, and deployment environments.", "Deploy a model-backed endpoint.", "Track cold start, p95, throughput, errors, and reproducibility.", ["Inference APIs and Streaming", "Containers and Runtime Images", "Cloud Deployment", "Queues Batching and Autoscaling"]),
            P("7.5", "Observability and Quality Operations", "Instrument AI systems across prompts, retrieval, model calls, tools, traces, and quality metrics.", "Add dashboards and alert rules.", "Track traces, eval pass rate, latency, errors, token use, and privacy-safe logs.", ["Logs Metrics and Traces", "Evaluation in CI", "Dashboards Alerts and Runbooks"]),
            P("7.6", "Reliability and Cost Control", "Prevent dependency failures, runaway retries, quota blowups, and silent quality regressions.", "Add reliability controls and budget alerts.", "Track retry rate, circuit breaks, cache hits, spend, and recovery time.", ["Timeouts Retries and Circuit Breakers", "Caching Routing and Quotas", "Incident Response and Postmortems"]),
        ],
    },
    {
        "num": 8,
        "name": "Optimization and Hardware",
        "tagline": "Make inference faster, cheaper, and more predictable.",
        "goal": "Understand inference performance, model optimization, serving engines, distributed inference, GPU basics, edge deployment, and accelerator tradeoffs.",
        "artifact": "An inference benchmark and optimization report for an open-weight or hosted model workload.",
        "metrics": ["TTFT", "TPOT", "tokens per second", "p95 latency", "device memory", "cost per 1000 requests", "quality regression"],
        "exit": ["explain prefill, decode, KV cache, batching, and memory math", "apply and evaluate optimization", "choose serving engines and targets", "reason about CPU, GPU, NPU, FPGA, edge, and cloud"],
        "parts": [
            P("8.1", "Inference Performance Model", "Use the measurement vocabulary and workload model behind optimization.", "Benchmark varied prompt, output, and batch shapes.", "Track TTFT, TPOT, throughput, p95, memory, and quality.", ["Latency Throughput and Cost Metrics", "Prefill Decode and KV Cache", "Batch Shape and Concurrency", "Benchmark Design"]),
            P("8.2", "Transformer Inference Internals", "Connect transformer computation to memory bandwidth, attention, cache layout, and sampling.", "Trace one decode step for a small model.", "Track weight memory, KV memory, attention cost, and decode bottleneck.", ["Weight Memory and Activations", "Attention and KV Cache Layout", "GEMM GEMV and MLP Blocks", "Sampling Hot Path"]),
            P("8.3", "Model Optimization", "Change or approximate computation while measuring quality risk.", "Compare baseline and optimized model variants.", "Track memory reduction, speedup, eval drop, validity, and failures.", ["Quantization Formats", "Calibration and Quality Checks", "Distillation and Pruning", "Speculative Decoding"]),
            P("8.4", "Serving Engines", "Understand how runtimes schedule, batch, stream, and manage model memory.", "Serve a model or design a serving plan.", "Track throughput, p95, memory, utilization, errors, and cost.", ["vLLM SGLang TGI and TensorRT LLM", "Continuous Batching", "Paged Attention", "Streaming and Scheduler Policy"]),
            P("8.5", "Distributed Inference", "Scale inference across replicas or devices when one process is not enough.", "Design a multi-GPU serving plan.", "Track memory fit, communication overhead, latency, and capacity.", ["Replica Parallelism", "Tensor Parallelism", "Pipeline and Expert Parallelism"]),
            P("8.6", "GPU and Kernel Basics", "Build the hardware intuition needed to read profiles and understand bottlenecks.", "Profile a simple GPU workload.", "Track occupancy, bandwidth, memory transfers, and kernel time.", ["CUDA Threads Blocks and Warps", "Memory Hierarchy", "Tensor Cores and Mixed Precision", "Triton and Custom Kernels"]),
            P("8.7", "Edge and Accelerator Co-Design", "Connect workloads to Jetson, mobile NPUs, FPGA prototypes, compilers, and future chips.", "Create an edge deployment or accelerator workload contract.", "Track power, thermals, memory, software support, and throughput.", ["Edge Runtime Targets", "Power Thermal and Memory Budgets", "ML Compilers and Graph Lowering", "FPGA ASIC and Dataflow Thinking"]),
        ],
    },
    {
        "num": 9,
        "name": "Security, Blockchain, ZKML",
        "tagline": "Secure, govern, and verify AI-enabled systems.",
        "goal": "Learn AI and agent security, application security, governance, blockchain fundamentals, smart contract risk, zero-knowledge concepts, and practical ZKML limits.",
        "artifact": "A threat model, red-team report, smart contract security lab, and tiny ZKML or verifiable computation demo.",
        "metrics": ["security tests", "attack success before and after mitigation", "risk severity table", "proof generation time", "verifier time or gas", "model size limits"],
        "exit": ["threat-model LLM and agent systems", "apply least privilege", "explain smart contract risks", "build or explain a tiny ZK proof and limits"],
        "parts": [
            P("9.1", "LLM and Agent Security", "Protect systems where models read untrusted content and call tools.", "Threat-model the Stage 6 agent.", "Track attacks, blocked actions, exposure, and residual risks.", ["Prompt Injection and Jailbreaks", "Tool Injection and Excessive Agency", "Data Leakage and Prompt Logs", "Insecure Output Handling"]),
            P("9.2", "Secure AI Application Architecture", "Apply ordinary AppSec and privacy controls to AI services and data flows.", "Create an AI risk register and controls plan.", "Track severity, owner, mitigation, detection, and residual status.", ["Authentication and Authorization", "Secrets and Service Accounts", "Dependency and Model Supply Chain", "Privacy PII and Data Retention"]),
            P("9.3", "Governance and Responsible AI", "Map risks to controls, monitoring, human oversight, documentation, and review processes.", "Write a governance note for a high-impact AI feature.", "Track risk treatment, oversight, monitoring, and documentation completeness.", ["Risk Mapping", "Human Oversight", "Fairness Bias and Toxicity", "Documentation and Auditability"]),
            P("9.4", "Blockchain Fundamentals", "Understand wallets, signatures, transactions, gas, state, and finality before AI systems touch chain state.", "Trace a simple transaction workflow.", "Track keys, permissions, transaction simulation, gas, and rollback assumptions.", ["Wallets Keys and Signatures", "Transactions Blocks and Gas", "Smart Contract State", "Oracles and Off Chain Data"]),
            P("9.5", "Smart Contract Security", "Recognize common contract vulnerabilities and design AI-to-chain permissions safely.", "Create vulnerable contracts, exploits, and fixes.", "Track vulnerabilities reproduced, tests added, gas impact, and residual risk.", ["Reentrancy and External Calls", "Access Control Bugs", "MEV Front Running and Oracle Risk"]),
            P("9.6", "ZK and Verifiable AI", "Use cryptographic verification for trust, privacy, and constrained model claims.", "Prove a tiny model-related computation.", "Track circuit size, proving time, verification time, precision loss, and model limits.", ["Zero Knowledge Fundamentals", "Circuits Witnesses and Provers", "zkVMs and Fixed Point ML", "ZKML Use Cases and Limits"]),
        ],
    },
    {
        "num": 10,
        "name": "Mastery",
        "tagline": "Own a complete AI system end to end.",
        "goal": "Integrate product judgment, LLM understanding, applications, agents, infrastructure, optimization, security, and communication into a capstone portfolio project.",
        "artifact": "A capstone AI system with architecture, implementation, evaluation, deployment, observability, cost, security review, and portfolio narrative.",
        "metrics": ["milestones complete", "eval pass rate", "latency and cost targets", "security review", "documentation quality", "demo reliability"],
        "exit": ["design before coding", "build, evaluate, deploy, secure, and monitor", "debug across the stack", "communicate work through docs, demos, and interviews"],
        "parts": [
            P("10.1", "Capstone Problem and Architecture", "Choose a narrow but real system and design it before coding.", "Write a capstone architecture document.", "Review requirements, alternatives, risks, eval plan, and operations.", ["Problem Selection", "Requirements and Constraints", "Architecture Decision Records", "Evaluation and Risk Plan"]),
            P("10.2", "Capstone Build Execution", "Build the capstone in vertical slices that integrate product, model, data, and deployment early.", "Implement milestone slices.", "Track milestones, eval trend, latency, cost, bugs, and reliability.", ["Vertical Slice Planning", "Integration Testing", "Deployment and Observability", "Failure Analysis"]),
            P("10.3", "Portfolio Communication", "Explain your work through READMEs, diagrams, eval reports, demos, and failure analysis.", "Create README, demo script, diagram, and results report.", "Check whether a reader can run or understand it in 15 minutes.", ["Technical Writing", "Architecture Diagrams", "Demo and Result Narrative"]),
            P("10.4", "Interview and Collaboration Readiness", "Turn project experience into clear debugging stories, design reviews, and collaboration habits.", "Prepare a portfolio walkthrough.", "Track clarity, specificity, evidence, and tradeoff explanations.", ["Debugging Stories", "Design Review Practice", "Code Walkthroughs"]),
            P("10.5", "Specialization and Research Frontiers", "Choose a deeper direction after the core architecture is complete.", "Write a specialization plan with an advanced project.", "Track depth, reproduction quality, benchmark rigor, and explanation quality.", ["Choosing a Direction", "Reading Papers", "Reproducing Systems", "Advanced Project Roadmaps"]),
        ],
    },
]


REFERENCE_SYNTHESIS = [
    "The agent roadmap shaped the agent loop, tools, MCP, memory, multi-agent, evaluation, security, and production sections.",
    "The AI hardware roadmap shaped inference workload contracts, CUDA and kernel thinking, Jetson and edge deployment, ML compiler concepts, FPGA/HLS, and accelerator co-design.",
    "The LLM Engineers Handbook shaped the production spine: data pipelines, RAG, domain boundaries, fine-tuning pipelines, evaluation, monitoring, and deployment.",
    "Hands-On Large Language Models shaped the conceptual LLM order: tokens, embeddings, transformers, prompting, semantic search, RAG, multimodal models, and fine-tuning.",
    "AI Engineering shaped the product-to-production flow: use-case judgment, model evaluation, prompt systems, RAG and agents, dataset engineering, inference optimization, architecture, guardrails, and feedback loops.",
    "W3Schools inspired the Exam UI style: simple learning cards, direct practice entry points, visible progress, and immediate answer checking.",
]


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = text.strip() + "\n"
    if path.suffix == ".md" or path.name == "README.md":
        content = "\n".join(line[4:] if line.startswith("    ") else line for line in content.splitlines()) + "\n"
    path.write_text(content, encoding="utf-8")


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def ordered(items: list[str]) -> str:
    return "\n".join(f"{i}. {item}" for i, item in enumerate(items, 1))


def link(label: str, target: str) -> str:
    return f"[{label}](<{target}>)"


def wrap_words(text: str, limit: int = 24) -> list[str]:
    lines: list[str] = []
    current: list[str] = []
    size = 0
    for word in text.split():
        next_size = len(word) if not current else size + 1 + len(word)
        if current and next_size > limit:
            lines.append(" ".join(current))
            current = [word]
            size = len(word)
        else:
            current.append(word)
            size = next_size
    if current:
        lines.append(" ".join(current))
    return lines or [text]


def mermaid_label(code: str, name: str, limit: int = 24) -> str:
    safe_code = html.escape(code, quote=True)
    lines = [f"<b>{safe_code}</b>"]
    lines.extend(html.escape(line, quote=True) for line in wrap_words(name, limit))
    return "<br/>".join(lines)


def stage_title(stage: dict) -> str:
    if stage["num"] == 4:
        return "Stage 4: Large Language Models"
    if stage["num"] == 8:
        return "Stage 8: Optimization and Hardware Acceleration"
    if stage["num"] == 9:
        return "Stage 9: AI Security, Blockchain, and ZKML"
    return f"Stage {stage['num']}: {stage['name']}"


def stage_path(stage: dict) -> str:
    return f"stages/{stage['num']}. {stage['name']}/index.md"


def stage_dir(stage: dict) -> Path:
    return STAGES_DIR / f"{stage['num']}. {stage['name']}"


def part_folder(part: dict) -> str:
    return f"{part['num']} {part['name']}"


def sub_code(part: dict, idx: int) -> str:
    return f"{part['num']}.{idx}"


def sub_folder(part: dict, idx: int, sub: str) -> str:
    return f"{sub_code(part, idx)} {sub}"


def part_dir(base: Path, part: dict) -> Path:
    return base / part_folder(part)


def sub_dir(pdir: Path, part: dict, idx: int, sub: str) -> Path:
    return pdir / sub_folder(part, idx, sub)


def concept_sentence(stage: dict, part: dict, sub: str) -> str:
    artifact = stage["artifact"].rstrip(".")
    return f"{sub} is the working skill inside {part['name']} that helps you build the stage artifact, {artifact}, while collecting enough evidence to trust the result."


def measure_text(part: dict) -> str:
    return re.sub(r"^(Track|Report|Compare|Measure|Review|Check|Validate)\s+", "", part["measure"], flags=re.IGNORECASE).rstrip(".")


def core_ideas(stage: dict, part: dict, sub: str) -> list[str]:
    if sub == "Frequency and Presence Penalties":
        return [
            "Frequency penalty discourages tokens more strongly each time they repeat.",
            "Presence penalty nudges the model away from tokens that have already appeared at least once.",
            "Both penalties adjust logits before sampling, so they interact with temperature, top-p, and top-k.",
            "Use penalties to reduce loops or repetitive phrasing, not to guarantee factuality or structure.",
            "Measure repetition, validity, latency, and quality before deciding a penalty helped.",
        ]
    return [
        f"Define {sub} in plain language before naming tools or frameworks.",
        f"Connect it to the stage artifact: {stage['artifact']}",
        f"Measure it with: {measure_text(part)}",
        "Name at least one failure mode, because real AI engineering is mostly controlled failure reduction.",
        "Keep the first implementation small enough to inspect by hand before scaling it.",
    ]


def mechanisms(stage: dict, part: dict, sub: str) -> list[str]:
    if sub == "Frequency and Presence Penalties":
        return [
            "Input: candidate token logits plus the tokens already generated in the current response.",
            "Transformation: subtract a penalty from logits for tokens that have already appeared.",
            "Contract: reduce unwanted repetition while preserving required terms, schema validity, and task quality.",
            f"Measurement: compare repeat rate, duplicate n-grams, validity, latency, and quality across settings.",
            "Failure mode: excessive penalties can make output wander, avoid necessary terms, or break exact formats.",
        ]
    stage_name = stage["name"]
    return [
        f"Input: identify what raw information, code, data, prompt, model output, trace, or user signal {sub} consumes.",
        f"Transformation: describe what changes between input and output in {part['name']}.",
        f"Contract: write the expected shape, constraints, and success criteria so another engineer can check it.",
        f"Measurement: use {measure_text(part)} as the first observable proof.",
        f"Failure mode: record how {sub} can fail specifically in {stage_name}, not only in theory.",
    ]


def worked_example(stage: dict, part: dict, sub: str) -> str:
    if sub == "Frequency and Presence Penalties":
        return (
            "Use one prompt that tends to repeat itself, such as asking for ten naming ideas, taglines, or short troubleshooting tips. "
            "Run it once with both penalties at zero, once with a modest frequency penalty, and once with a modest presence penalty. "
            "Keep the prompt, model, temperature, top-p, max tokens, and schema settings the same. "
            "Then compare duplicate phrases, required-term retention, output validity, latency, and human quality notes. "
            "The useful decision is not which penalty sounds better in theory; it is which setting reduces repetition without damaging the task contract."
        )
    artifact = stage["artifact"].rstrip(".")
    return (
        f"Imagine you are building the stage artifact: {artifact}. "
        f"For {sub}, start with the smallest useful slice. Write the input, the expected output, the boundary conditions, and one case that should fail. "
        f"Then implement only enough to observe the behavior. If the result works once, do not move on yet. Run it against a slightly different input, measure it with {measure_text(part)}, and add the result to your notes."
    )


def domain_guidance(stage: dict, part: dict, sub: str) -> list[str]:
    text = f"{stage['name']} {part['name']} {sub}".lower()
    rules = [
        (["frequency", "presence", "penalty", "penalties"], [
            "Frequency penalty lowers the probability of a token in proportion to how often that token has already appeared in the generated text.",
            "Presence penalty lowers the probability of a token once it has appeared at least once, which encourages the model to introduce new tokens or ideas.",
            "Both penalties are logit adjustments before sampling; they do not replace prompting, retrieval, validation, or evaluation.",
            "Use modest penalties when outputs loop, repeat wording, or need more variety in brainstorming and drafting tasks.",
            "Keep penalties low for structured outputs, code, citations, product names, required terminology, and any task where repetition is correct.",
            "Measure duplicate n-grams, repeated required fields, schema validity, and human quality notes before changing the setting permanently.",
        ]),
        (["json schema", "tool contract", "function calling", "tool errors", "idempotency"], [
            "A tool contract should name the action precisely, describe when to use it, define required and optional arguments, and state exactly what the tool returns.",
            "Use narrow argument types, enums, ranges, and validation rules so the model has fewer ways to produce ambiguous calls.",
            "Return structured observations that help the model decide the next step without leaking secrets or raw stack traces.",
            "Separate read-only, write, and destructive tools; the schema should not be the only safety boundary.",
            "Test malformed arguments, timeout behavior, duplicate calls, and permission failures before trusting the agent loop.",
        ]),
        (["mcp", "hosts", "clients", "servers", "resources tools"], [
            "MCP separates the host that runs the model experience from clients and servers that expose tools or resources.",
            "A server should expose only the tools and resources the agent genuinely needs for the task.",
            "Local MCP servers are useful for filesystem or developer workflows; remote servers need stronger authentication, authorization, and audit logs.",
            "Resource exposure is as important as tool exposure because retrieved context can influence model decisions.",
            "Document the trust boundary: what data leaves the host, what the server can do, and what requires user approval.",
        ]),
        (["agent", "react", "planner", "memory", "handoff", "multi-agent", "routing"], [
            "Agent behavior is a control-flow problem: state, decision, action, observation, and stop condition must be visible.",
            "Use the simplest loop that solves the task; planning and multi-agent coordination add cost and new failure modes.",
            "Trace every model call, tool call, observation, and stop reason so failures can be replayed.",
            "Memory should be selective and typed; storing everything often creates stale or unsafe context.",
            "Measure success per completed task, not per individual model call.",
        ]),
        (["token", "context", "transformer", "attention", "logits", "temperature", "top-p", "structured output"], [
            "LLMs operate on tokens, so cost, latency, truncation, and output limits should be calculated in tokens rather than words.",
            "Context is temporary working input, not durable memory; decide what belongs in the prompt, what should be retrieved, and what should be summarized.",
            "Generation controls change the probability distribution over next tokens; use low randomness for contracts and higher randomness only when variation is useful.",
            "Structured outputs should be validated by code, not trusted because the prompt requested JSON.",
            "When behavior changes, compare prompt tokens, output tokens, decoding settings, and schema validity before changing models.",
        ]),
        (["rag", "retrieval", "chunk", "metadata", "vector", "reranking", "citation", "grounded"], [
            "RAG quality depends on ingestion, chunking, metadata, retrieval, context assembly, and generation; test these components separately.",
            "Term retrieval is a strong baseline; vector retrieval helps semantic matches; hybrid retrieval often improves coverage.",
            "Chunking controls the tradeoff between precise evidence and enough surrounding context.",
            "Citations should point to evidence the model actually received, not sources discovered somewhere else.",
            "Unknown-answer behavior is a success case when the retrieval set contains no supporting evidence.",
        ]),
        (["metric", "evaluation", "eval", "test", "rubric", "judge", "calibration", "error analysis"], [
            "Evaluation starts by defining what good output means for the user and the workflow.",
            "Use exact checks whenever possible, rubrics when judgment is needed, and AI judges only with calibration examples and spot checks.",
            "Slice failures by source, task type, input length, user group, difficulty, or tool path to find actionable patterns.",
            "Regression tests protect existing behavior when prompts, models, data, or tools change.",
            "A metric should drive a decision: keep, roll back, investigate, route, retrain, or redesign.",
        ]),
        (["pipeline", "registry", "deployment", "serving", "container", "streaming", "observability", "reliability", "cost"], [
            "Production AI needs reproducible configs, versioned artifacts, release gates, and rollback paths for prompts, indexes, and models.",
            "Serving design should match workload shape: streaming for interactive UX, batching for throughput, queues for slow jobs.",
            "Observability must include model metadata, prompt version, token counts, retrieval details, tool calls, latency, and errors.",
            "Retries can multiply cost and duplicate side effects, so pair them with idempotency and budgets.",
            "Measure cost per successful task, not only cost per request.",
        ]),
        (["quantization", "kv cache", "prefill", "decode", "gpu", "cuda", "kernel", "tensor parallel", "edge", "accelerator"], [
            "Inference optimization starts with TTFT, TPOT, throughput, memory, and quality regression measurements.",
            "Prefill processes the input context; decode generates tokens autoregressively and is often memory-bandwidth sensitive.",
            "KV cache size grows with layers, hidden dimensions, context length, batch size, and precision.",
            "Quantization reduces memory and bandwidth but must be checked against task quality and structured-output validity.",
            "Hardware choices should follow a workload contract: context length, output length, concurrency, latency target, memory budget, and power limit.",
        ]),
        (["security", "prompt injection", "secret", "sandbox", "auth", "privacy", "governance", "risk"], [
            "Treat model inputs, retrieved documents, tool outputs, and user messages as potentially untrusted.",
            "The model should not enforce critical permissions by itself; policy must be checked in application code or tool boundaries.",
            "Secrets should not enter prompts, traces, eval logs, or vector indexes unless a deliberate secure design requires it.",
            "Security tests should include malicious instructions, malformed tool outputs, data exfiltration attempts, and unsafe generated output.",
            "Risk controls need owners, detection signals, and residual-risk notes.",
        ]),
        (["blockchain", "smart contract", "wallet", "gas", "oracle", "reentrancy", "zk", "zkml", "proof"], [
            "Blockchain actions are often public and hard to reverse, so AI systems should draft or simulate before signing.",
            "Private keys and signing permissions should stay outside the model loop and behind explicit policy gates.",
            "Smart contract security requires adversarial thinking around external calls, access control, oracles, upgrades, and transaction ordering.",
            "ZK proofs verify a specific statement about computation; they do not automatically prove the entire AI system is trustworthy.",
            "ZKML is constrained by arithmetic representation, circuit size, proving time, and model size.",
        ]),
        (["python", "pandas", "sql", "data", "schema", "visualization", "notebook"], [
            "Foundation work should produce code and data artifacts another engineer can run, inspect, and test.",
            "Data cleaning decisions should be recorded because they change model behavior later.",
            "Schemas catch upstream changes before they become silent evaluation or retrieval failures.",
            "Notebooks are useful for exploration, but reusable logic should move into modules, scripts, or tests.",
            "Visualizations should answer a decision question, not merely decorate the report.",
        ]),
        (["linear algebra", "probability", "statistics", "gradient", "loss", "autograd", "optimizer", "training"], [
            "Math becomes useful when it explains a specific model behavior, metric, or failure mode.",
            "Shapes, distributions, gradients, and losses should be connected to code and plotted examples.",
            "Small simulations reveal uncertainty and variance better than memorized definitions.",
            "Training failures often come from data, loss choice, learning rate, gradients, initialization, or evaluation bugs.",
            "Use tiny overfit tests and sanity checks before scaling model size.",
        ]),
    ]
    for keys, guidance in rules:
        if any(key in text for key in keys):
            return guidance
    return [
        f"In {stage['name']}, this topic should be studied through the stage artifact rather than as a standalone definition.",
        "Write the input, output, assumptions, measurement, and failure mode before implementation.",
        "Start with a small example that can be inspected manually.",
        "Add one edge case and one regression case.",
        "Only scale the implementation after the measurement supports the next decision.",
    ]


def mermaid_stage(stage: dict) -> str:
    lines = [
        "```mermaid",
        '%%{init: {"flowchart": {"htmlLabels": true, "nodeSpacing": 70, "rankSpacing": 90}, "themeVariables": {"fontSize": "18px"}} }%%',
        "flowchart LR",
    ]
    previous = None
    for idx, part in enumerate(stage["parts"], 1):
        node = f"P{idx}"
        lines.append(f'  {node}["{mermaid_label(part["num"], part["name"])}"]')
        if previous:
            lines.append(f"  {previous} --> {node}")
        previous = node
    lines.append("```")
    return "\n".join(lines)


def mermaid_part(part: dict) -> str:
    lines = [
        "```mermaid",
        '%%{init: {"flowchart": {"htmlLabels": true, "nodeSpacing": 80, "rankSpacing": 110}, "themeVariables": {"fontSize": "18px"}} }%%',
        "flowchart LR",
        f'  P["{mermaid_label(part["num"], part["name"], 22)}"]',
    ]
    for idx, sub in enumerate(part["subparts"], 1):
        lines.append(f'  P --> S{idx}["{mermaid_label(sub_code(part, idx), sub, 22)}"]')
    lines.append('  P --> E["<b>Exam</b><br/>Part practice"]')
    lines.append("```")
    return "\n".join(lines)


def part_extra_sections(stage: dict, part: dict) -> str:
    if stage["num"] != 4 or part["num"] != "4.3":
        return ""
    return dedent("""
    ## Generation Control Flow

    This diagram shows a beginner-friendly order for applying common generation controls during one next-token step. Stop sequences, max tokens, and structured-output checks sit around the sampling loop because they decide whether to continue, stop, validate, retry, or reject the result.

    <div class="roadmap-diagram roadmap-diagram--part" markdown="1">

    ```mermaid
    %%{init: {"flowchart": {"htmlLabels": true, "nodeSpacing": 70, "rankSpacing": 90}, "themeVariables": {"fontSize": "18px"}} }%%
    flowchart TD
        A["Prompt + text generated so far<br/>+ optional JSON schema or format contract"] --> B["Model outputs raw logits<br/>z_i for every candidate token"]
        B --> C["Count token history<br/>count_i and seen_i"]
        C --> D["Frequency + presence penalties<br/>z_pen_i = z_i - frequency_penalty * count_i - presence_penalty * seen_i"]
        D --> E["Temperature<br/>score_i = z_pen_i / temperature"]
        E --> F["Softmax<br/>P_i = exp(score_i) / sum_j exp(score_j)"]
        F --> G["Top-k filter<br/>keep the k highest probabilities"]
        G --> H["Top-p filter<br/>keep the smallest sorted group whose total probability reaches p"]
        H --> I["Structured-output constraint<br/>mask tokens that cannot continue valid JSON or schema<br/>(when constrained decoding is supported)"]
        I --> J["Renormalize<br/>remaining probabilities add to 100%"]
        J --> K["Sample one token"]
        K --> L["Append token to output"]
        L --> M{"Stop sequence matched?"}
        M -- "yes" --> Z["Stop and return output<br/>usually without the stop sequence"]
        M -- "no" --> N{"Max output tokens reached?"}
        N -- "yes" --> Y["Stop with length limit<br/>output may be incomplete"]
        N -- "no" --> O{"Structured output complete?"}
        O -- "no" --> A
        O -- "yes" --> P["Validate JSON/schema in code"]
        P --> Q{"Valid?"}
        Q -- "yes" --> Z
        Q -- "no" --> R["Handle failure<br/>retry, repair, or reject"]
    ```

    </div>

    Exact order can vary by provider or inference library. Some systems apply top-k before top-p, some expose only a few controls, and some add controls such as repetition penalty or min-p. Structured-output implementations also differ: some constrain token choices during decoding, while others validate or repair after the text is complete.

    Beginner model:

    1. The model creates raw logits.
    2. Frequency and presence penalties adjust logits for tokens already used.
    3. Temperature reshapes the logits.
    4. Softmax turns logits into probabilities.
    5. Top-k and top-p remove candidate tokens.
    6. Structured-output constraints can mask tokens that would break valid JSON or the schema.
    7. The remaining probabilities are rescaled.
    8. The model samples one token.
    9. Stop sequences, max tokens, and structured-output completion checks decide whether to stop or continue.
    10. Completed structured outputs should still be validated by code.
    """).strip() + "\n\n"


def stage_index(stage: dict, idx: int) -> str:
    title = stage_title(stage)
    part_rows = []
    sub_rows = []
    for part in stage["parts"]:
        pf = part_folder(part)
        part_rows.append(f"| {link(part['num'] + ' ' + part['name'], pf + '/index.md')} | {part['summary']} | {part['build']} |")
        for sidx, sub in enumerate(part["subparts"], 1):
            sf = sub_folder(part, sidx, sub)
            sub_rows.append(f"| {part['num']} | {link(sub_code(part, sidx) + ' ' + sub, pf + '/' + sf + '/index.md')} | {concept_sentence(stage, part, sub)} |")
    nav = []
    if idx:
        prev = STAGES[idx - 1]
        nav.append(f"Previous: {link(stage_title(prev), '../' + str(prev['num']) + '. ' + prev['name'] + '/index.md')}")
    if idx < len(STAGES) - 1:
        nxt = STAGES[idx + 1]
        nav.append(f"Next: {link(stage_title(nxt), '../' + str(nxt['num']) + '. ' + nxt['name'] + '/index.md')}")
    return dedent(f"""
    # {title}

    <span class="stage-badge">{stage['num']}</span> {stage['tagline']}

    ## Goal

    {stage['goal']}

    ## Roadmap to Master This Stage

    {ordered([
        "Read the stage goal and diagram before opening the parts.",
        "Move through the parts in order unless you can already pass the exit criteria.",
        "Study each sub-part folder: overview, deep dive, and examples/practice.",
        "Build the stage artifact in small slices and measure the listed metrics.",
        "Use the part exam after each part, or open the global Exam tab to test across the roadmap.",
    ])}

    ## Stage Structure Diagram

    <div class="roadmap-diagram roadmap-diagram--stage" markdown="1">

    {mermaid_stage(stage)}

    </div>

    ## Parts

    | Part | Simple explanation | Build focus |
    |---|---|---|
    {chr(10).join(part_rows)}

    ## Sub-Part Map

    | Part | Sub-part | Why it matters |
    |---|---|---|
    {chr(10).join(sub_rows)}

    ## Stage Artifact

    {stage['artifact']}

    ## What to Measure

    {bullet(stage['metrics'])}

    ## Exit Criteria

    {bullet(stage['exit'])}

    ## Navigation

    {" | ".join(nav) if nav else "Continue forward when the exit criteria are real."}
    """)


def part_index(stage: dict, part: dict) -> str:
    title = stage_title(stage)
    rows = []
    for idx, sub in enumerate(part["subparts"], 1):
        sf = sub_folder(part, idx, sub)
        rows.append(f"| {link(sub_code(part, idx) + ' ' + sub, sf + '/index.md')} | {concept_sentence(stage, part, sub)} |")
    return dedent(f"""
    # {part['num']} {part['name']}

    ## Role at {title}

    {part['summary']} This part is one capability inside the stage. It should leave behind an artifact, measurements, and a short explanation of failure modes.

    ## Explanation

    This part has {len(part['subparts'])} sub-parts because the topic needs that many learning units to feel natural. Some stages have more parts and some have fewer; the structure follows the topic, not a fixed template.

    ## Part Diagram

    <div class="roadmap-diagram roadmap-diagram--part" markdown="1">

    {mermaid_part(part)}

    </div>

    {part_extra_sections(stage, part)}## Sub-Parts

    | Sub-part folder | What it explains |
    |---|---|
    {chr(10).join(rows)}

    ## What a Person Who Masters This Part Can Do

    - Explain how {part['name']} supports {stage['artifact'].lower()}.
    - Build and inspect this artifact: {part['build']}
    - Measure progress with: {part['measure']}
    - Debug at least one failure mode before moving to the next part.

    ## Build and Measure

    **Build:** {part['build']}

    **Measure:** {part['measure']}

    ## Tests

    Take one 30-question exam after studying this part. It opens in a new browser tab so the study page stays available.

    <div class="exam-actions exam-actions--single">
      <a href="test/exam.html" target="_blank" rel="noopener">Open Part Exam</a>
    </div>

    ## Back to Stage

    Return to {link(title, "../index.md")}.
    """)


def sub_index(stage: dict, part: dict, idx: int, sub: str) -> str:
    return dedent(f"""
    # {sub_code(part, idx)} {sub}

    ## Why This Sub-Part Matters

    {concept_sentence(stage, part, sub)} A sub-part is now a folder so longer topics can grow without forcing everything into one huge page.

    ## Study Pages

    | Page | Purpose |
    |---|---|
    | [Deep Dive](<deep-dive.md>) | Full explanation, mechanisms, examples, and failure modes. |
    | [Examples and Practice](<examples-and-practice.md>) | Worked exercises, project drills, and self-check prompts. |

    ## Core Ideas

    {bullet(core_ideas(stage, part, sub))}

    ## How to Study It

    {ordered([
        "Read this overview and write the concept in your own words.",
        "Read the deep dive and identify the input, transformation, output, and failure mode.",
        "Complete the examples and practice page.",
        f"Add one measurement using: {part['measure']}",
    ])}

    ## Completion Standard

    - I can explain {sub} without naming a tool first.
    - I can connect it to the stage artifact.
    - I can show a small artifact, measurement, or test.
    - I know how it fails and what I would inspect first.

    Return to {link(part['num'] + ' ' + part['name'], '../index.md')}.
    """)


def deep_dive(stage: dict, part: dict, idx: int, sub: str) -> str:
    artifact = stage["artifact"].rstrip(".")
    return dedent(f"""
    # Deep Dive: {sub}

    ## Mental Model

    {concept_sentence(stage, part, sub)} Treat it as a small engineering contract: what enters, what changes, what leaves, how you know it worked, and how it can fail.

    ## Key Mechanisms

    {bullet(mechanisms(stage, part, sub))}

    ## Domain Details

    {bullet(domain_guidance(stage, part, sub))}

    ## Detailed Explanation

    Start with the user or engineering problem. In {stage['name']}, the learner is trying to produce this artifact: {artifact}. {sub} is one piece of that artifact. It should not be studied as an isolated vocabulary item; it should be tied to code, data, diagrams, tests, metrics, or operational behavior.

    A useful way to reason about {sub} is to ask four questions. First, what does it receive as input? Second, what assumptions does it make? Third, what output or decision does it create? Fourth, what would make that output untrustworthy? These questions keep the topic practical even when the surrounding AI field feels noisy.

    The implementation should begin small. If {sub} involves code, write the smallest script, notebook cell, route, prompt, schema, or benchmark that exposes the behavior. If it involves design, write a one-page plan with a diagram and at least one measurable acceptance criterion. If it involves security or evaluation, write a test case before building the mitigation.

    The measurement is the part that turns learning into engineering. For this part, use: {measure_text(part)}. The exact number does not need to be perfect at first. It needs to be honest, repeatable, and connected to a decision you would make next.

    ## Worked Example

    {worked_example(stage, part, sub)}

    ## Common Failure Modes

    - The concept is described correctly, but no artifact proves it.
    - The learner changes models, tools, or frameworks before measuring the current failure.
    - The implementation works only on the happy path.
    - The measurement is not connected to a decision.
    - The failure mode is too vague to debug.

    ## What Good Looks Like

    A strong learner can point to a small artifact, explain the tradeoff, show a measurement, and name the next improvement. For {sub}, that means the explanation is grounded in {part['name']} and the stage artifact rather than floating as general AI vocabulary.

    Return to {link(sub_code(part, idx) + ' ' + sub, 'index.md')}.
    """)


def examples_practice(stage: dict, part: dict, idx: int, sub: str) -> str:
    if sub == "Frequency and Presence Penalties":
        return dedent(f"""
        # Examples and Practice: {sub}

        ## Worked Practice

        1. Write one paragraph explaining the difference between frequency penalty and presence penalty.
        2. Draw a small diagram that shows token history, logit adjustment, sampling, and output.
        3. Run or outline three generations for the same prompt: no penalties, modest frequency penalty, and modest presence penalty.
        4. Measure it with: {part['measure']}
        5. Add one failure case where a penalty makes the answer worse.

        ## Mini Project Drill

        Create a file named `notes/{slug(sub)}.md` in your project workspace. Include:

        - the prompt you tested
        - the generation settings that stayed fixed
        - the frequency penalty and presence penalty values you compared
        - one example output for each setting
        - duplicate phrase or n-gram observations
        - schema validity or format validity, if relevant
        - one decision you would make from the result

        ## Check Your Understanding

        | Question | What a strong answer includes |
        |---|---|
        | What does frequency penalty do? | It penalizes repeated tokens more as they appear more often, which can reduce loops and repeated wording. |
        | What does presence penalty do? | It penalizes tokens after they have appeared once, which can push the model toward new tokens or ideas. |
        | When can penalties hurt? | They can avoid required terms, damage exact formats, weaken code, or make structured output less valid. |
        | How would you test them? | Keep the prompt and other decoding settings fixed, compare repeated runs, and measure repetition, validity, latency, and quality. |

        ## Stretch Exercise

        Repeat the drill on a structured-output prompt. Record whether penalties improve variety or damage contract validity.

        Return to {link(sub_code(part, idx) + ' ' + sub, 'index.md')}.
        """)
    return dedent(f"""
    # Examples and Practice: {sub}

    ## Worked Practice

    1. Write one paragraph explaining {sub} to a beginner.
    2. Draw the smallest diagram that shows input, transformation, output, and failure mode.
    3. Build or outline a tiny artifact connected to: {part['build']}
    4. Measure it with: {part['measure']}
    5. Add one failure case to your learning log.

    ## Mini Project Drill

    Create a file named `notes/{slug(sub)}.md` in your project workspace. Include:

    - the problem {sub} solves
    - the simplest implementation or design
    - the measurement you used
    - one example input
    - one expected output
    - one failure case
    - one decision you would make from the result

    ## Check Your Understanding

    | Question | What a strong answer includes |
    |---|---|
    | Why does {sub} matter? | It connects to {stage['artifact'].lower()} and names a practical risk. |
    | How would you test it? | It uses a small repeatable case and a measurable expected result. |
    | What breaks first? | It names a specific failure mode, not only "the model is bad". |
    | When should you move on? | When the artifact works on a realistic case and one edge case. |

    ## Stretch Exercise

    Revisit the same drill after finishing the next part. Update the note with what changed. This is how isolated concepts become connected system judgment.

    Return to {link(sub_code(part, idx) + ' ' + sub, 'index.md')}.
    """)


EXAM_LEVELS = [
    (1, "Recall"),
    (2, "Purpose"),
    (3, "Mechanism"),
    (4, "Artifact"),
    (5, "Measurement"),
    (6, "Failure Mode"),
    (7, "Debugging"),
    (8, "Tradeoff"),
    (9, "Production"),
    (10, "Mastery"),
]


def source_guidance(stage: dict, part: dict) -> str:
    haystack = f"{stage['name']} {part['name']}".lower()
    if stage["num"] == 4 or any(term in haystack for term in ["token", "transformer", "generation", "fine-tuning", "embedding"]):
        return "Use the Hands-On LLMs spine: tokens and embeddings, transformer behavior, generation controls, semantic search, and fine-tuning only when the data and evaluation support it."
    if stage["num"] in [5, 6] or any(term in haystack for term in ["rag", "agent", "prompt", "retrieval", "tool"]):
        return "Use the AI Engineering framing: decide whether the use case should exist, construct context carefully, evaluate outputs, manage hallucination risk, and keep a feedback loop."
    if stage["num"] == 7 or any(term in haystack for term in ["pipeline", "serving", "deployment", "observability", "infrastructure"]):
        return "Use the LLM Engineer's Handbook production spine: domain boundaries, data pipelines, RAG services, evaluation, monitoring, deployment, and CI/CD evidence."
    if stage["num"] == 8 or any(term in haystack for term in ["optimization", "hardware", "inference", "kernel", "serving engine"]):
        return "Use the optimization framing from AI Engineering and Hands-On LLMs bonus material: measure latency, memory, throughput, quantization effects, and user-visible quality together."
    if stage["num"] == 9 or any(term in haystack for term in ["security", "guardrail", "governance", "zk", "blockchain"]):
        return "Use the AI Engineering security framing: protect context, tools, data, permissions, evaluation, monitoring, and misuse paths before trusting a release."
    return "Use the shared book pattern: start from the problem, build the smallest artifact, evaluate it, inspect failures, and write the next engineering decision."


def part_questions(stage: dict, part: dict, qtype: str, count: int = 10) -> list[dict]:
    out = []
    pid = slug(part["num"] + "-" + part["name"])
    source = source_guidance(stage, part)
    answer_templates = [
        "Define {sub} inside {part_num} {part_name} without naming a tool first.",
        "Why does {sub} matter for the stage artifact?",
        "Explain the mechanism that makes {sub} useful in a real AI system.",
        "What concrete artifact would prove that you understand {sub}?",
        "Which measurement should decide whether {sub} is working?",
        "Name one failure mode of {sub} and the first signal that would expose it.",
        "A result involving {sub} is wrong. What do you inspect first, second, and third?",
        "What tradeoff does {sub} create between quality, cost, latency, risk, or maintainability?",
        "How would {sub} change when moving from a demo to production?",
        "Teach {sub} as a decision rule a senior AI engineer would use.",
    ]
    blank_items = [
        ("A concept is not mastered until it produces a concrete ____.", "artifact"),
        ("The purpose of {sub} should be tied to a user problem and a measurable ____.", "outcome"),
        ("A reliable system contract names input, output, assumptions, and ____.", "failure mode"),
        ("The part artifact for {part_name} should be small enough to inspect and strong enough to ____.", "measure"),
        ("Evaluation should compare behavior against examples, metrics, and ____ cases.", "edge"),
        ("When {sub} breaks, the failure should be recorded in the learning ____.", "log"),
        ("Debugging starts by reproducing the issue before changing the ____.", "implementation"),
        ("A strong engineering decision explains the quality, cost, latency, and risk ____.", "tradeoff"),
        ("Production readiness requires monitoring, rollback thinking, and a regression ____.", "guard"),
        ("Mastery means connecting {sub} to artifact, evaluation, failure, and next ____.", "decision"),
    ]
    apply_items = [
        ("A learner can define {sub}, but has no artifact. What should happen next?", "Build the smallest inspectable artifact and connect it to the part measurement."),
        ("A stakeholder asks for {sub}, but the user problem is vague. What is the best first move?", "Clarify the user outcome, risk, and acceptance criteria before choosing a tool."),
        ("The mechanism behind {sub} is unclear, but the demo appears to work. What should you do?", "Trace input, transformation, output, and failure assumptions before trusting the demo."),
        ("Your artifact for {sub} works only on the happy path. What is missing?", "Add an edge case and document the expected behavior before expanding scope."),
        ("The metric for {sub} improves while the user-visible answer gets worse. What should you inspect?", "Inspect examples, slices, and the metric definition before optimizing further."),
        ("A failure involving {sub} appears after release. What is the safest response?", "Reproduce the failure, compare against the guard, and record the regression before changing the system."),
        ("A teammate wants to switch models or frameworks to fix {sub}. What should you ask for first?", "Ask for the failure trace and baseline measurement that justify the change."),
        ("Two solutions for {sub} both work. One is slower and safer; one is faster and riskier. What decides?", "Choose using the documented tradeoff: user value, risk, latency, cost, and reversibility."),
        ("The demo for {sub} is ready for users. What production evidence is still needed?", "Add monitoring, rollback criteria, regression checks, and ownership for failures."),
        ("You are mentoring someone on {sub}. What final proof shows mastery?", "They can explain the decision rule, show the artifact, evaluate it, and debug a realistic failure."),
    ]
    distractors = [
        "Switch to a larger model immediately and skip the current measurement.",
        "Keep the demo result because it worked once on the easiest example.",
        "Delete the failing case so the reported metric looks cleaner.",
    ]

    for i, (level, label) in enumerate(EXAM_LEVELS[:count]):
        sub = part["subparts"][i % len(part["subparts"])]
        sid = f"{pid}-{qtype}-l{level}"
        common = {
            "id": sid,
            "stageId": f"s{stage['num']}",
            "partId": pid,
            "type": qtype,
            "level": level,
            "levelLabel": label,
            "source": source,
        }
        if qtype == "answer":
            question = answer_templates[i].format(sub=sub, part_num=part["num"], part_name=part["name"])
            common.update({
                "question": question,
                "answer": f"Connect {sub} to {stage['artifact'].rstrip('.')}. Use the part measurement ({measure_text(part)}) as evidence, mention the artifact ({part['build']}), and name a concrete failure mode. {source}",
            })
        elif qtype == "blank":
            template, answer = blank_items[i]
            common.update({
                "question": template.format(sub=sub, part_name=part["name"]),
                "answer": answer,
            })
        else:
            scenario, answer = apply_items[i]
            choices = [answer, *distractors]
            shift = i % len(choices)
            choices = choices[shift:] + choices[:shift]
            common.update({
                "question": scenario.format(sub=sub),
                "answer": answer,
                "choices": choices,
            })
        out.append(common)
    return out


def exam_app_html(asset_prefix: str, fixed_part_id: str = "", heading: str = "Exam", subtitle: str = "", directory: str = "") -> str:
    fixed_attr = f' data-fixed-part="{html.escape(fixed_part_id, quote=True)}"' if fixed_part_id else ""
    heading_attr = html.escape(heading, quote=True)
    subtitle_attr = html.escape(subtitle, quote=True)
    return f"""
    <div id="exam-app" class="exam-shell exam-app"{fixed_attr} data-heading="{heading_attr}" data-subtitle="{subtitle_attr}">
      <section class="exam-hero exam-hero--modern">
        <div>
          <p class="exam-kicker">Modern AI Engineer Roadmap</p>
          <h2 id="exam-title">{html.escape(heading)}</h2>
          <p id="exam-subtitle">{html.escape(subtitle or "Choose a part exam. Each part uses 30 levelled problems: 10 answer, 10 blank, and 10 apply.")}</p>
        </div>
        <div class="exam-summary-card" aria-label="Exam structure">
          <strong>30</strong>
          <span>10 x 3 types</span>
        </div>
      </section>
      <section class="exam-panel exam-config">
        <div class="exam-controls">
          <label id="exam-stage-label">Stage <select id="exam-stage"></select></label>
          <label id="exam-part-label">Part <select id="exam-part"></select></label>
          <label>Type <select id="exam-type"></select></label>
          <label>Count <select id="exam-count"><option>10</option><option>20</option><option selected>30</option></select></label>
          <button type="button" id="exam-start">Start Exam</button>
        </div>
      </section>
      <section class="exam-status-grid" aria-label="Exam status">
        <div class="exam-stat"><strong id="exam-total">0</strong><span>questions</span></div>
        <div class="exam-stat"><strong id="exam-done">0</strong><span>answered</span></div>
        <div class="exam-stat"><strong id="exam-score">0</strong><span>auto score</span></div>
      </section>
      <section class="exam-progress-wrap">
        <div class="exam-progress"><span id="exam-progress-bar"></span></div>
        <p id="exam-progress-text">Choose filters and start.</p>
      </section>
      <section id="exam-overview" class="exam-overview" aria-label="Question overview"></section>
      <section id="exam-question" class="exam-question"></section>
      <section id="exam-review" class="exam-review"></section>
    </div>
    {directory}
    <script src="{asset_prefix}/js/exam-data.js"></script>
    <script src="{asset_prefix}/js/exam-ui.js"></script>
    """


def part_exam_html(stage: dict, part: dict) -> str:
    pid = slug(part["num"] + "-" + part["name"])
    title = f"{part['num']} {part['name']} Exam"
    subtitle = f"30 levelled problems for {stage_title(stage)}: 10 answer, 10 blank, and 10 apply."
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="../../../../assets/css/custom.css">
</head>
<body class="standalone-exam">
<main class="standalone-exam__main">
{exam_app_html("../../../../assets", fixed_part_id=pid, heading=title, subtitle=subtitle)}
</main>
</body>
</html>"""


def exam_data() -> dict:
    stages = []
    parts = []
    questions = []
    for stage in STAGES:
        sid = f"s{stage['num']}"
        stages.append({"id": sid, "title": stage_title(stage), "path": stage_path(stage)})
        for part in stage["parts"]:
            pid = slug(part["num"] + "-" + part["name"])
            base_path = f"stages/{stage['num']}. {stage['name']}/{part_folder(part)}"
            parts.append({
                "id": pid,
                "stageId": sid,
                "title": f"{part['num']} {part['name']}",
                "path": f"{base_path}/index.md",
                "examPath": f"{base_path}/test/exam.html",
            })
            for qtype in ["answer", "blank", "apply"]:
                for q in part_questions(stage, part, qtype, 10):
                    item = {
                        "id": q["id"],
                        "stageId": sid,
                        "partId": pid,
                        "type": qtype,
                        "level": q["level"],
                        "levelLabel": q["levelLabel"],
                        "source": q["source"],
                        "question": q["question"],
                        "explanation": q["answer"],
                    }
                    if qtype == "blank":
                        item["answer"] = q["answer"]
                    elif qtype == "apply":
                        item["choices"] = q["choices"]
                        item["answer"] = q["answer"]
                    else:
                        item["answer"] = q["answer"]
                    questions.append(item)
    return {"stages": stages, "parts": parts, "questions": questions}


def exam_directory_html() -> str:
    groups = []
    for stage in STAGES:
        cards = []
        for part in stage["parts"]:
            base_path = f"../stages/{stage['num']}. {stage['name']}/{part_folder(part)}"
            cards.append(f"""
            <article class="exam-card exam-directory-card">
              <p class="exam-kicker">{html.escape(stage_title(stage))}</p>
              <h3>{html.escape(part['num'] + ' ' + part['name'])}</h3>
              <p>{html.escape(part['summary'])} This exam has 30 problems across 10 levels.</p>
              <div class="exam-actions exam-actions--single">
                <a href="{html.escape(base_path + '/test/exam.html', quote=True)}" target="_blank" rel="noopener">Open Exam</a>
              </div>
            </article>
            """)
        groups.append(f"""
        <details class="exam-stage-group" open>
          <summary>{html.escape(stage_title(stage))} - {len(stage['parts'])} part exams</summary>
          <div class="exam-directory-grid">
            {''.join(cards)}
          </div>
        </details>
        """)
    return f"""
    <section class="exam-directory" aria-labelledby="part-exam-directory">
      <h2 id="part-exam-directory">Part Exam Directory</h2>
      <p>Open any part exam directly. Every part has one standalone HTML exam with 30 levelled problems.</p>
      {''.join(groups)}
    </section>
    """


def exam_page() -> str:
    return dedent(f"""
    # Exam

    {exam_app_html("../assets", heading="Exam Center", subtitle="Select a stage, part, and question type. A full part exam uses 30 levelled problems: 10 answer, 10 blank, and 10 apply.", directory=exam_directory_html())}
    """)


def exam_js() -> str:
    return dedent("""
    (function () {
      const data = window.ROADMAP_EXAM_DATA;
      const app = document.getElementById("exam-app");
      if (!app || !data) return;

      const stageSelect = document.getElementById("exam-stage");
      const partSelect = document.getElementById("exam-part");
      const typeSelect = document.getElementById("exam-type");
      const countSelect = document.getElementById("exam-count");
      const startBtn = document.getElementById("exam-start");
      const questionBox = document.getElementById("exam-question");
      const reviewBox = document.getElementById("exam-review");
      const overviewBox = document.getElementById("exam-overview");
      const bar = document.getElementById("exam-progress-bar");
      const progressText = document.getElementById("exam-progress-text");
      const totalStat = document.getElementById("exam-total");
      const doneStat = document.getElementById("exam-done");
      const scoreStat = document.getElementById("exam-score");
      const title = document.getElementById("exam-title");
      const subtitle = document.getElementById("exam-subtitle");
      const fixedPartId = app.dataset.fixedPart || "";
      const typeOrder = { answer: 1, blank: 2, apply: 3 };
      const typeLabels = {
        answer: "Answer the question",
        blank: "Fill in the blank",
        apply: "Apply the concept",
      };

      let active = [];
      let index = 0;
      let answers = {};

      function option(value, label) {
        const el = document.createElement("option");
        el.value = value;
        el.textContent = label;
        return el;
      }

      function fillFilters() {
        stageSelect.appendChild(option("all", "All stages"));
        data.stages.forEach(stage => stageSelect.appendChild(option(stage.id, stage.title)));
        typeSelect.appendChild(option("all", "All question types"));
        typeSelect.appendChild(option("answer", "Answer the question"));
        typeSelect.appendChild(option("blank", "Fill in the blank"));
        typeSelect.appendChild(option("apply", "Apply the concept"));
        updateParts();
        if (fixedPartId) {
          const part = data.parts.find(p => p.id === fixedPartId);
          if (part) {
            stageSelect.value = part.stageId;
            updateParts();
            partSelect.value = fixedPartId;
            stageSelect.disabled = true;
            partSelect.disabled = true;
            countSelect.value = "30";
            app.classList.add("exam-app--fixed");
            if (title) title.textContent = app.dataset.heading || `${part.title} Exam`;
            if (subtitle) subtitle.textContent = app.dataset.subtitle || "30 levelled problems: 10 answer, 10 blank, and 10 apply.";
          }
        }
      }

      function updateParts() {
        partSelect.innerHTML = "";
        partSelect.appendChild(option("all", "All parts"));
        const stageId = stageSelect.value;
        data.parts
          .filter(part => stageId === "all" || part.stageId === stageId)
          .forEach(part => partSelect.appendChild(option(part.id, part.title)));
      }

      function filteredQuestions() {
        const fixedPart = fixedPartId ? data.parts.find(p => p.id === fixedPartId) : null;
        const stageId = fixedPart ? fixedPart.stageId : stageSelect.value;
        const partId = fixedPart ? fixedPart.id : partSelect.value;
        const type = typeSelect.value;
        let pool = data.questions.filter(q => {
          return (stageId === "all" || q.stageId === stageId)
            && (partId === "all" || q.partId === partId)
            && (type === "all" || q.type === type);
        });
        pool = pool.sort((a, b) => {
          if (a.partId !== b.partId) return a.partId.localeCompare(b.partId);
          if (typeOrder[a.type] !== typeOrder[b.type]) return typeOrder[a.type] - typeOrder[b.type];
          return a.level - b.level;
        });
        if (partId !== "all") return pool;
        return pool.slice(0, Number(countSelect.value));
      }

      function updateProgress() {
        const total = active.length || 1;
        const done = Object.keys(answers).length;
        const autoTotal = active.filter(q => q.type !== "answer").length;
        const autoCorrect = Object.values(answers).filter(a => a.correct === true).length;
        bar.style.width = Math.round((done / total) * 100) + "%";
        totalStat.textContent = active.length;
        doneStat.textContent = done;
        scoreStat.textContent = autoTotal ? `${autoCorrect}/${autoTotal}` : "review";
        progressText.textContent = active.length
          ? `${done} of ${active.length} answered · auto score ${autoTotal ? `${autoCorrect}/${autoTotal}` : "open review"}`
          : "Choose filters and start.";
      }

      function renderOverview() {
        if (!overviewBox) return;
        overviewBox.innerHTML = active.map((q, i) => {
          const state = answers[q.id] ? " answered" : "";
          const current = i === index ? " active" : "";
          return `<button type="button" class="exam-step${state}${current}" data-step="${i}"><span>${i + 1}</span><small>L${q.level}</small></button>`;
        }).join("");
        overviewBox.querySelectorAll("[data-step]").forEach(btn => {
          btn.addEventListener("click", () => {
            index = Number(btn.getAttribute("data-step"));
            renderQuestion();
          });
        });
      }

      function renderQuestion() {
        reviewBox.innerHTML = "";
        updateProgress();
        renderOverview();
        if (!active.length) {
          questionBox.innerHTML = "<div class='exam-empty'>No questions match these filters.</div>";
          if (overviewBox) overviewBox.innerHTML = "";
          return;
        }
        const q = active[index];
        const answered = answers[q.id];
        const part = data.parts.find(p => p.id === q.partId);
        let body = "";
        if (q.type === "answer") {
          const value = answered ? answered.value : "";
          body = `<textarea class="exam-textarea" id="exam-open-answer" rows="7" placeholder="Write a complete answer before checking the guide.">${escapeHtml(value || "")}</textarea>`;
        } else if (q.type === "blank") {
          const value = answered ? answered.value : "";
          body = `<input class="exam-input" id="blank-answer" value="${escapeHtml(value || "")}" placeholder="Type the missing term">`;
        } else {
          body = q.choices.map(choice => {
            const selected = answered && answered.value === choice ? " selected" : "";
            return `<button type="button" class="exam-choice${selected}" data-choice="${escapeHtml(choice)}">${escapeHtml(choice)}</button>`;
          }).join("");
        }
        questionBox.innerHTML = `
          <article class="exam-card exam-card--active modern-question">
            <div class="question-meta">
              <span class="level-chip">Level ${q.level}: ${escapeHtml(q.levelLabel)}</span>
              <span>${escapeHtml(typeLabels[q.type])} · ${escapeHtml(part ? part.title : "")}</span>
            </div>
            <h3>${index + 1}. ${escapeHtml(q.question)}</h3>
            <p class="exam-source">${escapeHtml(q.source || "")}</p>
            <div class="exam-choice-list">${body}</div>
            <div class="exam-actions">
              <button type="button" id="exam-check">Check</button>
              <button type="button" id="exam-prev">Previous</button>
              <button type="button" id="exam-next">Next</button>
              <button type="button" id="exam-finish">Finish</button>
            </div>
            <div id="exam-feedback" class="exam-feedback">${answered ? feedbackHtml(q, answered) : ""}</div>
          </article>`;
        questionBox.querySelectorAll("[data-choice]").forEach(btn => {
          btn.addEventListener("click", () => {
            questionBox.querySelectorAll(".exam-choice").forEach(b => b.classList.remove("selected"));
            btn.classList.add("selected");
          });
        });
        document.getElementById("exam-check").addEventListener("click", checkAnswer);
        document.getElementById("exam-prev").addEventListener("click", () => { index = Math.max(0, index - 1); renderQuestion(); });
        document.getElementById("exam-next").addEventListener("click", () => { index = Math.min(active.length - 1, index + 1); renderQuestion(); });
        document.getElementById("exam-finish").addEventListener("click", finish);
      }

      function checkAnswer() {
        const q = active[index];
        let value = "";
        if (q.type === "answer") {
          value = document.getElementById("exam-open-answer").value.trim();
        } else if (q.type === "blank") {
          value = document.getElementById("blank-answer").value.trim();
        } else {
          const selected = questionBox.querySelector(".exam-choice.selected");
          value = selected ? selected.getAttribute("data-choice") : "";
        }
        if (!value) return;
        let correct = null;
        if (q.type === "blank") {
          correct = normalize(value) === normalize(q.answer);
        } else if (q.type === "apply") {
          correct = value === q.answer;
        }
        answers[q.id] = { value, correct };
        document.getElementById("exam-feedback").innerHTML = feedbackHtml(q, answers[q.id]);
        updateProgress();
        renderOverview();
        localStorage.setItem("modern-ai-engineer-exam-last", JSON.stringify({ filters: [stageSelect.value, partSelect.value, typeSelect.value], answers }));
      }

      function feedbackHtml(q, answered) {
        if (q.type === "answer") {
          return `<div class="is-review"><strong>Guide.</strong> ${escapeHtml(q.explanation)}</div>`;
        }
        const status = answered.correct ? "Correct" : "Review";
        const klass = answered.correct ? "is-correct" : "is-review";
        return `<div class="${klass}"><strong>${status}.</strong> ${escapeHtml(q.explanation)}</div>`;
      }

      function finish() {
        const total = active.length;
        const done = Object.keys(answers).length;
        const autoTotal = active.filter(q => q.type !== "answer").length;
        const correct = Object.values(answers).filter(a => a.correct === true).length;
        questionBox.innerHTML = "";
        reviewBox.innerHTML = `
          <article class="exam-card exam-card--active exam-result-card">
            <p class="exam-kicker">Result</p>
            <h3>${done} of ${total} answered</h3>
            <p>Auto-scored result: ${correct} of ${autoTotal}. Open answers are guide-reviewed, so compare them carefully before moving on.</p>
            <div class="exam-review-list">
              ${active.map((q, i) => {
                const a = answers[q.id];
                const status = a && a.correct === true ? "correct" : "review";
                const marker = q.type === "answer" ? "Open review" : (a && a.correct ? "Correct" : "Review");
                return `<div class="exam-review-item ${status}"><strong>${i + 1}. Level ${q.level} · ${marker}</strong><br>${escapeHtml(q.question)}<br><span>${escapeHtml(q.explanation)}</span></div>`;
              }).join("")}
            </div>
          </article>`;
        bar.style.width = "100%";
        progressText.textContent = `${done} of ${total} answered · auto score ${correct}/${autoTotal}`;
        doneStat.textContent = done;
        scoreStat.textContent = `${correct}/${autoTotal}`;
      }

      function normalize(value) {
        return String(value || "").trim().toLowerCase().replace(/\\s+/g, " ");
      }

      function escapeHtml(value) {
        return String(value).replace(/[&<>"']/g, ch => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;" }[ch]));
      }

      stageSelect.addEventListener("change", updateParts);
      startBtn.addEventListener("click", () => {
        active = filteredQuestions();
        index = 0;
        answers = {};
        renderQuestion();
      });

      fillFilters();
      const params = new URLSearchParams(window.location.search);
      const partParam = params.get("part");
      if (partParam && data.parts.some(p => p.id === partParam)) {
        const part = data.parts.find(p => p.id === partParam);
        stageSelect.value = part.stageId;
        updateParts();
        partSelect.value = partParam;
        active = filteredQuestions();
        renderQuestion();
      } else if (fixedPartId) {
        active = filteredQuestions();
        renderQuestion();
      }
    })();
    """)


def home_index() -> str:
    rows = [f"| {s['num']} | {link(stage_title(s), stage_path(s))} | {s['tagline']} | {s['artifact']} |" for s in STAGES]
    return dedent(f"""
    # Modern AI Engineer Roadmap

    <div class="roadmap-hero" markdown="1">
    <img class="roadmap-hero__avatar" src="assets/images/avatar.png" alt="Modern AI Engineer Roadmap avatar">
    <p class="roadmap-hero__title">From first principles to production AI systems.</p>
    <p class="roadmap-hero__meta">A complete beginner-to-master architecture for AI engineering: foundations, ML, deep learning, LLMs, AI applications, agents, model infrastructure, optimization, hardware acceleration, security, blockchain, ZKML, and capstone mastery.</p>
    </div>

    ## Reference Synthesis

    {bullet(REFERENCE_SYNTHESIS)}

    ## Main Path

    | # | Stage | Simple purpose | Stage artifact |
    |---:|---|---|---|
    {chr(10).join(rows)}

    ## How the Architecture Works

    Stages do not all have the same number of parts. Parts do not all have the same number of sub-parts. The structure follows the learning topic. Every sub-part is a folder with an overview, deep dive, and examples/practice page.

    ## Start Here

    1. Read [How to Use](how-to-use.md).
    2. Open the [Roadmap Map](roadmap-map.md).
    3. Start Stage 0 unless you can already pass its exit criteria.
    4. Use the [Exam](exam/index.md) tab after studying each part.
    """)


def how_to_use() -> str:
    return dedent("""
    # How to Use This Roadmap

    ## The Rule

    Do not try to finish every resource before building. Learn just enough to build the next artifact, then use the artifact to reveal what you do not understand.

    ## Structure

    | Level | Meaning |
    |---|---|
    | Stage | A major skill area with a stage artifact and exit criteria |
    | Part | A folder inside the stage that explains one major capability |
    | Sub-part folder | A folder with an overview, deep dive, and examples/practice page |
    | Exam | One 30-question HTML exam per part plus one global Exam UI |

    The part and sub-part counts vary because the topics vary. A learner should not see the same artificial pattern everywhere.

    ## Weekly Study Loop

    1. Pick the current part.
    2. Study each sub-part folder.
    3. Build the smallest artifact connected to the part.
    4. Measure one thing.
    5. Take the local part exam or use the global [Exam](exam/index.md) tab.

    ## First 30 Days

    | Week | Focus | Output |
    |---|---|---|
    | 1 | Orientation, tooling, Git, Python environment | learning log and setup notes |
    | 2 | Python data stack and math refresh | small data analysis repo |
    | 3 | ML baseline and evaluation | model report with error analysis |
    | 4 | LLM basics and prompt tests | tokenizer, prompt, and model comparison notebook |
    """)


def roadmap_map() -> str:
    nodes = []
    links = []
    rows = []
    for stage in STAGES:
        nodes.append(f'  S{stage["num"]}["{stage["num"]}. {stage["name"]}<br/>{stage["tagline"]}"]')
        part_names = ", ".join(part["name"] for part in stage["parts"])
        rows.append(f"| {link(stage_title(stage), stage_path(stage))} | {len(stage['parts'])} | {part_names} |")
    for current, nxt in zip(STAGES, STAGES[1:]):
        links.append(f"  S{current['num']} --> S{nxt['num']}")
    return dedent(f"""
    # Roadmap Map

    ## Main Path

    ```mermaid
    flowchart TD
    {chr(10).join(nodes)}

    {chr(10).join(links)}
      S5 --> S7
      S6 --> S9
      S8 --> S10
    ```

    ## Stage Structure

    | Stage | Part count | Parts |
    |---|---:|---|
    {chr(10).join(rows)}
    """)


def project_ladder() -> str:
    rows = [f"| {s['num']} | {s['name']} | {s['artifact']} | {s['tagline']} |" for s in STAGES]
    return dedent(f"""
    # Project Ladder

    Projects are the spine of the roadmap. Each one should be small enough to finish, but real enough to show what you learned.

    | # | Stage | Project | What it proves |
    |---:|---|---|---|
    {chr(10).join(rows)}
    """)


def readme() -> str:
    return dedent("""
    # Modern AI Engineer Roadmap

    Beginner-to-master roadmap for becoming a modern AI engineer: AI and ML fundamentals, deep learning, LLMs, RAG, agents, model infrastructure, optimization, hardware acceleration, AI security, blockchain, ZKML, and capstone mastery.

    ## Architecture

    - Variable part counts by stage.
    - Variable sub-part counts by part.
    - Every sub-part is a folder with `index.md`, `deep-dive.md`, and `examples-and-practice.md`.
    - Every part has one local 30-question HTML exam.
    - The top-level Exam tab provides direct testing across all stages and parts.

    ## Local Preview

    ```bash
    python -m pip install -r requirements.txt
    mkdocs serve
    ```
    """)


def custom_css() -> str:
    return dedent("""
    :root {
      --md-grid-width: 96vw;
      --roadmap-teal: #0f766e;
      --roadmap-teal-dark: #0b5f58;
      --roadmap-ink: #1d2a24;
      --roadmap-muted: #5d6d66;
      --roadmap-line: rgba(15, 118, 110, 0.22);
      --roadmap-soft: #f2fbf9;
      --roadmap-gold: #f59e0b;
    }

    .md-grid {
      max-width: 96vw;
    }

    .md-main__inner {
      column-gap: clamp(0.75rem, 1.4vw, 1.25rem);
      margin-left: clamp(0.5rem, 1vw, 1rem);
      margin-right: clamp(0.5rem, 1vw, 1rem);
    }

    .md-content {
      flex: 1 1 auto;
      max-width: none;
      min-width: 0;
    }

    .md-content__inner {
      margin-left: clamp(0.5rem, 1vw, 1.2rem);
      margin-right: clamp(0.5rem, 1vw, 1.2rem);
    }

    @media (min-width: 76.25em) {
      .md-sidebar--primary {
        width: clamp(10.5rem, 12vw, 13rem);
      }

      .md-sidebar--secondary {
        width: clamp(9.5rem, 10vw, 11.5rem);
      }
    }

    .md-typeset h1,
    .md-typeset h2,
    .md-typeset h3 { letter-spacing: 0; }

    .roadmap-diagram {
      width: 100%;
      margin: 1rem 0 1.25rem;
      border: 1px solid var(--roadmap-line);
      border-radius: 8px;
      padding: 1rem;
      background: var(--roadmap-soft);
      overflow-x: auto;
    }

    .md-typeset .roadmap-diagram .mermaid {
      min-width: 56rem;
      text-align: center;
    }

    .md-typeset .roadmap-diagram--part .mermaid {
      min-width: 62rem;
    }

    .md-typeset .roadmap-diagram .mermaid svg {
      width: 100% !important;
      max-width: none !important;
      height: auto !important;
    }

    .md-typeset .roadmap-diagram .mermaid text {
      font-size: 17px !important;
    }

    .md-header__button.md-logo img,
    .md-header__button.md-logo svg {
      width: 2.15rem;
      height: 2.15rem;
      border-radius: 6px;
      object-fit: contain;
    }

    .roadmap-hero,
    .exam-hero {
      border: 1px solid var(--roadmap-line);
      border-radius: 8px;
      padding: 1.25rem;
      background: linear-gradient(135deg, rgba(15, 118, 110, 0.10), rgba(245, 158, 11, 0.10));
    }

    .roadmap-hero__avatar {
      float: right;
      width: clamp(5rem, 18vw, 7.5rem);
      height: clamp(5rem, 18vw, 7.5rem);
      margin: 0 0 0.75rem 1rem;
      border-radius: 8px;
    }

    .roadmap-hero__title {
      margin: 0;
      font-size: 1.75rem;
      line-height: 1.18;
    }

    .stage-badge {
      display: inline-block;
      min-width: 2.25rem;
      padding: 0.1rem 0.45rem;
      border-radius: 6px;
      color: #fff;
      background: var(--roadmap-teal);
      font-weight: 700;
      text-align: center;
    }

    .exam-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 0.55rem;
      margin: 1rem 0;
      max-width: 100%;
    }

    .md-typeset .exam-actions p {
      display: contents;
      margin: 0;
    }

    .exam-actions--part {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 12.5rem), 1fr));
    }

    .exam-actions--single {
      display: flex;
    }

    .exam-actions--single a {
      width: fit-content;
      min-width: min(100%, 12rem);
    }

    .exam-actions--compact {
      align-items: center;
    }

    .exam-actions a,
    .exam-actions button,
    .exam-secondary,
    .exam-filterbar button,
    #exam-start,
    #exam-check,
    #exam-prev,
    #exam-next,
    #exam-finish {
      border: 0;
      border-radius: 6px;
      padding: 0.62rem 0.9rem;
      color: #fff;
      background: var(--roadmap-teal);
      font-weight: 700;
      text-decoration: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      max-width: 100%;
      min-width: 0;
      line-height: 1.25;
      overflow-wrap: anywhere;
      text-align: center;
      white-space: normal;
    }

    .exam-actions a:hover,
    .exam-actions button:hover,
    .exam-secondary:hover,
    .exam-filterbar button:hover,
    #exam-start:hover,
    #exam-check:hover,
    #exam-prev:hover,
    #exam-next:hover,
    #exam-finish:hover {
      background: var(--roadmap-teal-dark);
    }

    .exam-shell {
      display: grid;
      gap: 1rem;
    }

    .exam-app {
      container-type: inline-size;
    }

    .exam-hero--modern {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
    }

    .exam-hero--modern h2 {
      margin: 0.1rem 0 0.35rem;
      font-size: clamp(1.45rem, 2vw, 2rem);
      line-height: 1.15;
    }

    .exam-hero--modern p {
      max-width: 58rem;
    }

    .exam-summary-card {
      flex: 0 0 auto;
      min-width: 8.5rem;
      border: 1px solid var(--roadmap-line);
      border-radius: 8px;
      padding: 0.9rem;
      background: var(--md-default-bg-color);
      text-align: center;
    }

    .exam-summary-card strong {
      display: block;
      color: var(--roadmap-teal);
      font-size: 2rem;
      line-height: 1;
    }

    .exam-summary-card span {
      color: var(--roadmap-muted);
      font-size: 0.78rem;
      font-weight: 800;
      text-transform: uppercase;
    }

    .exam-panel,
    .exam-card,
    .exam-question,
    .exam-review {
      border: 1px solid var(--roadmap-line);
      border-radius: 8px;
      padding: 1rem;
      background: var(--md-default-bg-color);
    }

    .exam-config {
      padding: 0.85rem;
    }

    .exam-app--fixed #exam-stage-label,
    .exam-app--fixed #exam-part-label {
      display: none;
    }

    .exam-controls {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(11rem, 1fr));
      gap: 0.75rem;
      align-items: end;
    }

    .exam-controls label {
      display: grid;
      gap: 0.25rem;
      color: var(--roadmap-muted);
      font-size: 0.82rem;
      font-weight: 700;
    }

    .exam-controls select,
    .exam-input {
      width: 100%;
      border: 1px solid var(--roadmap-line);
      border-radius: 6px;
      padding: 0.62rem;
      color: var(--md-default-fg-color);
      background: var(--md-default-bg-color);
    }

    .exam-progress {
      height: 0.65rem;
      border-radius: 999px;
      background: rgba(15, 118, 110, 0.16);
      overflow: hidden;
    }

    .exam-progress span {
      display: block;
      width: 0;
      height: 100%;
      background: var(--roadmap-teal);
      transition: width 160ms ease;
    }

    .exam-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 0.8rem;
      margin-top: 1rem;
    }

    .exam-status-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 0.75rem;
    }

    .exam-overview {
      display: flex;
      flex-wrap: wrap;
      gap: 0.35rem;
      border: 1px solid var(--roadmap-line);
      border-radius: 8px;
      padding: 0.65rem;
      background: var(--md-default-bg-color);
    }

    .exam-overview:empty {
      display: none;
    }

    .exam-step {
      width: 2.6rem;
      min-height: 2.5rem;
      border: 1px solid var(--roadmap-line);
      border-radius: 6px;
      color: var(--md-default-fg-color);
      background: rgba(15, 118, 110, 0.04);
      cursor: pointer;
    }

    .exam-step span,
    .exam-step small {
      display: block;
      line-height: 1.05;
    }

    .exam-step span {
      font-weight: 800;
    }

    .exam-step small {
      color: var(--roadmap-muted);
      font-size: 0.68rem;
    }

    .exam-step.active {
      border-color: var(--roadmap-teal);
      background: rgba(15, 118, 110, 0.14);
      box-shadow: 0 0 0 3px rgba(15, 118, 110, 0.14);
    }

    .exam-step.answered span {
      color: var(--roadmap-teal);
    }

    .exam-directory {
      margin-top: 1.5rem;
    }

    .exam-stage-group {
      border: 1px solid var(--roadmap-line);
      border-radius: 8px;
      margin: 0.8rem 0;
      padding: 0.75rem 1rem;
      background: var(--md-default-bg-color);
    }

    .exam-stage-group > summary {
      color: var(--md-default-fg-color);
      cursor: pointer;
      font-weight: 800;
    }

    .exam-directory-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
      gap: 0.8rem;
      margin-top: 0.8rem;
    }

    .exam-directory-card h3 {
      margin: 0.2rem 0 0.35rem;
      font-size: 1rem;
      line-height: 1.25;
    }

    .exam-directory-card p {
      margin: 0.35rem 0;
      color: var(--roadmap-muted);
      font-size: 0.85rem;
    }

    .exam-card {
      border-left: 4px solid var(--roadmap-teal);
    }

    .exam-card--active {
      border-left-width: 6px;
    }

    .exam-kicker {
      margin: 0 0 0.25rem;
      color: var(--roadmap-teal);
      font-size: 0.78rem;
      font-weight: 800;
      text-transform: uppercase;
    }

    .exam-choice-list {
      display: grid;
      gap: 0.55rem;
      margin: 1rem 0;
    }

    .exam-choice {
      border: 1px solid var(--roadmap-line);
      border-radius: 6px;
      padding: 0.75rem;
      color: var(--md-default-fg-color);
      background: rgba(15, 118, 110, 0.04);
      text-align: left;
      cursor: pointer;
    }

    .exam-choice.selected {
      outline: 3px solid rgba(15, 118, 110, 0.28);
      background: rgba(15, 118, 110, 0.12);
    }

    .modern-question h3 {
      margin: 0.65rem 0 0.4rem;
      font-size: 1.15rem;
      line-height: 1.35;
    }

    .level-chip {
      display: inline-flex;
      align-items: center;
      width: fit-content;
      border-radius: 999px;
      padding: 0.18rem 0.55rem;
      color: #fff;
      background: var(--roadmap-teal);
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
    }

    .exam-source {
      border-left: 3px solid var(--roadmap-line);
      margin: 0.6rem 0 0.9rem;
      padding-left: 0.75rem;
      color: var(--roadmap-muted);
      font-size: 0.84rem;
    }

    .exam-stat-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(9rem, 1fr));
      gap: 0.75rem;
      margin: 1rem 0;
    }

    .exam-stat {
      border: 1px solid var(--roadmap-line);
      border-radius: 8px;
      padding: 0.85rem;
      background: var(--md-default-bg-color);
    }

    .exam-stat strong {
      display: block;
      color: var(--roadmap-teal);
      font-size: 1.45rem;
      line-height: 1;
    }

    .exam-stat span {
      color: var(--roadmap-muted);
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
    }

    .exam-filterbar {
      display: flex;
      flex-wrap: wrap;
      gap: 0.55rem;
      margin: 1rem 0;
    }

    .exam-filterbar button.active {
      background: var(--roadmap-teal-dark);
      box-shadow: 0 0 0 3px rgba(15, 118, 110, 0.18);
    }

    .standalone-progress {
      margin: 0.75rem 0 1rem;
    }

    .standalone-question-grid {
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 22rem), 1fr));
    }

    .standalone-question h2 {
      margin: 0.45rem 0;
      font-size: 1rem;
      line-height: 1.35;
    }

    .question-meta,
    .exam-question-footer {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 0.6rem;
    }

    .question-meta {
      justify-content: space-between;
      color: var(--roadmap-muted);
      font-size: 0.78rem;
      font-weight: 800;
      text-transform: uppercase;
    }

    .question-support {
      color: var(--roadmap-muted);
      font-size: 0.84rem;
    }

    .exam-complete {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      text-transform: none;
    }

    .exam-textarea {
      width: 100%;
      min-height: 7rem;
      border: 1px solid var(--roadmap-line);
      border-radius: 6px;
      padding: 0.75rem;
      color: var(--md-default-fg-color);
      background: var(--md-default-bg-color);
      resize: vertical;
    }

    .exam-guide {
      margin-top: 0.75rem;
    }

    .exam-guide summary {
      color: var(--roadmap-teal);
      cursor: pointer;
      font-weight: 800;
    }

    .exam-result {
      color: var(--roadmap-muted);
      font-weight: 800;
    }

    .standalone-question.is-correct {
      box-shadow: inset 0 0 0 2px rgba(15, 118, 110, 0.24);
    }

    .standalone-question.is-review {
      box-shadow: inset 0 0 0 2px rgba(245, 158, 11, 0.30);
    }

    .exam-feedback .is-correct,
    .exam-review-item.correct {
      border-left: 4px solid var(--roadmap-teal);
      padding: 0.7rem;
      background: rgba(15, 118, 110, 0.10);
    }

    .exam-feedback .is-review,
    .exam-review-item.review {
      border-left: 4px solid var(--roadmap-gold);
      padding: 0.7rem;
      background: rgba(245, 158, 11, 0.10);
    }

    .standalone-exam {
      margin: 0;
      font-family: system-ui, -apple-system, Segoe UI, sans-serif;
      line-height: 1.55;
      background: #f6fbfa;
      color: var(--roadmap-ink);
    }

    .standalone-exam__main {
      max-width: 1180px;
      margin: 0 auto;
      padding: 1.25rem;
    }

    .md-typeset table:not([class]) { font-size: 0.78rem; }

    @media (max-width: 40rem) {
      .roadmap-hero__avatar {
        float: none;
        display: block;
        margin: 0 0 0.9rem;
      }

      .exam-hero--modern,
      .exam-status-grid {
        grid-template-columns: 1fr;
        display: grid;
      }

      .exam-summary-card {
        text-align: left;
      }
    }
    """)


def q(text: str) -> str:
    return '"' + text.replace('"', '\\"') + '"'


def mkdocs_yml() -> str:
    lines = [
        "site_name: Modern AI Engineer Roadmap",
        "site_url: https://aiZKP.github.io/modern-ai-engineer-roadmap/",
        "site_description: A beginner-to-master roadmap for modern AI engineering.",
        "site_author: aiZKP",
        "repo_url: https://github.com/aiZKP/modern-ai-engineer-roadmap",
        "repo_name: aiZKP/modern-ai-engineer-roadmap",
        "edit_uri: edit/main/docs/",
        "",
        "docs_dir: docs",
        "",
        "theme:",
        "  name: material",
        "  logo: assets/images/avatar.png",
        "  favicon: assets/images/avatar.png",
        "  palette:",
        '    - media: "(prefers-color-scheme: light)"',
        "      scheme: default",
        "      primary: teal",
        "      accent: amber",
        "      toggle:",
        "        icon: material/brightness-7",
        "        name: Switch to dark mode",
        '    - media: "(prefers-color-scheme: dark)"',
        "      scheme: slate",
        "      primary: teal",
        "      accent: amber",
        "      toggle:",
        "        icon: material/brightness-4",
        "        name: Switch to light mode",
        "  font: false",
        "  features:",
        "    - navigation.tabs",
        "    - navigation.indexes",
        "    - navigation.top",
        "    - navigation.footer",
        "    - search.suggest",
        "    - search.highlight",
        "    - content.code.copy",
        "    - toc.follow",
        "  icon:",
        "    repo: fontawesome/brands/github",
        "",
        "markdown_extensions:",
        "  - admonition",
        "  - attr_list",
        "  - def_list",
        "  - footnotes",
        "  - md_in_html",
        "  - tables",
        "  - pymdownx.details",
        "  - pymdownx.superfences:",
        "      custom_fences:",
        "        - name: mermaid",
        "          class: mermaid",
        "          format: !!python/name:pymdownx.superfences.fence_code_format",
        "  - pymdownx.highlight:",
        "      anchor_linenums: true",
        "      pygments_lang_class: true",
        "  - pymdownx.inlinehilite",
        "  - pymdownx.snippets",
        "  - pymdownx.tasklist:",
        "      custom_checkbox: true",
        "  - toc:",
        "      permalink: true",
        "      toc_depth: 3",
        "",
        "plugins:",
        "  - search",
        "",
        "extra_css:",
        "  - assets/css/custom.css",
        "",
        "nav:",
        "  - Home:",
        "    - Overview: index.md",
        "    - How to Use: how-to-use.md",
        "    - Roadmap Map: roadmap-map.md",
        "  - Stages:",
    ]
    for stage in STAGES:
        lines.append(f"    - {q(str(stage['num']) + '. ' + stage['name'])}:")
        lines.append(f"      - Overview: {q(stage_path(stage))}")
        for part in stage["parts"]:
            base = f"stages/{stage['num']}. {stage['name']}/{part_folder(part)}"
            lines.append(f"      - {q(part['num'] + ' ' + part['name'])}:")
            lines.append(f"        - Overview: {q(base + '/index.md')}")
            for idx, sub in enumerate(part["subparts"], 1):
                sbase = f"{base}/{sub_folder(part, idx, sub)}"
                lines.append(f"        - {q(sub_code(part, idx) + ' ' + sub)}:")
                lines.append(f"          - Overview: {q(sbase + '/index.md')}")
                lines.append(f"          - Deep Dive: {q(sbase + '/deep-dive.md')}")
                lines.append(f"          - Examples and Practice: {q(sbase + '/examples-and-practice.md')}")
    lines.extend([
        "  - Exam:",
        "    - Exam Dashboard: exam/index.md",
        "  - Projects:",
        "    - Project Ladder: projects/project-ladder.md",
        "",
    ])
    return "\n".join(lines)


def regenerate() -> None:
    if STAGES_DIR.exists():
        shutil.rmtree(STAGES_DIR)
    STAGES_DIR.mkdir(parents=True, exist_ok=True)

    for sidx, stage in enumerate(STAGES):
        sdir = stage_dir(stage)
        write(sdir / "index.md", stage_index(stage, sidx))
        for part in stage["parts"]:
            pdir = part_dir(sdir, part)
            write(pdir / "index.md", part_index(stage, part))
            for idx, sub in enumerate(part["subparts"], 1):
                sd = sub_dir(pdir, part, idx, sub)
                write(sd / "index.md", sub_index(stage, part, idx, sub))
                write(sd / "deep-dive.md", deep_dive(stage, part, idx, sub))
                write(sd / "examples-and-practice.md", examples_practice(stage, part, idx, sub))
            tdir = pdir / "test"
            write(tdir / "exam.html", part_exam_html(stage, part))

    write(DOCS / "index.md", home_index())
    write(DOCS / "how-to-use.md", how_to_use())
    write(DOCS / "roadmap-map.md", roadmap_map())
    write(DOCS / "projects" / "project-ladder.md", project_ladder())
    write(DOCS / "exam" / "index.md", exam_page())
    write(DOCS / "assets" / "css" / "custom.css", custom_css())
    write(DOCS / "assets" / "js" / "exam-data.js", "window.ROADMAP_EXAM_DATA = " + json.dumps(exam_data(), indent=2) + ";\n")
    write(DOCS / "assets" / "js" / "exam-ui.js", exam_js())
    write(ROOT / "README.md", readme())
    write(ROOT / "mkdocs.yml", mkdocs_yml())

    for rel in ["llms.txt", "meta", "resources", "tracks"]:
        path = DOCS / rel
        if path.is_dir():
            shutil.rmtree(path)
        elif path.exists():
            path.unlink()

    print(f"stages: {len(STAGES)}")
    print(f"parts: {sum(len(s['parts']) for s in STAGES)}")
    print(f"subparts: {sum(len(p['subparts']) for s in STAGES for p in s['parts'])}")
    print(f"subpart md files: {sum(len(p['subparts']) for s in STAGES for p in s['parts']) * 3}")
    print(f"part test files: {sum(len(s['parts']) for s in STAGES)}")
    print(f"exam questions: {len(exam_data()['questions'])}")


if __name__ == "__main__":
    regenerate()
