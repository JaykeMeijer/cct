from cars.parts.body.options.option import Body_option


class Body_option_spoiler(Body_option):
    identifier = 'body.option.spoiler'

    def __init__(self):
        print("Spoiler initialized")


mainclass = Body_option_spoiler
