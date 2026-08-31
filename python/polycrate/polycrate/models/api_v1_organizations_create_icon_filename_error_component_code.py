from typing import Literal

ApiV1OrganizationsCreateIconFilenameErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ORGANIZATIONS_CREATE_ICON_FILENAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsCreateIconFilenameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_organizations_create_icon_filename_error_component_code(
    value: str,
) -> ApiV1OrganizationsCreateIconFilenameErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_CREATE_ICON_FILENAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_ICON_FILENAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
