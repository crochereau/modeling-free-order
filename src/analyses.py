import numpy as np

from utils import pickle_load

from experiments import RESULTS_PATHS


def relative_test(gram_probs, ungram_probs, nb_sentences):
    """

    Args:
        probs: np.array containing per-sentence probabilities

    Returns:

    """
    stc_gram_probs = np.array([gram_probs[x:x + 36] for x in range(0, len(gram_probs), 36)])
    print(stc_gram_probs.size, stc_gram_probs[0].size)
    stc_ungram_probs = np.array([ungram_probs[x:x + 108] for x in range(0, len(ungram_probs), 108)])
    print(stc_ungram_probs.size, stc_ungram_probs[0].size)
    case_violations = np.array([[stc_ungram_probs[stc][x:x + 36] for x in range(0, len(stc_ungram_probs[stc]), 36)]
                                for stc in range(len(stc_ungram_probs))])
    print(case_violations.size, case_violations[0].size)

    stc_gram_sums = []
    for stc_idx in range(nb_sentences):
        tmp_sum = sum(stc_gram_probs[stc_idx])
        stc_gram_sums.append(tmp_sum)

    case_violations_sums = [[] for _ in range(nb_sentences)]
    for stc_idx in range(nb_sentences):
        for case_violation_idx in range(3):
            tmp_sum = sum(case_violations[stc_idx][case_violation_idx])
            # print(tmp_sum)
            case_violations_sums[stc_idx].append(tmp_sum)

    indicators = [[] for _ in range(nb_sentences)]
    for stc_idx in range(nb_sentences):
        for case_violation_idx in range(3):
            tmp_diff = stc_gram_sums[stc_idx] - case_violations_sums[stc_idx][case_violation_idx]
            tmp_indicator = 1 if tmp_diff > 0 else 0
            indicators[stc_idx].append(tmp_indicator)

    accuracy_nom_violation, accuracy_acc_violation, accuracy_dat_violation = 0, 0, 0
    for stc_idx in range(len(indicators)):
        accuracy_nom_violation += indicators[stc_idx][0]
        accuracy_acc_violation += indicators[stc_idx][1]
        accuracy_dat_violation += indicators[stc_idx][2]
    accuracy_nom_violation = accuracy_nom_violation / nb_sentences
    accuracy_acc_violation = accuracy_acc_violation / nb_sentences
    accuracy_dat_violation = accuracy_dat_violation / nb_sentences

    relative_results = [accuracy_nom_violation, accuracy_acc_violation, accuracy_dat_violation]

    return relative_results


def absolute_test(probs):
    return absolute_results


def normalized_relative_test(probs):
    return normalized_relative_results


def main():
    # FIXME: temporary comments
    # grammatical_probs = pickle_load(RESULTS_PATHS["3_args_masc_grammatical"])
    # ungrammatical_probs = pickle_load(RESULTS_PATHS["3_args_masc_ungrammatical"])

    grammatical_probs = pickle_load("results/model2_gram_probs.txt")
    ungrammatical_probs = pickle_load("results/model2_ungram_probs.txt")
    sentences_nb = int(len(grammatical_probs)/36)

    relative_accuracies = relative_test(grammatical_probs, ungrammatical_probs, sentences_nb)
    print(relative_accuracies)

    return relative_accuracies


if __name__ == "__main__":
    main()