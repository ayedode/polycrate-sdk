from typing import Literal

PatchedProviderDetailRequestVolumeDiscount = Literal["no", "planned", "unknown", "yes"]

PATCHED_PROVIDER_DETAIL_REQUEST_VOLUME_DISCOUNT_VALUES: set[PatchedProviderDetailRequestVolumeDiscount] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_patched_provider_detail_request_volume_discount(value: str) -> PatchedProviderDetailRequestVolumeDiscount:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_VOLUME_DISCOUNT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_VOLUME_DISCOUNT_VALUES!r}"
    )
