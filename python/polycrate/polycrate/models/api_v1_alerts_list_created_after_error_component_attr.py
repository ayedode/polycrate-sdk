from typing import Literal

ApiV1AlertsListCreatedAfterErrorComponentAttr = Literal["created_after"]

API_V1_ALERTS_LIST_CREATED_AFTER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsListCreatedAfterErrorComponentAttr] = {
    "created_after",
}


def check_api_v1_alerts_list_created_after_error_component_attr(
    value: str,
) -> ApiV1AlertsListCreatedAfterErrorComponentAttr:
    if value in API_V1_ALERTS_LIST_CREATED_AFTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_LIST_CREATED_AFTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
