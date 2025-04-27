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
- Scripts • Guides • Strategies • Technical • Research • Implementation 
- bland-ai • voice-modulation • example-scripts • strategy • implementation • technical • research • case-study
- Example Scripts • Implementation Guides • Strategy Documents • Technical References • Research Findings • Case Studies


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

**Presentation**
  - Add some resource URLs into the presentations 
  - Add more links to nav 
  - Update mobile nav button coloring 

**Jekyll Theme**
  - Polish side bar 
  - Polish footer 
  - Go through chat and add missing CSS 

**Component Navigation** 
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








## Project Structure 

Users/seanivore/Development/voice-mkt-sfa/
├── _config.yaml
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
├── about-our-agents
│   ├── technical-specifications.md
│   ├── what-is-sfa-single-file-agent.md
│   └── workflow-feedback-job-resume-case-study.md
├── about-our-agents.md
├── ai-agentic-brand-content-case-study
│   ├── brand-identity-briefings.md
│   ├── content-plan
│   │   ├── agent-configuration-prompt-input.md
│   │   ├── glossier-content-plan.md
│   │   ├── hydro-flask-content-plan.md
│   │   ├── jungalow-content-plan.md
│   │   └── production-flow-content-plan.md
│   ├── content-plan.md
│   ├── email-blast
│   │   ├── ai-prompt-configuration-agent.md
│   │   ├── glossier-email-campaign.md
│   │   ├── hydro-flask-email-campaign.md
│   │   └── production-flow-email-blast.md
│   ├── email-blast.md
│   ├── instagram-post
│   │   ├── glossier-instagram-posts.md
│   │   ├── hydro-flask-instagram-posts.md
│   │   ├── instagram-post-agentic-configuration.md
│   │   └── production-flow-instagram-posts.md
│   └── instagram-post.md
├── ai-agentic-brand-content-case-study.md
├── ai-voice-marketing
│   ├── agentic-research-planning-case-study.md
│   ├── bland-ai-guides
│   │   ├── api-documentation.md
│   │   └── app-ui-guide.md
│   ├── bland-ai-guides.md
│   ├── deep-research
│   │   ├── analysis-optimizing-voice-ai-mkt.md
│   │   ├── analysis-voice-mkt-home-services.md
│   │   ├── bland-ai-pro-tips.md
│   │   ├── bland-ai-voice-modulation.md
│   │   ├── strategy-assertive-urgent.md
│   │   ├── strategy-combinations.md
│   │   ├── strategy-curiosity-gap.md
│   │   ├── strategy-empathy-objection.md
│   │   └── strategy-strongest-combos.md
│   ├── deep-research.md
│   ├── implement-bland-modulation-research.html
│   ├── index-section-site-map
│   │   ├── influence-lead-type.md
│   │   ├── outcome-result-strategy.md
│   │   ├── strategy-name.md
│   │   ├── tactic-types.md
│   │   └── vocal-characteristics.md
│   ├── index-section-site-map.md
│   ├── research-implementation
│   │   ├── persona-strategy
│   │   │   ├── annotated-vo-scripts.md
│   │   │   ├── identifying-archetypes.md
│   │   │   └── tailored-tactical-frameworks.md
│   │   ├── persona-strategy.md
│   │   ├── voice-marketing-matrix.md
│   │   ├── writing-guide
│   │   │   ├── emotion-driven-copywriting.md
│   │   │   ├── modulation-sound-patterns.md
│   │   │   ├── notation-cheat-sheet.md
│   │   │   └── script-voice-indicators.md
│   │   └── writing-guide.md
│   ├── research-implementation.md
│   ├── sales-development-ai-secrets.html
│   ├── top-conversion-strategy
│   │   ├── assertive-urgent-emotional.md
│   │   ├── combine-optimize-tactics.md
│   │   ├── creating-curiosity-gap.md
│   │   ├── empathy-objection-handling.md
│   │   └── target-audience-groups.md
│   └── top-conversion-strategy.md
├── ai-voice-marketing.md
├── assets
│   ├── audio
│   │   ├── 130-hz-trust-frequency-ai-voice-mkt
│   │   │   ├── 130-hz-trust-frequency-ai-voice-mkt.sesx
│   │   │   ├── Backup
│   │   │   │   ├── 130-hz-trust-frequency-ai-voice-mkt_20250423T102545.107706.sesx
│   │   │   │   └── 130-hz-trust-frequency-ai-voice-mkt_20250423T102750.175025.sesx
│   │   │   └── Conformed Files
│   │   │       ├── 130 Hz clean pure sine wave TEST TONE frequency 48000 1.pkf
│   │   │       └── 130 Hz clean pure sine wave TEST TONE frequency 48000 1.wav
│   │   └── 130-hz-trust-frequency-ai-voice-mkt.mp3
│   ├── css
│   │   ├── alt-slides.css
│   │   ├── main.css
│   │   ├── markdown.css
│   │   └── pixel-animation.css
│   ├── docs
│   │   ├── CUBE-LOGO-TEXT-2.ai
│   │   ├── CUBE-LOGO-TEXT-LOWERCCASE.ai
│   │   ├── DEV_PLAN.md
│   │   ├── geometric-logo-text-art.ai
│   │   ├── jekyll-theme-design-plan.md
│   │   ├── MARKIT-HTML-CSS-LESS-HTML.md
│   │   └── ribbons-block-letters.ai
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
│   │   ├── block-logo-1.svg
│   │   ├── block-logo-2.svg
│   │   ├── brand-logo-art-inspo.png
│   │   ├── brand-logo-cubed-2.svg
│   │   ├── brand-logo-cubed-3.svg
│   │   ├── brand-logo-cubed.svg
│   │   ├── brand-text-logo.svg
│   │   ├── character-styles.png
│   │   ├── raining-giant-pixels.png
│   │   ├── terminal-blurred-glass-ui-inspiration.png
│   │   ├── thumbnail-presentation-1.webp
│   │   └── vscode-blurred-glass-inspiration.png
│   └── js
│       ├── pixel-animation.js
│       └── slideshow.js
├── best-practrices
├── case-studies.md
├── CLAUDE.md
├── CNAME
├── components
│   ├── footer.html
│   └── nav-sidebar.html
├── prompt-engineering-single-file-agents
├── README.md
├── single-file-agent-architecture.md
└── technical-documentation.md

27 directories, 121 files

Hidden project directories:
./.cursor
./.vscode

Hidden project files:
./.example.env
./.gitignore
./.sample.aider.conf.yml

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