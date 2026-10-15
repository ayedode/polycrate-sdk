from typing import Literal

ProviderDetailIso27001Status = Literal["no", "planned", "unknown", "yes"]

PROVIDER_DETAIL_ISO_27001_STATUS_VALUES: set[ProviderDetailIso27001Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_provider_detail_iso_27001_status(value: str) -> ProviderDetailIso27001Status:
    if value in PROVIDER_DETAIL_ISO_27001_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_ISO_27001_STATUS_VALUES!r}")
