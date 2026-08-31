from typing import Literal

ApiV1AlertsReconcileCreateSilenceEndsAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_ALERTS_RECONCILE_CREATE_SILENCE_ENDS_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsReconcileCreateSilenceEndsAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_alerts_reconcile_create_silence_ends_at_error_component_code(
    value: str,
) -> ApiV1AlertsReconcileCreateSilenceEndsAtErrorComponentCode:
    if value in API_V1_ALERTS_RECONCILE_CREATE_SILENCE_ENDS_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_SILENCE_ENDS_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
