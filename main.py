import logging
import os

import telebot
from telebot import types
from telebot.types import Message, CallbackQuery

logging.basicConfig(format='[%(levelname)s]%(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

bot = telebot.TeleBot(os.environ['TELEBOT_SELLER_TOKEN'])

ADS = 'Разместить объявление'
OFFICE = 'Личный кабинет'
SERVICES = 'Наши услуги'
MONEY = 'Пополнить баланс'
SUPPORT = 'Техподдержка'

default_markup = types.ReplyKeyboardMarkup()
default_markup.row(types.KeyboardButton(ADS), types.KeyboardButton(OFFICE))
default_markup.row(types.KeyboardButton(SERVICES))
default_markup.row(types.KeyboardButton(MONEY), types.KeyboardButton(SUPPORT))


@bot.message_handler(commands=['start', 'menu'])
def _send_welcome(message: Message):
    msg = (
        'Добро пожаловать!\n'
        'Этот бот поможет вам разместить объявление в чате _\n'
        'Помощь по использованию бота https://t.me/c/1242266411/9'
    )
    bot.send_message(message.chat.id, msg, reply_markup=default_markup)


SELL = 'sell'
BUY = 'buy'
ORDER_ADS_IN_CHAT = 'order_ads_in_chat'


@bot.message_handler(commands=['ads'])
@bot.message_handler(func=lambda msg: msg.text == ADS)
def _ads(message: Message):
    msg = (
        '👉 Продать  это услуга по продаже Вами рекламного место в вашем аккаунте (Платно)\n'
        '👉 Купить это услуга по поиску рекламного аккаунта (Бесплатно или Платно)\n'
        '👉 Заказать Рекламу в чате это услуга для Фрилансеров, Smm,  размещение Гивов, Марафонов или иных услуг (Платно)'
    )
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton('Продать', callback_data=SELL),
               types.InlineKeyboardButton('Купить', callback_data=BUY))
    markup.row(types.InlineKeyboardButton('Заказать Рекламу в чат', callback_data=ORDER_ADS_IN_CHAT))
    bot.send_message(message.chat.id, msg, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == SELL)
def _sell(call: CallbackQuery):
    msg = 'Создание нового объявления'
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'TODO: Опубликовать объявление')


@bot.callback_query_handler(func=lambda call: call.data == BUY)
def _buy(call: CallbackQuery):
    msg = 'Создание нового объявления'
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'TODO: Опубликовать объявление')


@bot.callback_query_handler(func=lambda call: call.data == ORDER_ADS_IN_CHAT)
def _order_ads_in_chat(call: CallbackQuery):
    msg = 'Создание нового объявления'
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'TODO: Опубликовать рекламное объявление')


@bot.message_handler(commands=['office'])
@bot.message_handler(func=lambda msg: msg.text == OFFICE)
def _office(message: Message):
    msg = (
        'Пользователь\n'
        '\n'
        'ID: _\n'
        f'Telegram ID: {message.from_user.id}\n'
        'Баланс: _ руб.\n'
        'Ваши активные объявления о продаже: _\n'
        'Ваши активные объявления о покупке: _\n'
        'Всего Ваших объявлений: _\n'
        'Ваша реферальная ссылка: _\n'
        'Ваши рефералы: _\n'
    )
    bot.send_message(message.chat.id, msg)


TELEGRAM_CHAT_PROMOTION = 'telegram_chat_promotion'
MAILING_IN_DIRECT = 'mailing_in_direct'
DEAL_GUARANTOR = 'deal_guarantor'


@bot.message_handler(func=lambda msg: msg.text == SERVICES)
def _services(message: Message):
    msg = 'Что вас интересует?'
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton('Продвижение телеграмм чатов', callback_data=TELEGRAM_CHAT_PROMOTION))
    markup.row(types.InlineKeyboardButton('Рассылка в директ', callback_data=MAILING_IN_DIRECT))
    markup.row(types.InlineKeyboardButton('Гарант сделки', callback_data=DEAL_GUARANTOR))
    bot.send_message(message.chat.id, msg, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == TELEGRAM_CHAT_PROMOTION)
def _telegram_chat_promotion(call: CallbackQuery):
    msg = (
        'Продвижение телеграмм чатов\n'
        'Поможем продвинуть ваш телеграмм чат. Будет закачана ваша целевая аудитория. Обращаться к _'
    )
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, msg)


@bot.callback_query_handler(func=lambda call: call.data == MAILING_IN_DIRECT)
def _mailing_in_direct(call: CallbackQuery):
    msg = (
        'Рассылка в директ\n'
        'Условия по рассылке в телеграмм канале: _'
    )
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, msg)


@bot.callback_query_handler(func=lambda call: call.data == DEAL_GUARANTOR)
def _deal_guarantor(call: CallbackQuery):
    msg = (
        'Гарант сделки\n'
        'Стоимость улгуи составляет 5% от суммы сделки.\n'
        'Чтобы воспользоваться услугой гаранта обращайтесь к _'
    )
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, msg)


@bot.message_handler(commands=['money'])
@bot.message_handler(func=lambda msg: msg.text == MONEY)
def _money(message: Message):
    msg = (
        'Ваш баланс: _ руб.\n'
        '\n'
        'Для пополнения баланса в боте реквизиты\n'
        'Сбербанк\n'
        '_\n'
        'Тинькофф\n'
        '_\n'
        'QIWI кошелек\n'
        '_\n'
        '\n'
        'К платежу ОБЯЗАТЕЛЬНО укажите ваш комментарий: _\n'
        '\n'
        'Минимальная сумма пополнения _ рублей\n'
        '\n'
        'Вы получите уведомление о том, что ваш счет пополнен, после чего сможете заказать отчет\n'
    )
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['support'])
@bot.message_handler(func=lambda msg: msg.text == SUPPORT)
def _support(message: Message):
    msg = 'Введите ваш вопрос в свободной текстовой форме'
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['help'])
def _help(message: Message):
    msg = (
        'Для использования бота напишите команду /start\n'
        'Откроется меню, которым вы сможете воспользоваться.\n'
        '\n'
        'Для размещения объявлений выберите нужный пункт меню, следуйте всем указаниям и ваше объявление будет опубликовано.\n'
        'После завершения добавления вам будет предложено несколько вариантов размещения объявления:\n'
        '   Единоразовое - объявление попадет в чат один раз\n'
        '   Автоматическое размещение - объявление будет публиковать повторно в соответсвие заданным вами параметрам.\n'
        'В случае если ваше объявление будет отклонено вам нжуно будет исправить объявление в соотвествие с замечаниями через личный кабинет.\n'
        '\n'
        'Более подробная информация располагается в большом посте-инструкции - https://t.me/insta1reklama/712479\n'
    )
    bot.send_message(message.chat.id, msg)


@bot.message_handler(func=lambda message: True)
def echo_all(message: Message):
    msg = 'Ваш запрос отправлен, ожидайте ответа'
    bot.send_message(message.chat.id, msg)


logger.info('BOOT POLLING')
bot.infinity_polling()
