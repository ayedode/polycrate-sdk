from typing import Literal

ApiV1DatasourcesIngestCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_DATASOURCES_INGEST_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesIngestCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_datasources_ingest_create_provider_error_component_attr(
    value: str,
) -> ApiV1DatasourcesIngestCreateProviderErrorComponentAttr:
    if value in API_V1_DATASOURCES_INGEST_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_INGEST_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
