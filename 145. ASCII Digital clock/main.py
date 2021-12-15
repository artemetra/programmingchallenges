from datetime import datetime

from strs import asciiset

def ascii_time(timestr: str) -> str:
    # somehow, this solution seems to be more concise than 'for' loops,
    # that were my initial idea. what all of this does is basically
    # just loop over all the characters and render them line by line.
    # i might rewrite this to be more readable and scalable (removing
    # constants like 5), but for now here it is.
    return "\n".join(
        [
            "   ".join([asciiset[ch][1:-1].split('\n')[line] for ch in timestr])
            for line in range(5)
        ]
    )

if __name__ == '__main__':
    now = datetime.now().strftime("%H:%M:%S")
    print(ascii_time(now))
