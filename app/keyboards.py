from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton) 

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Конечно!')],
                                     [KeyboardButton(text='Бесспорно!')]],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню...')

lala = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Да')],
                                     [KeyboardButton(text='Нет')]],
                            resize_keyboard=True)

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Футболки', callback_data='t-shirt')],
    [InlineKeyboardButton(text='Кроссовки', callback_data='snekers')],
    [InlineKeyboardButton(text='Кепки', callback_data='cap')]])