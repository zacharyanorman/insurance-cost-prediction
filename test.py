def count_smileys(arr):
    eyes = [';', ':']
    noses = ['-', '~']
    mouthes = [')', 'D']
    smiley_sum = 0

    for smiley in arr:
        if len(smiley) == 2:
            if smiley[0] in eyes and smiley[1] in mouthes:
                smiley_sum += 1
        if len(smiley) == 3:
            if smiley[0] in eyes and smiley[1] in noses and smiley[2] in mouthes:
                smiley_sum += 1
    return smiley_sum