"""Generates the static dodgersoccer.com site into ../dodgersoccer/"""
import os, html

OUT = os.path.join(os.path.dirname(__file__), "..", "dodgersoccer")
os.makedirs(os.path.join(OUT, "images"), exist_ok=True)
os.makedirs(os.path.join(OUT, "docs"), exist_ok=True)

NAV = [
    ("Home", "index.html", None),
    ("Schedule", "calendar.html", None),
    ("Coaches", "coaches.html", None),
    ("Honors", None, [("National Recognition", "national-recognition.html"),
                      ("All-State", "all-state.html"),
                      ("All-County", "all-county.html")]),
    ("Records", None, [("Season Records", "season-records.html"),
                       ("All-Time List", "all-time-list.html")]),
    ("Next Level Dodgers", "next-level-dodgers.html", None),
    ("Workouts / Nutrition", "workouts-nutrition.html", None),
    ("Forms", "forms.html", None),
]

SPONSORS = [
    ("msc-50th.png", "Madison Soccer Club 50th Anniversary"),
    ("madison-honda.jpg", "Madison Honda"),
    ("hlw.png", "HLW"),
    ("bagel-nosh.jpg", "Bagel Nosh Madison"),
    ("newsmile-orthodontics.jpg", "Newsmile Orthodontics, Michael Castagna DDS"),
    ("montclair-ucc.jpg", "Montclair Upper Cervical Chiropractic"),
]


def nav_html(current):
    items = []
    for label, href, children in NAV:
        if children:
            active = any(c[1] == current for c in children)
            sub = "".join(
                f'<li><a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{html.escape(l)}</a></li>'
                for l, h in children)
            items.append(
                f'<li class="has-sub{" active" if active else ""}">'
                f'<button type="button" class="sub-toggle" aria-expanded="false">{label} <span aria-hidden="true">▾</span></button>'
                f'<ul class="sub">{sub}</ul></li>')
        else:
            cur = ' aria-current="page"' if href == current else ""
            items.append(f'<li><a href="{href}"{cur}>{html.escape(label)}</a></li>')
    return "\n".join(items)


def page(filename, title, body, wide=False):
    sponsors = "".join(
        f'<li><img src="images/{f}" alt="{html.escape(a)}" loading="lazy"></li>' for f, a in SPONSORS)
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} | Dodger Soccer</title>
<meta name="description" content="Madison High School Dodgers boys soccer — schedules, coaches, honors, records and forms.">
<meta property="og:title" content="Dodger Soccer">
<meta property="og:image" content="images/logo.png">
<link rel="icon" href="images/logo.png">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="index.html">
      <img src="images/logo.png" alt="" width="56" height="56">
      <span>DODGER SOCCER</span>
    </a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav id="site-nav" aria-label="Main">
      <ul class="nav">
{nav_html(filename)}
      </ul>
    </nav>
  </div>
</header>

<section class="banner">
  <div class="wrap banner-inner">
    <div class="poy">
      <p class="kicker">2024 Morris County</p>
      <p>Team of the Year · Player of the Year · Coach of the Year</p>
      <a href="https://highschoolsports.nj.com/school/madison-madison/boyssoccer" target="_blank" rel="noopener">NJ.com Profile →</a>
    </div>
    <dl class="titles">
      <div><dt>Group II State Champions</dt><dd>'89 · '94 · '96 · '25</dd></div>
      <div><dt>Sectional Champions</dt><dd>'89 · '94 · '96 · '25</dd></div>
      <div><dt>County Champions</dt><dd>'09</dd></div>
      <div><dt>NJAC Conference Champions</dt><dd>'82 · '83 · '84 · '95 · '18 · '20 · '24 · '25 · '26</dd></div>
    </dl>
  </div>
</section>

<main id="main" class="wrap{' wide' if wide else ''}">
<h1>{html.escape(title)}</h1>
{body}
</main>

