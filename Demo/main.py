# (c) TICSIA
#
#  Demo bot main file
from DemoBot import DemoBot
import business_service as bl

def main():
    bot = DemoBot()
    bot.register_start_handler(bl.start_command)
   # bot.register_text_handler(user.sample_text,regexp='^[A-Za-z0-9]*')
    bot.run()
    
if __name__ == '__main__':
    main()