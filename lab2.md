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
### zad.2
```
kobieta(X) :-
    \+mezczyzna(X).

ojciec(X,Y) :-
    rodzic(Y,X),
    mezczyzna(X).
    
matka(X,Y) :-
    rodzic(Y,X),
    kobieta(X).

corka(X,Y) :-
    rodzic(X,Y),
    kobieta(X).

brat_rodzony(X,Y) :-
    rodzic(Y,A),
    rodzic(X,B),
    rodzic(Y,B),
    rodzic(X,A),
    mezczyzna(X).
    
brat_przyrodni(X,Y) :-
    rodzic(X,A),
    rodzic(Y,B),
    rodzic(Y,A),
    rodzic(X,C),
    mezyczyzna(X).

kuzyn(X,Y) :-
    rodzic(X,E),
    rodzic(E,F),
    rodzic(Y,G),
    rodzic(G,F),
    mezczyzna(X).

dziadek_od_strony_ojca(X,Y) :-
    ojciec(X,A),
    ojciec(A,Y).

dziadek_od_strony_matki(X,Y) :-
    ojciec(X,A),
    matka(A,Y).

dziadek(X,Y) :-
    rodzic(Y,A),
    ojciec(X,A).

babcia(X,Y) :-
    rodzic(Y,A),
    matka(X,A).

wnuczka(X,Y) :-
    rodzic(Y,A),
    rodzic(A,X),
    kobieta(Y).

przodek_do2pokolenia_wstecz(X,Y) :-
    rodzic(Y,A),
    rodzic(A,X).

przodek_do3pokolenia_wstecz(X,Y) :-
    rodzic(Y,A),
    rodzic(A,B),
    rodzic(B,X).
````
