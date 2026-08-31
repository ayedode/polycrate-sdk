from typing import Literal

ApiV1DatasourcesListKindErrorComponentCode = Literal["invalid_choice"]

API_V1_DATASOURCES_LIST_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1DatasourcesListKindErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_datasources_list_kind_error_component_code(value: str) -> ApiV1DatasourcesListKindErrorComponentCode:
    if value in API_V1_DATASOURCES_LIST_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_LIST_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
