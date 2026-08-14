async function loadComponent(selector, file) {
  const target = document.querySelector(selector);
  if (!target) return;

  try {
    const response = await fetch(file);
    if (!response.ok) throw new Error(`Não foi possível carregar ${file}`);
    target.innerHTML = await response.text();
  } catch (error) {
    console.error(error);
    target.setAttribute('hidden', '');
  }
}

document.addEventListener('DOMContentLoaded', () => {
  loadComponent('#header-placeholder', 'header.html');
  loadComponent('#footer-placeholder', 'footer.html');
});
