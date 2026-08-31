from typing import Literal

ApiV1AlertsReconcileCreateSilenceUrlErrorComponentAttr = Literal["silence_url"]

API_V1_ALERTS_RECONCILE_CREATE_SILENCE_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsReconcileCreateSilenceUrlErrorComponentAttr
] = {
    "silence_url",
}


def check_api_v1_alerts_reconcile_create_silence_url_error_component_attr(
    value: str,
) -> ApiV1AlertsReconcileCreateSilenceUrlErrorComponentAttr:
    if value in API_V1_ALERTS_RECONCILE_CREATE_SILENCE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_SILENCE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
