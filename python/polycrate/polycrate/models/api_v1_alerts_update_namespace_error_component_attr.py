from typing import Literal

ApiV1AlertsUpdateNamespaceErrorComponentAttr = Literal["namespace"]

API_V1_ALERTS_UPDATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsUpdateNamespaceErrorComponentAttr] = {
    "namespace",
}


def check_api_v1_alerts_update_namespace_error_component_attr(
    value: str,
) -> ApiV1AlertsUpdateNamespaceErrorComponentAttr:
    if value in API_V1_ALERTS_UPDATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
