```yaml
title: "Single-File Agent Technical Specifications"
categories: ["Technical", "Implementation", "Research"]
tags: ["technical", "implementation", "research"]
content_types: ["Technical References", "Implementation Guides", "Research Findings"]
description: "Detailed technical documentation of Single-File Agent tools, implementations, and performance optimizations including code examples and integration methods."
```

# Single-File Agent Technical Specifications

## Tool Implementations

### Essential File Tools

```python
{
    "name": "read_file",
    "description": "Read the content of a file from the local filesystem.",
    "input_schema": {
        "type": "object",
        "properties": {"file_path": {"type": "string"}},
        "required": ["file_path"]
    }
},
{
    "name": "read_multiple_files",
    "description": "Read the contents of multiple files simultaneously. This is more efficient than reading files one by one when you need to analyze or compare multiple files.",
    "input_schema": {
        "type": "object",
        "properties": {
            "paths": {
                "type": "array", 
                "items": {"type": "string"},
                "description": "Array of file paths to read"
            }
        },
        "required": ["paths"]
    }
},
{
    "name": "list_directory",
    "description": "List all files in a directory.",
    "input_schema": {
        "type": "object",
        "properties": {
            "directory_path": {"type": "string"},
            "pattern": {"type": "string", "default": "*.*"}
        },
        "required": ["directory_path"]
    }
},
{
    "name": "search_files",
    "description": "Recursively search for files and directories matching a pattern. Searches through all subdirectories from the starting path.",
    "input_schema": {
        "type": "object",
        "properties": {
            "path": {"type": "string", "description": "Starting directory path"},
            "pattern": {"type": "string", "description": "Search pattern to match files/directories"},
            "exclude_patterns": {
                "type": "array", 
                "items": {"type": "string"},
                "description": "Patterns to exclude from results",
                "default": []
            }
        },
        "required": ["path", "pattern"]
    }
},
{
    "name": "get_file_info",
    "description": "Retrieve detailed metadata about a file or directory.",
    "input_schema": {
        "type": "object",
        "properties": {
            "path": {"type": "string", "description": "Path to the file or directory"}
        },
        "required": ["path"]
    }
},
{
    "name": "save_output",
    "description": "Save content to the output file.",
    "input_schema": {
        "type": "object",
        "properties": {
            "content": {"type": "string"},
            "file_path": {"type": "string"}
        },
        "required": ["content", "file_path"]
    }
}
```

### Advanced Thinking & Decision Tools

#### The Think Tool

The "think" tool significantly improves Claude's performance by providing a dedicated space for structured thinking during complex tasks. In benchmark tests, it showed a 54% relative improvement in performance compared to not using it.

```python
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
}
```

##### When to Use the Think Tool
- Processing complex information from multiple sources
- Planning multi-step tasks
- Analyzing detailed requirements
- Making decisions with multiple factors to consider
- Reviewing and synthesizing tool results
- Handling long chains of tool calls
- Navigating detailed guidelines
- Making sequential decisions where each step builds on the previous one

##### Best Practices for Using the Think Tool
Before taking action or responding after receiving tool results, use the think tool as a scratchpad to:
- List specific rules that apply to the current request
- Check if all required information is collected
- Verify planned actions comply with policies
- Iterate over tool results for correctness

##### Example Think Tool Usage
When implementing a think tool, Claude will typically perform analysis like:

```
User wants to book 3 tickets to NYC with 2 checked bags each
- Need user ID to check:
  * Membership tier for baggage allowance
  * Which payments methods exist in profile
- Baggage calculation:
  * Economy class × 3 passengers
  * If regular member: 1 free bag each → 3 extra bags = $150
  * If silver member: 2 free bags each → 0 extra bags = $0
  * If gold member: 3 free bags each → 0 extra bags = $0
- Payment rules to verify:
  * Max 1 travel certificate, 1 credit card, 3 gift cards
  * All payment methods must be in profile
  * Travel certificate remainder goes to waste
- Plan:
1. Get user ID
2. Verify membership level for bag fees
3. Check which payment methods in profile and if their combination is allowed
4. Calculate total: ticket price + any bag fees
5. Get explicit confirmation for booking
```

##### Implementation Tips
- Strategic prompting with domain-specific examples significantly improves the model's use of the think tool
- Place complex guidance in the system prompt rather than the tool description
- Monitor and refine how Claude uses the tool in practice

