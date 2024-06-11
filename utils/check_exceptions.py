from pages.open_page import page


def check_exceptions():
    try:
        page.open_start_page()
    except Exception as e:
        return True
    return False
