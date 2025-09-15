import games

com_choice = games.get_com_num()

human_choice = games.get_human_num()

games.check_winner(com_choice, human_choice)