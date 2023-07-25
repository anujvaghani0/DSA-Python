import difflib


def normalize_string(s):
    # Remove spaces and convert to lowercase
    return "".join(s.split()).lower()


def calculate_normalized_precision_recall(true_entities, predicted_entities):
    true_positives = 0
    false_positives = 0
    false_negatives = 0

    true_entities_normalized = [normalize_string(entity) for entity in true_entities]
    predicted_entities_normalized = [normalize_string(entity) for entity in predicted_entities]

    for i in range(len(predicted_entities_normalized)):
        similarity = difflib.SequenceMatcher(None, true_entities_normalized[i],
                                             predicted_entities_normalized[i]).ratio()
        if similarity >= 0.5:  # Set a threshold for similarity
            true_positives += 1
        else:
            false_positives += 1

    false_negatives = len(true_entities) - true_positives

    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)

    return precision, recall


# Example usage with normalized entities
true_entities = ["'soumyakanta6@gmail.com"]
predicted_entities = ["Guru@Work', 'soumyakanta6@gmail.com"]

precision, recall = calculate_normalized_precision_recall(true_entities, predicted_entities)
print("Precision:", precision)
print("Recall:", recall)

