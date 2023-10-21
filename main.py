# Мой интерпретатор - Python 3.10.0('venv':venv)
# Все импортируемые библиотеки находятся у меня в виртуальной среде, созданной в этом проекте в папке venv
# На GitHub я ее не закоммитил, потому что много весит и долго коммитится
import flet
import flet_material as fm
# Это стандартная библиотека
import webbrowser


# Главный класс приложения
class App(flet.UserControl):
    # Эта функция вроде бы помогает наследованию для этого класса от другого класса flet.UserControl, но в этом я не уверен, по крайней мере так читал на StackOverflow
    def __init__(self):
        super().__init__()
    
    def MainContainer(self):
        # Контейнер со страницей
        # Здесь они должны переключаться при нажатии иконок страницы снизу приложения
        # Но пока что я вручную вписал какая страница тут отображается, потому что не знаю пока как сделать маршрутизацию страниц при нажатии иконок снизу 
        self.viewContainer = flet.Container(
            expand=True,
            content=SettingsView()
        )

        # Контейнер строки с иконками переключения страниц
        self.iconRow =flet.Row(
            alignment="center",
            controls=[
                flet.IconButton(
                    icon=flet.icons.CANDLESTICK_CHART_OUTLINED,
                    selected_icon=flet.icons.CANDLESTICK_CHART,
                    selected=True,
                    on_click=lambda e: self.SelectIcon(e)
                ),
                flet.IconButton(
                    icon=flet.icons.NOTIFICATIONS_OUTLINED,
                    selected_icon=flet.icons.NOTIFICATIONS,
                    selected=False,
                    on_click=lambda e: self.SelectIcon(e)
                ),
                flet.IconButton(
                    icon=flet.icons.SETTINGS_OUTLINED,
                    selected_icon=flet.icons.SETTINGS,
                    selected=False,
                    on_click=lambda e: self.SelectIcon(e)
                )
            ]
        )

        # Главный контейнер, содержащий в себе нижнюю строку с иконками переключения страниц и второй контейнер с просмотром выбранной страницы
        self.mainContainer = flet.Container(
            expand=True,
            content=flet.Column(
                alignment="center",
                controls=[
                    self.viewContainer,
                    self.iconRow
                ]
            )
        )
        return self.mainContainer
    
    # Функция изменения цвета иконки страницы при нажатии на иконку, чтобы было понятно какая страница выбрана
    def SelectIcon(self, e):
        for button in self.iconRow.controls[:]:
            button.selected = False
            button.update()
            if e.control.selected != True:
                e.control.selected = True
                e.control.update()

    # Функция построения и отрисовки всего приложения (Главного контейнера)
    def build(self):
        return flet.Column(
            expand=True,
            alignment="center",
            horizontal_alignment="center",
            controls=[
                self.MainContainer()
            ]
        )


# Класс страницы биржи (пока что не затрагиваю)
class ChartsView(flet.UserControl):
    def __init__(self):
        super().__init__()

    def StockInfoContainer(self):
        self.stockinfoContainer = flet.Container(
            expand=1,
            bgcolor=flet.colors.with_opacity(0.025, flet.colors.WHITE10),
            border_radius=5
        )
        return self.stockinfoContainer

    def ChartContainer(self):
        self.chartContainer = flet.Container(
            expand=4,
            bgcolor=flet.colors.with_opacity(0.025, flet.colors.WHITE10),
            border_radius=5
        )
        return self.chartContainer

    def build(self):
        return flet.Column(
            expand=True,
            alignment="center",
            horizontal_alignment="center",
            controls=[
                self.StockInfoContainer(),
                self.ChartContainer()
            ]
        )


# Класс страницы с уведомлениями (пока что не затрагиваю)
class NotificationsView(flet.UserControl):
    def __init__(self):
        super().__init__()

    def NotificationsContainer(self):
        self.notificationsContainer = flet.Container(
            expand=True,
            bgcolor=flet.colors.with_opacity(0.025, flet.colors.WHITE10),
            border_radius=5
        )
        return self.notificationsContainer

    def build(self):
        return flet.Column(
            expand=True,
            alignment="center",
            horizontal_alignment="center",
            controls=[
                self.NotificationsContainer()
            ]
        )


