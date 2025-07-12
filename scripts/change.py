# create project structure for agentkit

import os
import pathlib
from os import walk


if __name__ == "__main__":
    path = pathlib.Path(__file__).parent.parent / "agentkit"

    for root, dirs, files in walk(path):
        for file in files:
            if file.endswith(".py") and not file.startswith("__init__"):
                file_path = os.path.join(root, file)
                with open(file_path, "w") as f:
                    relative_path = pathlib.Path(file_path).relative_to(path)
                    import_path = (
                        relative_path.with_suffix("").as_posix().replace("/", ".")
                    )
                    f.write(f"from agents.{import_path} import * # noqa: F401, F403\n")
