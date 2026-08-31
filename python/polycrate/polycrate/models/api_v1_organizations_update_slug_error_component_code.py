from typing import Literal

ApiV1OrganizationsUpdateSlugErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed", "unique"
]

API_V1_ORGANIZATIONS_UPDATE_SLUG_ERROR_COMPONENT_CODE_VALUES: set[ApiV1OrganizationsUpdateSlugErrorComponentCode] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
    "unique",
}


def check_api_v1_organizations_update_slug_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdateSlugErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_SLUG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_SLUG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
