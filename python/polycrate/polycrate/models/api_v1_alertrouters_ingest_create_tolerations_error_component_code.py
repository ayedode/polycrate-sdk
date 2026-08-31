from typing import Literal

ApiV1AlertroutersIngestCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTROUTERS_INGEST_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersIngestCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alertrouters_ingest_create_tolerations_error_component_code(
    value: str,
) -> ApiV1AlertroutersIngestCreateTolerationsErrorComponentCode:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
