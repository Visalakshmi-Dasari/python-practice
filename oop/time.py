class Time():
    def __init__(self,seconds):
        self.seconds=seconds

    def convert_to_minutes(self):
        minutes=self.seconds/60
        remaining_seconds=self.seconds%60
        return str(minutes)+':'+str(remaining_seconds)

    def convert_to_hours(self):
        hours=self.seconds/3600
        remaining_seconds = self.seconds % 3600
        remaining_minutes = remaining_seconds / 60
        seconds_place = remaining_seconds % 60
        return str(hours)+':'+str(remaining_minutes)+':'+str(seconds_place)

test=Time(3800)
print test.convert_to_minutes()
print test.convert_to_hours()