from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command 
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()

class Register(StatesGroup):
    name = State()
    age = State()
    grade = State()

@router.message(CommandStart()) 
async def cmd_starts(message: Message): 
    await message.answer('Здравствуйте! Я бот, ваш помощник для регистрации на встречу нашего книжного клуба. Готовы начать?', reply_markup=kb.main) 


@router.message(F.text == 'Конечно!') 
async def lala(message: Message): 
    await message.answer('Ближайшая встреча планируется 29 января в 14:30. Удобно ли вам встретиться с нами в это время?', reply_markup=kb.lala)

@router.message(F.text == 'Бесспорно!') 
async def lala(message: Message): 
    await message.answer('Ближайшая встреча планируется 29 января в 14:30. Удобно ли вам встретиться с нами в это время?', reply_markup=kb.lala)


@router.message(F.text == 'Да') 
async def lala(message: Message): 
    await message.answer('Хорошо, на предстоящей встрече мы совершим увлекательное погружение в мир Антона Павловича Чехова, проследив за ключевыми этапами его биографии и раскрыв глубину его гения через призму таких произведений, как "Руководство для желающих жениться", "Попрыгунья" и "Крыжовник". Используйте команду /register, чтобы зарегистрироваться.')
    

@router.message(F.text == 'Нет') 
async def catalog(message: Message): 
    await message.answer('Хорошо, надеемся в следующий раз у вас получится.')


@router.message(Command('register'))
async def register(message:Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя.')

@router.message(Register.name)
async def register_name(message:Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer('Введите ваш возраст.')

@router.message(Register.age)
async def register_age(message:Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.grade)
    await message.answer('Введите ваш класс.')

@router.message(Register.grade)
async def register_age(message:Message, state: FSMContext):
    await state.update_data(grade=message.text)
    data = await state.get_data()
    await message.answer(f'Ваше имя: {data["name"]}\nВаш возраст: {data["age"]}\nКласс: {data["grade"]}\nМы вас ждем!')
    await state.clear()