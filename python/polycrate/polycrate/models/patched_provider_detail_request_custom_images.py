from typing import Literal

PatchedProviderDetailRequestCustomImages = Literal["", "no", "planned", "yes"]

PATCHED_PROVIDER_DETAIL_REQUEST_CUSTOM_IMAGES_VALUES: set[PatchedProviderDetailRequestCustomImages] = {
    "",
    "no",
    "planned",
    "yes",
}


def check_patched_provider_detail_request_custom_images(value: str) -> PatchedProviderDetailRequestCustomImages:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_CUSTOM_IMAGES_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_CUSTOM_IMAGES_VALUES!r}"
    )
