from typing import Literal

ApiV1ProvidersReconcileCreateUrlsErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_RECONCILE_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersReconcileCreateUrlsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_providers_reconcile_create_urls_error_component_code(
    value: str,
) -> ApiV1ProvidersReconcileCreateUrlsErrorComponentCode:
    if value in API_V1_PROVIDERS_RECONCILE_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_RECONCILE_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
