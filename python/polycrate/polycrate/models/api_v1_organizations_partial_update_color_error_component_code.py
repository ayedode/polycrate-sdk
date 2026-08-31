from typing import Literal

ApiV1OrganizationsPartialUpdateColorErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_COLOR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsPartialUpdateColorErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_organizations_partial_update_color_error_component_code(
    value: str,
) -> ApiV1OrganizationsPartialUpdateColorErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_COLOR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_COLOR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
