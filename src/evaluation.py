from rouge import Rouge

class Evaluation:
    def __init__(self):
        self.rouge = Rouge()

    def evaluate(self, generated_summary, reference_summary):
        scores = self.rouge.get_scores(generated_summary, reference_summary)
        return scores
