from hstest.stage_test import StageTest
from hstest.check_result import CheckResult
from hstest import dynamic_test, TestedProgram, WrongAnswer
import os
import shutil

# adapted from the first DuplicateFileHandler test

# dict for creating files
files = {
    'info.txt': {'path': ['root_folder'],
                 'content': 'eed110d0dbd1d89d1ffea807d1d8867'},
    'lost.json': {'path': ['root_folder'],
                  'content': '3a70ac2ebacf4174aa11dfbd1af835bd' * 32},
    'phones.csv': {'path': ['root_folder'],
                   'content': '671ab9fbf94dc377568fb7b2928960c9' * 3},
    'python.txt': {'path': ['root_folder'],
                   'content': 'd2c2ee4cbb368731f1a5399015160d7d' * 2},
    'bikeshare.csv': {'path': ['root_folder', 'calc'],
                      'content': 'c03285172453d7278a85a5db4d06423c' * 7},
    'server.php': {'path': ['root_folder', 'calc'],
                   'content': 'a5c662fe853b7ab48d68532791a86367' * 64},
    'db_cities.js': {'path': ['root_folder', 'files'],
                     'content': 'f2e5cf58ae9b2d2fd0ae9bf8fa1774da'},
    'some_text.txt': {'path': ['root_folder', 'files'],
                      'content': 'd2c2ee4cbb368731f1a5399015160d7d'},
    'cars.json': {'path': ['root_folder', 'files', 'stage'],
                  'content': '3a70ac2ebacf4174aa11dfbd1af835bd' * 89},
    'package-lock.json': {'path': ['root_folder', 'files', 'stage'],
                          'content': 'eebf1c62a13284ea1bcfe53820e83f11'},
    'index.js': {'path': ['root_folder', 'files', 'stage', 'src'],
                 'content': '797ac79aa6a3c2ef733fecbaff5a655f' * 2},
    'libs.txt': {'path': ['root_folder', 'files', 'stage', 'src'],
                 'content': '4909fd0404ac7ebe1fb0c50447975a2a'},
    'reviewslider.js': {'path': ['root_folder', 'files', 'stage', 'src'],
                        'content': 'abc96a9b62c4701f27cf7c8dbd484fdc' * 33},
    'spoiler.js': {'path': ['root_folder', 'files', 'stage', 'src'],
                   'content': 'b614ccac263d3d78b60b37bf35e860f3' * 4},
    'src.txt': {'path': ['root_folder', 'files', 'stage', 'src'],
                'content': 'eed110d0dbd1d89d1ffea807d1d88679' * 5},
    'toggleminimenu.js': {'path': ['root_folder', 'files', 'stage', 'src'],
                          'content': '7eceb7dd5a0daaccc32739e1dcc6c3b0'},
    'extraversion.csv': {'path': ['root_folder', 'project'],
                         'content': 'fc88cf4d79437fa06e6cfdd80bd0eed2' * 8},
    'index.html': {'path': ['root_folder', 'project'],
                   'content': '3f0f7b61205b863d2051845037541835'},
    'python_copy.txt': {'path': ['root_folder', 'project'],
                        'content': 'd2c2ee4cbb368731f1a5399015160d7d' * 1}
}


root_dir_path = os.path.join('module', 'root_folder')


def create_files(path):
    # delete root_folder
    if os.path.isdir(path):
        shutil.rmtree(path)

    # create files
    for key, dict_val in files.items():
        path = os.path.join('module', *dict_val['path'])
        if not os.path.isdir(path):
            os.makedirs(path)
        file_path = os.path.join(path, key)
        with open(file_path, 'a+') as f:
            f.write(dict_val['content'])


