from utils import SCORES_FILE_NAME

def add_score(difficulty):
    total = 0
    scores_file = open(SCORES_FILE_NAME, "a+")
    scores_file.seek(0)
    current_score = scores_file.read()

    if not current_score:
        points_of_winning = (difficulty * 3) + 5
        scores_file.write(str(points_of_winning))
        scores_file.close()

    else:
        points_of_winning = (difficulty * 3) + 5
        write_file = open(SCORES_FILE_NAME, "w")
        num = int(current_score)
        total = num+points_of_winning
        write_file.write(str(total))
        write_file.close()

    scores_file.close()



