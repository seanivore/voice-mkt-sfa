# Project Progress 

## Content Locations 

### Presentations & Homepage 

I moved the presentation decks into their own project directory to be able to publish them through GitHub Pages from a different repository. All of the assets and HTML for the homepages are still in this repository, but we are linking to and using the presentation deck's directory homepage. 

- Homepage: `https://presenting.august.style/`
- Presentation 1: `https://presenting.august.style/ai-voice-sales-development` 
- Presentation 2: `https://presenting.august.style/implement-ai-voice-marketing`

The homepage from this repository is still live. Nothing links to it but if a user ends up there, it does function properly. 

- Live but unused: `https://sfagent.august.style/`

### Resource & Case Studies 

Building off the above note, that leaves all the Markdown > HTML pages in this repository. Other than the presentation decks, the homepage tiles all link to live pages from this GitHub Pages Jekyll site publication. 

**Homepage Quick Links Section** 
- AI Voice Marketing Cheat Sheet: `https://sfagent.august.style/ai-voice-marketing-case-study/research-implementation/writing-guide/notation-cheat-sheet`
- Indexes & Section Map: `https://sfagent.august.style/ai-voice-marketing-case-study/index-section-site-map` 
- Voice Marketing Persona Scripts: `https://sfagent.august.style/ai-voice-marketing-case-study/research-implementation/persona-strategy/annotated-vo-scripts`
- Emotion-Driven Copywriting Guide: `https://sfagent.august.style/ai-voice-marketing-case-study/research-implementation/writing-guide/emotion-driven-copywriting` 

**Homepage Case Study Links Section** 
- Agentic Research & Implementation: `https://sfagent.august.style/ai-voice-marketing-case-study` 
- Automation Marketing Plan Creation: `https://sfagent.august.style/marketing-content-case-study` 

**Homepage All About SFA Links Section** 
- Workflow Assessment: `https://sfagent.august.style/building-successful-agents/testimonial-job-case-study` 
- Design Philosophy: `https://sfagent.august.style/building-successful-agents/best-practice-design-philosophy` 
- Art of SFA Prompt Writing: `https://sfagent.august.style/building-successful-agents/prompt-writing-professional` 
- Feature Upgrades: `https://sfagent.august.style/building-successful-agents/recent-agentic-workflow-feature-upgrades` 
- SFA Architecture: `https://sfagent.august.style/building-successful-agents/sfa-python-architecture` 
- Technical Specifications: `https://sfagent.august.style/building-successful-agents/technical-specifications` 

## Future Updates 

### Content UI 

- Quick-copy UI on script examples
- Open in Google Docs UI option 

### Search with Filtering 

- **Design Search UI**
  - Search bar
  - Filter sidebar
  - Results display
  - Sort controls
  - Preview cards

- **Setting up search**
  - Setup Jekyll Search Plugin
    - Add jekyll-search or similar to your _config.yml plugins
    - Create a JSON index of your content
  - Client-Side Search Implementation
    - Use a library like Lunr.js or Simple-Jekyll-Search
    - Link it to the search forms we've already created

- **Use Category and Tags as UI on Search**
  - Create category quick-links 
  - Build filtering system 

## Project Structure & Web Map 

Each directory has a Markdown "Section Page" to be converted into HTML at the same url name as the directly would have been. 

```plaintext
/Users/seanivore/Development/voice-mkt-sfa/
├── _config.yaml
├── _includes
│   ├── footer.html
│   └── sidebar.html
├── _layouts
│   ├── default.html
│   └── page.html
├── ai-voice-marketing-case-study --> ai-voice-marketing-case-study.md
│   ├── bland-ai-guides --> bland-ai-guides.md
│   │   ├── api-documentation.md
│   │   └── app-ui-guide.md
│   ├── deep-research --> deep-research.md
│   │   ├── analysis-optimizing-voice-ai-mkt.md
│   │   ├── analysis-voice-mkt-home-services.md
│   │   ├── bland-ai-pro-tips.md
│   │   ├── bland-ai-voice-modulation.md
│   │   ├── strategy-assertive-urgent.md
│   │   ├── strategy-combinations.md
│   │   ├── strategy-curiosity-gap.md
│   │   ├── strategy-empathy-objection.md
│   │   └── strategy-strongest-combos.md
│   ├── index-section-site-map --> index-section-site-map.md
│   │   ├── influence-lead-type.md
│   │   ├── outcome-result-strategy.md
│   │   ├── strategy-name.md
│   │   ├── tactic-types.md
│   │   └── vocal-characteristics.md
│   ├── research-implementation --> research-implementation.md
│   │   ├── persona-strategy --> persona-strategy.md
│   │   │   ├── annotated-vo-scripts.md
│   │   │   ├── identifying-archetypes.md
│   │   │   └── tailored-tactical-frameworks.md
│   │   ├── vocal-engineering-strategy-matrix.md
│   │   ├── writing-guide --> writing-guide.md
│   │   │   ├── emotion-driven-copywriting.md
│   │   │   ├── modulation-sound-patterns.md
│   │   │   ├── notation-cheat-sheet.md
│   │   │   └── script-voice-indicators.md
│   └── top-conversion-strategy --> top-conversion-strategy.md
│       ├── assertive-urgent-emotional.md
│       ├── combine-optimize-tactics.md
│       ├── creating-curiosity-gap.md
│       ├── empathy-objection-handling.md
│       └── target-audience-groups.md
├── assets
│   ├── css
│   │   ├── home.css
│   │   ├── markdown.css
│   │   ├── pixel-animation.css
│   │   └── wave-animation.css
│   ├── docs
│   │   └── brand-text-art.ai
│   ├── favicon
│   ├── images
│   └── js
│       ├── pixel-animation.js
│       └── wave-animation.js
├── building-successful-agents --> building-successful-agents.md
│   ├── best-practice-design-philosophy.md
│   ├── prompt-writing-professional.md
│   ├── recent-agentic-workflow-feature-upgrades.md
│   ├── sfa-python-architecture.md
│   ├── technical-specifications.md
│   └── testimonial-job-case-study.md
├── CLAUDE.md
├── CNAME
├── index.html
├── marketing-content-case-study --> marketing-content-case-study.md
│   ├── brand-identity-briefings.md
│   ├── content-plan --> content-plan.md
│   │   ├── agent-configuration-prompt-input.md
│   │   ├── glossier-content-plan.md
│   │   ├── hydro-flask-content-plan.md
│   │   ├── jungalow-content-plan.md
│   │   └── production-flow-content-plan.md
│   ├── email-blast --> email-blast.md
│   │   ├── ai-prompt-configuration-agent.md
│   │   ├── glossier-email-campaign.md
│   │   ├── hydro-flask-email-campaign.md
│   │   └── production-flow-email-blast.md
│   └── instagram-post --> instagram-post.md
│       ├── glossier-instagram-posts.md
│       ├── hydro-flask-instagram-posts.md
│       ├── instagram-post-agentic-configuration.md
│       └── production-flow-instagram-posts.md
└── README.md
```
