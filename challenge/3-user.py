#!/usr/bin/python3

class User:
    """
    Classe représentant un utilisateur avec un nom et un mot de passe.
    """

    def __init__(self, name, password):
        """
        Initialise une nouvelle instance de User.

        Args:
            name (str): Le nom de l'utilisateur.
            password (str): Le mot de passe associé à l'utilisateur.
        """
        self.name = name
        self.password = password

    def is_valid_password(self, input_password):
        """
        Vérifie si le mot de passe donné correspond au mot de passe de l'utilisateur.

        Args:
            input_password (str): Le mot de passe à vérifier.

        Returns:
            bool: True si le mot de passe correspond, False sinon.
        """
        return self.password == input_password

if __name__ == "__main__":
    u = User("Test User", "correct_password")
    print(u.name)
    # Vérification des mots de passe
    assert u.is_valid_password("correct_password") == True
    assert u.is_valid_password("wrong_password") == False