<section class="sponsors">
  <div class="wrap">
    <h2>Thank you to our Sponsors</h2>
    <ul class="sponsor-list">{sponsors}</ul>
  </div>
</section>

<footer class="site-footer">
  <div class="wrap footer-inner">
    <p><strong>Madison Dodgers Boys Soccer</strong><br>
    <a href="mailto:dodgersoccermhs@gmail.com">dodgersoccermhs@gmail.com</a></p>
    <ul class="social">
      <li><a href="https://www.instagram.com/dodger_soccer/" target="_blank" rel="noopener">Instagram</a></li>
      <li><a href="https://twitter.com/coachvasquezMHS" target="_blank" rel="noopener">X / Twitter</a></li>
      <li><a href="https://www.facebook.com/groups/1421674364746656" target="_blank" rel="noopener">Facebook</a></li>
    </ul>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
"""
    with open(os.path.join(OUT, filename), "w") as f:
        f.write(doc)


def honors_table(data):
    """data: list of (year, [(name, honor), ...])"""
    out = []
    for year, rows in data:
        lis = "".join(f"<tr><td>{html.escape(n)}</td><td>{html.escape(h)}</td></tr>" for n, h in rows)
        out.append(f'<section class="card"><h2>{year}</h2><table class="list"><thead><tr><th>Player</th><th>Honor</th></tr></thead><tbody>{lis}</tbody></table></section>')
    return f'<div class="grid">{"".join(out)}</div>'


def leaders(title, rows):
    lis = "".join(f'<tr><td class="rank">{r}</td><td>{html.escape(n)}</td><td class="yr">{y}</td><td class="num">{v}</td></tr>'
                  for r, n, y, v in rows)
    return f'<section class="card"><h2>{title}</h2><table class="list"><thead><tr><th>#</th><th>Player</th><th>Class</th><th class="num">Total</th></tr></thead><tbody>{lis}</tbody></table></section>'


# ---------------- HOME ----------------
page("index.html", "Home", """<style>main > h1{display:none}</style>
<div class="hero">
  <img src="images/hero.jpg" alt="Dodger Soccer team celebrating the 2025 NJSIAA Group II State Championship" onerror="this.parentElement.classList.add('no-img'); this.remove();">
  <div class="hero-text">
    <p class="kicker">Madison High School</p>
    <p class="hero-title">Boys Soccer</p>
    <p>2025 Group II State Champions · 2025 Sectional Champions · 2026 NJAC Champions</p>
  </div>
</div>
<div class="quick">
  <a href="calendar.html"><strong>Schedule</strong><span>Practices, games &amp; key dates</span></a>
  <a href="coaches.html"><strong>Coaches</strong><span>Meet the staff</span></a>
  <a href="all-time-list.html"><strong>Records</strong><span>Program leaders</span></a>
  <a href="forms.html"><strong>Forms</strong><span>Registration &amp; paperwork</span></a>
</div>
<section class="highlights">
  <div class="hl-text">
    <p class="kicker">Dodgers in Action</p>
    <h2>Season Highlights</h2>
    <p>Training, game days and the run to the 2025 Group II State Championship. Press play to watch.</p>
    <a class="btn" href="https://www.instagram.com/dodger_soccer/" target="_blank" rel="noopener">More on Instagram</a>
  </div>
  <video class="hl-video" controls playsinline preload="none" poster="media/highlights-poster.jpg">
    <source src="media/highlights.mp4" type="video/mp4">
    Your browser can't play this video.
  </video>
