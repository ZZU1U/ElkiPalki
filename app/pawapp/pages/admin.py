from flet import Text, Page
from ..components.appbar import MyAppBar


async def AdminPage(page: Page, back=None):
    await page.clean_async()
    print(page.dialog)
    page.appbar = MyAppBar(title='Панель админа', back=back)
    await page.add_async(Text("Admin Page"))
