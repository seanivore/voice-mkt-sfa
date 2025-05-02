---
title: "Bland AI API Documentation"
description: "Comprehensive technical documentation for the Bland AI API, including authentication, endpoints, parameters, and code examples for voice call automation."
categories: ["Vocal Engineering", "Coding"]
tags: ["applied", "platform"]
content_types: ["Technical"]
permalink: /ai-voice-marketing-case-study/bland-ai-guides/api-documentation/
---

# Bland AI API Documentation

## Overview

The Bland AI API enables developers to create and manage AI-powered phone calls with human-like voice agents. This documentation provides technical details for implementing Bland AI in your applications.

## Base URL

```
https://api.bland.ai/v1
```

## Authentication

All API requests require authentication using an API key.

```bash
authorization: YOUR_API_KEY
```

Include this header in all API requests. Failure to provide a valid API key will result in a 401 Unauthorized response.

### Example Request with Authentication

```bash
curl --request GET \
  --url https://api.bland.ai/v1/calls \
  --header 'authorization: YOUR_API_KEY'
```

## Rate Limits

The API has the following rate limits:
- 100 requests per minute per API key
- 5,000 requests per day per API key

Exceeding these limits will result in a 429 Too Many Requests response.

## Calls

Endpoints for creating and managing AI phone calls.

### Send Call

Initiates an AI phone call to a specified number.

```
POST /v1/calls
```

#### Request Parameters

| Name              | Type    | Required | Description                                      |
| ----------------- | ------- | -------- | ------------------------------------------------ |
| phone_number      | string  | Yes      | The phone number to call in E.164 format         |
| task              | string  | No       | The objective for the AI agent                   |
| pathway_id        | string  | No       | ID of a predefined conversation pathway          |
| voice             | string  | No       | Voice ID to use for the call                     |
| first_sentence    | string  | No       | First sentence the AI will say                   |
| wait_for_greeting | boolean | No       | Whether to wait for a greeting before speaking   |
| model             | string  | No       | AI model to use ("base", "enhanced", or "turbo") |
| language          | string  | No       | Language code (default: "en-US")                 |
| from              | string  | No       | Caller ID to display                             |
| record            | boolean | No       | Whether to record the call (default: true)       |

#### Example Request

```bash
curl --request POST \
  --url https://api.bland.ai/v1/calls \
  --header 'Content-Type: application/json' \
  --header 'authorization: YOUR_API_KEY' \
  --data '{
  "phone_number": "+15551234567",
  "task": "Schedule an appointment for a plumbing service",
  "voice": "matthew",
  "first_sentence": "Hello, this is Matthew from Acme Plumbing.",
  "wait_for_greeting": true,
  "model": "enhanced"
}'
```

#### Response

```json
{
  "status": "success",
  "message": "Call successfully queued.",
  "call_id": "9d404c1b-6a23-4426-953a-a52c392ff8f1",
  "batch_id": null
}
```

### List Calls

Retrieve a list of calls.

```
GET /v1/calls
```

#### Query Parameters

| Name   | Type    | Required | Description                                                            |
| ------ | ------- | -------- | ---------------------------------------------------------------------- |
| limit  | integer | No       | Maximum number of calls to return (default: 10, max: 100)              |
| offset | integer | No       | Number of calls to skip (default: 0)                                   |
| status | string  | No       | Filter by call status ("queued", "in-progress", "completed", "failed") |

#### Example Request

```bash
curl --request GET \
  --url 'https://api.bland.ai/v1/calls?limit=5&status=completed' \
  --header 'authorization: YOUR_API_KEY'
```

#### Response

```json
{
  "calls": [
    {
      "call_id": "9d404c1b-6a23-4426-953a-a52c392ff8f1",
      "status": "completed",
      "phone_number": "+15551234567",
      "duration": 120,
      "created_at": "2023-01-01T12:00:00Z",
      "updated_at": "2023-01-01T12:02:00Z"
    },
    // Additional calls...
  ],
  "total": 42,
  "limit": 5,
  "offset": 0
}
```

### Get Call Details

Retrieve details for a specific call.

```
GET /v1/calls/{call_id}
```

#### Path Parameters

| Name    | Type   | Required | Description                    |
| ------- | ------ | -------- | ------------------------------ |
| call_id | string | Yes      | Unique identifier for the call |

#### Example Request

```bash
curl --request GET \
  --url https://api.bland.ai/v1/calls/9d404c1b-6a23-4426-953a-a52c392ff8f1 \
  --header 'authorization: YOUR_API_KEY'
```

#### Response

