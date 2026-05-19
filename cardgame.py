import random
import time
import os

card_deck = {
    1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
    8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K'
}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def shuffle_animation(who, final_card):
    num_flashes = random.randint(8, 13)

    slow_print(f"\n {who} Chose...", delay=0.04)
    time.sleep(0.3)

    for i in range(num_flashes):
        fake_card = random.randint(1, 13)
        code = card_deck[fake_card]
        print(f"\r  [ {code:>2} ]", end='', flush=True)

        if i < num_flashes - 3:
            time.sleep(0.07)
        elif i < num_flashes - 1:
            time.sleep(0.2)
        else:
            time.sleep(0.45)

    final_code = card_deck[final_card]
    print(f"\r  [ {final_code:>2} ]", flush=True)
    time.sleep(0.2)

    slow_print(f"  >> {who} draws: {final_code}", delay=0.04)


def show_result(p_card, c_card, player_name):
    p = card_deck[p_card]
    c = card_deck[c_card]

    print("\n")
    print(f"   {player_name.upper():<15} COMPUTER")
    print(f"  ┌─────────┐     ┌─────────┐")
    print(f"  │ {p:>2}      │     │ {c:>2}      │")
    print(f"  │         │     │         │")
    print(f"  │         │ VS  │         │")
    print(f"  │         │     │         │")
    print(f"  │      {p:>2} │     │      {c:>2} │")
    print(f"  └─────────┘     └─────────┘")
    print()

    time.sleep(0.8)
    slow_print("  ─────────────────────────────", delay=0.02)

    if p_card > c_card:
        slow_print(f"  ★ {player_name} wins! ★", delay=0.06)
    elif c_card > p_card:
        slow_print("  ✖ Computer wins! ✖", delay=0.06)
    else:
        slow_print("  ═ It's a tie! ═", delay=0.06)

    slow_print("  ─────────────────────────────", delay=0.02)


# ── MAIN GAME ──

clear_screen()

slow_print("\n  ╔═══════════════════════════╗", delay=0.015)
slow_print("  ║     HIGH  CARD  DRAW      ║", delay=0.015)
slow_print("  ╚═══════════════════════════╝", delay=0.015)

time.sleep(0.5)
slow_print("\n  Two cards. One winner.", delay=0.015)
slow_print("  Let's see who fate favors...\n", delay=0.04)

# Inputs
player_name = input("Enter your name ❤️ : ")

while True:
    try:
        player_card = int(input("Choose a number from 1-13: "))
        if 1 <= player_card <= 13:
            break
        else:
            print("❌ Please choose between 1 and 13!")
    except ValueError:
        print("❌ Enter a valid number!")

computer_card = random.randint(1, 13)

# Animation
shuffle_animation(player_name, player_card)
time.sleep(0.6)
shuffle_animation("Computer", computer_card)
time.sleep(0.5)

# Result
show_result(player_card, computer_card, player_name)

print()