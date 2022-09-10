class CheckView:
    def get_user_entry(
        self,
        message_display,
        message_error,
        value_type,
        default_value=None,
        user_entry=None,
    ):
        """Création du classe qui permet de gérer les affichage des message
        et la vérification des informations saisi par l'utilisateur"""

        while True:
            value = input(message_display)
            if value_type == "numeric":
                if value.isnumeric():
                    value = int(value)
                    return value
                else:

                    print(message_error)
                    continue

            if value_type == "number_superior":
                if value.isnumeric():
                    value = int(value)
                    if value >= default_value:
                        return value

                    else:
                        print(message_error)
                        continue
            if value_type == "string":
                try:
                    float(value)
                    print(message_error)
                    continue
                except ValueError:
                    return value

            elif value_type == "date":
                if self.verify_date(value):
                    return value
                else:
                    print(message_error)
                    continue
            elif value_type == "selection":
                if value in user_entry:
                    return value
                else:
                    print(message_error)
                    continue

    @staticmethod
    def verify_date(value_to_test):
        if "-" not in value_to_test:
            return False
        else:
            splitted_date = value_to_test.split("-")
            for date in splitted_date:
                if not date.isnumeric():
                    return False
            return True

    @staticmethod
    def build_selection(iterable: list, display_message: str, user_entry: list) -> dict:
        display_message = display_message
        user_entry = user_entry

        for i, data in enumerate(iterable):
            display_message = display_message + f"{i+1} - {data['name']}\n"
            user_entry.append(str(i + 1))

        return {"message": display_message, "user_entry": user_entry}
