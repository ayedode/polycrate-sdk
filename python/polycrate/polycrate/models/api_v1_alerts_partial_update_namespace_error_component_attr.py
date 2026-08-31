from typing import Literal

ApiV1AlertsPartialUpdateNamespaceErrorComponentAttr = Literal["namespace"]

API_V1_ALERTS_PARTIAL_UPDATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsPartialUpdateNamespaceErrorComponentAttr
] = {
    "namespace",
}


def check_api_v1_alerts_partial_update_namespace_error_component_attr(
    value: str,
) -> ApiV1AlertsPartialUpdateNamespaceErrorComponentAttr:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
