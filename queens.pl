% Autor:
% Fecha: 30/01/2020
% [[0,0,0,q,0,0,0,0],[0,q,0,0,0,0,0,0],[0,0,0,0,0,0,0,q],[0,0,0,0,0,0,0,0],
%  [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
mejor(Queens,Mejor):-length(Queens,Xt),X is Xt+1,
       forK(Queens,X,1,Pq),heuG(Pq,Queens,Valores),
       maximo(Valores,M),posc(Valores,M,Pm),
       traeN(Pq,Pm,Mejor).
traeN([Elem|_],1,Elem).
traeN([_|Resto],N,Elem):-Nn is N-1,traeN(Resto,Nn,Elem).
posc([M|_],M,1).
posc([_|Resto],M,Pos):-posc(Resto,M,Post),Pos is Post+1.
heuG([],_,[]).
heuG([[X,Y]|Resto],Queens,[N|Res]):-append(Queens,[[X,Y]],Tq),
       length(Tq,T),Tt is T+1,heu(Tq,Tt,1,N),
       heuG(Resto,Queens,Res).
maximo([X|Xs],M) :- max_cola(Xs,X,M).
max_cola([],M,M).
max_cola([X|Xs],Ac,M):-NAc is max(Ac,X),max_cola(Xs,NAc,M).
heu(_,9,_,0).
heu(Queens,X,Y,T):-forK(Queens,X,Y,PosV),length(PosV,N),
           Xn is X+1,heu(Queens,Xn,1,Tt),T is N+Tt.
forK(_,_,9,[]).
forK(Queens,X,Y,Restq):-(verT(Y,Queens);diag([X,Y],Queens)),
                    Yn is Y+1,forK(Queens,X,Yn,Restq).
forK(Queens,X,Y,[[X,Y]|Restq]):-Yn is Y+1,forK(Queens,X,Yn,Restq).
verT(Y,[[_,Y]|_]).
verT(Y,[_|Restq]):-verT(Y,Restq).
diag([X1,Y1],[[X2,Y2]|_]):-X is abs(X2-X1),Y is abs(Y2-Y1),X==Y.
diag([X1,Y1],[_|Resq]):-diag([X1,Y1],Resq).
forI([P|_],_,0):-not(member(q,P)).
forI([P|Resto],I,Total):-member(q,P),In is I+1,forI(Resto,In,Tp),Total is 1+Tp.
forJ([P|_],_,[]):-not(member(q,P)).
forJ([P|Resto],I,[[I,Pos]|RestoQ]):-member(q,P),posQ(P,Pos),In is I+1,
                         forJ(Resto,In,RestoQ).
posQ([q|_],1).
posQ([_|Resto],Cont):-posQ(Resto,Cp),Cont is Cp+1.