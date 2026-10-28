
bird(sparrow).
bird(parrot).
bird(pigeon).
bird(ostrich).
bird(penguin).

can_fly(sparrow).
can_fly(parrot).
can_fly(pigeon).

cannot_fly(ostrich).
cannot_fly(penguin).

check_flight(Bird) :-
    can_fly(Bird),
    write(Bird),
    writeln(' can fly.').

check_flight(Bird) :-
    cannot_fly(Bird),
    write(Bird),
    writeln(' cannot fly.').

check_flight(Bird) :-
    \+ bird(Bird),
    writeln('Bird information not available.').
