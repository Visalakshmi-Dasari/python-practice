class Password_manager():
    old_passwords=['xyz','abc','ABC','123']
    def get_password(self):
        return self.old_passwords[-1]

    def set_password(self,new_password):

        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return 'password created'
        else:
            raise Exception('Your new password matched with old passwords. Password not created')

    def is_correct(self,string):
        if string==self.old_passwords[-1]:
            return True
        else:
            return False





test=Password_manager()
print test.old_passwords
print test.get_password()
print test.set_password('abc')
print test.is_correct('vishdee')
print test.old_passwords
