from typing import Literal

ApiV1DatasourcesSyncCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_SYNC_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesSyncCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_sync_create_tolerations_error_component_code(
    value: str,
) -> ApiV1DatasourcesSyncCreateTolerationsErrorComponentCode:
    if value in API_V1_DATASOURCES_SYNC_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
