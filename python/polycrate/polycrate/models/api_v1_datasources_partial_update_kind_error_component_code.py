from typing import Literal

ApiV1DatasourcesPartialUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DATASOURCES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesPartialUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_datasources_partial_update_kind_error_component_code(
    value: str,
) -> ApiV1DatasourcesPartialUpdateKindErrorComponentCode:
    if value in API_V1_DATASOURCES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
