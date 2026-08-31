from typing import Literal

ApiV1OrganizationsCreateNameErrorComponentAttr = Literal["name"]

API_V1_ORGANIZATIONS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1OrganizationsCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_organizations_create_name_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateNameErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
