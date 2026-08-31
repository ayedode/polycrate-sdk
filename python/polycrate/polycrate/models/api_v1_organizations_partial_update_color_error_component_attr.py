from typing import Literal

ApiV1OrganizationsPartialUpdateColorErrorComponentAttr = Literal["color"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_COLOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateColorErrorComponentAttr
] = {
    "color",
}


def check_api_v1_organizations_partial_update_color_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateColorErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_COLOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_COLOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
