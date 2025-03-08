
lines = []
club_votes = dict()
clubs_to_fill = ['Art Journaling - Use your creative side to respond to weekly prompts and explore your personal expression.  (25)',
    'Baseball Club  (20)',
    'Basketball Club (20)',
    'Bingo Club (25)',
    'Board Games Club  (20)',
    'Book Club - Read and enjoy your own books.  (20)',
    'Choir Club  (20)',
    'Crochet Club  -  Learn to create fun projects with yarn and crotchet hooks. All levels invited.  (20)',
    'Culture Club - Share your culture and  learn about other cultures. Student driven club!  (20)',
    'Disney Movie Club  (40)',
    'Four Square Club  (40)',
    'Gaming Club  (20)',
    'General Academic Support',
    'Green Team -  We work on environmentally friendly projects for our school like recycling and gardening.(20)',
    'Jazz Club - View live jazz performances and discuss styles albums history trends etc.  (20)',
    'Lego Club  (20)',
    'Minecraft Club  (20)',
    'Origami Club - Explore the ancient art of paper folding.  (20)',
    'Puzzle Club  (20)',
    'Unity Club - A supportive space for students who are friendly to all diverse peers. (20)',
    'Volleyball Club  (20)',
    'Walking Club  (40)']

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

def parse_students_allowed_from(club_name):
    if club_name.startswith('General Academic Support'):
        return 420
    
    a = club_name.split('(')
    b = a[1].split(')')
    return int(b[0])

def populate_club(club_name, lines):
    m = parse_students_allowed_from(club_name)
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
#        if line.count('Harry Potter') > 0 or line.count('Green Team') > 0 or line.count('Mindfulness Club') > 0 or line.count('Unity Club') > 0:
#            continue
#        if line.count('Book Club') > 0 or line.count('Crochet Club') > 0 or line.count('Jazz Band') > 0: 
#            continue

        line = line.strip()
        count(line)
        lines.append(line.split(','))

#print(lines)
#print(club_votes)        

print(str(dict(sorted(club_votes.items(), key=lambda item: item[1]))))
print('------------------------------------------------------------')

for c in clubs_to_fill:
    lines = populate_club(c, lines)

print('\nRemainder:')
for l in lines:
    print(','.join(l))

assert(parse_students_allowed_from('General Academic Support (like the current 9th Period)') == 420)
assert(parse_students_allowed_from('Lego Club  (20)') == 20)
assert(parse_students_allowed_from('Disney Movie Club  (40)') == 40)
assert(parse_students_allowed_from('Art Journaling - Use your creative side to respond to weekly prompts and explore your personal expression.  (25)') == 25)
