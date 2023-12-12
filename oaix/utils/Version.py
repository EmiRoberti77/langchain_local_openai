class Version:
    def __init__(self) -> None:
        self.version: str = "v 0.1.5"
        self.name: str = ("oaix",)
        self.description: str = "gen ai engine"

    def toJson(self):
        return {
            "version": self.version,
            "name": self.name,
            "description": self.description,
        }
