# Bland AI Technical Guide - Part 1: API Basics

## Table of Contents

1. [API Overview and Architecture](#api-overview-and-architecture)
2. [Authentication Methods](#authentication-methods)
3. [Core Endpoints](#core-endpoints)
4. [Request/Response Formats](#requestresponse-formats)

## API Overview and Architecture

### Introduction to Bland AI API

Bland AI provides a powerful, easy-to-integrate voice call API that enables developers to create and manage AI-powered phone conversations. The API is designed to be simple yet flexible, allowing for the creation of natural-sounding, low-latency voice interactions for various use cases including sales, customer service, appointment scheduling, and more.

The Bland AI API is a RESTful API accessible at `https://api.bland.ai/v1/` that follows standard HTTP conventions and uses JSON for data exchange.

### Core Architecture

Bland AI's voice technology is built on three core AI models working in tandem:

1. **Speech-to-text (transcription)**: Listens to incoming audio and converts it to text
2. **Language model**: Processes the transcribed text and determines appropriate responses
3. **Text-to-speech**: Converts the AI's response into natural-sounding audio

![Bland AI Architecture](https://i.imgur.com/placeholder.png)

### Key Features

- **Low latency**: Response times under two seconds (compared to industry standard of five seconds)
- **Dynamic conversations**: Fully contextual interactions rather than pre-recorded responses
- **Function calling**: Ability to call external functions during phone calls to perform actions like scheduling appointments or updating databases
- **Multi-language support**: Ability to handle conversations in multiple languages
- **Customizable voices**: Options to select from available voices or create custom ones
- **Conversational pathways**: Define structured conversation flows for different scenarios

### API Capabilities

The Bland AI API supports both outbound and inbound call scenarios:

#### Outbound Calls

For outbound calls, developers can:

- Initiate calls to specified phone numbers
- Define the AI agent's task and personality
- Set up conversation pathways
- Configure voice settings and parameters
- Handle call analysis and transcription

#### Inbound Calls

For inbound calls, developers can:

- Purchase and configure phone numbers
- Set up AI agents to answer incoming calls
- Define conversation handling logic
- Integrate with external systems via webhooks

## Authentication Methods

Bland AI uses API key-based authentication for securing API requests. This section covers how to obtain and use API keys with the Bland AI platform.

### API Key Authentication

All requests to the Bland AI API must include an API key in the `authorization` header. This key authenticates your application and determines your access permissions.

#### Obtaining an API Key

To obtain an API key:

1. Create an account on the [Bland AI Developer Portal](https://www.bland.ai/)
2. Navigate to your account settings or API section
3. Generate a new API key
4. Store this key securely - it will not be displayed again

#### Using the API Key

Include your API key in the `authorization` header of all API requests:

```http
authorization: your_api_key_here
```

#### API Key Security Best Practices

- Never expose your API key in client-side code
- Store API keys in environment variables or secure key management systems
- Rotate keys periodically for enhanced security
- Use different keys for development and production environments

### Custom Twilio Integration

For enterprise users, Bland AI supports integration with your own Twilio account through a feature called BYOT (Bring Your Own Twilio).

#### Setting Up Twilio Integration

1. Create an encrypted key by sending a POST request to `/v1/accounts` with your Twilio credentials:

```bash
curl --request POST \
  --url https://api.bland.ai/v1/accounts \
  --header 'Content-Type: application/json' \
  --header 'authorization: your_api_key_here' \
  --data '{
  "account_sid": "your_twilio_account_sid",
  "auth_token": "your_twilio_auth_token"
}'
```

2. Store the returned `encrypted_key` securely

3. Use this encrypted key in the `encrypted_key` header when making call-related API requests

## Core Endpoints

The Bland AI API is organized into several logical groups of endpoints. This section covers the main endpoint categories and their functions.

### Calls Endpoints

These endpoints handle the creation and management of phone calls.

#### Send a Call

```http
POST /v1/calls
```

Initiates an outbound AI phone call with specified parameters.

**Example Request:**

```bash
curl --request POST \
  --url https://api.bland.ai/v1/calls \
  --header 'Content-Type: application/json' \
  --header 'authorization: your_api_key_here' \
  --data '{
  "phone_number": "+12223334444",
  "task": "You are a friendly customer service representative calling to confirm an appointment for tomorrow at 2pm. Introduce yourself as Sarah from Acme Services.",
  "voice": "emma"
}'
```

**Example Response:**

```json
{
  "status": "success",
  "message": "Call successfully queued.",
  "call_id": "9d404c1b-6a23-4426-953a-a52c392ff8f1",
  "batch_id": null
}
```

#### Get Call Details

```http
GET /v1/calls/{call_id}
```

Retrieves detailed information about a specific call, including transcripts and metadata.

**Example Request:**

```bash
curl --request GET \
  --url https://api.bland.ai/v1/calls/9d404c1b-6a23-4426-953a-a52c392ff8f1 \
  --header 'authorization: your_api_key_here'
```

**Example Response:**

```json
{
  "call_id": "9d404c1b-6a23-4426-953a-a52c392ff8f1",
  "call_length": 2.5,
  "to": "+12223334444",
  "from": "+17163511654",
  "request_data": {
    "phone_number": "+12223334444",
    "task": "You are a friendly customer service representative..."
  },
  "completed": true,
  "created_at": "2023-10-15T14:30:45.123456+00:00",
  "inbound": false,
  "queue_status": "completed",
  "transcripts": [
    {
      "id": 123456,
      "created_at": "2023-10-15T14:31:02.123456+00:00",
      "text": "Hello?",
      "user": "user"
    },
    {
      "id": 123457,
      "created_at": "2023-10-15T14:31:05.123456+00:00",
      "text": "Hi there! This is Sarah from Acme Services. I'm calling to confirm your appointment for tomorrow at 2pm.",
      "user": "assistant"
    }
  ]
}
```

#### List Calls

```http
GET /v1/calls
```

Retrieves a list of calls with optional filtering parameters.

#### Stop Active Call

```http
POST /v1/calls/stop
```

Stops an active call in progress.

#### Analyze Call with AI

```http
POST /v1/calls/analyze
```

Performs AI analysis on a completed call to extract insights.

### Conversational Pathways Endpoints

These endpoints manage conversation flows that guide the AI through structured interactions.

#### Create Pathway

```http
POST /v1/pathways
```

Creates a new conversation pathway.

#### Get Pathway Information

```http
GET /v1/pathways/{pathway_id}
```

Retrieves details about a specific pathway.

#### List Pathways

```http
GET /v1/pathways
```

Retrieves a list of all pathways.

#### Update Pathway

```http
POST /v1/pathways/{pathway_id}
```

Updates an existing pathway.

#### Delete Pathway

```http
DELETE /v1/pathways/{pathway_id}
```

Deletes a pathway.

### Phone Numbers Endpoints

These endpoints handle the management of phone numbers for inbound and outbound calls.

#### Purchase Phone Number

```http
POST /v1/numbers
```

Purchases a new phone number for use with Bland AI.

#### List Numbers

```http
GET /v1/numbers
```

Retrieves a list of phone numbers associated with your account.

#### Update Inbound Number Details

```http
POST /v1/numbers/{number_id}
```

Updates configuration for an inbound phone number.

### Voices Endpoints

These endpoints manage voice profiles used by the AI agents.

#### List Voices

```http
GET /v1/voices
```

Retrieves a list of available voices.

#### Clone a Voice

```http
POST /v1/voices/clone
```

Creates a custom voice clone (enterprise feature).

#### Generate Audio Sample

```http
POST /v1/voices/sample
```

Generates an audio sample using a specified voice.

### Custom Tools Endpoints

These endpoints manage custom tools that can be used by the AI during calls.

#### Create a Custom Tool

```http
POST /v1/tools
```

Creates a custom tool that can take AI input and call external APIs.

**Example Request:**

```bash
curl --request POST \
  --url https://api.bland.ai/v1/tools \
  --header 'Content-Type: application/json' \
  --header 'authorization: your_api_key_here' \
  --data '{
  "name": "CheckInventory",
  "description": "Check if a product is in stock",
  "speech": "Let me check our inventory system for you.",
  "url": "https://api.yourcompany.com/inventory",
  "method": "GET",
  "query": {
    "product_id": "{{input.product_id}}"
  },
  "input_schema": {
    "type": "object",
    "properties": {
      "product_id": {
        "type": "string"
      }
    }
  }
}'
```

#### List Custom Tools

```http
GET /v1/tools
```

Retrieves a list of custom tools.

## Request/Response Formats

This section covers the standard formats for requests and responses when interacting with the Bland AI API.

### General Request Format

All API requests to Bland AI follow these general guidelines:

1. **Base URL**: All requests are made to `https://api.bland.ai/v1/`

2. **Headers**:
   - `Content-Type: application/json` for requests with a body
   - `authorization: your_api_key_here` for authentication

3. **HTTP Methods**:
   - `GET`: For retrieving data
   - `POST`: For creating new resources or performing actions
   - `PATCH`: For updating resources
   - `DELETE`: For removing resources

4. **Request Body**: When required, request bodies are sent as JSON objects

### General Response Format

Responses from the Bland AI API typically include:

1. **Status Codes**:
   - `200 OK`: Successful request
   - `201 Created`: Resource successfully created
   - `400 Bad Request`: Invalid request parameters
   - `401 Unauthorized`: Authentication failure
   - `404 Not Found`: Resource not found
   - `500 Internal Server Error`: Server-side error

2. **Response Body**: JSON-formatted with these common fields:
   - `status`: Typically "success" or "error"
   - `message`: Human-readable description of the result
   - Additional fields specific to the endpoint

### Common Data Structures

#### Call Object

Represents a phone call in the system:

```json
{
  "call_id": "9d404c1b-6a23-4426-953a-a52c392ff8f1",
  "call_length": 2.5,
  "to": "+12223334444",
  "from": "+17163511654",
  "request_data": { /* original request parameters */ },
  "completed": true,
  "created_at": "2023-10-15T14:30:45.123456+00:00",
  "inbound": false,
  "queue_status": "completed",
  "transcripts": [ /* array of transcript objects */ ],
  "recording_url": "https://storage.bland.ai/recordings/call_9d404c1b.mp3"
}
```

#### Transcript Object

Represents a single utterance in a conversation:

```json
{
  "id": 123456,
  "created_at": "2023-10-15T14:31:02.123456+00:00",
  "text": "Hello?",
  "user": "user"
}
```

#### Voice Object

Represents a voice profile:

```json
{
  "voice_id": "v-abc123",
  "name": "Emma",
  "gender": "female",
  "preview_url": "https://storage.bland.ai/voices/emma_sample.mp3",
  "custom": false
}
```

### Error Handling

When an error occurs, the API returns an error response with details:

```json
{
  "status": "error",
  "message": "Invalid phone number format",
  "error_code": "INVALID_PARAMETER",
  "details": {
    "parameter": "phone_number",
    "reason": "Phone number must be in E.164 format"
  }
}
```

### Pagination

For endpoints that return lists of objects, pagination is supported through these parameters:

**Request Parameters**:
- `limit`: Maximum number of items to return (default: 20, max: 100)
- `offset`: Number of items to skip (default: 0)

**Response Format**:
```json
{
  "status": "success",
  "data": [ /* array of objects */ ],
  "pagination": {
    "total": 157,
    "limit": 20,
    "offset": 0,
    "has_more": true
  }
}
```

## Conclusion

This guide has provided an overview of the Bland AI API basics, including its architecture, authentication methods, core endpoints, and request/response formats. With this foundation, developers can begin integrating Bland AI's voice capabilities into their applications.

In Part 2 of this technical guide, we will explore advanced features, including conversational pathways, custom tools, and best practices for creating effective voice interactions.

---

© 2024 Bland AI Technical Documentation - Part 1