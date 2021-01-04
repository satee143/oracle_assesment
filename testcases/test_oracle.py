from scripts.homepage import homepage
from scripts.results import RESULTSPAGE
import pytest



# @pytest.mark.usefixtures('setup')
class Testlogin():


    def test_login(self,search='capital'):
        driver = self.driver
        home = homepage(driver)
        home.enter_text_in_searchbox(search)
        results=home.search_list()
        print(results)
        if search in str(results):
            print('Test passed')
        else:
            print('test failed')

    @pytest.mark.parametrize("search", ["Saturn","Saturday's Market","Krux"])
    def test_getting_create_count(self,search):
        driver = self.driver
        home = homepage(driver)
        home.selecting_search_keyword(search)
        results = RESULTSPAGE(driver)
        results.getting_creative_count()

    def test_verify_random_link_in_searchbox(self,search='Saturn'):
        driver = self.driver
        home = homepage(driver)
        home.selecting_search_keyword(search)
        results = RESULTSPAGE(driver)
        results.getting_creative_count()
        stauts=results.verify_random_link_enabled()
        assert stauts==True,'test failed'
        print(stauts)
        url=results.get_random_link()
        print('Random Link URL is :',url)

    def test_verify_share_link_on_ad(self,search='Saturn'):
        driver = self.driver
        home = homepage(driver)
        home.selecting_search_keyword(search)
        results = RESULTSPAGE(driver)
        results.checking_popup_share_link()

