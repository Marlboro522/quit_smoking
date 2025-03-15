class UrgeEntry:
    def __init__(self, timestamp: str, intensity: int, note: str = ""):
        self.timestamp = timestamp
        self.intensity = intensity
        self.note=note
    
    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "intensity": self.intensity,
            "note": self.note
        }
    
    @staticmethod
    def from_dict(data: dict):
        return UrgeEntry(data["timestamp"], data["intensity"], data.get("note", ""))

    def __str__(self):
        return f"Timestamp: {self.timestamp}, Intensity: {self.intensity}, Note: {self.note}"

