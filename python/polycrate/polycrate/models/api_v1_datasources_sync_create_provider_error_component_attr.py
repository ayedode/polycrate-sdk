from typing import Literal

ApiV1DatasourcesSyncCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_DATASOURCES_SYNC_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesSyncCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_datasources_sync_create_provider_error_component_attr(
    value: str,
) -> ApiV1DatasourcesSyncCreateProviderErrorComponentAttr:
    if value in API_V1_DATASOURCES_SYNC_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
