
monkey(at_door).

can_get_banana :-
    monkey(at_door),
    write('Monkey moves to the box.'), nl,
    write('Monkey pushes the box under the bananas.'), nl,
    write('Monkey climbs onto the box.'), nl,
    write('Monkey grabs the bananas.'), nl,
    write('Monkey gets the bananas!'), nl.
