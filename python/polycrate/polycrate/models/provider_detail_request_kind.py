from typing import Literal

ProviderDetailRequestKind = Literal["hardware", "infrastructure", "software"]

PROVIDER_DETAIL_REQUEST_KIND_VALUES: set[ProviderDetailRequestKind] = {
    "hardware",
    "infrastructure",
    "software",
}


def check_provider_detail_request_kind(value: str) -> ProviderDetailRequestKind:
    if value in PROVIDER_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_KIND_VALUES!r}")