class FileManagerTest(StageTest):

    @dynamic_test()
    def test1(self):
        x = 'ls'
        expected_result_list = ['calc',
                                'files',
                                'project',
                                'info.txt',
                                'lost.json',
                                'phones.csv',
                                'python.txt']
        pr = TestedProgram()
        pr.start()
        output = pr.execute(stdin=x)
        if not output:
            raise WrongAnswer('Your program did not print anything.')
        subs_before_files_check = 0
        for i in output.split():
            if '.' not in i:
                if subs_before_files_check == 0:
                    continue
                else:
                    raise WrongAnswer('Please print all subdirectories before printing files.')
            else:
                subs_before_files_check = 1  # a file extension has been printed
        output_cleaned = output.lower().strip().replace(' ', '')
        check = all(n in output_cleaned for n in expected_result_list)
        return CheckResult(check, f'Wrong message returned. \nInput message: {x} \nYou printed: {output} \nWe expected the contents of root_folder: 3 directories and 4 files.')

    @dynamic_test()
    def test2(self):
        x = 'cd files\nls\nrm'
        expected_result_list = ['Specify the file or directory']
        pr = TestedProgram()
        pr.start()
        output = pr.execute(stdin=x)
        if not output:
            raise WrongAnswer('Your program did not print anything.')
        output_cleaned = output.lower().strip().replace(' ', '')
        expected_results_cleaned = [s.lower().strip().replace(' ', '') for s in expected_result_list]
        check = all(n in output_cleaned for n in expected_results_cleaned)
        return CheckResult(check, f'Wrong message returned. \nInput message: {x} \nYou printed: {output} \nWe expected {expected_result_list}')

    @dynamic_test()
    def test3(self):
        x = 'cd files\nls\nrm'
        expected_result_list = ['Specify the file or directory']
        pr = TestedProgram()
        pr.start()
        output = pr.execute(stdin=x)
        if not output:
            raise WrongAnswer('Your program did not print anything.')
        output_cleaned = output.lower().strip().replace(' ', '')
        expected_results_cleaned = [s.lower().strip().replace(' ', '') for s in expected_result_list]
        check = all(n in output_cleaned for n in expected_results_cleaned)
        return CheckResult(check, f'Wrong message returned. \nInput message: {x} \nYou printed: {output} \nWe expected {expected_result_list}')

    @dynamic_test()
    def test4(self):
        x = 'cd files\nls\nrm ouhoip'
        expected_result_list = ['No such file or directory']
        pr = TestedProgram()
        pr.start()
        output = pr.execute(stdin=x)
        if not output:
            raise WrongAnswer('Your program did not print anything.')
        output_cleaned = output.lower().strip().replace(' ', '')
        expected_results_cleaned = [s.lower().strip().replace(' ', '') for s in expected_result_list]
        check = all(n in output_cleaned for n in expected_results_cleaned)
        return CheckResult(check, f'Wrong message returned. \nInput message: {x} \nYou printed: {output} \nWe expected {expected_result_list}')

    @dynamic_test()
    def test5(self):
        x = 'cd files\nls\nrm stage\nrm some_text.txt\nls'
        expected_removals_list = ['stage',
                                  'some_text.txt']
        pr = TestedProgram()
        pr.start()
        output = pr.execute(stdin=x)
        if not output:
            raise WrongAnswer('Your program did not print anything.')
        output_cleaned = output.lower().strip().replace(' ', '')
        expected_removals_cleaned = [s.lower().strip().replace(' ', '') for s in expected_removals_list]
        check = all(n not in output_cleaned[-1] for n in expected_removals_cleaned)
        return CheckResult(check, f'Wrong message returned. \nInput message: {x} \nYou printed: {output} \nWe expected the removal of {expected_removals_list}')

    @dynamic_test()
    def test6(self):
        x = 'mv'
        expected_result_list = ['Specify the current name of the file or directory and the new name']
        pr = TestedProgram()
        pr.start()
        output = pr.execute(stdin=x)
        if not output:
            raise WrongAnswer('Your program did not print anything.')
        output_cleaned = output.lower().strip().replace(' ', '')
        expected_results_cleaned = [s.lower().strip().replace(' ', '') for s in expected_result_list]
        check = all(n in output_cleaned for n in expected_results_cleaned)
        return CheckResult(check, f'Wrong message returned. \nInput message: {x} \nYou printed: {output} \nWe expected {expected_result_list}')

    @dynamic_test()
    def test7(self):
        x = 'cd files\nls\nmv pork bork'
        expected_result_list = ['No such file or directory']
        pr = TestedProgram()
        pr.start()
        output = pr.execute(stdin=x)
        if not output:
            raise WrongAnswer('Your program did not print anything.')
        output_cleaned = output.lower().strip().replace(' ', '')
        expected_results_cleaned = [s.lower().strip().replace(' ', '') for s in expected_result_list]
        check = all(n in output_cleaned for n in expected_results_cleaned)
        return CheckResult(check, f'Wrong message returned. \nInput message: {x} \nYou printed: {output} \nWe expected {expected_result_list}')

    @dynamic_test()
    def test8(self):
        x = 'cd files\nls\nmv flower'
        expected_result_list = ['Specify the current name of the file or directory and the new name']
        pr = TestedProgram()
        pr.start()
        output = pr.execute(stdin=x)
        if not output:
            raise WrongAnswer('Your program did not print anything.')
        output_cleaned = output.lower().strip().replace(' ', '')
        expected_results_cleaned = [s.lower().strip().replace(' ', '') for s in expected_result_list]
        check = all(n in output_cleaned for n in expected_results_cleaned)
        return CheckResult(check, f'Wrong message returned. \nInput message: {x} \nYou printed: {output} \nWe expected {expected_result_list}')

    @dynamic_test()
    def test9(self):
        x = 'cd project\nls\nmv extraversion.csv index.html'
        expected_result_list = ['The file or directory already exists']
        pr = TestedProgram()
        pr.start()
        output = pr.execute(stdin=x)
        if not output:
            raise WrongAnswer('Your program did not print anything.')
        output_cleaned = output.lower().strip().replace(' ', '')
        expected_results_cleaned = [s.lower().strip().replace(' ', '') for s in expected_result_list]
        check = all(n in output_cleaned for n in expected_results_cleaned)
        return CheckResult(check, f'Wrong message returned. \nInput message: {x} \nYou printed: {output} \nWe expected {expected_result_list}')

    @dynamic_test()
    def test10(self):
        x = 'cd files\nls\nmv db_cities.js db_skylines.js\nmkdir stage\nmv stage stages\nmv stages stag\nls'
        expected_result_list = ['stag', 'db_skylines.js']
        pr = TestedProgram()
        pr.start()
        output = pr.execute(stdin=x)
        if not output:
            raise WrongAnswer('Your program did not print anything.')
        output_cleaned = output.lower().strip().replace(' ', '')
        expected_results_cleaned = [s.lower().strip().replace(' ', '') for s in expected_result_list]
        check = all(n in output_cleaned for n in expected_results_cleaned)
        return CheckResult(check, f'Wrong message returned. \nInput message: {x} \nYou printed: {output} \nWe expected {expected_result_list}')

    @dynamic_test()
    def test11(self):
        x = 'cd files\nls\nmkdir'
        expected_result_list = ['Specify the name of the directory to be made']
        pr = TestedProgram()
        pr.start()
        output = pr.execute(stdin=x)
        if not output:
            raise WrongAnswer('Your program did not print anything.')
        output_cleaned = output.lower().strip().replace(' ', '')
        expected_results_cleaned = [s.lower().strip().replace(' ', '') for s in expected_result_list]
        check = all(n in output_cleaned for n in expected_results_cleaned)
        return CheckResult(check, f'Wrong message returned. \nInput message: {x} \nYou printed: {output} \nWe expected {expected_result_list}')

    @dynamic_test()
    def test12(self):
        x = 'cd files\nmkdir stage\nmkdir stage'
        expected_result_list = ['The directory already exists']
        pr = TestedProgram()
        pr.start()
        output = pr.execute(stdin=x)
        if not output:
            raise WrongAnswer('Your program did not print anything.')
        output_cleaned = output.lower().strip().replace(' ', '')
        expected_results_cleaned = [s.lower().strip().replace(' ', '') for s in expected_result_list]
        check = all(n in output_cleaned for n in expected_results_cleaned)
        return CheckResult(check, f'Wrong message returned. \nInput message: {x} \nYou printed: {output} \nWe expected {expected_result_list}')

    @dynamic_test()
    def test13(self):
        x = 'cd files\nls\nmkdir flower\ncd flower\nmkdir nectar\nmkdir stamen\nmkdir pollen\nmkdir smells\nls'
        expected_result_list = ['nectar',
                                'stamen',
                                'smells',
                                'pollen']
        pr = TestedProgram()
        pr.start()
        output = pr.execute(stdin=x)
        if not output:
            raise WrongAnswer('Your program did not print anything.')
        output_cleaned = output.lower().strip().replace(' ', '')
        expected_results_cleaned = [s.lower().strip().replace(' ', '') for s in expected_result_list]
        check = all(n in output_cleaned for n in expected_results_cleaned)
        return CheckResult(check, f'Wrong message returned. \nInput message: {x} \nYou printed: {output} \nWe expected {expected_result_list}')

    def after_all_tests(self):
        try:
            create_files(root_dir_path)
        except Exception as ignored:
            pass

    def generate(self):
        try:
            create_files(root_dir_path)
        except Exception as ignored:
            pass
        return []


if __name__ == '__main__':
    FileManagerTest().run_tests()
