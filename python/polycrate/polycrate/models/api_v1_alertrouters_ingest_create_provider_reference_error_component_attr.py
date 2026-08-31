from typing import Literal

ApiV1AlertroutersIngestCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_ALERTROUTERS_INGEST_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersIngestCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_alertrouters_ingest_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1AlertroutersIngestCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
