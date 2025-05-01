# Variable-Input Single-File Agent (SFA) Standardization

## Intention 

Clearly layout the means for standardization and validation of any SFA. 

## Validation 

- Functional Validation 
The goal or intention in designing any SFA is that all that is required to use it for a use-case is to prepare a standardized JSON object containing variable values. 

- Logic Validation 
When describing the logic of how variables work in a new SFA, the ability to come up with two use-cases for which the variable values are easily identified will clue you in as if if the logic is sound. 

- JSON Object Validation 
Once the variables meanings are defined, create a template JSON object. Following the template will suffice as validation. 

- Universal Setup Script Validation 
Given any JSON object, nothing else, it will write a script that applies the indicated variable values to the indicated SFA, and then it set up to execute according to the indicated command variable. 

- SFA Validation 
If all that is required to use a SFA is the command provided, running the SFA with the JSON object, then the SFA would be validated after two different use-cases both complete successfully. 

### Full Validation Flow 

1. Define universal variable keys 
2. Create template JSON object 
3. Identify SFA logic 
4. Identify two use-cases that fit the SFA logic 
5. Fill out JSON objects with variable values for both use-cases 
6. Write python code for the SFA 
7. Create universal setup script* 
8. Use setup script once per use-case's JSON object* 
9. Run each use-case's custom command 
10. If both use-cases complete successfully, all elements are validated 

## JSON Object Standardization 

### Universal Variables 

| Variable  | Standard Description                                   | Task Agent Examples                  |
| --------- | ------------------------------------------------------ | ------------------------------------ |
| -- S      | what SFA to use                                        | `/path/to/task_agent.py`             |
| -- U      | Goal; Agent's system message task overview statement   | `You're an expert writer who...`     |
| -- X      | Topic; 'WHAT' task is happening to                     | `Write about X_PATH...`              |
| -- X_PATH | Input-1; array of file paths or directory of files     | `/path/to/input-1.md`                |
| -- Y      | Details; 'HOW' task is to happen                       | `Use Y_PATH to write...`             |
| -- Y_PATH | Input-2; array of file paths or directory of files     | `/path/to/input-2.md`                |
| -- Z      | Format of output; prompt context unless protocol sent  | `List, analysis, outline, logs`      |
| -- O      | Output path                                            | `"/path/to/TASK_LOG.md"`             |
| -- A      | Command; added to shell by script to activate use-case | `"[task] [use-case-term] [variant]"` |
| -- F      | Path to the Use-Case's sub-directory; JSON location    | `./use-case/<directory-name>/`       |

### Breakdown of Variables 
- S PATH — the absolute path to the SFA python file that these variables are intended to be used with 
- U — one sentence describing what the agent is trying to accomplish, taking it a step further the python task "research" or "writing" 
- X — this is **WHAT** the task is happening to, which might be a sentence, few words, or a path to a document 
- X PATH — second 'X' is always included, but will say 'N/A' unless there is a path to be included for 'X'  
- Y — this is **HOW** the task should be done, which might be a protocol, an outline, or a few sentence description of what to do
- Y PATH — second 'Y' is always included, but will say 'N/A' unless there is a path to be included for 'Y'  
- Z — This is the format of the output, a list, analysis, outline, etc. and can get as simple or specific as needed 
- O — This is the path to the output, which will be used as input for the next agent or task completion 
- A — This is the command that will be added to the shell by the setup script to activate the use-case variant 
- F — This is the path to the Use-Case's sub-directory; JSON location 

See a detailed example of a use-case with variables in the [JSON_EXAMPLES.json](./JSON_EXAMPLE.json) file. 

## Command Writing Protocol 

### Command Structure 

#### For Each Agent & Phase In The Use-Case

  1    2    3
agent use variant

1. 'agent' 
   - The first word of any SFA use-case command represents the agent 
   - All use-cases that use the same agent will have the same first word of their custom command. 
   - **New SFA needs the command checked; run through terminal with `which` to see if it is already in use.** 
2. 'use-case' 
   - The second word of the command is the use-case grouping or category. 
   - All the steps in the use-case will have this second word. 
3. 'variant' 
   - The third word of the command is a variant of the specific use-case. 
   - This is what differentiates the different steps in the use-case. 

#### For The Entire Use-Case Flow 

There will also need to be a command for running the entire flow of the new SFA use-case. 

- Since this is specific to the use-case the standardization is less strict. 
  - I.e. the only time this command is used is to run the entire flow. 
  - E.g. when you are doing the same thing as when it was set up. 
- Try to make it similar to the other commands but, 
  - Don't use the same first word if the flow uses multiple agents

GENERAL RULE OF THUMB: *The goal is that it be helpful for humans to use* 

Make sure it follow the rest of the rules below, otherwise just make sure it makes sense. 

### Command Writing Rules 

**Always avoid** these in a command:

  1. No plural 
  2. No present participle verbs (gerunds with helping verbs)
  3. No punctuation like hyphens
  4. No past tense verbs (e.g. `wrote`, `finished`, etc.)

**Always use** these in a command: 

   1. Use the simplest grammatical form of the word 
   2. Use present tense 
   3. Abbreviate when it is sensible 
   4. Be short and concise 

## Directory Organizational Protocol 

### SFA Files & Documentation 

Agent python file naming structure: `sfa_<purpose>_agent.py` 
Documentation: `README.md`

  - Project directory README.md file in project root 
  - Once validated, an agent's SFA python file is moved out of the workbench and into the main project root 
  - The SFA is added to the main README.md file with a sentence or two to describe what it does *IN GENERAL* 
  - README.md includes all other standard README.md information with *no use-case-specifics*. 

### Setup Scripts 

General script run with any new JSON: `use-case-variant-setup.sh` 
General script to run the entire use-case agentic flow: `use-case-agentic-flow-setup.sh` 

### Use-Case Files & Documentation 
Each new use-case gets a sub-directory: `./sfa-use-cases/<use-case-name>/` 
Documentation: `README.md` 
Variables: `use-case-variant-config.json` 
Variant scripts: `<agent-use-variant>.sh` 
Use-case flow script: `<use-case-name>-agentic-flow.sh`

  - The README.md file defines the use case logic, the SFA to be used, and overall agentic flow. 
  - For each phase of the use-case, e.g. each SFA that is run, needs variables defined in a JSON file. 
  - When run with the general setup script, the JSON files produce scripts to run each phase of the use-case. 
  - The final script will run the entire use-case flow. 
 