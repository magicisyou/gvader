import flet as ft
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialise vader sentiment analysis
sid = SentimentIntensityAnalyzer()

def show_sentiment_scores(statement):
    sentiment_scores = sid.polarity_scores(statement)
    result_row.controls[0].controls[0].content.value=sentiment_scores['neg']
    result_row.controls[1].controls[0].content.value=sentiment_scores['neu']
    result_row.controls[2].controls[0].content.value=sentiment_scores['pos']
    result_row.controls[3].controls[0].content.value=sentiment_scores['compound']
    result_row.update()

result_row=ft.Row(
    controls=[
        ft.Column(
            controls=[
                ft.CircleAvatar(
                    bgcolor=ft.colors.RED_300,
                    radius=100,
                    content=ft.Text('0.0',color=ft.colors.BLUE_GREY,size=38),
                ),
                ft.Text(
                    'Negative Score',
                    color=ft.colors.BLUE_GREY,
                    width=200,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
        ),
        ft.Column(
            controls=[
                ft.CircleAvatar(
                    bgcolor=ft.colors.YELLOW_300,
                    radius=100,
                    content=ft.Text('0.0',color=ft.colors.BLUE_GREY,size=38),
                ),
                ft.Text(
                    'Neutral Score',
                    color=ft.colors.BLUE_GREY,
                    width=200,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
        ),
        ft.Column(
            controls=[
                ft.CircleAvatar(
                    bgcolor=ft.colors.GREEN_300,
                    radius=100,
                    content=ft.Text('0.0',color=ft.colors.BLUE_GREY,size=38),
                ),
                ft.Text(
                    'Positive Score',
                    color=ft.colors.BLUE_GREY,
                    width=200,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
        ),
        ft.Column(
            controls=[
                ft.CircleAvatar(
                    bgcolor=ft.colors.BLUE_300,
                    radius=100,
                    content=ft.Text('0.0',color=ft.colors.BLUE_GREY,size=38),
                ),
                ft.Text(
                    'Compound Score',
                    color=ft.colors.BLUE_GREY,
                    width=200,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
        ),
    ],
    alignment=ft.MainAxisAlignment.SPACE_AROUND,
    vertical_alignment=ft.CrossAxisAlignment.CENTER,
)

textfield=ft.TextField(
    label='Enter sentence to analyze',
    hint_text='Enter the sentence or words to analyze and get its score',
    on_submit=lambda _:show_sentiment_scores(textfield.value),
    multiline=True,
    min_lines=3,
    shift_enter=True,
)

page_content=ft.SafeArea(
    ft.Column(
        [
            ft.Text(
                'GVADER GUI for VADER',
                size=24,
                color=ft.colors.BLUE_GREY_500,
            ),
            ft.Divider(),
            textfield,
            ft.FilledTonalButton(
                'Analyze',
                width=200,
                height=80,
                on_click=lambda _:show_sentiment_scores(textfield.value),
                style=ft.ButtonStyle(
                    shape={
                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=10),
                    },
                    padding=ft.padding.all(10),
                ),
            ),
            ft.Row(height=75),
            result_row,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
)

def main(page: ft.Page):
    page.title = "GVADER"
    page.theme = ft.theme.Theme(color_scheme_seed=ft.colors.BLUE_GREY)
    page.add(page_content)

ft.app(main)
