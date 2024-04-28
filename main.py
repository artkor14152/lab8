with open("data [1nzNjv].csv") as file:
    for line in file:
        data = line.split (',')
        name = f"{data[3][1:]} {data[4][1:-1]}"
        print(name)

Survided = []
NotSurvided = []
with open("data [1nzNjv].csv")as f:
    next(f)
    for line in f:
        data = line.split(',')
        isSurvided = data[1]
        if isSurvided == '1':
            Survided.append(float(data[10]))
        else:
            NotSurvided.append(float(data[10]))
    priseSurvided = sum(Survided) / len(Survided)
    priseNotSurvided = sum(NotSurvided) / len(NotSurvided)
    print(f"{priseSurvided:0.2f}")
    print(f"{priseNotSurvided:0.2f}")