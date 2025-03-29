import carClass, person

benz = carClass.Car()
# benz.whatCar()
benz.setModel("Mercedez AMG GLE 63s")
print(benz.getModel())


josh = person.Person()

if josh.height == 5:
    print("its 5")
else:
    print("its 0")