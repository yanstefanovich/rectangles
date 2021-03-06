import test_data
from src.containment import containment

print('Testing containment')
print('Should pass containment between rec_1 and rec_4')
print(containment(test_data.rec_1, test_data.rec_4))
print('Should pass containment between rec_1 and rec_5')
print(containment(test_data.rec_1, test_data.rec_5))
print('Should pass containment between rec_2 and rec_4')
print(containment(test_data.rec_2, test_data.rec_4))
print('Should pass containment between rec_2 and rec_5')
print(containment(test_data.rec_2, test_data.rec_5))
print('Should pass containment between rec_3 and rec_4')
print(containment(test_data.rec_3, test_data.rec_4))
print('Should pass containment between rec_3 and rec_5')
print(containment(test_data.rec_3, test_data.rec_5))
print('Should not pass containment between rec_4 and rec_5')
print(containment(test_data.rec_4, test_data.rec_5))
print('Should not pass containment between rec_1 and rec_2')
print(containment(test_data.rec_1, test_data.rec_2))
print('Should not pass containment between rec_1 and rec_3')
print(containment(test_data.rec_1, test_data.rec_3))
print('Should not pass containment between rec_3 and rec_2')
print(containment(test_data.rec_3, test_data.rec_2))