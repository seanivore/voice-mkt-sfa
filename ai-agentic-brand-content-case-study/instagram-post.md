# Social Media Content Development Workflow

## Overview
This Single-File Agent (SFA) workflow automates the development of social media content for brands, specifically focusing on creating, reviewing, and finalizing Instagram posts. The workflow simulates a professional agency process, moving from initial content creation through review to final client-ready deliverables.

## Setup 

The workflow is set up by invoking the `sfa setup` command, including the path to the configuration file for this workflow `/use-case/doc-content-plan/doc-brand-social-config.json`. 

```bash
sfa setup doc-brand-social-config.json
```

## Workflow Phases

### Phase 1: Content Creation
- Takes brand identity and content plan as inputs
- Creates 3 distinct Instagram post concepts
- Each post includes image description, caption, and hashtag strategy
- Outputs individual markdown files for each post concept

### Phase 2: Content Review  
- Analyzes draft posts for engagement potential and brand alignment
- Evaluates image concepts, captions, and hashtag strategies
- Considers Instagram-specific performance factors
- Produces detailed review document with actionable feedback

### Phase 3: Content Finalization
- Implements review feedback to refine all posts
- Enhances visual descriptions and emotional impact
- Optimizes for presentation to client's creative team
- Creates single consolidated final deliverable document

## Usage

Run the workflow using the following command:

```bash
doc brand social
```

## Expected Outputs

The workflow generates the following files:

1. Draft Posts (`/use-case/doc-brand-social/`)
   - `BRAND_IG_POST_1.md`
   - `BRAND_IG_POST_2.md`
   - `BRAND_IG_POST_3.md`

2. Review Document (`/use-case/doc-brand-social/`)
   - `BRAND_SOCIAL_REVIEW.md`

3. Final Deliverable (`/use-case/doc-brand-social/`)
   - `BRAND_SOCIAL_FINAL.md`

Each output builds upon the previous phase, culminating in a client-ready presentation document that includes refined Instagram posts aligned with the brand's content strategy.

## Directory Content 

**[Instagram Post for Glossier](../ai-agentic-brand-content-case-study/instagram-post/glossier-instagram-posts.md)**

**[Instagram Post for Hydro Flask](../ai-agentic-brand-content-case-study/instagram-post/hydro-flask-instagram-posts.md)**

**[Instagram Post Draft & Feedback All Brands](../ai-agentic-brand-content-case-study/instagram-post/production-flow-instagram-posts.md)**