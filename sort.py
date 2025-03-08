
lines = []
club_votes = dict()
# sorted from least to most popular:
clubs_to_fill = [
    'Culture Club - Share your culture and  learn about other cultures. Student driven club!  (20)',
    'Green Team -  We work on environmentally friendly projects for our school like recycling and gardening.(20)',
    'Choir Club  (20)',
    'Unity Club - A supportive space for students who are friendly to all diverse peers. (20)',
    'Jazz Club - View live jazz performances and discuss styles albums history trends etc.  (20)',
    'Bingo Club (25)',
    'Book Club - Read and enjoy your own books.  (20)',
    'Puzzle Club  (20)',
    'Origami Club - Explore the ancient art of paper folding.  (20)',
    'Art Journaling - Use your creative side to respond to weekly prompts and explore your personal expression.  (25)',
    'Crochet Club  -  Learn to create fun projects with yarn and crotchet hooks. All levels invited.  (20)',
    'Baseball Club  (20)',
    'General Academic Support',
    'Minecraft Club  (20)',    
    'Four Square Club  (40)',
    'Board Games Club  (20)',     
    'Basketball Club (20)', 
    'Gaming Club  (20)',    
    'Volleyball Club  (20)',
    'Lego Club  (20)',
    'Walking Club  (40)',
    'Disney Movie Club  (40)']

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
    if club_name.startswith('Disney Movie Club') or club_name.startswith('Four Square Club') or club_name.startswith('Walking Club'):
        return 40
    if club_name.startswith('General Academic Support'):
        return 420
    return 16

def populate_club(club_name, lines):
    m = students_allowed(club_name)
    print('\n' + club_name + ':,,')

    found = 0
    
    # choices are in cols 5-7
    for i in range(5, 8):
        j = 0
        while j < len(lines):

            if lines[j][i] == c:
                print(lines[j][2] + ', ' + lines[j][3] + ',' + lines[j][4])
                found += 1
                lines = lines[:j] + lines[j+1:]
            else:
                j += 1

            if found == m:
                return lines
    
    return lines                    

with open('votes.csv') as fp:
    for line in fp:
        line = line.strip()
        count(line)
        lines.append(line.split(','))

# print(lines)
# print(club_votes)        

# print(str(dict(sorted(club_votes.items(), key=lambda item: item[1]))))
# print('------------------------------------------------------------')

for c in clubs_to_fill:
    lines = populate_club(c, lines)

print('\nRemainder:,,')
for l in lines:
    print(l[2] + ', ' + l[3] + ',' + l[4])
