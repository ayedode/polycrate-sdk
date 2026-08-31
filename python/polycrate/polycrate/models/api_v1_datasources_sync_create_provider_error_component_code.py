from typing import Literal

ApiV1DatasourcesSyncCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DATASOURCES_SYNC_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesSyncCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_datasources_sync_create_provider_error_component_code(
    value: str,
) -> ApiV1DatasourcesSyncCreateProviderErrorComponentCode:
    if value in API_V1_DATASOURCES_SYNC_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
