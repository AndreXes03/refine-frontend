(() => {
  const params = new URLSearchParams(location.search);
  const variant = params.get("variant") === "before" ? "before" : "after";
  document.documentElement.dataset.variant = variant;

  const note = document.querySelector("[data-variant-label]");
  if (note) note.textContent = variant;

  const toast = document.querySelector(".toast");
  let timer;
  function announce(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add("visible");
    clearTimeout(timer);
    timer = setTimeout(() => toast.classList.remove("visible"), 1600);
  }

  document.querySelectorAll("[data-action]").forEach((control) => {
    control.addEventListener("click", () => announce(control.dataset.message || "Action completed"));
  });

  document.querySelectorAll("[data-tab]").forEach((control) => {
    control.addEventListener("click", () => {
      control.parentElement.querySelectorAll("[data-tab]").forEach((item) => item.classList.remove("active"));
      control.classList.add("active");
      announce(`${control.textContent.trim()} selected`);
    });
  });

  const search = document.querySelector("[data-table-search]");
  if (search) {
    search.addEventListener("input", () => {
      const query = search.value.trim().toLowerCase();
      document.querySelectorAll("tbody tr").forEach((row) => {
        row.hidden = query !== "" && !row.textContent.toLowerCase().includes(query);
      });
    });
  }
})();
