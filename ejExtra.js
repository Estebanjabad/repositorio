// Queremos representar un equipo de fútbol 5. 
// Para ello necesitamos tener el nombre de cada jugador,
//  su posición (arco, defensa, mediocampo, adelante) y su 
//  edad. ¿Cómo representamos a cada jugador? ¿Cómo representamos
//   un equipo? ¿Cómo representamos los 8 equipos que juegan el torneo?


let Messi = {
    nombre: "Lionel Messi",
    posicion: "adelante",
    edad: 31
}

let Messi2 = {
    nombre: "Lionel Messi",
    posicion: "arco",
    edad: 31
}

let Messi3 = {
    nombre: "Lionel Messi",
    posicion: "adelante",
    edad: 31
}

let Messi4 = {
    nombre: "Lionel Messi",
    posicion: "adelante",
    edad: 31
}
let equipo = [Messi, Messi2]

let equipo2 = [Messi3, Messi4]
let torneo = [equipo, equipo2]


console.log(torneo[0][1].posicion)




