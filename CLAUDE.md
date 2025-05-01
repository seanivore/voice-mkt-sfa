# Homepage Layout 

I love the little icons on the tiles; so cute! 

Can we move the CSS in the index.html file to a new CSS file called home.css? It'll help make updating the homepage easier in the future. I love it though, just have some updates for the layout tiles. 

So the framing of the website, and homepage, is that it is a presentation of the case studies using SFA. The AI voice marketing is just one of the case studies. It just so happens that we also have two presentations for that case study. 

So we just need to update the band link, the title, description, etc. so that it makes sense for SFA presentations. 

Then we do want to highlight the presentations first. One per row, two rows. No image for the presentation homepage tile. And we'll put two 'quick resource' type links next to each. I'll break down the sections below. 

Feel free to make any wording changes you want. I just grabbed the title of each page and used it for the tile. 

----

# Header Navigation 

## Left Side 
[Agentic Workflow Case Studies](./index.html)

## Right Side 
[About Our Agents](./building-successful-agents.md)
[Workflow Assessment](./building-successful-agents/testimonial-job-case-study.md)

# Hero Section 

**TITLE:** Building Successful Agents

**DESCRIPTION:** Comprehensive overview of the variable-input single-file agent (SFA), from case studies to technical architecture, explaining how these AI agents work with variable-input design, workflow management, and tool integration capabilities.

# Deck Section 

Home Services AI Voice Marketing Decks

## First Row 
- Two half-height tiles on the left.
- On the right, a featured tile for the first presentation. 

### Left Column **Quick Resource Links**
[Bland AI Voice Marketing Cheat Sheet](./ai-voice-marketing-case-study/research-implementation/writing-guide/notation-cheat-sheet.md)
[Exploring the AI Voice Marketing Content](./ai-voice-marketing-case-study/index-section-site-map.md)

### Right Column **Presentation Tile**
[Secrets of Bland AI Voice Service Representatives](./ai-voice-marketing-case-study/sales-development-ai-secrets.html)

## Second Row 
- Two half-height tiles on the right this time, opposite of the row above. 
- On the left, a featured tile for the second presentation that is as high as the two stacked tiles beside it on the right. 

### Left Column **Presentation Tile**
[Making Bland AI Technical Strategies Practical](./ai-voice-marketing-case-study/implement-bland-modulation-research.html)

### Right Column **Quick Resource Links**
[Strategic Voice Marketing Personas with Scripts](./ai-voice-marketing-case-study/research-implementation/persona-strategy/annotated-vo-scripts.md)
[Emotion-Driven Marketing Copywriting Guide](./ai-voice-marketing-case-study/research-implementation/writing-guide/emotion-driven-copywriting.md)

# Case Study Section 

Case Studies on SFA Use-Cases 

## Third Row 
- Two standard tiles in one row 

[Agentic Research & Implementation Case Study](./ai-voice-marketing-case-study.md)
[Automating AI to Create A Comprehensive Marketing Plan](./marketing-content-case-study.md)

All About SFA 

## Fourth & Fifth Row 
- Two rows of three standard tiles in one row

[Agentic Workflow Assessment](./building-successful-agents/testimonial-job-case-study.md)
[SFA Design Philosophy](./building-successful-agents/best-practice-design-philosophy.md)
[The Art and Science of SFA Prompting](./building-successful-agents/prompt-writing-professional.md)
[Recent Agentic Workflow Feature Upgrades](./building-successful-agents/recent-agentic-workflow-feature-upgrades.md)
[What Makes SFA Architecture Unique](./building-successful-agents/sfa-python-architecture.md)
[Single-File Agent Technical Specifications](./building-successful-agents/technical-specifications.md)


----

## Production Phase Tracking 

### Ready For Production 

  - Breadcrumb tracking has been added to the Jekyll theme --> will this work okay with the way we have "section" pages? 
  - Front matter added to all markdown files 
  - Foundation for search, filtering, and tags built 
  - Pages ready for category quick-links 
  - Search layout Jekyll theme ready 
  - It is responsive 

### Questions 
  - I noticed that the markdown.css file has nav bar styling. Is there a nav bar? I didn't see one. Asking because it seems like the side bar is enough and that the nav bar is not needed. 
  - Similarly, it seems like the footer can just be the copy right. 

----

# Sidebar Updates 

  - Let's reorganize to the following below
  - Add in a "Also See" section right below the "Quick Resource Links" that just shows links to the rest of the pages in that same section  

**Quick Resource Links**
- Voice Engineering Cheat Sheet
- Emotion Driven Copywriting
- Persona Scripts for Top AI Marketing Strategies
- Key Voice Variables Matrix 

**See Also**

**Home Services AI Voice Marketing Decks**
- Secrets of Bland AI Voice Service Representatives 
- Making Bland AI Technical Strategies Practical  

**AI Voice Marketing Sections**
- Research Implementation
  - Voice Marketing Persona Strategy
  - Voice Marketing Writing Guides
