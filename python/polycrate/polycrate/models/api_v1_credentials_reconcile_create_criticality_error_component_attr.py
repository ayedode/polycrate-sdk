from typing import Literal

ApiV1CredentialsReconcileCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_CREDENTIALS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsReconcileCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_credentials_reconcile_create_criticality_error_component_attr(
    value: str,
) -> ApiV1CredentialsReconcileCreateCriticalityErrorComponentAttr:
    if value in API_V1_CREDENTIALS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
