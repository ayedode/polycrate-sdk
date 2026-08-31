from typing import Literal

ApiV1KubernetesWorkerPoolsUpdateSshKeyCredentialIdErrorComponentAttr = Literal["ssh_key_credential_id"]

API_V1_KUBERNETES_WORKER_POOLS_UPDATE_SSH_KEY_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsUpdateSshKeyCredentialIdErrorComponentAttr
] = {
    "ssh_key_credential_id",
}


def check_api_v1_kubernetes_worker_pools_update_ssh_key_credential_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsUpdateSshKeyCredentialIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_UPDATE_SSH_KEY_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_UPDATE_SSH_KEY_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
