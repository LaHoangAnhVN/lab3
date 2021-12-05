import yaml
from tqdm import tqdm
import argparse


def sort_by(ls: list, name: str) -> list:
    new_list = []
    n = len(ls)
    for i in range(n):
        new_list.append(ls[i])
    gap = int(n // 2)

    while gap > 0:
        for i in range(gap, n):
            tmp = new_list[i][name]
            cop = new_list[i]
            j = i
            while j >= gap and new_list[j - gap][name] > tmp:
                new_list[j] = new_list[j - gap]
                j -= gap

            new_list[j] = cop
        gap = gap // 2
    return new_list


class ReadFile:
    path: str

    def __init__(self, p: str) -> None:
        self.path = p

    def read_file(self) -> list:
        tmp = []
        with open(self.path, 'r') as f:
            result = yaml.safe_load(f)
        for i in result:
            tmp.append(i)
        return tmp


class WriteFile:
    path: str

    def __init__(self, name: str) -> None:
        self.path = name

    def write_file(self, res) -> None:
        tmp = []
        for i in tqdm(range(len(res)), desc="File was wrote", ncols=100):
            tmp.append(res[i])
        yaml.dump(tmp, open(self.path, 'w', encoding="utf-8"), default_flow_style=False)


parser1 = argparse.ArgumentParser("Input & output parser1 ")
parser1.add_argument("-input", type=str, help="Input path")
parser1.add_argument("-output1", type=str, help="Output path")
parser1.add_argument("-output2", type=str, help="Output path")
pars1 = parser1.parse_args()
read1 = ReadFile(pars1.input)
data1 = read1.read_file()
new_ls_1 = sort_by(data1, 'weight')
write1 = WriteFile(pars1.output1)
write1.write_file(new_ls_1)


new_ls_2 = sort_by(data1, 'age')
write2 = WriteFile(pars1.output2)
write2.write_file(new_ls_2)

