from comfy.comfy_types import IO


class WaitFor:
    """Delay returning a value until wait_for has executed (execution ordering)."""

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "wait_for": (IO.ANY,),
                "value": (IO.ANY,),
            },
        }

    RETURN_TYPES = (IO.ANY,)
    RETURN_NAMES = ("value",)
    FUNCTION = "wait"
    CATEGORY = "Comfyui_Qwen3-VL-Instruct"
    DESCRIPTION = "Returns value unchanged after wait_for finishes. Use to sequence model loads."

    def wait(self, wait_for, value):
        return (value,)


class WaitForString:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "wait_for": (IO.ANY,),
                "text": ("STRING", {"multiline": True, "default": ""}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "wait"
    CATEGORY = "Comfyui_Qwen3-VL-Instruct"
    DESCRIPTION = "Returns text after wait_for finishes. Use for negative prompts gated on purge."

    def wait(self, wait_for, text):
        return (text,)
