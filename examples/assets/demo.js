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

  const search = document.querySelector("[data-list-search]");
  if (search) {
    search.addEventListener("input", () => {
      const query = search.value.trim().toLowerCase();
      document.querySelectorAll("[data-search-item]").forEach((item) => {
        item.hidden = query !== "" && !item.textContent.toLowerCase().includes(query);
      });
    });
  }

  const workspaceName = document.querySelector("[data-workspace-name]");
  const workspaceSlug = document.querySelector("[data-workspace-slug]");
  const previewName = document.querySelector("[data-preview-name]");
  const previewSlug = document.querySelector("[data-preview-slug]");
  if (workspaceName && previewName) {
    workspaceName.addEventListener("input", () => {
      previewName.textContent = workspaceName.value.trim() || "Untitled workspace";
    });
  }
  if (workspaceSlug && previewSlug) {
    workspaceSlug.addEventListener("input", () => {
      const slug = workspaceSlug.value.trim() || "workspace";
      previewSlug.textContent = `orbit.so/${slug}`;
    });
  }
})();
