"""
---------------------------------------------------------------------------
I Python kan man skicka in 'default' parametrar! Istället för att
skicka in en nolla i loop kan du askicka in en default prameter
som är default-värdet du väljer om inget annat anges i anropet.
Exempel:
    def loop(tot, start, end=0):
        ...

    Och vid anrop loop(tot, n) Så kommer end vara 0.
    Vid anrop loop(tot, n, 2) kommer end vara end=2.
    (Jag böt plats på parameterdefinitionen i funktionen för exemplet.)


I din lösning skickar du med en variabel, tot,  i varje funktionsanrop som till slut är resultatet. 
Det funkar, men hade man kunnat gjort på något annat sätt?

Kanske hade man kunnat returnera start * loop(start+1, end) och haft return 1 i basfallet för loop istället?
---------------------------------------------------------------------------
"""


#edvbe696
def choose(k,n):    
    tot = 1
    if(k-n > n):
        return (loop(k,tot,(k-n))//loop(n,tot))
    else:
        return (loop(k,tot,n)//loop((k-n),tot))


def loop(start,tot,end=0):
    if start>(end):
        tot*=start
        start-=1
        return loop(start,tot,end)
    else: 
        return tot
        
    
