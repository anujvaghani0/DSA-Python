# import difflib
#
#
# def normalize_string(s):
#     # Remove spaces and convert to lowercase
#     return "".join(s.split()).lower()
#
#
# def calculate_normalized_precision_recall(true_entities, predicted_entities):
#     true_positives = 0
#     false_positives = 0
#     false_negatives = 0
#
#     true_entities_normalized = [normalize_string(entity) for entity in true_entities]
#     predicted_entities_normalized = [normalize_string(entity) for entity in predicted_entities]
#
#     for i in range(len(predicted_entities_normalized)):
#         similarity = difflib.SequenceMatcher(None, true_entities_normalized[i],
#                                              predicted_entities_normalized[i]).ratio()
#         if similarity >= 0.5:  # Set a threshold for similarity
#             true_positives += 1
#         else:
#             false_positives += 1
#
#     false_negatives = len(true_entities) - true_positives
#
#     precision = true_positives / (true_positives + false_positives)
#     recall = true_positives / (true_positives + false_negatives)
#
#     return precision, recall
#
#
#
# # Example usage with normalized entities
# true_entities = ["anuj vaghani","nirmal trivedi","ajay pawar","madhuri bhoyar"]
# predicted_entities = ["anuj vaghani","nirmal tri","pawar","bhoyar kumari"]
#
# precision, recall = calculate_normalized_precision_recall(true_entities, predicted_entities)
# print("Precision:", precision)
# print("Recall:", recall)
#

def pattern(n):
    for i in range(1, n + 1):
        for k in range(1, n - i + 1):
            print(" ", end="")
        for j in range(i, 0, -1):
            print(f"{j}  ", end="")
        for j in range(1, i):
            print(f"{j + 1}  ", end="")

        print(end="\n")


    # pattern(5)

