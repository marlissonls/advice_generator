from app.app import Advice

def main() -> None:
    """ Gets a new advice from an advice API, prints it and writes the advice to a json file. """

    advice = Advice()
    print(advice, end="\n\n")

    advice.write_advice()
    
    print(Advice.show_old_advices())

if __name__ == '__main__':
    main()