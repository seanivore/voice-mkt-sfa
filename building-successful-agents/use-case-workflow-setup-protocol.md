# Setup Protocol for SFA Use Cases

## Overview

This guide walks you through creating a new use case for the Single File Agents framework. Use this alongside the reference documents for detailed specifications.

## Reference Documents 

- `STANDARDIZATION.md` — Detailed specifications for variables and naming conventions
- `JSON_VARIABLE_EXAMPLES.md` — Example configurations for different use cases

## Step-by-Step Process

### 1. Create Use Case Directory

Create a dedicated directory for your use case:

```bash
mkdir use-case/your-use-case-name
```

Name this directory according to the command you'll use to run it, following naming conventions in `STANDARDIZATION.md`.

### 2. Create Configuration File

Create a JSON configuration file for your use case:

```bash
touch use-case/your-use-case-name/your-use-case-name-config.json
```

### 3. Define Use Case Variables

Edit your configuration file to define all necessary variables:

- Write detailed instructions as you would for an LLM prompt
- Specify input/output paths and formats
- Define command structure and parameters
- Reference `JSON_VARIABLE_EXAMPLES.md` for examples

### 4. Define New Agents (Optional)

If your use case requires new agent types:

```bash
touch agent-workbench/your-agent-name.md
```

Keep agent definitions generic and reusable across multiple use cases.

### 5. Run Setup Script

Generate your use case workflow:

```bash
sfa setup your-use-case-name-config.json
```

This creates:
- Executable script for your workflow
- README documentation for your use case

### 6. Test Your Workflow

Verify that your workflow runs as expected:

```bash
cd use-case/your-use-case-name
./your-use-case-name.sh
```

Or use the custom command if you've set one up:

```bash
your custom command
```

### 7. Use Your Agentic Workflow

Once testing is complete, your workflow is ready for regular use.

## Troubleshooting

If your workflow doesn't run as expected:

1. Verify your configuration file format (valid JSON)
2. Check that all file paths are correct
3. Ensure input files exist in the specified locations
4. Verify API keys are properly set in your environment
5. Look for error messages in the console output
