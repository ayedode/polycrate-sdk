from typing import Literal

ProviderDetailRequestVolumeDiscount = Literal["no", "planned", "unknown", "yes"]

PROVIDER_DETAIL_REQUEST_VOLUME_DISCOUNT_VALUES: set[ProviderDetailRequestVolumeDiscount] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_provider_detail_request_volume_discount(value: str) -> ProviderDetailRequestVolumeDiscount:
    if value in PROVIDER_DETAIL_REQUEST_VOLUME_DISCOUNT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_VOLUME_DISCOUNT_VALUES!r}")
