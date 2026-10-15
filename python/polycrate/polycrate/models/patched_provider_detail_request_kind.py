from typing import Literal

PatchedProviderDetailRequestKind = Literal["hardware", "infrastructure", "software"]

PATCHED_PROVIDER_DETAIL_REQUEST_KIND_VALUES: set[PatchedProviderDetailRequestKind] = {
    "hardware",
    "infrastructure",
    "software",
}


def check_patched_provider_detail_request_kind(value: str) -> PatchedProviderDetailRequestKind:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_KIND_VALUES!r}")
