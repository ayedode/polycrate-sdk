from typing import Literal

ApiV1AlertsReconcileCreateSilenceEndsAtErrorComponentAttr = Literal["silence_ends_at"]

API_V1_ALERTS_RECONCILE_CREATE_SILENCE_ENDS_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsReconcileCreateSilenceEndsAtErrorComponentAttr
] = {
    "silence_ends_at",
}


def check_api_v1_alerts_reconcile_create_silence_ends_at_error_component_attr(
    value: str,
) -> ApiV1AlertsReconcileCreateSilenceEndsAtErrorComponentAttr:
    if value in API_V1_ALERTS_RECONCILE_CREATE_SILENCE_ENDS_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_SILENCE_ENDS_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
