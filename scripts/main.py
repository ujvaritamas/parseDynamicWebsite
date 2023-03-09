import parser
import analytic
import handle_dynamic_webpage
import logger

logger = logger.create_logger()

inp_w = [
            {'url':"https://games.crossfit.com/leaderboard/open/2023?view=0&division=2&region=0&scaled=0&sort=0", 'dest': 'w0.html'},
            {'url':"https://games.crossfit.com/leaderboard/open/2023?view=0&division=2&region=0&scaled=0&sort=0&page=2", 'dest': 'w1.html'},
            {'url':"https://games.crossfit.com/leaderboard/open/2023?view=0&division=2&region=0&scaled=0&sort=0&page=3", 'dest': 'w2.html'},
            {'url':"https://games.crossfit.com/leaderboard/open/2023?view=0&division=2&region=0&scaled=0&sort=0&page=4", 'dest': 'w3.html'},
            {'url':"https://games.crossfit.com/leaderboard/open/2023?view=0&division=2&region=0&scaled=0&sort=0&page=5", 'dest': 'w4.html'}
        ]

inp_m = [
            {'url':"https://games.crossfit.com/leaderboard/open/2023?view=0&division=1&region=0&scaled=0&sort=0", 'dest': 'w0.html'},
            {'url':"https://games.crossfit.com/leaderboard/open/2023?view=0&division=1&region=0&scaled=0&sort=0&page=2", 'dest': 'w1.html'},
            {'url':"https://games.crossfit.com/leaderboard/open/2023?view=0&division=1&region=0&scaled=0&sort=0&page=3", 'dest': 'w2.html'},
            {'url':"https://games.crossfit.com/leaderboard/open/2023?view=0&division=1&region=0&scaled=0&sort=0&page=4", 'dest': 'w3.html'},
            {'url':"https://games.crossfit.com/leaderboard/open/2023?view=0&division=1&region=0&scaled=0&sort=0&page=5", 'dest': 'w4.html'}
        ]

webpage_handler = handle_dynamic_webpage.CfPageHandler()

logger.info("parse results")
webpage_handler.collect(inp_m)

p = parser.Parser()
p.parse_results()
p.log_athletes()


analytic = analytic.Analytic(p.athletes)

print(analytic.get_average_age())
print(analytic.get_average_weight())
print(analytic.get_average_height())\

logger.info("delete results")
webpage_handler.remove_tmp_dir()

