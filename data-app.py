import justpy as jp


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(
        a=wp, text="Analysis of Book Reviews", classes="text-h1 text-center q-pa-md"
    )
    p1 = jp.QDiv(a=wp, text="These graphs represent book review analysis")
    return wp


jp.justpy(app)
