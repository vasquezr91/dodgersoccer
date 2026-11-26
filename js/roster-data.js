/* =====================================================================
   DODGER SOCCER ROSTER
   ---------------------------------------------------------------------
   One line = one player card. To add a player, copy a whole line
   (from { to },) and change the details. To remove one, delete the line.

   number   : jersey number
   first    : first name
   last     : last name
   position : GK = Goalkeeper   DF = Defender   MF = Midfielder
              W  = Winger       ST = Striker
   grade    : Senior, Junior, Sophomore, Freshman
   year     : graduation year, e.g. "2027"
   photo    : file name of the photo in the images/players/ folder.
              Leave it as "" to show the placeholder silhouette.

   VARSITY ONLY: the stats shown in the pop-up for each position are
   set in ROSTER_STATS at the bottom of this file.

   Players are sorted automatically by position, then by jersey number,
   so you can type them in any order.
   ===================================================================== */

window.ROSTER = {

  varsity: [
    // Goalkeepers
    { number: 1,  first: "First", last: "Last", position: "GK", grade: "Senior", year: "2027", saves: 0, seasons: 3, photo: "" },
    { number: 24, first: "First", last: "Last", position: "GK", grade: "Junior", year: "2028", saves: 0, seasons: 2, photo: "" },
    // Defenders
    { number: 4,  first: "First", last: "Last", position: "DF", grade: "Junior", year: "2028", goals: 0, assists: 0, seasons: 2, photo: "" },
    // Midfielders
    { number: 8,  first: "First", last: "Last", position: "MF", grade: "Senior", year: "2027", goals: 0, assists: 0, seasons: 3, photo: "" },
    // Wingers
    { number: 11, first: "First", last: "Last", position: "W",  grade: "Senior", year: "2027", goals: 0, assists: 0, seasons: 3, photo: "" },
    // Strikers
    { number: 9,  first: "First", last: "Last", position: "ST", grade: "Junior", year: "2028", goals: 0, assists: 0, seasons: 2, photo: "" },
  ],

  jv: [
    { number: 1,  first: "First", last: "Last", position: "GK", grade: "Sophomore", year: "2029", photo: "" },
    { number: 10, first: "First", last: "Last", position: "MF", grade: "Sophomore", year: "2029", photo: "" },
  ],

  freshmen: [
    { number: 1,  first: "First", last: "Last", position: "GK", grade: "Freshman",  year: "2030", photo: "" },
    { number: 7,  first: "First", last: "Last", position: "W",  grade: "Freshman",  year: "2030", photo: "" },
  ],

};

/* =====================================================================
   STATS SHOWN IN THE VARSITY POP-UP, BY POSITION
   ---------------------------------------------------------------------
   Each stat is written as  ["word in the player line", "Label shown"].
   To track a new stat (for example tackles), add ["tackles", "Tackles"]
   to that position's list, then add  tackles: 0,  to each of those
   players' lines above.
   ===================================================================== */

window.ROSTER_STATS = {
  GK: [ ["saves", "Saves"], ["seasons", "Seasons"] ],
  DF: [ ["goals", "Goals"], ["assists", "Assists"], ["seasons", "Seasons"] ],
  MF: [ ["goals", "Goals"], ["assists", "Assists"], ["seasons", "Seasons"] ],
  W:  [ ["goals", "Goals"], ["assists", "Assists"], ["seasons", "Seasons"] ],
  ST: [ ["goals", "Goals"], ["assists", "Assists"], ["seasons", "Seasons"] ],
};