#### Decision Making Tool

```python
{
    "name": "make_decision",
    "description": "Make a decision between multiple options with reasoning. Use this to determine the next course of action or to make important choices during the workflow.",
    "input_schema": {
        "type": "object",
        "properties": {
            "options": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of available options to choose from"
            },
            "decision": {
                "type": "string",
                "description": "The selected option"
            },
            "reasoning": {
                "type": "string",
                "description": "Explanation of why this decision was made"
            },
            "confidence": {
                "type": "number",
                "minimum": 0,
                "maximum": 1,
                "description": "Confidence level in the decision (0.0 to 1.0)"
            }
        },
        "required": ["options", "decision", "reasoning", "confidence"]
    }
}
```

### Web Search & Vision Capabilities

```python
{
    "name": "web_search",
    "description": "Search the web using Brave Search API to find current information on a topic.",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The search query to look up on the web"
            },
            "num_results": {
                "type": "integer",
                "description": "Number of results to return (1-5)",
                "default": 3
            }
        },
        "required": ["query"]
    }
},
{
    "name": "perplexity_search",
    "description": "Search using Perplexity AI to get detailed, source-backed answers to complex questions. This provides more thorough research and deeper context than regular web search.",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The research question or query to investigate"
            },
            "focus": {
                "type": "string",
                "enum": ["academic", "normal", "concise", "creative"],
                "description": "The focus mode for the search",
                "default": "normal"
            }
        },
        "required": ["query"]
    }
},
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
}
```

## Performance Optimizations

### Token-Efficient Tools

SFAs leverage Claude's token-efficient-tools beta, which can reduce token usage by up to 70% for tool-heavy interactions.

```python
# Enable token-efficient-tools in the API call
response = anthropic_client.beta.messages.create(
    model="claude-3-7-sonnet-20250219",
    system=system_message,
    messages=conversation_history,
    max_tokens=8192,
    tools=TOOLS,
    temperature=0.3,
    betas=["token-efficient-tools-2025-02-19", "prompt-caching-2024-07-31"]
)
```

Requests using this beta save an average of 14% in output tokens (up to 70%), which also reduces latency. Exact token reduction and latency improvements depend on the overall response shape and size.

### Prompt Caching

SFAs support Claude's prompt caching feature, which significantly reduces token usage and improves response time for repetitive operations.

```python
# Enable prompt caching in the API call
response = anthropic_client.beta.messages.create(
    model="claude-3-7-sonnet-20250219",
    system=system_message,
    messages=conversation_history,
    max_tokens=8192,
    tools=TOOLS,
    temperature=0.3,
    betas=["token-efficient-tools-2025-02-19", "prompt-caching-2024-07-31"]
)

# Track cache performance
cache_creation_tokens = getattr(response.usage, 'cache_creation_input_tokens', 0)
cache_read_tokens = getattr(response.usage, 'cache_read_input_tokens', 0)
```

### Token Usage Tracking

The TokenCounter class tracks token usage and estimated costs, providing visibility into API consumption.

```python
class TokenCounter:
    def __init__(self):
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_cached_tokens = 0
        self.total_cost = 0.0
        self.cached_tokens_savings = 0.0
        
    def update(self, input_tokens, output_tokens, cached_tokens=0):
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens
        self.total_cached_tokens += cached_tokens
        
        # Calculate costs (approximate values)
        input_cost = input_tokens * 0.000003  # $3 per million tokens
        output_cost = output_tokens * 0.000015  # $15 per million tokens
        cached_cost_savings = cached_tokens * 0.000003 * 0.9  # 90% discount on cached tokens
        
        self.total_cost += input_cost + output_cost
        self.cached_tokens_savings += cached_cost_savings
```

## Workflow Automation Features

### Automatic Phase Completion

SFAs can automatically complete a phase when all required output files have been saved, streamlining multi-phase workflows.

```python
# Handle multiple output files
if tool_name == "save_output":
    saved_path = tool_input.get("file_path", "")
    if saved_path in output_path:
        saved_outputs.add(saved_path)
        console.print(f"[green]Output saved to target path:[/green] {saved_path}")
        
        # Check if all expected outputs have been saved
        if set(output_path).issubset(saved_outputs):
            output_saved = True
            console.print(f"[green]All {len(output_path)} expected outputs saved. Phase completion triggered automatically[/green]")
        else:
            remaining = len(output_path) - len(saved_outputs)
            console.print(f"[yellow]Progress: {len(saved_outputs)}/{len(output_path)} outputs saved. {remaining} remaining.[/yellow]")

# Check if task complete
if tool_name == "complete_task" or output_saved:
    task_complete = True
```

