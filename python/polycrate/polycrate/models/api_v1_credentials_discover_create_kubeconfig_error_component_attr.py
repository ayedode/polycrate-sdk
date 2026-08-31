from typing import Literal

ApiV1CredentialsDiscoverCreateKubeconfigErrorComponentAttr = Literal["kubeconfig"]

API_V1_CREDENTIALS_DISCOVER_CREATE_KUBECONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsDiscoverCreateKubeconfigErrorComponentAttr
] = {
    "kubeconfig",
}


def check_api_v1_credentials_discover_create_kubeconfig_error_component_attr(
    value: str,
) -> ApiV1CredentialsDiscoverCreateKubeconfigErrorComponentAttr:
    if value in API_V1_CREDENTIALS_DISCOVER_CREATE_KUBECONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_DISCOVER_CREATE_KUBECONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
