from typing import Literal

ProviderDetailC5Status = Literal["none", "planned", "typ1", "typ2"]

PROVIDER_DETAIL_C5_STATUS_VALUES: set[ProviderDetailC5Status] = {
    "none",
    "planned",
    "typ1",
    "typ2",
}


def check_provider_detail_c5_status(value: str) -> ProviderDetailC5Status:
    if value in PROVIDER_DETAIL_C5_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_C5_STATUS_VALUES!r}")
