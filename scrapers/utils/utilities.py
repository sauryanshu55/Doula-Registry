"""
Use this function to write to a scratch file the parsed code, since there is only a limited amount of 
lines th terminal can show.
"""
def write_to_scratch(content, overwrite):
    mode = "w" if overwrite else "a"
    with open("scratch.txt", mode) as file:
        file.write(content + "\n")


