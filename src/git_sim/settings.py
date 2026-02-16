import pathlib
from typing import List, Union

from pydantic_settings import BaseSettings

from git_sim.enums import StyleOptions, ColorByOptions, ImgFormat, VideoFormat

class Settings(BaseSettings):
    all: bool = False
    allow_no_commits: bool = False
    animate: bool = False
    auto_open: bool = True
    color_by: Union[ColorByOptions, None] = None
    files: Union[List[pathlib.Path], None] = None
    fadeout: bool = False
    font_context: bool = False
    font: str = "Monospace"
    hide_first_tag: bool = False
    hide_merged_branches: bool = False
    highlight_commit_messages: bool = False
    img_format: ImgFormat = ImgFormat.JPG
    INFO_STRING: str = "Simulating:"
    invert_branches: bool = False
    light_mode: bool = False
    logo: pathlib.Path = pathlib.Path(__file__).parent.resolve() / "logo.png"
    low_quality: bool = False
    max_branches_per_commit: int = 1
    max_tags_per_commit: int = 1
    media_dir: pathlib.Path = pathlib.Path().cwd()
    n_default: int = 5
    n: int = 5
    output_only_path: bool = False
    outro_bottom_text: str = "Learn more at initialcommit.com"
    outro_top_text: str = "Thanks for using Initial Commit!"
    quiet: bool = False
    reverse: bool = False
    repo: str = ""
    show_command_as_title: bool = True
    show_intro: bool = False
    show_outro: bool = False
    speed: float = 1.5
    stdout: bool = False
    style: Union[StyleOptions, None] = StyleOptions.CLEAN
    title: str = "Git-Sim, by initialcommit.com"
    transparent_bg: bool = False
    use_colors: bool = False
    video_format: VideoFormat = VideoFormat.MP4

    class Config:
        env_prefix = "git_sim_"

settings = Settings()
