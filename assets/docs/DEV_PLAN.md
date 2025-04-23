# Development Plan: Voice Marketing Research Presentation

Content that is impressive in its own right, not any more or less impressive because of SFA. Reflecting my creative ability more than anything; the resources I use are only secondary in how they help me create at such a large scale. Must make sure the design is strong because his initial ask was if I could take on design work. 

## Project Overview
*File is being cleaned up and condensed as we go.*

We are at [PHASE 2: Build Slideshow](#phase-2-build-slideshow)

[Presentation Deck Design](#main-slides-section-design)
[Review Feedback](#review-feedback)
[Home Page Design](#home-page-design)
[Project Directory Structure](#project-directory-structure)

----

## Core Structure
1. Home page with overall navigation 
2. Presentation style deck section 
3. Document pages are markdown converted to HTML

## Development 

Continue working on the slide show until it is finished. It is the most important information to convey and time is of the essence. 

### Phase 1: Planning & Preparing
~~- Design Concept Planning for slideshow~~
~~- Design Concept Planning for homepage~~
~~- Compile scrolling logic and implementation~~
~~- Typography and color scheme~~
~~- Write slide copy~~
~~- Sean finish brand logo text SVG~~
~~- Review finalized planning~~

### Phase 2: Build Slideshow 
~~- Build slideshow section~~
~~- Make sure it is responsive~~
~~- Finish a second slide copy review to finalize~~
~~- Review slide design ~~
- Implement slide design 
--> [Feedback](#review-feedback)

**NOTE:** I have renamed the first presentation to `sales-development-ai-secrets.html` and moved it to the `ai-voice-telemarketing` directory. I've also linked to it below. 

- Implement feedback 
- Add final copy for presentation 1
- Allow for feedback review 
- When review and feedback is complete, add final copy for presentation 2
- Allow for feedback review 

*Presentation one:* 
[sales-development-ai-secrets.html](../../ai-voice-telemarketing/sales-development-ai-secrets.html)
[SLIDES_1_NARRATIVE.md](./SLIDES_1_NARRATIVE.md)

*Presentation two:* 
implement-ai-voice-marketing-research.html
[SLIDE_2_REVIEW_RESULTS.md](../docs/SLIDE_2_REVIEW_RESULTS.md)

#### Phase 2, continued. Preparing Pages for Resource Links in Presentations 
- Clean up markdown documents 
- Markdown > HTML Jekyll Template 
- Prepare for GitHub Pages deployment 
- Add URLs for these resources where needed
  - Referenced on slides 
  - Referenced in Navigation 
- Launch now so that the two slide shows can be presented if they need to be 

### Phase 3: Build Homepage  
- Sean finish colored-wavy shapes SVG for slides 
- Build homepage with just motion art
- New modular tiles link to pages (reference Portfolio's modular tiles and update after)
- Breadcrumb tracking 
- Make sure it is responsive 
- Prepare for updated website GitHub Pages deployment 
- Launch entire site this time  

### Phase 4: Improvements 
- Make homepage interactive 
- Add search functionality 
- Research section facelift 
- Quick-copy UI on script examples
- Quick-jump to sections
- Open in Google Docs UI option 
- Filtered viewing options

## Technical Stack

### Frontend
- Modern framework (React/Next.js)
- Responsive design system
- Animation library
- State management

### Content Management
- Markdown processing
- Dynamic routing
- Search functionality
- Reference system

----

# Main Slides Section Design 

## Background and Scrolling UX 

Creates a 'Slides' of deck experience. Scrolling UX replicates the macOS workspace swipe navigation on trackpads and mobile devices. UI key is swipe to next slide and let go before the 50% mark and it bounces back to the center of the page you were on. Let go after the 50% mark and it bounces out to the next panel's center. Use subtle arrows, visual cues, keyboard alternative scrolling. Appears on page load and then disappears when the user scrolls. 

## Interactive Elements 

### The Static Art 
Inspiration for [brand art](../images/brand-logo-art-inspo.png) background. Just pretend the phone isn't in the middle. Silhouette of mountains in the distance of the desert vibe. Actually is a [SVG](../images/brand-logo-cubed.svg) of brand logo text. On top we'll place very similar colored-wavy shapes. 

### Motion Logic 
The brand logo text will be almost exactly 100 vw wide and sticky so that it stays with the screen as it scrolls, with content of the file moving off to the side while new content moves in from the other side. The colored-wavy shapes will move similar to the content on the panels and will be static, made to fit across all of the panels; if there are 8 panels, it will be 800 vw wide exactly, with a bleed, e.g. the image goes right up as if off the screen. 

This should create a resource light but engaging UX that makes the left and right scrolling of the page feel intuitive instead of unusual. 

### Developing the Real Thing 

I'd like to hold off making the wavy shapes until we have the scrolling effect and content in place, including the sticky brand logo text art. This will ensure I only make it once, for the perfect fit. 

----

# Review Feedback 

## Scrolling 

Re: Scrolling, can we make it so that the arrows at the bottom of the page stay there instead of disappearing? Those work when you click them. And using the keyboard arrows works to move from section to section. 
Re: Scrolling, however you still can't use the scrolling on the trackpad at all; up and down does nothing, and swiping with gestures like that JS/CSS I found online, along with any changes you did or didn't make, doesn't work either. 
  - Should we look it up? Unless you set it up a way you knew of, the directions I found were direct from the Google Results and I mean that AI is honestly not very accurate in general. 
  - How does it all work? Like is this a common thing or not? I assumed so just by how easily that Google AI was able to provide an answer, but the site I made with v0 had issues with this same request. 
  - If all else fails we should ask Perplexity. They find really accurate results because they can search for sentiment, they're like tapped into Reddit that way. 
  - I just added a new Perplexity search MCP and refreshed all the MCPs. 

Re: Navigation Bar, Love the updated mobile nav character. Thank you for that. Clicking all those mobile nav links work as well, they go right to the correct section of the pseudo-slideshow. 
Re: Navigation Bar, I've added to images to this message. Though it hides my mouse when I take a screenshot, my mouse was hovering in both images. The first one, when our pages is positioned at 0-100vw. But the second was at 100vw-200vw and it didn't work. The buttons just don't highlight with hover and you can see that clicking them doesn't register. This is the same from 200vw all the way to the end of the page. 
Re: Navigation Bar, Also the nav buttons on the desktop version don't go anywhere even on the first-slide where they visually appear like they are functioning. 
  - What is the difference between the mobile and the desktop implementation with scrolling? I have a feeling it might be able that on desktop. Wdyt? It just doesn't seem to understand what to do. Because it is notable that the the nav buttons, which are anchors right?, *do* work on mobile view of the nav. 
  - However, I also wanted to note that I previewed the site locally on Safari and it looked like it had no CSS. *ACTUALLY* I bet you it is the freaking path issue. Why does that keep happening?! 
  - Either way, maybe we should try that other method for testing. You ran a server from the terminal, right? Because I'm curious if that might solve the path issue. But I'm also thinking I could look at it on my phone if we preview that way and see if the swiping works on mobile. 
  - Then we'd have an even more solid indication of it is actually the mobile versus desktop implementation at a deeper level or not. 

Okay one more thing that seems really notable, re: scrolling. At first the keyboard arrows work great! But when I go back to the page or look at it for a while and then try them again, they only move the page a tiny bit while you have the button pressed. That's weird right? Maybe we need to remove any complexity from the scrolling logic, if there is any to make it  more like the Mac OS scrolling UX, and see if it works at all or better. 

OMG so weird — when it was stuck between pages because of the keyboard arrows suddenly only nudging it a bit, I tried the swipe gesture on the trackpad and it worked. No idea what that means. But then it didn't work again. 

I don't really want to dig into the CSS and design tweaks I want to make until we can figure out these items. At that point we can chat about the Video embedding and option of doing an MP3 instead. I hate that I can see the Youtube thumbnail because it completely ruins the joke. 


## Title Slide Savvy (Re: Narrative Slide Show)

[130 Hz Sound](https://youtu.be/S7Jv1EZ7N8c?si=pwFslPGGj6CzsYpw). I could always get an actual MP3 if that is easier. Might be easier to be sneaky about the fact that the audio we're about to share helps with nothing tangible. 

## No Images Are Previewing In Any Browser **FIXED BUT FYI**

- Images weren't showing up because some of the paths weren't changing from relative to absolute when previewed. For example, I copied this from one of them now working as you can tell by the URL it created: "file:///assets/favicon/favicon-96x96.png" 
- They work now because I added "./" to all the paths. 
- IDK who "manages" HTML, like... globally, but I broke down the logic-rule, explained the consequences (that we're experiencing here), and then showed how allowing both "/" and "./" when you're writing a path from a file in the root to anywhere else breaks the logic by using an example of applying the broken logic's "logic" to an example. Hopefully they know about this issue because it is pain. Here is if you're curious. I put this together one day while spending hours trying to figure out exactly why so many paths on an old website we were making local wasn't working. `/Users/seanivore/Development/_resources/ai-dev-docs/_notes/SITE_ISSUES.md` 

----

# Home Page Design 

For the background of the deck slides section I proposed a two layer piece of art that create an interesting UX with one static and the length of all the slides, and the other moving with the screen as it scrolls. 

I'd like to explore a more visual motion art background for the home page, also our landing page. I have a similar piece of inspiration art for it, that uses one of the same pieces of art, but then are vibrant squares that look like extra big pixels that showering down from the art element. [Inspiration Art](../images/raining-giant-pixels.png) 

My logic is that, this is a presentation-centric site, that initially was only planned as it seemed the simplest way to showcase the agent work I could do for my friend Cliff's project for a client. I want to keep that mentality by not over-complicating the home page. This is one of those very rare occasions where it doesn't need to be marketing focused, so let's revel in that. 

Note that there are two main labor-intensive sections of this site. All the secondary pages will just be cleaned-up, simplified markdown files that jekyll can convert to HTML. That leaves design for the slides, proposed below; which I don't think will be complicated. The background is a simple 'fixed' versus sticky background dual layer art. Otherwise it is static — just the motion of scrolling creates the interactive feel. It also  proposes a very effect UX feel for side scrolling inspired by Mac OS, but I found implementation directions so easily I don't think that will be difficult either. Then the rest is just adding the text we composed. 

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

----

# Project Directory Structure 

Here's a tree so that we get all our asset reference paths correct, with **some updates in indicated** below. 

Users/seanivore/Development/voice-mkt-sfa/
├── ai-voice-telemarketing
│   ├── actionable-implementation
│   │   ├── persona-with-strategy
│   │   │   ├── persona-development.md
│   │   │   ├── voice-persona-scripts.md
│   │   │   └── voice-persona-strategy.md
│   │   └── writing-voice
│   │       ├── cheat-sheet.md
│   │       ├── modulation-guide.md
│   │       └── script-voice-indicators.md
│   ├── bland-ai-guides
│   │   ├── api-documentation.md
│   │   └── app-ui-guide.md
│   ├── full-research          `<-- Kept purely for reference, not main content to link to`
│   └── top-voice-strategy
│       ├── assertive-urgent.md
│       ├── curiosity-gap.md
│       ├── empathy-objection.md
│       ├── strategy-combo.md
│       └── strongest.md
├── assets                                   `<-- Removed font files and added Adobe provided CSS link`
│   ├── css
│   │   └── **main.css**              `<-- Separated CSS from the homepage HTML file`
│   ├── docs                                `<-- Draft things; moved DEV_PLAN.md, SLIDE_DRAFTS.md, and SLIDE_2_REVIEW_RESULTS.md to here`
│   │   ├── DEV_PLAN.md                              `<-- You are here`
│   │   ├── geometric-logo-text-art.ai
│   │   ├── ribbons-block-letters.ai
│   │   ├── SLIDE_1_REVIEW_RESULTS.md               `<-- Narrative slide to be first presentation version`
│   │   └── SLIDES_2_NARRATIVE.md               `<-- Original presentation, needs name to make sense next to "narrative deck"`
│   ├── favicon
│   └── images
├── CLAUDE.md
├── content-production-case-study                     `<-- Started reorganizing, preparing for phase 4`
│   ├── brand-identity-briefings.md
│   ├── content-plan
│   │   ├── glossier-content-plan.md
│   │   ├── hydro-flask-content-plan.md
│   │   ├── jungalow-content-plan.md
│   │   └── production-flow-content-plan.md
│   ├── email-blast
│   │   ├── glossier-email-campaign.md
│   │   ├── hydro-flask-email-campaign.md
│   │   └── production-flow-email-blast.md
│   ├── instagram-post
│   │   ├── glossier-instagram-posts.md
│   │   ├── hydro-flask-instagram-posts.md
│   │   └── production-flow-instagram-posts.md
│   └── writing-guide
│       └── emotion-driven-copywriting.md
├── cost-benefit.md
├── index.html                               `<-- Current primary HTML and JS file, combined`
└── README.md

18 directories, 62 files

Hidden project directories:
./.cursor
./.vscode

Hidden project files:
./.example.env
./.gitignore
./.sample.aider.conf.yml
