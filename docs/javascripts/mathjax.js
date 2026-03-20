window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
  },
};

document.addEventListener("DOMContentLoaded", function () {
  // Supporto per il cambio pagina istantaneo di Zensical
  if (typeof MathJax !== "undefined") {
    MathJax.typesetPromise();
  }
});
