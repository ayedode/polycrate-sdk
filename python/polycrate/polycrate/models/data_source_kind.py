from typing import Literal

DataSourceKind = Literal["api", "otc-status", "polycrate-hub", "rss", "webhook"]

DATA_SOURCE_KIND_VALUES: set[DataSourceKind] = {
    "api",
    "otc-status",
    "polycrate-hub",
    "rss",
    "webhook",
}


def check_data_source_kind(value: str) -> DataSourceKind:
    if value in DATA_SOURCE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_SOURCE_KIND_VALUES!r}")
