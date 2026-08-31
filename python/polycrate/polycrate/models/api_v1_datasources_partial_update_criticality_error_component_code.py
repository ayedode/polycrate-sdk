from typing import Literal

ApiV1DatasourcesPartialUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_DATASOURCES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesPartialUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_datasources_partial_update_criticality_error_component_code(
    value: str,
) -> ApiV1DatasourcesPartialUpdateCriticalityErrorComponentCode:
    if value in API_V1_DATASOURCES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
