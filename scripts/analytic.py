class Analytic:
    def __init__(self, athletes):
        self.athletes = athletes

    def get_average_age(self):
        avg_age = 0
        none_cnt = 0
        for athlete in self.athletes:
            if athlete.age:
                avg_age += athlete.age
            else:
                none_cnt += 1

        return avg_age/(len(self.athletes)-none_cnt)

    def get_average_weight(self):
        avg_weight = 0
        none_cnt = 0
        for athlete in self.athletes:
            if athlete.weight:
                avg_weight += athlete.weight
            else:
                none_cnt += 1

        return avg_weight/(len(self.athletes)-none_cnt)

    def get_average_height(self):
        avg_height = 0
        none_cnt = 0
        for athlete in self.athletes:
            if athlete.height:
                avg_height += athlete.height
            else:
                none_cnt += 1

        return avg_height/(len(self.athletes)-none_cnt)