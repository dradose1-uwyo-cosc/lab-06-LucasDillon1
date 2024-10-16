# Lucas Dillon
# UWYO COSC 1010
# 10/15/24
# Lab 06
# Lab Section: 16
# Sources, people worked with, help given to: Got some assistance from Jackson Fetsco with the round function.
# 


random_string = """
jppamiqxegokaizvkyawwurhewtcxohryzptznyuedhhmawpic
pkzwuiorngdfcsgqnlyifzyaivehpiyszykqprbcsobygzhadd
yfddbulxmcnyvqhesmnybyuhxjqqmhdxwhcselasiayqhctnlw
hakethjahqnvjdowhlyzosemxkbenestxgvgncmffkcxldcmkl
itclmqdhrbdgzwtvdxwedcknbyaecvttjphtxubvhwvcvjqayy
almxuxjbcmznnzekptfzbldsjwpvringlmalwufvlppeiendur
dyophftqjkghhncwxoksqaqnpueudpygiytqgpcgjqsjbtbpzi
vaeczmyicnednjjoxkpnjmpfbgyjnbfjlweqqppodfxfzzwkuf
rldgryyhceuikimoavosuzuozthmatcgxcmkxnaxmsevkcumby
spiajlbycvrluxdkfavxidzalxuixqkxiybhfuqhcvmrhzbzse
idjwgwdwgfkyreozkyoxdvhixfejxjfgkkgobescboyfshiovu
fxdyvfsnmjzsphgmtldlaoehofcspzujghcdcxzggvunpbtglr
topplmkviuewwpoaplmbpgejmymxbyzzwbnujrlysszmxkjerb
zpiewqvgopvhmmcgwcyvxvwhdvfgsrybcozhdtwujhdbxzznkc
ergcqbetpgwrejuluqfxchlihunzbcdwboysjqenjxzbgqbycx
dybxpyztjyxpkqfvxullzkedpkjjobhymfinpvprxejktyrpai
ehjgwahpquzcmvclatdfcmattavoehnhnzveoxwnmnptxbvxto
gpcobgzdhsjevhcohkltftmrqkosknkxeylhqxkkctbnusijgr
uvecpbqmylqdaohkfaqbgeokyyipumjuaaayikdzyxfrpaieyo
uxiosjwioebsjtslblfurgcodtyaggzovzfnnyjngawiwbbtqi
kqqhnkwheolpqzasmsmbxqkeiqvogquobphewznfsnlkkizhca
cbiyvxpmjxywqvzqtshfvnfbusphggexfqzepsrduvtovdsknl
ztyuwugprkhbmktfvrenbmqgdjwnkeugtojrpqfmjhtrlcqcpq
pwsguedzgvktpwbqkhkueymjtxbvzmdfjopzkygujrjdtogssg
cxczryuqhhgjlpultkoffescpzyjrfqqabnhkfdnhkylpjamxk
uxidjkqdrkxqjqjtflebvwhcvqjciykzhrvppvxhvpedgznwty
kujglixooczrhxziasjxddfcghzlwrqcyiilpruhdfvitewxzg
dzcvmvnoskchscgoqfsojfvahlwkrslzeirlblseplcmpmbmum
ibrdamvqfstydtjopdkdcbnnmpifxckozyxzluhcqbqtpismog
ulufaajxvuizvdzioxfvypxovptkibcrjvfidomejknuggfrtp
kptwffersvqjknemkejsgspckwqisdcliuezhbeqpwgrjcqajl
huobykkbujmyuuinbwdklqfhvakyozzsxghfyownjjwqtkxgkf
ipdbjzxfogozstfsektujsvklrvecditiectuvtfibohmxxzna
cpqzeoburtquuizhypugnkvuwbdxnraareqkofhfjobrpcsuxq
nbafxlkuafbfsiuyrxdusqyasqyrwhdjrukgxdackumvairlgn
fjhenwbrdghbevgqbybpwncclolgqyuhallbqtzdywbvlzwtil
jctmsxjortnxvlbhuhkblppewjhqjzxrwgftlturxjuwfoaqpp
sgfnxwxolkbrpdmpniitoljzaxabgtnelrmryetxqypwrjdyjc
zipwbdpbazxpesmrcfuikeamtlsrgxrhzfytecenyydeemrhxj
gmdruhillntvpadzbroyygydpmonwuakruvxbdrqhtrjvoqsin
gjbarzvuqplmsmbwtqfghteoknbxmaokwlqqfoblmzsxczjzfj
mzmawtarjdtgongqqufhhdjwcinhlxcsgoltjycxrkloqozxoi
crlfmgflzzxgiiliqlksxyaydsohhahzxtsufzppftvgbpsdlx
ertfmbothijzrrdvfrnsohnwulcxvcvxngvmznhazxrgdsugij
fracotpirvqemsiuualpkpvtmtgchmowkmvoolrjfblrtwkmtr
xhawucytgwlahddkhxxfublukkdldpovqokntydhzzrxiisdwu
ujrkoewqoflyebogbwgdhriwkkoiofwtjlhxxtmzkklzbcmxhv
lrslowamkcwolbcgfkfciegdwqskuazxnycqkkggzsowcmafay
ibmkdwkqmdkjesqnjiqpijixbwjhenmsrrlpcseliiajlvcaac
zkdenxczyooloczcaahnkehbwimvieedpdlqfafbqvxvfmvabd
"""
random_string = random_string.replace("\n","") #remove all newline characters
print(len(random_string)) # Print out the size for reference 

