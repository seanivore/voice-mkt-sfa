# Development Plan: Voice Marketing Research Presentation

## Project Overview

Content that is impressive in its own right, not any more or less impressive because of SFA. Reflecting my creative ability more than anything; the resources I use are only secondary in how they help me create at such a large scale. Must make sure the design is strong because his initial ask was if I could take on design work. 

## Core Structure
1. Home page with overall navigation 
2. Presentation style deck section 
3. Document pages are markdown converted to HTML

## Development 

First work on the slideshow from start to finish. It is the most important information to convey and time is of the essence. 

### Phase 1: Planning & Preparing
~~- Design Concept Planning for slideshow~~
~~- Design Concept Planning for homepage~~
~~- Compile scrolling logic and implementation~~
~~- Typography and color scheme~~
~~- Write slide copy~~
~~- Sean finish brand logo text SVG~~
- Review finalized planning 

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
│   ├── fonts
│   │   ├── `102 hidden font files`
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

Find .h1 as 'Lorem ipsum' using bold, not black; .h2 as 'SeanAugust' to the right; .p as the block of lorem ipsum text; .accent-1 as '28% increase'; the remaining 'SeanAugust' to the left side is the same as what the brand logo text art is. [Character Styles](assets/images/character-styles.png)

The URLs are included because this is the first time I've seen Adobe put the CSS right on the page. Maybe it doesn't show up if I wasn't logged in. Regardless though I did download all of the fonts from their hidden folder. If we want to use them that way, we'll need to do something Claude did for our Portfolio and create a script the looks at the font file's 'get info' to find the font name and then renames the file. Then change the font file type to .ttf. from .otf. This took them a minute to write and it ran perfectly so either way is fine. The [fonts](assets/fonts) directory is full with the whole family of each. 

#### Agency FB Sans Serif as .h1
[Boxy and thick](https://fonts.adobe.com/fonts/agency-fb)

```CSS
.h1 {
font-family: agency-fb, sans-serif;
font-style: bold;
font-weight: 700;
}
```

#### Vinyl OT Oblique as .h2

[Vinyl OT Oblique](https://fonts.adobe.com/fonts/vinyl)

```CSS
.h2 {
font-family: vinyl, sans-serif;
font-style: oblique;
font-weight: 400;
}
```

#### Gimlet Text Narrow as .p
[Gimlet Text Narrow](https://fonts.adobe.com/fonts/gimlet-text)

```CSS
.p {
font-family: gimlet-text-narrow, serif;
font-style: normal;
font-weight: 400;
}
```

[Sizmo Line Pro Lite](https://fonts.adobe.com/fonts/ff-sizmo)

```CSS
.accent-1 {
font-family: sizmo-line, sans-serif;
font-style: light;
font-weight: 300;
}
```

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

## Favicon 

Place in Head of website: 

```HTML
<link rel="icon" type="image/png" href="/assets/favicon/favicon-96x96.png" sizes="96x96" />
<link rel="icon" type="image/svg+xml" href="/assets/favicon/favicon.svg" />
<link rel="shortcut icon" href="/assets/favicon/favicon.ico" />
<link rel="apple-touch-icon" sizes="180x180" href="/assets/favicon/apple-touch-icon.png" />
<meta name="apple-mobile-web-app-title" content="AUGUST" />
<link rel="manifest" href="/assets/favicon/site.webmanifest" />
```

# Review Feedback 

## CSS <-- and --> HTML (lol) 

Off the bat just want to make sure you're planning on separating out the CSS to a /styles.css file during our next update to the HTML? It is a token-max-output pet peeve of mine. That said it might have had the same fate the following issues. Only 3.8k right now so NBD but I'm actually OCD haha. 

## Scrolling Doesn't Work without JS 

Also just FYI there are two JS scripts for the scrolling to work 😉 I very carefully included them for you in the dev plan. 

## No Images Are Previewing In Any Browser **FIXED**

Okay so... So the images weren't showing up. This is an oddity that pisses me off. When we pull my websites from Webflow/Framer there are always some paths that won't convert from relative. Here is one of the favicon I just pulled directly from the console for our current index.html preview that isn't working in any browser: "file:///assets/favicon/favicon-96x96.png" — lol wtf 

Pisses me off because: 

- In big projects, like my huge 'webflow-store' it will convert some of them with "./" and some with "/" IN THE SAME FILE, and refuse to convert some with "./" and some with "/" IN THE SAME FILE. 
- In all cases, as with currently, in the IDE I can click through the path to the file with "/" -- usually the full-proof way of testing your paths. Not here! 
- Using the IDE to input a path by the pop-up modal UI, it will always use "/" -- which all browsers are not finding right now. 

I spent so long trying to figure all this out for my 'webflow-store' site: @SITE_ISSUES.md

Clear rule that took me hours to figure out is: Write the path to accommodate where you are writing from, not where you are going. This subtle different is key apparently. 

"/" = ROOT no matter where the page you are on is 
"./" = Same directory the page you are on is in  
"../" = Back Up this many directories first 
"../../" = Back Up two directories (if you're on a page at fashion/lookbook/ for example) 

BUT — I would wager that this is the problem: because programmers are crazy, when you write a path to root from root, both "./" and "/" work. This doesn't make logical sense because, it is all about these characters before a path because every path starts from the root. So the conflict/annoyance/confusion is that "assets/images/brand-text-logo.svg" is NOT IN THE SAME DIRECTORY AS THE INDEX.HTML FILE and therefore "./" should NOT work!!! 

Genuinely think that HTML in general is having this confusion. 

BUT I just tried it and when I put a period in front of the paths in the index.html file, it worked. 

DOES NOT LOAD IN BROWSER: "/assets/images/brand-text-logo.svg"
LOADS IN BROWSER: "./assets/images/brand-text-logo.svg"

But watch, we're going to update them to have period and I bet you later they will stop working with freaking periods. 

Anyway. 

## Title Slide Savvy 

Omg, so let's use an impressive stat about how many Hz to speak at to improve conversions. Make it seem normal and like obvious how to do it. Then hook the joke by using the YouTube iFrame API's HTML to auto play WHAT 180 Hz SOUNDS LIKE. Spoiler: Hilariously like nothing helpful at all. It'll come of hilarious because it sort of sets things up like "oh god damn it, is everything here that Sean provided going to be completely useless?" Bait and switch, because then we're like BOOM cheat sheet to write this as notation in scripts. 

This YouTube API sounds PERFECT. is one page document has some HTML and JS to be able to queue it for playback and adjust volume to make sure it is up. There are certain events too which makes me wonder if we can burry the joke/lead even more rather than them going to the next slide and seeing the YouTube video's thumbnail giving away what it will play. [YouTube IFrame API](https://developers.google.com/youtube/iframe_api_reference) [GitHub YouTube API Examples](https://github.com/youtube/api-samples) [130 Hz Sound](https://youtu.be/S7Jv1EZ7N8c?si=pwFslPGGj6CzsYpw)

I could always get an actual MP3 if that is easier. Might be easier to be sneaky about the fact that the audio we're about to share helps with nothing tangible. 
