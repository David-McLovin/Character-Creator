'''
This class includes the optional additional information to be printed to keep the main file organized
'''
import tkinter as tk

class Information:

    def general(self, stringVar):
        stringVar.set("Dungeons and Dragons is a tabletop roleplaying game in which you create a fictional" + 
            " character to interact with the world around you. To create a character, you can either build" +
             " one manually or use the automated character generator.")


    def race(self, stringVar):
        stringVar.set("There are a variety of different lands and cultures in the world of D&D, with a variety" + 
            " of races to match. Each of the races comes with unique special abilities or skills, as shown below.\n\n")

    def dnd_class(self, stringVar):
        stringVar.set("Classes are essentially the job or role of your character. These influence a character's skills"
         + "and the methods they may use to interact with the world, whether it be through brute force or "
         + "more subtle tactics.\n\n")

    def stats(self, stringVar):
        stringVar.set(stringVar.get() + "Stats are your character's proficiencies with different skills, such as strength or charisma. You "
        + "will use these stats when you interact with the world, to determine how efficient you are in the "
        + "task at hand. Higher stats mean you're more likely to be able to do an action, such as lifting a "
        + "boulder or shooting a bow. You can either accept the default stats or roll for your own.\n\n")