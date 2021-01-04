from selenium.webdriver.common.action_chains import ActionChains


class RESULTSPAGE:

    def __init__(self, driver):
        self.driver = driver
        self.creative_count_testbox_class = 'creative-count'
        self.random_link_xpath = "//a[text()='Random Brand']"
        self.ad_popup_class = 'er-creative  '
        self.share_link_class = 'share-link'

    def getting_creative_count(self):
        value = self.driver.find_element_by_class_name(self.creative_count_testbox_class).text
        print('creative List is :', value)

    def verify_random_link_enabled(self):
        return self.driver.find_element_by_xpath(self.random_link_xpath).is_enabled()

    def get_random_link(self):
        return self.driver.find_element_by_xpath(self.random_link_xpath).get_attribute('href')

    def checking_popup_share_link(self):
        # get  element
        popup = self.driver.find_element_by_class_name(self.ad_popup_class)

        # create action chain object
        action = ActionChains(self.driver)

        # perform the operation
        action.move_to_element(popup).click().perform()
        return 'Share Link is enabled:', self.driver.find_element_by_class_name('share-link').is_enabled()