This feature supports both single and multiple output files. When the 'O' field in the JSON configuration contains a list of file paths, the agent will track which files have been saved and only complete the phase when all expected outputs are created. Progress is reported after each file is saved.

### Decision Output for Workflow Branching

The make_decision tool saves decisions to a JSON file, enabling conditional branching in workflows.

```python
decision_output = {
    "options": options,
    "decision": decision,
    "reasoning": reasoning,
    "confidence": confidence,
    "timestamp": str(datetime.datetime.now())
}

decision_path = "last_decision.json"
with open(decision_path, 'w') as f:
    json.dump(decision_output, f, indent=2)
```

## Integration with External Services

### Web Search Implementation

```python
def web_search(query, num_results=3):
    api_key = brave_subscription_token or brave_api_key
    if not api_key:
        return "Error: Neither Brave API key nor X-Subscription-Token found in environment variables"
        
    headers = {"Accept": "application/json", "X-Subscription-Token": api_key}
    response = requests.get(
        "https://api.search.brave.com/res/v1/web/search",
        params={"q": query, "count": num_results},
        headers=headers,
        timeout=30
    )
    
    if not response.ok:
        return f"Error: HTTP error {response.status_code} from Brave API"
        
    results = response.json().get("web", {}).get("results", [])
    
    # Process and format results
    # ...

    return formatted_results
```

### Perplexity Search Implementation

```python
def perplexity_search(query, focus="normal"):
    """Search using Perplexity AI to get detailed, source-backed answers to complex questions."""
    try:
        if not perplexity_api_key:
            return "Error: Perplexity API key not found in environment variables"
            
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {perplexity_api_key}"
        }
        
        # Create appropriate system message based on focus mode
        system_message = "Be precise and concise."
        if focus == "academic":
            system_message = "You are an academic researcher providing thorough, well-sourced information."
        elif focus == "concise":
            system_message = "Provide extremely concise answers with just the key facts."
        elif focus == "creative":
            system_message = "Explore creative connections and provide thoughtful, expansive answers."
        
        payload = {
            "model": "sonar-pro-online",
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": query}
            ]
        }
        
        response = requests.post(
            "https://api.perplexity.ai/chat/completions",
            headers=headers,
            json=payload,
            timeout=60
        )
        
        # Process and format results with citations
        # ...
        
        return formatted_answer_with_citations
        
    except Exception as e:
        return f"Error performing Perplexity search: {str(e)}"
```

### Image Analysis Implementation

```python
def analyze_image(image_path, analysis_type="general"):
    if not os.path.exists(image_path):
        return f"Error: Image file not found at {image_path}"
        
    # Read and encode the image
    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")
        
    # Determine image format for media_type
    image_format = image_path.split(".")[-1].lower()
    if image_format == "jpg":
        image_format = "jpeg"
    media_type = f"image/{image_format}"
    
    # Get image dimensions
    with Image.open(image_path) as img:
        width, height = img.size
        
    # Create a prompt
    prompt = f"Please analyze this image. Analysis type: {analysis_type}. Image dimensions: {width}x{height} pixels."
    
    # Call Claude to analyze the image
    response = anthropic_client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=1500,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": image_data
                        }
                    },
                    {"type": "text", "text": prompt}
                ]
            }
        ]
    )
    
    # Return analysis with metadata
    # ...
```

## Implementation Guidelines

### Error Handling Best Practices

All tool implementations should use comprehensive error handling:

```python
try:
    # Tool implementation
    result = operation()
    return result
except Exception as e:
    return f"Error: {str(e)}"
```

### Conversation Flow Management

Maintain a clean conversation history with appropriate roles:

```python
# Add Claude's response to conversation history
conversation_history.append({
    "role": "assistant",
    "content": response.content
})

# Add tool result to conversation
conversation_history.append({
    "role": "user",
    "content": [
        {
            "type": "tool_result",
            "tool_use_id": tool_id,
            "content": tool_result
        }
    ]
})
```

# SFA Technical Specifications

