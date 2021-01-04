class homepage():

    def __init__(self, driver):
        self.driver = driver
        self.search_box_id = 'adsearch-input'
        self.search_list_class='search-bar-dropdown-row'
        self.search_list_link_class='search-bar-dropdown-row-info'

    def enter_text_in_searchbox(self,search):
        self.driver.find_element_by_id(self.search_box_id).send_keys(search)

    def search_list(self):
        search_results = self.driver.find_elements_by_class_name(self.search_list_class)
        list = []
        for result in search_results:
            list.append(result.text.lower())

        return list

    def selecting_search_keyword(self,search):
        self.enter_text_in_searchbox(search)
        results = self.driver.find_elements_by_class_name(self.search_list_link_class)
        for result in results:
            #print(result.text)
            if result.text == search:
                result.click()
                break
            else:
                print('No search results found with given keyword')




