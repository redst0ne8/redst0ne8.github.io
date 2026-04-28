// ─────────────────────────────────────────────
//  CONFIGURATION — edit these two values only
// ─────────────────────────────────────────────
const BACKEND_PIN      = "69420";          // Change to your desired PIN (any length)
const BACKEND_REDIRECT = "https://backend.redst0ne8.site/index"; // Change to your backend URL
// ─────────────────────────────────────────────

let entered = "";

function openModal() {
  entered = "";
  updateDots();
  document.getElementById("modalOverlay").classList.add("open");
  clearError();
}

function closeModal() {
  document.getElementById("modalOverlay").classList.remove("open");
  entered = "";
  updateDots();
  clearError();
}

function pressKey(key) {
  if (key === "del") {
    entered = entered.slice(0, -1);
    updateDots();
    clearError();
    return;
  }
  if (key === "enter") {
    checkPin();
    return;
  }
  if (entered.length >= BACKEND_PIN.length) return;
  entered += key;
  updateDots();
  if (entered.length === BACKEND_PIN.length) {
    setTimeout(checkPin, 80); // slight delay so last dot fills visually
  }
}

function updateDots() {
  for (let i = 0; i < BACKEND_PIN.length; i++) {
    const dot = document.getElementById("d" + i);
    if (!dot) continue;
    dot.classList.toggle("filled", i < entered.length);
  }
}

function checkPin() {
  if (entered === BACKEND_PIN) {
    window.location.href = BACKEND_REDIRECT;
  } else {
    showError();
    shakeDots();
    entered = "";
    setTimeout(() => { updateDots(); }, 500);
  }
}

function showError() {
  document.getElementById("pinError").classList.add("show");
}

function clearError() {
  document.getElementById("pinError").classList.remove("show");
}

function shakeDots() {
  const dots = document.getElementById("pinDots");
  dots.style.transition = "transform 0.05s";
  const seq = [8, -8, 6, -6, 4, -4, 0];
  let i = 0;
  const step = () => {
    if (i >= seq.length) { dots.style.transform = ""; return; }
    dots.style.transform = `translateX(${seq[i++]}px)`;
    setTimeout(step, 50);
  };
  step();
}

// Allow keyboard input
document.addEventListener("keydown", (e) => {
  if (!document.getElementById("modalOverlay").classList.contains("open")) return;
  if (e.key === "Escape") { closeModal(); return; }
  if (e.key === "Backspace") { pressKey("del"); return; }
  if (e.key === "Enter") { pressKey("enter"); return; }
  if (/^\d$/.test(e.key)) { pressKey(e.key); }
});

// Click outside modal to close
document.getElementById("modalOverlay").addEventListener("click", (e) => {
  if (e.target === e.currentTarget) closeModal();
});

// Build dots dynamically based on PIN length
(function buildDots() {
  const container = document.getElementById("pinDots");
  container.innerHTML = "";
  for (let i = 0; i < BACKEND_PIN.length; i++) {
    const dot = document.createElement("div");
    dot.className = "pin-dot";
    dot.id = "d" + i;
    container.appendChild(dot);
  }
})();
