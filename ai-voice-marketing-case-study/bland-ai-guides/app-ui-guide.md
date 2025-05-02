---
title: "Bland AI User Interface Guide"
description: "Comprehensive guide to navigating and utilizing the Bland AI user interface, featuring detailed walkthroughs of dashboard functions, campaign creation, workflow building, and analytics features."
categories: ["Vocal Engineering", "Planning"]
tags: ["applied", "platform", "specific"]
content_types: ["Guides", "References", "Technical"]
permalink: /ai-voice-marketing-case-study/bland-ai-guides/app-ui-guide/
---

# Bland AI User Interface Guide

## Introduction

This guide provides a comprehensive overview of Bland AI's user interface, focusing on practical instructions for non-technical users. Bland AI is a conversational AI platform that enables businesses to automate phone calls with ultra-realistic AI voice agents. The platform can handle both inbound and outbound calls for various use cases including sales, customer service, appointment scheduling, and more.

This guide will walk you through the main components of Bland AI's interface, including the dashboard, workflow builder, campaign creation process, and other key features.

## Table of Contents

1. [Dashboard Overview](#dashboard-overview)
2. [Campaign Creation Process](#campaign-creation-process)
3. [Conversational Pathways (Workflow Builder)](#conversational-pathways-workflow-builder)
4. [Voice Selection and Customization](#voice-selection-and-customization)
5. [Script Creation Tools](#script-creation-tools)
6. [Testing and Quality Assurance](#testing-and-quality-assurance)
7. [Analytics and Reporting](#analytics-and-reporting)
8. [Account Management](#account-management)
9. [Tips for Effective Campaign Setup](#tips-for-effective-campaign-setup)

## Dashboard Overview

After logging into Bland AI at [app.bland.ai/dashboard](https://app.bland.ai/dashboard), you'll be presented with the main dashboard interface. This serves as your central hub for managing all aspects of your AI voice campaigns.

### Main Dashboard Sections

- **Navigation Sidebar**: Located on the left side of the screen, this menu provides access to all main features:
  - Dashboard (home)
  - Send Call
  - Conversational Pathways
  - Analytics
  - Custom Tools
  - Vector Stores
  - Phone Numbers
  - Settings

- **Overview Panel**: The central area displays key metrics and recent activity, including:
  - Recent calls
  - Call statistics
  - Account usage
  - Quick access to common actions

- **Account Information**: At the top right, you'll find your account details, notifications, and access to account settings.

### Key Metrics Displayed

The dashboard provides at-a-glance metrics including:

- Total call minutes used
- Number of completed calls
- Success rates
- Average call duration
- Billing information

### Navigation Tips

- Use the search function at the top of the sidebar to quickly find specific features
- Hover over icons for tooltip descriptions of each feature
- The notification bell will alert you to important system updates or campaign completions

## Campaign Creation Process

Creating a new campaign in Bland AI involves several steps, from initial setup to deployment. Here's a step-by-step walkthrough:

### Step 1: Initiate a New Campaign

1. From the dashboard, click on "Send Call" in the left navigation menu
2. You'll be presented with the call creation interface

### Step 2: Configure Basic Call Settings

1. **Phone Numbers**:
   - Enter the recipient's phone number in the "Phone Number" field
   - Select your outbound caller ID from the "Send From" dropdown

2. **Model Selection**:
   - Choose from available AI models:
     - **Base Model**: Best for following scripts and procedures, supports all features
     - **Enhanced Model**: Faster latency, more conversational, works best with objective-based prompts
     - **Turbo Model**: Fastest latency and most realistic conversation, but has limited capabilities

### Step 3: Create Your Script/Prompt

1. In the "Instructions" text area, write your script or select from templates
2. Include clear instructions for the AI agent, including:
   - Agent identity (name, role, company)
   - Conversation objective
   - Sample dialogues
   - Response guidelines

### Step 4: Advanced Settings (Optional)

Configure additional options as needed:

- **Voice Selection**: Choose from available voice profiles
- **Language**: Select the language for the call
- **Interruption Threshold**: Adjust how sensitive the agent is to interruptions
- **Custom Parameters**: Add any specific parameters for your campaign

### Step 5: Test Your Campaign

1. Click "Send Test Call" to test your configuration
2. Listen to the test call and review the transcript
3. Make adjustments to your script or settings as needed

### Step 6: Deploy Your Campaign

1. Once satisfied with your test results, click "Send Call" to launch your campaign
2. For batch campaigns, you can upload a CSV file with multiple contacts

## Conversational Pathways (Workflow Builder)

Conversational Pathways is Bland AI's visual workflow builder that allows you to create branching conversations with a node-based interface. This feature gives you greater control over your AI agent and the conversational flow.

### Accessing the Workflow Builder

1. From the dashboard, click on "Conversational Pathways" in the left navigation menu
2. Click "Create a Pathway" to start a new workflow or select an existing one to edit

### Understanding the Interface

- **Canvas**: The main workspace where you build your conversation flow
- **Toolbar**: Contains tools for adding nodes and managing your workflow
- **Properties Panel**: Displays settings for the currently selected node

### Key Components

#### Nodes

Nodes are the building blocks of your conversation flow. Each node represents an action point during the call or instructional information for your agent.

To create a node:

1. Click the "Add new Node" button at the top-left of the screen
2. Give your node a descriptive name
3. Add instructions for what the agent should say or do at this point

Nodes can contain:
- Dialogue instructions
- Questions to ask
- Information to collect
- Actions to perform

#### Pathways

Pathways connect nodes and define the possible conversation flows. They determine when the agent should move from one node to another based on the user's responses.

To create a pathway:

1. Click on the purple circle at the bottom of a node
2. Drag your mouse to connect to the top purple circle of another node
3. Click on the "New Pathway" button that appears on the connecting line
4. Enter a label that describes when this pathway should be taken (e.g., "user agrees", "user needs more information")

#### Conditions

Conditions ensure that certain criteria are met before the agent moves to the next node. If the condition is not met, the agent will stay on the current node and continue trying to fulfill the condition.

To add a condition to a node:

1. Select the node
2. In the properties panel, add your condition (e.g., "You must get the date, time, and number of guests for this reservation")

### Creating a Basic Branching Conversation

1. **Start with an Introduction Node**:
   - Create a node for your agent's introduction
   - Include a greeting and purpose statement

2. **Add a Question Node**:
   - Create a node that asks a key question
   - This will be the branching point in your conversation

3. **Create Response Nodes**:
   - Add nodes for different possible responses
   - Connect these to the Question Node with appropriate pathways

4. **Add Follow-up Nodes**:
   - For each response path, create appropriate follow-up nodes
   - Continue building out the conversation flow as needed

5. **Add Closing Nodes**:
   - Create nodes for successfully concluding the conversation
   - Include any necessary wrap-up information or next steps

### Advanced Workflow Features

#### Global Nodes

Global Nodes take precedence over regular pathway decisions. They're useful for handling situations that could occur at any point in the conversation.

To create a Global Node:

1. Create a new node
2. In the properties panel, check the "Global Node" option
3. Define when this node should be triggered

Example uses for Global Nodes:
- Handling requests to speak to a human
- Responding to abusive language
- Addressing common questions that might come up at any time

#### Webhooks

Webhooks allow you to execute external API calls at specific points in the conversation.

To add a webhook to a node:

1. Select the node
2. In the properties panel, click "Add Webhook"
3. Configure the webhook with the necessary URL and parameters

Webhooks can be used to:
- Update your CRM with customer information
- Check appointment availability
- Process payments
- Send confirmation emails or texts

#### Knowledge Base Integration

You can connect your agent to a knowledge base to help it answer specific questions.

1. In the properties panel of a node, click "Add Knowledge Base"
2. Upload relevant documents or enter information
3. The agent will use this information to answer questions related to the topic

## Voice Selection and Customization

Bland AI offers various voice options to personalize your AI agent's speech.

### Available Voice Options

- **Standard Voices**: Bland AI provides a library of pre-recorded human voices with different accents and languages
- **Custom Voices**: Enterprise clients can work with Bland's engineering team to create custom voices

### Selecting a Voice

1. During campaign creation, look for the "Voice" dropdown menu
2. Browse available voices and select the one that best fits your brand
3. You can preview voices by clicking the play button next to each option

### Voice Customization Parameters

Depending on your subscription level, you may have access to additional voice customization options:

- **Speaking Rate**: Adjust how quickly the agent speaks
- **Pitch**: Fine-tune the voice pitch for a more natural sound
- **Emphasis**: Control how the agent emphasizes certain words or phrases

### Voice Cloning (Enterprise Feature)

Enterprise clients can create custom voice profiles that match specific requirements:

1. Contact Bland AI's support team to inquire about voice cloning
2. Provide voice samples according to their specifications
3. Once created, your custom voice will appear in your voice selection options

## Script Creation Tools

Effective scripts are crucial for successful AI voice campaigns. Bland AI provides several tools to help you create engaging and effective scripts.

### Basic Script Structure

A well-structured script typically includes:

1. **Agent Identity**: Define who the AI agent is, their role, and their speaking style
2. **Conversation Objective**: Clearly state the purpose of the call
3. **Sample Dialogues**: Provide examples of how conversations should flow
4. **Response Guidelines**: Instructions on how to handle specific situations

### Script Templates

Bland AI offers pre-built templates for common use cases:

1. From the campaign creation screen, look for the "Templates" option
2. Browse available templates by category
3. Select a template that matches your use case
4. Customize the template to fit your specific needs

### Script Writing Tips

- **Use Conversational Language**: Write how people actually speak, not how they write
- **Keep It Simple**: Use straightforward vocabulary and avoid complex jargon
- **Include Variations**: Provide multiple ways for the agent to express similar ideas
- **Add Context**: Give the AI enough background information to handle unexpected responses

### Script Testing

1. Use the "Preview" function to see how your script will be interpreted
2. Send test calls to yourself to hear how the agent delivers your script
3. Review transcripts to identify areas for improvement

## Testing and Quality Assurance

Before deploying your AI voice campaigns at scale, it's important to thoroughly test them for quality and effectiveness.

### Test Call Process

1. From the campaign creation screen, click "Send Test Call"
2. Enter your phone number to receive the test call
3. Interact with the agent as a typical recipient would
4. After the call, review the transcript and recording

### Call Monitoring

During active campaigns, you can monitor calls in real-time:

1. Navigate to the "Analytics" section
2. Select the campaign you want to monitor
3. Click on active calls to listen in or view live transcripts

### Quality Assurance Checklist

Use this checklist to evaluate your AI voice campaigns:

- Does the agent introduce itself clearly?
- Does the conversation flow naturally?
- Can the agent handle common objections or questions?
- Does the agent stay on script while sounding natural?
- Is the voice quality clear and professional?
- Does the agent correctly capture and process information?

### Iterative Improvement

1. Identify areas for improvement based on test calls and monitoring
2. Make adjustments to your script, workflow, or voice settings
3. Test again to verify improvements
4. Continue this process until you're satisfied with the results

## Analytics and Reporting

Bland AI provides analytics tools to help you track the performance of your voice campaigns and make data-driven decisions.

### Accessing Analytics

1. Click on "Analytics" in the left navigation menu
2. You'll see an overview of all your campaigns and their performance

### Key Metrics

The analytics dashboard displays several important metrics:

- **Call Volume**: Total number of calls made or received
- **Call Duration**: Average length of calls
- **Completion Rate**: Percentage of calls that achieved their objective
- **Transfer Rate**: Percentage of calls transferred to human agents
- **Conversation Flow**: Visual representation of how conversations typically progress

### Call Recordings and Transcripts

1. From the Analytics dashboard, click on any call to access its details
2. You can listen to the recording and view the full transcript
3. The transcript highlights key moments and decision points

### Exporting Reports

1. Use the "Export" button to download reports in various formats (CSV, PDF)
2. Schedule regular reports to be sent to your email
3. Customize reports to include the metrics most relevant to your goals

### Performance Optimization

Use analytics to identify opportunities for improvement:

- Look for common drop-off points in conversations
- Identify frequently asked questions that the agent struggles with
- Compare performance across different scripts or voice options
- Track changes in performance over time

## Account Management

Managing your Bland AI account effectively ensures smooth operation of your voice campaigns.

### Account Settings

1. Click on your profile icon in the top-right corner
2. Select "Settings" from the dropdown menu
3. Here you can manage:
   - Billing information
   - API keys
   - Notification preferences
   - Account security

### User Management (Enterprise Feature)

Enterprise accounts can manage team access to the platform:

1. Navigate to the "Settings" section
2. Select "Team Members"
3. From here you can:
   - Invite new team members
   - Assign roles and permissions
   - Remove users
   - Track user activity

### Billing and Usage

1. In the "Settings" section, click on "Billing"
2. View your current plan, usage, and billing history
3. Update payment methods or change your subscription plan

### API Integration

For technical users, Bland AI offers API access:

1. In the "Settings" section, click on "API"
2. Generate API keys for secure access
3. Access documentation for integrating Bland AI with your systems

## Tips for Effective Campaign Setup

Based on best practices, here are some tips for creating effective AI voice campaigns using Bland AI's interface:

### Planning Your Campaign

1. **Define Clear Objectives**: Determine exactly what you want to achieve with your campaign
2. **Know Your Audience**: Consider who will be receiving the calls and what their needs are
3. **Map the Conversation**: Sketch out the conversation flow before building it in the platform
4. **Prepare for Variations**: Anticipate different responses and create pathways for each

### Optimizing Your Workflow

1. **Start Simple**: Begin with a basic conversation flow and add complexity gradually
2. **Use Conditions Effectively**: Ensure your agent collects all necessary information
3. **Implement Global Nodes**: Add handlers for common interruptions or questions
4. **Test Thoroughly**: Try different conversation paths to ensure everything works as expected

### Creating Natural Conversations

1. **Write Conversationally**: Use contractions, casual language, and varied sentence structures
2. **Include Small Talk**: Add brief pleasantries to make conversations feel more natural
3. **Vary Responses**: Provide multiple versions of similar responses to avoid repetition
4. **Add Pauses**: Use commas and periods strategically to create natural speech patterns

### Continuous Improvement

1. **Review Call Transcripts**: Regularly analyze calls to identify improvement opportunities
2. **A/B Test Scripts**: Try different approaches to see what works best
3. **Gather Feedback**: Ask recipients about their experience with your AI agent
4. **Update Regularly**: Refine your workflows based on performance data and feedback

## Conclusion

Bland AI's user interface provides a powerful yet accessible way to create, manage, and optimize AI voice campaigns. By understanding the dashboard, mastering the Conversational Pathways workflow builder, and utilizing the platform's voice and script creation tools, even non-technical users can create effective voice experiences.

Remember that creating great AI voice campaigns is an iterative process. Start with clear objectives, build thoughtful conversation flows, test thoroughly, and continuously refine based on performance data and feedback.

With practice and experimentation, you'll be able to create AI voice campaigns that engage your audience, achieve your business objectives, and provide a positive experience for your customers.