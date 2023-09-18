import musicalbeeps
import random

MIDDLE_C = "C4"
TONE_LENGTH = 2  # 2 seconds

notes = input("what notes do you want to test? ")
notes = notes.replace(' ', '').split(',')
lowest = int(input("lowest octave? "))
highest = int(input("highest octave? "))
player = musicalbeeps.Player(volume = 0.3, mute_output=True)

while True:
    print("playing reference tone C4...")
    player.play_note(MIDDLE_C, TONE_LENGTH)
    input("")
    mystery_note = random.choice(notes)
    random_octave = random.choice(range(lowest, highest+1))
    mystery_note_octave = mystery_note + str(random_octave)
    print("playing mystery note...")
    player.play_note(mystery_note_octave, TONE_LENGTH)
    guess = input("what's the note and octave number? ")
    if guess == mystery_note_octave:
        print("correct!")
    else:
        print(f"that's not correct... the note was {mystery_note_octave}")
        print(f"your guess {guess} would have sounded like this")
        player.play_note(guess, TONE_LENGTH)
    quit = input("keep playing? ")
    if quit == "no":
        break