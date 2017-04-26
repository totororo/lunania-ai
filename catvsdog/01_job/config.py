from os.path import join as join_path
import os


abspath = os.path.dirname(os.path.abspath(__file__))
lock_file = os.path.join(abspath, 'lock')
data_dir = join_path(abspath, '..', '99_data')
train_dir = join_path(data_dir, 'train')
validation_dir = join_path(data_dir, 'validation')
result_dir = join_path(abspath, '..', '90_result')

syserr = 'S001'
inputerr = 'B001'
