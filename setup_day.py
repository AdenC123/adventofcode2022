import argparse
import pathlib
import shutil


parser = argparse.ArgumentParser(description='Setup directory for an Advent of Code day')
parser.add_argument('day', type=int)
args = parser.parse_args()

print("Creating day {}".format(args.day))
folder_path = pathlib.Path(__file__).parent.resolve() / "day{}".format(args.day)
template_path = folder_path.parent / "template.py"

folder_path.mkdir()
(folder_path / "input.txt".format(args.day)).touch()
(folder_path / "test.txt".format(args.day)).touch()
shutil.copy(template_path, folder_path / "day{}.py".format(args.day))
print('Done')
