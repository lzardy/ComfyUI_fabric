from nodes import KSampler
from .fabric.fabric import fabric_sample


class KSamplerFABRIC:
    @classmethod
    def INPUT_TYPES(s):
        inputs = KSampler.INPUT_TYPES()
        added_inputs = {
            "required": {
                "null_pos": ("CONDITIONING",),
                "null_neg": ("CONDITIONING",),
                "pos_weight": ("FLOAT", {"default": 1., "min": 0., "max": 1., "step": 0.01}),
                "neg_weight": ("FLOAT", {"default": 1., "min": 0., "max": 1., "step": 0.01}),
                "feedback_start": ("INT", {"default": 1, "min": 1, "max": 10000, "step": 1}),
                "feedback_end": ("INT", {"default": 20, "min": 1, "max": 10000, "step": 1}),
            },
            "optional": {
                "pos_latents": ("LATENT",),
                "neg_latents": ("LATENT",),
            }
        }
        inputs["required"].update(added_inputs["required"])
        if "optional" not in inputs:
            inputs["optional"] = {}
        inputs["optional"].update(added_inputs["optional"])
        return inputs

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "sample"
    CATEGORY = "FABRIC"

    def sample(self, *args, **kwargs):
        return fabric_sample(*args, **kwargs)


NODE_CLASS_MAPPINGS = {
    "KSamplerFABRIC": KSamplerFABRIC,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "KSamplerFABRIC": "KSampler With FABRIC",
}
