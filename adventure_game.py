import time
import random

mistakes = 0


def print_slow(input_text):
    print(input_text)
    # time.sleep(2)


def intro():
    print_slow(
        "As you traverse a lush mountain landscape you happen upon "
        "A collosal dragon. It's emerald scales shimmering in the sunlight. "
        "The dragon hasn't noticed you yet. You must make a decision "
        "that will almost certainly impact the outcome of this quest.")
    user_decision()


def user_decision():
    actions = ["1: Attack", "2: Sneak around", "3: Talk"]
    print_slow("How will you proceed?")

    for action in actions:
        print_slow(action)

    decision = input("Please choose: ")
    initial_choice(decision)


def initial_choice(choice):
    if choice == "1":
        attack()
    elif choice == "2":
        sneak()
    elif choice == "3":
        talk()
    else:
        print_slow("What are you doing!! This is no time to be goofing around")
        if mistake_counter():
            user_decision()


def play_again():
    global mistakes
    mistakes = 0
    while True:
        print_slow("Would you like to play again? Yes/No")
        choice = input("Please choose: ").lower()
        if choice == "yes":
            take_quest()
            break
        elif choice == "no":
            print_slow("Thanks for playing!!!")
            break
        else:
            print_slow("You must enter Yes/No -__-")


def dysentary_game_over():
    print_slow(
        "You drink from the water and begin your search for path "
        "back to town. You die of dysentary. GAME OVER!")
    play_again()


def failed_quest_game_over():
    print_slow(
        "You find the path and make it back to town successfully. "
        "You have failed the quest but at least you have your life. "
        "However meaningless it is. GAME OVER!")
    play_again()


def mistake_game_over():
    bad_outcomes = [
        "Slips on banana peel and plummits to death. GAME OVER!",
        "A wizards miscast fireball falls from the sky incinerating you "
        "instantly. GAME OVER!", "You spot a curious looking mushroom "
        "and decide to have a snack. GAME OVER!"]
    outcome = random.choice(bad_outcomes)
    print_slow("All that goofing off can be costly.")
    print_slow(outcome)
    play_again()


def cross_game_over():
    print_slow(
        "You slowly begin crossing the bridge, gaining confidence "
        "the further you go. When you are about 10 feet away from "
        "the end you hear a creaking noise The boards under your "
        "feet give way and you plummet. GAME OVER!")
    play_again()


def winning():
    print_slow(
        "You accept the dragons offer and he then scoops your up "
        "with his tail and places you on his back. As the dragon "
        "starts flying you take in the beautiful landscape and watch "
        "as another adventure plummets through the bridge you almost "
        "took. As you reach the top the dragon lets you off and you "
        "offer him your thanks. You turn and see your prize. The fabled "
        "hidden stash of dwarven booze. You are able to find your way "
        "back to town and become the town Hero. WIN!!")
    play_again()

#counts the number of mistakes a user makes when entering input. More than 3 and game over!
def mistake_counter():
    global mistakes
    mistakes += 1
    if mistakes >= 3:
        mistake_game_over()
    else:
        return True


def validate_input(prompt, options, stage):
    while True:
        option = input(prompt)
        if option in options:
            return option
        print_slow("You really should quit goofing off.")
        if mistake_counter():
            redirect_validation(stage)
            break
        break


def redirect_validation(stage):
    if stage == 1:
        return attack_stage_two()
    if stage == 2:
        return sneak_stage_two()
    if stage == 3:
        return talk_stage_two()


def attack():
    print_slow(
        "You bravely charge forward towards the dragon, Wielding your "
        "legendary sword that has been passed down through your family "
        "for generations! Your sword shatters on the dragons emerald "
        "scales and he bats you down the mountain!!! You awaken near "
        "a small body of water several hours later. You are bruised and "
        "sore but didn't sustain any life threatening injuries. You notice "
        "the water and how thirsty you are. The water is still but doesn't "
        "appear contaminated. Will you drink here or search for a path "
        "back to town?")
    attack_stage_two()


def attack_stage_two():
    actions = ["1: Drink", "2: Search"]
    decision = validate_input(f"Please choose {actions} : ", ["1", "2"], 1)
    if decision == "1":
        dysentary_game_over()
    if decision == "2":
        failed_quest_game_over()


def sneak():
    print_slow(
        "You are able to find some bushes and begin to sneak past the dragon. "
        "As you work your way past a rabbit jumps out and distracts the "
        "dragon the dragon remains unaware as you silently pass by once "
        "you are past the dragon you come upon a rickety old bridge. You are "
        "so close to your goal. What will you do?")
    sneak_stage_two()


def sneak_stage_two():
    actions = ["1: cross", "2: go back"]
    decision = validate_input(f"Please choose {actions} : ", ["1", "2"], 2)
    if decision == "1":
        cross_game_over()
    if decision == "2":
        failed_quest_game_over()


def talk():
    print_slow(
        """You confidently approach the dragon and speak. "I am on a """
        """quest and need to reach the top of this mountain. Will you """
        """allow me to pass?" The dragon just sits there staring stunned """
        """that a human would speak to him. After awhile you decide to """
        """pass and thats when the dragon speaks. "The bridge past here """
        """is badly worn and I would not suggest using it. If you need """
        """to get to the top of the mountain. I would glady fly you there """
        """myself" You have a decision to make. Accept the dragons ride or """
        """use the bridge.""")
    talk_stage_two()


def talk_stage_two():
    actions = ["1: bridge", "2: fly"]
    decision = validate_input(f"Please choose {actions} : ", ["1", "2"], 3)
    if decision == "1":
        cross_game_over()
    if decision == "2":
        winning()


def take_quest():
    intro()


take_quest()
