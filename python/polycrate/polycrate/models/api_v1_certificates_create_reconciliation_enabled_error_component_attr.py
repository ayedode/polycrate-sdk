from typing import Literal

ApiV1CertificatesCreateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_CERTIFICATES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_certificates_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1CertificatesCreateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_CERTIFICATES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
