from typing import Literal

ApiV1OrganizationsDiscoverCreateLegalNameErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed", "unique"
]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_LEGAL_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsDiscoverCreateLegalNameErrorComponentCode
] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
    "unique",
}


def check_api_v1_organizations_discover_create_legal_name_error_component_code(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateLegalNameErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_LEGAL_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_LEGAL_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
