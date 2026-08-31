from typing import Literal

ApiV1HostsUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_HOSTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsUpdateAnnotationsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_hosts_update_annotations_error_component_code(
    value: str,
) -> ApiV1HostsUpdateAnnotationsErrorComponentCode:
    if value in API_V1_HOSTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
