# Showcasing SFA Use-Cases 

This is a multi-layered development plan, being produced for multiple purposes, and shipping in phases. 

## Cliff Has An AI Voice Marketing Client In The Home Service Industry

  - The idea came from my conversation with Cliff 
  - I didn't tell him I was doing this. 
  - I've held off to make dropping this bomb more of a gut check. 
  - We'll see if he is divergent-friendly enough to be chill with that. 

## Finding Future Freelance Clients Myself 

  - I need to show off my creative work 
  - We've design with intention towards growth and longevity 
  - The information preparation is easy and fast thanks to markdown 
  - The presentation is priceless; easily duplicated, designed, and filled with new information 

### **FWIW MY CURRENT IDEA FOR MY DESPERATE JOB HUNT**

I really suck at the client getting and communication side of things. I'm really good at the project like really really good. 

So like, how do I find a partner to work with who had opposite skills? God if I could find someone who rocked at getting clients we could be a freaking powerhouse. BUT I have no idea where to start to find someone. Further, finding someone is in the same wheelhouse as finding clients. Catch-22. 

Regardless, I think our next task has to be getting better set up on freelance platforms. 

I also need to update my portfolio so that it is more about VISUALS. Plus now I have 5 local webflow sites to show off and one in the works. Plus my current portfolio is great to keep as more of a catalog of work. But for a new portfolio, visual only and SUPER SELECTIVE. That's after we get this project out. 

## Project Overview 

Showcase impressive work, in an impressive way, using a framework that can easily be repurposed and grown. 

### Current Development Focus 

  - Present the SFA via what it has made of value 
  - Frame the story around what is produced, not the agent tool 
  - Show my ability to use my resources, which is the SFA 
  - Highlight my ability to work quickly and create impressive design  

### Core Structure

  1. Home page with overall navigation 
  2. Presentation style deck section 
  3. Document pages are markdown converted to HTML
  4. Search and filtering system

## Technical Stack

### Frontend
   - Modern framework (React/Next.js)
   - Responsive design system
   - Animation library
   - State management
   - Search UI components

### Content Management

  - Jekyll for static site generation
  - Markdown processing with front matter
  - Dynamic routing
  - Search functionality:
    - Jekyll search plugin
    - Tag-based filtering
    - Category organization
  - Reference system

### Search Implementation

  1. Add Jekyll search plugin
  2. Implement front matter for all content
  3. Create search index
  4. Build search UI components
  5. Add filtering system
  6. Implement results display
  7. Add search analytics

## Categories, Tags, and Content Types 

**CATEGORIES** (2 per document):
1. Vocal Engineering
2. Copywriting
3. Planning
4. Coding
5. Designing

**TAGS** (1 per document):
1. conceptual
2. applied
3. specific
4. overview
5. platform

**CONTENT_TYPE** (1-2 per document):
1. Research
2. Case Study
3. Technical
4. Framework
5. Reference
6. Guide 

----

## Production Phase Tracking 

### Ready For Production 

  - Breadcrumb tracking has been added to the Jekyll theme 
  - Front matter added to all markdown files 
  - Foundation for search, filtering, and tags built 
  - Pages ready for category quick-links 
  - Search layout Jekyll theme ready 
  - It is responsive 

### Phase: Presentation with Resources 

DELIVERABLE --> PUBLISH 

  - **Presentation**
    - Add some resource URLs into the presentations 
    - Add more links to nav 
    - Update mobile nav button coloring 

  - **Jekyll Theme**
    - Polish side bar 
    - Polish footer 
    - Go through chat and add missing CSS 

  - **Component Navigation** 
    - JS is on page and JS directory 
    - Second presentation needs new components 

### Phase: Build Features Out 

  - **Add a CSS animation behind the transparent text brand logos**

  - **Category and tag filtering**
    - Create category quick-links 
    - Build filtering system 

  - **Setting up search**
    - Setup Jekyll Search Plugin
      - Add jekyll-search or similar to your _config.yml plugins
      - Create a JSON index of your content
    - Client-Side Search Implementation
      - Use a library like Lunr.js or Simple-Jekyll-Search
      - Link it to the search forms we've already created

### Phase: Homepage  
  - Build homepage just motion art
  - New modular tiles link to pages 
  - Make sure it is responsive 

