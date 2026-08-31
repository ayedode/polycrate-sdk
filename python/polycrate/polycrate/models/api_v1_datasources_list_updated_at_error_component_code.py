from typing import Literal

ApiV1DatasourcesListUpdatedAtErrorComponentCode = Literal["invalid"]

API_V1_DATASOURCES_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1DatasourcesListUpdatedAtErrorComponentCode] = {
    "invalid",
}


def check_api_v1_datasources_list_updated_at_error_component_code(
    value: str,
) -> ApiV1DatasourcesListUpdatedAtErrorComponentCode:
    if value in API_V1_DATASOURCES_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
