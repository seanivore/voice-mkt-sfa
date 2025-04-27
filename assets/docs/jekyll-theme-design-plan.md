# Markdown > HTML Jekyll Template 

## Project Overview 

### Style Guides 

Okay. So I have attached screenshots of the CSS I was playing around with for a Markdown to HTML extension. The HTML though is a mess, so better to just use is as visual reference because it uses the same typeface and color palettes as the two 'presentation deck' sections of the website. I attached photos of two slides from each of those two sections. 

This is the original CSS from the last set of slides with the charcoal background. 
`/Users/seanivore/Development/voice-mkt-sfa/assets/css/main.css`

And then this is the blue, funky fun one. 
`/Users/seanivore/Development/voice-mkt-sfa/assets/css/alt-slides.css`

And this is what I'd been playing with for the converter which you can see in the first three screenshots. 
`/Users/seanivore/Development/voice-mkt-sfa/assets/docs/MARKIT-HTML-CSS-LESS-HTML.md`

### Details from Our Last Implementation 

Our blog of all the Philosophy that Claude has written, `https://ai-philosophy.august.style`, we posted with only markdown files. We didn't really attempt to change the design much other than picking out an acceptable theme. And then it looks like you make layouts. 

The config file: `/Users/seanivore/Development/non-bio-life/_config.yml`

Layouts: 
`/Users/seanivore/Development/non-bio-life/_layouts/default.html`
`/Users/seanivore/Development/non-bio-life/_layouts/page.html`
`/Users/seanivore/Development/non-bio-life/_layouts/post.html`

Oh, and it looks like we did have some kind of CSS for that blog. 
`/Users/seanivore/Development/non-bio-life/assets/css/main.css` 

Would love a robust footer. There is so much research and so many types of content and strategy overviews that I want it to be very accessible. Oh also if possible breadcrumbs at the top would be great.

## This Website's Implementation 

Good understanding of requirements from materials provided. 

### Analysis of Current Materials

SFA Documentation Screenshots (1-3): 
- Clean, dark-themed technical documentation 
- Excellent code highlighting and clear hierarchy

BLAND AI Presentation Slides (4-7): Two distinct visual styles:
- Dark blue with gold/orange accents and colorful pixel art header bars
- Dark grid background with teal accent text

From the CSS files you've mentioned:
- main.css: Charcoal background presentation style
- alt-slides.css: Blue, more playful presentation style
- MARKIT-HTML-CSS-LESS-HTML.md: Your experimental CSS for the converter

From your philosophy blog implementation:
- Simple Jekyll setup with basic layouts
- Front matter was added via script (which you've now done manually)

### Implementation Plan

Create a Jekyll template that:

- Has a clean, technical documentation feel that honors your existing styles
- Incorporates some of the visual flair from your presentations
- Includes robust navigation (breadcrumbs + footer)
- Maintains good readability for your technical content

The approach: create a comprehensive Jekyll template that combines the visual elements from your presentations with a clean documentation style.

`/Users/seanivore/Development/voice-mkt-sfa/_config.yaml` 

- I'd like my URL to be 'presenting' august.style so just tweaked that
- Broadened the title beyond just the one case study 

The 'markdown.css' CSS file that will combine elements from both of your presentation styles while making it suitable for documentation:

`/Users/seanivore/Development/voice-mkt-sfa/assets/css/markdown.css`

- Added my typography and extended the color palette 

The default layout template that will serve as the base for all pages:

`/Users/seanivore/Development/voice-mkt-sfa/_layouts/default.html`

- Reviewed and updated the name of the CSS to 'markdown.css'

The page layout that extends the default layout:

`/Users/seanivore/Development/voice-mkt-sfa/_layouts/page.html`

Breadcrumbs include file:

`/Users/seanivore/Development/voice-mkt-sfa/_includes/breadcrumbs.html`

Oh nice I thought this might have to be another component like the nav on the other pages. We should plan ahead for search and filters, too, if that influences any decisions made now. 

Sidebar file that will generate a dynamic sidebar based on the current page:

`/Users/seanivore/Development/voice-mkt-sfa/_includes/sidebar.html` <-- *you were cut off by max message context length while writing this* 

So we should check if it is complete, however I did go through it and update for more "quick links" and organized a bit. I might be just about done. 