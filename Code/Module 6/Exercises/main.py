# (c) TICSIA
#
#  Demo bot main file
from DemoBot import DemoBot
import business_service as bl

def main():
    bot = DemoBot()
    bot.register_start_handler(bl.start_command)
  
    bot.run()
    
if __name__ == '__main__':
    main()