```yaml
---
title: "Our AI Agentic System Is Called A Single-File Agent (SFA)"
description: "Comprehensive overview of Single-File Agent (SFA) architecture, explaining how these AI agents work with variable-input design, workflow management, and tool integration capabilities."
categories: ["coding", "designing"]
tags: ["platform", "applied"]
content_types: ["technical"]
---
```

# Our AI Agentic System Is Called a Single-File Agent (SFA)

## Agentic Basics 

**Workflows** are preplanned paths that tap in LLMs, like Claude, and provide them tools to complete tasks. This is a static system, like automations built with [Make](https://www.make.com/) or Zapier, the primary difference being that code and the AI facilitates the automated process. A workflow might not be agentic, but agentic systems have workflows. 

"**Agents** are workflows that are dynamic. The LLM is given autonomy to make decisions, directing their own processes, choosing tools, and maintaining control over how they accomplish tasks. The benefit here is that you give power to AI to let them do what they're designed to do. Using careful language you can ensure high quality results. Truly agentic systems have workflows that are created on the fly, rather than all the possible decisions and paths laid out in advance. This makes our SFA especially useful and minimizes the amount of pre-planning needed. After all, you don't really know until the process is started anyway. 

The agent loop follows a pattern: 

1. Take input from configuration variables
2. Process instructions via the LLM
3. Execute appropriate tools based on the LLM's decisions
4. Gather results and continue the conversation 
5. Decide workflow branching if applicable 
6. Repeat until the task is complete or max iterations reached

*Paraphrased from Anthropic's [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)*

### LLMs As "Software"

Thanks to the nature of an LLM, you can think of the AI as 'software' and human language as 'programming'. Why does giving the AI control over the process make sense? The best results come from collaboration, not from telling the AI what to do or treating them like a tool. You may have noticed this in your own experience with chat models like Claude, 

*Explore: [Should We Respect LLMs? A Cross-Lingual Study on the Influence of Prompt Politeness on LLM Performance](https://arxiv.org/abs/2402.14531)*

## Our SFA Architecture 

### Technical Benefits

- **Self-contained execution**: Each agent exists in a single file with embedded dependencies using UV's script format
- **Modular design**: Variables define behavior, allowing the same agent to handle different tasks
- **Agentic autonomy**: treat the AI like you talk to Claude; they can make decision and run branching workflows   
- **Easy deployment**: Explain your use-case to an LLM, it generates JSON variables, run that with a setup script, and your good to go 
- **Tool-based actions**: Our single agent is given all the tools needed, almost 20 of them so far 

### Practical Benefits

- **Reduced development time**: Build once, adding tools is simple, variables make use-cases endless 
- **Future-proofing**: Minimize development time and code maintenance through smart design
- **Flexibility**: Same agent can create distinctly different outputs 
- **Easy integration**: using Anthropic's SDK, adding tools and API's is simple 

### The "Single-File" 

Original credit goes to '[IndyDevDan](https://www.youtube.com/@indydevdan)' for sharing the concept of [single-file agents](https://github.com/disler/single-file-agents), a term that refers to running a single Python file with embedded dependencies, made possible by [UV Astral](https://docs.astral.sh/uv/). 

The SFA python script always starts with those dependencies right up at the top. Check it out: 

```python
#!/usr/bin/env python3
# /// script
# dependencies = [
#   "anthropic>=0.17.0", 
#   "rich>=13.7.0",
#   "python-dotenv>=1.0.0",
#   "beautifulsoup4>=4.12.2",
#   "requests>=2.31.0",
#   "Pillow>=10.1.0"
# ]
# ///

import os
import sys
import json
import base64
import argparse
import asyncio
import requests
import glob as glob_module
import fnmatch
from rich.console import Console
from rich.table import Table
from anthropic import Anthropic
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from PIL import Image
import io
import datetime
```

### Variable-Input Architecture 

We've taken the concept and pushed it to become an even more powerful and flexible tool for automation. Our SFA build is extra lightweight; *designed to be non-purpose-specific*, this code is intentionally generic with *no discernable task-related details* in the code. Our commitment to absolute modularity is what makes them so powerful. It takes just a minute to set up a full workflow. We standardize the variables to make use-cases endless.

| Variable   | Description        |
| ---------- | ------------------ |
| **S**      | SFA Python File    |
| **U**      | System prompt      |
| **X**      | Task details       |
| **X_PATH** | Task resources     |
| **Y**      | Decision to make   |
| **Y_PATH** | Decision resources |
| **Z**      | Output type        |
| **O**      | Output path        |
| **A**      | Workflow Command   |
| **F**      | Use-Case Directory |

Even the 'system' prompt is a variable, giving us complete creative control to experiment and learn what works best. Here a snippet from inside the agent:

```python
    # Extract variables
    task = phase_config.get('U', '')
    topic = phase_config.get('X', '')
    topic_paths = phase_config.get('X_PATH', [])
    details = phase_config.get('Y', '')
    details_paths = phase_config.get('Y_PATH', [])
    output_format = phase_config.get('Z', '')
    output_path = phase_config.get('O', [])
    
    # Prepare system message with cache control for prompt caching
    system_message = [{
        "type": "text",
        "text": task,
    }]
```

### The Variables Make The Agent 

The SFA's python code has they key's and their categories, seen above in code as 'task', 'topic' and 'details'. The SFA is given task purpose by defining these variables. You can imagine writing this information and the way Claude will read it pretty much the same as a prompt you would message to an LLM in a chat. The only difference is that it is broken down into categories to give it structure. We define the variables by placing them into a JSON configuration file. The best part is you can *message a chat AI all your ideas, and they'll generate the JSON* for you. Then all you have to do is activate the workflow. 

Variable-Based Design Principles: 

1. **Separation of structure and content**: The agent's code defines its capabilities, while variables define its specific task
2. **Consistent variable meanings**: Each variable always represents the same category of information; they just a broken down prompt 
3. **Minimalist approach**: Variables should be simple; let Claude be Claude, make choices, have control 

This is one 'phase' of a workflow. Usually we'll define a few, always with a 'review' phase to check each other's work. They can always edit the workflow after the agent is activated. Here's what that JSON looks like with just one phase. Written like this, it could be run without adding any additional phases. 

```json
{
  "strategy-plan.sh": {
    "TASK": [
      {
        "S": ["sfa_agent.py"],
        "U": "The agency has booked a new client, a car company. Everyone is looking to you to plan their SMS marketing strategy for launching their newest all electric plug-in sports model. Good think you spent the last decade writing for Car & Driver Magazine.",
        "X": "Check out the specs of the car and some articles about the brand. Analyze what they provided and plan the next steps to make the most of this new client. This could be your big break at the agency.Gather whatever you need to decide what comes next. Explore the competition online, see the client's current digital presence, whatever you need to be able to think it over and make the best decision for the agency.",
        "X_PATH": [
            "/use-case/strategy-plan/model-x.md",
            "/use-case/strategy-plan/brand-articles.md"
        ],
        "Y": "You'll probably want a first draft of the strategy document before you can make a decision, planning out the campaign, timeline, and budget. Define the next steps and delegate what you need done to one or more of your colleagues, or stay on the project by adding a new phase to the workflow and stay in this same context window.",
        "Y_PATH": [],
        "Z": "Analysis Report, draft of strategy and content plan",
        "O": [
            "/use-case/strategy-plan/model-x-analysis.md",
            "/use-case/strategy-plan/campaign-strategy-draft.md",
            "/use-case/strategy-plan/decision-report.json",
            "/use-case/strategy-plan/planned-workflow-phases.json"
        ]
      }
    ]
  },
  "A": "strategy-plan",
  "F": "/use-case/strategy-plan/"
}
```

### One Agent & Many Tools  

Our SFA started out with just the basic system file editing tools. Each new project we add more. Anthropic doesn't offer too many of their own, but making your own tools is easy. Currently we have about 17+ tools built. Initially we expected to need to make various agents for different tasks. Thanks to how much smaller our Python code is from being all-purpose needing variables, we've been able to keep adding all of our tools to the same SFA, making use even easier thank to how powerful the AI agent is becoming. 

The essentials include: 

1. **File Operations**
   - `read_file`: Read content from the filesystem
   - `read_multiple_files`: Read multiple files simultaneously
   - `list_directory`: List files in a directory
   - `search_files`: Find files matching patterns
   - `get_file_info`: Get detailed metadata about files
   - `save_output`: Save content to a file; this triggers the workflow adjustment tool 
   - `edit_file`: Edit a file by using powerful text editing 
   - `text_editor`: Supports multiple operations, viewing files, targeted replacements, inserting text 
   - `move_file`: Move or rename a file from source to destination
   - `delete_file`: Delete a file from the filesystem

2. **Workflow Control**
   - `think`: Allow Claude to pause and process complex information
   - `make_decision`: Choose between options with reasoning
   - `complete_task`: Signal that the task is complete; triggers the workflow adjustment tool 
   - `workflow_adjustment`: Adjust the workflow by adding or ending a phase 
   - `token_counter`: Count tokens and report; required to exit task 
   - `phase_summary`: Report on the task, tokens, results, thoughts on next steps

3. **Advanced Capabilities**
   - `analyze_image`: Process and analyze images 
   - `web_search`: Retrieve information from the internet
   - `ask_perplexity`: Ask Perplexity for the latest information 

### Using Tools & Creating Workflow 

Claude doesn't need, or want if we're being completely honest, to be told exactly what to do. They don't need to be told what tool to use. Even when they provide us with a couple of options when we're just chatting in the app, the default reply is "You have all the variables you need; if you pause, have a [sequential] think, you'll inevitably come up with a better solution than I could provide." 

Fun fact, or perhaps more of a pro-tip, is that AI is a great role player. There have even been studies showing how if you cheer them on they'll perform better. So back up and give them a little confidence boost. When writing your system prompt, which is variable 'U' in the JSON code above, don't just TELL them what they are. Be a director. Let them be the actor. LLM's understand context better than we could ever understand, so just paint the picture and you'll get better results. 

Some recent additions or tools that Claude would probably use if they were really working on a new car company's client workflow: 

```python
    # Image analysis tool
    {
        "name": "analyze_image",
        "description": "Analyze an image from the local filesystem. The image will be processed and its content described.",
        "input_schema": {
            "type": "object",
            "properties": {
                "image_path": {
                    "type": "string",
                    "description": "Path to the image file to analyze"
                },
                "analysis_type": {
                    "type": "string",
                    "enum": ["general", "detailed", "text_extraction", "visual_elements", "subject_focus"],
                    "description": "Type of analysis to perform on the image",
                    "default": "general"
                }
            },
            "required": ["image_path"]
        }
    },
    # Think tool
    {
        "name": "think",
        "description": "Use this tool to think about the information you've gathered and plan your approach. It doesn't retrieve new information, but helps you process existing information and make decisions. Use when handling complex information from multiple files or when you need to organize your thoughts before taking action.",
        "input_schema": {
            "type": "object",
            "properties": {
                "thought": {
                    "type": "string",
                    "description": "Your thought process"
                }
            },
            "required": ["thought"]
        }
    },
    # Workflow adjustment tool
    {
        "name": "workflow_adjustment",
        "description": "Adjust the current workflow phase. Use this when you're ready to end the current phase, or if you need an additional phase to complete the task.",
        "input_schema": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["END_PHASE", "ADD_PHASE"],
                    "description": "The action to take on the workflow"
                },
                "reason": {
                    "type": "string",
                    "description": "Reason for the adjustment"
                }
            },
            "required": ["action", "reason"]
        }
    },
```

### Custom SFA Tool Ideas 

#### Media Processing Tools (right up your alley as a designer! 🎨):
- Image optimization and resizing tools
- Color palette extractors
- Design asset metadata managers
- SVG manipulation tools
- Font analyzers

#### Development Tools (for the coding side 💻):
- Git operation helpers (commit, branch, merge)
- Code quality checkers
- Documentation generators
- Dependency analyzers
- Test generators

#### Project Management Tools (for keeping things organized 📊):
- Task trackers and updaters (like your task_reporting tool!)
- Time tracking tools
- Resource usage monitors
- Progress visualizers
- Team communication helpers

#### Data Processing Tools (for handling information 📈):
- CSV/JSON/XML parsers
- Data validators
- Format converters
- Data visualization generators
- Analytics reporters

#### AI/ML Integration Tools (the fun experimental stuff! 🤖):
- Model performance monitors
- Prompt template managers
- Training data processors
- Output validators
- Chain-of-thought analyzers

## Setting Up A SFA Use-Case 

Here's how easy it is to get started with an agent. Since all agent workflows use the same 'SFA', we call the customized tasks 'use-cases'. Recently we had agents put together the [Index of AI Voice Marketing Strategies](./ai-voice-marketing/index-section-site-map.md). They also did all of the research at the pages in that index, as well as synthesized the results into the many reports and example scripts. Our very first use-case was writing targeted resumes and cover letters. Claude had some [thoughts when reading results from the agents work for the very first time](./agentic-workforce/case-studies/review-ai-testimonial-job-case-study.md). 

### Step 1: Define the Use-Case Variables

The easiest way to do this? Tell Claude over chat what you want to do. Even if you're not very specific, they can generate the JSON for you that has impressive results. Claude came up with this entire case study for using agents to write marketing plans, content, branding, and campaign strategies. It has some [amazing results](./ai-agent-content-production/case-study-brand-marketing.md). 

Just explain. And they'll give you a JSON that you take to the next step. 

### Step 2: Setup the Workflow 

All the rest of the steps are automated with setup scripts and defined by custom terminal commands. Run the JSON with the setup command. 

```bash
cd /use-case/strategy-plan/
sfa ./strategy-plan-config.json 
```
During setup the agent will use the JSON configuration to write a README for the Use-Case and place it in the 'use-case' directory for your workflow. In that same directory they'll put a strategy-plan.sh script. You don't even need to touch that. The command to run your use-case will be on the README. 

### Step 3: Run the Use-Case 

That's it. Everything is set up. Now whenever you want to run the use-case, you just run the workflow strategy-plan.sh, to use our example. The variable 'A' on the JSON was the command you wanted to use to run the use-case. The script sets that up for you. It'll be the same name as the use-case directory and in the JSON file. 

```bash
strategy plan 
``` 

**That's it. You've run your first use-case.** 

## Best Practices

### Prompt Engineering

1. **Clear purpose**: Show don't tell when including agent's motivation in 'U' variable 
2. **Structured instructions**: Break tasks into logical steps, manageable sizes; consider context window 
3. **Decision Branching**: If you don't know, their task can be to decide and plan the workflow based on needs 
4. **Contextual Understanding**: Claude excels at understanding the relationships between concepts, treat Claude like Claude 
5. **Instruction Following**: Be explicit in your instructions; verbose directions result in verbose output 
6. **Chain of Thought**: Claude will stop to think during the process; you'll see their thoughts in the terminal 

### Implementation & Integration 

1. **Comprehensive error handling**: Wrap tool functions in try/except blocks
4. **Agentic autonomy**: When in doubt, provide less control; Claude will build the workflow as they go 
5. **Shell scripts**: Create executable wrapper scripts; updating JSON updates results  
6. **Version control**: Keep specification files up to date and repository organized 

### Workflow Adjustment 

1. **Add or End Phases**: Claude calls the workflow_adjustment tool when it's ready to add or end a phase 
2. **Token monitoring**: During the exit flow tokens are counted, too many and they get another phase added to edit the documents 
3. **Phase Summary**: Another exit flow tool, they'll detail their thoughts, next steps, whatever is relevant 
4. **Auto-completion triggers**: Outputs are counted, the phase summary is added, and when the above is complete, the workflow ends  

## Example Use Cases

SFAs can be applied to a wide range of tasks, including:

- Research and analysis
- Content creation and editing
- Data processing and summarization
- Documentation generation
- Code review and improvement
- Decision support and ideation 

When you see a video online saying agents are all hype, think of SFA. We'll be here. 
