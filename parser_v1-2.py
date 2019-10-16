
def parse_(sel):
    import csv

    if sel == 1:
        parsed = open("MTND.csv","w+")                               # open/create result file
        raw = open("data_Multitone Distortion_MTND.txt","r")      # open raw-data file in object
    else:
        if sel == 2:
            parsed = open("MTF.csv","w+")                               # open/create result file
            raw = open("data_Hx (f) Magnitude_Measured.txt","r")      # open raw-data file in object
        else:
            if sel == 3:
                parsed = open("ICHD.csv","w+")                               # open/create result file
                raw = open("data_Instantaneous Distortion_Distortion.txt","r")      # open raw-data file in object
            else:
                if sel == 4:
                    parsed = open("THD.csv","w+")                               # open/create result file
                    raw = open("data_Harmonic Distortion_THD.txt","r")      # open raw-data file in object
                else:
                    parsed = open("SPL.csv","w+")                               # open/create result file
                    raw = open("data_p (f) Spectrum_Signal level.txt","r")      # open raw-data file in object


    dummyf = csv.reader(raw, delimiter="\t")                    # open dummy file to extract from object
    dummyl = next(dummyf)                                       # extract dummy line (header)

    # Write header to CSV file
    parsed.write("Stage_ID,Device_ID,Frequency,Value\n")
    col = 0                 # column counter
    #stage = 1               # stage value
    stage = int(input("Type the Stage ID: "))
    spkcount = 0            # speaker counter

    for spk in zip(*[line for line in csv.reader(raw, delimiter="\t")]):
        if col==0:
            freq = spk      # first column contains frequency
            col = col+1
        else:
            i = 0
            for data in spk:
                parsed.write(str(stage))
                parsed.write(',')
                parsed.write(str(spkcount))
                parsed.write(',')
                parsed.write(str(freq[i]))
                parsed.write(',')
                parsed.write(str(data))
                parsed.write('\n')
                i = i+1
            col=col+1
        spkcount = spkcount+1
    parsed.close()
    raw.close()


print("1: MTND\n2: MTF\n3: ICHD\n4: THD\n5: SPL\n")
sel = int(input("Select a data type: "))

if sel == 1:
    parse_(sel)
else:
    if sel == 2:
        parse_(sel)
    else:
        if sel == 3:
            parse_(sel)
        else:
            if sel == 4:
                parse_(sel)
            else:
                parse_(sel)