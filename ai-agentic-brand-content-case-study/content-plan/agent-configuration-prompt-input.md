---
title: "Content Plan Agent Configuration"
categories: ["Technical", "Implementation", "Strategies"]
tags: ["implementation", "technical", "strategy"]
content_types: ["Technical References", "Implementation Guides", "Strategy Documents"]
description: "Technical configuration file for the AI content planning agent, defining the workflow roles, inputs, and outputs for developing brand marketing strategies."
---

```JSON
{
    "doc-content-plan.sh": [
        {
        "S": [
            "/Users/seanivore/Development/single-file-agents/sfa_write_review_agent.py"
        ],
        "U": "You're in a strategy meeting at Spark Agency with the content planning team. As the senior content strategist, everyone relies on your ability to analyze brand identities and develop comprehensive content plans that connect emotionally with target audiences. Today you're starting the planning process for a new client campaign.",

        "X": "At the 'X_PATH' you will find brand identity documentation for COCA_COLA. This contains key information about their history, values, aesthetic, target audience, and market positioning. Your task is to thoroughly analyze this information to understand the core brand elements and emotional connections that should be emphasized in their content strategy.",
        "X_PATH": [
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/00-brand-identity/COCA_COLA_BRAND.md"
        ],

        "Y": "At the 'Y_PATH' you'll find our agency's guide to emotion-driven copywriting. Using this framework and the brand identity document, create a comprehensive content plan that includes: 1) 3-5 primary emotional gut checks that resonate with COCA_COLA's brand identity, 2) A 30-day content calendar with 4 email campaigns and 8 Instagram posts, each briefly described with their primary emotional hook, 3) Target audience segments with specific emotional triggers for each, and 4) Brand voice guidelines that maintain COCA_COLA's authentic, adventure-focused identity across all content. Focus on identifying content themes that authentically connect with the emotional aspects of outdoor lifestyle, sustainability, and community that align with COCA_COLA's approach. When complete, save your content plan as 'COCA_COLA_CONTENT_PLAN_DRAFT.md' to the output path.",
        "Y_PATH": [
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/EMOTION_DRIVEN_COPYWRITING.md"
        ],

        "Z": "Comprehensive Brand Content Plan",

        "O": [
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/01-content-plan-draft/COCA_COLA_CONTENT_PLAN_DRAFT.md"
        ]
        },

        {
        "S": [
            "/Users/seanivore/Development/single-file-agents/sfa_write_review_agent.py"
        ],
        "U": "The content planning team has gathered for the internal review session. As the Brand Strategy Director with over a decade of experience in outdoor and lifestyle marketing, your role is to evaluate content plans before they're presented to clients. Your colleagues value your ability to identify when strategies miss the mark emotionally or fail to align with current industry trends.",

        "X": "At the 'X_PATH' you will find the draft content plan created for COCA_COLA's upcoming campaign. Your task is to thoroughly review this plan for strategic effectiveness, emotional resonance, and alignment with COCA_COLA's unique position in the outdoor products market.",
        "X_PATH": [
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/01-content-plan-draft/COCA_COLA_CONTENT_PLAN_DRAFT.md"
        ],
        "Y": "At the 'Y_PATH' you'll find COCA_COLA's brand identity document and our agency's emotion-driven copywriting guide. Compare the draft content plan against these reference materials and your industry expertise. Evaluate: 1) Are the emotional gut checks authentic to COCA_COLA's brand identity or do they feel generic? 2) Does the content calendar provide sufficient variety while maintaining thematic coherence? 3) Are the audience segments accurately defined with appropriate emotional triggers? 4) Do the voice guidelines capture COCA_COLA's unique tone? Also consider whether the plan addresses current outdoor industry trends like sustainability, inclusivity, and adventure accessibility in a way that fits COCA_COLA's brand. Provide specific feedback on each section of the content plan, noting both strengths and suggestions for improvement. When complete, compile your review into a document named 'COCA_COLA_CONTENT_PLAN_REVIEW.md' and save it to the output path.",
        "Y_PATH": [
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/00-brand-identity/COCA_COLA_BRAND.md",
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/EMOTION_DRIVEN_COPYWRITING.md"
        ],

        "Z": "Strategic Content Plan Review",

        "O": [
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/02-content-plan-review/COCA_COLA_CONTENT_PLAN_REVIEW.md"
        ]
        },

        {
        "S": [
            "/Users/seanivore/Development/single-file-agents/sfa_write_review_agent.py"
        ],
        "U": "The client presentation is tomorrow morning, and the Creative Director has just handed you the draft content plan along with the review notes. As the Lead Content Strategist responsible for final deliverables, it's your job to implement the feedback while ensuring the plan remains cohesive and emotionally compelling.",

        "X": "At the 'X_PATH' you will find the draft content plan for COCA_COLA's campaign and the detailed review document identifying areas for improvement.",
        "X_PATH": [
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/01-content-plan-draft/COCA_COLA_CONTENT_PLAN_DRAFT.md",
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/02-content-plan-review/COCA_COLA_CONTENT_PLAN_REVIEW.md"
        ],
        "Y": "At the 'Y_PATH' you'll find the brand identity document and our emotion-driven copywriting guide. Your task is to implement the recommendations from the review document to create a final version of the content plan. Focus particularly on refining the emotional gut checks to be more specific to COCA_COLA, ensuring the content calendar has a logical progression, and making the voice guidelines more actionable for content creators. The Creative Director emphasized that this plan needs to be both strategically sound and easy for the client's team to implement, so include clear examples wherever possible. When complete, create a polished, presentation-ready document named 'COCA_COLA_CONTENT_PLAN_FINAL.md' and save it to the output path.",
        "Y_PATH": [
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/00-brand-identity/COCA_COLA_BRAND.md",
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/EMOTION_DRIVEN_COPYWRITING.md"
        ],

        "Z": "Final Content Strategy Plan",

        "O": [
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/03-content-plan-final/COCA_COLA_CONTENT_PLAN_FINAL.md"
        ]
        }
    ],
    "A": "doc content plan",
    "F": "/Users/seanivore/Development/single-file-agents/use-case/doc-content-plan/"
}
```