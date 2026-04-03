"""Advent of Code 2025, Day 2"""
raw_values = ('3737332285-3737422568,5858547751-5858626020,166911-236630,15329757-15423690,753995-801224,'
                '1-20,2180484-2259220,24-47,73630108-73867501,4052222-4199117,9226851880-9226945212,7337-24735,'
                '555454-591466,7777695646-7777817695,1070-2489,81504542-81618752,2584-6199,8857860-8922218,'
                '979959461-980003045,49-128,109907-161935,53514821-53703445,362278-509285,151-286,625491-681593,'
                '7715704912-7715863357,29210-60779,3287787-3395869,501-921,979760-1021259')
sum = 0
input_values = raw_values.split(',')

for elem in input_values:
    boundary = elem.split('-')
    begin = int(boundary[0])
    end = int(boundary[1]) + 1

    for num in range(begin, end):
        num_to_str = str(num)
        if len(num_to_str) % 2 == 0:
            middle = int(len(num_to_str)/2)
            substring = num_to_str[0:middle]
            if str(num).count(substring) == 2:
                sum += num