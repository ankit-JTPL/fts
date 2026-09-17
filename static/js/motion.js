window.addEventListener("DOMContentLoaded", () => {
  // 1. Top Level Plugin Registration
  if (typeof gsap !== "undefined" && typeof ScrollTrigger !== "undefined") {
    gsap.registerPlugin(ScrollTrigger);

    // Optional ScrollSmoother register if loaded
    if (typeof ScrollSmoother !== "undefined") {
      gsap.registerPlugin(ScrollSmoother);
    }

    // =========================================
    // 1. HORIZONTAL SCROLL (Tracks Section)
    // =========================================
    const rail = document.getElementById("tracks-horizontal-rail");
    const section = document.getElementById("tracks-fullscreen-section");

    if (rail && section) {
      const getScrollAmount = () => rail.scrollWidth - window.innerWidth;

      gsap.to(rail, {
        x: () => -getScrollAmount(),
        ease: "none",
        scrollTrigger: {
          trigger: section,
          start: "top top",
          end: () => `+=${getScrollAmount()}`, // Fixed: Exact scroll distance calculation
          pin: true,
          scrub: 1,
          invalidateOnRefresh: true,
        },
      });
    }

    // =========================================
    // 2. FADE UP
    // =========================================
    gsap.utils.toArray(".fade-up").forEach((element) => {
      gsap.from(element, {
        scrollTrigger: {
          trigger: element,
          start: "top 85%",
          toggleActions: "play none none reverse",
        },
        y: 50, // Reduced from 80 for smoother feel
        opacity: 0,
        duration: 0.8,
        ease: "power3.out",
        clearProps: "transform,opacity",
      });
    });

    // =========================================
    // 3. SLIDE LEFT
    // =========================================
    gsap.utils.toArray(".slide-left").forEach((element) => {
      gsap.from(element, {
        scrollTrigger: {
          trigger: element,
          start: "top 85%",
          toggleActions: "play none none reverse", // Fixed "reset" bug
        },
        x: -120, // 200 is too far off-screen on mobile, 120 is ideal
        opacity: 0,
        duration: 1,
        ease: "power3.out",
        clearProps: "transform,opacity",
      });
    });

    // =========================================
    // 4. SLIDE RIGHT
    // =========================================
    gsap.utils.toArray(".slide-right").forEach((element) => {
      gsap.from(element, {
        scrollTrigger: {
          trigger: element,
          start: "top 85%",
          toggleActions: "play none none reverse", // Fixed "reset" bug
        },
        x: 120,
        opacity: 0,
        duration: 1,
        ease: "power3.out",
        clearProps: "transform,opacity",
      });
    });

    // =========================================
    // 5. ZOOM IN
    // =========================================
    gsap.utils.toArray(".zoom-in").forEach((element) => {
      gsap.from(element, {
        scrollTrigger: {
          trigger: element,
          start: "top 85%",
          toggleActions: "play none none reverse", // Fixed "reset" bug
        },
        scale: 0.85,
        opacity: 0,
        duration: 0.8,
        ease: "back.out(1.5)",
        clearProps: "transform,opacity",
      });
    });

    // =========================================
    // 6. STAGGER GRID 
    // =========================================
    gsap.utils.toArray(".stagger-wrapper").forEach((wrapper) => {
      const items = wrapper.querySelectorAll(".stagger-item");

      if (items.length > 0) {
        gsap.from(items, {
          scrollTrigger: {
            trigger: wrapper,
            start: "top 88%",
            toggleActions: "play none none reverse",
          },
          y: 40,
          opacity: 0,
          stagger: 0.12,
          duration: 0.7,
          ease: "power2.out",
          clearProps: "transform,opacity",
        });
      }
    });
  }
});