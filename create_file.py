import io

def save(txt,title):
    #*************************************
    # write to file with utf8 encoding
    #*************************************

    filename = title.lower() + '.tex'
    with io.open(filename,'w',encoding='utf8') as f:
        f.write(txt)
    f.close()
