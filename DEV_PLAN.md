# Development Plan: Voice Marketing Research Presentation

## Project Overview

Content that is impressive in its own right, not any more or less impressive because of SFA. Reflecting my creative ability more than anything; the resources I use are only secondary in how they help me create at such a large scale. Must make sure the design is strong because his initial ask was if I could take on design work. 

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
- Build slideshow section
- Use Portfolio's modular HTML (and update it)
- Make sure it is responsive 
- Markdown > HTML Jekyll Template  
- Clean up markdown document 
- This should be individually launched

### Phase 3: Build Homepage & Other Pages 
- Sean create colored-wavy shapes SVG for slides 
- Build homepage with just motion art
- New modular tiles link to pages
- Breadcrumb tracking
- Make sure it is responsive 
- This is point to launch entire site 

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

## Project Directory Structure 

Here's a tree so that we get all our asset reference paths correct. 

Users/seanviore/Development/voice-mkt-sfa/
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
│   ├── full-research
│   │   ├── analysis-optimizing-voice-ai-mkt.md
│   │   ├── analysis-voice-mkt-home-services.md
│   │   ├── bland-ai-pro-tips.md
│   │   ├── bland-ai-voice-modulation.md
│   │   ├── strategy-assertive-urgent.md
│   │   ├── strategy-combinations.md
│   │   ├── strategy-curiosity-gap.md
│   │   ├── strategy-empathy-objection.md
│   │   └── strategy-strongest-combos.md
│   └── top-voice-strategy
│       ├── assertive-urgent.md
│       ├── curiosity-gap.md
│       ├── empathy-objection.md
│       ├── strategy-combo.md
│       └── strongest.md
├── assets
│   ├── docs
│   │   └── geometric-logo-text-art.ai
│   ├── favicon
│   │   ├── apple-touch-icon.png
│   │   ├── favicon-96x96.png
│   │   ├── favicon.ico
│   │   ├── favicon.svg
│   │   ├── site.webmanifest
│   │   ├── web-app-manifest-192x192.png
│   │   └── web-app-manifest-512x512.png
│   └── images
│       ├── agency-fb-sans-serif.png
│       ├── brand-logo-art-inspo.png
│       ├── character-styles-png
│       ├── gimlet-micro-serif.png
│       ├── raining-giant-pixels.png
│       ├── brand-text-logo.svg
│       ├── terminal-blurred-glass-ui-inspiration.png
│       ├── avatar-black.png
│       ├── avatar-colored.png
│       └── vscode-blurred-glass-inspiration.png
├── CLAUDE.md
├── content-production-case-study
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
├── DEV_PLAN.md
├── README.md
└── SLIDE_DRAFTS.md

## Home Page Design 

For the background of the deck slides section I proposed a two layer piece of art that create an interesting UX with one static and the length of all the slides, and the other moving with the screen as it scrolls. 

I'd like to explore a more visual motion art background for the home page, also our landing page. I have a similar piece of inspiration art for it, that uses one of the same pieces of art, but then are vibrant squares that look like extra big pixels that showering down from the art element. [Inspiration Art](assets/images/raining-giant-pixels.png) 

My logic is that, this is a presentation-centric site, that initially was only planned as it seemed the simplest way to showcase the agent work I could do for my friend Cliff's project for a client. I want to keep that mentality by not over-complicating the home page. This is one of those very rare occasions where it doesn't need to be marketing focused, so let's revel in that. 

Note that there are two main labor-intensive sections of this site. All the secondary pages will just be cleaned-up, simplified markdown files that jekyll can convert to HTML. That leaves design for the slides, proposed below; which I don't think will be complicated. The background is a simple 'fixed' versus sticky background dual layer art. Otherwise it is static — just the motion of scrolling creates the interactive feel. It also  proposes a very effect UX feel for side scrolling inspired by Mac OS, but I found implementation directions so easily I don't think that will be difficult either. Then the rest is just adding the text we composed. 

The home page is the only other section that requires some design work, other than a simple frame CSS/HTML theme edit for the Jekyll conversion. I've yet to really figure out the rest of the home page design and layout other than those raining pixels. Adn I'm thinking we'll make them motion but not interactive at first then double back if we have time to give some cursor interaction fun. I started planning the 'sections' or tiles or however we present the links to the secondary pages and the deck, but am not sure how to mix it up with the fun raining art idea yet. 

### Primary Sections For Navigation 

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

## Main 'Slides' Section Design 

### Background and Scrolling UX 

