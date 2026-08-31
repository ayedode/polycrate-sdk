from typing import Literal

ApiV1OrganizationsCreateLegalNameErrorComponentAttr = Literal["legal_name"]

API_V1_ORGANIZATIONS_CREATE_LEGAL_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateLegalNameErrorComponentAttr
] = {
    "legal_name",
}


def check_api_v1_organizations_create_legal_name_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateLegalNameErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_LEGAL_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_LEGAL_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
