from typing import Literal

ProviderDetailCustomImages = Literal["", "no", "planned", "yes"]

PROVIDER_DETAIL_CUSTOM_IMAGES_VALUES: set[ProviderDetailCustomImages] = {
    "",
    "no",
    "planned",
    "yes",
}


def check_provider_detail_custom_images(value: str) -> ProviderDetailCustomImages:
    if value in PROVIDER_DETAIL_CUSTOM_IMAGES_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_CUSTOM_IMAGES_VALUES!r}")
