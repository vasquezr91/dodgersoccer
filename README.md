# Dodger Soccer website (dodgersoccer.com)

Plain HTML/CSS/JS, no Weebly, no build tools needed. Open `index.html` in a browser to preview.

## 1. Files still needed

All logos, coach photos, the team photo, sponsor logos and the highlight video are already in place.
Still missing (save into the `docs/` folder with these exact names):

| Save as | Download from |
|---|---|
| `fall_athletics_registration.pdf` | https://www.dodgersoccer.com/uploads/4/4/8/3/44832113/fall_athletics___marching_band_registration.pdf |
| `meal_plan.pdf` | https://www.dodgersoccer.com/uploads/4/4/8/3/44832113/meal_plan.pdf |
| `pre-summer_workouts.pdf` | https://www.dodgersoccer.com/uploads/4/4/8/3/44832113/pre-summer_workouts.pdf |

Optional: a photo for Michael Moore saved as `images/michael-moore.jpg` (his card shows initials until then — tell Claude and it will hook it up).

## 2. Editing content

Every page is a normal `.html` file. Open in any text editor (VS Code is free) and change the text.

* **Colors:** top of `css/style.css` (`--maroon`, `--gold`). Change them to match your logo.
* **Next Level Dodgers:** in `next-level-dodgers.html`, copy a `<figure>…</figure>` block for each player and edit the photo name and caption.
* **Calendar:** the schedule page embeds your existing Google Calendar, so keep updating events in Google Calendar as you do now.
* **Menu, banner, sponsors, footer** appear on every page. To change them everywhere at once, edit `build.py` and run `python3 build.py`, or edit each HTML file by hand.

## 3. Hosting (free options)

* **Netlify** (easiest): netlify.com → "Add new site" → "Deploy manually" → drag this whole folder onto the page.
* **Cloudflare Pages** or **GitHub Pages** also work and are free.

Then point your domain at it: in your domain registrar (or Weebly's domain settings if you bought the domain through Weebly), follow the host's "add custom domain" instructions. If the domain is registered through Weebly/Square, transfer it to a registrar like Cloudflare or Namecheap before closing the Weebly account.

## Old Weebly URLs

Some page names changed slightly. To keep old links working, add redirects on your host (Netlify: the included `_redirects` file handles this).