# Above is a string with 2500 characters.
# Create a program that goes through and counts the occurrence of each character, excluding \n using a dictionary (Check)
# Output each letter and its corresponding occurrence in alphabetical order (Check)
# Output which letter occurred the most (Check)
# Output which letter occurred the least (Check)
# Output what the percentage of the string each character is, again in alphabetical (Check)


letter_dict = {}  # Creates a new dictionary.

for letter in range(0, len(random_string)):       # Iterates through the string.
    if random_string[letter] not in letter_dict:  # A check to ensure a letter is not already in the dictionary.
        letter_dict[random_string[letter]] = 1    # If not, creates a new dictionary entry with an initial occurrence value of 1.
    else:
        letter_dict[random_string[letter]] += 1   # Increases the count for a letter by one otherwise.

#The below method to sort a dictionary is because apparently "dict has no attribute sort."

# better_letter_dictionary = {}
# for key in sorted(letter_dict):
#     better_letter_dictionary[key] = letter_dict[key]
# print(better_letter_dictionary)

#Never mind, after a brief period I realized that using sorted() and item() will work.

better_letter_dict = {}                         # Creates a new list to use later. Takes inspiration from the above commented code.
for key, value in sorted(letter_dict.items()):  # Iterates through the old list, but sorted.
    print(f"{key}: {value} times")              # Prints out the letter and count of the letter.
    better_letter_dict[key] = value             # Takes the opportunity to create a new dictionary based on the sorted dictionary.

most_occurred = "a"                                                   # Starts at letter a, because the sorted list is alpabetical.
least_occurred = "a"                                                  # Same as previous line.
for key in better_letter_dict:
    if better_letter_dict[key] > better_letter_dict[most_occurred]:   # Checks to see if the current iteration has a higher value than the previous highest.
        most_occurred = key                                           # If so, updates most occurred to the new highest.
    if better_letter_dict[key] < better_letter_dict[least_occurred]:  # Checks to see if the current iteration has a lower value than the previous lowest.
        least_occurred = key                                          # If so, updates least occurred to new lowest.
        
#Tips and trick:
# You can iterate through strings like you would a list
# All characters are lowercase 
# Each letter will be PAIRED with its corresponding value 
# That is to say, this is a great use of dictionaries
    # You will need to add the letter to the dictionary on first occurrence 
    # Then increment its corresponding count 


#Load all the elements into a dictionary
#Will need to first declare a dictionary 

# Output: each letter and its corresponding occurrence in alphabetical order

print("*"*75)

# Output which letter occurred the most 

print(f"The letter that occurred the most is {most_occurred}")
print("*"*75)

# Output which letter occurred the least 

print(f"The letter that occurred the least is {least_occurred}")
print("*"*75)

# Output what the percentage of the string each character is, again in alphabetical

# The below code is a really hard section to read, but essentially:
# it iterates through the sorted list, and for each letter, it 
# divides the number of occurrences by the length of the string,
# multiplies by 100 to get a percent, and rounds to one decimal 
# place.

for key in better_letter_dict:
    print(f"{key} is {round(better_letter_dict[key]/len(random_string)*100, 1)}% of the string.")

