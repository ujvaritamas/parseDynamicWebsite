from bs4 import BeautifulSoup
import os
import logger

class Athlete():
    def __init__(self, logger_obj):
        self.name = None
        self.info = None
        self.rank = None
        self.judge = None
        self.logger = logger_obj

    def log_athlete(self):
        self.logger.debug('=============Athlete==============')
        self.logger.debug("name: {}".format(self.name))
        self.logger.debug("info: {}".format(self.info))
        self.logger.debug("rank: {}".format(self.rank))
        self.logger.debug("judge: {}".format(self.judge))
        self.logger.debug('=============Athlete==============')


class Parser():
    def __init__(self):
        self.logger = logger.create_logger()
        #TODO corrected later
        self._temp_folder_path = os.path.join(os.path.dirname(__file__), 'temp_folder')
        self.athletes = []


    def parse_results(self):
        files = os.listdir(self._temp_folder_path)

        for html_file in os.listdir(self._temp_folder_path):
            html_file_path = os.path.join(self._temp_folder_path, html_file)

            self.parse_file(html_file_path)

            

        self.logger.debug("html files: {}".format(files))

    def log_athletes(self):
        for athlete in self.athletes:
            athlete.log_athlete()

    def parse_file(self, html_file_path):
        #open the file
        with open(html_file_path) as fp:
            soup = BeautifulSoup(fp, "html.parser")

        leaderboard = soup.find_all(class_='main-content loading')

        for l in leaderboard:
            children = l.find_all(True)

        athlete = None
        for child in children:
            value = child.get('value')
            id = child.get('id')
            c = child.get('class')

            if c == ['expand']:
                if athlete:
                    self.athletes.append(athlete)
                athlete = Athlete(self.logger)

            if c == ['first-name']:
                first_name = child.contents[0]
            if c == ['last-name']:
                last_name = child.contents[0]
                athlete.name = first_name + ' ' + last_name
            if c == ['info']:
                info = child.contents
                athlete.info = info
            if c == ['rank']:
                rank = child.contents
                athlete.rank = rank
            if c == ['judge']:
                judge = child.contents
                athlete.judge = judge
                


            


p = Parser()
p.parse_results()
p.log_athletes()