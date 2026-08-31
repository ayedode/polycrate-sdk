from typing import Literal

ApiV1OrganizationsCreateColorErrorComponentAttr = Literal["color"]

API_V1_ORGANIZATIONS_CREATE_COLOR_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1OrganizationsCreateColorErrorComponentAttr] = {
    "color",
}


def check_api_v1_organizations_create_color_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateColorErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_COLOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_COLOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
