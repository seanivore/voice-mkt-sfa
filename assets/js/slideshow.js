/**
 * Slide Show Navigation System
 * Implements macOS-style swipe behavior with momentum and snapping
 */

document.addEventListener("DOMContentLoaded", () => {
  // Core elements
  const scrollableContainer = document.getElementById("slides");
  const navArrows = document.getElementById("navArrows");
  const prevSlide = document.getElementById("prevSlide");
  const nextSlide = document.getElementById("nextSlide");
  const mobileNavToggle = document.getElementById("mobileNavToggle");
  const mobileNav = document.getElementById("mobileNav");

  // Only proceed if we found the slides container
  if (!scrollableContainer) return;

  // Add our special scroll snap mode
  scrollableContainer.classList.add("scroll-snap-mode");

  // Calculate slide dimensions
  const getSlideWidth = () => document.querySelector(".slide").offsetWidth;
  const getMaxScroll = () =>
    scrollableContainer.scrollWidth - scrollableContainer.offsetWidth;

  // Track scroll state
  let startX = 0;
  let isScrolling = false;
  let timeoutId;
  let currentPosition = 0;
  let isDragging = false;
  let startScrollLeft = 0;

  // Setup navigation links
  const setupNavLinks = () => {
    const navLinks = document.querySelectorAll('.nav-link[href^="#slide"]');

    navLinks.forEach((link) => {
      link.addEventListener("click", (e) => {
        e.preventDefault();
        const targetId = link.getAttribute("href").substring(1);
        const targetSlide = document.getElementById(targetId);

        if (targetSlide) {
          // Close mobile nav if it's open
          if (mobileNav && mobileNav.classList.contains("active")) {
            mobileNav.classList.remove("active");
            mobileNavToggle.classList.remove("active");
          }

          // Scroll to the target slide
          const slideIndex = Array.from(
            document.querySelectorAll(".slide")
          ).indexOf(targetSlide);
          const slideWidth = getSlideWidth();
          const targetPosition = slideIndex * slideWidth;

          scrollableContainer.scrollTo({
            left: targetPosition,
            behavior: "smooth",
          });

          showThenHideArrows();
        }
      });
    });
  };

  // MacOS-style snapping logic
  const snapToSlide = () => {
    const slideWidth = getSlideWidth();
    const currentScroll = scrollableContainer.scrollLeft;
    const slideIndex = Math.round(currentScroll / slideWidth);
    const targetPosition = slideIndex * slideWidth;

    scrollableContainer.scrollTo({
      left: targetPosition,
      behavior: "smooth",
    });
  };

  // Navigation functions
  const goToNextSlide = () => {
    const slideWidth = getSlideWidth();
    const currentSlideIndex = Math.floor(
      scrollableContainer.scrollLeft / slideWidth
    );
    const targetPosition = (currentSlideIndex + 1) * slideWidth;

    // Don't go past the end
    if (targetPosition <= getMaxScroll()) {
      scrollableContainer.scrollTo({
        left: targetPosition,
        behavior: "smooth",
      });
    }

    showThenHideArrows();
  };

  const goToPrevSlide = () => {
    const slideWidth = getSlideWidth();
    const currentSlideIndex = Math.round(
      scrollableContainer.scrollLeft / slideWidth
    );
    const targetPosition = (currentSlideIndex - 1) * slideWidth;

    // Don't go past the beginning
    if (targetPosition >= 0) {
      scrollableContainer.scrollTo({
        left: targetPosition,
        behavior: "smooth",
      });
    }

    showThenHideArrows();
  };

  // Arrow visibility management
  const showThenHideArrows = () => {
    navArrows.classList.remove("hidden");

    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => {
      navArrows.classList.add("hidden");
    }, 1500);
  };

  // Mouse wheel (trackpad) handling
  scrollableContainer.addEventListener("wheel", (event) => {
    event.preventDefault();

    // Handle horizontal trackpad gestures (deltaX) first
    if (Math.abs(event.deltaX) > Math.abs(event.deltaY)) {
      const newPosition = scrollableContainer.scrollLeft + event.deltaX;

      if (newPosition >= 0 && newPosition <= getMaxScroll()) {
        scrollableContainer.scrollLeft = newPosition;
      }
    }
    // If it's primarily vertical scroll (or a regular mouse wheel), treat as horizontal
    else {
      const newPosition = scrollableContainer.scrollLeft + event.deltaY;

      if (newPosition >= 0 && newPosition <= getMaxScroll()) {
        scrollableContainer.scrollLeft = newPosition;
      }
    }

    showThenHideArrows();
  });

  // Touch/drag handling for mobile and desktop
  scrollableContainer.addEventListener("mousedown", (event) => {
    isDragging = true;
    startX = event.pageX;
    startScrollLeft = scrollableContainer.scrollLeft;
    scrollableContainer.style.cursor = "grabbing";
    event.preventDefault();
  });

  window.addEventListener("mouseup", () => {
    if (isDragging) {
      isDragging = false;
      scrollableContainer.style.cursor = "grab";
      snapToSlide();
    }
  });

  window.addEventListener("mousemove", (event) => {
    if (!isDragging) return;
    const deltaX = event.pageX - startX;
    scrollableContainer.scrollLeft = startScrollLeft - deltaX;
    showThenHideArrows();
  });

  // Mobile touch events
  scrollableContainer.addEventListener("touchstart", (event) => {
    startX = event.touches[0].clientX;
    startScrollLeft = scrollableContainer.scrollLeft;
    isScrolling = true;
  });

  scrollableContainer.addEventListener("touchmove", (event) => {
    if (!isScrolling) return;

    // Calculate swipe distance
    const currentX = event.touches[0].clientX;
    const deltaX = currentX - startX;

    // Update scroll position with momentum-based tracking
    const newScrollPosition = startScrollLeft - deltaX;

    if (newScrollPosition >= 0 && newScrollPosition <= getMaxScroll()) {
      scrollableContainer.scrollLeft = newScrollPosition;
    }

    showThenHideArrows();
  });

  scrollableContainer.addEventListener("touchend", () => {
    if (isScrolling) {
      isScrolling = false;
      snapToSlide();
    }
  });

  // Arrow navigation buttons
  if (prevSlide) {
    prevSlide.addEventListener("click", goToPrevSlide);
  }

  if (nextSlide) {
    nextSlide.addEventListener("click", goToNextSlide);
  }

  // Keyboard navigation
  document.addEventListener("keydown", (event) => {
    if (event.key === "ArrowLeft") {
      goToPrevSlide();
    }
    if (event.key === "ArrowRight") {
      goToNextSlide();
    }
  });

  // Scroll events to show/hide arrows
  scrollableContainer.addEventListener("scroll", () => {
    showThenHideArrows();
  });

  // Mobile navigation toggle
  if (mobileNavToggle && mobileNav) {
    mobileNavToggle.addEventListener("click", () => {
      mobileNav.classList.toggle("active");
      mobileNavToggle.classList.toggle("active");
    });
  }

  // Setup all navigation links
  setupNavLinks();

  // Show arrows on page load, then hide
  showThenHideArrows();
});
