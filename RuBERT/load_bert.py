from sentence_transformers import SentenceTransformer
from txtai.embeddings import Embeddings
from txtai import graph
from sklearn.metrics.pairwise import cosine_similarity

class ruBERT:
    def __init__(self, model_path="sergeyzh/rubert-mini-sts", content=True, functions=None, expressions=None):
        self.model_path = model_path
        self.content = content
        self.functions = [{"name": "graph", "function": "graph.attribute"},]
        self.expressions = [{"name": "category", "expression": "graph(indexid, 'category')"},
{"name": "topic", "expression": "graph(indexid, 'topic')"},]
        self.embeddings = Embeddings(path=self.model_path, content=self.content, functions=self.functions, expressions=self.expressions)


    def get_sentence_embeddings(self, sentences):
        if self.embeddings is None:
            self.load_embeddings()
        return self.embeddings.embed(sentences)

    def calculate_similarity(self, sentence1, sentence2):
        if self.embeddings is None:
            self.load_embeddings()
        emb1 = self.embeddings.embed([sentence1])[0]
        emb2 = self.embeddings.embed([sentence2])[0]
        return cosine_similarity([emb1], [emb2])[0][0]


