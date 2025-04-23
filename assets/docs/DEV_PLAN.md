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

```CSS 
.scrollable-container {
/* enables horizontal scrolling on the element */
  overflow-x: scroll;
/* prevents the page from being dragged back to the previous page when the horizontal scroll reaches the edges */
  overscroll-behavior-x: contain;
}
```

```JavaScript
// Trackpad handling
const scrollableContainer = document.querySelector('.scrollable-container');
// This event listener detects trackpad scrolling
scrollableContainer.addEventListener('mousewheel', (event) => {
//Prevents the default scrolling behavior (page navigation).
  event.preventDefault();

  // Get scroll boundaries
  const maxX = scrollableContainer.scrollWidth - scrollableContainer.offsetWidth;

  // Prevent scrolling beyond boundaries and determine the direction of scrolling by checking event.deltaX value
  const currentScroll = scrollableContainer.scrollLeft;
  const newScrollPosition = currentScroll + event.deltaX;

  if (newScrollPosition < 0) {
    scrollableContainer.scrollLeft = 0;
    return;
  }
  if (newScrollPosition > maxX) {
    scrollableContainer.scrollLeft = maxX;
    return;
  }

  // Apply the scroll
  scrollableContainer.scrollLeft = newScrollPosition;
});
```

```JavaScript
// Mobile handling
const scrollableContainer = document.querySelector('.scrollable-container');
let startX = 0;
let isScrolling = false;
// Handle touch events on mobile devices
scrollableContainer.addEventListener('touchstart', (event) => {
  startX = event.touches[0].clientX;
  isScrolling = true;
});
// Handle touch events on mobile devices
scrollableContainer.addEventListener('touchmove', (event) => {
  if (!isScrolling) return;
  event.preventDefault();

  // Get scroll boundaries
  const maxX = scrollableContainer.scrollWidth - scrollableContainer.offsetWidth;

  // Calculate swipe distance (Track the touch position and calculate the distance swiped. Update the scroll position accordingly.)
  const currentX = event.touches[0].clientX;
  const deltaX = currentX - startX;

  // Update scroll position (Track the touch position and calculate the distance swiped. Update the scroll position accordingly.)
  scrollableContainer.scrollLeft -= deltaX;

  // Prevent scrolling beyond boundaries
  if (scrollableContainer.scrollLeft < 0) {
    scrollableContainer.scrollLeft = 0;
  }
  if (scrollableContainer.scrollLeft > maxX) {
    scrollableContainer.scrollLeft = maxX;
  }
});

scrollableContainer.addEventListener('touchend', () => {
  isScrolling = false;
});
```

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

## Changes 

File updates:
- I separated into CSS and HTML files. CSS is at /assets/css/main.css
- Let's also separate out the JS. 
- I removed the fonts from the repo and added the Adobe link. 

Design updates:
- Updated the SVG logo to this cool looking cubist stylized font that is two that are layered and staggered and transparent so it is rad looking. Changed background color to play well with the logo transparency. Made a large number of changes to the CSS until it felt perfect. 
- On the navigation bar I added shading depth, pulled away from edge, curved the corners, set height to fit content. I made similar changes to the mobile nav and buttons. I often do this and will probably make little changes every time I'm working in there. I'll try to include the most notable changes, but just FYI so that if you see something that looks changed from what you recall you can just check with me. 

Slide show updates:
- I went to create a title slide and it turned into something so big that I made it into a second slide show. All copy is finalized. When you check them out, LMK what you think. I feel like they both have value, but I didn't want one super long presentation. I condensed a lot, but got to a point where I just didn't want to remove anymore. 
- COPY FOR NARRATIVE SLIDE SHOW: `/Users/seanivore/Development/voice-mkt-sfa/assets/docs/SLIDES_1_NARRATIVE.md`
- COPY FOR ORIGINAL SLIDE SHOW: `/Users/seanivore/Development/voice-mkt-sfa/assets/docs/SLIDE_2_REVIEW_RESULTS.md` 
- This new version is very much a "narrative" version, but so I'm not sure what to call the other version. When we figure out what to call each to identify them, let's change their HTML file names to their appropriate URL slugs. At that point the 'index.html' will only be the HTML for the home page. 

## Scrolling  

1. It doesn't work.I thought there was no JS but just found it at the bottom of the HTML. 
2. Sort of weird we can click the UI buttons even when you can't see them. Do they need to be clickable at all? 

## Navigation Bar

1. We need a better "^" character. Maybe just different font and size. 
2. Is there a way to make it so the shadow doesn't rotate with the button when clicked? Maybe we move the rotation to just the character "^" inside the circle button? 
3. On desktop, the nav buttons don't click when you are not on the first slide. 
4. On mobile when you click the buttons they turn a light blue and then the same brown the other buttons change to when pressed. There is some kind of delay, I think maybe a transition for fading in. Note that there is no blue when buttons are pressed on desktop. 

## Title Slide Savvy (Re: Narrative Slide Show)

Omg, what do you think of this idea. I'm thinking we should use an impressive stat about how many Hz to speak at to improve conversions. Make it seem normal and like obvious how to do it. Then hook the joke by using the YouTube iFrame API's HTML to auto play WHAT 180 Hz SOUNDS LIKE. Spoiler: Hilariously like nothing helpful at all. It'll come of hilarious because it sort of sets things up like "oh god damn it, is everything here that Sean provided going to be completely useless?" Bait and switch, because then we're like BOOM cheat sheet to write this as notation in scripts. 

This YouTube API sounds PERFECT. is one page document has some HTML and JS to be able to queue it for playback and adjust volume to make sure it is up. There are certain events too which makes me wonder if we can burry the joke/lead even more rather than them going to the next slide and seeing the YouTube video's thumbnail giving away what it will play. [YouTube IFrame API](https://developers.google.com/youtube/iframe_api_reference) [GitHub YouTube API Examples](https://github.com/youtube/api-samples) [130 Hz Sound](https://youtu.be/S7Jv1EZ7N8c?si=pwFslPGGj6CzsYpw)

I could always get an actual MP3 if that is easier. Might be easier to be sneaky about the fact that the audio we're about to share helps with nothing tangible. 

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
