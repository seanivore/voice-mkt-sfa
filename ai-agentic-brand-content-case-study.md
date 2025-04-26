# Using AI to Produce Content 

A breakdown of the process of using AI to produce content and what can be found in the case study spread across this section of the website. 

## Agentic Generation 

In the following section a tool we call 'Single-File Agents' (SFA) are used to produce content. The agents are not trained in any way and are not created for any specific one task. The Python code that makes up the 'agent' consists of a single script, and is very intentionally written to be as generic as possible, leaving openings that direct the AI to a series of alphabetic character's that represent variables. These variables are what make the 'generic' agent able to do highly specified tasks that require many steps, using various tools, and making decisions that branch their workflow, even creating next steps in the workflow live. 

### The Role of AI 

The script itself is built using the Anthropic Claude API. This is what allows the script to be so open-ended. In application, the AI essentially serves as software, and the natural english language provided by the 'variable input' is equivalent to playing the role of additional code for that software. 

### Claude AI Using Tools 

Over time the script for the agent goes through series of updates in which we add new tools. Currently we add tools that we need for other project. The tools are a combination of Anthropic produced solutions, and custom developed tooling specifically for the operation of our agent. To date, April 2025, todays agent has all tools needed to manage documents on your computer, research topics using traditional web searching and using communication with AI designed for providing web search results, and review provided or found images to provide or index imagery. They also have a tool specifically designed for thinking, in which the AI will stop what they are doing when they have gathered information so that they can review it, think through what they need to do step-by-step, and then can change their mind and make revisions to their process as they go. To compliment these tools they also have a tool specifically for making decisions and for changing their workflow allowing for flexibility meaning less planning required by the human. 

### Research and Analysis Case Study 

You can see a great example of one of these real-life use-cases in the other section of the website, 'AI Voice Marketing'. In that project agents conducted deep research on the topic of voice marketing, and then used the results of that research to produce a comprehensive guide to voice marketing that included data-backed to strategies for a specific industry, examples of script writing, and even got very specific into the details of using the exact tool that the client had purchased. 

## Content Production Case Study

The content found in this section was done as an example of what the SFA are capable of. The preparation process was simple. We chose to show how the agent can help with marketing by selecting brand identity information found online using a very quick web search. The workflows then had the agents review this information, along with a marketing copywriting guide, then producing a marketing plan and collection of content. 

### Illustrating the Process 

This example was set up very quickly. It was a last minute decision put together just 30 minutes before a phone call with a business owner. It started with a web search for brand information in which the very first search result happened to provide two paragraph brand identity information for a handful of well-known modern brands. 

## The Human Input 

### Context Information 

The **"[Brand Identity Briefings](./ai-agentic-brand-content-case-study/brand-identity-briefings.md)"** took less than five minutes to gather. The information found online was pasted directly into text documents and placed in a folder on the computer. Each brand identity overview you can see is very short but informative, the three used have an average of just 210 words. The AI choose the following brands from the list. 

1. Glossier
2. Hydro Flask
3. Jungalow

## The AI Input 

### Configuration Prompt

The plan for the workflow and what content to produce was placed into a configuration file for each of the workflows. This was shockingly easy. On the human side, all that was needed was explaining to the chat AI what we were generally trying to do, and then providing a copy of the example configuration file. The chat AI used the example configuration file, which is written in JSON code, and was able to produce the workflow files in seconds. 

In this case, in part because of the time crunch, the human did not even provide details. As a case study this made things particularly interesting because we were surprised by the results ourselves. The chat AI planned the following workflows. The setup command uses the configuration files and first creates a 'README' file for each workflow before setting everything else up. Those are included with each below. 

1. **[Content Plan](./ai-agentic-brand-content-case-study/content-plan.md)**

The content plan was the first workflow to be produced. It is a comprehensive plan that includes a 30-day content calendar, target audience segments, and a brand voice guide. Again, none of that was provided by the human. It was all produced by the chat AI. 

- [Content Planning Configuration File](./ai-agentic-brand-content-case-study/content-plan/agent-configuration-prompt-input.md)

2. **[Email Campaign](./ai-agentic-brand-content-case-study/email-blast.md)**

In the content plan the chat AI decided that the agent workflow would use the content plan to produce subsequent pieces of content. This was quite an elegant surprise. The first it detailed to have produced was the email campaign. 

- [Email Campaign Configuration File](./ai-agentic-brand-content-case-study/email-blast/ai-prompt-configuration-agent.md)

3. **[Instagram Post](./ai-agentic-brand-content-case-study/instagram-post.md)**

The final piece of content to be produced was an Instagram post. These were probably the most interesting results because we didn't know what to expect for the visual component. As with the content plan, the result was a plan describing exactly what visual imagery should be captured. 

- [Instagram Post Configuration File](./ai-agentic-brand-content-case-study/instagram-post/instagram-post-agentic-configuration.md)

## Agentic Workflow 

If you reviewed any of the above files you'll have noted that the AI agent was not just tasked with creating content and that is it, rather it was a whole process of agents working together to help each other improve the work. 

1. The first agent was tasked with gathering information about the brand. It used the brand identity document shared above, along with a marketing copywriting guide, and produced a first draft. This was the case for all workflows: The content plan, the email blast, and the social media post. 

2. The second agent was tasked with reviewing the first draft. It was provided the first draft, along with the same brand identity document, marketing copywriting guide, and content plan for the later two pieces of content. The AI then went and provided line-by-line feedback, checked for mistakes, and all around worked to help improve the content. 

3. The third agent was tasked with taking the feedback and making the necessary changes to the content. 

