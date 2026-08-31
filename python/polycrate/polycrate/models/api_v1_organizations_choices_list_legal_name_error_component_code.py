from typing import Literal

ApiV1OrganizationsChoicesListLegalNameErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_ORGANIZATIONS_CHOICES_LIST_LEGAL_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsChoicesListLegalNameErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_organizations_choices_list_legal_name_error_component_code(
    value: str,
) -> ApiV1OrganizationsChoicesListLegalNameErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_CHOICES_LIST_LEGAL_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CHOICES_LIST_LEGAL_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
