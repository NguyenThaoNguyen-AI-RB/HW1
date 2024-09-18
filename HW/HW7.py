class Programmer:
    def __init__(self, name, languages, skills):
        self.name = name
        self.languages = languages
        self.skills = skills
    def watch_course(self, course_name, language, skills_earned):
        self.course_name = course_name
        self.language = language
        self.skills_earned = skills_earned
        if self.language == self.languages:
            self.skills += self.skills_earned
            return f"{self.name} watched {self.course_name}"
        else:
            return f"{self.name} does not know {self.language}"
    def change_language(self, new_language, skills_needed):
        self.new_language = new_language
        self.skills_needed = skills_needed
        if self.skills >= self.skills_needed:
            if self.languages != self.new_language:
                previous_language = self.languages
                self.languages = self.new_language
                return f"{self.name} switched from {previous_language} to {new_language}"
            else:
                return f"{self.name} already knows {new_language}"
        else:
            needed_skills = skills_needed - self.skills
            return f"{self.name} needs {needed_skills} more skills"
programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
