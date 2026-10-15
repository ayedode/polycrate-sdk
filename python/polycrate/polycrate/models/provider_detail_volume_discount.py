from typing import Literal

ProviderDetailVolumeDiscount = Literal["no", "planned", "unknown", "yes"]

PROVIDER_DETAIL_VOLUME_DISCOUNT_VALUES: set[ProviderDetailVolumeDiscount] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_provider_detail_volume_discount(value: str) -> ProviderDetailVolumeDiscount:
    if value in PROVIDER_DETAIL_VOLUME_DISCOUNT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_VOLUME_DISCOUNT_VALUES!r}")
