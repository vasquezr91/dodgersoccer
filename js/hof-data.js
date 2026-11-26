/* =====================================================================
   DODGER SOCCER HALL OF FAME
   ---------------------------------------------------------------------
   Each { ... }, block is one Hall of Famer. Copy a whole block to add
   another; delete a block to remove one.

   first, last : name
   year        : high school graduation year, e.g. "2019"
   position    : GK, DF, MF, W (winger) or ST (striker)
   photo       : file name in the images/players/ folder
                 ("" shows the placeholder silhouette)
   stats       : as many as you like, each written as  ["Label", "Number"]
   accolades   : honors earned as a Dodger (All-State, All-County, records...)
   awards      : independent awards (national, college, club, community...)

   Players appear newest graduation year first.
   ===================================================================== */

window.HALL_OF_FAME = [

  {
    first: "First", last: "Last", year: "2019", position: "MF", photo: "",
    stats: [ ["Goals", "0"], ["Assists", "0"], ["Seasons", "4"] ],
    accolades: [
      "All-State 1st Team (Year)",
      "All-County 1st Team (Year)",
    ],
    awards: [
      "Independent award (Year)",
    ],
  },

  {
    first: "First", last: "Last", year: "2012", position: "GK", photo: "",
    stats: [ ["Saves", "0"], ["Shutouts", "0"], ["Seasons", "4"] ],
    accolades: [
      "All-County 1st Team (Year)",
    ],
    awards: [
      "Independent award (Year)",
    ],
  },

  {
    first: "First", last: "Last", year: "2009", position: "ST", photo: "",
    stats: [ ["Goals", "0"], ["Assists", "0"], ["Seasons", "4"] ],
    accolades: [
      "All-County 1st Team (Year)",
    ],
    awards: [
      "Independent award (Year)",
    ],
  },

];
