import os
import mutagen

# get the current directory
dir_path = os.path.dirname(os.path.realpath(__file__))

# get all .ogg files in the directory
files = [f for f in os.listdir(dir_path) if f.endswith(".ogg")]

# sort the files alphabetically
files.sort()

# store the lengths of each file in a list
lengths = []
for file in files:
    audio = mutagen.File(os.path.join(dir_path, file))
    lengths.append(int(audio.info.length) * 20)

# create the lengths.txt file
with open(os.path.join(dir_path, "lengths.txt"), "w") as f:
    for i, (length, file) in enumerate(zip(lengths, files)):
        f.write("execute if score song song matches {} if score songtick songtick matches {} run function alttp:music/{}\n".format(i + 1, length, file))
