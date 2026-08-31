from typing import Literal

ApiV1DatasourcesListScope = Literal["system", "user"]

API_V1_DATASOURCES_LIST_SCOPE_VALUES: set[ApiV1DatasourcesListScope] = {
    "system",
    "user",
}


def check_api_v1_datasources_list_scope(value: str) -> ApiV1DatasourcesListScope:
    if value in API_V1_DATASOURCES_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_LIST_SCOPE_VALUES!r}")
