
open_file = open("sample.txt")
story = open_file.read().lower()
open_file.close()

exclude = "!.?,:;"
for excluded_char in exclude:
    story = story.replace(excluded_char, "").replace("\n", "")

ex_words = (" a ", " able ", " about ", " across ", " after ", " all ", " almost ", " also ", " am ", " among ", " an ",
            " and ", " any ", " are ", " as ", " at ", " be ",
            " because ", " been ", " but ", " by ", " can ", " cannot ", " could ", " dear ", " did ", " do ", " does ",
            " either ", " else ", " ever ", " every ",
            " for ", " from ", " get ", " got ", " had ", " has ", " have ", " he ", " her ", " hers ", " him ",
            " his ", " how ", " however ", " i ", " if ", " in ", " into ", " is ",
            " it ", " its ", " just ", " least ", " let ", " like ", " likely ", " may ", " me ", " might ", " most ",
            " must ", " my ", " neither ", " no ", " nor ",
            " not ", " of ", " off ", " often ", " on ", " only ", " or ", " other ", " our ", " own ", " rather ",
            " said ", " say ", " says ", " she ", "should",
            " since ", " so ", " some ", " than ", " that ", " the ", " their ", " them ", " then ", " there ",
            " these ", " they ", " this ", " tis ", " to ", " too ",
            " twas ", " us ", " wants ", " was ", " we ", " were ", " what ", " when ", " where ", " which ", " while ",
            " who ", " whom ", " why ", " will ", " with ", " would ", " yet ", " you ", " your ")
for excluded_words in ex_words:
    story = story.replace(excluded_words, "")

new_story = story.split()

counter_dict = {}
for word in new_story:
    if word in counter_dict.keys():
        counter_dict[word] += 1
    else:
        counter_dict[word] = 1
# print(help(list))

# story = words.sort()

sorted_list = sorted(counter_dict.items(), key=lambda x: x[1])

new_list = []

for num in range(20):
    new_list.append(sorted_list.pop())
    for wordlist, count in new_list:
        new_new_list = "{} {}".format(wordlist, count)
    print(new_new_list)
