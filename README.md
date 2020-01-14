# telegram_button

Append buttons to telegram message.

## usage

```
import telegram_button as bt
# default button list is [👍, ❤️, 😂, 😢, 😡]
bot.send_message(chat_id, text='test message',reply_markup=bt.get(YOUR_BUTTON_LIST))
bt.addHandlers(dispatcher, YOUR_BUTTON_LIST)
```

## how to install

`pip3 install telegram_button`