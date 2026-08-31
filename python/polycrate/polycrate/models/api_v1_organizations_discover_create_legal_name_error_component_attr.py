from typing import Literal

ApiV1OrganizationsDiscoverCreateLegalNameErrorComponentAttr = Literal["legal_name"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_LEGAL_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateLegalNameErrorComponentAttr
] = {
    "legal_name",
}


def check_api_v1_organizations_discover_create_legal_name_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateLegalNameErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_LEGAL_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_LEGAL_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