### Phase: Build Features Out
  - Make homepage interactive 
  - Quick-copy UI on script examples 
  - Quick-jump to sections 
  - Open in Google Docs UI option 
  - Filtered viewing options 
  - Design Search UI
    - Search bar
    - Filter sidebar
    - Results display
    - Sort controls
    - Preview cards

----

## Project Structure & Web Map 

Each directory has a Markdown "Section Page" to be converted into HTML at the same url name as the directly would have been. 

```
Users/seanivore/Development/voice-mkt-sfa/
├── CLAUDE.md                                                       <- You are here
├── _config.yaml                                                    <- GitHub Pages Jekyll Configuration
├── _includes                                                       <- Markdown > HTML Components
│   ├── breadcrumbs.html
│   ├── footer.html
│   ├── sidebar-research.html
│   └── sidebar.html
├── _layouts                                                        <- Markdown > HTML Layouts
│   ├── default.html
│   ├── page.html
│   ├── research.html
│   └── search.html
├── CNAME                                                 <- Defining Custom Domain
├── ./.example.env                                        <- Anthropic, OpenAI, Gemini, Brave, and Perplexity API Keys
├── ./.gitignore                                          <- Store your API keys in an .env file BEFORE running `git init` 
├── ./.vscode
├── `case-studies --> case-studies.md`                    <- Case Studies Using Agents to Produce Impressive Work
│   ├── marketing-content-case-study.md                   <- Give agent a brand identity and they write amazing marketing plans 
│   ├── strategy-research-case-study.md                   <- AI voice marketing deep research and findings 
│   └── testimonial-job-case-study.md                     <- Write's resumes and cover letters targeted for job postings 
├── `ai-voice-marketing --> ai-voice-marketing.md`
│   ├── `bland-ai-guides --> bland-ai-guides.md`          <- Agents researched using BLAND AI for a client 
│   │   ├── api-documentation.md                          <- Need API docs? Just send out an agent to gather them 
│   │   └── app-ui-guide.md
│   ├── `deep-research --> deep-research.md`              <- Research after AI cleaned it up one time 
│   │   ├── analysis-optimizing-voice-ai-mkt.md
│   │   ├── analysis-voice-mkt-home-services.md
│   │   ├── bland-ai-pro-tips.md
│   │   ├── bland-ai-voice-modulation.md
│   │   ├── strategy-assertive-urgent.md
│   │   ├── strategy-combinations.md
│   │   ├── strategy-curiosity-gap.md
│   │   ├── strategy-empathy-objection.md
│   │   └── strategy-strongest-combos.md
│   ├── `index-section-site-map --> index-section-site-map.md`   <- AI also produced the details for an index section 
│   │   ├── influence-lead-type.md
│   │   ├── outcome-result-strategy.md
│   │   ├── strategy-name.md
│   │   ├── tactic-types.md
│   │   └── vocal-characteristics.md
│   ├── `research-implementation --> research-implementation.md`
│   │   ├── `persona-strategy --> persona-strategy.md`
│   │   │   ├── tailored-tactical-frameworks.md             <- Step 1 agents defined strategic frameworks 
│   │   │   ├── identifying-archetypes.md                   <- Step 2 agents came up with archetypes that fit the framework voice 
│   │   │   └── annotated-vo-scripts.md                     <- Step 3 agents used the archetypes to write scripts for each strategy 
│   │   ├── `writing-guide --> writing-guide.md`
│   │   │   ├── emotion-driven-copywriting.md                     <- The key to marketing conversions is emotional gut checks 
│   │   │   ├── modulation-sound-patterns.md
│   │   │   ├── notation-cheat-sheet.md                     <- One-sheet guide for creative production of AI voice
│   │   │   └── script-voice-indicators.md
│   │   └── vocal-engineering-strategy-matrix.md
│   ├── `top-conversion-strategy --> top-conversion-strategy.md`
│   │   ├── assertive-urgent-emotional.md
│   │   ├── combine-optimize-tactics.md
│   │   ├── creating-curiosity-gap.md
│   │   ├── empathy-objection-handling.md
│   │   └── target-audience-groups.md 
│   ├── **sales-development-ai-secrets.html**                          <- Presentation Deck
│   └── **implement-bland-modulation-research.html**                   <- Presentation Deck
├── assets
│   ├── audio
│   │   ├── 130-hz-trust-frequency-ai-voice-mkt.mp3
│   │   └── 130-hz-trust-frequency-ai-voice-mkt.sesx
│   ├── components                          <- Webflow/Framer vibes but self-coded because who wants to create a nav on every page
│   │   ├── footer.html
│   │   └── nav-sidebar.html
│   ├── css
│   │   ├── alt-slides.css                <- Presentation deck number 2 
│   │   ├── main.css                      <- Presentation deck number 1 
│   │   ├── markdown.css                  <- Jekyll converts markdown to HTML using our CSS 
│   │   └── pixel-animation.css           <- CSS animations are my new favorite thing 
│   ├── docs
│   │   ├── brand-text-art.ai
│   │   ├── DESIGN_BRIEF.md              <- When AI codes, most of the work is in designing the prompts, including design briefs 
│   │   └── jekyll-theme-design.md
│   ├── favicon
│   │   ├── apple-touch-icon.png
│   │   ├── favicon-96x96.png
│   │   ├── favicon.ico
│   │   ├── favicon.svg
│   │   ├── site.webmanifest
│   │   ├── web-app-manifest-192x192.png
│   │   └── web-app-manifest-512x512.png
│   ├── images
│   │   ├── avatar-black.png
│   │   ├── avatar-colored.png
│   │   ├── brand-text-art-1.svg
│   │   ├── brand-text-art-2.svg
│   │   ├── character-styles.png
│   │   ├── inspo-bland-ai-raining-giant-pixels.png
│   │   ├── inspo-bland-ai-web-design.png
│   │   └── thumbnail-presentation-1.webp
│   └── js
│       ├── pixel-animation.js
│       └── slideshow.js                      <- I requested it 'Slide with Gestures like using MacOS workspaces
├── `building-successful-agents --> building-successful-agents.md`
│   ├── agent-python-architecture.md
│   ├── best-practice-design-philosophy.md
│   ├── prompt-writing-professional.md
│   ├── technical-specifications.md
│   ├── use-case-workflow-setup-protocol.md
│   ├── use-case-workflow-standardization.md
│   ├── use-case-workflow-variable-configuration.md
│   └── what-is-an-sfa.md
├── `marketing-content-case-study --> marketing-content-case-study.md`
│   ├── `content-plan --> content-plan.md`
│   │   ├── agent-configuration-prompt-input.md
│   │   ├── glossier-content-plan.md
│   │   ├── hydro-flask-content-plan.md
│   │   ├── jungalow-content-plan.md
│   │   └── production-flow-content-plan.md
│   ├── `email-blast --> email-blast.md`
│   │   ├── ai-prompt-configuration-agent.md
│   │   ├── glossier-email-campaign.md
│   │   ├── hydro-flask-email-campaign.md
│   │   └── production-flow-email-blast.md
│   ├── `"instagram-post --> instagram-post.md"`
│   │   ├── glossier-instagram-posts.md
│   │   ├── hydro-flask-instagram-posts.md
│   │   ├── instagram-post-agentic-configuration.md
│   │   └── production-flow-instagram-posts.md
│   └── brand-identity-briefings.md
├── **implement-bland-modulation-research.html**                      <- Custom Designed Presentation Deck
└── **sales-development-ai-secrets.html**                             <- Custom Designed Presentation Deck  
```

## Custom SFA Tool Ideas 

### Media Processing Tools (right up your alley as a designer! 🎨):
- Image optimization and resizing tools
- Color palette extractors
- Design asset metadata managers
- SVG manipulation tools
- Font analyzers

### Development Tools (for the coding side 💻):
- Git operation helpers (commit, branch, merge)
- Code quality checkers
- Documentation generators
- Dependency analyzers
- Test generators

### Project Management Tools (for keeping things organized 📊):
- Task trackers and updaters (like your task_reporting tool!)
- Time tracking tools
- Resource usage monitors
- Progress visualizers
- Team communication helpers

### Data Processing Tools (for handling information 📈):
- CSV/JSON/XML parsers
- Data validators
- Format converters
- Data visualization generators
- Analytics reporters

### AI/ML Integration Tools (the fun experimental stuff! 🤖):
- Model performance monitors
- Prompt template managers
- Training data processors
- Output validators
- Chain-of-thought analyzers