- Bland AI Implementation Guides
- Top Conversion Strategies 
- Deep Research Analysis 
- Strategy Index & Section Map
  - Lead & Influence-Type
  - Outcome & Results
  - Name & Framework 
  - Types of Tactics
  - Voice Characteristics

**Case Study**
- Automating AI to Create A Comprehensive Marketing Plan
- Agentic Research and Planning for AI Voice Marketing 

**Building Successful Agents**
- Our AI Agentic System Is Called A Single-File Agent (SFA)
- Agentic Workflow Assessment
- Best Practice Design Philosophy 
- The Art and Science of SFA Prompting 
- Recent Agentic Workflow Feature Upgrades 
- What Makes SFA Architecture Unique 
- Single-File Agent Technical Specifications

### Phase: Presentation with Resources 

DELIVERABLE --> PUBLISH 

  - **Presentation**
    - Add some resource URLs into the presentations 
    - Add more links to nav 
    - Update mobile nav button coloring 

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

```plaintext
/Users/seanivore/Development/voice-mkt-sfa/
├── CLAUDE.md
├── README.md
├── _config.yaml
├── CNAME
├── _includes
│   ├── breadcrumbs.html
│   ├── footer.html
│   ├── sidebar-research.html
│   └── sidebar.html
├── _layouts
│   ├── default.html
│   ├── page.html
│   ├── research.html
│   └── search.html
├── ai-voice-marketing.md 
│   ├── bland-ai-guides.md
│   │   ├── api-documentation.md
│   │   └── app-ui-guide.md
│   ├── deep-research.md
│   │   ├── analysis-optimizing-voice-ai-mkt.md
│   │   ├── analysis-voice-mkt-home-services.md
│   │   ├── bland-ai-pro-tips.md
│   │   ├── bland-ai-voice-modulation.md
│   │   ├── strategy-assertive-urgent.md
│   │   ├── strategy-combinations.md
│   │   ├── strategy-curiosity-gap.md
│   │   ├── strategy-empathy-objection.md
│   │   └── strategy-strongest-combos.md
│   ├── index-section-site-map.md
│   │   ├── influence-lead-type.md
│   │   ├── outcome-result-strategy.md
│   │   ├── strategy-name.md
│   │   ├── tactic-types.md
│   │   └── vocal-characteristics.md
│   ├── research-implementation.md
│   │   ├── persona-strategy.md
│   │   │   ├── annotated-vo-scripts.md
│   │   │   ├── identifying-archetypes.md
│   │   │   └── tailored-tactical-frameworks.md
│   │   ├── writing-guide.md
│   │   │   ├── emotion-driven-copywriting.md
│   │   │   ├── modulation-sound-patterns.md
│   │   │   ├── notation-cheat-sheet.md
│   │   │   └── script-voice-indicators.md
│   │   └── vocal-engineering-strategy-matrix.md
│   ├── top-conversion-strategy.md
│   │   ├── assertive-urgent-emotional.md
│   │   ├── combine-optimize-tactics.md
│   │   ├── creating-curiosity-gap.md
│   │   ├── empathy-objection-handling.md
│   │   └── target-audience-groups.md
│   ├── strategy-research-case-study.md
│   ├── sales-development-ai-secrets.html  <-- HTML DESIGNED PAGE 
│   └── implement-bland-modulation-research.html<-- HTML DESIGNED PAGE 
├── building-successful-agents.md
│   ├── best-practice-design-philosophy.md
│   ├── prompt-writing-professional.md
│   ├── recent-agentic-workflow-feature-upgrades.md
│   ├── sfa-python-architecture.md
│   ├── technical-specifications.md
│   └── testimonial-job-case-study.md
├── marketing-content-case-study.md
│   ├── content-plan.md
│   │   ├── agent-configuration-prompt-input.md
│   │   ├── glossier-content-plan.md
│   │   ├── hydro-flask-content-plan.md
│   │   ├── jungalow-content-plan.md
│   │   └── production-flow-content-plan.md
│   ├── email-blast.md
│   │   ├── ai-prompt-configuration-agent.md
│   │   ├── glossier-email-campaign.md
│   │   ├── hydro-flask-email-campaign.md
│   │   └── production-flow-email-blast.md
│   ├── instagram-post.md
│   │   ├── glossier-instagram-posts.md
│   │   ├── hydro-flask-instagram-posts.md
│   │   ├── instagram-post-agentic-configuration.md
│   │   └── production-flow-instagram-posts.md
│   └── brand-identity-briefings.md
└── assets
    ├── audio
    ├── components
    │   ├── footer.html
    │   └── nav-sidebar.html
    ├── css
    │   ├── alt-slides.css
    │   ├── main.css
    │   ├── markdown.css
    │   └── pixel-animation.css
    ├── docs
    │   ├── brand-text-art.ai
    │   ├── DESIGN_BRIEF.md
    │   └── jekyll-theme-design.md
    ├── favicon
    ├── images
    └── js
        ├── pixel-animation.js
        └── slideshow.js
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