from typing import Literal

ApiV1HostsCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_HOSTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsCreateAnnotationsErrorComponentAttr] = {
    "annotations",
}


def check_api_v1_hosts_create_annotations_error_component_attr(
    value: str,
) -> ApiV1HostsCreateAnnotationsErrorComponentAttr:
    if value in API_V1_HOSTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
