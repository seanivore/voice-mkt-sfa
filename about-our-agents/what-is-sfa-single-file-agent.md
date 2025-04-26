# Variable-Input Single File Agents (SFA)

## What is a SFA?

A SFA is a Python script that runs an AI agent (Claude) with a suite of tools to perform complex tasks through dynamic workflows. The agent can read/write files, analyze images, conduct web research, and make autonomous decisions to navigate multi-step processes.

What makes our implementation special is its variable-input architecture - complex prompts are broken down into simple categories that make it easy to define new workflows without changing the core agent code.

### Key Features

- **Dynamic Workflows**: Agents can create and adjust workflows as they work
- **Token-Aware**: Automatic token management prevents truncated outputs
- **Context Retention**: Same-context phase continuation for document revisions
- **Phase Summaries**: Detailed tracking of accomplishments and decisions
- **Tool-Rich Environment**: File operations, web search, image analysis, and more
- **Simple Setup**: Just describe your task, get a command to run it

## Quick Start

```bash
# Setup a new workflow (recommended)
sfa -s /path/to/your/config.json    # Generates workflow script and README

# Run workflows
sfa /path/to/your/config.json       # Run directly
sfa json                           # Use 'json' as shorthand for most recent config
```

## Workflow Control

The SFA supports dynamic workflow execution through labeled tasks in your configuration:

#### Task Labels
- `TASK_*`: Entry point tasks
- `DECISION_*`: Branching points based on agent decisions
- `REVIEW_TASK`: Review phase

#### Features
- **Dynamic Branching**: Workflows adapt based on agent decisions
- **Task Reports**: Automatic tracking of accomplishments and decisions
- **Smart Fallback**: Gracefully handles unmatched decisions by continuing to the next logical task

#### Example Structure
```json
{
  "workflow-name": {
    "TASK_INITIAL": [{...}],
    "DECISION_1": [{...}],
    "DECISION_2": [{...}],
    "REVIEW_TASK": [{...}]
  }
}
```

> **Tip**: Always use `sfa -s` when setting up a new workflow - it creates a helpful README and a convenient activation command in your use-case directory.

## Core Capabilities

### 1. Workflow Management
- Dynamic phase creation and adjustment
- Automatic token optimization
- Context-aware phase transitions
- Comprehensive phase summaries

### 2. File Operations
- Read/write/edit files
- Search and organize content
- Manage multiple outputs
- Token-safe document handling

### 3. Research & Analysis
- Web search integration
- Image analysis
- Advanced research via Perplexity AI
- Content synthesis

### 4. Decision Making
- Autonomous workflow branching
- Task planning and adjustment
- Progress tracking
- Result verification

## Example Use-Cases

1. Content Creation & Marketing
   - Research and write marketing copy
   - Create social media campaigns
   - Draft email sequences
   - Generate targeted content

2. Documentation & Analysis
   - Update technical documentation
   - Research and summarize topics
   - Create reports and presentations
   - Analyze and organize information

3. Job Application Materials
   - Create targeted resumes
   - Write compelling cover letters
   - Research companies
   - Customize applications

## Documentation

- [SFA Basics](./SFA_BASICS.md): Core concepts and architecture
- [Technical Specifications](./SPECIFICATIONS.md): Detailed implementation guide
- [Setup Protocol](./agent-workbench/protocol-guide/SETUP_PROTOCOL.md): Workflow creation guide

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/single-file-agents.git
cd single-file-agents

# Set up your environment
echo "ANTHROPIC_API_KEY=your_api_key_here" > .env
echo "BRAVE_API_KEY=your_api_key_here" > .env
echo "PERPLEXITY_API_KEY=your_api_key_here" > .env

# Install command-line tools
./install-sfa-commands.sh
```

## Project Structure

```plaintext
single-file-agents/
├── agent-workbench/          # Development resources
├── sfa_main.py              # Core agent implementation
├── setup-sfa-workflow.sh    # Workflow setup script
└── use-case/                # Example workflows
```

## Contributing

See [SPECIFICATIONS.md](./SPECIFICATIONS.md) for development guidelines.

## License

MIT License 

----

## Directory Content 

- **[About Section](../about-our-agents.md)**
  - [Technical Specifications](../about-our-agents/technical-specifications.md)
  - [What Is A Single-File Agent](../about-our-agents/what-is-sfa-single-file-agent.md)
  - [Workflow Feedback Job Resume Case Study](../about-our-agents/workflow-feedback-job-resume-case-study.md)
- **Case Studies**
  - [AI Agentic Brand Content Case Study](../ai-agentic-brand-content-case-study.md)
  - [Agentic Research Case Study](../ai-voice-marketing/agentic-research-planning-case-study.md)
- **Section Pages**
  - [AI Voice Marketing Research & Implementation Guide](../ai-voice-marketing.md)
  - [AI Voice Marketing Deep Research](../ai-voice-marketing/deep-research.md)
  - [AI Voice Marketing Writing Guide](../ai-voice-marketing/research-implementation/writing-guide.md)
  - [Top Conversion Strategies for AI Voice Marketing](../ai-voice-marketing/top-conversion-strategy.md)
- **[Index Pages](../ai-voice-marketing/index.md)**
  - [AI Voice Marketing Strategies by Tactic Type Index](../ai-voice-marketing/index/tactic-types.md)
  - [AI Voice Marketing Strategies by Name Index](../ai-voice-marketing/index/strategy-name.md)
  - [AI Voice Marketing Strategies by Vocal Characteristic Index](../ai-voice-marketing/index/vocal-characteristics.md)
  - [AI Voice Marketing Strategies by Influence and Lead Type Index](../ai-voice-marketing/index/influence-lead-type.md)
  - [AI Voice Marketing Strategies by Outcome Results Index](../ai-voice-marketing/index/outcome-result-strategy.md)