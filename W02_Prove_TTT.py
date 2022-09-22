# 9/21/2022
# Make Tic-Tac_Toe
# Shaun Vann
# Can break it intentionally, but it won't break if the rules are followed

def main():
    game_on = True;
    count = 0;

    tiles = ["1","2","3","4","5","6","7","8","9"];

    player_turn = "x";
    end = "";

    while game_on and count <= 9:
        print(f"{tiles[0]} | {tiles[1]} | {tiles[2]}");
        print("--+--+--");
        print(f"{tiles[3]} | {tiles[4]} | {tiles[5]}");
        print("--+--+--");
        print(f"{tiles[6]} | {tiles[7]} | {tiles[8]}");

        square = int(input(f"{player_turn}'s turn to choose a square (1-9): "));
        tiles[square - 1] = player_turn;

        if player_turn == "x":
            player_turn = "o";
        else:
            player_turn = "x";
        
        if tiles[0] == tiles[1] and tiles[1] == tiles[2]:
            if tiles[0] == "x":
                end = "x_victory";
            else:
                end = "o_victory";
        if tiles[3] == tiles[4] and tiles[4] == tiles[5]:
            if tiles[3] == "x":
                end = "x_victory";
            else:
                end = "o_victory";
        if tiles[6] == tiles[7] and tiles[7] == tiles[8]:
            if tiles[6] == "x":
                end = "x_victory";
            else:
                end = "o_victory";
        if tiles[0] == tiles[3] and tiles[3] == tiles[6]:
            if tiles[0] == "x":
                end = "x_victory";
            else:
                end = "o_victory";
        if tiles[1] == tiles[4] and tiles[4] == tiles[7]:
            if tiles[1] == "x":
                end = "x_victory";
            else:
                end = "o_victory";
        if tiles[2] == tiles[5] and tiles[5] == tiles[8]:
            if tiles[2] == "x":
                end = "x_victory";
            else:
                end = "o_victory";
        if tiles[0] == tiles[4] and tiles[4] == tiles[8]:
            if tiles[0] == "x":
                end = "x_victory";
            else:
                end = "o_victory";
        if tiles[2] == tiles[4] and tiles[4] == tiles[6]:
            if tiles[2] == "x":
                end = "x_victory";
            else:
                end = "o_victory";
        
        if end != "" and end == "x_victory":
            game_on = False;
            print("Good game. Thanks for playing!\nX won!");
        elif end != "" and end == "o_victory":
            game_on = False;
            print("Good game. Thanks for playing!\nO won!");
        
        count += 1;

if __name__ == "__main__":
    main();