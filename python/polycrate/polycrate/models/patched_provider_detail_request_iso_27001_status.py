from typing import Literal

PatchedProviderDetailRequestIso27001Status = Literal["no", "planned", "unknown", "yes"]

PATCHED_PROVIDER_DETAIL_REQUEST_ISO_27001_STATUS_VALUES: set[PatchedProviderDetailRequestIso27001Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_patched_provider_detail_request_iso_27001_status(value: str) -> PatchedProviderDetailRequestIso27001Status:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_ISO_27001_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_ISO_27001_STATUS_VALUES!r}"
    )