This document provides detailed technical specifications for Single-File Agents (SFAs), including tool implementations, code structure, and performance features.

## Agent Implementation

### Core Dependencies

```python
# /// script
# dependencies = [
#   "anthropic>=0.17.0", 
#   "rich>=13.7.0",
#   "python-dotenv>=1.0.0",
#   "pillow>=10.1.0",       # For image analysis
#   "requests>=2.31.0",     # For web requests
#   "tenacity>=8.2.3",      # For retries
#   "httpx>=0.24.1",        # For async HTTP
# ]
# ///
```

### Essential Imports

```python
import os
import sys
import json
import argparse
import asyncio
import glob
import time
from pathlib import Path
from typing import List, Dict, Any, Optional, Union
from rich.console import Console
from rich.table import Table
from anthropic import Anthropic
from dotenv import load_dotenv
```

### Base Agent Structure

The standard agent structure includes:

1. **Environment Setup**: Loading API keys and initializing clients
2. **Tool Definitions**: Declaring tools with their schemas
3. **Tool Implementations**: Functions that execute tool actions
4. **Main Loop**: Processing the agent conversation with Claude
5. **Configuration Handling**: Loading and parsing JSON configuration

## Token Management

The `TokenCounter` class tracks token usage:

```python
class TokenCounter:
    def __init__(self):
        self.input_tokens = 0
        self.output_tokens = 0
        
    def add_input_tokens(self, count):
        self.input_tokens += count
        
    def add_output_tokens(self, count):
        self.output_tokens += count
        
    def get_total_tokens(self):
        return self.input_tokens + self.output_tokens
        
    def get_estimated_cost(self, input_cost_per_1k=0.03, output_cost_per_1k=0.15):
        input_cost = (self.input_tokens / 1000) * input_cost_per_1k
        output_cost = (self.output_tokens / 1000) * output_cost_per_1k
        return input_cost + output_cost
```

## Prompt Caching

Prompt caching improves performance by storing previously generated responses:

```python
class PromptCache:
    def __init__(self, cache_dir=".cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        
    def get_cache_key(self, messages):
        # Generate a unique key for the message set
        return hash_function(json.dumps(messages))
        
    def get_cached_response(self, messages):
        key = self.get_cache_key(messages)
        cache_file = self.cache_dir / f"{key}.json"
        
        if cache_file.exists():
            with open(cache_file, 'r') as f:
                return json.load(f)
        return None
        
    def cache_response(self, messages, response):
        key = self.get_cache_key(messages)
        cache_file = self.cache_dir / f"{key}.json"
        
        with open(cache_file, 'w') as f:
            json.dump(response, f)
```

## Tool Specifications

### File Operations

#### 1. `read_file`

Reads content from a single file.

```json
{
  "type": "function",
  "function": {
    "name": "read_file",
    "description": "Read the content of a file",
    "parameters": {
      "type": "object",
      "properties": {
        "file_path": {
          "type": "string",
          "description": "Path to the file to read"
        }
      },
      "required": ["file_path"]
    }
  }
}
```

#### 2. `read_multiple_files`

Reads content from multiple files simultaneously.

```json
{
  "type": "function",
  "function": {
    "name": "read_multiple_files",
    "description": "Read the content of multiple files at once",
    "parameters": {
      "type": "object",
      "properties": {
        "file_paths": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of file paths to read"
        }
      },
      "required": ["file_paths"]
    }
  }
}
```

#### 3. `list_directory`

Lists files in a directory.

```json
{
  "type": "function",
  "function": {
    "name": "list_directory",
    "description": "List files in a directory",
    "parameters": {
      "type": "object",
      "properties": {
        "directory_path": {
          "type": "string",
          "description": "Path to the directory to list"
        },
        "pattern": {
          "type": "string",
          "description": "Optional glob pattern to filter files",
          "default": "*"
        }
      },
      "required": ["directory_path"]
    }
  }
}
```

#### 4. `search_files`

Searches for files matching patterns recursively.

```json
{
  "type": "function",
  "function": {
    "name": "search_files",
    "description": "Search for files matching a pattern recursively",
    "parameters": {
      "type": "object",
      "properties": {
        "base_path": {
          "type": "string",
          "description": "Base directory to start the search from"
        },
        "pattern": {
          "type": "string",
          "description": "Glob pattern to match files"
        },
        "max_depth": {
          "type": "integer",
          "description": "Maximum directory depth to search",
          "default": 5
        }
      },
      "required": ["base_path", "pattern"]
    }
  }
}
```

