import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # TODO: Read database file into a variable
    database = []
    with open(sys.argv[1], "r") as data:
        reader = csv.DictReader(data)
        for row in reader:
            tmp = {}
            for key in row:
                if row[key].isdecimal():
                    tmp[key] = int(row[key])
                else:
                    tmp[key] = row[key]
            database.append(tmp)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as target:
        sequence = target.read()

    # TODO: Find longest match of each STR in DNA sequence
    keys = list(database[0].keys())
    keys.pop(0)

    matches = {}
    for key in keys:
        matches[key] = longest_match(sequence, key)

    # TODO: Check database for matching profiles
    match = False
    for i in range(len(database)):
        count = 0
        for key in keys:
            if database[i][key] == matches[key]:
                count += 1
            if count == len(keys):
                print(database[i]["name"])
                match = True

    if match == False:
        print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
