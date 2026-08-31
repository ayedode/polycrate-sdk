from typing import Literal

ApiV1DatasourcesListKind = Literal["api", "otc-status", "polycrate-hub", "rss", "webhook"]

API_V1_DATASOURCES_LIST_KIND_VALUES: set[ApiV1DatasourcesListKind] = {
    "api",
    "otc-status",
    "polycrate-hub",
    "rss",
    "webhook",
}


def check_api_v1_datasources_list_kind(value: str) -> ApiV1DatasourcesListKind:
    if value in API_V1_DATASOURCES_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_LIST_KIND_VALUES!r}")
