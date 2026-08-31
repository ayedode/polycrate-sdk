from typing import Literal

ApiV1CertificatesUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_CERTIFICATES_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_certificates_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1CertificatesUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1_CERTIFICATES_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
