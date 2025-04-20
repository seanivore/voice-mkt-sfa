# Development Plan: Voice Marketing Research Presentation

## Project Overview
Present voice marketing research and strategies in an engaging, professional website format that emphasizes immediate business value while providing depth through linked resources.

## Core Structure

### 1. Landing Experience
- Emotional hook from slide presentation
- Clear value proposition
- Visual representation of voice marketing impact
- Quick-access navigation to key sections

### 2. Main Content Sections
Each section follows presentation flow:
- Client's Challenge
- Our Challenge
- The Discovery
- The Solution
- Strategy Examples
- Implementation Tools

### 3. Resource Library
Organized access to all research documents:
- Voice Strategy Documents
- Technical Guides
- Implementation Frameworks
- Case Studies & Examples

## Technical Requirements

### Design System
- Clean, professional aesthetic
- Clear typography hierarchy
- Consistent color scheme
- Mobile-responsive layout
- Accessible navigation

### Interactive Elements
- Slide-style navigation
- Expandable research sections
- Quick-copy script examples
- Linked reference system
- Progress tracking

### Content Organization
- Progressive disclosure of information
- Clear pathways through material
- Easy access to source documents
- Practical implementation guides

## Development Phases

### Phase 1: Core Structure
- Set up project architecture
- Implement basic navigation
- Create content templates
- Establish design system

### Phase 2: Content Integration
- Format all research documents
- Create interactive elements
- Implement cross-referencing
- Build resource library

### Phase 3: Enhancement
- Add interactive examples
- Implement progress tracking
- Create quick-reference tools
- Optimize user experience

### Phase 4: Polish
- Refine animations
- Optimize performance
- Add final styling
- Test all functionality

## Key Features

### Navigation System
- Slide-style main navigation
- Quick-jump to sections
- Breadcrumb tracking
- Progress indicators

### Content Display
- Progressive reveal of information
- Expandable research sections
- Linked references
- Quick-copy functionality

### Resource Management
- Organized document library
- Search functionality
- Filtered viewing options
- Download capabilities

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

## Quality Assurance

### Testing Requirements
- Mobile responsiveness
- Cross-browser compatibility
- Performance optimization
- Accessibility compliance

### Success Metrics
- Navigation clarity
- Content accessibility
- Load time optimization
- User engagement tracking

## Future Considerations

### Potential Enhancements
- Interactive voice examples
- Real-time script testing
- Community contributions
- Integration with voice platforms

### Scalability
- Content expansion system
- Version control for research
- User accounts (if needed)
- Analytics integration

## Implementation Notes

### Priority Features
1. Clear navigation system
2. Easy access to research
3. Quick-copy functionality
4. Mobile optimization

### Development Guidelines
- Focus on immediate value
- Maintain professional aesthetic
- Ensure easy maintenance
- Prioritize performance

## Timeline & Milestones

### Week 1: Setup & Structure
- Project setup
- Core architecture
- Basic navigation
- Content templates

### Week 2: Content & Features
- Research integration
- Interactive elements
- Cross-referencing
- Resource library

### Week 3: Enhancement & Testing
- User experience optimization
- Performance testing
- Content refinement
- Bug fixes

### Week 4: Polish & Launch
- Final styling
- Documentation
- Launch preparation
- Deployment

## Documentation Requirements

### Technical Documentation
- Setup instructions
- Maintenance guides
- Update procedures
- Troubleshooting

### Content Guidelines
- Formatting standards
- Reference system
- Content organization
- Update processes

## Maintenance Plan

### Regular Updates
- Content refreshes
- Performance optimization
- Feature enhancements
- Bug fixes

### Monitoring
- Usage analytics
- Performance metrics
- Error tracking
- User feedback

## Next Steps

1. Review and finalize technical requirements
2. Set up development environment
3. Begin Phase 1 implementation
4. Schedule regular progress reviews 

----

## Main 'Slides' Section Design 

### Background and Scrolling UX 

Creates a 'Slides' of deck experience. 

Imagine a horizontally scrolling website that is a dark charcoal color, almost black but slightly faded. Each "panel" or "slide" is 100 vw x 100 vh. 

For scrolling, let's create a horizontal scrolling experience that mimics the macOS workspace swipe navigation on trackpads and mobile devices by combining CSS for overflow and over-scroll behavior with JavaScript event handling. 

The key is that you can push the content to the next or previous panel but it bounces back to the center unless you cross the 50% mark at which point you can let go and it bounces back to that next or previous panel's center. 

Visual cues are transparent glass-like and simple < and > arrows at the bottom of the screen on pageload until the user scrolls. We can make them look similar to the narrow and wide left and right directional keys on a keyboard, then offer that as an alternative scrolling method. 

Regarding preventing default behavior, I guess I'm not sure why that is needed. 

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

Almost one column. Make the right column take up 80% of the width. Then along the left side-bar, taking up the remaining 20% of the screen, a navigation panel that provides direct links to resources to read more in depth about the content of the slide. 

On mobile, it is a vertical stack of links in a model that shows using a hamburger menu. The icon should be a very simple ^ arrow, but with a wider stance. When clicked it flips 180º and shows the links as they would appear along the left side on desktop. 

### Typography and Color Scheme 

[Boxy and thick](https://fonts.adobe.com/fonts/agency-fb)
Sort of futura-esque, but much heavier bold, not as condensed, and interestingly shapely. 
The style and weight might not be accurate below. See [Agency FB](assets/images/agency-fb-sans-serif.png) for the correct style and weight, or to use a second weight for another heading. Note to not use the heaviest weight as it looks too much like the .brand font. 

```CSS
.H1 {
font-family: agency-fb, sans-serif;
font-style: normal;
font-weight: 700;
}
```

[Gimlet Micro](https://fonts.adobe.com/fonts/gimlet-micro)
Elegant, timeless, very readable. Classic. Times New Roman but hip. 
The style and weight might not be accurate below. See [Gimlet Micro](assets/images/gimlet-micro-serif.png) for the correct style and weight, or to use a second weight for another heading. 

```CSS
.p {
font-family: gimlet-micro, serif;
font-style: normal;
font-weight: 300;
}
```

### Interactive Elements 

The brand font is [Pressio](https://fonts.adobe.com/fonts/pressio). Depending on how much it lets me edit it, we might be able to actually use the CSS. Otherwise I'm going to either use the [lowercase](assets/images/pressio-black-lower-case.png) or [uppercase](assets/images/pressio-black-upper-case.png) version, and convert it to vectors, then open up the white space to make it less legible. I'm not sure [transforming](https://developer.mozilla.org/en-US/docs/Web/CSS/transform) the letters will look as good as an edited SVG. 

```CSS
.brand {
font-family: pressio, sans-serif;
font-style: normal;
font-weight: 700;
}
```
I would like to have it across the lower-middle of the screen, and stays with the screen as it scrolls. With paths edited it will sort of look like the silhouette of mountains in the distance of the desert. 

Over top of it, and varying in wavy color shapes, reaching from the start of the first panel on the left to the end of the last panel on the right, when the user scrolls left and right it will move in front of the [brand font art](assets/images/brand-logo-art-inspo.png). Just pretend the phone isn't in that inspiration image. 

The UX would be that the colors on top of the brand font art move, staying with whatever is on the screen. At the same time, the the shapes of the brand font art stay still behind the colors, moving with the screen as it scrolls, the content on the page moving off to one side of the screen as new content moves in from the other side. 

The result should be a very engaging but simple to implement UX that will be a great way to keep the user engaged with the content as they scroll, even helping encourage them to intuitively understand the horizontal scrolling behavior. 
