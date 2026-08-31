from typing import Literal

ApiV1OrganizationsPartialUpdateUrlsErrorComponentCode = Literal["invalid"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_URLS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsPartialUpdateUrlsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_organizations_partial_update_urls_error_component_code(
    value: str,
) -> ApiV1OrganizationsPartialUpdateUrlsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_URLS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_URLS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
