def car():
    model_name = input("What is the Vehicle Model: ")
    vehicle_name = input("What is the Vehicle Name: ")
    f1.write('  AddTextEntry(' + "'%s'" %model_name + ', ' + "'%s'" %vehicle_name + ')' + ',' + '\n')

with open('vehicle_name.lua', 'w+') as f:
   f.write('function AddTextEntry(key, value)\n' + '   Citizen.InvokeNative(GetHashKey("ADD_TEXT_ENTRY"), key, value)\n' + 'end\n')
   f.write('\n' + 'Citizen.CreateThread(function()\n')
f.close

more = input("Do you want to add vehicles? (Y/N): ")

if more == "Y" or more == "y":
    with open('vehicle_name.lua', 'a+') as f1:
        num = int(input('How many cars would you like to add: '))
        for i in range(num):
            if num == num:
                car()
                print(" ")
            else:
                f1.write('\n' + 'end')

else:
    with open('vehicle_name.lua', 'a+') as end1:
        end1.write('\n' + 'end')
        print("Shap!")

with open('vehicle_name.lua', 'a+') as f2:
    f2.write('end')