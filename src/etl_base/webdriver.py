from os import getenv

from selenium.webdriver import ChromeOptions, Remote

from .exc import CommandExecutorNotSpecifiedException


class Webdriver(Remote):
    def __init__(self, **kwargs) -> None:
        opts = kwargs.pop('opts')
        if not opts:
            opts = ChromeOptions()
            opts.add_argument('--ignore-ssl-errors=yes')
            opts.add_argument('--ignore-certificate-errors')

        command_executor_url = getenv('COMMAND_EXECUTOR')
        if not command_executor_url:
            raise CommandExecutorNotSpecifiedException

        super().__init__(
            command_executor=command_executor_url,
            options=opts
        )
