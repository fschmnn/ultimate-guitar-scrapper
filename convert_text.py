#==============================================================================
# convert the raw input to a LaTeX format
#==============================================================================

numbers = ['1','2','3','4','5','6','7','8','9',' ']

# function to split line into single chords
def split_row(row):
    line = []
    while row:
        try: item, row = row.lstrip().split(' ', 1)
        except: item, row = row.lstrip(), ''
        line.append(item)
    return line

# *************************************
# format for LaTeX
# *************************************
def parse(txt,title,interpret):
    #split input into list
    INPUT = txt.split('\n')

    length = len(INPUT)
    INPUT.append('')
    OUTPUT = []
    endenv = ''
    i = 0

    OUTPUT.append('\\begin{song}[title={' + title + '},interpret={' + interpret +'}]')
    # main loop
    while i < length:
        row = INPUT[i]

        # use empty space p to determine if a row is a "chord-row"
        if row != '':
            p = (row.count(' ') / len(row))
        else:
            p = 0

        if row == '':
            if endenv != '':
                OUTPUT.append(endenv)
                OUTPUT.append('')
                endenv = ''
            i += 1
        # determine environment
        elif row[0] == '[':
            env = row[row.find("[")+1:row.find("]")].lower()
            for string in numbers: env = env.replace(string,'')
            OUTPUT.append('\\begin{' + env + '}')
            endenv = '\\end{' + env + '}'
            i += 1
            if INPUT[i] == '': i += 1

        # place chords over text
        elif p >.50:
            # determine chord and position
            chords = split_row(row)
            index = []
            j = 0
            for chord in chords:
                idx = row.find(chord,j)
                index.append(idx)
                j = idx

            # create new line for text + chords
            textrow = INPUT[i+1]

            # check if textrow is long enough
            if len(textrow)<index[-1]:
                textrow += ' '* (index[-1]-len(textrow)+1)

            for chord, idx in zip(reversed(chords), reversed(index)):
                textrow = textrow[:idx] + '\chord{' + chord + '}' + textrow[idx:]
            textrow += '\\\\'

            # append result
            OUTPUT.append(textrow.replace('”','"').replace('“','"').replace('#','\sharp').replace("’","'"))
            i += 2
        else:
            OUTPUT.append(row + '\\\\' )
            i += 1

    OUTPUT.append('\\end{song}')

    txt = ''
    for line in OUTPUT:
        txt += line + '\n'

    return txt
