# Sample JSON Object for Variable-Input Workflow

```json
{
    "carrots-script.sh": [
        {
        "TASK_1": [
            {
            "S": ["sfa_agent.py"],
            "U": "Description of the agent.",
            "X": "See the resource file named 'DOC_1'. Please review it and complete the requested research at the URL provided. Identify one core tactical approach from each, and then create a simple, easy to read, document. You may do more research if need. If you do, include sources.",
            "X_PATH": [
                "/Users/seanivore/Development/single-file-agents/use-case/carrots/CARROTS.md",
                "https://github.com/carrots-ai/mcp-get-carrots-fast/"
            ],
            "Y": "When complete, save the document appending 'DRAFT_1' to the end of the file name and then make a decision according to what you believe the document needs most next, before it gets a final review.",
            "Y_PATH": [
                "1. More research",
                "2. More examples",
                "3. Simplify language"
            ],
            "Z": [
                "Detailed Next Steps",
                "Updated Document"
            ],
            "O": [
                "/Users/seanivore/Development/single-file-agents/use-case/carrots/CARROTS_DRAFT_1.md",
                "/Users/seanivore/Development/single-file-agents/use-case/carrots/decision_1.json"
            ]
            }
            ]
        },
        {
        "DECISION_1": [
            {
            "S": ["sfa_agent.py"],
            "U": "Description of research agent.",
            "X": "Check the resources for two files. Review 'decision_1.json' for a description of research to be completed. Detail your findings in 'CARROTS_DRAFT_1.md'.",
            "X_PATH": [
                "/Users/seanivore/Development/single-file-agents/use-case/carrots/decision_1.json",
                "/Users/seanivore/Development/single-file-agents/use-case/carrots/CARROTS_DRAFT_1.md"
            ],
            "Y": "After you are finished, save the document appending 'DRAFT_2' to the end of the file and send it for final review.",
            "Y_PATH": [],
            "Z": "Document prepared for final review",
            "O": "/Users/seanivore/Development/single-file-agents/use-case/carrots/CARROTS_DRAFT_2.md"
            }
            ]
        },
        {
        "DECISION_2": [
            {
            "S": ["sfa_agent.py"],
            "U": "Description of research agent.",
            "X": "Check the resources for two files. Review 'decision_2.json' for a description of examples to add to the document 'CARROTS_DRAFT_1.md'.",
            "X_PATH": [
                "/Users/seanivore/Development/single-file-agents/use-case/carrots/decision_2.json",
                "/Users/seanivore/Development/single-file-agents/use-case/carrots/CARROTS_DRAFT_1.md"
            ],
            "Y": "After you are finished, save the document appending 'DRAFT_2' to the end of the file and send it for final review.",
            "Y_PATH": [],
            "Z": "Document prepared for final review",
            "O": "/Users/seanivore/Development/single-file-agents/use-case/carrots/CARROTS_DRAFT_2.md"
            }
            ]
        },
        {
        "DECISION_3": [
            {
            "S": ["sfa_agent.py"],
            "U": "Description of research agent.",
            "X": "Check the resources for two files. Review 'decision_3.json' for a description of the major edits the document 'CARROTS_DRAFT_1.md' needs.",
            "X_PATH": [
                "/Users/seanivore/Development/single-file-agents/use-case/carrots/decision_3.json",
                "/Users/seanivore/Development/single-file-agents/use-case/carrots/CARROTS_DRAFT_1.md"
            ],
            "Y": "After you are finished, save the document appending 'DRAFT_2' to the end of the file and send it for final review.",
            "Y_PATH": [],
            "Z": "Document prepared for final review",
            "O": "/Users/seanivore/Development/single-file-agents/use-case/carrots/CARROTS_DRAFT_2.md"
            }
            ]
        },
        {
        "REVIEW_TASK": [
            {
            "S": ["sfa_agent.py"],
            "U": "Description of research agent.",
            "X": "At the 'X_PATH' find 'CARROTS_DRAFT_2.md'. Review the document for accuracy and completeness.",
            "X_PATH": ["/Users/seanivore/Development/single-file-agents/use-case/carrots/CARROTS_DRAFT_2.md"],
            "Y": "After you are finished, save the document appending 'FINAL' to the end of the file and send it for final review.",
            "Y_PATH": [],
            "Z": "Final document",
            "O": "/Users/seanivore/Development/single-file-agents/use-case/carrots/CARROTS_FINAL.md"
            }
            ]
        }
    ],  
        "A": "best doc update",
        "F": "User/seanivore/Development/single-file-agents/use-case/best-doc-update/"
}
```