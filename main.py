import flet
import flet_material as fm
import webbrowser



class App(flet.UserControl):
    def __init__(self):
        super().__init__()
    
    def MainContainer(self):
        self.viewContainer = flet.Container(
            expand=True,
            content=SettingsView()
        )

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
    
    def SelectIcon(self, e):
        for button in self.iconRow.controls[:]:
            button.selected = False
            button.update()
            if e.control.selected != True:
                e.control.selected = True
                e.control.update()

    def build(self):
        return flet.Column(
            expand=True,
            alignment="center",
            horizontal_alignment="center",
            controls=[
                self.MainContainer()
            ]
        )



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



class SettingsView(flet.UserControl):
    def __init__(self):
        super().__init__()

    def TelegramButton(e):
        webbrowser.open("https://t.me/melcxre")

    def DiscordButton(e):
        webbrowser.open("https://discordapp.com/users/362630323118407695/")

    def GitHubButton(e):
        webbrowser.open("https://github.com/melcxre/Stonks")

    #def ThemeSwitch(e):
    #    theme_switch = (
    #        flet.ThemeMode.DARK
    #        if flet.Page.theme_mode == flet.ThemeMode.LIGHT
    #        else flet.ThemeMode.LIGHT
    #    )
    #    return theme_switch

    def SettingsContainer(self):
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
                            flet.Switch(
                                #on_change=self.ThemeSwitch()
                            )
                        ]
                    )
                ]
            )
        )
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

    def build(self):
        return flet.Column(
            expand=True,
            alignment="center",
            horizontal_alignment="center",
            controls=[
                self.SettingsContainer()
            ]
        )



def main(page: flet.Page):
    page.title = "Stonks"
    page.window_min_height = 700
    page.window_min_width = 300
    page.theme_mode = flet.ThemeMode.DARK
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.add(App().build())
    page.update()



if __name__ == "__main__":
    flet.app(target=main)