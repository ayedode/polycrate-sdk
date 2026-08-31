from typing import Literal

ApiV1AlertroutersIngestCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ALERTROUTERS_INGEST_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersIngestCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_alertrouters_ingest_create_provider_error_component_code(
    value: str,
) -> ApiV1AlertroutersIngestCreateProviderErrorComponentCode:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