```json
{
  "call_id": "9d404c1b-6a23-4426-953a-a52c392ff8f1",
  "status": "completed",
  "phone_number": "+15551234567",
  "task": "Schedule an appointment for a plumbing service",
  "voice": "matthew",
  "duration": 120,
  "transcript": [
    {
      "speaker": "ai",
      "text": "Hello, this is Matthew from Acme Plumbing.",
      "timestamp": "2023-01-01T12:00:05Z"
    },
    {
      "speaker": "human",
      "text": "Hi, I need someone to fix my leaking faucet.",
      "timestamp": "2023-01-01T12:00:10Z"
    },
    // Additional transcript entries...
  ],
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-01T12:02:00Z"
}
```

### Stop Active Call

Stop an in-progress call.

```
POST /v1/calls/{call_id}/stop
```

#### Path Parameters

| Name    | Type   | Required | Description                    |
| ------- | ------ | -------- | ------------------------------ |
| call_id | string | Yes      | Unique identifier for the call |

#### Example Request

```bash
curl --request POST \
  --url https://api.bland.ai/v1/calls/9d404c1b-6a23-4426-953a-a52c392ff8f1/stop \
  --header 'authorization: YOUR_API_KEY'
```

#### Response

```json
{
  "status": "success",
  "message": "Call stopped successfully."
}
```

### Get Audio Recording

Retrieve the audio recording for a completed call.

```
GET /v1/calls/{call_id}/recording
```

#### Path Parameters

| Name    | Type   | Required | Description                    |
| ------- | ------ | -------- | ------------------------------ |
| call_id | string | Yes      | Unique identifier for the call |

#### Example Request

```bash
curl --request GET \
  --url https://api.bland.ai/v1/calls/9d404c1b-6a23-4426-953a-a52c392ff8f1/recording \
  --header 'authorization: YOUR_API_KEY' \
  --output recording.mp3
```

#### Response

Binary audio file (MP3 format)

## Voices

Endpoints for managing voice profiles.

### List Voices

Retrieve a list of available voices.

```
GET /v1/voices
```

#### Example Request

```bash
curl --request GET \
  --url https://api.bland.ai/v1/voices \
  --header 'authorization: YOUR_API_KEY'
```

#### Response

```json
{
  "voices": [
    {
      "voice_id": "matthew",
      "name": "Matthew",
      "gender": "male",
      "language": "en-US",
      "type": "standard"
    },
    {
      "voice_id": "sophia",
      "name": "Sophia",
      "gender": "female",
      "language": "en-US",
      "type": "standard"
    },
    // Additional voices...
  ]
}
```

### Clone a Voice

Create a custom voice clone.

```
POST /v1/voices/clone
```

#### Request Parameters

| Name      | Type   | Required | Description                         |
| --------- | ------ | -------- | ----------------------------------- |
| name      | string | Yes      | Name for the cloned voice           |
| audio_url | string | Yes      | URL to audio file for voice cloning |
| language  | string | No       | Language code (default: "en-US")    |

#### Example Request

```bash
curl --request POST \
  --url https://api.bland.ai/v1/voices/clone \
  --header 'Content-Type: application/json' \
  --header 'authorization: YOUR_API_KEY' \
  --data '{
  "name": "Custom Voice",
  "audio_url": "https://example.com/sample.mp3",
  "language": "en-US"
}'
```

#### Response

```json
{
  "status": "success",
  "voice_id": "custom-123456",
  "name": "Custom Voice",
  "status": "processing"
}
```

### Get Voice Details

Retrieve details for a specific voice.

```
GET /v1/voices/{voice_id}
```

#### Path Parameters

| Name     | Type   | Required | Description                     |
| -------- | ------ | -------- | ------------------------------- |
| voice_id | string | Yes      | Unique identifier for the voice |

#### Example Request

```bash
curl --request GET \
  --url https://api.bland.ai/v1/voices/matthew \
  --header 'authorization: YOUR_API_KEY'
```

#### Response

```json
{
  "voice_id": "matthew",
  "name": "Matthew",
  "gender": "male",
  "language": "en-US",
  "type": "standard",
  "created_at": "2023-01-01T00:00:00Z"
}
```

### Delete a Voice

Delete a custom voice.

```
DELETE /v1/voices/{voice_id}
```

#### Path Parameters

| Name     | Type   | Required | Description                     |
| -------- | ------ | -------- | ------------------------------- |
| voice_id | string | Yes      | Unique identifier for the voice |

#### Example Request

```bash
curl --request DELETE \
  --url https://api.bland.ai/v1/voices/custom-123456 \
  --header 'authorization: YOUR_API_KEY'
```

#### Response

```json
{
  "status": "success",
  "message": "Voice deleted successfully."
}
```

## Phone Numbers

Endpoints for managing phone numbers.

### Purchase Phone Number

Purchase a new phone number.

