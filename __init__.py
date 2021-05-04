from mycroft import MycroftSkill, intent_file_handler


class ErzaehlMirWas(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('was.mir.erzaehl.intent')
    def handle_was_mir_erzaehl(self, message):
        self.speak_dialog('was.mir.erzaehl')


def create_skill():
    return ErzaehlMirWas()