### First Draft and Review Feedback 

For ease of reviewing this phase, all the drafts and review feedback have been combined into one document for each workflow. 

**[Content Plan For All Brands](./ai-agentic-brand-content-case-study/content-plan/production-flow-content-plan.md)** 

**[Email Campaign For All Brands](./ai-agentic-brand-content-case-study/email-blast/production-flow-email-blast.md)**

**[Instagram Post For All Brands](./ai-agentic-brand-content-case-study/instagram-post/production-flow-instagram-posts.md)**

The result is a comprehensive set of content that is ready for the client. 

### AI Agent's Final Deliverables 

#### Glossier Marketing Campaign 

Inside you'll find an overview of the 'brand essence', the primary emotional gut checks, the target audience segments, the brand voice guidelines, and a 60-day content calendar. The target audience's emotional triggers were quite compelling and spot-on for the brand, including 'The Minimalist Essentialist', 'The Conscious Beauty Advocate', 'The Authentic Self-Expresser', 'The Community Connector', and 'The Beauty Novice'.

**[Content Plan for Glossier](./ai-agentic-brand-content-case-study/content-plan/glossier-content-plan.md)** 

This was followed by the brand voice guidelines. This was filled with thoughts like 'Like talking to a knowledgeable friend' and 'Every word serves a purpose'. They expressed the importance of 'Using first-person plural ("we") to reinforce community' and 'Employ second-person ("you") to create direct connection'. The tone attributes were also quite spot-on and aligned with the brand essence. The rest of the document included "do's and don't's" which were quite helpful. 

We have to say, we were shocked by the amount of detail in the whole document. The content calender was well thought out and connected all of the branding concepts expressed, through the full two months. They capped the content planning off with "themes for ongoing development" which was genuinely a great touch. After working for a decade in marketing, we can say that this level of detail is not often seen in content planning documents. The information, insights, and tips was endless and the amount of content created that follows was nothing compared to what could have been produced from the planner. 

If you've used AI you know that two of their most valuable skills is to help with ideation and making sure that plans are comprehensive, not skipping anything that should be included. This was clear when the content planning was followed by KPI measurement defined, coupled with emotional gut checks, and even a refinement process to keep on improving the content as data from analytics was collected. They ended the document with tips for the content creators and gave them a check list. 

Frankly, I'd have loved this kind of detail provided to me when producing the content myself, or when managing content producers and strategists. It was truly impressive. 

**[Email Campaign for Glossier](./ai-agentic-brand-content-case-study/email-blast/glossier-email-campaign.md)**

Honestly, I didn't expect much from the email blast example. I'm rarely impressed with brands when it comes to email marketing, and find that a lot of their success in KPIs is due to high turnover of both content and individuals on the list. Not to mention that most people don't spend the time unsubscribing, and some brands even illegally hide their unsubscribe button. But, much like the content plan, perhaps because of the content plan, the email blast was a success.

**[Instagram Post for Glossier](./ai-agentic-brand-content-case-study/instagram-post/glossier-instagram-posts.md)**

We expect what we'd get when working in-house with producers and human strategists. Typically that would be a couple sentences at most for the image, and a pretty basic caption. What we got included an introduction, detailed image description, acceptable captions, and hashtag strategy for each post. It went further than that, the campaign implementation notes had tips for optimal engagement, visual cohesion, and even themes for the posting schedule. 

Truly, from years of experience, even if this was just a starting point for a human working at Glossier: Any human would be extremely well set up to succeed with this content plan and email campaign. 

#### Hydro Flask Marketing Campaign 

This time they planned out TikTok and Youtube and even drafted countless posts in the actual content plan. The AI planned cross-channel integration into the strategy. Again, absolutely none of this was provided by the human. We won't completely detail everything here like we did for Glossier. Believe us, it is equally as worth clicking through and reviewing the intricate, well branded, thoughtful planning and descriptions for all parts of the entire marketing campaign. 

**[Content Plan for Hydro Flask](./ai-agentic-brand-content-case-study/content-plan/hydro-flask-content-plan.md)**

**[Email Campaign for Hydro Flask](./ai-agentic-brand-content-case-study/email-blast/hydro-flask-email-campaign.md)**

**[Instagram Post for Hydro Flask](./ai-agentic-brand-content-case-study/instagram-post/hydro-flask-instagram-posts.md)**

#### Jungalow Marketing Campaign 

It was not expected, but the Jungalow content plan was the most comprehensive of the three, and the visual details were incredible. This is incredibly valuable work and if my team had planned this, I would have been extremely impressed, and the pressure would have been on to make sure it was executed flawlessly. 

**[Content Plan for Jungalow](./ai-agentic-brand-content-case-study/content-plan/jungalow-content-plan.md)**

## Conclusion 

This was a fun project. It was a great example of how the AI can be used to produce content that is not only high quality, but also aligned with the brand voice and marketing goals. If ever anyone wasn't sure if both quality and quantity could be increased together, this does the trick. 

Again, the biggest takeaway I think was (1) the input information was barely 200 word per brand, (2) these all were more impressive than most humans have handed in after days of work, and this took minutes for the AI agents to create, and most significantly, (3) the idea that this would set up any human working in marketing for some serious success. You could spend a couple days making changes, even if you made a ton of changes everywhere, you'd still come out on top because it is a guide for everything you need and it jump starts the brainstorming. 

I'd love to hear your thoughts on this project. If you have any questions, please don't hesitate to reach out.

## Contact Me 

Sean August Horvath 

[Email](mailto:sean@august.style)

[LinkedIn](https://www.linkedin.com/in/seanivore/)