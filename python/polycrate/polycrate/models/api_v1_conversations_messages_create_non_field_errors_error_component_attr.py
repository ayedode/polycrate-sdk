from typing import Literal

ApiV1ConversationsMessagesCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_CONVERSATIONS_MESSAGES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_conversations_messages_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
