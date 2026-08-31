from typing import Literal

ApiV1AlertroutersIngestCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_ALERTROUTERS_INGEST_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersIngestCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_alertrouters_ingest_create_provider_error_component_attr(
    value: str,
) -> ApiV1AlertroutersIngestCreateProviderErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
