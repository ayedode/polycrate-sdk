from typing import Literal

ApiV1AlertsUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_ALERTS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsUpdateArchivedErrorComponentAttr] = {
    "archived",
}


def check_api_v1_alerts_update_archived_error_component_attr(value: str) -> ApiV1AlertsUpdateArchivedErrorComponentAttr:
    if value in API_V1_ALERTS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
