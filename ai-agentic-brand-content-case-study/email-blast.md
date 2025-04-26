# Brand Email Campaign Workflow

## Overview
This Single-File Agent (SFA) workflow automates the process of creating, reviewing, and finalizing an email marketing campaign based on brand identity documents and content plans. The workflow is specifically designed for crafting emotionally resonant, brand-aligned email campaigns that drive engagement while maintaining authentic voice and messaging.

## Setup 

The workflow is set up by invoking the `sfa setup` command, including the path to the configuration file for this workflow `/use-case/doc-content-plan/doc-brand-email-config.json`. 

```bash
sfa setup doc-brand-email-config.json
```

## Workflow Phases

### 1. Initial Email Campaign Creation
- Takes brand identity and content plan as inputs
- Creates initial email campaign components:
  - Subject line with emotional gut check
  - Email body (2-3 paragraphs)
  - Call-to-action
- Outputs separate files for each component

### 2. Email Campaign Review
- Reviews draft email components against brand guidelines and best practices
- Evaluates:
  - Subject line effectiveness
  - Email body emotional resonance
  - CTA clarity and positioning
  - Overall flow and brand voice consistency
- Produces detailed review document with specific feedback

### 3. Final Campaign Optimization
- Incorporates review feedback
- Optimizes for mobile viewing
- Strengthens emotional elements
- Creates final, client-ready email campaign document
- Includes formatting and styling notes

## Usage

To run the workflow, execute the following command from the project root:

```bash
doc brand email
```

## Expected Outputs

The workflow generates the following files:

1. Initial Draft Components:
```
/use-case/doc-brand-email/
  ├── BRAND_EMAIL_SUBJECT.md
  ├── BRAND_EMAIL_BODY.md
  └── BRAND_EMAIL_CTA.md
```

2. Review Document:
```
/use-case/doc-brand-email/
  └── BRAND_EMAIL_REVIEW.md
```

3. Final Campaign:
```
/use-case/doc-brand-email/
  └── BRAND_EMAIL_FINAL.md
```

The final output combines all components into a single, formatted document ready for client review, with clear section headers and formatting guidelines for implementation.

## Directory Content 

**[Email Campaign for Glossier](../ai-agentic-brand-content-case-study/email-blast/glossier-email-campaign.md)**

**[Email Campaign for Hydro Flask](../ai-agentic-brand-content-case-study/email-blast/hydro-flask-email-campaign.md)**

**[Email Campaign Draft & Feedback All Brands](../ai-agentic-brand-content-case-study/email-blast/production-flow-email-blast.md)**