from typing import Literal

PatchedDataSourceRequestKind = Literal["api", "otc-status", "polycrate-hub", "rss", "webhook"]

PATCHED_DATA_SOURCE_REQUEST_KIND_VALUES: set[PatchedDataSourceRequestKind] = {
    "api",
    "otc-status",
    "polycrate-hub",
    "rss",
    "webhook",
}


def check_patched_data_source_request_kind(value: str) -> PatchedDataSourceRequestKind:
    if value in PATCHED_DATA_SOURCE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_DATA_SOURCE_REQUEST_KIND_VALUES!r}")
