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

[Boxy and thick](https://fonts.adobe.com/fonts/agency-fb)
Sort of futura-esque, but much heavier bold, not as condensed, and interestingly shapely. 
The style and weight might not be accurate below. See [Agency FB](assets/images/agency-fb-sans-serif.png) for the correct style and weight, or to use a second weight for another heading. Note to not use the heaviest weight as it looks too much like the .brand font. 

```CSS
.h1 {
font-family: agency-fb, sans-serif;
font-style: bold;
font-weight: 700;
}
```

[Vinyl OT Oblique](https://fonts.adobe.com/fonts/vinyl)

```CSS
.h2 {
font-family: vinyl, sans-serif;
font-style: oblique;
font-weight: 400;
}
```

[Gimlet Micro](https://fonts.adobe.com/fonts/gimlet-micro)
[Gimlet Text Narrow](https://fonts.adobe.com/fonts/gimlet-text)
Elegant, timeless, very readable. Classic. Times New Roman but hip. 
The style and weight might not be accurate below. See [Gimlet Micro](assets/images/gimlet-micro-serif.png) for the correct style and weight, or to use a second weight for another heading. 

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

[P22 Glaser Babyteeth Solid](https://fonts.adobe.com/fonts/p22-glaser)

```CSS
.accent-2 {
font-family: p22-glaser-babyteeth-solid, sans-serif;
font-style: normal;
font-weight: 400;
}
.accent-3 {
font-family: p22-glaser-kitchen-regular, sans-serif;
font-style: normal;
font-weight: 400;
}
```

### Interactive Elements 

#### The Static Art 
Inspiration for [brand art](assets/images/brand-logo-art-inspo.png) background. Just pretend the phone isn't in the middle. Silhouette of mountains in the distance of the desert vibe. Actually is a [SVG](assets/images/SVG/brand-text-logo-v11.svg) of brand logo text. On top we'll place very similar colored-wavy shapes. 

Colors below are directly from the inspiration image. Let's pick our own, but still make sure they are that vibe of euphoric sunrise gradient of colors. 


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