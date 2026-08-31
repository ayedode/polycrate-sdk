from typing import Literal

ApiV1ProvidersReconcileCreateCertificationsErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_RECONCILE_CREATE_CERTIFICATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersReconcileCreateCertificationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_providers_reconcile_create_certifications_error_component_code(
    value: str,
) -> ApiV1ProvidersReconcileCreateCertificationsErrorComponentCode:
    if value in API_V1_PROVIDERS_RECONCILE_CREATE_CERTIFICATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_RECONCILE_CREATE_CERTIFICATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
