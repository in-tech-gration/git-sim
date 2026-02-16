import sys
import git
import manim as m

from typing import List

from git_sim.git_sim_base_command import GitSimBaseCommand
from git_sim.settings import settings


class Add(GitSimBaseCommand):

    def __init__(self, files: List[str]):
        super().__init__()
        self.hide_first_tag = True
        self.allow_no_commits = True
        self.files = files
        settings.hide_merged_branches = True
        self.n = self.n_default

        try:
            self.selected_branches.append(self.repo.active_branch.name)
        except TypeError:
            pass

        for file in self.files:
            if file not in [modified_file.a_path for modified_file in self.repo.index.diff(None)] + [
                untracked_file for untracked_file in self.repo.untracked_files
            ]:
                print(f"git-sim error: No modified file with name: '{file}'")
                sys.exit()

        self.cmd += f"{type(self).__name__.lower()} {' '.join(self.files)}"

    def construct(self):
        if not settings.stdout and not settings.output_only_path and not settings.quiet:
            print(f"{settings.INFO_STRING} {self.cmd}")

        self.show_intro()
        self.parse_commits()
        self.recenter_frame()
        self.scale_frame()
        self.vsplit_frame()
        self.setup_and_draw_zones()
        self.show_command_as_title()
        self.fadeout()
        self.show_outro()

    def populate_zones(
        self,
        firstColumnFileNames,
        secondColumnFileNames,
        thirdColumnFileNames,
        firstColumnArrowMap={},
        secondColumnArrowMap={},
        thirdColumnArrowMap={},
    ):
        # modified_file in here, might not be the most precise term. Using for now. Keep an eye on it.
        for modified_file in self.repo.index.diff(None):
            print("modified_file", modified_file)
            if "git-sim_media" not in modified_file.a_path:
                secondColumnFileNames.add(modified_file.a_path)
                for file in self.files:
                    if file == modified_file.a_path:
                        thirdColumnFileNames.add(modified_file.a_path)
                        secondColumnArrowMap[modified_file.a_path] = m.Arrow(
                            stroke_width=3, color=self.fontColor
                        )
        try:
            # TODO: Rename y to something more descriptive
            for y in self.repo.index.diff("HEAD"):
                if "git-sim_media" not in y.a_path:
                    thirdColumnFileNames.add(y.a_path)
        except git.exc.BadName:
            for (y, _stage), entry in self.repo.index.entries.items():
                if "git-sim_media" not in y:
                    thirdColumnFileNames.add(y)

        for untracked_file in self.repo.untracked_files:
            if "git-sim_media" not in untracked_file:
                firstColumnFileNames.add(untracked_file)
                for file in self.files:
                    if file == untracked_file:
                        thirdColumnFileNames.add(untracked_file)
                        firstColumnArrowMap[untracked_file] = m.Arrow(
                            stroke_width=3, color=self.fontColor
                        )
