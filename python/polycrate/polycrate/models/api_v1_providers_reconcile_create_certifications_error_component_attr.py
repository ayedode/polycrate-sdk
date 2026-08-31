from typing import Literal

ApiV1ProvidersReconcileCreateCertificationsErrorComponentAttr = Literal["certifications"]

API_V1_PROVIDERS_RECONCILE_CREATE_CERTIFICATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersReconcileCreateCertificationsErrorComponentAttr
] = {
    "certifications",
}


def check_api_v1_providers_reconcile_create_certifications_error_component_attr(
    value: str,
) -> ApiV1ProvidersReconcileCreateCertificationsErrorComponentAttr:
    if value in API_V1_PROVIDERS_RECONCILE_CREATE_CERTIFICATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_RECONCILE_CREATE_CERTIFICATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
