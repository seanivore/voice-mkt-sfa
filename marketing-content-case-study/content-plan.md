---
title: "Document Content Planning Workflow"
description: "Detailed workflow documentation for an AI-powered content planning system that develops, reviews, and refines brand content strategies through a three-phase agency simulation process."
categories: ["Coding"]
tags: ["specific"]
content_types: ["Case Study"]
---

# Document Content Planning Workflow

*Note: This is an example of of the automatically generated README created when setting up a new workflow. It is not a part of the workflow itself.*

## Overview
This Single-File Agent workflow automates the process of creating a comprehensive content strategy for a brand. The workflow simulates a professional marketing agency's content planning process, from initial strategy development through review and final refinement.

## Setup 

The directives were provided by the user as a prompt that was broken down into a collection of variables representing the provided resources, the directions, and the expected outputs. That 'configuration' document is located at `/use-case/doc-content-plan/doc-content-plan-config.json`. 

First the workflow is set up by invoking the `sfa setup` command. 

```bash
sfa setup doc-content-plan-config.json
```

This command reviews the configuration file and first produces this very README.md file. It then produces a script that integrates the configuration into the SFA framework. One of the variables in the configuration file is the command that will execute the workflow. The setup finished up by making that command executable. 

## Workflow Phases

This is an overview of what the configuration file is directing the workflow to do. Each of these is a phase which calls an agent to perform a task. In this flow the agents create content, then review it, then refine it. 

### 1. Initial Content Plan Development
- Agent Role: Senior Content Strategist
- Analyzes brand identity documentation
- Creates initial content plan including:
  - Emotional gut checks
  - 30-day content calendar
  - Target audience segments
  - Brand voice guidelines
- Output: `BRAND_CONTENT_PLAN_DRAFT.md`

### 2. Strategic Review
- Agent Role: Brand Strategy Director
- Reviews draft content plan
- Evaluates strategic effectiveness and emotional resonance
- Provides detailed feedback on all sections
- Output: `BRAND_CONTENT_PLAN_REVIEW.md`

### 3. Final Plan Refinement
- Agent Role: Lead Content Strategist
- Implements review feedback
- Refines emotional elements and strategic components
- Creates presentation-ready final document
- Output: `BRAND_CONTENT_PLAN_FINAL.md`

## Usage 

Run the workflow using the following command. Brand identity documents are provided in the `use-case/doc-content-plan/resources` directory. 

```bash
doc content plan
```

## Expected Outputs

The workflow will generate three documents in sequence:

1. `/use-case/doc-content-plan/BRAND_CONTENT_PLAN_DRAFT.md`
   - Initial content strategy draft

2. `/use-case/doc-content-plan/BRAND_CONTENT_PLAN_REVIEW.md`
   - Detailed review and feedback

3. `/use-case/doc-content-plan/BRAND_CONTENT_PLAN_FINAL.md`
   - Polished, final content strategy plan

Each document builds upon the previous one, creating a complete content planning process from initial concept to final deliverable.

## Requirements
- Single-File Agents framework
- Access to specified resource files:
  - BRAND brand identity documentation
  - Emotion-driven copywriting guide

## Notes

The results are impressive for the ~200-some words of the brand identity documentation. The workflow is able to create a comprehensive content plan that is both strategic and emotionally engaging. The marketing plan is particularly impressive, detailed, and thoughtful. We also rather enjoyed the Instagram post ideas as they were spot on for the brand voice and tone, and the content was rather trendy and fun. 

## Directory Content 

**[Content Plan for Jungalow](../marketing-content-case-study/content-plan/jungalow-content-plan.md)**

**[Content Plan for Glossier](../marketing-content-case-study/content-plan/glossier-content-plan.md)**

**[Content Plan for Hydro Flask](../marketing-content-case-study/content-plan/hydro-flask-content-plan.md)**

**[Content Plan Draft & Feedback All Brands](../marketing-content-case-study/content-plan/production-flow-content-plan.md)**