#### 5. `get_file_info`

Retrieves detailed metadata about files.

```json
{
  "type": "function",
  "function": {
    "name": "get_file_info",
    "description": "Get metadata information about a file",
    "parameters": {
      "type": "object",
      "properties": {
        "file_path": {
          "type": "string",
          "description": "Path to the file to get information about"
        }
      },
      "required": ["file_path"]
    }
  }
}
```

#### 6. `save_output`

Saves content to a file.

```json
{
  "type": "function",
  "function": {
    "name": "save_output",
    "description": "Save content to a file",
    "parameters": {
      "type": "object",
      "properties": {
        "file_path": {
          "type": "string",
          "description": "Path where the file should be saved"
        },
        "content": {
          "type": "string",
          "description": "Content to write to the file"
        },
        "append": {
          "type": "boolean",
          "description": "Whether to append to the file or overwrite it",
          "default": false
        }
      },
      "required": ["file_path", "content"]
    }
  }
}
```

### Decision Making

#### 1. `think`

Allows Claude to process complex information.

```json
{
  "type": "function",
  "function": {
    "name": "think",
    "description": "Think through a complex problem step by step",
    "parameters": {
      "type": "object",
      "properties": {
        "thought_process": {
          "type": "string",
          "description": "Detailed step-by-step reasoning about the problem"
        }
      },
      "required": ["thought_process"]
    }
  }
}
```

#### 2. `make_decision`

Chooses between options with reasoning.

```json
{
  "type": "function",
  "function": {
    "name": "make_decision",
    "description": "Make a decision between multiple options with reasoning",
    "parameters": {
      "type": "object",
      "properties": {
        "options": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of options to choose from"
        },
        "reasoning": {
          "type": "string",
          "description": "Reasoning for the decision"
        },
        "decision": {
          "type": "string",
          "description": "The selected option"
        }
      },
      "required": ["options", "reasoning", "decision"]
    }
  }
}
```

### Workflow Control

#### 1. `workflow_adjustment`

Controls phase completion and workflow branching.

```json
{
  "type": "function",
  "function": {
    "name": "workflow_adjustment",
    "description": "Control phase completion and workflow branching. This tool handles task completion, token counting, and phase transitions.",
    "parameters": {
      "type": "object",
      "properties": {
        "action": {
          "type": "string",
          "enum": ["END_PHASE", "ADD_PHASE"],
          "description": "Whether to end the current phase or add a new phase"
        },
        "reason": {
          "type": "string",
          "description": "Explanation for the workflow adjustment"
        },
        "token_count": {
          "type": "integer",
          "description": "Current token count for output verification"
        },
        "phase_summary": {
          "type": "object",
          "properties": {
            "accomplishments": {
              "type": "array",
              "items": {"type": "string"},
              "description": "List of key accomplishments in this phase"
            },
            "token_counts": {
              "type": "object",
              "description": "Token counts for each output document"
            },
            "decisions": {
              "type": "array",
              "items": {"type": "string"},
              "description": "Any decisions made during this phase"
            },
            "next_steps": {
              "type": "array",
              "items": {"type": "string"},
              "description": "Recommended next steps or phase requirements"
            }
          },
          "required": ["accomplishments", "token_counts", "next_steps"]
        }
      },
      "required": ["action", "reason", "phase_summary"]
    }
  }
}
```

#### 2. `save_output`

Save content to a file and trigger workflow adjustment if needed.

```json
{
  "type": "function",
  "function": {
    "name": "save_output",
    "description": "Save content to a file and potentially trigger phase completion or token revision.",
    "parameters": {
      "type": "object",
      "properties": {
        "content": {
          "type": "string",
          "description": "Content to write to the file"
        },
        "file_path": {
          "type": "string",
          "description": "Path where the file should be saved"
        },
        "append": {
          "type": "boolean",
          "description": "Whether to append to the file or overwrite it",
          "default": false
        },
        "check_tokens": {
          "type": "boolean",
          "description": "Whether to perform token checking",
          "default": true
        }
      },
      "required": ["content", "file_path"]
    }
  }
}
```

#### 3. `complete_task`

Signal task completion and generate phase summary.

