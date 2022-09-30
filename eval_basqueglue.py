import json
from argparse import ArgumentParser
from datasets import load_metric

###USAGE 

#python3 eval_basqueglue.py  \
#        --task [nerc_id | nerc_od | intent | slot | bhtc | bec | vaxx | qnli | wic | coref] \
#        --pred prediction_file.jsonl \
#        --ref reference_file.jsonl #(usually test.jsonl)

token_tasks = ["slot", "nerc_id", "nerc_od"]
text_tasks = ["intent", "bhtc", "bec", "qnli", "vaxx"]
span_tasks = ["wic", "coref"]

parser = ArgumentParser()
parser.add_argument("-t", "--task", dest="task",
                    help="task from BasqueGLUE to eval (nerc_id, nerc_od, slot, intent, bhtc, bec, qnli, vaxx, wic, coref)", metavar="TASK")
parser.add_argument("-p", "--pred", dest="pred_file",
                    help="path to prediction file", metavar="PRED")
parser.add_argument("-r", "--ref", dest="ref_file",
                    help="path to reference file", metavar="REF")

args = parser.parse_args()
variables = vars(args)



task = variables["task"]
print(f"TASK: {task}")

if task in token_tasks:
	task_type = "token"

elif task in text_tasks:
	task_type = "text"

elif task in span_tasks:
	task_type = "span"

else:
    print("TASK NOT FOUND: Choose a task with --task (nerc_id, nerc_od, slot, intent, bhtc, bec, qnli, vaxx, wic, coref) \n")
    print("USAGE: python3 eval_basqueglue.py --task [task] --pred prediction_file.jsonl --ref reference_file.jsonl\n")

    task_type = "?"

print(f"Task type: {task_type} classification\n")



GLUEus_path = "."
pred_path = "."

ref_file = f"{GLUEus_path}/{task}/test.jsonl"
pred_file = f"{pred_path}/{task}/pred.jsonl"


if variables["ref_file"] and variables["pred_file"]:
    ref_file = variables["ref_file"]
    pred_file = variables["pred_file"]
else:
	print("ref_file or pred_file MISSING!\n")
	print("USAGE: python3 eval_basqueglue.py --task [task] --pred prediction_file.jsonl --ref reference_file.jsonl\n")



print(f"Reference file: {ref_file}")
print(f"Prediction file: {pred_file}")



def read_token_tags(file):

    with open(file, "r") as json_file: 
        json_list = list(json_file)

        tags = []

        for json_str in json_list:
            tags.append(json.loads(json_str)["tags"])

    return tags



def read_text_labels(file):

    with open(file, "r") as json_file: 
        json_list = list(json_file)

        labels = []

        for json_str in json_list:
            labels.append(json.loads(json_str)["label"])

    return labels



def label2int_dict(labels):

    l2i_dict = {}
    n = 0

    for label in labels:

        if label not in l2i_dict:

            l2i_dict[label] = n
            n += 1

    return l2i_dict




print(f"### RESULTS ###")

if task_type in ["text", "span"] :

	references = read_text_labels(ref_file)
	predictions = read_text_labels(pred_file)

	l2i_dict = label2int_dict(references+predictions)

	print(l2i_dict)

	references = [l2i_dict[r] for r in references]
	predictions = [l2i_dict[p] for p in predictions]

	labels = list(set(references+predictions))

	accuracy_metric = load_metric("accuracy")
	f1_metric = load_metric("f1")

	acc = accuracy_metric.compute(references=references, predictions=predictions)
	print(f"Acc: {acc}")


	f1_macro = f1_metric.compute(references=references, predictions=predictions, average="macro")
	f1_micro = f1_metric.compute(references=references, predictions=predictions, average="micro")

	print(f"F1 Macro: {f1_macro}")
	print(f"F1 micro: {f1_micro}")

	if task == "vaxx":
		f1_class = f1_metric.compute(references=references, predictions=predictions, average=None)["f1"]
		print(f"F1 for each class: {f1_class}")
		#f1_class = f1_metric.compute(references=references, predictions=predictions, labels=[1, 2], average=None)[f1]
		f1_vaxx =  (f1_class[1]+f1_class[2])/2
		print(f"F1 vaxx: {f1_vaxx}            #(avg F1 FAVOR & AGAINST)")

elif task_type == "token":

	references = read_token_tags(ref_file)
	predictions = read_token_tags(pred_file)


	metric = load_metric("seqeval")
	results = metric.compute(predictions=predictions, references=references)
	print(results)

	#https://github.com/huggingface/datasets/blob/master/metrics/glue/glue.py
