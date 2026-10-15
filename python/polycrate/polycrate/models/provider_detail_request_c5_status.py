from typing import Literal

ProviderDetailRequestC5Status = Literal["none", "planned", "typ1", "typ2"]

PROVIDER_DETAIL_REQUEST_C5_STATUS_VALUES: set[ProviderDetailRequestC5Status] = {
    "none",
    "planned",
    "typ1",
    "typ2",
}


def check_provider_detail_request_c5_status(value: str) -> ProviderDetailRequestC5Status:
    if value in PROVIDER_DETAIL_REQUEST_C5_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_C5_STATUS_VALUES!r}")
