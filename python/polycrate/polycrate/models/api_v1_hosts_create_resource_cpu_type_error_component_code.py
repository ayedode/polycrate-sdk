from typing import Literal

ApiV1HostsCreateResourceCpuTypeErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_HOSTS_CREATE_RESOURCE_CPU_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsCreateResourceCpuTypeErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_hosts_create_resource_cpu_type_error_component_code(
    value: str,
) -> ApiV1HostsCreateResourceCpuTypeErrorComponentCode:
    if value in API_V1_HOSTS_CREATE_RESOURCE_CPU_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_CREATE_RESOURCE_CPU_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
