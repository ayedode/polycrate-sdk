from typing import Literal

ApiV1DatasourcesSyncCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_DATASOURCES_SYNC_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesSyncCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_datasources_sync_create_criticality_error_component_code(
    value: str,
) -> ApiV1DatasourcesSyncCreateCriticalityErrorComponentCode:
    if value in API_V1_DATASOURCES_SYNC_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
