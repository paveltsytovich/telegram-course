# (c) TICSIA
#
#  Demo bot main file
from DemoBot import DemoBot
import business_service as bl

def main():
    bot = DemoBot()
    bot.register_start_handler(bl.start_command)
    bot.register_text_handler(bl.check_phone,regexp='^Телефон [()0-9]*')
    bot.register_text_handler(bl.check_email,regexp='^Почта ')
    bot.register_text_handler(bl.train_schedule,regexp='^Расписание ')
    bot.register_text_handler(bl.filter_handler,regexp='^[A-Za-z0-9]*')
    
    bl.init()
    bl.init_nosql()
    
    bot.run()
    
if __name__ == '__main__':
    main()