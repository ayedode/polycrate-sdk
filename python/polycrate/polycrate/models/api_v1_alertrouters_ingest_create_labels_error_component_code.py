from typing import Literal

ApiV1AlertroutersIngestCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_ALERTROUTERS_INGEST_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersIngestCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_alertrouters_ingest_create_labels_error_component_code(
    value: str,
) -> ApiV1AlertroutersIngestCreateLabelsErrorComponentCode:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
