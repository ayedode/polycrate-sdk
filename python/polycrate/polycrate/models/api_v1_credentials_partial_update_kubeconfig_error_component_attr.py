from typing import Literal

ApiV1CredentialsPartialUpdateKubeconfigErrorComponentAttr = Literal["kubeconfig"]

API_V1_CREDENTIALS_PARTIAL_UPDATE_KUBECONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsPartialUpdateKubeconfigErrorComponentAttr
] = {
    "kubeconfig",
}


def check_api_v1_credentials_partial_update_kubeconfig_error_component_attr(
    value: str,
) -> ApiV1CredentialsPartialUpdateKubeconfigErrorComponentAttr:
    if value in API_V1_CREDENTIALS_PARTIAL_UPDATE_KUBECONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_PARTIAL_UPDATE_KUBECONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
