from typing import Literal

ApiV1CredentialsReconcileCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_CREDENTIALS_RECONCILE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsReconcileCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_credentials_reconcile_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1CredentialsReconcileCreateTolerationsErrorComponentAttr:
    if value in API_V1_CREDENTIALS_RECONCILE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_RECONCILE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
