from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_conversations_messages_create_config_error_component import (
        ApiV1ConversationsMessagesCreateConfigErrorComponent,
    )
    from ..models.api_v1_conversations_messages_create_content_error_component import (
        ApiV1ConversationsMessagesCreateContentErrorComponent,
    )
    from ..models.api_v1_conversations_messages_create_content_kind_error_component import (
        ApiV1ConversationsMessagesCreateContentKindErrorComponent,
    )
    from ..models.api_v1_conversations_messages_create_conversation_error_component import (
        ApiV1ConversationsMessagesCreateConversationErrorComponent,
    )
    from ..models.api_v1_conversations_messages_create_kind_error_component import (
        ApiV1ConversationsMessagesCreateKindErrorComponent,
    )
    from ..models.api_v1_conversations_messages_create_meta_error_component import (
        ApiV1ConversationsMessagesCreateMetaErrorComponent,
    )
    from ..models.api_v1_conversations_messages_create_name_error_component import (
        ApiV1ConversationsMessagesCreateNameErrorComponent,
    )
    from ..models.api_v1_conversations_messages_create_non_field_errors_error_component import (
        ApiV1ConversationsMessagesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_conversations_messages_create_organization_error_component import (
        ApiV1ConversationsMessagesCreateOrganizationErrorComponent,
    )
    from ..models.api_v1_conversations_messages_create_provider_id_error_component import (
        ApiV1ConversationsMessagesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_conversations_messages_create_status_error_component import (
        ApiV1ConversationsMessagesCreateStatusErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ConversationsMessagesCreateValidationError")


@_attrs_define
class ApiV1ConversationsMessagesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ConversationsMessagesCreateConfigErrorComponent |
            ApiV1ConversationsMessagesCreateContentErrorComponent |
            ApiV1ConversationsMessagesCreateContentKindErrorComponent |
            ApiV1ConversationsMessagesCreateConversationErrorComponent | ApiV1ConversationsMessagesCreateKindErrorComponent
            | ApiV1ConversationsMessagesCreateMetaErrorComponent | ApiV1ConversationsMessagesCreateNameErrorComponent |
            ApiV1ConversationsMessagesCreateNonFieldErrorsErrorComponent |
            ApiV1ConversationsMessagesCreateOrganizationErrorComponent |
            ApiV1ConversationsMessagesCreateProviderIdErrorComponent |
            ApiV1ConversationsMessagesCreateStatusErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ConversationsMessagesCreateConfigErrorComponent
        | ApiV1ConversationsMessagesCreateContentErrorComponent
        | ApiV1ConversationsMessagesCreateContentKindErrorComponent
        | ApiV1ConversationsMessagesCreateConversationErrorComponent
        | ApiV1ConversationsMessagesCreateKindErrorComponent
        | ApiV1ConversationsMessagesCreateMetaErrorComponent
        | ApiV1ConversationsMessagesCreateNameErrorComponent
        | ApiV1ConversationsMessagesCreateNonFieldErrorsErrorComponent
        | ApiV1ConversationsMessagesCreateOrganizationErrorComponent
        | ApiV1ConversationsMessagesCreateProviderIdErrorComponent
        | ApiV1ConversationsMessagesCreateStatusErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_conversations_messages_create_content_error_component import (
            ApiV1ConversationsMessagesCreateContentErrorComponent,
        )
        from ..models.api_v1_conversations_messages_create_content_kind_error_component import (
            ApiV1ConversationsMessagesCreateContentKindErrorComponent,
        )
        from ..models.api_v1_conversations_messages_create_conversation_error_component import (
            ApiV1ConversationsMessagesCreateConversationErrorComponent,
        )
        from ..models.api_v1_conversations_messages_create_kind_error_component import (
            ApiV1ConversationsMessagesCreateKindErrorComponent,
        )
        from ..models.api_v1_conversations_messages_create_meta_error_component import (
            ApiV1ConversationsMessagesCreateMetaErrorComponent,
        )
        from ..models.api_v1_conversations_messages_create_name_error_component import (
            ApiV1ConversationsMessagesCreateNameErrorComponent,
        )
        from ..models.api_v1_conversations_messages_create_non_field_errors_error_component import (
            ApiV1ConversationsMessagesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_conversations_messages_create_organization_error_component import (
            ApiV1ConversationsMessagesCreateOrganizationErrorComponent,
        )
        from ..models.api_v1_conversations_messages_create_provider_id_error_component import (
            ApiV1ConversationsMessagesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_conversations_messages_create_status_error_component import (
            ApiV1ConversationsMessagesCreateStatusErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ConversationsMessagesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesCreateContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesCreateContentKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesCreateOrganizationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesCreateConversationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesCreateMetaErrorComponent):
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
        from ..models.api_v1_conversations_messages_create_config_error_component import (
            ApiV1ConversationsMessagesCreateConfigErrorComponent,
        )
        from ..models.api_v1_conversations_messages_create_content_error_component import (
            ApiV1ConversationsMessagesCreateContentErrorComponent,
        )
        from ..models.api_v1_conversations_messages_create_content_kind_error_component import (
            ApiV1ConversationsMessagesCreateContentKindErrorComponent,
        )
        from ..models.api_v1_conversations_messages_create_conversation_error_component import (
            ApiV1ConversationsMessagesCreateConversationErrorComponent,
        )
        from ..models.api_v1_conversations_messages_create_kind_error_component import (
            ApiV1ConversationsMessagesCreateKindErrorComponent,
        )
        from ..models.api_v1_conversations_messages_create_meta_error_component import (
            ApiV1ConversationsMessagesCreateMetaErrorComponent,
        )
        from ..models.api_v1_conversations_messages_create_name_error_component import (
            ApiV1ConversationsMessagesCreateNameErrorComponent,
        )
        from ..models.api_v1_conversations_messages_create_non_field_errors_error_component import (
            ApiV1ConversationsMessagesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_conversations_messages_create_organization_error_component import (
            ApiV1ConversationsMessagesCreateOrganizationErrorComponent,
        )
        from ..models.api_v1_conversations_messages_create_provider_id_error_component import (
            ApiV1ConversationsMessagesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_conversations_messages_create_status_error_component import (
            ApiV1ConversationsMessagesCreateStatusErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ConversationsMessagesCreateConfigErrorComponent
                | ApiV1ConversationsMessagesCreateContentErrorComponent
                | ApiV1ConversationsMessagesCreateContentKindErrorComponent
                | ApiV1ConversationsMessagesCreateConversationErrorComponent
                | ApiV1ConversationsMessagesCreateKindErrorComponent
                | ApiV1ConversationsMessagesCreateMetaErrorComponent
                | ApiV1ConversationsMessagesCreateNameErrorComponent
                | ApiV1ConversationsMessagesCreateNonFieldErrorsErrorComponent
                | ApiV1ConversationsMessagesCreateOrganizationErrorComponent
                | ApiV1ConversationsMessagesCreateProviderIdErrorComponent
                | ApiV1ConversationsMessagesCreateStatusErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_create_error_type_0 = (
                        ApiV1ConversationsMessagesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_create_error_type_1 = (
                        ApiV1ConversationsMessagesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_create_error_type_2 = (
                        ApiV1ConversationsMessagesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_create_error_type_3 = (
                        ApiV1ConversationsMessagesCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_create_error_type_4 = (
                        ApiV1ConversationsMessagesCreateContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_create_error_type_5 = (
                        ApiV1ConversationsMessagesCreateContentKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_create_error_type_6 = (
                        ApiV1ConversationsMessagesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_create_error_type_7 = (
                        ApiV1ConversationsMessagesCreateOrganizationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_create_error_type_8 = (
                        ApiV1ConversationsMessagesCreateConversationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_create_error_type_9 = (
                        ApiV1ConversationsMessagesCreateMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_conversations_messages_create_error_type_10 = (
                    ApiV1ConversationsMessagesCreateConfigErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_conversations_messages_create_error_type_10

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_conversations_messages_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_conversations_messages_create_validation_error.additional_properties = d
        return api_v1_conversations_messages_create_validation_error

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
