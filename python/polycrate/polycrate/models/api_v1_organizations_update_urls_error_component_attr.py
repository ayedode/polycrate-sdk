from typing import Literal

ApiV1OrganizationsUpdateUrlsErrorComponentAttr = Literal["urls"]

API_V1_ORGANIZATIONS_UPDATE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1OrganizationsUpdateUrlsErrorComponentAttr] = {
    "urls",
}


def check_api_v1_organizations_update_urls_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateUrlsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
