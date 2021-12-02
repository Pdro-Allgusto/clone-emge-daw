/* botão voltar para o topo */
  const backToTopButton = document.querySelector(".back-to-top");

  function backToTop() {
    if (this.window.scrollY >= 560) {
      backToTopButton.classList.add("show");
    } else {
      backToTopButton.classList.remove("show");
    }
  }

  /* When Scroll */
  window.addEventListener("scroll", function () {
    backToTop();
  });


