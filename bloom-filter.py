#!/usr/bin/env python
# COMP 455 Term Project
# Check available usernames with a Bloom Filter

import mmh3
import os
import argparse

class BloomFilter:

    def __init__(self, bit_array_size, number_hashes):
        # Initialize the bit array
        self.bit_array_size = bit_array_size
        self.bit_array = [0] * bit_array_size
        self.number_hashes = number_hashes

    # Add usernames into the bit array
    def add_to_bit_array(self, username):

        for seed_count in range(self.number_hashes):
            result = mmh3.hash(username, seed_count) % self.bit_array_size

            self.bit_array[result] = 1

    # Check if the username is in the bit_array
    def check_availability(self, username):

        for seed_count in range(self.number_hashes):

            # Calculate hash on given username
            given_username = mmh3.hash(username, seed_count) % self.bit_array_size

        if self.bit_array[given_username] == 0:
            print("Username {0} is available!".format(username))
        else:
            print("Username {0} not available.".format(username))

def main():
    # Create bloom filter object. There are 7944 names in the all-names text file
    bloom_filter = BloomFilter(8000, 1)

    # Open the file with the usernames
    file_path = os.path.dirname(os.path.realpath(__file__)) + "/names/all-names.txt"

    # Read in the names from the txt file line by line
    with open(file_path) as unavailable_usernames:
        for name in unavailable_usernames:
            bloom_filter.add_to_bit_array(name.rstrip('\n'))

    parser = argparse.ArgumentParser()

    parser.add_argument("username", help="Username to check")

    args = parser.parse_args()

    if args.username:
        bloom_filter.check_availability(args.username)
    else:
        print("Unknown option. Enter a valid option.")

if __name__ == '__main__':
    main()
