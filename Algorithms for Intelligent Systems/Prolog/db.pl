% Query.

 
% Prolog focuses on describing facts and relationships about problems rather then on creating a series of steps to solve that problem.
 
 
% These Facts and Rules are stored in a file called a Database or Knowledge Base
 
 
% You load a knowledge base like this [knowledge]. or this consult('knowledge.pl'). 

% halt. exits the prolog system
 
% listing. Displays the contents of the database
 
% All these commands are called predicates
 
 
% ---------- INTRODUCTION ----------
 
% write prints text between quotes to the screen
 
% nl stands for new line and \'s allows you to use quotes
 
% write('Hello World'),nl,write('Let\'s Program').
 
 
% This is a fact where loves is a predicate and romeo and juliet are atoms (constants) and loves arguments
 
loves(romeo, juliet).
 
% This is a rule where :- (if) says if the item on the right is true, then so is the item on the left
 
loves(juliet, romeo) :- loves(romeo, juliet).
 
% Evaluating whether the goal was met in the terminal loves(juliet, romeo). = yes
 
 
% Facts and Rules are called clauses
 
 
% A Variable is an object we can't name at the time of execution
 
% Variables are uppercase while atoms are lowercase
 
% loves(romeo, X). = X = juliet
 
 
% ---------- FACTS ----------
 
% Write the relationship first followed by the objects between parenthese followed by a dot

% albert, male, female are atom constants that must begin with a lowercase letter unless they are between single quotes
 
% An atom can contain letters, numbers, +, -, _, *, /, <, >, :, ., ~, &
 
% AN ATOM CANNOT START WITH _

% The name before parenthese is called the predicate
 
% The names in parenthese are called arguments

% Let's define information about the people above
 
 
male(albert).
male(bob).
male(bill).
male(carl).
male(charlie).
male(dan).
male(edward).
 
female(alice).
female(betsy).
female(diana).
 
% We can find out if alice is a woman with
 
% female(alice). = yes
 
% listing(male). = list all clauses defining the predicate male
 
% male(X), female(Y). = Show all combinations of male and female
 
 
% ---------- RULES ----------
 
% Rules are used when you want to say that a fact depends on a group of facts
 
 
% NOTE : You'll get the discontiguous predicate warning if you don't keep your predicates together
 
 
happy(albert).
happy(alice).
happy(bob).
happy(bill).
with_albert(alice).
 
% We can define the Fact that when Bob is happy he runs
 
% :- stands for if
 
runs(albert) :- happy(albert).
% runs(albert). = yes
 
 
% We can check if 2 conditions are true by putting a comma (and) between questions (CONJUCTIONS)
 
dances(alice) :-
  happy(alice),
  with_albert(alice).
 
% We can define predicates to keep commands brief
 
does_alice_dance :- dances(alice),
       write('When Alice is happy and with Albert she dances').
% Just type does_alice_dance. in the terminal
 
 
% Both rules must be true to get a yes result
 
swims(bob) :-
  happy(bob),
  near_water(bob).
% swims(bob). = no
 
 
% We can create 2 instances and if either comes back true the result will be yes
 
swims(bill) :-
  happy(bill).
 
swims(bill) :-
  near_water(bill).
% swims(bill). = yes
 
 
% ---------- VARIABLES ----------
 
% A variable is an object we are unable to name when writing a program.
 
% An instantiated variable is one that stands for an object.
 
% A variable begins with an uppercase letter or _ and can contain
 
% the same symbols as atoms.
 
% The same variable name used in 2 different questions represents 2
 
% completely different variables.
 
 
% An uninstantiated variable can be used to search for any match.
 
 
% Return all females (Type ; to cycle through them)
 
% female(X). X = alice X = betsy X = diana
 
 
parent(albert, bob).
parent(albert, betsy).
parent(albert, bill).
 
parent(alice, bob).
parent(alice, betsy).
parent(alice, bill).
 
parent(bob, carl).
parent(bob, charlie).

% When you are cycling through the results the no at the end signals that there are no more results
 
% parent(X, bob). X = albert; X = alice.
 
% parent(X, bob), dances(X). X = alice.
 
 
% Who is Bobs parent? Does he have parents?
 
% parent(Y, carl), parent(X, Y). = 

% X = albert, Y = bob;
% X = alice Y = bob.

% Find Alberts grandchildren
 
% Is Albert a father? Does his children have any children?
 
% parent(albert, X), parent(X, Y). = 

% X = bob, Y = carl;
% X = bob, Y = charlie.
 
 
% Use custom predicate for multiple results
 
get_grandchild :- 
	parent(albert, X),
	parent(X, Y),
	write("Albert's gradchild is "),
	write(Y), nl.
 
% Do Carl and Charlie share a parent
 
% Who is Carls parent? Is this same X a parent of Charlie
 
% parent(X, carl), parent(X, charlie). = X = bob
 
 
% Use format to get the results
 
% ~w represents where to put each value in the list at the end
 
% ~n is a newline
 
% ~s is used to input strings
 
get_same_parent :- 
	parent(X, carl),
    parent(X, charlie),
    format('~w ~s carl and charlie ~n', [X, "has two children,"]).
 
% Does Carl have an Uncle?
 
% Who is Carls parent? Who is Carls fathers brother?
 
brother(bob, bill).
% parent(X, carl), brother(X, Y). = X = bob, Y = bill

get_uncle :-
	parent(X, carl),
	brother(X, Y),
	format('~w is the brother of ~w and the uncle of ~s', [Y, X, "carl!"]).


% Demonstrate axioms and derived facts
 
% We can also use variables in the database
 
% If you get the singleton warning, that means you defined a variable that you didn't do anything with. (This is ok sometimes)
 
grand_parent(X, Y) :-
  parent(Z, X),
  parent(Y, Z).
% grand_parent(carl, A). = A = albert, A = alice


% X blushes if X is human
 
blushes(X) :- 
	human(X).

human(derek).
 
% If we say one thing is true when somehing else is true, we can also find that match if we only assign one thing to be true here.
 
% blushes(derek). = yes


% Another example on cause and effect
 
stabs(tybalt,mercutio,sword).
hates(romeo, X) :- 
	stabs(X, mercutio, sword).
% hates(romeo, X). = X = tybalt
 
 
% We can use _ (anonymous variable) if we won't use the variable more than once
 
% The value of an anonymous var is not output
 
% Check if any males exist in the database : male(_). = yes