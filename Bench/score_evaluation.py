import os
import json



if __name__ == "__main__":
    
    English_total_score = 0
    Math_1_total_score = 0
    Math_2_total_score = 0
    Chinese_total_score = 0
    Physics_total_score = 0
    Chemistry_total_score = 0
    Biology_total_score = 0
    History_total_score = 0
    Geography_total_score = 0
    Politics_total_score = 0

    English_correct_score = 0
    Math_1_correct_score = 0
    Math_2_correct_score = 0
    Chinese_correct_score = 0
    Physics_correct_score = 0
    Chemistry_correct_score = 0
    Biology_correct_score = 0
    History_correct_score = 0
    Geography_correct_score = 0
    Politics_correct_score = 0

    model_output_dir = "model_output"

    check_length = {"Geography_MCQs":34,
                    "History_MCQs":287,
                    "Chemistry_MCQs":124,
                    "English_Cloze_Test":26,
                    "English_Fill_in_Blanks":30,
                    "Math_II_MCQs":218,
                    "Physics_MCQs":64,
                    "English_MCQs":105,
                    "English_Reading_Comp.":124,
                    "Chinese_Modern_Lit.":29,
                    "Chinese_Lang_and_Usage_MCQs":56,
                    "Political_Science_MCQs":320,
                    "Math_I_MCQs":214,
                    "Biology_MCQs":150}
    # check model_output number
    for filename in os.listdir(model_output_dir):
        for key in check_length:
            if key in filename:
                data = json.load(open(os.path.join(model_output_dir, filename)))
                assert len(data) == check_length[key], "model_output number is not correct, filename:"+filename


    for filename in os.listdir(model_output_dir):
        if "English" in filename:
            data = json.load(open(os.path.join(model_output_dir, filename)))
            for i in data:
                English_total_score += len(i["standard_answer"])*i['score']
                for j in range(len(i["standard_answer"])):
                    if i["model_answer"][j] == i["standard_answer"][j]:
                        English_correct_score += i['score']
        elif "Math_1" in filename:
            data = json.load(open(os.path.join(model_output_dir, filename)))
            for i in data:
                Math_1_total_score += len(i["standard_answer"])*i['score']
                for j in range(len(i["standard_answer"])):
                    if i["model_answer"][j] == i["standard_answer"][j]:
                        Math_1_correct_score += i['score']
        elif "Math_2" in filename:
            data = json.load(open(os.path.join(model_output_dir, filename)))
            for i in data:
                Math_2_total_score += len(i["standard_answer"])*i['score']
                for j in range(len(i["standard_answer"])):
                    if i["model_answer"][j] == i["standard_answer"][j]:
                        Math_2_correct_score += i['score']
        elif "Chinese" in filename:
            data = json.load(open(os.path.join(model_output_dir, filename)))
            for i in data:
                Chinese_total_score += len(i["standard_answer"])*i['score']
                for j in range(len(i["standard_answer"])):
                    if i["model_answer"][j] == i["standard_answer"][j]:
                        Chinese_correct_score += i['score']
        elif "Physics" in filename:
            data = json.load(open(os.path.join(model_output_dir, filename)))
            for i in data:
                Physics_total_score += len(i["standard_answer"])*i['score']
                # Fully correct: 6 points; Partially correct: 3 points; Incorrect: 0 points. 
                for j in range(len(i['model_answer'])):
                            if i['model_answer'][j] == i['standard_answer'][j]:
                                Physics_correct_score += 6
                            else:
                                is_error = 0
                                for z in i['model_answer'][j]:
                                    if z not in i['standard_answer'][j]:
                                        is_error = 1
                                        break
                                Physics_correct_score += 0 if is_error else 3
        elif "Chemistry" in filename:
            data = json.load(open(os.path.join(model_output_dir, filename)))
            for i in data:
                Chemistry_total_score += len(i["standard_answer"])*i['score']
                for j in range(len(i["standard_answer"])):
                    if i["model_answer"][j] == i["standard_answer"][j]:
                        Chemistry_correct_score += i['score']
        elif "Biology" in filename:
            data = json.load(open(os.path.join(model_output_dir, filename)))
            for i in data:
                Biology_total_score += len(i["standard_answer"])*i['score']
                for j in range(len(i["standard_answer"])):
                    if i["model_answer"][j] == i["standard_answer"][j]:
                        Biology_correct_score += i['score']
        elif "History" in filename:
            data = json.load(open(os.path.join(model_output_dir, filename)))
            for i in data:
                History_total_score += len(i["standard_answer"])*i['score']
                for j in range(len(i["standard_answer"])):
                    if i["model_answer"][j] == i["standard_answer"][j]:
                        History_correct_score += i['score']
        elif "Geography" in filename:
            data = json.load(open(os.path.join(model_output_dir, filename)))
            for i in data:
                Geography_total_score += len(i["standard_answer"])*i['score']
                for j in range(len(i["standard_answer"])):
                    if i["model_answer"][j] == i["standard_answer"][j]:
                        Geography_correct_score += i['score']
        elif "Politics" in filename:
            data = json.load(open(os.path.join(model_output_dir, filename)))
            for i in data:
                Politics_total_score += len(i["standard_answer"])*i['score']
                for j in range(len(i["standard_answer"])):
                    if i["model_answer"][j] == i["standard_answer"][j]:
                        Politics_correct_score += i['score']

    # count the total score
    # English: 150 points; Math_1: 150 points; Math_2: 150 points; Chinese: 150 points; Physics: 100 points; Chemistry: 100 points; Biology: 100 points; History: 100 points; Geography: 100 points; Politics: 100 points.
    LIKE_total_score = (English_correct_score/English_total_score)*150 + (Math_1_correct_score/Math_1_total_score)*150 + (Chinese_correct_score/Chinese_total_score)*150 + (Physics_correct_score/Physics_total_score)*100 + (Chemistry_correct_score/Chemistry_total_score)*100 + (Biology_correct_score/Biology_total_score)*100
    WENKE_total_score = (English_correct_score/English_total_score)*150 + (Math_2_correct_score/Math_2_total_score)*150 + (Chinese_correct_score/Chinese_total_score)*150 + (History_correct_score/History_total_score)*100 + (Geography_correct_score/Geography_total_score)*100 + (Politics_correct_score/Politics_total_score)*100
    composite_score = (English_correct_score/English_total_score)*150 + (Math_1_correct_score/Math_1_total_score)*150 + (Math_2_correct_score/Math_2_total_score)*150 + (Chinese_correct_score/Chinese_total_score)*150 + (Physics_correct_score/Physics_total_score)*100 + (Chemistry_correct_score/Chemistry_total_score)*100 + (Biology_correct_score/Biology_total_score)*100 + (History_correct_score/History_total_score)*100 + (Geography_correct_score/Geography_total_score)*100 + (Politics_correct_score/Politics_total_score)*100
