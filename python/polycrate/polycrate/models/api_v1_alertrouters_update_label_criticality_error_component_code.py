from typing import Literal

ApiV1AlertroutersUpdateLabelCriticalityErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTROUTERS_UPDATE_LABEL_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersUpdateLabelCriticalityErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alertrouters_update_label_criticality_error_component_code(
    value: str,
) -> ApiV1AlertroutersUpdateLabelCriticalityErrorComponentCode:
    if value in API_V1_ALERTROUTERS_UPDATE_LABEL_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_UPDATE_LABEL_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
