from typing import Literal

ApiV1CredentialsCreateKubeconfigErrorComponentAttr = Literal["kubeconfig"]

API_V1_CREDENTIALS_CREATE_KUBECONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsCreateKubeconfigErrorComponentAttr
] = {
    "kubeconfig",
}


def check_api_v1_credentials_create_kubeconfig_error_component_attr(
    value: str,
) -> ApiV1CredentialsCreateKubeconfigErrorComponentAttr:
    if value in API_V1_CREDENTIALS_CREATE_KUBECONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_CREATE_KUBECONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