```
POST /v1/numbers
```

#### Request Parameters

| Name         | Type   | Required | Description                  |
| ------------ | ------ | -------- | ---------------------------- |
| area_code    | string | No       | Desired area code            |
| country_code | string | No       | Country code (default: "US") |

#### Example Request

```bash
curl --request POST \
  --url https://api.bland.ai/v1/numbers \
  --header 'Content-Type: application/json' \
  --header 'authorization: YOUR_API_KEY' \
  --data '{
  "area_code": "415",
  "country_code": "US"
}'
```

#### Response

```json
{
  "status": "success",
  "number_id": "PN-1234567890",
  "phone_number": "+14155551234",
  "monthly_cost": 15.00
}
```

### List Numbers

Retrieve a list of purchased phone numbers.

```
GET /v1/numbers
```

#### Example Request

```bash
curl --request GET \
  --url https://api.bland.ai/v1/numbers \
  --header 'authorization: YOUR_API_KEY'
```

#### Response

```json
{
  "numbers": [
    {
      "number_id": "PN-1234567890",
      "phone_number": "+14155551234",
      "status": "active",
      "monthly_cost": 15.00,
      "created_at": "2023-01-01T00:00:00Z"
    },
    // Additional numbers...
  ]
}
```

### Update Inbound Number Details

Configure how inbound calls to a number are handled.

```
POST /v1/numbers/{number_id}
```

#### Path Parameters

| Name      | Type   | Required | Description                            |
| --------- | ------ | -------- | -------------------------------------- |
| number_id | string | Yes      | Unique identifier for the phone number |

#### Request Parameters

| Name        | Type   | Required | Description                                           |
| ----------- | ------ | -------- | ----------------------------------------------------- |
| task        | string | No       | The objective for the AI agent handling inbound calls |
| voice       | string | No       | Voice ID to use for inbound calls                     |
| webhook_url | string | No       | URL to receive call events                            |

#### Example Request

```bash
curl --request POST \
  --url https://api.bland.ai/v1/numbers/PN-1234567890 \
  --header 'Content-Type: application/json' \
  --header 'authorization: YOUR_API_KEY' \
  --data '{
  "task": "Answer customer questions about our business hours and services",
  "voice": "sophia",
  "webhook_url": "https://example.com/webhook"
}'
```

#### Response

```json
{
  "status": "success",
  "message": "Number updated successfully."
}
```

## Conversational Pathways

Endpoints for managing conversation flows.

### Create Pathway

Create a new conversation pathway.

```
POST /v1/pathways
```

#### Request Parameters

| Name        | Type   | Required | Description                 |
| ----------- | ------ | -------- | --------------------------- |
| name        | string | Yes      | Name for the pathway        |
| description | string | No       | Description of the pathway  |
| nodes       | array  | Yes      | Array of conversation nodes |

#### Example Request

```bash
curl --request POST \
  --url https://api.bland.ai/v1/pathways \
  --header 'Content-Type: application/json' \
  --header 'authorization: YOUR_API_KEY' \
  --data '{
  "name": "Appointment Scheduler",
  "description": "Pathway for scheduling appointments",
  "nodes": [
    {
      "id": "start",
      "type": "start",
      "next": "greeting"
    },
    {
      "id": "greeting",
      "type": "message",
      "content": "Hello, I'm calling to help you schedule an appointment. Is now a good time to talk?",
      "next": "check_availability"
    },
    // Additional nodes...
  ]
}'
```

#### Response

```json
{
  "status": "success",
  "pathway_id": "PW-1234567890",
  "name": "Appointment Scheduler"
}
```

### List Pathways

Retrieve a list of conversation pathways.

```
GET /v1/pathways
```

#### Example Request

```bash
curl --request GET \
  --url https://api.bland.ai/v1/pathways \
  --header 'authorization: YOUR_API_KEY'
```

#### Response

```json
{
  "pathways": [
    {
      "pathway_id": "PW-1234567890",
      "name": "Appointment Scheduler",
      "description": "Pathway for scheduling appointments",
      "created_at": "2023-01-01T00:00:00Z",
      "updated_at": "2023-01-01T00:00:00Z"
    },
    // Additional pathways...
  ]
}
```

### Get Pathway Details

Retrieve details for a specific pathway.

```
GET /v1/pathways/{pathway_id}
```

#### Path Parameters

| Name       | Type   | Required | Description                       |
| ---------- | ------ | -------- | --------------------------------- |
| pathway_id | string | Yes      | Unique identifier for the pathway |

#### Example Request

```bash
curl --request GET \
  --url https://api.bland.ai/v1/pathways/PW-1234567890 \
  --header 'authorization: YOUR_API_KEY'
```

#### Response

