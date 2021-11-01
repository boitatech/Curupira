# Little logging library
# __ madness.

import colorama as __colorama
import threading as __threading

__lock = __threading.Lock()

__colorama.init()

class __msg_type(int):
	debug   = 9,
	success = 10,
	err     = 12,
	warn    = 14


__str_type = {
    __msg_type.debug:   ".",
    __msg_type.success: "+",
   	__msg_type.err:     "!",
    __msg_type.warn:    "*"
}

__str_color = {
    __msg_type.debug:   __colorama.Fore.BLUE + __colorama.Style.BRIGHT,
    __msg_type.success: __colorama.Fore.GREEN + __colorama.Style.BRIGHT,
   	__msg_type.err:     __colorama.Fore.RED + __colorama.Style.BRIGHT,
    __msg_type.warn:    __colorama.Fore.YELLOW + __colorama.Style.BRIGHT
}


def __get_type(type: __msg_type) -> str: return __str_type[type]
def __get_color(type: __msg_type) -> str: return __str_color[type]


def __log(type: __msg_type, content: str) -> None:
    color = __get_color(type)
    str_type = __get_type(type)

    reset = __colorama.Fore.RESET

    debug_color = reset
    if type == __msg_type.debug:
        debug_color = __colorama.Fore.BLACK + __colorama.Style.BRIGHT

    __lock.acquire()
    print(f'{color}[{str_type}]{reset} {debug_color}{content}{reset}')
    __lock.release()


# Public
class log:
    def debug(content: str) -> None: __log(__msg_type.debug, content)
    def success(content: str) -> None: __log(__msg_type.success, content)
    def err(content: str) -> None: __log(__msg_type.err, content)
    def warn(content: str) -> None: __log(__msg_type.warn, content)