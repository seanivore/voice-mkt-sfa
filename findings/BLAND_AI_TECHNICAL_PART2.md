# Bland AI Technical Guide - Part 2: Workflow Builder

## Table of Contents

1. [Introduction](#introduction)
2. [Workflow Builder Architecture](#workflow-builder-architecture)
3. [Branching Conversation System](#branching-conversation-system)
4. [Logic Implementation](#logic-implementation)
5. [Conversation Pathways](#conversation-pathways)
6. [Advanced Features and Integration](#advanced-features-and-integration)
7. [Best Practices](#best-practices)

## Introduction

This technical guide focuses on Bland AI's workflow builder capabilities, specifically the Conversational Pathways system that enables the creation of sophisticated, branching AI phone conversations. Bland AI's approach to conversation design leverages a visual, node-based architecture that allows for precise control over conversation flow while maintaining natural-sounding interactions.

Conversational Pathways represent Bland AI's solution for creating structured yet flexible AI phone agents that can handle complex decision trees, integrate with external systems, and adapt to user responses in real-time. This guide will explore the technical components of this system and provide practical implementation examples.

## Workflow Builder Architecture

### Core Components

Bland AI's workflow builder is built around two primary components:

1. **Nodes**: Individual blocks representing specific conversation points or actions
2. **Pathways**: Connections between nodes that determine conversation flow

This architecture follows a flowchart-like structure, where each node contains instructions for the AI agent, and pathways determine how the conversation progresses based on user responses.

### Node Types

Bland AI's workflow builder supports several specialized node types, each serving a specific function in the conversation flow:

#### Default Node

The standard node type for conversation handling. It contains instructions for the AI agent on what to say or ask at that point in the conversation.

```json
{
  "id": "node_1",
  "type": "Default",
  "data": {
    "name": "Introduction",
    "prompt": "Introduce yourself as a customer service representative for Acme Inc. Ask how you can help the customer today.",
    "isStart": true
  }
}
```

Default nodes can be configured to use either:
- **Dynamic AI-generated responses**: The AI generates appropriate dialogue based on the prompt
- **Static text**: Fixed responses that are always delivered exactly as written

#### End Call Node

Terminates the conversation with an optional closing message.

```json
{
  "id": "node_end",
  "type": "End Call",
  "data": {
    "name": "End Conversation",
    "prompt": "Thank the customer for their time and end the call politely."
  }
}
```

#### Transfer Call Node

Transfers the current call to a different phone number, such as a human agent or another department.

```json
{
  "id": "node_transfer",
  "type": "Transfer Call",
  "data": {
    "name": "Transfer to Sales",
    "prompt": "Inform the customer you'll transfer them to the sales team who can better assist with their inquiry.",
    "transferNumber": "+15551234567"
  }
}
```

#### Knowledge Base Node

Provides the AI agent with access to specific information to answer user questions.

```json
{
  "id": "node_kb",
  "type": "Knowledge Base",
  "data": {
    "name": "Product Information",
    "prompt": "Use this information to answer questions about our product specifications.",
    "knowledgeBase": "Product X specifications: Weight: 2.5kg, Dimensions: 30x20x10cm, Battery life: 8 hours..."
  }
}
```

#### Webhook Node

Executes HTTP requests to external systems during the conversation, allowing for real-time data retrieval or updates.

```json
{
  "id": "node_webhook",
  "type": "Webhook",
  "data": {
    "name": "Check Order Status",
    "prompt": "I'll check your order status right away.",
    "webhookUrl": "https://api.example.com/orders/{order_id}",
    "method": "GET",
    "headers": {
      "Authorization": "Bearer {api_key}"
    },
    "responsePrompt": "Tell the customer their order status based on the webhook response."
  }
}
```

#### Wait for Response Node

Similar to the Default Node but specifically designed to handle situations where the user needs time to respond or might put the call on hold.

```json
{
  "id": "node_wait",
  "type": "Wait for Response",
  "data": {
    "name": "Collect Order Number",
    "prompt": "Ask for the customer's order number and wait patiently if they need time to find it.",
    "maxWaitTime": 60
  }
}
```

### Node Configuration

Each node can be configured with various parameters:

- **Name**: Descriptive label for the node
- **Prompt**: Instructions for the AI on what to say or how to respond
- **Conditions**: Requirements that must be met before proceeding
- **Static Text**: Optional fixed text to be spoken instead of AI-generated responses
- **Node-specific parameters**: Additional settings based on node type

## Branching Conversation System

Bland AI's branching conversation system allows for dynamic, non-linear conversations that can adapt to user responses and follow different paths based on the context.

### Pathway Creation

Pathways connect nodes and determine the possible conversation flows. To create a pathway:

1. Select the source node (where the pathway begins)
2. Connect it to a target node (where the pathway leads)
3. Define the conditions under which this pathway should be followed

Visually, pathways appear as dotted lines connecting the nodes in the workflow builder interface.

### Decision Points

Decision points occur when multiple pathways branch from a single node. The AI agent must decide which pathway to follow based on the user's response and the defined conditions.

Example of a node with multiple pathways:

```json
{
  "id": "decision_node",
  "type": "Default",
  "data": {
    "name": "Service Options",
    "prompt": "Ask if the customer is interested in our Basic or Premium service plan."
  },
  "pathways": [
    {
      "id": "path_basic",
      "target": "basic_service_node",
      "label": "Customer chooses Basic",
      "description": "Select this pathway if the customer expresses interest in the Basic service plan."
    },
    {
      "id": "path_premium",
      "target": "premium_service_node",
      "label": "Customer chooses Premium",
      "description": "Select this pathway if the customer expresses interest in the Premium service plan."
    },
    {
      "id": "path_undecided",
      "target": "more_info_node",
      "label": "Customer needs more information",
      "description": "Select this pathway if the customer is undecided or requests more information about the plans."
    }
  ]
}
```

### Pathway Labels and Descriptions

Pathway labels and descriptions help the AI agent determine which path to follow:

- **Labels**: Short descriptions of the condition (e.g., "Customer says yes")
- **Descriptions**: More detailed explanations of when to follow this pathway (e.g., "Select THIS PATHWAY IF the customer explicitly agrees to the offer")

The AI uses these labels and descriptions to match the user's response to the appropriate pathway, creating a natural conversation flow.

## Logic Implementation

Bland AI's workflow builder includes several mechanisms for implementing logic in conversations.

### Node Conditions

Conditions can be set on nodes to ensure specific criteria are met before proceeding. If the condition is not met, the AI agent will remain at the current node and continue to work toward fulfilling the condition.

Example condition:

```
"You must get the date, time, and number of guests for this reservation"
```

With this condition, the AI agent will stay at the current node until it has collected all three pieces of information (date, time, and number of guests).

### Variable Extraction and Comparison

The AI can extract variables from user responses and use them for conditional logic:

```json
{
  "condition": {
    "type": "comparison",
    "variable": "guest_count",
    "operator": ">",
    "value": 8,
    "pathwayIfTrue": "large_party_node",
    "pathwayIfFalse": "standard_reservation_node"
  }
}
```

In this example, if the extracted `guest_count` is greater than 8, the conversation will follow the pathway to the "large_party_node"; otherwise, it will proceed to the "standard_reservation_node".

### Global Nodes

Global nodes are a powerful feature that can be accessed from any point in the conversation. They're particularly useful for handling:

- Interruptions
- Common requests that might occur at any time
- Emergency situations or escalations

A global node has implicit connections to all other nodes in the workflow. When triggered, the AI executes the global node's instructions and then either:

1. Returns to the previous node (automatic return)
2. Follows a specified pathway to another node (redirection)
3. Continues based on new pathway conditions from the global node

Example global node configuration:

```json
{
  "id": "global_transfer",
  "type": "Default",
  "data": {
    "name": "Transfer to Human Agent",
    "prompt": "Apologize to the customer and offer to transfer them to a human agent.",
    "isGlobal": true,
    "autoReturn": false,
    "enableForwarding": true,
    "forwardToNode": "transfer_node"
  }
}
```

This global node can be triggered from any point in the conversation when the AI detects that the customer wants to speak to a human agent.

### Loop Conditions

Loop conditions allow the AI to repeat a node until certain criteria are met:

```json
{
  "id": "verification_node",
  "type": "Default",
  "data": {
    "name": "Verify Identity",
    "prompt": "Ask for the customer's account number and last four digits of their SSN for verification. Keep asking until you have both pieces of information.",
    "loopCondition": "Continue asking until you have both the account number AND the last four digits of their SSN."
  }
}
```

## Conversation Pathways

Conversation pathways in Bland AI represent the overall flow and structure of the AI phone conversation.

### Pathway Initialization

Every conversation pathway begins with a designated start node, marked with the `isStart: true` property. This is the entry point for the conversation.

```json
{
  "id": "start_node",
  "type": "Default",
  "data": {
    "name": "Greeting",
    "prompt": "Greet the customer warmly and introduce yourself as an AI assistant for Acme Inc.",
    "isStart": true
  }
}
```

### Pathway Navigation

The AI agent navigates through the conversation by:

1. Executing the current node's instructions
2. Listening to the user's response
3. Determining which pathway to follow based on the response and pathway conditions
4. Moving to the next node and repeating the process

This continues until an End Call node is reached or the user terminates the call.

### Dynamic vs. Static Responses

Bland AI supports both dynamic AI-generated responses and static text responses:

- **Dynamic responses**: The AI generates appropriate dialogue based on the prompt and context
- **Static responses**: Fixed text that is always delivered exactly as written

Example node with static text:

```json
{
  "id": "legal_disclaimer",
  "type": "Default",
  "data": {
    "name": "Legal Disclaimer",
    "staticText": "This call may be recorded for quality and training purposes. Your information will be handled according to our privacy policy at example.com/privacy.",
    "useStaticText": true
  }
}
```

### Conversation Control

Additional controls for managing the conversation include:

- **Interruption threshold**: Controls how sensitive the AI is to user interruptions
- **Skip user response**: Allows the AI to continue without waiting for user input
- **Block interruptions**: Prevents the AI from being interrupted during critical information delivery

```json
{
  "id": "important_info",
  "type": "Default",
  "data": {
    "name": "Critical Information",
    "prompt": "Explain the important safety information clearly and completely.",
    "blockInterruptions": true,
    "interruptionThreshold": 0.9
  }
}
```

## Advanced Features and Integration

### Webhook Integration

Webhook nodes allow the AI agent to interact with external systems during the conversation:

```json
{
  "id": "appointment_webhook",
  "type": "Webhook",
  "data": {
    "name": "Schedule Appointment",
    "prompt": "I'll schedule that appointment for you right away.",
    "webhookUrl": "https://api.example.com/appointments",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json",
      "Authorization": "Bearer {api_key}"
    },
    "body": {
      "customer_name": "{customer_name}",
      "appointment_date": "{appointment_date}",
      "appointment_time": "{appointment_time}",
      "service_type": "{service_type}"
    },
    "responsePrompt": "Confirm the appointment details with the customer based on the response from the scheduling system."
  }
}
```

This allows the AI to perform actions like:
- Checking order status
- Scheduling appointments
- Updating customer information
- Processing payments
- Sending confirmation emails or SMS

### Knowledge Base Integration

Knowledge Base nodes provide the AI with specific information to reference during the conversation:

```json
{
  "id": "product_kb",
  "type": "Knowledge Base",
  "data": {
    "name": "Product Specifications",
    "knowledgeBase": "Product X specifications:\n- Price: $299.99\n- Dimensions: 10" x 8" x 2"\n- Weight: 1.5 lbs\n- Battery life: 12 hours\n- Warranty: 2 years\n\nProduct Y specifications:\n- Price: $499.99\n- Dimensions: 12" x 10" x 3"\n- Weight: 2.2 lbs\n- Battery life: 18 hours\n- Warranty: 3 years",
    "prompt": "Use this information to answer any specific questions about our products X and Y."
  }
}
```

### API Integration

The entire Conversational Pathways system can be managed via Bland AI's API, allowing for programmatic creation and modification of workflows:

```bash
# Create a new pathway
curl --request POST \
  --url https://api.bland.ai/v1/pathway \
  --header 'Content-Type: application/json' \
  --header 'authorization: YOUR_API_KEY' \
  --data '{
  "name": "Customer Support Pathway",
  "description": "Handles general customer inquiries and support requests",
  "nodes": [...],
  "edges": [...]
}'

# Update an existing pathway
curl --request POST \
  --url https://api.bland.ai/v1/pathway/PATHWAY_ID \
  --header 'Content-Type: application/json' \
  --header 'authorization: YOUR_API_KEY' \
  --data '{
  "name": "Updated Customer Support Pathway",
  "description": "Improved flow for handling customer inquiries",
  "nodes": [...],
  "edges": [...]
}'
```

## Best Practices

### Designing Effective Nodes

1. **Clear prompts**: Write clear, specific instructions for the AI agent
2. **Single purpose**: Each node should focus on a single task or question
3. **Natural transitions**: Ensure smooth transitions between nodes
4. **Error handling**: Include pathways for unexpected responses

### Optimizing Branching Logic

1. **Limit complexity**: Avoid overly complex decision trees
2. **Descriptive labels**: Use clear, descriptive labels for pathways
3. **Default paths**: Always include a default path for unexpected responses
4. **Test thoroughly**: Test all possible conversation paths

### Conversation Flow Tips

1. **Start simple**: Begin with a basic flow and add complexity gradually
2. **Use global nodes**: Implement global nodes for common interruptions
3. **Balance control and flexibility**: Allow the AI some flexibility while maintaining control over critical paths
4. **Monitor and refine**: Use the live call logs to monitor conversations and refine your workflow

---

This technical guide provides a comprehensive overview of Bland AI's workflow builder architecture, branching conversation system, logic implementation, and conversation pathways. By leveraging these powerful features, developers can create sophisticated AI phone agents capable of handling complex conversations while maintaining natural, human-like interactions.