```json
{
  "pathway_id": "PW-1234567890",
  "name": "Appointment Scheduler",
  "description": "Pathway for scheduling appointments",
  "nodes": [
    {
      "id": "start",
      "type": "start",
      "next": "greeting"
    },
    {
      "id": "greeting",
      "type": "message",
      "content": "Hello, I'm calling to help you schedule an appointment. Is now a good time to talk?",
      "next": "check_availability"
    },
    // Additional nodes...
  ],
  "created_at": "2023-01-01T00:00:00Z",
  "updated_at": "2023-01-01T00:00:00Z"
}
```

## Custom Tools

Endpoints for creating and managing custom tools that can be used during calls.

### Create a Custom Tool

Create a new custom tool.

```
POST /v1/tools
```

#### Request Parameters

| Name         | Type   | Required | Description                               |
| ------------ | ------ | -------- | ----------------------------------------- |
| name         | string | Yes      | Name for the tool                         |
| description  | string | Yes      | Description of what the tool does         |
| speech       | string | No       | Text the AI will say while using the tool |
| url          | string | Yes      | URL endpoint for the tool                 |
| method       | string | Yes      | HTTP method ("GET", "POST", etc.)         |
| headers      | object | No       | HTTP headers to include                   |
| body         | object | No       | Request body template                     |
| input_schema | object | No       | JSON schema for tool inputs               |

#### Example Request

```bash
curl --request POST \
  --url https://api.bland.ai/v1/tools \
  --header 'Content-Type: application/json' \
  --header 'authorization: YOUR_API_KEY' \
  --data '{
  "name": "CheckAvailability",
  "description": "Check available appointment slots",
  "speech": "Let me check our available appointment slots for you.",
  "url": "https://example.com/api/availability",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json",
    "X-API-Key": "YOUR_API_KEY"
  },
  "body": {
    "date": "{{date}}",
    "service": "{{service}}"
  },
  "input_schema": {
    "type": "object",
    "properties": {
      "date": {
        "type": "string",
        "format": "date"
      },
      "service": {
        "type": "string"
      }
    },
    "required": ["date", "service"]
  }
}'
```

#### Response

```json
{
  "status": "success",
  "tool_id": "TL-1234567890"
}
```

### List Custom Tools

Retrieve a list of custom tools.

```
GET /v1/tools
```

#### Example Request

```bash
curl --request GET \
  --url https://api.bland.ai/v1/tools \
  --header 'authorization: YOUR_API_KEY'
```

#### Response

```json
{
  "tools": [
    {
      "tool_id": "TL-1234567890",
      "name": "CheckAvailability",
      "description": "Check available appointment slots",
      "created_at": "2023-01-01T00:00:00Z"
    },
    // Additional tools...
  ]
}
```

## Error Codes

The API uses standard HTTP status codes to indicate the success or failure of requests.

| Status Code | Description                                        |
| ----------- | -------------------------------------------------- |
| 200         | OK - The request was successful                    |
| 400         | Bad Request - Invalid parameters or request format |
| 401         | Unauthorized - Invalid or missing API key          |
| 403         | Forbidden - Insufficient permissions               |
| 404         | Not Found - Resource not found                     |
| 429         | Too Many Requests - Rate limit exceeded            |
| 500         | Internal Server Error - Server error               |

### Error Response Format

```json
{
  "status": "error",
  "code": "invalid_parameter",
  "message": "Invalid phone number format",
  "details": {
    "parameter": "phone_number",
    "value": "5551234567",
    "expected": "E.164 format (e.g., +15551234567)"
  }
}
```

## Webhooks

Bland AI can send webhook notifications for various events. Configure webhook URLs when creating or updating resources.

### Webhook Events

| Event                   | Description                      |
| ----------------------- | -------------------------------- |
| call.queued             | Call has been queued             |
| call.started            | Call has started                 |
| call.completed          | Call has completed               |
| call.failed             | Call has failed                  |
| call.transcript_updated | Call transcript has been updated |

### Webhook Payload Example

```json
{
  "event": "call.completed",
  "call_id": "9d404c1b-6a23-4426-953a-a52c392ff8f1",
  "timestamp": "2023-01-01T12:02:00Z",
  "data": {
    "phone_number": "+15551234567",
    "duration": 120,
    "status": "completed"
  }
}
```

## Limits and Quotas

- Maximum call duration: 30 minutes
- Maximum concurrent calls: Depends on your plan (default: 10)
- Maximum custom voices: Depends on your plan (default: 5)
- Maximum custom tools: Depends on your plan (default: 20)
- Maximum pathway nodes: 100 per pathway

## Conclusion

This documentation covers the core functionality of the Bland AI API. For additional support or questions, contact support@bland.ai.