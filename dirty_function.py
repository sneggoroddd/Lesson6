import  random


def random_famous(famous, count =2):
    '''
    недетерминированая функция

    :param famos:список людей
    :param count:количество
    :return:возвращает случайных людей
    '''
    return random.sample(famous, count)