```json
{
  "type": "function",
  "function": {
    "name": "complete_task",
    "description": "Mark the current task as complete and generate phase summary",
    "parameters": {
      "type": "object",
      "properties": {
        "completion_message": {
          "type": "string",
          "description": "Message describing the completed task"
        },
        "phase_summary": {
          "type": "object",
          "properties": {
            "accomplishments": {
              "type": "array",
              "items": {"type": "string"}
            },
            "token_counts": {
              "type": "object"
            },
            "decisions": {
              "type": "array",
              "items": {"type": "string"}
            },
            "next_steps": {
              "type": "array",
              "items": {"type": "string"}
            }
          },
          "required": ["accomplishments", "token_counts", "next_steps"]
        }
      },
      "required": ["completion_message", "phase_summary"]
    }
  }
}
```

### Advanced Capabilities

#### 1. `web_search`

Retrieves information from the internet.

```json
{
  "type": "function",
  "function": {
    "name": "web_search",
    "description": "Search the web for information",
    "parameters": {
      "type": "object",
      "properties": {
        "query": {
          "type": "string",
          "description": "Search query"
        },
        "num_results": {
          "type": "integer",
          "description": "Number of results to return",
          "default": 5
        }
      },
      "required": ["query"]
    }
  }
}
```

#### 2. `analyze_image`

Processes and analyzes images.

```json
{
  "type": "function",
  "function": {
    "name": "analyze_image",
    "description": "Analyze an image and extract information",
    "parameters": {
      "type": "object",
      "properties": {
        "image_path": {
          "type": "string",
          "description": "Path to the image file"
        },
        "analysis_type": {
          "type": "string",
          "description": "Type of analysis to perform",
          "enum": ["general", "text", "objects", "colors", "composition"],
          "default": "general"
        }
      },
      "required": ["image_path"]
    }
  }
}
```

## Tool Implementation Examples

### File Operations Example

```python
def read_file(file_path):
    """Read the content of a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return {"content": content}
    except Exception as e:
        return {"error": f"Error reading file: {str(e)}"}

def search_files(base_path, pattern, max_depth=5):
    """Search for files matching a pattern recursively."""
    try:
        files = []
        base = Path(base_path)
        
        if not base.exists():
            return {"error": f"Base path does not exist: {base_path}"}
            
        # Convert glob pattern to Path-compatible pattern
        if '**' not in pattern:
            # For each level up to max_depth
            for i in range(max_depth + 1):
                # Build pattern with current depth
                depth_path = base
                for _ in range(i):
                    depth_path = depth_path / '*'
                search_pattern = str(depth_path / pattern)
                matches = glob.glob(search_pattern, recursive=False)
                files.extend(matches)
        else:
            # Pattern already contains recursive search
            search_pattern = str(base / pattern)
            files = glob.glob(search_pattern, recursive=True)
            
        # Sort and get relative paths
        files = sorted(files)
        
        return {
            "matches": files,
            "count": len(files)
        }
    except Exception as e:
        return {"error": f"Error searching files: {str(e)}"}
```

### Web Search Implementation

```python
async def web_search(query, num_results=5):
    """Search the web for information using Brave Search API."""
    try:
        api_key = os.getenv("BRAVE_SEARCH_API_KEY")
        if not api_key:
            return {"error": "Brave Search API key not found. Please set BRAVE_SEARCH_API_KEY environment variable."}
            
        url = "https://api.search.brave.com/res/v1/web/search"
        headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
            "X-Subscription-Token": api_key
        }
        params = {
            "q": query,
            "count": min(num_results, 10),  # API limit is 10
            "text_format": "plain",
            "search_lang": "en"
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
        results = []
        if "web" in data and "results" in data["web"]:
            for result in data["web"]["results"][:num_results]:
                results.append({
                    "title": result.get("title", ""),
                    "url": result.get("url", ""),
                    "description": result.get("description", "")
                })
                
        return {
            "query": query,
            "results": results,
            "count": len(results)
        }
    except Exception as e:
        return {"error": f"Error performing web search: {str(e)}"}
```

### Image Analysis Implementation

