


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

