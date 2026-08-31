from typing import Literal

ApiV1CredentialsReconcileCreateNameErrorComponentAttr = Literal["name"]

API_V1_CREDENTIALS_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsReconcileCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_credentials_reconcile_create_name_error_component_attr(
    value: str,
) -> ApiV1CredentialsReconcileCreateNameErrorComponentAttr:
    if value in API_V1_CREDENTIALS_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
