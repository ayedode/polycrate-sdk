from typing import Literal

ApiV1AlertsCreateNamespaceErrorComponentAttr = Literal["namespace"]

API_V1_ALERTS_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsCreateNamespaceErrorComponentAttr] = {
    "namespace",
}


def check_api_v1_alerts_create_namespace_error_component_attr(
    value: str,
) -> ApiV1AlertsCreateNamespaceErrorComponentAttr:
    if value in API_V1_ALERTS_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
