---
layout: research
title: Single-File Agent Architecture
description: A comprehensive overview of how Single-File Agents (SFAs) are structured and function, explaining their core design principles and technical implementation.
categories: ["Coding", "Designing"]
tags: ["Specific"]
content_types: ["Technical", "Framework"]
---

## What Makes SFA Architecture Unique

Single-File Agents (SFAs) represent a approach to AI tool development that prioritizes simplicity, portability, and functionality in a single Python file. Unlike traditional multi-file applications that require complex dependencies and configuration, SFAs encapsulate everything needed for operation in one coherent unit. 

## Core Architectural Principles

### Self-Contained Design

The entire agent operates from a single Python file, eliminating dependency management challenges and making deployment dramatically simpler. This same file, or the 'SFA', accrues more tools over time, is able to develop their own workflows after the flow has been activated, and in each phase of the ever-changing loops, they tend to decide to think about their next moves. 

### Variable Configuration

SFAs use a modular JSON configuration approach that allows for quick adaptation to different use cases without modifying the core codebase. The JSON is really just a normal prompt you'd message to a chat LLM, but broken into structured categories and default to included where to find context for their task as well as where to output the results of their work.

### Function-First Approach

The architecture prioritizes clear functional boundaries that make extending agent capabilities straightforward while maintaining core stability. The idea is to take any cognitive effort that isn't directly related to the task at hand, and move it into a function and part of the code, while designing it in a way that implies rather than directs.

### LLM Integration

SFAs leverage large language models through standardized API calls, providing a consistent interface while allowing different models to be used interchangeably. The SFA decide to take a more orchestrating approach to a task flow, looking at the big picture, delegating tasks to other agents who are sometimes called as tools and other times called to work in parallel. They've also got the option to work in sync, collaborating and communicating with the other model of your choice in real time.  

## Key Components

### Configuration Handler

The configuration system processes input JSON to determine agent behavior, allowing runtime customization without code changes. That is to say, literally nothing other than a new SFA file is needed to completely change the behavior of the agent from something like deep research to reviewing and creating meta data for images, to sending out updates on different Discord and Slack channels as needed. 

### API Connector

A standardized interface for communicating with various LLM services (OpenAI, Anthropic, etc.) that abstracts away provider-specific implementation details. In fact, tools like LiteLLM offer a single API call, or use of their SDK, to have access to over 100 different models. So next time you need a 1M token window for a giant document you can call in Gemini 2.5 Pro, which is still free, or call in o3-mini(high) and get an interactive digital animation of a ball bouncing around the inside of a 4D hyper cube with perfect physics.  

### Prompt Engineering Layer

A sophisticated system for constructing and managing prompts that incorporates variables, templates, and context management. Whether the AI is opting to add another phase of up to 20 loops and stay in their current content to keep working, or writing out details for the next LLM called in via their phase summary output document, every layer of what takes an SFA from generic to specific is a layered and carefully crafted prompt. 

### Data Processing Pipeline

Handles input and output formatting, ensuring consistent data flow throughout agent operations. From documents to imagery to markdown and JSON, the SFA is able to process and output in a wide variety of formats thanks to how the SFA is constructed. 

### Result Manager

Processes responses from the LLM and formats them according to project specifications. Again, here we're taking cognitive load off of our lead LLM wherever we can. Even the activation of a new workflow using the setup script results in a full README document all about the workflow, without our LLM, or human, having to do any of the heavy lifting. 

## Implementation Guidelines

When implementing the SFA architecture, follow these guidelines:

1. Maintain the single-file principle even when tempted to split functionality
   - Validate the SFA by coming up with two completely different workflows 
   - Run the workflows back to back, a truly modular system will be handle both with ease 
2. Use the standard JSON configuration format for all variable aspects
   - They're nothing more than a path for context, a location for a system prompt, and another for the task prompt 
   - Better yet, describe what you need to have done to a chat LLM and let them fill out the JSON template for you 
3. Implement the core functional interfaces consistently 
   - Does the SFA code look a little boring? Good 
   - With each addition, refactoring, or change, review the codebase in its entirety 
4. Keep API-specific code isolated and abstracted 
   - At first it might not seem easy to keep specifics out of the main SFA 
   - Give it time and contemplation and you'll soon see that the logic is a lot easier than you thought 
5. Document all functions and components thoroughly
   - Not just one technical document, but a few at different levels of detail, comprehension, and complexity 
   - Create a rule wherever possible to end any work on the SFA by updating all documents in the project directory 
   - We do this by cleaning up the directory

## See Also

- [SFA Basics](../building-successful-agents.md)
- [Technical Specifications](./technical-specifications.md)
- [Implementation Guide](./use-case-workflow-standardization.md)