from typing import Literal

ProviderDetailRequestIso27001Status = Literal["no", "planned", "unknown", "yes"]

PROVIDER_DETAIL_REQUEST_ISO_27001_STATUS_VALUES: set[ProviderDetailRequestIso27001Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_provider_detail_request_iso_27001_status(value: str) -> ProviderDetailRequestIso27001Status:
    if value in PROVIDER_DETAIL_REQUEST_ISO_27001_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_ISO_27001_STATUS_VALUES!r}")
