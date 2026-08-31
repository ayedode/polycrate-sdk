from typing import Literal

ApiV1OrganizationsCreateUrlsErrorComponentCode = Literal["invalid"]

API_V1_ORGANIZATIONS_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1OrganizationsCreateUrlsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_organizations_create_urls_error_component_code(
    value: str,
) -> ApiV1OrganizationsCreateUrlsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
