from typing import Literal

ApiV1OrganizationsPartialUpdateLegalNameErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed", "unique"
]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_LEGAL_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsPartialUpdateLegalNameErrorComponentCode
] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
    "unique",
}


def check_api_v1_organizations_partial_update_legal_name_error_component_code(
    value: str,
) -> ApiV1OrganizationsPartialUpdateLegalNameErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_LEGAL_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_LEGAL_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
