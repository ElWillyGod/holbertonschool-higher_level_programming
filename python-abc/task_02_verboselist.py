#!/usr/bin/python3
"""class verboseList"""


class VerboseList(list):
    """lisr class"""

    def append(self, obj):
        """append"""

        super().append(obj)
        print(f"Added [{obj}] to the list.")

    def extend(self, obj):
        """extend"""

        super().extend(obj)
        print(f"Extended the list with [{len(obj)}] items.")

    def remove(self, obj):
        """remove"""

        super().remove(obj)
        print(f"Removed [{obj}] from the list.")

    def pop(self, obj):
        """pop"""

        super().pop(obj)
        if obj is None:
            print(f"Popped [{self[-1]}] from the list.")
        else:
            print(f"Popped [[self[obj]]] from the list.")
