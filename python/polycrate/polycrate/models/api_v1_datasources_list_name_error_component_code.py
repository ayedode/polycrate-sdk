from typing import Literal

ApiV1DatasourcesListNameErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_DATASOURCES_LIST_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1DatasourcesListNameErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_datasources_list_name_error_component_code(value: str) -> ApiV1DatasourcesListNameErrorComponentCode:
    if value in API_V1_DATASOURCES_LIST_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_LIST_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
