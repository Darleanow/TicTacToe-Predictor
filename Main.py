lst={}
sep=1
incorrectcounter=0
for i in range(3):
    line = input()
    for a in line:
        if a=='.':
            incorrectcounter+=1
            if incorrectcounter==9:
                print("false")
                exit(0)
        lst[sep]=a
        sep+=1
if lst[1]=="O" and lst[2]=='O' and lst[3]=='.':
    res=f"OOO\n{lst[4]}{lst[5]}{lst[6]}\n{lst[7]}{lst[8]}{lst[9]}"
elif lst[1]=="O" and lst[5]=="O" and lst[9]==".":
    res=f"{lst[1]}{lst[2]}{lst[3]}\n{lst[4]}{lst[5]}{lst[6]}\n{lst[7]}{lst[8]}O"
elif lst[1]=="O" and lst[4]=="O" and lst[7]==".":
    f"{lst[1]}{lst[2]}{lst[3]}\n{lst[4]}{lst[5]}{lst[6]}\n0{lst[8]}{lst[9]}"
elif lst[1]=="O" and lst[2]=='.' and lst[3]=='O':
    res=f"OOO\n{lst[4]}{lst[5]}{lst[6]}\n{lst[7]}{lst[8]}{lst[9]}"
elif lst[1]=="O" and lst[5]=="." and lst[9]=="O":
    res=f"{lst[1]}{lst[2]}{lst[3]}\n{lst[4]}O{lst[6]}\n{lst[7]}{lst[8]}O"
elif lst[1]=="O" and lst[4]=="." and lst[7]=="O":
    res=f"{lst[1]}{lst[2]}{lst[3]}\nO{lst[5]}{lst[6]}\nO{lst[8]}{lst[9]}"
elif lst[1]=="." and lst[2]=='O' and lst[3]=='O':
    res=f"OOO\n{lst[4]}{lst[5]}{lst[6]}\n{lst[7]}{lst[8]}{lst[9]}"
elif lst[1]=="." and lst[5]=="O" and lst[9]=="O":
    res=f"O{lst[2]}{lst[3]}\n{lst[4]}O{lst[6]}\n{lst[7]}{lst[8]}O"
elif lst[1]=="." and lst[4]=="O" and lst[7]=="O":
    res=f"O{lst[2]}{lst[3]}\nO{lst[5]}{lst[6]}\nO{lst[8]}{lst[9]}"
elif lst[2]=="." and lst[5]=='O' and lst[8]=='O':
    res=f"{lst[1]}O{lst[3]}\n{lst[4]}{lst[5]}{lst[6]}\n{lst[7]}{lst[8]}{lst[9]}"
elif lst[2]=="O" and lst[5]=="." and lst[8]=="O":
    res=f"{lst[1]}{lst[2]}{lst[3]}\n{lst[4]}O{lst[6]}\n{lst[7]}{lst[8]}{lst[9]}"
elif lst[2]=="O" and lst[5]=="O" and lst[8]==".":
    res=f"{lst[1]}{lst[2]}{lst[3]}\n{lst[4]}{lst[5]}{lst[6]}\n{lst[7]}O{lst[9]}"
elif lst[3]=="." and lst[6]=='O' and lst[9]=='O':
    res=f"{lst[1]}{lst[2]}O\n{lst[4]}{lst[5]}{lst[6]}\n{lst[7]}{lst[8]}{lst[9]}"
elif lst[3]=="O" and lst[6]=='.' and lst[9]=='O':
    res=f"{lst[1]}{lst[2]}{lst[3]}\n{lst[4]}{lst[5]}O\n{lst[7]}{lst[8]}{lst[9]}"
elif lst[3]=="O" and lst[6]=='O' and lst[9]=='.':
    res=f"{lst[1]}{lst[2]}{lst[3]}\n{lst[4]}{lst[5]}{lst[6]}\n{lst[7]}{lst[8]}O"
elif lst[3]=="." and lst[5]=="O" and lst[7]=="O":
    res=f"{lst[1]}{lst[2]}O\n{lst[4]}{lst[5]}{lst[6]}\n{lst[7]}{lst[8]}{lst[9]}"
elif lst[3]=="O" and lst[5]=="." and lst[7]=="O":
    res=f"{lst[1]}{lst[2]}{lst[3]}\n{lst[4]}O{lst[6]}\n{lst[7]}{lst[8]}{lst[9]}"
elif lst[3]=="O" and lst[5]=="O" and lst[7]==".":
    res=f"{lst[1]}{lst[2]}{lst[3]}\n{lst[4]}{lst[5]}{lst[6]}\nO{lst[8]}{lst[9]}"
elif lst[4]=="." and lst[5]=="O" and lst[6]=="O":
    res=f"{lst[1]}{lst[2]}{lst[3]}\nO{lst[5]}{lst[6]}\n{lst[7]}{lst[8]}{lst[9]}"
elif lst[4]=="O" and lst[5]=="." and lst[6]=="O":
    res=f"{lst[1]}{lst[2]}{lst[3]}\n{lst[4]}O{lst[6]}\n{lst[7]}{lst[8]}{lst[9]}"
elif lst[4]=="O" and lst[5]=="O" and lst[6]==".":
    res=f"{lst[1]}{lst[2]}{lst[3]}\n{lst[4]}{lst[5]}O\n{lst[7]}{lst[8]}{lst[9]}"
elif lst[7]=="." and lst[8]=="O" and lst[9]=="O":
    res=f"{lst[1]}{lst[2]}{lst[3]}\n{lst[4]}{lst[5]}{lst[6]}\nO{lst[8]}{lst[9]}"
elif lst[7]=="." and lst[8]=="." and lst[9]=="O":
    res=f"{lst[1]}{lst[2]}{lst[3]}\n{lst[4]}{lst[5]}{lst[6]}\n{lst[7]}O{lst[9]}"
elif lst[7]=="." and lst[8]=="O" and lst[9]==".":
    res=f"{lst[1]}{lst[2]}{lst[3]}\n{lst[4]}{lst[5]}{lst[6]}\n{lst[7]}{lst[8]}O"
else:
    print("false")
    exit(0)
print(res)
