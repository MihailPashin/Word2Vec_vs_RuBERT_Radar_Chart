import pandas
import gensim
class word2vec:
    """Un utilisateur."""
    TOKEN_RE = re.compile(r'[\w\d]+')
    def __init__(self, name: str):
        """Initialise un nom et une methode de contact."""
        self.name = name


    def creating_word2vec_model():
      train_tokens = tokenize_corpus(full_dataset)
      kostroma_word2vec = gensim.models.Word2Vec(sentences=train_tokens, vector_size=30,
                                      window=4, min_count=5, workers=6,
                                      sg=2, epochs=20)
      return kostroma_word2vec

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Переименуйте модель")
        else:
            self.__name = value

    def tokenize_text_simple_regex(txt, min_token_size=4):
        #print(txt)
        txt = txt.lower()
        all_tokens = TOKEN_RE.findall(txt)
        return [token for token in all_tokens if len(token) >= min_token_size]

    def character_tokenize(txt):
        return list(txt)

    def tokenize_corpus(texts, tokenizer=tokenize_text_simple_regex, **tokenizer_kwargs):
        #print(texts)
        return [tokenizer(text, **tokenizer_kwargs) for text in texts]
    def build_vocabulary(tokenized_texts, max_size=50000, max_doc_freq=0.89, min_count=5, pad_word=None):
        word_counts = collections.defaultdict(int)
        doc_n = 0

        # посчитать количество документов, в которых употребляется каждое слово
        # а также общее количество документов
        for txt in tokenized_texts:
            doc_n += 1
            unique_text_tokens = set(txt)
            for token in unique_text_tokens:
                word_counts[token] += 1

        # убрать слишком редкие и слишком частые слова
        word_counts = {word: cnt for word, cnt in word_counts.items()
                       if cnt >= min_count and cnt / doc_n <= max_doc_freq}

        # отсортировать слова по убыванию частоты
        sorted_word_counts = sorted(word_counts.items(),
                                    reverse=True,
                                    key=lambda pair: pair[1])

        # добавим несуществующее слово с индексом 0 для удобства пакетной обработки
        if pad_word is not None:
            sorted_word_counts = [(pad_word, 0)] + sorted_word_counts

        # если у нас по прежнему слишком много слов, оставить только max_size самых частотных
        if len(word_counts) > max_size:
            sorted_word_counts = sorted_word_counts[:max_size]

        # нумеруем слова
        word2id = {word: i for i, (word, _) in enumerate(sorted_word_counts)}

        # нормируем частоты слов
        word2freq = np.array([cnt / doc_n for _, cnt in sorted_word_counts], dtype='float32')

        return word2id, word2freq


PAD_TOKEN = '__PAD__'
NUMERIC_TOKEN = '__NUMBER__'
NUMERIC_RE = re.compile(r'^([0-9.,e+\-]+|[mcxvi]+)$', re.I)
