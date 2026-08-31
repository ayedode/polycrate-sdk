from typing import Literal

ApiV1DatasourcesIngestCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_DATASOURCES_INGEST_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesIngestCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_datasources_ingest_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1DatasourcesIngestCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_DATASOURCES_INGEST_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_INGEST_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
