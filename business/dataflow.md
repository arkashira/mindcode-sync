 # Context
Product: mindcode-sync
Repo: https://github.com/arkashira/mindcode-sync
Hypothesis: A tool that assists developers in high-level thinking and provides accurate low-level implementation, reducing errors and increasing productivity.
BD rationale: The pain point requires a tool that provides high-level thinking and accurate low-level implementation, which is not addressed by the current axentx product portfolio.
Market data:

- Total developers: 12,000,000
- Developers using AI tools: 2,000,000
- Developers facing high-level thinking challenges: 1,500,000
- Developers facing low-level implementation challenges: 1,200,000
- Developers facing both challenges: 1,000,000

# Task
Generate `dataflow.md`

## System Dataflow Architecture

### External Data Sources
- Developer code repositories (e.g., GitHub, GitLab)
- AI models (e.g., TensorFlow, PyTorch)
- Developer feedback and logs

### Ingestion Layer
- API Gateway
- Authentication and Authorization (OAuth, JWT)

### Processing/Transform Layer
- Code analysis engine (based on AI models)
- High-level thinking engine (based on AI models)
- Low-level implementation engine (based on AI models)
- Error detection and correction engine

### Storage Tier
- Code repository (for storing analyzed and corrected code)
- Feedback and log storage (for continuous improvement)

### Query/Serving Layer
- RESTful API for developers to interact with the system
- Real-time feedback and suggestions

### Egress to User
- Developer dashboards (web and mobile)
- Integration with IDEs (e.g., Visual Studio Code, IntelliJ IDEA)

```
                 +----------------+
                 | External Data  |
                 +---------------+
                           |
               +----------------+
               | Ingestion Layer |
               +----------------+
                           |
         +----------------+----------------+
         | Processing/Transform Layer | Storage Tier |
         +----------------+----------------+
                           |
               +----------------+----------------+
               | Query/Serving Layer | Egress to User |
               +----------------+----------------+
```