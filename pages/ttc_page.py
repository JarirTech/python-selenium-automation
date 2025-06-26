from pages.base_page import Page


class TargetTermConditions(Page):

    def verify_ttc_opened(self):
        self.wait_for_url_contains('terms-conditions')