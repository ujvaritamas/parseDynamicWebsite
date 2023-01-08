import parser
import analytic
import handle_dynamic_webpage
import logger

logger = logger.create_logger()

inp_w = [
            {'url':"https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0", 'dest': 'w0.html'},
            {'url':"https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0&page=2", 'dest': 'w1.html'}
        ]

webpage_handler = handle_dynamic_webpage.CfPageHandler()

logger.info("parse woman results")
webpage_handler.collect(inp_w)

p = parser.Parser()
p.parse_results()
p.log_athletes()


analytic = analytic.Analytic(p.athletes)

print(analytic.get_average_age())
print(analytic.get_average_weight())
print(analytic.get_average_height())\

logger.info("delete woman results")
webpage_handler.remove_tmp_dir()

