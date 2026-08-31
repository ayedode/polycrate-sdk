from typing import Literal

ApiV1OrganizationsArchiveCreateCachedK8SClusterCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_K8S_CLUSTER_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsArchiveCreateCachedK8SClusterCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_organizations_archive_create_cached_k8s_cluster_count_error_component_code(
    value: str,
) -> ApiV1OrganizationsArchiveCreateCachedK8SClusterCountErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_K8S_CLUSTER_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_K8S_CLUSTER_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
