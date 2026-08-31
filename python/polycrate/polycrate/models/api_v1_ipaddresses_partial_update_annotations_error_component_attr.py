from typing import Literal

ApiV1IpaddressesPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_IPADDRESSES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_ipaddresses_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1IpaddressesPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_IPADDRESSES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
