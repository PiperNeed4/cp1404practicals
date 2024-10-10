from prac_01.broken_score import score


def main():
    choice = input(f"(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit").upper()
    if choice == "G":
        score = get_valid_score()
    elif choice == "P":
        print_result(score)
    elif choice == "S":
        show_stars(score)


def get_valid_score():
    score = int(input("Enter score from 0-100: "))
    while score < 0 or score > 100:
        print("Invalid score")
    return score


def print_result(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def show_stars(score):
    print("*" * score)


main()
