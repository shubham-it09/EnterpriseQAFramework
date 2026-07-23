from datetime import datetime
from pathlib import Path


class ArtifactManager:
    """
    Creates and manages framework artifact folders.
    """

    _run_folder = (
        Path("artifacts")
        / datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    )

    @classmethod
    def get_logs_folder(cls) -> Path:
        """
        Returns logs folder for current execution.
        """

        path = cls._run_folder / "logs"
        print("Path :", path)
        print("Exists before :", path.exists())

        path.mkdir(
            parents=True,
            exist_ok=True
        )
        print("Exists after :", path.exists())

        return path

    @classmethod
    def get_screenshots_folder(cls) -> Path:
        """
        Returns screenshots folder for current execution.
        """

        path = cls._run_folder / "screenshots"
        print("Path :", path)
        print("Exists before :", path.exists())

        path.mkdir(
            parents=True,
            exist_ok=True
        )
        print("Exists after :", path.exists())
        return path



if __name__ == "__main__":

    logs = ArtifactManager.get_logs_folder()
    screenshots = ArtifactManager.get_screenshots_folder()

    print(logs.resolve())
    print(screenshots.resolve())