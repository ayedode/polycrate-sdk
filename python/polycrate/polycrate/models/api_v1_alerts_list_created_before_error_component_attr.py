from typing import Literal

ApiV1AlertsListCreatedBeforeErrorComponentAttr = Literal["created_before"]

API_V1_ALERTS_LIST_CREATED_BEFORE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsListCreatedBeforeErrorComponentAttr] = {
    "created_before",
}


def check_api_v1_alerts_list_created_before_error_component_attr(
    value: str,
) -> ApiV1AlertsListCreatedBeforeErrorComponentAttr:
    if value in API_V1_ALERTS_LIST_CREATED_BEFORE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_LIST_CREATED_BEFORE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
