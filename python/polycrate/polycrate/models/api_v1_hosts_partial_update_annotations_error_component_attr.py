from typing import Literal

ApiV1HostsPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_HOSTS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_hosts_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1HostsPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
