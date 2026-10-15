from typing import Literal

ProviderDetailDedicatedAvailable = Literal["", "no", "planned", "yes"]

PROVIDER_DETAIL_DEDICATED_AVAILABLE_VALUES: set[ProviderDetailDedicatedAvailable] = {
    "",
    "no",
    "planned",
    "yes",
}


def check_provider_detail_dedicated_available(value: str) -> ProviderDetailDedicatedAvailable:
    if value in PROVIDER_DETAIL_DEDICATED_AVAILABLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_DEDICATED_AVAILABLE_VALUES!r}")
