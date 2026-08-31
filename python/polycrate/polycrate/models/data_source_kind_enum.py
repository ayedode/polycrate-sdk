from typing import Literal

DataSourceKindEnum = Literal["api", "otc-status", "polycrate-hub", "rss", "webhook"]

DATA_SOURCE_KIND_ENUM_VALUES: set[DataSourceKindEnum] = {
    "api",
    "otc-status",
    "polycrate-hub",
    "rss",
    "webhook",
}


def check_data_source_kind_enum(value: str) -> DataSourceKindEnum:
    if value in DATA_SOURCE_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_SOURCE_KIND_ENUM_VALUES!r}")
