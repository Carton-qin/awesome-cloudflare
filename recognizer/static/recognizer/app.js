(function () {
  const dropzone = document.getElementById("dropzone");
  const fileInput = document.querySelector("input[type='file']");
  const form = document.getElementById("upload-form");

  function submitFiles(files) {
    const dataTransfer = new DataTransfer();
    files.forEach((file) => dataTransfer.items.add(file));
    fileInput.files = dataTransfer.files;
    form.submit();
  }

  if (dropzone) {
    ["dragenter", "dragover"].forEach((eventName) => {
      dropzone.addEventListener(eventName, (e) => {
        e.preventDefault();
        e.stopPropagation();
        dropzone.classList.add("is-dragover");
      });
    });

    ["dragleave", "drop"].forEach((eventName) => {
      dropzone.addEventListener(eventName, (e) => {
        e.preventDefault();
        e.stopPropagation();
        dropzone.classList.remove("is-dragover");
      });
    });

    dropzone.addEventListener("drop", (e) => {
      const files = Array.from(e.dataTransfer.files).filter((f) => f.type.startsWith("image/"));
      if (files.length) submitFiles(files);
    });
  }

  document.addEventListener("paste", (e) => {
    const items = Array.from(e.clipboardData.items || []);
    const files = items
      .filter((item) => item.kind === "file")
      .map((item) => item.getAsFile())
      .filter(Boolean);
    if (files.length) submitFiles(files);
  });

  document.querySelectorAll("button[data-copy]").forEach((button) => {
    button.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(button.getAttribute("data-copy"));
        button.textContent = "已复制";
        setTimeout(() => (button.textContent = "复制"), 1200);
      } catch (err) {
        button.textContent = "失败";
        setTimeout(() => (button.textContent = "复制"), 1200);
      }
    });
  });
})();
