import json
import glob

def print_scores(dirname):
    scores = {}
    for filename in glob.glob(f"{dirname}/*.json"):
        scores[filename] = {}

        with open(filename,"r",encoding="utf-8") as infile:
            for result in json.load(infile):
                for subject, score in result.items():
                    scores[filename].setdefault(subject,[])
                    scores[filename][subject].append(score)

    for one_class in scores:
        print(one_class)
        for subject, subject_scores in scores[one_class].items():
            min_score = min(subject_scores)
            max_score = max(subject_scores)
            average_score = (sum(subject_scores) / len(subject_scores))

            print(subject)
            print(min_score)
            print(max_score)
            print(average_score)

if __name__ == "__main__" :
    print_scores("/Users/kyu-deokkim/Downloads/scores")