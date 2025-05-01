# Jekyll Theme Updates 

Let's go through what is set up and what we actually need because when I was working on these with Claude, they made a bunch of new pages and I scrapped a bunch of them this morning because I just want to get the most important stuff out there ASAP. 

## Some thoughts on the below. 

- Will the breadcrumb work okay with the way we have "section" pages? 
- The markdown.css file has nav bar styling. Is there a nav bar? I don't think we need a nav bar when all of these pages will display the side bar. 
- Same with the footer; let's just use the copyright info for that just like on the home page. 
- There was a research and a search page HTML but I deleted them for now for clarity.
- Can we make sure that the side bar is on all the pages? I'm not sure if we have a difference between default and page. 

### _layouts

_layouts/default.html 
_layouts/page.html 

### _includes

_includes/breadcrumbs.html 
_includes/footer.html 
_includes/sidebar.html 

### Other 

_config.yaml 
./assets/css/markdown.css 

### Sidebar Updates

**Quick Resource Links**
- Voice Engineering Cheat Sheet `./ai-voice-marketing-case-study/research-implementation/writing-guide/notation-cheat-sheet.md`
- Emotion Driven Copywriting `./ai-voice-marketing-case-study/research-implementation/writing-guide/emotion-driven-copywriting.md`
- Persona Scripts for Top AI Marketing Strategies `./ai-voice-marketing-case-study/research-implementation/persona-strategy/annotated-vo-scripts.md`
- Key Voice Variables Matrix `./ai-voice-marketing-case-study/research-implementation/vocal-engineering-strategy-matrix.md`

**See Also** 
{% if current_url contains '/bland-ai-guides/' %}
- API Documentation `./ai-voice-marketing-case-study/bland-ai-guides/api-documentation.md`
- App UI Guide `./ai-voice-marketing-case-study/bland-ai-guides/app-ui-guide.md`
{% endif %}

{% if current_url contains '/deep-research/' %}
- Analysis Optimizing Voice AI Marketing `./ai-voice-marketing-case-study/deep-research/analysis-optimizing-voice-ai-mkt.md`
- Analysis Voice Marketing Home Services `./ai-voice-marketing-case-study/deep-research/analysis-voice-mkt-home-services.md`
- Bland AI Pro Tips `./ai-voice-marketing-case-study/deep-research/bland-ai-pro-tips.md`
- Bland AI Voice Modulation `./ai-voice-marketing-case-study/deep-research/bland-ai-voice-modulation.md`
- Strategy Assertive Urgent `./ai-voice-marketing-case-study/deep-research/strategy-assertive-urgent.md`
- Strategy Combinations `./ai-voice-marketing-case-study/deep-research/strategy-combinations.md`
- Strategy Curiosity Gap `./ai-voice-marketing-case-study/deep-research/strategy-curiosity-gap.md`
- Strategy Empathy Objection `./ai-voice-marketing-case-study/deep-research/strategy-empathy-objection.md`
- Strategy Strongest Combos `./ai-voice-marketing-case-study/deep-research/strategy-strongest-combos.md`
{% endif %}

{% if current_url contains '/index-section-site-map/' %}
- Influence & Lead Type `./ai-voice-marketing-case-study/index-section-site-map/influence-lead-type.md`
- Outcome & Results `./ai-voice-marketing-case-study/index-section-site-map/outcome-result-strategy.md`
- Name & Framework `./ai-voice-marketing-case-study/index-section-site-map/strategy-name.md`
- Types of Tactics `./ai-voice-marketing-case-study/index-section-site-map/tactic-types.md`
- Voice Characteristics `./ai-voice-marketing-case-study/index-section-site-map/vocal-characteristics.md`
{% endif %}

{% if current_url contains '/research-implementation/' %}
- Voice Marketing Persona Strategy `./ai-voice-marketing-case-study/research-implementation/persona-strategy.md`
- Annotated VO Scripts `./ai-voice-marketing-case-study/research-implementation/persona-strategy/annotated-vo-scripts.md`
- Identifying Archetypes `./ai-voice-marketing-case-study/research-implementation/persona-strategy/identifying-archetypes.md`
- Tailored Tactical Frameworks `./ai-voice-marketing-case-study/research-implementation/persona-strategy/tailored-tactical-frameworks.md`
- Voice Marketing Writing Guides `./ai-voice-marketing-case-study/research-implementation/writing-guide.md`
- Emotion Driven Copywriting `./ai-voice-marketing-case-study/research-implementation/writing-guide/emotion-driven-copywriting.md`
- Modulation Sound Patterns `./ai-voice-marketing-case-study/research-implementation/writing-guide/modulation-sound-patterns.md`
- Notation Cheat Sheet `./ai-voice-marketing-case-study/research-implementation/writing-guide/notation-cheat-sheet.md`
- Script Voice Indicators `./ai-voice-marketing-case-study/research-implementation/writing-guide/script-voice-indicators.md`
{% endif %}

