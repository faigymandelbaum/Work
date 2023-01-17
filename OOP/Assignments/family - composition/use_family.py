from family import Family
from family_members import FamilyMember

def main():
    family_member4 = FamilyMember("Faigy", 21, False)
    family_member3 = FamilyMember("Dov", 24, False)
    family_member1 = FamilyMember("Tatty", 62, True)
    family_member6 = FamilyMember("Yosef", 13, True)
    family_member5 = FamilyMember("Motty", 17, False)
    family_member2 = FamilyMember("Mommy", 59, True)

    family_members = [family_member1, family_member2, family_member3, family_member4, family_member5, family_member6] 

    my_family = Family('Mandelbaum', "Sorotzkin 26", "doing Chessed", family_members)
    print (my_family)

if __name__ == '__main__':
    main()    
