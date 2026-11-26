/* Next Level Dodgers pop-up.
   Click a player to see their college photo next to their Madison
   (high school) photo.

   HOW TO ADD A HIGH SCHOOL PHOTO:
   Save it in  images/next-level/high-school/  using the SAME file name
   as the player's college photo. Example:
     college photo:      images/next-level/gui-dos-santos.jpg
     high school photo:  images/next-level/high-school/gui-dos-santos.jpg
   No code changes needed. If there's no high school photo yet, the
   pop-up shows "Photo coming soon". */
(function () {
  var PLACEHOLDER = "images/players/placeholder.png";

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  // build the pop-up once
  var dlg = document.createElement("dialog");
  dlg.className = "hof-dialog nl-dialog";
  dlg.setAttribute("aria-labelledby", "nl-name");
  dlg.innerHTML = '<button type="button" class="hof-close" aria-label="Close">&times;</button><div class="nl-body"></div>';
  document.body.appendChild(dlg);
  dlg.querySelector(".hof-close").addEventListener("click", function () { dlg.close(); });
  dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });

  function photoBox(src, label, fallbackText) {
    return '<figure class="nl-photo">' +
      '<div class="nl-frame"><img src="' + esc(src) + '" alt="' + esc(label) + '" ' +
      'onerror="this.onerror=null;this.src=\'' + PLACEHOLDER + '\';this.parentNode.classList.add(\'empty\');' +
      'this.parentNode.setAttribute(\'data-empty\',\'' + fallbackText + '\')"></div>' +
      "<figcaption>" + esc(label) + "</figcaption></figure>";
  }

  function open(fig) {
    var img = fig.querySelector("img");
    var src = img.getAttribute("src");
    var file = src.split("/").pop();
    var hs = fig.getAttribute("data-hs") || "images/next-level/high-school/" + file;
    var name = (fig.querySelector("figcaption strong") || {}).textContent || "";
    var college = (fig.querySelector("figcaption span") || {}).textContent || "";
    var section = fig.closest("section");
    var level = section && section.querySelector("h2") ? section.querySelector("h2").textContent : "";

    dlg.querySelector(".nl-body").innerHTML =
      '<div class="nl-head">' +
        '<p class="kicker">Next Level Dodgers' + (level ? " · " + esc(level) : "") + "</p>" +
        '<h2 id="nl-name">' + esc(name) + "</h2>" +
        (college ? '<p><span class="pill">' + esc(college) + "</span></p>" : "") +
      "</div>" +
      '<div class="nl-photos">' +
        photoBox(hs, "At Madison", "Photo coming soon") +
        photoBox(src, "In College", "Photo coming soon") +
      "</div>";
    if (dlg.showModal) dlg.showModal(); else dlg.setAttribute("open", "");
  }

  document.querySelectorAll(".gallery figure").forEach(function (fig) {
    fig.classList.add("nl-clickable");
    fig.setAttribute("tabindex", "0");
    fig.setAttribute("role", "button");
    var n = fig.querySelector("figcaption strong");
    if (n) fig.setAttribute("aria-label", "View " + n.textContent);
    fig.addEventListener("click", function () { open(fig); });
    fig.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); open(fig); }
    });
  });
})();
