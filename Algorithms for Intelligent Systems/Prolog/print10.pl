print_to_10(10) :- 
	write(10),
	nl.

print_to_10(X) :-
	write(X),
	nl,
	Y is X+1,
	print_to_10(Y).


%% print_to_10(1).