from typing import Literal

DataSourceRequestKind = Literal["api", "otc-status", "polycrate-hub", "rss", "webhook"]

DATA_SOURCE_REQUEST_KIND_VALUES: set[DataSourceRequestKind] = {
    "api",
    "otc-status",
    "polycrate-hub",
    "rss",
    "webhook",
}


def check_data_source_request_kind(value: str) -> DataSourceRequestKind:
    if value in DATA_SOURCE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_SOURCE_REQUEST_KIND_VALUES!r}")
