import parser
import analytic


p = parser.Parser()
p.parse_results()
p.log_athletes()


analytic = analytic.Analytic(p.athletes)

print(analytic.get_average_age())
print(analytic.get_average_weight())
print(analytic.get_average_height())
