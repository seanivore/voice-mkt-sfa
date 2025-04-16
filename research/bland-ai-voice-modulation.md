<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# I would love as much of this kind of "cheat sheet" quick reference guide notes specifically for manipulating voice in Bland AI:

Pro Tip: Use brackets or all-caps for modulation cues, e.g.,
“Our service is GUARANTEED [upward inflection].”
“That’s just \$29 a month [pause 0.8s, lower pitch].”

Absolutely! Here’s a **Bland AI Voice Modulation Cheat Sheet**—a quick-reference guide for scripting and manipulating voice characteristics in your Bland AI pathways, based on platform documentation and best practices[^1][^2][^4][^6][^8]:

---

# Bland AI Voice Modulation Cheat Sheet

## 1. **Notation for Modulation in Scripts**

Use clear, bracketed cues or ALL CAPS to direct the AI’s delivery:

- **[pause Xs]** — Insert a pause of X seconds
    - “That’s just \$29 a month [pause 0.8s].”
- **[upward inflection]** — End with a rising tone (for questions, excitement)
    - “Our service is GUARANTEED [upward inflection].”
- **[downward inflection]** — End with a falling tone (for authority, finality)
    - “This offer ends Friday [downward inflection].”
- **[lower pitch] / [higher pitch]** — Adjust vocal pitch for authority or urgency
    - “We’re here to help [lower pitch].”
- **[slower] / [faster]** — Control pacing for clarity or urgency
    - “Let’s walk through your options [slower].”
- **[cheerful] / [empathetic] / [urgent]** — Set emotional tone
    - “Great news! [cheerful] You qualify for a discount.”
- **[emphasize: word/phrase]** — Add stress to key points
    - “This is a LIMITED TIME offer [emphasize: limited time].”

---

## 2. **Common Modulation Cues \& When to Use Them**

| Cue | Use Case Example | Effect |
| :-- | :-- | :-- |
| [pause 0.5s] | After price or key info | Lets info sink in |
| [upward inflection] | On questions, offers, or CTAs | Invites response, excitement |
| [downward inflection] | On closing, price, or guarantees | Authority, confidence |
| [lower pitch] | On objections, price discussions | Trust, calm |
| [higher pitch] | On emergencies, urgency | Energy, alertness |
| [slower] | On complex info, legal, or price | Clarity, seriousness |
| [faster] | On greetings, excitement, urgency | Energy, engagement |
| [cheerful] | On good news, welcomes | Warmth, positivity |
| [empathetic] | On complaints, objections | Builds rapport |
| [urgent] | On emergencies, deadlines | Drives action |
| [emphasize: word] | On discounts, deadlines, guarantees | Focuses attention |

---

## 3. **Technical Parameters \& API Tips**

- **Response Timing**:
    - Adjust “patience” (API: 50–200) for how long AI waits before responding[^2].
        - 50: Fast, back-and-forth
        - 100: Natural pace (default)
        - 200: Patient, allows for long pauses
- **Model Selection**:
    - `base`: Best for custom scripting and modulation
    - `turbo`: Fastest, most natural, but fewer custom features[^2]
- **Randomness (Temperature)**:
    - 0 = Deterministic, 1 = More varied/creative[^2]
- **Pathways**:
    - Use Pathway Generation to quickly build and test different modulation strategies[^4][^7]

---

## 4. **Pro Tips for Scripting in Bland AI**

- **Always notate modulation cues in your script**—Bland’s engine interprets these for more human-like delivery[^8].
- **Test and iterate**: Use Bland’s testing tool to hear how your cues sound and adjust for naturalness[^6].
- **A/B test**: Create multiple script versions (e.g., [cheerful] vs. [authoritative]) and compare conversion rates[^4].
- **Combine cues**:
    - “You’re all set! [cheerful][pause 0.5s] Your appointment is confirmed for Friday [downward inflection].”
- **Emotional context**:
    - “I understand that’s frustrating [empathetic][slower]. Let’s see what we can do [upward inflection].”

---

## 5. **Sample Script Snippets**

- “Hi! This is [Company] [cheerful][faster]. I have great news about your account [pause 0.5s].”
- “Your service is scheduled for tomorrow [downward inflection][slower].”
- “Would you like to hear about our special offer? [upward inflection][pause 0.3s] It ends soon [urgent][emphasize: ends soon].”
- “I completely understand your concern [empathetic][lower pitch]. Let’s work through this together [slower].”

---

## 6. **Quick Reference Table**

| Modulation Cue | Script Notation Example |
| :-- | :-- |
| Pause | [pause 0.5s] |
| Upward Inflection | [upward inflection] |
| Downward Inflection | [downward inflection] |
| Lower Pitch | [lower pitch] |
| Higher Pitch | [higher pitch] |
| Slower | [slower] |
| Faster | [faster] |
| Cheerful | [cheerful] |
| Empathetic | [empathetic] |
| Urgent | [urgent] |
| Emphasize | [emphasize: word/phrase] |

---

**Keep this cheat sheet handy when scripting in Bland AI.**
Test, listen, and iterate—modulation cues are your secret weapon for making AI sound truly human and persuasive![^1][^2][^4][^6][^8]

<div>⁂</div>

[^1]: https://www.bland.ai

[^2]: https://docs.bland.ai/api-v1/post/calls

[^3]: https://www.reddit.com/r/SideProject/comments/1av05zd/i_recreated_a_voice_ai_that_2xd_booked_calls_in/

[^4]: https://docs.bland.ai/tutorials/pathways

[^5]: https://www.bland.ai/blogs/bland-babel-ai-transcription-optimization

[^6]: https://www.bland.ai/blogs/the-bland-ai-voice-call-api

[^7]: https://www.youtube.com/watch?v=rWucJkdp3Go

[^8]: https://www.bland.ai/blogs/voice-technology-human-like-voices

[^9]: https://callin.io/bland-ai-whitelabel/

[^10]: https://www.voicedrop.ai/bland-ai-integration/

