from typing import Literal

ApiV1OrganizationsReconcileCreateUrlsErrorComponentCode = Literal["invalid"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsReconcileCreateUrlsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_organizations_reconcile_create_urls_error_component_code(
    value: str,
) -> ApiV1OrganizationsReconcileCreateUrlsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
