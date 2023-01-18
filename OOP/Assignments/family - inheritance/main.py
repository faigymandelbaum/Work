from parent import Parent
from child import Child

def main():
    Tatty = Parent("Tatty", "Mandelbaum", 62)
    Mommy = Parent("Mommy", "Mandelbaum", 62)
    child1 = Child("Dovid", "Mandelbaum", 35)
    child2 = Child("Dovid", "Mandelbaum", 35)

    print (child1)
    print (Tatty.babysit())
    
    print (Tatty)
    print (child1.babysit())
    
    

main()    