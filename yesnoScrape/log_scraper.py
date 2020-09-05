import pyautogui
import pytesseract
from PIL import Image, ImageFilter


class LogScaperException(Exception):
    raise


class LogScraper:
    def __init__(self, ally_names, enemy_names=[], current_page=1)
        self.ally_names = ally_names
        self.enemy_names = enemy_names
        self.current_page = current_page
        self.total_pages = None
        self.current_log = None
        self.previous_log = None
        self.log_coords = None
        self.button_locations = None
        self.raw_logs = ""
        self.log_count = 0

    def get_all_logs(self):
        # self.set_button_locations
        # self.get_log_coords
        # self.get_total_pages
        # prevoius_log = None
        # for page in pages
        # current_log = get_log
        # self.raw_logs + current_log
        pass

    def get_log(self):
        # take_screenshot_of_log with self.log_coords
        # new_log = self.read_logs
        # if current_log, previous = current_log
        # self.current_log = new_log
        # return current_log
        pass

    def read_log(self, new_log):
        # Fuck with new log colors so that it can be more easily read
        # source[B].point(lambda i: i > 105 and 255)
        # convert new_log into text
        # return new_log_text
        pass

    def take_screenshot_of_log(self):
        # take screenshot with log_coords
        new_screenshot = pyautogui.screenshot(f'/log_screenshots/log_screenshot_{self.log_count}.png')
        self.log_count += 1
        # return the image
        return new_screenshot

    def scroll_down(self):
        # Scroll down to get more log entries.
        # _is_at_end_of_page check
        # if false screenshot and scrape return true
        # if true _go_to_next_page return false
        pass

    def go_to_next_page(self):
        # click next page buttons
        pyautogui.click(pyautogui.center(self.button_locations['next_page']))
        pass

    def is_at_end_of_page(self):
        # Check if the first entry of the current log is a duplicate from previous logs
        # Check if the first entry of the current log is an incomplete
        pass

    def _set_button_locations(self):
        # locate all, summon, back and next page (maybe do this on init?)
        all_loc = pyautogui.locateOnScreen('./images/all_dir_button.png')
        summon_loc = pyautogui.locateOnScreen('./images/summon_dir_button.png')
        back_loc = pyautogui.locateOnScreen('./images/back_button.png')
        next_loc = pyautogui.locateOnScreen('./images/next_page_button.png')

        if not all_loc or not summon_loc or not back_loc or not next_loc:
            print('Could not find one of the buttons. Crashing and burning in a storm of hellfire and brimstone.')
            raise LogScaperException()

        # set the self.button_locations variable
        self.button_locations['all'] = all_loc
        self.button_locations['summon'] = summon_loc
        self.button_locations['next_page'] = back_loc
        self.button_locations['back_button'] = next_loc

    def _get_log_region(self):
        # Using the all button, summon button, and next page button, get the coords needed to screenshot the logs
        left = self.button_locations['all'].left
        top = self.button_locations['all'].top - self.button_locations['all'].height
        width = self.button_locations['summon'].left + self.button_locations['summon'].width
        height = self.button_locations['next_page'].top - top
        return (left, top, width, height)

    def _get_page_number_region(self):
        # Use coords of back & next page to take screenshot of where page numbers variable
        left = self.button_locations['back_button'].left + self.button_locations['back_button'].width
        top = self.button_locations['back_button'].top
        width = self.button_locations['next_page'].left - left
        height = self.button_locations['back_button'].height
        return (left, top, width, height)

    def _get_page_numbers(self):
        # take new_screenshot of current page number
        page_numbers_image = pyautogui.screenshot(region=(self._get_page_number_region))
        # parse for page numbers
        current_page_raw, total_pages_raw = _make_log_text_parseable(page_numbers_image)
        try:
            current_page = int(current_page_raw)
            total_pages = int(total_pages_raw)
        except ValueError:
            print(f'Got a page number that could not be turned into an int. ({current_page_raw}/{total_pages_raw})')
            raise LogScaperException(f'Got a page number that could not be turned into an int. \
                                        ({current_page_raw}/{total_pages_raw})')
        return current_page, total_pages

    def _make_log_text_parsable(self, log_image):
        # Fuck with new log colors so that it can be more easily read
        source = log_image.split()
        updated_source = source[2].point(lambda i: i > 105 and 255)
        return updated_source


    def _page_numbers_from_image(self, page_numbers_image):
        # Make blurry numbers less blurry so they can be read
        parsable_numbers = page_numbers_image.filter(ImageFilter.EDGE_ENHANCE)
        page_numbers_raw = pytesseract.image_to_string(parsable_numbers)
        page_numbers = page_numbers_raw.split('\n')[0]
        current_page, total_pages = page_numbers.split('/')
        return current_page, total_pages