```python
def analyze_image(image_path, analysis_type="general"):
    """Analyze an image and extract information."""
    try:
        if not os.path.exists(image_path):
            return {"error": f"Image file not found: {image_path}"}
            
        # For this implementation, we'll prepare the image for Claude's vision capabilities
        with open(image_path, "rb") as image_file:
            # Convert image to base64 for API
            import base64
            image_data = base64.b64encode(image_file.read()).decode("utf-8")
            
        # In the actual implementation, we would send this to Claude through the API
        # Here we're just returning the confirmation
        return {
            "status": "success",
            "message": f"Image at {image_path} prepared for {analysis_type} analysis",
            "analysis_type": analysis_type
        }
    except Exception as e:
        return {"error": f"Error analyzing image: {str(e)}"}
```

## Automatic Phase Completion

The agent can automatically complete the current phase when the output is saved:

```python
async def save_output(file_path, content, append=False):
    """Save content to a file and potentially trigger phase completion."""
    try:
        # Create directories if they don't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Write content to file
        mode = "a" if append else "w"
        with open(file_path, mode, encoding="utf-8") as file:
            file.write(content)
            
        # Check if this matches the output path in config
        # If so, we can auto-complete the phase
        if file_path == current_phase_config.get('O'):
            task_status["task_complete"] = True
            console.print(f"[green]Output saved to {file_path} and phase marked as complete![/green]")
        else:
            console.print(f"[green]Output saved to {file_path}[/green]")
            
        return {"file_path": file_path, "success": True}
    except Exception as e:
        return {"error": f"Error saving output: {str(e)}"}
```

## Error Handling

Robust error handling is essential for agent reliability:

```python
async def handle_tool_call(name, tool_input):
    """Handle a tool call with proper error handling."""
    try:
        if name == "read_file":
            return await read_file(tool_input.get("file_path", ""))
        elif name == "save_output":
            return await save_output(
                tool_input.get("file_path", ""),
                tool_input.get("content", ""),
                tool_input.get("append", False)
            )
        # Other tool handlers...
        else:
            return {"error": f"Unknown tool: {name}"}
    except Exception as e:
        # Log the error and return a structured error response
        console.print(f"[red]Error in tool {name}: {str(e)}[/red]")
        return {"error": f"Error executing tool {name}: {str(e)}"}
```

## Performance Optimization

These techniques improve agent performance:

1. **Batched Processing**: Process multiple files at once
2. **Parallel Tool Execution**: Run multiple tools concurrently
3. **Response Streaming**: Process Claude's response as it's generated
4. **Caching**: Store previous results for reuse
5. **Rate Limiting**: Implement backoff strategies for API calls

```python
# Example of parallel tool execution
async def process_tool_calls(tool_calls):
    """Process multiple tool calls in parallel."""
    tasks = []
    for tool_call in tool_calls:
        name = tool_call["function"]["name"]
        arguments = json.loads(tool_call["function"]["arguments"])
        tasks.append(handle_tool_call(name, arguments))
        
    return await asyncio.gather(*tasks)
```

## Agent Loop Implementation

The core agent loop:

```python
async def run_agent_loop():
    """Run the main agent loop with workflow adjustment support."""
    while not task_complete and current_iteration < max_iterations:
        try:
            # Get Claude's response
            response = await get_claude_response()
            
            # Handle tool calls
            for tool_call in response.tool_calls:
                result = await handle_tool_call(tool_call)
                
                # Check for workflow adjustments
                if tool_call.name in ['save_output', 'complete_task']:
                    # Verify tokens and handle phase completion
                    adjustment = await handle_workflow_adjustment(
                        action="END_PHASE",
                        reason="output_saved",
                        phase_summary=result.get('phase_summary', {})
                    )
                    
                    if adjustment['status'] == 'phase_reset':
                        # Continue same phase for revision
                        continue
                    elif adjustment['status'] == 'phase_completed':
                        # End phase and potentially start next
                        task_complete = True
                        break
                        
            # Update conversation history
            update_conversation_history(response, tool_results)
            
        except Exception as e:
            handle_error(e)
            
    return task_complete
```

## Configuration Handling

Load and process configuration files:

```python
def load_config(config_file):
    """Load and validate the configuration file."""
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
            
        # Validate required fields
        workflow_key = next((k for k in config.keys() if k != 'A' and k != 'F'), None)
        if not workflow_key:
            raise ValueError("No workflow found in configuration")
            
        phases = config[workflow_key]
        if not phases or not isinstance(phases, list):
            raise ValueError("No phases defined in workflow")
            
        # Validate each phase
        for i, phase in enumerate(phases):
            required_vars = ['S', 'U', 'Z']
            for var in required_vars:
                if var not in phase:
                    raise ValueError(f"Required variable '{var}' missing in phase {i}")
                    
        return config
        
    except Exception as e:
        console.print(f"[red]Error loading configuration: {str(e)}[/red]")
        sys.exit(1)
```

