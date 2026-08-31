from typing import Literal

ApiV1ProvidersReconcileCreateUrlsErrorComponentAttr = Literal["urls"]

API_V1_PROVIDERS_RECONCILE_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersReconcileCreateUrlsErrorComponentAttr
] = {
    "urls",
}


def check_api_v1_providers_reconcile_create_urls_error_component_attr(
    value: str,
) -> ApiV1ProvidersReconcileCreateUrlsErrorComponentAttr:
    if value in API_V1_PROVIDERS_RECONCILE_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_RECONCILE_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