Creates a 'Slides' of deck experience. Imagine a horizontally scrolling website that is a off-white. Each "panel" or "slide" is 100 vw x 100 vh. (I wanted black but the inspiration art is black object on white and I can't picture it otherwise in a way I like.)

```CSS
body {
background-color: #fffdf6;
}
```

Scrolling UX replicates the macOS workspace swipe navigation on trackpads and mobile devices. It must not be unusual because the Google AI gathered the implementation details. Please make sure indeed make sense. 

The key with what makes the swiping workspaces to enjoyable is that you can push the content into to the next or previous panel but it bounces back to the center unless you cross the 50% mark, at which point you can let go and it bounces out to that next or previous panel's center instead, like it is weighted. 

Let's use incredible subtle arrow visual cues; the background art described below is our additional subconscious cues to scroll horizontally. The actual arrows should be of a transparent slightly-blurred glass effect, with the left < and right > arrow appearing indented or etched into the glass and frosted. They should appear on page-load and then disappear when the user scrolls. Below in equally subtle, transparent system font we should write "USE KEYBOARD DIRECTIONAL ARROWS" as our alternative scrolling method. 

Regarding preventing default behavior, I guess I'm not sure why that is needed. Or rather, I would prefer if when the user with a mouse and scroll wheel, goes to scroll down, the page should intuitively scroll to the next section, even though it is to the right. I've never found this confusing. 

Bonus points because it means the whole presentation is more basically mobile first because it is so natural on a phone to use gestures. 

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

### Content Column and Sidebar Navigation 

Two columns, one row. The right column takes up 80% of the width. Then along the left side-bar, taking up the remaining 20% of the screen, a navigation panel that provides direct links to resources to read more in depth about the content of the slide. 

On mobile, we'll use a hamburger menu but the icon is a very simple ^ arrow at the top right of the screen. It is appears to be the same material design as the arrows used in the scrolling UX. When clicked it flips 180º and shows the links as they would appear along the left side on desktop. The links are also in a model that matches the button: transparent, blurred glass. 

My Mac OS terminal does a nice job of [the glass effect](assets/images/terminal-blurred-glass-ui-inspiration.png). VS Code also does a nice job of this, and just like with my desktop background, we'll [see the art on the webpage](assets/images/terminal-blurred-glass-ui-inspiration.png) when in the slides section. This is very trendy, but it gives us opportunity to use our colors on the text; perhaps color-coding certain links with certain colors so that if needed one could super quickly identify the cheat sheet and navigate to it. One more thought, that might be best saved for phase 4, is to have the content the is currently over the art on the page disappear when the user opens the navigation modal, so that we're emphasizing the design choice. In fact, I like this idea so much that we might consider having at least a few links in a site-wide navigation, using the same hamburger menu style for desktop as well to keep our design language consistent and not clutter the presentation. 

### Typography and Color Scheme 

Added fonts to the CSS file. [Character Styles](assets/images/character-styles.png). The [fonts](/assets/fonts) directory is full with the whole family of each should we figure out how to pull the name from the metadata info. 


### Interactive Elements 

#### The Static Art 
Inspiration for [brand art](assets/images/brand-logo-art-inspo.png) background. Just pretend the phone isn't in the middle. Silhouette of mountains in the distance of the desert vibe. Actually is a [SVG](assets/images/brand-text-logo.svg) of brand logo text. On top we'll place very similar colored-wavy shapes. 

Colors below are directly from the inspiration image. Let's pick our own, but still make sure they are that vibe of euphoric sunrise gradient of colors. 

Note that this is made to go across the bottom of the screen with a nice margin below. 

```CSS
.brand-art-logo {
color: #151515;
}
.brand-art-wave {
color: #051644;
color: #560c78; 
color: #b92826;
color: #ec652b;
color: #edac3c;
}
```

#### Motion Logic 
The brand logo text will be almost exactly 100 vw wide and sticky so that it stays with the screen as it scrolls, with content of the file moving off to the side while new content moves in from the other side. The colored-wavy shapes will move similar to the content on the panels and will be static, made to fit across all of the panels; if there are 8 panels, it will be 800 vw wide exactly, with a bleed, e.g. the image goes right up as if off the screen. 

This should create a resource light but engaging UX that makes the left and right scrolling of the page feel intuitive instead of unusual. 

#### Developing the Real Thing 

I'd like to hold off making the wavy shapes until we have the scrolling effect and content in place, including the sticky brand logo text art. This will ensure I only make it once, for the perfect fit. 

----

# Review Feedback 

## Changes 

I separated into CSS and HTML files. CSS is at /assets/css/main.css

Updated the SVG logo to this cool looking cubist stylized font that is two that are layered and staggered and transparent so it is rad looking. Changed background color to play well with the logo transparency. 

## Navigation 

I added some depth with shading, pulled it from the bleed edge, curved the corners, more shadow below, and then set height to fit content. I made similar changes to the mobile nav and buttons. I'll probably continue working on the edges little by little every time we work on this. Uses system font for buttons. Honestly I love system font, if this wasn't a presentation purpose website I'd be strict to only using that. 

I gotta find a better "^" character maybe just different font and size. 

Is there a way to make it so the shadow doesn't rotate with the button when clicked? Maybe we move the rotation to just the character "^"? 

NOTE: on desktop, the nav buttons don't work on the other slides. Also it is sort of weird that you can click the UI helper buttons when they're not even there. Honestly if we make them not clickable at all that'd be okay with me. 

On mobile when you click the buttons they turn a light blue and then the same brown the other buttons change to when pressed. There is some kind of delay, I think maybe a transition for fading in. Note that there is no blue when buttons are pressed on desktop. 

## Scrolling Doesn't Work  

I thought there was no JS but just found it at the bottom of the HTML! 


## No Images Are Previewing In Any Browser **FIXED**

Images weren't showing up. Honestly I'm pretty sure this is a glitch with the way HTML is designed in general. All the paths didn't change to absolute. Here is one of the favicon I just pulled directly from the console for our current index.html preview that isn't working in any browser: "file:///assets/favicon/favicon-96x96.png". 

THis happens all the time. @SITE_ISSUES.md 

"/" = ROOT no matter where the page you are on is 
"./" = Same directory the page you are on is in  
"../" = Back Up this many directories first 
"../../" = Back Up two directories (if you're on a page at fashion/lookbook/ for example) 

And I've spent a lot of time trying to figure it out. At the core it is because the rule the *almost* always follows the logic is that paths are written to accommodate where you are writing from, not where you are going. This subtle difference is key. 

Which is why this is a glitch. The root paths anywhere sometimes require "./" and sometimes require "/". My webflow-short site has conflicts IN THE SAME FILE. 

It is pretty annoying. Even if you use the IDE to select a path from the UI modal pop-up, it follow the rule and does not give a a path written on a file at the root, like index.html going to say /assets/favicon/favicon-96x96.png. The rule is "./" is reserved for "in the same directory as you are writing from" and obviously index.html is not in the same directory as the favicon. 

I won't be surprised if it eventually wants the periods to be removed. but for now I updated them all. This whole file was actually sort of strange like design stuff was appearing over time -- at first I thought you were in the file making nice updates lol. 

## Title Slide Savvy 

Omg, so let's use an impressive stat about how many Hz to speak at to improve conversions. Make it seem normal and like obvious how to do it. Then hook the joke by using the YouTube iFrame API's HTML to auto play WHAT 180 Hz SOUNDS LIKE. Spoiler: Hilariously like nothing helpful at all. It'll come of hilarious because it sort of sets things up like "oh god damn it, is everything here that Sean provided going to be completely useless?" Bait and switch, because then we're like BOOM cheat sheet to write this as notation in scripts. 

This YouTube API sounds PERFECT. is one page document has some HTML and JS to be able to queue it for playback and adjust volume to make sure it is up. There are certain events too which makes me wonder if we can burry the joke/lead even more rather than them going to the next slide and seeing the YouTube video's thumbnail giving away what it will play. [YouTube IFrame API](https://developers.google.com/youtube/iframe_api_reference) [GitHub YouTube API Examples](https://github.com/youtube/api-samples) [130 Hz Sound](https://youtu.be/S7Jv1EZ7N8c?si=pwFslPGGj6CzsYpw)

I could always get an actual MP3 if that is easier. Might be easier to be sneaky about the fact that the audio we're about to share helps with nothing tangible. 

## Fonts 

Interest thing. Sonny 3.5 from months ago when we first started setting up my portfolio site, we pulled the fonts directly for the dumb hidden file they put them in, they ran a command to rename them from their ".47208.otf" random name to literally "47208.otf first. Then we went through almost the exact same experience as today except not listening to me, lol. Because last time they tried 'font forge' and it didn't work. Then I told them that if you open the font file's info the metadata has the font name. So last time they wrote a script that looked there and did that. Then they wrote another script to change the file from .otf to .ttf. I remember so specifically because it was the first thing they every wrote a script on the fly for and ran the terminal command. It took them only a few minutes and 100s of fonts were fixed — I even still have them named because I put them back in the hidden folder in a "file name" sub-folder and they're still .otf files. 

Well this time, they kep trying to use font forge and then was having issues from there being spaces in some of the names. And they eventually gave up because "my font forge isn't working". And I was like, you didn't even use that last time! THEN they said the pixelated fonts were really cool for another project and AGREED THAT ADOBE ROTATES FONTS QUICKLY SO THEY MIGHT NOT BE THERE by then. So I guess for now we're using the Adobe import method. Then they made this super weird document of cards in HTML showing off the names of the fonts and acted like they didn't know I had the Adobe web font link to import them. So very weird. Like yes I have it but also I have paid monthly to adobe for a decade I think I can have my fonts considering they put them on my computer like can they even put thing on my property and then say it isn't my property? So weird. Anyway. 

Super weird file: `/Users/seanivore/Development/_resources/ai-dev-docs/adobe-fonts-demo.html` @adobe-fonts-demo.html 
Many attempts: `/Users/seanivore/Development/voice-mkt-sfa/assets/docs/convert-name-fonts/` @/assets/docs/convert-name-fonts/ 
Such rad fonts I spent an hour just looking threw all the new additions: 
`/Users/seanivore/Development/_resources/ai-dev-docs/font-examples` @ai-dev-docs/font-examples/

I updated all the font names to be exact matches from Adobe. I added the import link. 