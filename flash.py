# coding=UTF-8
import logging
import esptool
import toml

def flashRom(rom, port, baud):
    command_erase = ['--chip', 'esp32c3', '--port',
                     port, '--baud', baud, 'erase_flash']
    command_flash = ['--chip', 'esp32c3', '--port',
                     port, '--baud', baud, 'write_flash', '0x0', rom]
    logging.info("erase")
    esptool.main(command_erase)
    logging.info("write")
    esptool.main(command_flash)

if __name__ == '__main__':
    conf = toml.load("conf.toml")
    flashRom(conf['firmware']['path'],
             conf['device']['port'],
             conf['device']['baud'])
