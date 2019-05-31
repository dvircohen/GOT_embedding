from pprint import pprint
from scipy import spatial

from gensim.models import FastText
import pandas as pd
import numpy as np
from gensim import utils
from gensim.utils import SaveLoad

# from embedding.utils import get_char_list, get_adj_from_json

pass

def cosine_similarity(word1, word2):
    cosine_similarity = 1 - spatial.distance.cosine(word1, word2)
    return np.abs(cosine_similarity)


def test_words_similarity(books_model, tv_show_model):
    list_of_words = ['stark', 'dragon', 'jon', 'cersei', 'arya']

    words_triples_list = get_triplets_list()

    for word in list_of_words:
        book_most_similar = books_model.wv.most_similar_cosmul(positive=word)
        tv_most_similar = tv_show_model.wv.most_similar_cosmul(positive=word)
        print("\nWord: {}. \n\tBooks most similar - {} \n\tTV show most similar - {}".format(
            word, [x[0] for x in book_most_similar][:3], [x[0] for x in tv_most_similar][:3]
        ))

    for words_triples in words_triples_list:
        book_most_similar = [x[0] for x in books_model.wv.most_similar_cosmul(positive=[words_triples[1], words_triples[2]],
                                               negative=[words_triples[0]])[:5]]
        tv_most_similar = [x[0] for x in tv_show_model.wv.most_similar_cosmul(positive=[words_triples[1], words_triples[2]],
                                                               negative=[words_triples[0]])[:5]]
        print("\n{} is to {} like {} is to: \n\tBooks - {} \n\tTV show - {}".format(
            words_triples[0], words_triples[1], words_triples[2], book_most_similar, tv_most_similar
        ))



def get_womanly_words(model, adjectives_list, woman_words_list):
    words_embd_dict = {}
    for word in woman_words_list:
        try:
            words_embd_dict[word] = model[word]
        except KeyError:
            pass

    words_embd_df = pd.DataFrame(words_embd_dict).T
    woman_embd = np.array(words_embd_df.mean(axis=0), dtype=np.float32)

    similarity_list = []
    for word in adjectives_list:
        try:
            if model.wv.vocab[word].count < 20:
                continue
            similarity_tuple = (word, cosine_similarity(model[word], woman_embd))
            similarity_list.append(similarity_tuple)
        except KeyError:
            pass
    similarity_list = sorted(similarity_list,key=lambda x: x[1])
    return similarity_list


def get_similart_words_embd(model, source_mame = "Books"):
    woman_words_list, man_words_list = get_man_and_woman_words_list()

    adjectives_list = get_adjectives_list()
    # adjectives_list = list(set(adjectives_list + get_adj_from_json()))

    manly_words = [x[0] for x in get_womanly_words(model, adjectives_list, man_words_list)]
    womanly_words = [x[0] for x in get_womanly_words(model, adjectives_list, woman_words_list)]

    print("\n{}:".format(source_mame))
    print("\nManly adjectives: \n\t{}".format(
        ", ".join(manly_words[:8])
    ))
    print("\nWomanly adjectives: \n\t{}".format(
        ", ".join(womanly_words[:8])
    ))


    return manly_words, womanly_words


if __name__ == '__main__':
    books_model_path = "../data/w2v_models/book_v1_model"
    tv_show_model_path = "../data/w2v_models/tv_show_v1_model"

    books_model = SaveLoad.load(books_model_path)
    tv_show_model = SaveLoad.load(tv_show_model_path)

    test_words_similarity(books_model, tv_show_model)


    books_manly_words, books_womanly_words = get_similart_words_embd(books_model, source_mame='Books')
    tv_manly_words, tv_womanly_words = get_similart_words_embd(tv_show_model, source_mame='TV Show')

    similarity_df = pd.DataFrame([books_manly_words, books_womanly_words, tv_manly_words, tv_womanly_words ]).T
    similarity_df.columns = ['books manly words', 'books womanly words', 'tv manly words', 'tv womanly words']
    similarity_df.to_csv('../data/similarity_tables/manly_and_womanly_words.csv')



