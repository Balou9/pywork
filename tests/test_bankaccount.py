import pytest
from bankaccount import BankAccount 

a1 = BankAccount()
a1.set_details('Mike', 200)

def test_account_get_details():  
    assert a1.display() == 'Mike 200'

# a2 = BankAccount()
# a2.set_details('Tom')
 
# a1.display()
# a2.display()
 
# a1.withdraw(100)
# a2.deposit(500)
 
# a1.display()
# a2.display()