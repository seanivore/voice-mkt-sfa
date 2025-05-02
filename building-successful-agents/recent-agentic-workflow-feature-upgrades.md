---
title: Updating the SFA Main Loop
description: An overview of the most recent changes to the SFA main loop to include a new phase adjustment workflow.
categories: ["Coding"]
tags: ["applied"]
content_types: ["Guide"]
permalink: /building-successful-agents/recent-agentic-workflow-feature-upgrades/
---

# SFA Main Update: Phase Adjustment Workflow

After this, the agent will have complete control over crafting the work flow live as they work and as they decide what needs to come in what order to achieve whatever the goals may be. 

`sfa_main.py` for testing without affecting the original agent. Then retire `sfa_agent.py` along with any document from the updates at the time. 

## Key Components of the Implementation

1. Workflow Adjustment Tool

- Simple tool with two actions: **END_PHASE** and **ADD_PHASE**
- Clean, straightforward interface for Claude

2. Phase Reset Function

- Resets iteration counter without ending the phase
- Maintains the same Claude instance
- Adds a clear message to conversation history

3. Token Checking Integration

- Always checks tokens before saving
- Resets phase for revision if over limit
- Includes token count in output messages

4. Task Report Tool Update

- Standardized phase summary format
- Includes accomplishments, token counts, decisions, and next steps
- Triggers phase completion when saved

5. Main Loop Modifications

- Warns Claude before reaching max iterations
- Provides option to request more iterations
- Alternatively, allows for preparing information to hand off to the next phase and a new LLM 

Encourage decision making with consideration made for their context window. 

## Benefits of This Approach

- **Simplicity**: Clean, straightforward flow with minimal branching
- **Efficiency**: No unnecessary tracking of trigger sources
- **Consistency**: Standardized phase summary format
- **Flexibility**: Seamless handling of both ending and extending phases
- **Reliability**: Token checking integrated into the workflow

## Phase Adjustment Logic 

```plaintext
PHASE RUNNING (CLAUDE INSTANCE ACTIVE)
           |
           ↓
+---------------------+     "workflow_adjustment"
| End phase triggered | <-- "save_output"
+---------------------+     "complete_task"
           |
           ↓
  +----------------------+
  | Workflow adjustment? |   <-- Primary router
  +----------------------+
     /         |         \
  [NO]       [YES]       [YES]
   /           |           \
  ↓            ↓            ↓
[END PHASE]    |            |
  |            |            |
  |   +-------------+       |
  |   | ADD PHASE   |       |
  |   | TO WORKFLOW |       |
  |   |  AND END    |       |
  |   +-------------+       |
  |        ↓                |
  |        |       +--------------+
  |        |       | ADD PHASE TO |
  |        |       | WORKFLOW AND |
  |        |       | RESET LOOPS  | <-- Keep
  |        |       +--------------+     working
  |        ↓                |
  ↓        |                ↓
+---------------+           |
| < 7k tokens?  |           |
+---------------+           |
   /       \                |
  /         \               |
[YES]       [NO]------------+
  |                         |
  |                         |
  |                         |
  |                         |
  |                         |
+---------------------+     |
| Write Phase Summary |     |
+---------------------+     |
         |                  |
         |                  |
         ↓                  |
+--------------------+      |
| SAVE PHASE SUMMARY |      |
| SAVE OTHER OUTPUTS |      |
+--------------------+      |
         |                  |
         ↓                  ↓
         |        +---------------------+
         |        | START NEW PHASE     |
         |        | SAME CONTEXT WINDOW |
         |        +---------------------+
         |                  |
         |                  |
         ↓                  ↓
   [PHASE COMPLETE]     [NEXT PHASE]
         |                  |
         ↓                  ↓
 [WORKFLOW CONTINUES     [WORKFLOW
  OR COMPLETES]          CONTINUES]
```

### Comments for Each Section

1. End Phase Triggered

- Forwarded: `save_output` `complete_task` 
- To new tool: `adjust_workflow`

2. Adjust Workflow 

- No: Task Phase Done 
- Yes: Add Phase

3. If Adding Phase...

- Keep your context window 
- Add to workflow and exit phase 

4. Check Tokens 

- If you're exiting
- Even if adding workflow phase and exiting 

5. Over Or Under 7k Tokens 

- Under you can keep going 
- Over, you must keep contest and add phase 

6. Write Phase Summary 

- If you're exiting, write a summary 
- If you're adding a phase, provide info. for next agent

7. Save Outputs and Summary 

- Saving all planned outputs  
- Saving a summary 
- Exit is triggered 

8. Reset Loop Counter 

- If you were over 7k tokens 
- If you added a same-context window phase 
- You get your loop counter Reset
- Continue working 

9. Reset Phase Loops Ending Start Flow Again 
10. Next Phases Ending Start Flow Again 

### Overview of the Workflow

The key is that the control of the workflow is completely in the hands of the agent. If they were just planning out other tasks, they can add a new phase to the workflow for the next agent, and then leave a guide for them in the phase summary report. If they want to keep working or need to adjust the size of their output file, they get to stay in the same content, the loop counter reset, making it a "new phase" or reset phase. And of course, if you're done, then you just need to count the tokens of our output files, then write a phase summary report; saving these items will trigger actual completion of the phase. 