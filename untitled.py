    # Create array of Preferences, Size Candidates x Voters , Rand range 1-Candidates
import random
import numpy
Sims = 1000

TotalHypWinners = [0 for x in range(0, Sims)]
TotalFPWinners = [0 for x in range(0, Sims)]


for xtotal in range(0, Sims):
    Candidates = 15
    Voters = 1000
    Winners = 6
    Exclude = []
    Preferences = [[0 for x in range(1, Candidates+1)] for y in range(1, Voters+1)]
    #print Preferences
    for v in range(1, Voters+1):
        Exclude = [0 for c in range(0, Candidates+1)]
        #print Exclude
        for c in range(1, Candidates+1):
            r = 100
            while r in Exclude or r is 100:
                r = random.randrange(1, Candidates+1)
                Preferences[v-1][c-1] = r
            Exclude[c-1] = Preferences[v-1][c-1]
            #print Exclude
        #print v
        #print Preferences[v]
        #print c
        #print (Preferences[v][1:Candidates])
    #print Preferences[0:Voters][0:Candidates]
    #print Preferences[999][0:Candidates]
    #print Preferences[998][0:Candidates]


    # Tally up the first preferences for each candidate
    FirstPreferences = [0 for x in range(1, Candidates+1)]
    for vote in range(1, Voters+1):
        for cand in range(1, Candidates+1):
            if Preferences[vote-1][cand-1] == 1:
                FirstPreferences[cand-1] += 1
    VoterPreferenceUse = [1 for x in range(0, Voters)]

    #print "FirstPreferences:"
    #print FirstPreferences

    #Tally all preferences individually
    AllPreferences = [[0 for y in range(1, Candidates+1)] for x in range(1, Candidates+1)]
    for vote in range(1, Voters+1):
        for order in range(1, Candidates+1):
            for cand in range(1, Candidates+1):
                if Preferences[vote-1][cand-1] == order:
                    AllPreferences[order-1][cand-1] += 1
    VoterPreferenceUse = [1 for x in range(0, Voters)]
    #print AllPreferences


    UnWeightedSum = list(FirstPreferences)
    for cand in range(1, Candidates+1):
        UnWeightedSum[cand-1] = 0
        for candid in range(1, Candidates+1):
            UnWeightedSum[cand-1] += AllPreferences[candid-1][cand-1]
    #print UnWeightedSum
    # UnWeightedSum proves that every candidate received a preference by each voter
    # and serves as example code to construct the weighted sums
    #print FirstPreferences
    #print AllPreferences[0]
    HyperbolicDecreasingWeightedPreferences = [float(0) for i in FirstPreferences]
    for cand in range(1, Candidates+1):
        for pref in range(1, Candidates+1):
            HyperbolicDecreasingWeightedPreferences[cand-1] += float(1)/float(pref) * float(AllPreferences[pref-1][cand-1])
            #print float(1)/float(pref) * float(AllPreferences[pref-1][cand-1])
        #print "hyp"
        #print HyperbolicDecreasingWeightedSum[pref - 1]
    for i in range(0, len(HyperbolicDecreasingWeightedPreferences)):
        HyperbolicDecreasingWeightedPreferences[i] = int(HyperbolicDecreasingWeightedPreferences[i])

    #print "HyperbolcDecreasingWeightedPreferences:"
    #print HyperbolicDecreasingWeightedPreferences


    FirstPastPreferences = list(FirstPreferences)

    Removed = [0 for x in range(0, Candidates)]
    for removal in range(Winners, Candidates):
        fpmin = min(FirstPastPreferences)
        locmin = FirstPastPreferences.index(fpmin)
        FirstPastPreferences[locmin] = Voters*10
        Removed[locmin] = 1
        for vote in range(1, Voters + 1):
            changed = False
            if Preferences[vote - 1][locmin - 1] == VoterPreferenceUse[vote - 1]:
                for cand in range(1, Candidates + 1):
                    if Removed[cand - 1] == 0:
                        if Preferences[vote - 1][cand - 1] == (VoterPreferenceUse[vote - 1] + 1):
                                FirstPastPreferences[cand - 1] += 1
                                changed = True
            if changed == True:
                VoterPreferenceUse[vote - 1] += 1

    for i in range(0, len(FirstPastPreferences)):
        if FirstPastPreferences[i] == (Voters*10):
            FirstPastPreferences[i] = 0

    # print "FirstPastPreferences:"
    # print FirstPastPreferences




    # Determine the winners of each system
    FirstPastWinners = [0 for i in range(1, Winners+1)]
    HyperbolicWinners = list(FirstPastWinners)
    FirstPastCurrentMaxPlace = 0
    HyperbolicCurrentMaxPlace = 0

    for win in range(1, Winners+1):
        FirstPastMax = max(FirstPastPreferences)
        FirstPastCurrentMaxPlace = FirstPastPreferences.index(FirstPastMax)
        FirstPastPreferences[FirstPastCurrentMaxPlace] = 0
        FirstPastWinners[win-1] = FirstPastCurrentMaxPlace

        HyperbolicMax = max(HyperbolicDecreasingWeightedPreferences)
        HyperbolicCurrentMaxPlace = HyperbolicDecreasingWeightedPreferences.index(HyperbolicMax)
        HyperbolicDecreasingWeightedPreferences[HyperbolicCurrentMaxPlace] = 0
        HyperbolicWinners[win-1] = HyperbolicCurrentMaxPlace

    # print "HyperbolicWinners:"
    # print HyperbolicWinners
    # print "FirstPastWinners:"
    # print FirstPastWinners

    TotalHypWinners[xtotal] = HyperbolicWinners
    TotalFPWinners[xtotal] = FirstPastWinners

HypFPSimilarityCount = [0 for x in range(0, Sims)]
for sim in range(0, Sims):
    for cand in range(0, Winners):
        for candid in range(0, Winners):
            if TotalHypWinners[sim][cand] == TotalFPWinners[sim][candid]:
                HypFPSimilarityCount[sim] += 1
HypFPSimilarity = numpy.array(HypFPSimilarityCount)


print "Average Number of Similar Winners:"
print sum(HypFPSimilarityCount)/float(len(HypFPSimilarityCount))
print "Standard Deviation of Similar Winners:"
print numpy.std(HypFPSimilarity)

# running up to here takes approximately 10 minutes for Hyp and FPS.