{% if current_url contains '/top-conversion-strategy/' %}
- Assertive Urgent Emotional `./ai-voice-marketing-case-study/top-conversion-strategy/assertive-urgent-emotional.md`
- Combine Optimize Tactics `./ai-voice-marketing-case-study/top-conversion-strategy/combine-optimize-tactics.md`
- Creating Curiosity Gap `./ai-voice-marketing-case-study/top-conversion-strategy/creating-curiosity-gap.md`
- Empathy Objection Handling `./ai-voice-marketing-case-study/top-conversion-strategy/empathy-objection-handling.md`
- Target Audience Groups `./ai-voice-marketing-case-study/top-conversion-strategy/target-audience-groups.md`
{% endif %}

{% if current_url contains '/building-successful-agents/' %}
- Design Philosophy `./building-successful-agents/best-practice-design-philosophy.md`
- Prompt Writing `./building-successful-agents/prompt-writing-professional.md`
- Feature Upgrades `./building-successful-agents/recent-agentic-workflow-feature-upgrades.md`
- SFA Architecture `./building-successful-agents/sfa-python-architecture.md`
- Technical Specifications `./building-successful-agents/technical-specifications.md`
{% endif %}

{% if current_url contains '/marketing-content-case-study/content-plan/' %}
- Agent Configuration Prompt Input `./marketing-content-case-study/content-plan/agent-configuration-prompt-input.md`
- Glossier Content Plan `./marketing-content-case-study/content-plan/glossier-content-plan.md`
- Hydro Flask Content Plan `./marketing-content-case-study/content-plan/hydro-flask-content-plan.md`
- Jungalow Content Plan `./marketing-content-case-study/content-plan/jungalow-content-plan.md`
- Production Flow Content Plan `./marketing-content-case-study/content-plan/production-flow-content-plan.md`
{% endif %}

{% if current_url contains '/marketing-content-case-study/email-blast/' %}
- AI Prompt Configuration Agent `./marketing-content-case-study/email-blast/ai-prompt-configuration-agent.md`
- Glossier Email Campaign `./marketing-content-case-study/email-blast/glossier-email-campaign.md`
- Hydro Flask Email Campaign `./marketing-content-case-study/email-blast/hydro-flask-email-campaign.md`
- Production Flow Email Blast `./marketing-content-case-study/email-blast/production-flow-email-blast.md`
{% endif %}

{% if current_url contains '/marketing-content-case-study/instagram-post/' %}
- Glossier Instagram Posts `./marketing-content-case-study/instagram-post/glossier-instagram-posts.md`
- Hydro Flask Instagram Posts `./marketing-content-case-study/instagram-post/hydro-flask-instagram-posts.md`
- Production Flow Instagram Posts `./marketing-content-case-study/instagram-post/production-flow-instagram-posts.md`
{% endif %}

{% if current_url contains '/marketing-content-case-study/' %}
- Content Plan `./marketing-content-case-study/content-plan.md`
- Email Blast `./marketing-content-case-study/email-blast.md`
- Instagram Post `./marketing-content-case-study/instagram-post.md`
- Brand Identity Briefings `./marketing-content-case-study/brand-identity-briefings.md`
{% endif %}

**Home Services AI Voice Marketing Decks**
- Secrets of AI Voice Service Representatives `./ai-voice-marketing-case-study/sales-development-ai-secrets.html`
- Making Technical Strategies Practical `./ai-voice-marketing-case-study/implement-bland-modulation-research.html`

**AI Voice Marketing Sections**
- Research Implementation `./ai-voice-marketing-case-study/research-implementation.md`
- Bland AI Implementation Guides `./ai-voice-marketing-case-study/bland-ai-guides.md`
- Top Conversion Strategies `./ai-voice-marketing-case-study/top-conversion-strategy.md`
- Deep Research Analysis `./ai-voice-marketing-case-study/deep-research.md`
- Strategy Index & Section Map `./ai-voice-marketing-case-study/index-section-site-map.md`

**Case Study**
- Agentic Marketing Department `./marketing-content-case-study.md`
- Researching AI Voice Marketing `./ai-voice-marketing-case-study.md`

**Building Successful Agents**
- About Our Agents `./building-successful-agents.md`
- Workflow Assessment `./building-successful-agents/testimonial-job-case-study.md`





----

## Production Phase Tracking 

### Ready For Production 
  - Front matter added to all markdown files 
  - Foundation for search, filtering, and tags built 
  - Pages ready for category quick-links 
  - Search layout Jekyll theme ready 
  - It is responsive 

### Questions 
  - Similarly, it seems like the footer can just be the copy right. 

----

# Sidebar Updates 

  - Let's reorganize to the following below
  - Add in a "Also See" section right below the "Quick Resource Links" that just shows links to the rest of the pages in that same section  



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