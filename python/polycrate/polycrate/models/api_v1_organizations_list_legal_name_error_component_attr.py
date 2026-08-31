from typing import Literal

ApiV1OrganizationsListLegalNameErrorComponentAttr = Literal["legal_name"]

API_V1_ORGANIZATIONS_LIST_LEGAL_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsListLegalNameErrorComponentAttr
] = {
    "legal_name",
}


def check_api_v1_organizations_list_legal_name_error_component_attr(
    value: str,
) -> ApiV1OrganizationsListLegalNameErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_LIST_LEGAL_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_LIST_LEGAL_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
