try_dict ={'a': False,
                                   'b': False,
                                   'background': {'age': 12,
                                                  'congenital_disease': 'None',
                                                  'gentic_disease': 'None',
                                                  'response': '1歲啊。\n'
                                                              '那麼孩子出生時是否足月呢？',
                                                  'ten_month': 'None',
                                                  'weight': 'None'},
                                   'behavior': {'q1': 'None',
                                                'q10': 'None',
                                                'q11': 'None',
                                                'q12': 'None',
                                                'q13': 'None',
                                                'q2': 'None',
                                                'q3': 'None',
                                                'q4': 'None',
                                                'q5': 'None',
                                                'q6': 'None',
                                                'q7': 'None',
                                                'q8': 'None',
                                                'q9': 'None'},
                                   'c': False,
                                   'environment': {'3c': 'None',
                                                   'school': 'None'},
                                   'latestQuest': '',
                                   'response': []
                                   }

def get_key_from_value(dict, val):
    resultList = []
    for key, value in dict.items():
        if val == value:
            resultList.append(key)
    return resultList 

waiting_question = get_key_from_value(try_dict["background"], "None")
print(len(waiting_question))