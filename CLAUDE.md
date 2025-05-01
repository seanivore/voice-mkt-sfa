# Showcasing SFA Use-Cases 

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

#### Categories, Tags, and Content Types 

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
- Vocal Engineering Cheat Sheet
- Emotion Driven Copywriting
- Persona Scripts for Top AI Marketing Strategies
- Key Voice Variables Matrix 

**See Also**

**Home Services Telemarketing Presentations**
- Secrets of AI Voice Service Representatives & Bland AI
- Making Technical Strategies Practical for Bland AI 

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