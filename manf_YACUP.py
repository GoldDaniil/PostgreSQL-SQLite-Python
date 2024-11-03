import sys
from collections import defaultdict
import uuid


class ArtefactSystem:
    def __init__(self):
        self.parts_to_artefact = {}
        self.artefacts = {}

    def create(self, part_id):
        if part_id in self.parts_to_artefact:
            return "ERROR: EXISTING PART"

        artefact_id = self.generate_artefact_id()
        self.parts_to_artefact[part_id] = artefact_id
        self.artefacts[artefact_id] = {part_id}
        return artefact_id

    def merge(self, artefact_id1, artefact_id2):
        if artefact_id1 not in self.artefacts or artefact_id2 not in self.artefacts:
            return "ERROR: NO SUCH ARTEFACT"

        new_artefact_id = self.generate_artefact_id()
        new_parts = self.artefacts[artefact_id1].union(self.artefacts[artefact_id2])

        for part in new_parts:
            self.parts_to_artefact[part] = new_artefact_id

        self.artefacts[new_artefact_id] = new_parts

        del self.artefacts[artefact_id1]
        del self.artefacts[artefact_id2]

        return new_artefact_id

    def get_parts(self, artefact_id):
        if artefact_id not in self.artefacts:
            return "ERROR: NO SUCH ARTEFACT"

        return " ".join(sorted(self.artefacts[artefact_id]))

    def generate_artefact_id(self):
        return str(uuid.uuid4())[:8]


def main():
    system = ArtefactSystem()

    for line in sys.stdin:
        command = line.strip().split()

        if command[0] == "CREATE":
            part_id = command[1]
            result = system.create(part_id)
            print(result)

        elif command[0] == "MERGE":
            artefact_id1 = command[1]
            artefact_id2 = command[2]
            result = system.merge(artefact_id1, artefact_id2)
            print(result)

        elif command[0] == "GET":
            if command[1] == "PARTS":
                artefact_id = command[2]
                result = system.get_parts(artefact_id)
                print(result)

        elif command[0] == "EXIT":
            break


if __name__ == "__main__":
    main()
