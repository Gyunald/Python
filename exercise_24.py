def reverse_lines(infilename, outfilename):
    with open(infilename) as infile, open(outfilename,"w") as outfile:
        for one_line in infile :
            outfile.write(f"{one_line.rstrip()[::-1]}\n")

if __name__ == "__main__" :
    reverse_lines("/Users/kyu-deokkim/Downloads/p24.txt","/Users/kyu-deokkim/Downloads/p25.txt")

if __name__ == "__main__" :
    reverse_lines("/Users/kyu-deokkim/Downloads/p24.txt","/Users/kyu-deokkim/Downloads/p25.txt")