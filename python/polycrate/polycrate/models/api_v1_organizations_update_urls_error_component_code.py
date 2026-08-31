from typing import Literal

ApiV1OrganizationsUpdateUrlsErrorComponentCode = Literal["invalid"]

API_V1_ORGANIZATIONS_UPDATE_URLS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1OrganizationsUpdateUrlsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_organizations_update_urls_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdateUrlsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_URLS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_URLS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
