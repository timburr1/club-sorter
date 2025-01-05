
lines = []
club_votes = dict()
clubs_to_fill = ['Puzzle Club', 'Baseball Club', 'Minecraft Club', 'Spirit Club', 'Weight Lifting Club', 'Board Games Club', 'Basketball Club', 'Walking Club', 'Lego Club', 'Gaming Club', 'Volleyball Club', 'Movie Club (Not Disney)', 'DISNEY Movie Club', 'General Academic Support']

# count the total number of votes for each club
def count(input):
    global club_votes

    i = input.split(',')
    for j in range(5, 8):
        if i[j] == '':
            continue
        if club_votes.get(i[j]) == None:
            club_votes[i[j]] = 1
        else:
            club_votes[i[j]] += 1

def students_allowed(club_name):
    if club_name == 'Basketball Club' or club_name == 'Walking Club':
        return 40
    if club_name == 'General Academic Support':
        return 420
    return 20

def populate_club(club_name, lines):
    m = students_allowed(club_name)
    print('\n' + club_name + ':')

    found = 0
    
    # choices are in cols 5-7
    for i in range(5, 8):
        j = 0
        while j < len(lines):

            if lines[j][i] == c:
                print(','.join(lines[j]))
                found += 1
                lines = lines[:j] + lines[j+1:]
            else:
                j += 1

            if found == m:
                return lines
    
    return lines                    

with open('votes.csv') as fp:
    for line in fp:
        # These clubs are already squared away:
        if line.count('Harry Potter') > 0 or line.count('Green Team') > 0 or line.count('Mindfulness Club') > 0 or line.count('Unity Club') > 0:
            continue
        if line.count('Book Club') > 0 or line.count('Crochet Club') > 0 or line.count('Jazz Band') > 0: 
            continue

        line = line.strip()
        # count(line)
        lines.append(line.split(','))
        
# print(str(dict(sorted(club_votes.items(), key=lambda item: item[1]))))

for c in clubs_to_fill:
    lines = populate_club(c, lines)

print('\nRemainder:')
for l in lines:
    print(','.join(l))
