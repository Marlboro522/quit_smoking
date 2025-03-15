"""Program for replacing my smoking urge with venting."""

from repository import UrgeRepository
from cli import DeviateCLI

if __name__ == "__main__":
    repo = UrgeRepository()
    cli = DeviateCLI(repo)
    cli.run()
