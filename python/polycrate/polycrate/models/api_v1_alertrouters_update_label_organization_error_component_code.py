from typing import Literal

ApiV1AlertroutersUpdateLabelOrganizationErrorComponentCode = Literal[
    "blank", "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTROUTERS_UPDATE_LABEL_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersUpdateLabelOrganizationErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alertrouters_update_label_organization_error_component_code(
    value: str,
) -> ApiV1AlertroutersUpdateLabelOrganizationErrorComponentCode:
    if value in API_V1_ALERTROUTERS_UPDATE_LABEL_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_UPDATE_LABEL_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
