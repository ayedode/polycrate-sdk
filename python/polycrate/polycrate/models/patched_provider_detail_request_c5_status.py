from typing import Literal

PatchedProviderDetailRequestC5Status = Literal["none", "planned", "typ1", "typ2"]

PATCHED_PROVIDER_DETAIL_REQUEST_C5_STATUS_VALUES: set[PatchedProviderDetailRequestC5Status] = {
    "none",
    "planned",
    "typ1",
    "typ2",
}


def check_patched_provider_detail_request_c5_status(value: str) -> PatchedProviderDetailRequestC5Status:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_C5_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_C5_STATUS_VALUES!r}")
