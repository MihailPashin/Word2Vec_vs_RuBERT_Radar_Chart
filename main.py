from Word2Vec.distributive_semantics import word2vec
from messages.textSystem import TextContactSystem
from messages.owlSystem import OwlContactSystem
from messages.utils import send_mass_messages


if __name__ == "__main__" :
    # Our main program.
    alice = User("Alice", TextContactSystem("0102030405"))
    bob = User("Bob", OwlContactSystem("4 Privet Drive"))

    user_list = [alice, bob]
    send_mass_messages("Hello {name}, Comment vas-tu?", user_list)
    send_mass_messages(
        "Salut {name}. Tes informations de contact sont-elles corrects?"
        " Nous avons celles-ci: {contact_info}.",
        user_list,
    )
    word2vec_fast = word2vec('kostroma_word2vec',)
