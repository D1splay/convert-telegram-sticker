# convert-telegram-sticker

Программа автоматизирует конвертацию большого количества файлов, не соответствующих формату стикеров для Telegram. Как это работает? У вас есть файлы размером 1000x1000 в формате .jpg, тогда как для стикеров в Telegram требуется формат .png размером 512x512. Программа позволит вам автоматизировать процесс обработки.

**Установка**

```bash
curl -L -o converter https://github.com/D1splay/convert-telegram-sticker/releases/download/beta/converter-0.1-b
```

**Использование**

```bash
converter -i /dir/test/in -o /dir/test/stickers -c
```

```bash
usage: convert_lib.py [-h] -i INPUT -o OUTPUT [-c]

Convert images to 512x512 PNG images with transparent padding.

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input folder containing images
  -o OUTPUT, --output OUTPUT
                        Output folder for converted images
  -c, --convert         Convert images to PNG format if not already in PNG format
```

Донат:

BITCOIN: 1PNix46PfNvpZW4Hc84guu4b6auSUoytLQ

USDT TRC20: TKHB6wu99V9TpmixM8gBU96JXZniC55EGw

USDT TON: UQBUJ2r5r5MPbM68sbMgBmTVmcvwv6PpamlKTdsD8uTT2jkH

TON: UQBUJ2r5r5MPbM68sbMgBmTVmcvwv6PpamlKTdsD8uTT2jkH

**[Лицензия GNU General Public License v3.0](https://github.com/D1splay/convert-telegram-sticker/blob/main/LICENSE)** 

