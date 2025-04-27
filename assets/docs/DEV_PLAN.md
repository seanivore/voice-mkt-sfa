# Development Plan: Voice Marketing Research Presentation

Content that is impressive in its own right, not any more or less impressive because of SFA. Reflecting my creative ability more than anything; the resources I use are only secondary in how they help me create at such a large scale. Must make sure the design is strong because his initial ask was if I could take on design work. 

## Project Overview
*File is being cleaned up and condensed as we go.*

We are at [PHASE 2: Build Slideshow](#phase-2-build-slideshow)

[Presentation Deck Design](#main-slides-section-design)
[Review Feedback](#feedback-and-updates)
[Home Page Design](#home-page-design)
[Project Directory Structure](#project-directory-structure)

----

## Core Structure
1. Home page with overall navigation 
2. Presentation style deck section 
3. Document pages are markdown converted to HTML
4. Search and filtering system

## Development 

Continue working on the slide show until it is finished. It is the most important information to convey and time is of the essence. 

~~### Phase 1: Planning & Preparing~~
~~- Design Concept Planning for slideshow~~
~~- Design Concept Planning for homepage~~
~~- Compile scrolling logic and implementation~~
~~- Typography and color scheme~~
~~- Write slide copy~~
~~- Sean finish brand logo text SVG~~
~~- Review finalized planning~~

~~### Phase 2: Build Slideshow~~
~~- Build slideshow section~~
~~- Make sure it is responsive~~
~~- Finish a second slide copy review to finalize~~
~~- Review slide design~~
~~- Implement slide design~~
~~- Implement feedback~~
~~- Add final copy for presentation 1~~
~~- Allow for feedback review~~
~~- Finished updates to 'sales-development-ai-secrets.html'~~
~~- Duplicated file to make 'implement-bland-modulation-research.html'~~
~~- Address feedback about MP3 player instead of video player~~
~~- Add final copy for presentation 2~~
~~- Presentation 2 review~~
~~- Clean up markdown documents~~
~~- update slugs~~
~~- Put to gether index~~
~~- Create groupings for index~~
- Markdown > HTML Jekyll Template
~~- Prepare for GitHub Pages deployment~~
- Add URLs for these resources where needed
  - Referenced on slides
  - Referenced in Navigation 
- Launch now so that the two slide shows can be presented if they need to be 

---- 

# Feedback and Updates 

## Front Matter 

There is a full project directory tree in the [CLAUDE.md](../../CLAUDE.md) file with all, exactly, 60 pages currently in the project. 

## Components 

It looks like the same JS used on the actual page, and again in the ./components/ directory. 

## Sean to Finish Buttons of Mobile Navigation 

----

### Phase 3: Build Homepage  
- Give the presentation's a CSS animation behind the transparent text brand logos  
- Build homepage just motion art
- New modular tiles link to pages (reference Portfolio's modular tiles and update after)
- Breadcrumb tracking                          `<-- this should be another component`
- Make sure it is responsive 
- Add search functionality:
  - Jekyll-based search implementation
  - Tag-based filtering system
  - Category quick-links
- Prepare for updated website GitHub Pages deployment 
- Launch entire site this time  

### Phase 4: Content Organization & Search
- Implement Jekyll front matter for all markdown files:
  ```yaml
  ---
  title: "Document Title"
  categories: ["scripts", "guides", "strategies"]
  tags: ["bland-ai", "voice-modulation", "example-scripts"]
  content_types: ["implementation", "research", "technical"]
  ---
  ```
- Add quick-filters on search page:
  - Content Type
  - Category
  - Tags
- Implement search features:
  - Full-text search
  - Category/tag filtering
  - Sort by relevance
  - Search result previews

### Phase 5: Enhanced Features
- Make homepage interactive 
- Quick-copy UI on script examples 
- Quick-jump to sections 
- Open in Google Docs UI option 
- Filtered viewing options 
- Advanced search features:
  - Save searches
  - Search history
  - Related content suggestions
  - Popular searches

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

## Content Organization

### Categories
- Scripts
- Guides
- Strategies
- Technical
- Research
- Implementation

### Content Types
- Example Scripts
- Implementation Guides
- Strategy Documents
- Technical References
- Research Findings
- Case Studies

### Tags
- bland-ai
- voice-modulation
- example-scripts
- strategy
- implementation
- technical
- research
- case-study

## Search Features

### Basic Search
- Full-text search
- Category filters
- Tag filters
- Sort options
- Result previews

### Advanced Features
- Save searches
- Search history
- Related content
- Popular searches
- Quick filters

## Implementation Guidelines

### Front Matter
- Required fields
- Optional fields
- Category rules
- Tag conventions

### Search UI
- Search bar
- Filter sidebar
- Results display
- Sort controls
- Preview cards

### Content Display
- Category pages
- Tag pages
- Search results
- Related content

----

# Main Slides Section Design 

## Background and Scrolling UX 

Horizontally scrolling page with panels serving as slides for a presentation deck. Ideally will have a Mac OS workspace UX vibe when swiping. Alternatives and indicators have been added. 

## Interactive Elements 

### The Static Art 

Inspiration for [brand art](../images/brand-logo-art-inspo.png) background. Just pretend the phone isn't in the middle. Silhouette of mountains in the distance of the desert vibe. Actually is a [SVG](../images/brand-logo-cubed.svg) of brand logo text. On top we'll place very similar colored-wavy shapes. 

### Motion Logic 

The brand logo text will be almost exactly 100 vw wide and sticky so that it stays with the screen as it scrolls, with content of the file moving off to the side while new content moves in from the other side. The colored-wavy shapes will move similar to the content on the panels and will be static, made to fit across all of the panels; if there are 8 panels, it will be 800 vw wide exactly, with a bleed, e.g. the image goes right up as if off the screen. 

This should create a resource light but engaging UX that makes the left and right scrolling of the page feel intuitive instead of unusual. 

### Developing the Real Thing 

I'd like to hold off making the wavy shapes until we have the scrolling effect and content in place, including the sticky brand logo text art. This will ensure I only make it once, for the perfect fit. 

----

# Home Page Design 

For the background of the deck slides section I proposed a two layer piece of art that create an interesting UX with one static and the length of all the slides, and the other moving with the screen as it scrolls. 

I'd like to explore a more visual motion art background for the home page, also our landing page. I have a similar piece of inspiration art for it, that uses one of the same pieces of art, but then are vibrant squares that look like extra big pixels that showering down from the art element. [Inspiration Art](../images/raining-giant-pixels.png) 

My logic is that, this is a presentation-centric site, that initially was only planned as it seemed the simplest way to showcase the agent work I could do for my friend Cliff's project for a client. I want to keep that mentality by not over-complicating the home page. This is one of those very rare occasions where it doesn't need to be marketing focused, so let's revel in that. 

Note that there are two main labor-intensive sections of this site. All the secondary pages will just be cleaned-up, simplified markdown files that jekyll can convert to HTML. That leaves design for the slides, proposed below; which I don't think will be complicated. The background is a simple 'fixed' versus sticky background dual layer art. Otherwise it is static — just the motion of scrolling creates the interactive feel. It also  proposes a very effect UX feel for side scrolling inspired by Mac OS, but I found implementation directions so easily I don't think that will be difficult either. Then the rest is just adding the text we composed. 

The home page is the only other section that requires some design work, other than a simple frame CSS/HTML theme edit for the Jekyll conversion. I've yet to really figure out the rest of the home page design and layout other than those raining pixels. Adn I'm thinking we'll make them motion but not interactive at first then double back if we have time to give some cursor interaction fun. I started planning the 'sections' or tiles or however we present the links to the secondary pages and the deck, but am not sure how to mix it up with the fun raining art idea yet. 

## Home Page Tile & Content Layout 

*I'm picturing the first three being laid out in two columns, the larger two-row-tall tile for presentation on the right. On the left two narrow rows for quick reference docs and easy access to script examples.*

**Deck Presentation**
Tile section that just links to the first slide. 

**AI Voice Marketing Cheat Sheets**
Script Writing Cheat Sheet 
Simple over view of the main strategies 
Emotion-based writing guide 

**Actionable Telephony Documents**
Persona Overview With Scripts 
Solution-Oriented Strategy Scripts 

*Then this next one could be three tiles in one row, reminiscent of pricing pages.*

**AI Voice MKT Case Study Documents**
1. The 5 top strategies.
- Five top Tactics
1. Personas that fit the strategies. 
- Persona Strategy
1. Information on controlling AI voice. 
- Creating Modulation 
- Using Indicators 

*Then this is a row with two columns.* 

**Agentic Production**
Overview 
- Cost, Benefit, Process 
- Glimpse into the SFA workings 
Looking Ahead 
- Pull the 'future potential' last page of the deck info to a page here 
- Pull the running list of custom tool build ideas here as well 

*This is another row with narrow columns that show the flow of the content.*

**Content Production Case Study** 
Overview 
- Input: Brand Identity Briefings 
- Comprehensive: Content Plans 
- Social: Instagram Posts 
- Direct: Email Blast

*Honestly these are more of a 'just making sure you see the full scope of what we can do' kind of thing.* 

**Deep Research Documents**
- Full Research for AI Voice Marketing 

