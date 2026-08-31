from typing import Literal

ApiV1SecretmanagerManagersArchiveCreateK8SClusterErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "null", "required"
]

API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersArchiveCreateK8SClusterErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_secretmanager_managers_archive_create_k8s_cluster_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersArchiveCreateK8SClusterErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
