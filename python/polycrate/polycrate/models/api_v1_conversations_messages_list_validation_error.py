from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_conversations_messages_list_content_kind_error_component import (
        ApiV1ConversationsMessagesListContentKindErrorComponent,
    )
    from ..models.api_v1_conversations_messages_list_conversation_error_component import (
        ApiV1ConversationsMessagesListConversationErrorComponent,
    )
    from ..models.api_v1_conversations_messages_list_kind_error_component import (
        ApiV1ConversationsMessagesListKindErrorComponent,
    )
    from ..models.api_v1_conversations_messages_list_organization_error_component import (
        ApiV1ConversationsMessagesListOrganizationErrorComponent,
    )
    from ..models.api_v1_conversations_messages_list_search_error_component import (
        ApiV1ConversationsMessagesListSearchErrorComponent,
    )
    from ..models.api_v1_conversations_messages_list_sender_error_component import (
        ApiV1ConversationsMessagesListSenderErrorComponent,
    )
    from ..models.api_v1_conversations_messages_list_status_error_component import (
        ApiV1ConversationsMessagesListStatusErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ConversationsMessagesListValidationError")


@_attrs_define
class ApiV1ConversationsMessagesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ConversationsMessagesListContentKindErrorComponent |
            ApiV1ConversationsMessagesListConversationErrorComponent | ApiV1ConversationsMessagesListKindErrorComponent |
            ApiV1ConversationsMessagesListOrganizationErrorComponent | ApiV1ConversationsMessagesListSearchErrorComponent |
            ApiV1ConversationsMessagesListSenderErrorComponent | ApiV1ConversationsMessagesListStatusErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ConversationsMessagesListContentKindErrorComponent
        | ApiV1ConversationsMessagesListConversationErrorComponent
        | ApiV1ConversationsMessagesListKindErrorComponent
        | ApiV1ConversationsMessagesListOrganizationErrorComponent
        | ApiV1ConversationsMessagesListSearchErrorComponent
        | ApiV1ConversationsMessagesListSenderErrorComponent
        | ApiV1ConversationsMessagesListStatusErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_conversations_messages_list_content_kind_error_component import (
            ApiV1ConversationsMessagesListContentKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_list_conversation_error_component import (
            ApiV1ConversationsMessagesListConversationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_list_kind_error_component import (
            ApiV1ConversationsMessagesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_list_organization_error_component import (
            ApiV1ConversationsMessagesListOrganizationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_list_sender_error_component import (
            ApiV1ConversationsMessagesListSenderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_list_status_error_component import (
            ApiV1ConversationsMessagesListStatusErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ConversationsMessagesListOrganizationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesListStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesListConversationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesListContentKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesListSenderErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_conversations_messages_list_content_kind_error_component import (
            ApiV1ConversationsMessagesListContentKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_list_conversation_error_component import (
            ApiV1ConversationsMessagesListConversationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_list_kind_error_component import (
            ApiV1ConversationsMessagesListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_list_organization_error_component import (
            ApiV1ConversationsMessagesListOrganizationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_list_search_error_component import (
            ApiV1ConversationsMessagesListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_list_sender_error_component import (
            ApiV1ConversationsMessagesListSenderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_list_status_error_component import (
            ApiV1ConversationsMessagesListStatusErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ConversationsMessagesListContentKindErrorComponent
                | ApiV1ConversationsMessagesListConversationErrorComponent
                | ApiV1ConversationsMessagesListKindErrorComponent
                | ApiV1ConversationsMessagesListOrganizationErrorComponent
                | ApiV1ConversationsMessagesListSearchErrorComponent
                | ApiV1ConversationsMessagesListSenderErrorComponent
                | ApiV1ConversationsMessagesListStatusErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_list_error_type_0 = (
                        ApiV1ConversationsMessagesListOrganizationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_list_error_type_1 = (
                        ApiV1ConversationsMessagesListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_list_error_type_2 = (
                        ApiV1ConversationsMessagesListStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_list_error_type_3 = (
                        ApiV1ConversationsMessagesListConversationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_list_error_type_4 = (
                        ApiV1ConversationsMessagesListContentKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_list_error_type_5 = (
                        ApiV1ConversationsMessagesListSenderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_conversations_messages_list_error_type_6 = (
                    ApiV1ConversationsMessagesListSearchErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_conversations_messages_list_error_type_6

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_conversations_messages_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_conversations_messages_list_validation_error.additional_properties = d
        return api_v1_conversations_messages_list_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
