from urllib import request
from project import Project
import toml



class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)
        toml_string = content
        parsed = toml.loads(toml_string)
        print(parsed) #dictionary
        tool = parsed.get('tool')
        proj = tool.get('poetry')
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(proj.get('name'),proj.get('description'),proj.get('dependencies'),proj.get('dev-dependencies'))
