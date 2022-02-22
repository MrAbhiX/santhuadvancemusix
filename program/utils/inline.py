""" inline section button """

from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)


def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="📠ᴍᴇɴᴜ", callback_data=f'stream_menu_panel | {user_id}'),
      InlineKeyboardButton(text="🚵sᴋɪᴘ", callback_data=f'skip_current_song'),
      InlineKeyboardButton(text="🔊ᴠᴏʟᴜᴍᴇ", callback_data=f'set_volume'),
    ], 
    [
      InlineKeyboardButton(text="💘ɴᴇᴛᴡᴏʀᴋ📡", url="https://t.me/santhubotupadates"),
      InlineKeyboardButton(text="💖ɢʀᴏᴜᴘ💝", url="https://t.me/santhuvc"),
    ], 
    [ 
      InlineKeyboardButton(text="🗑ᴄʟᴏsᴇ", callback_data=f'set_close'),
    ]
  ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="😶sᴛᴏᴘ", callback_data=f'set_stop | {user_id}'),
      InlineKeyboardButton(text="🤔ᴘᴀᴜsᴇ", callback_data=f'set_pause | {user_id}'),
      InlineKeyboardButton(text="🙄ʀᴇsᴜᴍᴇ", callback_data=f'set_resume | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="💔ᴍᴜᴛᴇ", callback_data=f'set_mute | {user_id}'),
      InlineKeyboardButton(text="💘ᴜɴᴍᴜᴛᴇ", callback_data=f'set_unmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="◁", callback_data='stream_home_panel'),
    ]
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🗑 ᴄʟᴏsᴇ", callback_data="set_close"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "◁", callback_data="stream_menu_panel"
      )
    ]
  ]
)
