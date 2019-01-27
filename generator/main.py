import sys
import generate as g

# this main is purely to test the functionality
# without interacting with the webpage

def main():

    ig_flag = int(sys.argv[1])
    creds_path = str(sys.argv[2])

    # post on instagram or not?

    if ig_flag == 0:

        hashtags = sys.argv[3:]

        # post to twitter
        g.generate_tweet(creds_path, hashtags)

    elif ig_flag == 1:

        src_text = str(sys.argv[3])
        length = int(sys.argv[4])
        photo_path = str(sys.argv[5])

        g.generate_ig(src_text, creds_path, length, photo_path)

if __name__ == '__main__':
    main()