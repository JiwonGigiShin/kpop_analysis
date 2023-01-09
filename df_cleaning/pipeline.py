from sklearn.pipeline import Pipeline

import preprocessing

def set_pipeline():
    '''
    create pipeline for preprocessing
    '''
    blocks = {
            'lowercase': ('lowercase', preprocessing.LowerCase()),
            'regex': ('regex', preprocessing.RegexRemover()),
            'numbers': ('numbers', preprocessing.NumRemover()),
            'punctuation': ('punctuation', preprocessing.PuncRemover()),
            'lemmatizer': ('lemmatizer', preprocessing.Lemmatizer()),
            'remove_words': ('WordRemover', preprocessing.WordRemover()),
            'split_words': ('split_words', preprocessing.WordSplitter())
        }

    incl_blocks = [blocks[bloc] for bloc in blocks]

    pipe = Pipeline(incl_blocks)

    return pipe
