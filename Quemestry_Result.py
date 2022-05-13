def chemestry_result(a):
     
    He_adds_powdered_iron_to_a = float(a[0].E.get()) #.mL
    and_finds_that_it_has_a_mass_of = float(a[1].E.get())      / 1000 #.mg.
    mass_of_copper = float(a[2].E.get()) #g*mol #Need to find it
    molar_mass_of_CuSO4 =  float(a[3].E.get()) #g/mol #Need to find it
            
    moles_Cu = and_finds_that_it_has_a_mass_of / mass_of_copper

    mass_of_CuSO4 = moles_Cu * molar_mass_of_CuSO4

    concentration_of_CuSO4 = mass_of_CuSO4 / He_adds_powdered_iron_to_a

    concentration_of_CuSO4 = concentration_of_CuSO4 * 1000

    return concentration_of_CuSO4
   
