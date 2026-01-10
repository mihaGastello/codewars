geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    return_birds = []

    for bird in birds:
        if bird not in geese:
            return_birds.append(bird)

    return return_birds


def goose_filter2(birds):
    return [bird for bird in birds if bird not in geese]
