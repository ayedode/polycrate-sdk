from typing import Literal

ApiV1CredentialsReconcileCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_CREDENTIALS_RECONCILE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsReconcileCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_credentials_reconcile_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1CredentialsReconcileCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_CREDENTIALS_RECONCILE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_RECONCILE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
