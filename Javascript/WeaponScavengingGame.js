/**
 * Weapon Scavenging
 *
 * The given 2-dimensional array is the assumption of the number of areas that exist.
 *
 * Officer John looks for weapons that he could get from the area he passes and aims to get as mush as possible from the total energy he has.
 * When He passes an area the energy -1.
 * 
 * The weapon he is looking for is in the form of a code like the following :
 * R : Revolver
 * H : Handgun
 * S : Shotgun
 * 
 * If he finds another type or other item then it is ignored.
 *
 * Example :
 * [
 *      ["#","#","S","#","H","#","R"],
 *      ["X","#","#","A","R","H","S"],
 *      ["R","#","K","#","?","S","H"]
 * ]
 *
 * Test Case I
 * Energi : 21
 * Result :
 * [
 *      ["Revolver",3], ["Hangun",3], ["Shotgun",3]
 * ]
 *
 * Test Case II
 * Energi : 7
 * Result :
 * [
 *      ["Revolver",1], ["Handgun", 1], ["Shotgun",1]
 * ]
 */

 const searchWeapons = (map, energy) => {
    if (energy === undefined) {
      return "You don't have energy";
    }
    let Shotgun = 0;
    let Handgun = 0;
    let Revolver = 0;
  
    for (let i = 0; i < map.length; i++) {
      if (energy == 0) {
        break;
      }
  
      for (let j = 0; j < map[i].length; j++) {
        energy--;
        if (map[i][j] == "S") {
          Shotgun++;
        } else if (map[i][j] == "H") {
          Handgun++;
        } else if (map[i][j] == "R") {
          Revolver++;
        }
        if (energy == 0) {
          break;
        }
      }
    }
    
    return [
      ["Revolver", Revolver],
      ["Handgun", Handgun],
      ["Shotgun", Shotgun],
    ];
  };
  
  console.log(
    searchWeapons(
      [
        ["R", "H", "#", "#", "S"],
        ["#", "#", "R", "S", "#"],
        [" ", " ", "R", "H", "S"],
      ],
      10
    )
  );
  // [['Revolver',2],['Handgun',1], ['Shotgun,2]]
  
  console.log(searchWeapons([["#", "#", "#"]]));
  // You don't have energy
  
  console.log(
    searchWeapons(
      [
        ["#", "#", "#", "#", "?"],
        ["#", " ", "@"],
        ["R", "H", "S", "?", " ", "A", "B"],
      ],
      19
    )
  );
  // [["Revolver",1], ['Handgun',1], ['Shotgun',1]]
  