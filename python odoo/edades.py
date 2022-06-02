edades={"mariano":27,"roberto":24,"maria":19,"ana":33}
max=0
for persona in edades:
    if(max<edades[persona]):
        max=edades[persona]
        personaMayor=persona
print(personaMayor + " su edad es "+ str(max))        
