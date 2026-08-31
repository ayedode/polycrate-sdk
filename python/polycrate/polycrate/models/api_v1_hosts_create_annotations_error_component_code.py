from typing import Literal

ApiV1HostsCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_HOSTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsCreateAnnotationsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_hosts_create_annotations_error_component_code(
    value: str,
) -> ApiV1HostsCreateAnnotationsErrorComponentCode:
    if value in API_V1_HOSTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
