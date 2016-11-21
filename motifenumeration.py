def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count + 1
    return count

def Suffix(Pattern):
    suffix = Pattern[1:len(Pattern)]
    return suffix

def HammingDistance(p, q):
    hammingdistance = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hammingdistance += 1
    return hammingdistance

def Neighbors(Pattern, d):
    nucleotides = ["A","C","G","T"]
    if d == 0:
        return [Pattern]
    if len(Pattern) == 1:
        return nucleotides
    Neighborhood = []
    SuffixNeighbors = Neighbors(Suffix(Pattern),d)
    for SuffixNeighbor in SuffixNeighbors:
        if HammingDistance(Suffix(Pattern),SuffixNeighbor) < d:
            for nucleotide in nucleotides:
                Neighborhood.append(nucleotide+SuffixNeighbor)
        else:
            Neighborhood.append(Pattern[0]+SuffixNeighbor)
    return Neighborhood

def remove_duplicates(Items):
    ItemsNoDuplicates = []
    for item in Items:
        if item not in ItemsNoDuplicates:
            ItemsNoDuplicates.append(item)
    return ItemsNoDuplicates



def MotifEnumeration(Dna,k,d):
    Patterns = []
    for i in range(len(Dna)):
        for j in range(len(Dna[i])-k+1):
            pattern = Dna[i][j:j+k]
            #print(pattern)
            neighbors = Neighbors(pattern,d)
            #print(neighbors)

            for neighbor in neighbors:
                counts = [0]*len(Dna)
                #print(neighbor)
                neighborhood = Neighbors(neighbor,d)
                #print(neighborhood)
                for item in neighborhood:
                    for k in range(len(Dna)):
                        #print(item)
                        #print(Dna[k])
                        #print(PatternCount(item,Dna[k]))
                        if PatternCount(item,Dna[k]) > 0:
                            counts[k] += 1
                #print(counts)
                totcount = 0
                for count in counts:
                    if count > 0:
                        totcount += 1
                if totcount == len(Dna):
                    Patterns.append(neighbor)
    Patterns = remove_duplicates(Patterns)
    return Patterns
