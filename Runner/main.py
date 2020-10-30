# (c) TICSIA
#
#  Demo bot main file
from DemoBot import DemoBot
import user

def main():
    bot = DemoBot()
    bot.register_start_handler()
    bot.register_text_handler(user.sample_text,regexp='^[A-Za-z0-9]*')
    bot.run()
    
if __name__ == '__main__':
    main()