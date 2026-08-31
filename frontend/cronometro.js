// Contador pro dia 26 de outubro
(function(){
  function getTarget(){
    const now = new Date();
    let year = now.getFullYear();
    // Mês é index = 0: 9 = October
    let target = new Date(year, 9, 26, 0, 0, 0, 0);
    if (target <= now) target = new Date(year + 1, 9, 26, 0, 0, 0, 0);
    return target;
  }

  const el = document.getElementById('countdown');
  if (!el) return;

  function update(){
    const now = new Date();
    const diff = getTarget() - now;
    if (diff <= 0){
      el.textContent = '00d 00:00:00';
      clearInterval(interval);
      return;
    }
    let s = Math.floor(diff / 1000);
    const days = Math.floor(s / 86400); s %= 86400;
    const hours = Math.floor(s / 3600); s %= 3600;
    const minutes = Math.floor(s / 60);
    const seconds = s % 60;
    el.textContent = days + 'd ' + String(hours).padStart(2,'0') + 'h ' + String(minutes).padStart(2,'0') + 'm ' + String(seconds).padStart(2,'0') + 's';
  }

  update();
  const interval = setInterval(update, 1000);
})();