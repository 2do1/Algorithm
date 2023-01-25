t = int(input())

for _ in range(t):
    record_sound = input().split() # 녹음된 소리

    while True:
        animal_sounds = input() 

        if animal_sounds == "what does the fox say?":
            break

        cry_sound = animal_sounds.split()[-1]

        while cry_sound in record_sound:
            record_sound.remove(cry_sound)
    
    print(" ".join(record_sound))