</section>
""")

# ---------------- CALENDAR ----------------
import base64, urllib.parse
CAL_IDS = ["4fqsqu5v8e2p09qrqoeelms5o0@group.calendar.google.com",
           "7886mn4a35ucver8up2a4503nuvd9ndv@import.calendar.google.com",
           "en.usa#holiday@group.v.calendar.google.com"]
CAL = ("https://calendar.google.com/calendar/embed?height=700&wkst=1&ctz=America%2FNew_York&showPrint=0"
       + "".join("&src=" + base64.b64encode(c.encode()).decode().rstrip("=") for c in CAL_IDS)
       + "&color=%23ad1457&color=%23ad1457&color=%230b8043")
page("calendar.html", "Schedule", f"""
<section class="card dates">
  <h2>2025 Important Dates</h2>
  <ul>
    <li><strong>June 16</strong> Summer practices start (Mon–Thurs, 8–10 AM)</li>
    <li><strong>July 14</strong> Registration &amp; physicals due</li>
    <li><strong>July 19–26</strong> Summer blackout week</li>
    <li><strong>Aug 17–19</strong> Official tryouts (Mon–Wed, 8–11 AM)</li>
    <li><strong>Aug 25</strong> First scrimmage</li>
    <li><strong>Sept 1</strong> Season opens</li>
  </ul>
</section>
<div class="cal-wrap">
  <iframe src="{CAL}" title="Dodger Soccer calendar" loading="lazy"></iframe>
</div>
""", wide=True)

# ---------------- COACHES ----------------
coaches = [
    ("Rich Vasquez", "Head Varsity Coach", "rich-vasquez.jpg"),
    ("Matt Murphy", "Assistant Varsity Coach", "matt-murphy.jpg"),
    ("Tanner Lambeseder", "Head JV Coach", "tanner-lambeseder.jpg"),
    ("Peter Carroll", "Head Freshmen Coach", "peter-carroll.jpg"),
    ("Jeff Scott", "Goalie Coach", "jeff-scott.jpg"),
    ("Michael Moore", "Athletic Trainer", "michael-moore.jpg"),
]
cc = ""
for n, t, img in coaches:
    initials = "".join(p[0] for p in n.split())
    pic = (f'<img src="images/{img}" alt="{n}" loading="lazy" onerror="this.replaceWith(Object.assign(document.createElement(\'span\'),{{className:\'initials\',textContent:\'{initials}\'}}))">'
           if img else f'<span class="initials">{initials}</span>')
    cc += f'<li class="coach">{pic}<h3>{n}</h3><p>{t}</p></li>'
page("coaches.html", "Coaches", f"""
<section class="card awards">
  <img src="images/coaches.jpg" alt="Dodger Soccer coaching staff" loading="lazy" "coaches.jpeg">
  <div>
    <h2>Coaching Honors</h2>
    <ul>
      <li>2026 NJSIAA Boys Soccer Coach of the Year</li>
      <li>2025 USC New Jersey Small School Coach of the Year</li>
      <li>2024 &amp; 2025 NJ.com NJAC Coach of the Year</li>
      <li>2024 Morris County Coach of the Year</li>
    </ul>
  </div>
</section>
<ul class="coaches">{cc}</ul>
""")

# ---------------- HONORS ----------------
page("all-region-all-american.html", "All Region / All American", """
<section class="card feature">
  <img src="images/matthew-munoz.jpg" alt="Matthew Munoz" loading="lazy" onerror="this.remove()">
  <div>
    <h2>2024</h2>
    <ul>
      <li>Morris County Team of the Year</li>
      <li>Morris County Player of the Year</li>
      <li>Morris County Coach of the Year</li>
    </ul>
  </div>
