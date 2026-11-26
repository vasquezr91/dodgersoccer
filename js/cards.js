/* Builds the player cards for roster.html and hall-of-fame.html.
   You shouldn't need to edit this file: change js/roster-data.js
   or js/hof-data.js instead. */
(function () {
  var POS = {
    GK: "Goalkeepers", DF: "Defenders", MF: "Midfielders", W: "Wingers", ST: "Strikers", FW: "Forwards"
  };
  var POS_ONE = {
    GK: "Goalkeeper", DF: "Defender", MF: "Midfielder", W: "Winger", ST: "Striker", FW: "Forward"
  };
  var POS_ORDER = ["GK", "DF", "MF", "W", "ST", "FW"];
  var PLACEHOLDER = "images/players/placeholder.png";

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  function cardHTML(p, opts) {
    var last = String(p.last || "");
    var size = last.length > 11 ? " xlong" : last.length > 8 ? " long" : "";
    var photo = p.photo ? opts.folder + p.photo : PLACEHOLDER;
    var tag = opts.button ? "button" : "div";
    var extra = opts.button ? ' type="button" data-index="' + opts.index + '" aria-label="View ' + esc(p.first + " " + p.last) + '"' : "";
    return (
      "<" + tag + ' class="pcard"' + extra + ">" +
        '<img class="pcard-photo" src="' + esc(photo) + '" alt="" loading="lazy" onerror="this.onerror=null;this.src=\'' + PLACEHOLDER + '\'">' +
        '<span class="pcard-num">' + esc(opts.big) + "</span>" +
        '<span class="pcard-pos" title="' + esc(POS_ONE[p.position] || "") + '">' + esc(p.position || "") + "</span>" +
        '<span class="pcard-name"><span class="pcard-first">' + esc(p.first) + "</span>" +
        '<span class="pcard-last' + size + '">' + esc(last) + "</span></span>" +
        (opts.sub ? '<span class="pcard-sub">' + esc(opts.sub) + "</span>" : "") +
        '<span class="pcard-bar"></span>' +
      "</" + tag + ">"
    );
  }

  /* ---------------- ROSTER ---------------- */
  var rosterEl = document.getElementById("roster");
  if (rosterEl && window.ROSTER) {
    var levels = ["varsity", "jv", "freshmen"];
    var byId = [];   // varsity players, in the order their cards appear
    levels.forEach(function (lvl) {
      var panel = document.getElementById("level-" + lvl);
      var players = (window.ROSTER[lvl] || []).slice();
      if (!players.length) {
        panel.innerHTML = '<p class="lede">Roster coming soon.</p>';
        return;
      }
      var html = "";
      POS_ORDER.forEach(function (pos) {
        var group = players.filter(function (p) { return p.position === pos; })
          .sort(function (a, b) { return (a.number || 0) - (b.number || 0); });
        if (!group.length) return;
        html += '<section class="pos-group"><h2>' + POS[pos] + '</h2><div class="pcard-grid">' +
          group.map(function (p) {
            var sub = [p.grade, p.year ? "Class of " + p.year : ""].filter(Boolean).join(" · ");
            if (lvl === "varsity") {
              byId.push(p);
              return cardHTML(p, { folder: "images/players/", big: p.number, sub: sub, button: true, index: byId.length - 1 });
            }
            return cardHTML(p, { folder: "images/players/", big: p.number, sub: sub });
          }).join("") + "</div></section>";
      });
      panel.innerHTML = html;
    });

    var pdlg = document.getElementById("player-profile");
    if (pdlg) {
      document.getElementById("level-varsity").addEventListener("click", function (e) {
        var b = e.target.closest(".pcard");
        if (!b) return;
        var p = byId[+b.getAttribute("data-index")];
        var cfg = (window.ROSTER_STATS && window.ROSTER_STATS[p.position]) ||
          (p.position === "GK" ? [["saves", "Saves"], ["seasons", "Seasons"]]
                               : [["goals", "Goals"], ["assists", "Assists"], ["seasons", "Seasons"]]);
        var stats = cfg.map(function (c) { return [c[1], p[c[0]]]; });
        var photo = p.photo ? "images/players/" + p.photo : PLACEHOLDER;
        pdlg.querySelector(".hof-body").innerHTML =
          '<div class="hof-photo"><img src="' + esc(photo) + '" alt="' + esc(p.first + " " + p.last) +
            '" onerror="this.onerror=null;this.src=\'' + PLACEHOLDER + '\'"></div>' +
          '<div class="hof-info">' +
            '<p class="kicker">Varsity · #' + esc(p.number) + "</p>" +
            '<h2 id="player-name"><span>' + esc(p.first) + "</span> " + esc(p.last) + "</h2>" +
            '<p class="hof-meta"><span class="pill">' + esc(POS_ONE[p.position] || p.position || "") + "</span>" +
            (p.grade ? ' <span class="pill pill-light">' + esc(p.grade) + "</span>" : "") + "</p>" +
            "<h3>Graduation Year</h3>" +
            '<p class="grad-year">Class of ' + esc(p.year || "—") + "</p>" +
            "<h3>Statistics</h3>" +
            '<div class="stat-row">' + stats.map(function (st) {
              var v = (st[1] === undefined || st[1] === "") ? "—" : st[1];
              return '<div class="stat"><strong>' + esc(v) + "</strong><span>" + esc(st[0]) + "</span></div>";
            }).join("") + "</div>" +
          "</div>";
        if (pdlg.showModal) pdlg.showModal(); else pdlg.setAttribute("open", "");
      });
      pdlg.querySelector(".hof-close").addEventListener("click", function () { pdlg.close(); });
      pdlg.addEventListener("click", function (e) { if (e.target === pdlg) pdlg.close(); });
    }

    var tabs = rosterEl.querySelectorAll('[role="tab"]');
    function show(lvl, push) {
      tabs.forEach(function (t) {
        var on = t.getAttribute("data-level") === lvl;
        t.setAttribute("aria-selected", on);
        t.tabIndex = on ? 0 : -1;
        document.getElementById("level-" + t.getAttribute("data-level")).hidden = !on;
      });
      if (push) history.replaceState(null, "", "#" + lvl);
    }
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { show(t.getAttribute("data-level"), true); });
      t.addEventListener("keydown", function (e) {
        var d = e.key === "ArrowRight" ? 1 : e.key === "ArrowLeft" ? -1 : 0;
        if (!d) return;
        var next = tabs[(i + d + tabs.length) % tabs.length];
        next.focus(); next.click();
      });
    });
    var start = location.hash.replace("#", "");
    show(levels.indexOf(start) > -1 ? start : "varsity", false);
  }

  /* ---------------- HALL OF FAME ---------------- */
  var hofEl = document.getElementById("hof-grid");
  if (hofEl && window.HALL_OF_FAME) {
    var list = window.HALL_OF_FAME.slice().sort(function (a, b) {
      return String(b.year).localeCompare(String(a.year));
    });
    hofEl.innerHTML = list.map(function (p, i) {
      return cardHTML(p, {
        folder: "images/players/", big: "'" + String(p.year).slice(-2),
        sub: "Class of " + p.year, button: true, index: i
      });
    }).join("");

    var dlg = document.getElementById("hof-profile");
    function li(items) {
      return (items && items.length)
        ? "<ul>" + items.map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("") + "</ul>"
        : '<p class="muted">None listed</p>';
    }
    function open(i) {
      var p = list[i];
      var photo = p.photo ? "images/players/" + p.photo : PLACEHOLDER;
      dlg.querySelector(".hof-body").innerHTML =
        '<div class="hof-photo"><img src="' + esc(photo) + '" alt="' + esc(p.first + " " + p.last) +
          '" onerror="this.onerror=null;this.src=\'' + PLACEHOLDER + '\'"></div>' +
        '<div class="hof-info">' +
          '<p class="kicker">Hall of Fame · Class of ' + esc(p.year) + "</p>" +
          '<h2 id="hof-name"><span>' + esc(p.first) + "</span> " + esc(p.last) + "</h2>" +
          '<p class="hof-meta"><span class="pill">' + esc(POS_ONE[p.position] || p.position || "") + "</span></p>" +
          "<h3>Statistics</h3>" +
          '<div class="stat-row">' + (p.stats || []).map(function (s) {
            return '<div class="stat"><strong>' + esc(s[1]) + "</strong><span>" + esc(s[0]) + "</span></div>";
          }).join("") + "</div>" +
          '<div class="hof-cols"><div><h3>Accolades</h3>' + li(p.accolades) + "</div>" +
          "<div><h3>Independent Awards</h3>" + li(p.awards) + "</div></div>" +
        "</div>";
      if (dlg.showModal) dlg.showModal(); else dlg.setAttribute("open", "");
    }
    hofEl.addEventListener("click", function (e) {
      var b = e.target.closest(".pcard");
      if (b) open(+b.getAttribute("data-index"));
    });
    dlg.querySelector(".hof-close").addEventListener("click", function () { dlg.close(); });
    dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });
  }
})();
