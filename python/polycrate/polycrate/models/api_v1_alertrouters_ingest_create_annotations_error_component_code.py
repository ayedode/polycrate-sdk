from typing import Literal

ApiV1AlertroutersIngestCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_ALERTROUTERS_INGEST_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersIngestCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_alertrouters_ingest_create_annotations_error_component_code(
    value: str,
) -> ApiV1AlertroutersIngestCreateAnnotationsErrorComponentCode:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
