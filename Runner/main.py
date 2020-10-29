# (c) TICSIA
#
#  Demo bot main file
from DemoBot import DemoBot
def sample_text(message):
    print(message)
    return message[::-1]

def main():
    bot = DemoBot()
    bot.register_start_handler()
    bot.register_text_handler(sample_text,'^[A-Za-z0-9]*')
    bot.run()
    
if __name__ == '__main__':
    main()