</section>
""")

page("all-state.html", "All-State", honors_table([
    ("2025", [("Matthew Munoz", "All-State 1st Team; North II Sectional Player of the Year"),
              ("Matthew Munoz", "All Group 2 — 1st Team"),
              ("Guilherme Dos Santos", "All Group 2 — 3rd Team"),
              ("Matthew Munoz", "North II — 1st Team"),
              ("Guilherme Dos Santos", "North II — 1st Team"),
              ("Santiago Rodriguez", "North II — 2nd Team"),
              ("Callum Regan", "North II — 3rd Team")]),
    ("2024", [("Matthew Munoz", "All-State 1st Team; North II Sectional Player of the Year"),
              ("Matthew Munoz", "All Group 2 — 1st Team"),
              ("Guilherme Dos Santos", "All Group 2 — 3rd Team"),
              ("Matthew Munoz", "North II — 1st Team"),
              ("Guilherme Dos Santos", "North II — 1st Team"),
              ("Santiago Rodriguez", "North II — 2nd Team"),
              ("Callum Regan", "North II — 3rd Team")]),
    ("2023", [("Matthew Munoz", "North II All-State")]),
    ("2020", [("Juan Angel Agudelo", "North II All-State")]),
    ("2019", [("Brandom Ocampo", "3rd Team")]),
    ("2018", [("Lucas DiGiacomo", "1st Team"), ("Brendan Mulcahy", "3rd Team"),
              ("Brandom Ocampo", "Honorable Mention"), ("Brendan Armstrong", "Honorable Mention")]),
    ("2017", [("Lucas DiGiacomo", "Honorable Mention")]),
]))

ac = {
    "2025": [("Justin Macrina", "1st"), ("Andrew Haviland", "1st"), ("Gui Dos Santos", "2nd"), ("Nolan Keane", "3rd"),
             ("Cal Regan", "3rd"), ("Liam Goldberg", "HM"), ("Jake Witte", "HM")],
    "2024": [("Matthew Munoz", "1st — Morris County Player of the Year"), ("Santiago Rodriguez", "1st"),
             ("Gui Dos Santos", "1st"), ("Cal Regan", "2nd"), ("JD Aritzabal", "HM"), ("Scott Sullivan", "HM")],
    "2023": [("Matthew Munoz", "3rd"), ("Gui Dos Santos", "HM"), ("Kyle Piechnik", "HM")],
    "2022": [("Matt Salazar", "3rd"), ("Eric Selquist", "HM"), ("Ruari Callaghan", "HM")],
    "2021": [("Eric Selquist", "HM"), ("Juan Cadavid", "HM")],
    "2020": [("Juan Angel", "1st"), ("Matthias Hendrickson", "2nd"), ("Christian Williams", "HM"), ("Owen Eilander", "HM")],
    "2019": [("Brandom Ocampo", "2nd"), ("Brendan Armstrong", "HM"), ("Matt Beneventano", "HM")],
    "2018": [("Lucas DiGiacomo", "1st"), ("Brendan Mulcahy", "1st"), ("Brandom Ocampo", "2nd"),
             ("Brendan Armstrong", "2nd"), ("Jack Flanagan", "HM"), ("Matt Beneventano", "HM")],
    "2017": [("Lucas DiGiacomo", "3rd"), ("Brendan Armstrong", "HM"), ("Matt Warshaw", "HM")],
    "2016": [("JP Scheunke", "2nd"), ("Tim Azzollini", "3rd")],
    "2014": [("Jonathan Miller", "2nd"), ("Tim Azzollini", "2nd"), ("Cole Crescas", "3rd"), ("Michael Noto", "3rd")],
    "2013": [("Yorme Cosme", "2nd"), ("Cole Crescas", "2nd"), ("Reid Collins", "2nd")],
    "2012": [("Anton Benedikt", "2nd"), ("Raz Lesham", "3rd")],
    "2011": [("Matt Gilbert", "1st"), ("Vincent Bennett", "2nd"), ("Peter Willis", "3rd")],
    "2010": [("Matt Gilbert", "1st"), ("Danny Giraldo", "2nd"), ("Jorge Hoyos", "3rd")],
    "2009": [("Jonathon Aguirre", "1st"), ("Matt Gilbert", "1st"), ("Doug Willis", "1st"), ("Forrest Benfors", "3rd")],
}
page("all-county.html", "All-County", '<p class="lede">Team: 1st, 2nd, 3rd, or HM (Honorable Mention).</p>' + honors_table(list(ac.items())))

# ---------------- RECORDS ----------------
page("season-records.html", "Season Records", """
<table class="list records">
<thead><tr><th>Record</th><th class="num">Mark</th><th>Season</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Best record</td><td class="num">20-1-2</td><td>Fall 2025</td><td>Undefeated in conference play</td></tr>
<tr><td>Most team goals</td><td class="num">68</td><td>Fall 2024</td><td></td></tr>
<tr><td>Most individual goals</td><td class="num">22</td><td>2026</td><td>Grayson Gorski</td></tr>
<tr><td>Most team assists</td><td class="num">53</td><td>Fall 2024</td><td></td></tr>
<tr><td>Most individual assists</td><td class="num">14</td><td>2024 / 2018</td><td>Gui Dos Santos (2024), Lucas DiGiacomo (2018)</td></tr>
<tr><td>Most saves</td><td class="num">157</td><td>2018</td><td>Brendan Armstrong</td></tr>
<tr><td>Most shutouts</td><td class="num">11</td><td>2025</td><td>Callum Regan</td></tr>
<tr><td>Fewest goals against</td><td class="num">17</td><td>Fall 2025</td><td></td></tr>
</tbody></table>
""")

page("all-time-list.html", "All-Time List", '<div class="grid">' + "".join([
    leaders("Goals", [(1, "Lucas DiGiacomo", "'19", 36), (2, "Matt Munoz", "'25", 35), (3, "Gui Dos Santos", "'26", 33),
                      (4, "Jonathan Miller", "'15", 29), (5, "Grayson Gorski", "'29", 26), (6, "Vincent Bennett", "'12", 24),
                      (7, "Brendan Mulcahy", "'19", 23), (7, "Justin Macrina", "'25", 23), (9, "Brandom Ocampo", "'20", 18),
                      (10, "Matt Jackson", "'16", 14)]),
    leaders("Assists", [(1, "Lucas DiGiacomo", "'19", 34), (2, "Gui Dos Santos", "'26", 27), (3, "Matthew Munoz", "'25", 17),
                        (3, "Santiago Rodriguez", "'25", 17), (5, "Brendan Mulcahy", "'19", 14), (6, "Andrew Haviland", "'26", 13),
                        (7, "Liam Goldberg", "'26", 13), (8, "Schuyler Fuchsman", "'16", 11), (9, "Ben Smith", "'28", 9),
                        (9, "Jonathan Miller", "'15", 9)]),
    leaders("Saves", [(1, "Brendan Armstrong", "'20", 387), (2, "Cal Regan", "'26", 196), (3, "Matt Gilbert", "'12", 180),
                      (4, "Ruari Callaghan", "'23", 159), (5, "Sean Tully", "'22", 89), (6, "Mike Noto", "'16", 82),
                      (7, "Reid Collins", "'14", 81), (8, "Sebastian Villarevia", "'27", 46)]),
    leaders("Shutouts", [(1, "Matt Gilbert", "'12", 32), (2, "Cal Regan", "'26", 19), (3, "Brendan Armstrong", "'20", 17),
                         (4, "Reid Collins", "'14", 11), (5, "Sebastian Villarevia", "'27", 10), (5, "Mike Noto", "'16", 10),
                         (7, "Ruari Callaghan", "'23", 9), (8, "Sean Tully", "'22", 6)]),
]) + "</div>")

# ---------------- NEXT LEVEL ----------------
# Each player: (photo file in images/next-level/, name line, college line)
# Sections with no photos yet are hidden automatically.
def gallery(title, items):
    items = [i for i in items if os.path.exists(os.path.join(OUT, "images", "next-level", i[0]))]
    if not items:
        return ""
    figs = "".join(
        f'<figure><img src="images/next-level/{f}" alt="{html.escape(n)}" loading="lazy">'
        f'<figcaption><strong>{html.escape(n)}</strong><span>{html.escape(c)}</span></figcaption></figure>'
        for f, n, c in items)
    return f'<section><h2>{title}</h2><div class="gallery">{figs}</div></section>'

D1 = [
    ("gui-dos-santos.jpg", "Gui Dos Santos '26", "Seton Hall University '30"),
    ("schuyler-fuchsman.jpg", "Schuyler Fuchsman '16", "Boston University '20"),
    ("matt-gilbert.jpg", "Matt Gilbert '12", "Boston University '17"),
    ("jonathon-aguirre.jpg", "Jonathon Aguirre '09", "Duke '13"),
]
D3 = [
    ("mm.jpg", "Matthew Munoz '25", "Drew University"),
    ("jd.jpg", "JD Aritzabal '25", "FDU"),
    ("brandom-ocampo.jpg", "Brandom Ocampo '20", "Drew University '24"),
    ("lucas-digiacomo.jpg", "Lucas DiGiacomo '19", "Gettysburg '23"),
    ("juan-pineda.jpg", "Juan Pineda '22", "FDU '25"),
    ("christian-williams.jpg", "Christian Williams '21", "Susquehanna University '25"),
    ("matt-warshaw.jpg", "Matt Warshaw '18", "FDU '22"),
    ("anton-benedikt.jpg", "Anton Benedikt '13", "Penn State Behrend '17"),
    ("daniel-giraldo.jpg", "Daniel Giraldo '12", "Drew University '17"),
    ("vincent-bennett.jpg", "Vincent Bennett '12", "RPI '17"),
    ("jackson-hurst.jpg", "Jackson Hurst '11", "Drew University '15"),
    ("enzo-martirano.jpg", "Enzo Martirano '09", "William Paterson '17"),
    ("nico-martirano.jpg", "Nico Martirano '09", "William Paterson '16"),
    ("kevin-reinhardt.jpg", "Kevin Reinhardt '09", "Montclair State '13"),
    ("tanner-lambeseder.jpg", "Tanner Lambeseder '09", "SCAD '13"),
]
CLUB = []

page("next-level-dodgers.html", "Next Level Dodgers",
     '<p class="lede">Dodgers who went on to play college soccer.</p>'
     + gallery("NCAA Division I", D1) + gallery("NCAA Division III", D3) + gallery("NCAA Club", CLUB))

# ---------------- WORKOUTS ----------------
page("workouts-nutrition.html", "Workouts / Nutrition", """
<div class="grid">
  <section class="card doc">
    <h2>Meal Plan</h2>
    <object data="docs/meal_plan.pdf" type="application/pdf"><p>Your browser can't show this PDF.</p></object>
    <a class="btn" href="docs/meal_plan.pdf" download>Download Meal Plan (PDF)</a>
  </section>
  <section class="card doc">
    <h2>Independent Workouts</h2>
    <object data="docs/pre-summer_workouts.pdf" type="application/pdf"><p>Your browser can't show this PDF.</p></object>
    <a class="btn" href="docs/pre-summer_workouts.pdf" download>Download Workouts (PDF)</a>
  </section>
</div>
""", wide=True)

# ---------------- FORMS ----------------
page("forms.html", "Forms", """
<section class="card doc">
  <h2>Fall 2025 Athletic Registration</h2>
  <p>Please complete the registration packet from the MHS Admin Team.</p>
  <ul class="inline-dates">
    <li><strong>Aug 18</strong> First official practice</li>
    <li><strong>Sept 4</strong> First competition</li>
    <li><strong>Nov 21</strong> Season ends</li>
  </ul>
  <object data="docs/fall_athletics_registration.pdf" type="application/pdf"><p>Your browser can't show this PDF.</p></object>
  <a class="btn" href="docs/fall_athletics_registration.pdf" download>Download Registration Packet (PDF)</a>
</section>
""", wide=True)

print("done")
