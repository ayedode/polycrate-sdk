from typing import Literal

ApiV1AlertsDiscoverCreateNamespaceErrorComponentAttr = Literal["namespace"]

API_V1_ALERTS_DISCOVER_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsDiscoverCreateNamespaceErrorComponentAttr
] = {
    "namespace",
}


def check_api_v1_alerts_discover_create_namespace_error_component_attr(
    value: str,
) -> ApiV1AlertsDiscoverCreateNamespaceErrorComponentAttr:
    if value in API_V1_ALERTS_DISCOVER_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
