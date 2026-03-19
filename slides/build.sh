#!/usr/bin/env bash
# Build presentation.html from fragments
# Usage: ./build.sh [en]

set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"

if [[ "${1:-}" == "en" ]]; then
  SUFFIX="-en"
  OUT="presentation-en.html"
else
  SUFFIX=""
  OUT="presentation.html"
fi

HEADER="$DIR/academic-light.css"
PARTS=(
  "$DIR/ch-opening${SUFFIX}.html"
  "$DIR/ch-part1${SUFFIX}.html"
  "$DIR/ch-part2${SUFFIX}.html"
  "$DIR/ch-part3${SUFFIX}.html"
  "$DIR/ch-closing${SUFFIX}.html"
)

# Verify all fragments exist
for f in "$HEADER" "${PARTS[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "Missing: $f" >&2
    exit 1
  fi
done

{
  echo '<!DOCTYPE html>'
  echo '<html lang="zh-CN">'
  echo '<head>'
  echo '<meta charset="UTF-8">'
  echo '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
  echo '<title>CC Research Playbook</title>'
  echo '<link rel="preconnect" href="https://fonts.googleapis.com">'
  echo '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Source+Serif+4:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">'
  echo '<style>'
  cat "$HEADER"
  echo '</style>'
  echo '</head>'
  echo '<body>'
  echo '<div class="progress-bar" id="progressBar"></div>'
  echo '<nav class="nav-dots" id="navDots"></nav>'
  echo '<div class="slide-counter mono dim" id="slideCounter" style="position:fixed;bottom:clamp(0.5rem,1.5vh,1rem);right:clamp(0.8rem,2vw,1.5rem);font-size:clamp(0.6rem,0.8vw,0.75rem);z-index:1000;opacity:0.5;">1 / 1</div>'
  for part in "${PARTS[@]}"; do
    cat "$part"
  done
  cat <<'JSEOF'
<script>
class SlidePresentation {
    constructor() {
        this.slides = document.querySelectorAll('.slide');
        this.currentSlide = 0;
        this.progressBar = document.getElementById('progressBar');
        this.navDots = document.getElementById('navDots');
        this.slideCounter = document.getElementById('slideCounter');
        this.createNavDots();
        this.setupIntersectionObserver();
        this.setupKeyboard();
        this.setupWheel();
        this.setupTouch();
        this.updateProgress();
    }
    createNavDots() {
        this.slides.forEach((_, i) => {
            const dot = document.createElement('button');
            dot.className = 'nav-dot' + (i === 0 ? ' active' : '');
            dot.setAttribute('aria-label', `Slide ${i + 1}`);
            dot.addEventListener('click', () => this.goTo(i));
            this.navDots.appendChild(dot);
        });
    }
    setupIntersectionObserver() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    const index = Array.from(this.slides).indexOf(entry.target);
                    if (index !== -1) {
                        this.currentSlide = index;
                        this.updateProgress();
                        this.updateDots();
                    }
                }
            });
        }, { threshold: 0.5 });
        this.slides.forEach(slide => observer.observe(slide));
    }
    setupKeyboard() {
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowDown' || e.key === 'ArrowRight' || e.key === ' ') {
                e.preventDefault(); this.next();
            } else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') {
                e.preventDefault(); this.prev();
            } else if (e.key === 'Home') {
                e.preventDefault(); this.goTo(0);
            } else if (e.key === 'End') {
                e.preventDefault(); this.goTo(this.slides.length - 1);
            }
        });
    }
    setupWheel() {
        let lastWheel = 0;
        document.addEventListener('wheel', (e) => {
            e.preventDefault();
            const now = Date.now();
            if (now - lastWheel < 800) return;
            lastWheel = now;
            const delta = Math.abs(e.deltaX) > Math.abs(e.deltaY) ? e.deltaX : e.deltaY;
            if (delta > 0) this.next();
            else if (delta < 0) this.prev();
        }, { passive: false });
    }
    setupTouch() {
        let startX = 0;
        document.addEventListener('touchstart', (e) => { startX = e.touches[0].clientX; }, { passive: true });
        document.addEventListener('touchend', (e) => {
            const diff = startX - e.changedTouches[0].clientX;
            if (Math.abs(diff) > 50) { if (diff > 0) this.next(); else this.prev(); }
        }, { passive: true });
    }
    goTo(index) {
        if (index >= 0 && index < this.slides.length) {
            this.slides[index].scrollIntoView({ behavior: 'smooth', inline: 'start', block: 'nearest' });
        }
    }
    next() { this.goTo(this.currentSlide + 1); }
    prev() { this.goTo(this.currentSlide - 1); }
    updateProgress() {
        const pct = ((this.currentSlide + 1) / this.slides.length) * 100;
        this.progressBar.style.width = pct + '%';
        this.slideCounter.textContent = `${this.currentSlide + 1} / ${this.slides.length}`;
    }
    updateDots() {
        const dots = this.navDots.querySelectorAll('.nav-dot');
        dots.forEach((d, i) => d.classList.toggle('active', i === this.currentSlide));
    }
}
document.addEventListener('DOMContentLoaded', () => new SlidePresentation());
</script>
JSEOF
  echo '</body>'
  echo '</html>'
} > "$DIR/$OUT"

echo "Built: slides/$OUT"
