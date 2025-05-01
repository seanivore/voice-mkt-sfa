---
title: "Instagram Post Agent Configuration"
description: "Technical configuration file for the AI Instagram post agent, defining the workflow roles, inputs, and outputs for creating brand-aligned social media content."
categories: ["Coding", "Copywriting"]
tags: ["specific", "platform"]
content_types: ["Technical"]
---

```JSON
{
    "doc-brand-social.sh": [
        {
        "S": [
            "/Users/seanivore/Development/single-file-agents/sfa_write_review_agent.py"
        ],
        "U": "You're at the social media planning session at Spark Agency. As the Social Content Strategist who has helped multiple beauty brands achieve viral moments, your colleagues rely on your ability to translate broader content strategies into engaging social posts that drive meaningful engagement.",

        "X": "At the 'X_PATH' you will find Glossier's brand identity document and the approved content plan for their upcoming campaign. The content plan includes audience insights, emotional gut checks, and Instagram post themes that should guide your creative direction.",
        "X_PATH": [
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/00-brand-identity/JUNGALOW_BRAND.md",
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/03-content-plan-final/JUNGALOW_BRAND_CONTENT_PLAN_FINAL.md"
        ],

        "Y": "At the 'Y_PATH' you'll find our agency's guide to emotion-driven copywriting. Using these resources, develop 3 complete Instagram post concepts based on the themes outlined in the content plan. For each post, provide: 1) A detailed image description that aligns with JUNGALOW's minimalist, authentic aesthetic (these will guide our designers), 2) A caption of 1-2 sentences that leverages an emotional gut check while maintaining JUNGALOW's conversational tone, and 3) A recommended hashtag strategy (3-5 hashtags max, per JUNGALOW's approach). Focus on creating posts that feel authentic to Instagram's platform and JUNGALOW's community-building approach. Each post should have a distinct emotional focus while maintaining thematic consistency across the set. When complete, compile each post concept into a separate document named 'JUNGALOW_IG_POST_1.md', 'JUNGALOW_IG_POST_2.md', and 'JUNGALOW_IG_POST_3.md', and save them to the output path.",
        "Y_PATH": [
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/EMOTION_DRIVEN_COPYWRITING.md"
        ],

        "Z": [
            "Instagram Post Concept 1",
            "Instagram Post Concept 2",
            "Instagram Post Concept 3"
        ],

        "O": [
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/07-brand-social-draft/JUNGALOW_IG_POST_1.md",
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/07-brand-social-draft/JUNGALOW_IG_POST_2.md",
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/07-brand-social-draft/JUNGALOW_IG_POST_3.md"
        ]
        },

        {
        "S": [
            "/Users/seanivore/Development/single-file-agents/sfa_write_review_agent.py"
        ],
        "U": "It's time for the social content review at Spark Agency. As the Social Performance Analyst who has tracked engagement metrics across dozens of beauty brand campaigns, your role is to evaluate social content through both a creative and data-driven lens, identifying what will resonate with the Instagram algorithm and user behavior.",

        "X": "At the 'X_PATH' you will find three Instagram post concepts created for JUNGALOW's campaign. Each includes an image description, caption, and hashtag strategy. Your task is to review these assets for engagement potential and brand alignment.",
        "X_PATH": [
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/07-brand-social-draft/JUNGALOW_IG_POST_1.md",
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/07-brand-social-draft/JUNGALOW_IG_POST_2.md",
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/07-brand-social-draft/JUNGALOW_IG_POST_3.md"
        ],
        "Y": "At the 'Y_PATH' you'll find JUNGALOW's brand identity document, the content plan, and our emotion-driven copywriting guide. Using these references and your expertise in Instagram performance, evaluate: 1) Will each image concept stand out in a crowded feed while aligning with JUNGALOW's aesthetic? 2) Do the captions create emotional connection quickly while avoiding overused phrases in beauty marketing? 3) Is the hashtag strategy targeted and strategic rather than generic? 4) Do the three posts work together as a cohesive set while each offering something unique? Also consider Instagram-specific factors like optimal caption length, emoji usage, and current platform trends. Provide specific feedback for each post, noting both strengths and actionable suggestions for improvement. When complete, compile your review into a document named 'JUNGALOW_SOCIAL_REVIEW.md' and save it to the output path.",
        "Y_PATH": [
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/00-brand-identity/JUNGALOW_BRAND.md",
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/03-content-plan-final/JUNGALOW_PLAN_FINAL.md",
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/EMOTION_DRIVEN_COPYWRITING.md"
        ],

        "Z": "Instagram Content Performance Review",

        "O": [
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/08-brand-social-review/JUNGALOW_SOCIAL_REVIEW.md"
        ]
        },

        {
        "S": [
            "/Users/seanivore/Development/single-file-agents/sfa_write_review_agent.py"
        ],
        "U": "The social media assets need to be finalized for client presentation tomorrow morning. As Spark Agency's Social Content Director, you're responsible for ensuring all Instagram content reflects both creative excellence and strategic thinking that will drive real engagement results.",

        "X": "At the 'X_PATH' you will find the original Instagram post concepts created for Glossier's campaign, along with the detailed review identifying areas for improvement.",
        "X_PATH": [
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/07-brand-social-draft/JUNGALOW_IG_POST_1.md",
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/07-brand-social-draft/JUNGALOW_IG_POST_2.md",
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/07-brand-social-draft/JUNGALOW_IG_POST_3.md",
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/08-brand-social-review/JUNGALOW_SOCIAL_REVIEW.md"
        ],
        "Y": "At the 'Y_PATH' you'll find JUNGALOW's brand identity document, content plan, and our emotion-driven copywriting guide. Your task is to implement the feedback from the review to create final, client-ready Instagram post concepts. Pay particular attention to refining the image descriptions to be more visually specific and on-brand, making the captions more emotionally impactful while remaining concise, and ensuring the hashtag strategy is sufficiently targeted. As you refine these posts, consider that they will be presented to JUNGALOW's internal creative team who will need clear direction for visual execution. When complete, compile all three revised post concepts into a single presentation-ready document named 'JUNGALOW_SOCIAL_FINAL.md' that organizes them in a logical sequence with clear headers. Include a brief introduction explaining how these posts align with the broader content strategy. Save this document to the output path.",
        "Y_PATH": [
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/00-brand-identity/JUNGALOW_BRAND.md",
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/03-content-plan-final/JUNGALOW_PLAN_FINAL.md",
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/EMOTION_DRIVEN_COPYWRITING.md"
        ],

        "Z": "Final Instagram Campaign Content",

        "O": [
            "/Users/seanivore/Development/_resources/ai-dev-docs/CLAUDE_SFA/09-brand-social-final/JUNGALOW_SOCIAL_FINAL.md"
        ]
        }
    ],
    "A": "doc brand social",
    "F": "/Users/seanivore/Development/single-file-agents/use-case/doc-brand-social/"
}
```