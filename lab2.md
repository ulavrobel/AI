### zad.1.1
- a) rodzenstwo
- b) kuzynostwo
- c) swat
- d) macocha
- e) przyrodnie rodzenstwo
- f) szwagrowie
- g) dziwny przypadek

### zad1.2
```
przykA(X,Y) :-
    rodzic(Y,A),
    rodzic(X,B),
    rodzic(Y,B),
    rodzic(X,A).

przykB(X,Y) :-
    rodzic(X,E),
    rodzic(E,F),
    rodzic(Y,G),
    rodzic(G,F).

przykC(X,Y) :-
    rodzic(B,A),
    rodzic(C,A),
    rodzic(X,B),
    rodzic(Y,C).

przykD(X,Y) :-
    rodzic(A,X),
    rodzic(Y,B),
    rodzic(A,B).

przykE(X,Y) :-
    rodzic(A,X),
    rodzic(B,X),
    rodzic(B,Y),
    rodzic(C,Y).

przykF(X,Y) :-
    rodzic(X,A),
    rodzic(B,C),
    rodzic(C,A),
    rodzic(B,Y).
    
przykG(X,Y) :-
    rodzic(A,X),
    rodzic(A,B),
    rodzic(B,C),
    rodzic(C,Y),
    rodzic(D,X),
    rodzic(D,Y).
```
