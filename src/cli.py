from repository import UrgeRepository as rep
import argparse
from models import UrgeEntry
from datetime import datetime
class DeviateCLI:
    def __init__(self, urge_repository):
        self.urge_repository = urge_repository
     
    def run(self):
        parser = argparse.ArgumentParser(description='Deviate Urge Tracker')
        parser.add_argument('--mode', choices=['log', 'summary', 'list'], help='Operation mode')
        parser.add_argument('--intensity', type=int, help='Urge intensity')
        parser.add_argument('--note', help='Note for urge')
        parser.add_argument('--urge-id', type=int, help='Urge ID to delete or edit')
        args = parser.parse_args()
        if args.mode == 'log':
            self.log_urge(args.intensity, args.note)
            print('Urge logged successfully.')
        elif args.mode =='summary':
            self.show_summary()
        elif args.mode == 'list':
            self.list_urges()
            print('Listed logged urges.')
        else:
            print("Invalid mode. Use --mode log, summary, or list.")
        


    def log_urge(self, intensity: int, note: str = ""):
        now = datetime.now().isoformat(timespec='seconds')
        entry = UrgeEntry(timestamp=now, intensity=intensity, note=note)
        self.urge_repo.add_urge(entry)
        print(f" Logged urge at {entry.timestamp} with intensity {intensity}.")

    def list_urges(self):
        urges = self.urge_repo.get_all_urges()
        if not urges:
            print("No urges logged yet.")
            return
        print("\n Logged Urges:\n-----------------")
        for entry in urges:
            print(entry)

    def show_summary(self):
        summary = self.urge_repo.get_urge_summary()
        if not summary:
            print("No urges to summarize.")
            return
        print("\n Urge Summary by Date:\n-------------------------")
        for date, count in summary.items():
            print(f"{date}: {count} urges")
    
