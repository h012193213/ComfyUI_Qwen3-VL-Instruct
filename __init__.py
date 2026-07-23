from .nodes import Qwen3_VQA
from .util_nodes import ImageLoader, VideoLoader, VideoLoaderPath
from .path_nodes import MultiplePathsInput
from .wait_nodes import WaitFor, WaitForString

WEB_DIRECTORY = "./web"
# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Qwen3_VQA": Qwen3_VQA,
    "ImageLoader": ImageLoader,
    "VideoLoader": VideoLoader,
    "VideoLoaderPath": VideoLoaderPath,
    "MultiplePathsInput": MultiplePathsInput,
    "Qwen3WaitFor": WaitFor,
    "Qwen3WaitForString": WaitForString,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Qwen3_VQA": "Qwen3 VQA",
    "ImageLoader": "Load Image Advanced",
    "VideoLoader": "Load Video Advanced",
    "VideoLoaderPath": "Load Video Advanced (Path)",
    "MultiplePathsInput": "Multiple Paths Input",
    "Qwen3WaitFor": "Wait For (Qwen3)",
    "Qwen3WaitForString": "Wait For String (Qwen3)",
}
