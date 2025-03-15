import json
import os
from models import UrgeEntry
from datetime import datetime

class UrgeRepository:
    def __init__(self, storage_path = None):
        self.storage_path = storage_path or "urges.json"
        dir_path = os.path.dirname(self.storage_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        if not os.path.exists(self.storage_path):
            with open(self.storage_path, "r") as file:
                json.dump([],file)

    def load_urges(self):
        with open(self.storage_path, "r") as file:
            data = json.load(file)
            return [UrgeEntry.from_dict(entry) for entry in data]
    
    def save_urges(self,entries):
        with open(self.storage_path, "w") as file:
            json.dump([entry.to_dict() for entry in entries], file,indent=2)
    
    def add_urge(self, urge_entry: UrgeEntry):
        entries = self.load_urges()
        entries.append(urge_entry)
        self.save_urges(entries)
    
    def get_all_urges(self):
        return self.load_urges()
    
    def get_urge_by_id(self, urge_id: int):
        entries = self.load_urges()
        return next((entry for entry in entries if entry.timestamp == urge_id), None)
    
    def get_urge_summary(self):
        entries = self._load_entries()
        summary = {}
        for entry in entries:
            date = entry.timestamp.split("T")[0]
            summary[date] = summary.get(date, 0) + 1
        return summary

