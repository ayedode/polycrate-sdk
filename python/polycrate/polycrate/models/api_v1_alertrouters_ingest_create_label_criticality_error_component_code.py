from typing import Literal

ApiV1AlertroutersIngestCreateLabelCriticalityErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTROUTERS_INGEST_CREATE_LABEL_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersIngestCreateLabelCriticalityErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alertrouters_ingest_create_label_criticality_error_component_code(
    value: str,
) -> ApiV1AlertroutersIngestCreateLabelCriticalityErrorComponentCode:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_LABEL_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_LABEL_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
