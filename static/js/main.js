
// is for image carouse 
document.addEventListener("DOMContentLoaded", () => {
    const mask = document.getElementById("js-gallery-mask");
    const rail = document.getElementById("js-smooth-rail");
    if (!mask || !rail) return;
    const cards = Array.from(rail.children);
    cards.forEach(card => rail.appendChild(card.cloneNode(true)));

    let autoSpeed = 0.8; 
    let currentX = 0;

    let isDragging = false;
    let isHovered = false;
    let startX = 0;
    let dragOffsetX = 0;

    function renderMarquee() {
      const resetPoint = rail.scrollWidth / 2;

      if (!isDragging && !isHovered) {
        currentX -= autoSpeed;
      }

      if (currentX <= -resetPoint) {
        currentX += resetPoint;
      } else if (currentX > 0) {
        currentX -= resetPoint;
      }

      rail.style.transform = `translateX(${currentX}px)`;
      requestAnimationFrame(renderMarquee);
    }

    mask.addEventListener("mouseenter", () => isHovered = true);
    mask.addEventListener("mouseleave", () => {
      isHovered = false;
      isDragging = false;
    });

    mask.addEventListener("mousedown", (e) => {
      isDragging = true;
      startX = e.pageX - currentX;
      dragOffsetX = 0;
    });

    window.addEventListener("mousemove", (e) => {
      if (!isDragging) return;
      e.preventDefault();
      
      const x = e.pageX;
      currentX = x - startX;
    });

    window.addEventListener("mouseup", () => {
      isDragging = false;
    });

    mask.addEventListener("touchstart", (e) => {
      isDragging = true;
      startX = e.touches[0].pageX - currentX;
    });

    mask.addEventListener("touchmove", (e) => {
      if (!isDragging) return;
      currentX = e.touches[0].pageX - startX;
    });

    mask.addEventListener("touchend", () => {
      isDragging = false;
    });

    renderMarquee();
  });

  
document.addEventListener('DOMContentLoaded', function () {
    const tabs = document.querySelectorAll('.agenda-tab');
    const days = document.querySelectorAll('.agenda-day');

    tabs.forEach(tab => {
        tab.addEventListener('click', function () {
            const target = this.getAttribute('data-target');

            // Reset all tabs to inactive style
            tabs.forEach(t => {
                t.classList.remove('bg-[var(--primary)]', 'border-[var(--primary)]');
                t.classList.add('bg-white/5', 'border-[var(--border)]');
            });

            // Activate clicked tab
            this.classList.remove('bg-white/5', 'border-[var(--border)]');
            this.classList.add('bg-[var(--primary)]', 'border-[var(--primary)]');

            // Show matching day, hide the rest
            days.forEach(day => {
                if (day.id === target) {
                    day.classList.remove('hidden');
                } else {
                    day.classList.add('hidden');
                }
            });
        });
    });
});