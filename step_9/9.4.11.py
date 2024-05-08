s = input()
count = 0
symbol = ''
for i in s:
    if s.count(i) >= count and i != symbol:
        symbol = i
        count = s.count(i)

print(symbol)


# s = input()
#
# most_common = s[0]
# for el in s:
#     if s.count(el) >= s.count(most_common):
#         most_common = el
#
# print(most_common)


# AHahahahahahahah
# se = input()
# q=0
# w=0
# e=0
# r=0
# t=0
# y=0
# u=0
# i=0
# o=0
# p=0
# a=0
# s=0
# d=0
# f=0
# g=0
# h=0
# j=0
# k=0
# l=0
# z=0
# x=0
# c=0
# v=0
# b=0
# n=0
# m=0
# Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N,M=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
# qq,qw,qe,qr,qt,qy,qu,qi,qo,qp,qa,qs,qd,qf,qg,qh,qj,qk,ql,qz,qx,qc,qv,qb,qn,qm,wq,ww,we,wr,wt,wy,wu=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
# QQ,QW,QE,QR,QT,QY,QU,QI,QO,QP,QA,QS,QD,QF,QG,QH,QJ,QK,QL,QZ,QX,QC,QV,QB,QN,QM,WQ,WW,WE,WR,WT,WY,WU=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
# eq,ew,ee,er,et,ey,eu,ei,eo,ep=0,0,0,0,0,0,0,0,0,0
# for it in range(len(se)):
#     if se[it] in 'q':
#         q+=1
#     elif se[it] in 'w':
#         w+=1
#     elif se[it] in 'e':
#         e+=1
#     elif se[it] in 'r':
#         r+=1
#     elif se[it] in 't':
#         t+=1
#     elif se[it] in 'y':
#         y+=1
#     elif se[it] in 'u':
#         u+=1
#     elif se[it] in 'i':
#         i+=1
#     elif se[it] in 'o':
#         o+=1
#     elif se[it] in 'p':
#         p+=1
#     elif se[it] in 'a':
#         a+=1
#     elif se[it] in 's':
#         s+=1
#     elif se[it] in 'd':
#         d+=1
#     elif se[it] in 'f':
#         f+=1
#     elif se[it] in 'g':
#         g+=1
#     elif se[it] in 'h':
#         h+=1
#     elif se[it] in 'j':
#         j+=1
#     elif se[it] in 'k':
#         k+=1
#     elif se[it] in 'l':
#         l+=1
#     elif se[it] in 'z':
#          z+=1
#     elif se[it] in 'x':
#         x+=1
#     elif se[it] in 'c':
#         c+=1
#     elif se[it] in 'v':
#         v+=1
#     elif se[it] in 'b':
#         b+=1
#     elif se[it] in 'n':
#         n+=1
#     elif se[it] in 'm':
#         m+=1
#     elif se[it] in 'Q':
#         Q+=1
#     elif se[it] in 'W':
#         W+=1
#     elif se[it] in 'E':
#         E+=1
#     elif se[it] in 'R':
#         R+=1
#     elif se[it] in 'T':
#         T+=1
#     elif se[it] in 'Y':
#         Y+=1
#     elif se[it] in 'U':
#         U+=1
#     elif se[it] in 'I':
#         I+=1
#     elif se[it] in 'O':
#         O+=1
#     elif se[it] in 'P':
#         P+=1
#     elif se[it] in 'A':
#         A+=1
#     elif se[it] in 'S':
#         S+=1
#     elif se[it] in 'D':
#         D+=1
#     elif se[it] in 'F':
#         F+=1
#     elif se[it] in 'G':
#         G+=1
#     elif se[it] in 'H':
#         H+=1
#     elif se[it] in 'J':
#         J+=1
#     elif se[it] in 'K':
#         K+=1
#     elif se[it] in 'L':
#         L+=1
#     elif se[it] in 'Z':
#         Z+=1
#     elif se[it] in 'X':
#         X+=1
#     elif se[it] in 'C':
#         C+=1
#     elif se[it] in 'V':
#         V+=1
#     elif se[it] in 'B':
#         B+=1
#     elif se[it] in 'N':
#         N+=1
#     elif se[it] in 'M':
#         M+=1
#     elif se[it] in 'й':
#         qq+=1
#     elif se[it] in 'ц':
#         qw+=1
#     elif se[it] in 'у':
#         qe+=1
#     elif se[it] in 'к':
#         qr+=1
#     elif se[it] in 'е':
#         qt+=1
#     elif se[it] in 'н':
#         qy+=1
#     elif se[it] in 'г':
#         qu+=1
#     elif se[it] in 'ш':
#         qi+=1
#     elif se[it] in 'щ':
#         qo+=1
#     elif se[it] in 'з':
#         qp+=1
#     elif se[it] in 'х':
#         qa+=1
#     elif se[it] in 'ъ':
#         qs+=1
#     elif se[it] in 'ф':
#         qd+=1
#     elif se[it] in 'ы':
#         qf+=1
#     elif se[it] in 'в':
#         qg+=1
#     elif se[it] in 'а':
#         qh+=1
#     elif se[it] in 'п':
#         qj+=1
#     elif se[it] in 'р':
#         qk+=1
#     elif se[it] in 'о':
#         ql+=1
#     elif se[it] in 'л':
#         qz+=1
#     elif se[it] in 'д':
#         qx+=1
#     elif se[it] in 'ж':
#         qc+=1
#     elif se[it] in 'э':
#         qv+=1
#     elif se[it] in 'я':
#         qb+=1
#     elif se[it] in 'ч':
#         qn+=1
#     elif se[it] in 'с':
#         qm+=1
#     elif se[it] in 'м':
#         wq+=1
#     elif se[it] in 'и':
#         ww+=1
#     elif se[it] in 'т':
#         we+=1
#     elif se[it] in 'ь':
#         wr+=1
#     elif se[it] in 'б':
#         wt+=1
#     elif se[it] in 'ю':
#         wy+=1
#     elif se[it] in 'ё':
#         wu+=1
#     elif se[it] in 'Й':
#         QQ+=1
#     elif se[it] in 'Ц':
#         QW+=1
#     elif se[it] in 'У':
#         QE+=1
#     elif se[it] in 'К':
#         QR+=1
#     elif se[it] in 'Е':
#         QT+=1
#     elif se[it] in 'Н':
#         QY+=1
#     elif se[it] in 'Г':
#         QU+=1
#     elif se[it] in 'Ш':
#         QI+=1
#     elif se[it] in 'Щ':
#         QO+=1
#     elif se[it] in 'З':
#         QP+=1
#     elif se[it] in 'Х':
#         QA+=1
#     elif se[it] in 'Ъ':
#         QS+=1
#     elif se[it] in 'Ф':
#         QD+=1
#     elif se[it] in 'Ы':
#         QF+=1
#     elif se[it] in 'В':
#         QG+=1
#     elif se[it] in 'А':
#         QH+=1
#     elif se[it] in 'П':
#         QJ+=1
#     elif se[it] in 'Р':
#         QK+=1
#     elif se[it] in 'О':
#         QL+=1
#     elif se[it] in 'Л':
#         QZ+=1
#     elif se[it] in 'Д':
#         QX += 1
#     elif se[it] in 'Ж':
#         QC += 1
#     elif se[it] in 'Э':
#         QV += 1
#     elif se[it] in 'Я':
#         QB += 1
#     elif se[it] in 'Ч':
#         QN += 1
#     elif se[it] in 'С':
#         QM += 1
#     elif se[it] in 'М':
#         WQ += 1
#     elif se[it] in 'И':
#         WW += 1
#     elif se[it] in 'Т':
#         WE += 1
#     elif se[it] in 'Ь':
#         WR += 1
#     elif se[it] in 'Б':
#         WT += 1
#     elif se[it] in 'Ё':
#         WY += 1
#     elif se[it] in 'Ю':
#         WU += 1
#     elif se[it] in '0':
#         eq += 1
#     elif se[it] in '1':
#         ew += 1
#     elif se[it] in '2':
#         ee += 1
#     elif se[it] in '3':
#         er += 1
#     elif se[it] in '4':
#         et += 1
#     elif se[it] in '5':
#         ey += 1
#     elif se[it] in '6':
#         eu += 1
#     elif se[it] in '7':
#         ei += 1
#     elif se[it] in '8':
#         eo += 1
#     elif se[it] in '9':
#         ep += 1
# RS=max(q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m,Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N,M,qq,qw,qe,qr,qt,qy,qu,qi,qo,qp,qa,qs,qd,qf,qg,qh,qj,qk,ql,qz,qx,qc,qv,qb,qn,qm,wq,ww,we,wr,wt,wy,QQ,QW,QE,QR,QT,QY,QU,QI,QO,QP,QA,QS,QD,QF,QG,QH,QJ,QK,QL,QZ,QX,QC,QV,QB,QN,QM,WQ,WW,WE,WR,WT,WY,eq,ew,ee,er,et,ey,eu,ei,eo,ep)
# if RS==q:
#     print('q')
# elif RS==w:
#     print('w')
# elif RS==e:
#     print('e')
# elif RS==r:
#     print('r')
# elif RS==t:
#     print('t')
# elif RS==y:
#     print('y')
# elif RS==u:
#     print('u')
# elif RS==i:
#     print('i')
# elif RS==o:
#     print('o')
# elif RS==p:
#     print('p')
# elif RS==a:
#     print('a')
# elif RS==s:
#     print('s')
# elif RS==d:
#     print('d')
# elif RS==f:
#     print('f')
# elif RS==g:
#     print('g')
# elif RS==h:
#     print('h')
# elif RS==j:
#     print('j')
# elif RS==k:
#     print('k')
# elif RS==l:
#     print('l')
# elif RS==z:
#     print('z')
# elif RS==x:
#     print('x')
# elif RS==c:
#     print('c')
# elif RS==v:
#     print('v')
# elif RS==b:
#     print('b')
# elif RS==n:
#     print('n')
# elif RS==m:
#     print('m')
# elif RS==Q:
#     print('Q')
# elif RS==W:
#     print('W')
# elif RS==E:
#     print('E')
# elif RS==R:
#     print('R')
# elif RS==T:
#     print('T')
# elif RS==Y:
#     print('Y')
# elif RS==U:
#     print('U')
# elif RS==I:
#     print('I')
# elif RS==O:
#     print('O')
# elif RS==P:
#     print('P')
# elif RS==A:
#     print('A')
# elif RS==S:
#     print('S')
# elif RS==D:
#     print('D')
# elif RS==F:
#     print('F')
# elif RS==G:
#     print('G')
# elif RS==H:
#     print('H')
# elif RS==J:
#     print('J')
# elif RS==K:
#     print('K')
# elif RS==L:
#     print('L')
# elif RS==Z:
#     print('Z')
# elif RS==X:
#     print('X')
# elif RS==C:
#     print('C')
# elif RS==V:
#     print('V')
# elif RS==B:
#     print('B')
# elif RS==N:
#     print('N')
# elif RS==M:
#     print('M')
# elif RS==qq:
#     print('й')
# elif RS==qw:
#     print('ц')
# elif RS==qe:
#     print('у')
# elif RS==qr:
#     print('к')
# elif RS==qt:
#     print('е')
# elif RS==qy:
#     print('н')
# elif RS==qu:
#     print('г')
# elif RS==qi:
#     print('ш')
# elif RS==qo:
#     print('щ')
# elif RS==qp:
#     print('з')
# elif RS==qa:
#     print('х')
# elif RS==qs:
#     print('ъ')
# elif RS==qd:
#     print('ф')
# elif RS==qf:
#     print('ы')
# elif RS==qg:
#     print('в')
# elif RS==qh:
#     print('а')
# elif RS==qj:
#     print('п')
# elif RS==qk:
#     print('р')
# elif RS==ql:
#     print('о')
# elif RS==qz:
#     print('л')
# elif RS==qx:
#     print('д')
# elif RS==qc:
#     print('ж')
# elif RS==qv:
#     print('э')
# elif RS==qb:
#     print('я')
# elif RS==qn:
#     print('ч')
# elif RS==qm:
#     print('с')
# elif RS==wq:
#     print('м')
# elif RS==ww:
#     print('и')
# elif RS==we:
#     print('т')
# elif RS==wr:
#     print('ь')
# elif RS==wt:
#     print('б')
# elif RS==wy:
#     print('ю')
# elif RS==wu:
#     print('ё')
# elif RS==QQ:
#     print('Й')
# elif RS==QW:
#     print('Ц')
# elif RS==QE:
#     print('У')
# elif RS==QR:
#     print('К')
# elif RS==QT:
#     print('Е')
# elif RS==QY:
#     print('Н')
# elif RS==QU:
#     print('Г')
# elif RS==QI:
#     print('Ш')
# elif RS==QO:
#     print('Щ')
# elif RS==QP:
#     print('З')
# elif RS==QA:
#     print('Х')
# elif RS==QS:
#     print('Ъ')
# elif RS==QD:
#     print('Ф')
# elif RS==QF:
#     print('Ы')
# elif RS==QG:
#     print('В')
# elif RS==QH:
#     print('А')
# elif RS==QJ:
#     print('П')
# elif RS==QK:
#     print('Р')
# elif RS==QL:
#     print('О')
# elif RS==QZ:
#     print('Л')
# elif RS==QX:
#     print('Д')
# elif RS==QC:
#     print('Ж')
# elif RS==QV:
#     print('Э')
# elif RS==QB:
#     print('Я')
# elif RS==QN:
#     print('Ч')
# elif RS==QM:
#     print('С')
# elif RS==WQ:
#     print('М')
# elif RS==WW:
#     print('И')
# elif RS==WE:
#     print('Т')
# elif RS==WR:
#     print('Ь')
# elif RS==WT:
#     print('Б')
# elif RS==WY:
#     print('Ю')
# elif RS==WU:
#     print('Ё')
# elif RS==eq:
#     print('0')
# elif RS==ew:
#     print('1')
# elif RS==ee:
#     print('2')
# elif RS==er:
#     print('3')
# elif RS==et:
#     print('4')
# elif RS==ey:
#     print('5')
# elif RS==eu:
#     print('6')
# elif RS==ei:
#     print('7')
# elif RS==eo:
#     print('8')
# elif RS==ep:
#     print('9')
