from typing import Literal

ProviderDetailRequestCustomImages = Literal["", "no", "planned", "yes"]

PROVIDER_DETAIL_REQUEST_CUSTOM_IMAGES_VALUES: set[ProviderDetailRequestCustomImages] = {
    "",
    "no",
    "planned",
    "yes",
}


def check_provider_detail_request_custom_images(value: str) -> ProviderDetailRequestCustomImages:
    if value in PROVIDER_DETAIL_REQUEST_CUSTOM_IMAGES_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_CUSTOM_IMAGES_VALUES!r}")
