from typing import Literal

ApiV1CredentialsArchiveCreateKubeconfigErrorComponentAttr = Literal["kubeconfig"]

API_V1_CREDENTIALS_ARCHIVE_CREATE_KUBECONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsArchiveCreateKubeconfigErrorComponentAttr
] = {
    "kubeconfig",
}


def check_api_v1_credentials_archive_create_kubeconfig_error_component_attr(
    value: str,
) -> ApiV1CredentialsArchiveCreateKubeconfigErrorComponentAttr:
    if value in API_V1_CREDENTIALS_ARCHIVE_CREATE_KUBECONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_ARCHIVE_CREATE_KUBECONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
