# Comprehensive Voice Marketing Cheat Sheet for Bland AI

## VOICE MODULATION TECHNIQUES

### Basic Notation System

Use these clear, bracketed cues in your scripts to direct the AI's delivery:

| Modulation Cue | Script Notation | Effect |
| :-- | :-- | :-- |
| **Pauses** | `[pause 0.8s]` | Creates natural breaks, lets information sink in |
| **Inflection** | `[upward inflection]` or `[downward inflection]` | Controls tone at end of sentences |
| **Pitch** | `[lower pitch]` or `[higher pitch]` | Adjusts vocal pitch for authority or urgency |
| **Pace** | `[slower]` or `[faster]` | Controls speaking speed for clarity or energy |
| **Emotion** | `[cheerful]`, `[empathetic]`, `[urgent]` | Sets emotional tone |
| **Emphasis** | `[emphasize: word/phrase]` or `ALL CAPS` | Adds stress to key points |

### Strategic Applications of Voice Modulation

| Situation | Recommended Modulation | Example |
| :-- | :-- | :-- |
| **Introducing offers** | `[cheerful][faster]` | "Hi! This is [Company] [cheerful][faster]. I have great news about your account [pause 0.5s]." |
| **Presenting prices** | `[pause 0.5s][lower pitch]` | "That's just $29 a month [pause 0.8s, lower pitch]." |
| **Handling objections** | `[empathetic][lower pitch][slower]` | "I completely understand your concern [empathetic][lower pitch]. Let's work through this together [slower]." |
| **Creating urgency** | `[urgent][emphasize: ends soon]` | "This offer ends Friday [urgent][emphasize: ends soon][downward inflection]." |
| **Asking questions** | `[upward inflection][pause 0.3s]` | "Would you like to hear about our special offer? [upward inflection][pause 0.3s]" |
| **Confirming details** | `[downward inflection][slower]` | "Your service is scheduled for tomorrow [downward inflection][slower]." |

## BLAND AI PLATFORM STRATEGIES

### Pathway Generation & Script Design

- **Use Pathway Generation**: Create 80% of your conversational flow from a simple prompt, then refine for nuance
- **Script for Modulation**: Directly notate voice cues in your prompts using the notation system above
- **Combine Cues for Natural Speech**:
  - "You're all set! [cheerful][pause 0.5s] Your appointment is confirmed for Friday [downward inflection]."
  - "I understand that's frustrating [empathetic][slower]. Let's see what we can do [upward inflection]."

### Testing & Optimization

- **A/B Test Pathways**: Create multiple versions (e.g., empathetic vs. assertive) and compare results
- **Track Analytics**: Monitor conversion, hang-up, and engagement rates for each pathway
- **Iterate Regularly**: Review misunderstood queries and drop-off points to fine-tune scripts

### Technical Parameters

- **Response Timing** (API: 50–200):
  - 50: Fast, back-and-forth conversations
  - 100: Natural pace (default)
  - 200: Patient, allows for longer pauses
- **Model Selection**:
  - `base`: Best for custom scripting and modulation
  - `turbo`: Fastest, most natural, but fewer custom features
- **Randomness (Temperature)**:
  - 0 = Deterministic responses
  - 1 = More varied/creative responses

### Advanced Implementation

- **Emotional Context Integration**: Match voice modulation to customer situations
  - For emergencies: "Urgent, higher pitch, faster pace"
  - For price objections: "Lower pitch, slower, calm"
  - For good news: "Cheerful, upward inflection, lively pace"

- **Guardrails & Brand Consistency**:
  - Define "off-limits" topics and fallback responses
  - Set escalation triggers for human handoff

- **API & Workflow Integration**:
  - Connect to CRM/schedulers to trigger actions from call flow
  - Map the full customer journey across voice, SMS, and email

- **Continuous Learning**:
  - Use analytics to personalize future calls
  - Segment audience and tailor scripts for each segment

## SAMPLE SCRIPT SNIPPETS

### Opening with Energy
```
Hi [Name]! This is [Agent] from [Company] [cheerful][faster]. 
I'm calling about your recent inquiry [pause 0.5s].
Do you have a moment to chat? [upward inflection]
```

### Presenting Offers
```
I'd like to tell you about our EXCLUSIVE offer [emphasize: exclusive][higher pitch].
For just $29 a month [pause 0.8s][lower pitch], you'll receive unlimited access to our premium service.
This offer is GUARANTEED [upward inflection] to save you money.
```

### Handling Objections
```
I completely understand your concern [empathetic][lower pitch].
Many of our customers initially felt the same way [pause 0.5s].
However [slower], they found that our service actually saved them time and money in the long run [downward inflection].
```

### Creating Urgency & Closing
```
This special pricing ends this Friday [urgent][emphasize: ends this Friday].
Shall we go ahead and set up your account today? [upward inflection][pause 0.3s]
Great! [cheerful] Let me confirm your details [slower].
```

## QUICK REFERENCE SUMMARY

1. **Script for "how to say it"** not just "what to say"
2. **Use clear notation** for pauses, inflection, pitch, pace, and emotion
3. **Test different approaches** with A/B testing and analytics
4. **Match voice modulation** to the customer's situation and emotional state
5. **Combine modulation techniques** for natural, persuasive speech
6. **Iterate based on results** to continuously improve performance

---

**Remember**: The right voice modulation can dramatically improve engagement and conversion rates. Test, listen, and refine your approach based on real results.