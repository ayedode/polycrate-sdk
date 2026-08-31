from typing import Literal

ApiV1CredentialsReconcileCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_CREDENTIALS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsReconcileCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_credentials_reconcile_create_criticality_error_component_code(
    value: str,
) -> ApiV1CredentialsReconcileCreateCriticalityErrorComponentCode:
    if value in API_V1_CREDENTIALS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
