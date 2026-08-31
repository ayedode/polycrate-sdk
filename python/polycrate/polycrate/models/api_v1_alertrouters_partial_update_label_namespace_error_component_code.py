from typing import Literal

ApiV1AlertroutersPartialUpdateLabelNamespaceErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTROUTERS_PARTIAL_UPDATE_LABEL_NAMESPACE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersPartialUpdateLabelNamespaceErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alertrouters_partial_update_label_namespace_error_component_code(
    value: str,
) -> ApiV1AlertroutersPartialUpdateLabelNamespaceErrorComponentCode:
    if value in API_V1_ALERTROUTERS_PARTIAL_UPDATE_LABEL_NAMESPACE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_PARTIAL_UPDATE_LABEL_NAMESPACE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
