from typing import Literal

ApiV1OrganizationsUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_ORGANIZATIONS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_organizations_update_display_name_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