# Класс страницы с настройками приложения и информации о приложении
class SettingsView(flet.UserControl):
    def __init__(self):
        super().__init__()

    # Функции открытия ссылок на мои контакты на странице настроек
    def TelegramButton(e):
        webbrowser.open("https://t.me/melcxre")

    def DiscordButton(e):
        webbrowser.open("https://discordapp.com/users/362630323118407695/")

    def GitHubButton(e):
        webbrowser.open("https://github.com/melcxre/Stonks")

    # Страница настроек и информации о приложении
    def SettingsContainer(self):
        #Контейнер с описанием приложения и контактами
        self.appAbout = flet.Container(
            expand=True,
            content=flet.Column(
                alignment="center",
                controls=[
                    flet.Row(
                        alignment="center",
                        controls=[
                            flet.Image(
                                src="./assets/logo.png",
                                width=200,
                                height=200
                            )
                        ]
                    ),
                    flet.Row(
                        alignment="center",
                        controls=[
                            flet.Text(
                                "Автор",
                                color=flet.colors.TEAL_ACCENT_200,
                                style=flet.TextThemeStyle.BODY_LARGE
                            ),
                            flet.Text(
                                "-"
                            ),
                            flet.Text(
                                "melcxre",
                                style=flet.TextThemeStyle.BODY_LARGE
                            )
                        ]
                    ),
                    flet.Row(
                        alignment="center",
                        controls=[
                            flet.Text(
                                "Версия",
                                color=flet.colors.TEAL_ACCENT_200,
                                style=flet.TextThemeStyle.BODY_LARGE
                            ),
                            flet.Text(
                                "-"
                            ),
                            flet.Text(
                                "1.0.0",
                                style=flet.TextThemeStyle.BODY_LARGE
                            )
                        ]
                    ),
                    flet.Row(
                        alignment="center",
                        controls=[
                            flet.IconButton(
                                icon=flet.icons.TELEGRAM,
                                on_click=lambda e: self.TelegramButton()
                            ),
                            flet.IconButton(
                                icon=flet.icons.DISCORD,
                                on_click=lambda e: self.DiscordButton()
                            ),
                            flet.IconButton(
                                icon=flet.icons.CODE,
                                on_click=lambda e: self.GitHubButton()
                            )
                        ]
                    )
                ]
            )
        )
        # Контейнер с настройками
        self.appSettings = flet.Container(
            expand=True,
            content=flet.Column(
                alignment="center",
                controls=[
                    flet.Row(
                        alignment="center",
                        controls=[
                            flet.Text(
                                "Тема",
                                style=flet.TextThemeStyle.BODY_LARGE
                            ),
                            # Этот свитчер должен вызывать функцию ThemeSwitch() из главной main(page: flet.Page) функции, чтобы менять тему всего приложения
                            # Но я не понимаю как передать выполнение этой функции в этот класс при переключении свитчера
                            # Саму фишку я взял с официальной документации Flet, но проблема в том что у них и функция переключения темы находится в главной функции main,
                            # И свитчер добавляется в той же функции main через page.add()
                            # Но в моем случае свитчер находится в классе страницы настроек, которая потом отрисовывается в главном классе приложения
                            # Поэтому я не понимаю как мне вызвать эту функцию здесь, ведь добавлять свитчер на главную через page.add() сломает весь смысл того что я пишу все через классы
                            # И свитчер по сути будет не на странице настроек а вообще в самом приложении на постоянке висеть где-то, так мне кажется не красиво
                            # Пока что в ООП я особо не разбираюсь
                            flet.Switch(
                                #on_change=main().ThemeSwitch()
                            )
                        ]
                    )
                ]
            )
        )
        # Сама страница настроек на которую добавляется и описание приложения и настройки приложения
        self.settingsContainer = flet.Container(
            expand=True,
            bgcolor=flet.colors.with_opacity(0.025, flet.colors.WHITE10),
            border_radius=5,
            content=flet.Column(
                alignment="center",
                controls=[
                    self.appAbout,
                    self.appSettings
                ]
            )
        )
        return self.settingsContainer

    # Сборка и отрисовка страницы настроек
    def build(self):
        return flet.Column(
            expand=True,
            alignment="center",
            horizontal_alignment="center",
            controls=[
                self.SettingsContainer()
            ]
        )


# Главная функция
def main(page: flet.Page):
    page.title = "Stonks"
    page.window_min_height = 700
    page.window_min_width = 300
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"


    # Та самая функция переключения темы приложения
    def ThemeSwitch(e):
        page.theme_mode = (
            flet.ThemeMode.DARK
            if page.theme_mode == flet.ThemeMode.LIGHT
            else flet.ThemeMode.LIGHT
        )
        page.update()
    page.theme_mode = flet.ThemeMode.DARK



    page.add(App().build())
    page.update()



if __name__ == "__main__":
    flet.app(target=main)