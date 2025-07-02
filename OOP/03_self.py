class AnimalVoices:
  name="Lion"
  voice = "Roar"
  def make_sound(self):
      print(f"{self.name} makes a {self.voice} sound")
      return self.voice
animal = AnimalVoices()
animal.name = "Women"
animal.voice = "Curl"
animal.make_sound()


