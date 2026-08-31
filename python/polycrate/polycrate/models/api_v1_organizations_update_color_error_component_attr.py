from typing import Literal

ApiV1OrganizationsUpdateColorErrorComponentAttr = Literal["color"]

API_V1_ORGANIZATIONS_UPDATE_COLOR_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1OrganizationsUpdateColorErrorComponentAttr] = {
    "color",
}


def check_api_v1_organizations_update_color_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateColorErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_COLOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_COLOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
