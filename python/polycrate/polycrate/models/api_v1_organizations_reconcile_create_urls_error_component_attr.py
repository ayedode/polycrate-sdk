from typing import Literal

ApiV1OrganizationsReconcileCreateUrlsErrorComponentAttr = Literal["urls"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateUrlsErrorComponentAttr
] = {
    "urls",
}


def check_api_v1_organizations_reconcile_create_urls_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateUrlsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