## Advanced Features

### Auto-Resolving Variables

```python
def resolve_variables(phase_config):
    """Resolve variables from different representations to standard format."""
    resolved = {}
    
    for key, value in phase_config.items():
        # Handle list vs string for paths
        if key in ['S', 'X_PATH', 'Y_PATH', 'O']:
            if isinstance(value, list):
                resolved[key] = value
            elif isinstance(value, str):
                resolved[key] = [value]
            else:
                resolved[key] = []
        else:
            resolved[key] = value
            
    return resolved
```

### Extension Points

The agent framework can be extended with custom tools:

```python
def register_custom_tool(name, description, parameters, implementation):
    """Register a custom tool with the agent."""
    # Add tool definition to TOOLS list
    TOOLS.append({
        "type": "function",
        "function": {
            "name": name,
            "description": description,
            "parameters": parameters
        }
    })
    
    # Register the implementation
    TOOL_IMPLEMENTATIONS[name] = implementation
    
    console.print(f"[green]Registered custom tool: {name}[/green]")
```

## Error Code Reference

Common error codes and troubleshooting:

| Error Code  | Description                     | Troubleshooting                                          |
| ----------- | ------------------------------- | -------------------------------------------------------- |
| `CONFIG_01` | Missing required variables      | Check your JSON configuration has all required variables |
| `CONFIG_02` | Invalid file path format        | Ensure paths use the correct format for your OS          |
| `API_01`    | Claude API authentication error | Verify your API key is set correctly                     |
| `API_02`    | Rate limit exceeded             | Implement backoff or reduce request frequency            |
| `TOOL_01`   | Tool execution error            | Check the tool parameters and file paths                 |
| `FILE_01`   | File not found                  | Verify the file exists at the specified path             |
| `FILE_02`   | Permission denied               | Check file permissions                                   |

----

## Directory Content 

- About Section
  - [About Our AI Agent Research & Production](../about-our-agents.md)
  - [Technical Specifications](../about-our-agents/technical-specifications.md)
  - [What Is A Single-File Agent](../about-our-agents/what-is-sfa-single-file-agent.md)
  - [Workflow Feedback Job Resume Case Study](../about-our-agents/workflow-feedback-job-resume-case-study.md)
- Case Studies 
  - [AI Agentic Brand Content Case Study](../ai-agentic-brand-content-case-study.md)
  - [Agentic Research Case Study](../ai-voice-marketing/agentic-research-planning-case-study.md)
- Section Pages 
  - [AI Voice Marketing Research & Implementation Guide](../ai-voice-marketing.md)
  - [AI Voice Marketing Deep Research](../ai-voice-marketing/deep-research.md)
  - [AI Voice Marketing Research Implementation](../ai-voice-marketing/research-implementation.md)
  - [AI Voice Marketing Writing Guides](../ai-voice-marketing/research-implementation/writing-guide.md)
  - [AI Voice Marketing Persona Strategy](../ai-voice-marketing/research-implementation/persona-strategy.md)
  - [Top Conversion Strategies for AI Voice Marketing](../ai-voice-marketing/top-conversion-strategy.md)
- Index Pages
  - [Index of AI Voice Marketing Strategy Section Content](../ai-voice-marketing/index-section-site-map.md)
  - [AI Voice Marketing Strategies by Tactic Type Index](../ai-voice-marketing/index-section-site-map/tactic-types.md)
  - [AI Voice Marketing Strategies by Name Index](../ai-voice-marketing/index-section-site-map/strategy-name.md)
  - [AI Voice Marketing Strategies by Vocal Characteristic Index](../ai-voice-marketing/index-section-site-map/vocal-characteristics.md)
  - [AI Voice Marketing Strategies by Influence and Lead Type Index](../ai-voice-marketing/index-section-site-map/influence-lead-type.md)
  - [AI Voice Marketing Strategies by Outcome Results Index](../ai-voice-marketing/index-section-site-map/outcome-result-strategy.md)