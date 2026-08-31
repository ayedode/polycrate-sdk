from typing import Literal

ApiV1AlertroutersIngestCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_ALERTROUTERS_INGEST_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersIngestCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_alertrouters_ingest_create_criticality_error_component_code(
    value: str,
) -> ApiV1AlertroutersIngestCreateCriticalityErrorComponentCode:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
