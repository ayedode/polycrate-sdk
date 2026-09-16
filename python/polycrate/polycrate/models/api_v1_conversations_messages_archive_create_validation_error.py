from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_conversations_messages_archive_create_config_error_component import (
        ApiV1ConversationsMessagesArchiveCreateConfigErrorComponent,
    )
    from ..models.api_v1_conversations_messages_archive_create_content_error_component import (
        ApiV1ConversationsMessagesArchiveCreateContentErrorComponent,
    )
    from ..models.api_v1_conversations_messages_archive_create_content_kind_error_component import (
        ApiV1ConversationsMessagesArchiveCreateContentKindErrorComponent,
    )
    from ..models.api_v1_conversations_messages_archive_create_kind_error_component import (
        ApiV1ConversationsMessagesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_conversations_messages_archive_create_meta_error_component import (
        ApiV1ConversationsMessagesArchiveCreateMetaErrorComponent,
    )
    from ..models.api_v1_conversations_messages_archive_create_name_error_component import (
        ApiV1ConversationsMessagesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_conversations_messages_archive_create_non_field_errors_error_component import (
        ApiV1ConversationsMessagesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_conversations_messages_archive_create_provider_id_error_component import (
        ApiV1ConversationsMessagesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_conversations_messages_archive_create_status_error_component import (
        ApiV1ConversationsMessagesArchiveCreateStatusErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ConversationsMessagesArchiveCreateValidationError")


@_attrs_define
class ApiV1ConversationsMessagesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ConversationsMessagesArchiveCreateConfigErrorComponent |
            ApiV1ConversationsMessagesArchiveCreateContentErrorComponent |
            ApiV1ConversationsMessagesArchiveCreateContentKindErrorComponent |
            ApiV1ConversationsMessagesArchiveCreateKindErrorComponent |
            ApiV1ConversationsMessagesArchiveCreateMetaErrorComponent |
            ApiV1ConversationsMessagesArchiveCreateNameErrorComponent |
            ApiV1ConversationsMessagesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1ConversationsMessagesArchiveCreateProviderIdErrorComponent |
            ApiV1ConversationsMessagesArchiveCreateStatusErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ConversationsMessagesArchiveCreateConfigErrorComponent
        | ApiV1ConversationsMessagesArchiveCreateContentErrorComponent
        | ApiV1ConversationsMessagesArchiveCreateContentKindErrorComponent
        | ApiV1ConversationsMessagesArchiveCreateKindErrorComponent
        | ApiV1ConversationsMessagesArchiveCreateMetaErrorComponent
        | ApiV1ConversationsMessagesArchiveCreateNameErrorComponent
        | ApiV1ConversationsMessagesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1ConversationsMessagesArchiveCreateProviderIdErrorComponent
        | ApiV1ConversationsMessagesArchiveCreateStatusErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_conversations_messages_archive_create_content_error_component import (
            ApiV1ConversationsMessagesArchiveCreateContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_archive_create_content_kind_error_component import (
            ApiV1ConversationsMessagesArchiveCreateContentKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_archive_create_kind_error_component import (
            ApiV1ConversationsMessagesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_archive_create_meta_error_component import (
            ApiV1ConversationsMessagesArchiveCreateMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_archive_create_name_error_component import (
            ApiV1ConversationsMessagesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_archive_create_non_field_errors_error_component import (
            ApiV1ConversationsMessagesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_archive_create_provider_id_error_component import (
            ApiV1ConversationsMessagesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_archive_create_status_error_component import (
            ApiV1ConversationsMessagesArchiveCreateStatusErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ConversationsMessagesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesArchiveCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesArchiveCreateContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesArchiveCreateContentKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsMessagesArchiveCreateMetaErrorComponent):
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
        from ..models.api_v1_conversations_messages_archive_create_config_error_component import (
            ApiV1ConversationsMessagesArchiveCreateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_archive_create_content_error_component import (
            ApiV1ConversationsMessagesArchiveCreateContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_archive_create_content_kind_error_component import (
            ApiV1ConversationsMessagesArchiveCreateContentKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_archive_create_kind_error_component import (
            ApiV1ConversationsMessagesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_archive_create_meta_error_component import (
            ApiV1ConversationsMessagesArchiveCreateMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_archive_create_name_error_component import (
            ApiV1ConversationsMessagesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_archive_create_non_field_errors_error_component import (
            ApiV1ConversationsMessagesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_archive_create_provider_id_error_component import (
            ApiV1ConversationsMessagesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_messages_archive_create_status_error_component import (
            ApiV1ConversationsMessagesArchiveCreateStatusErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ConversationsMessagesArchiveCreateConfigErrorComponent
                | ApiV1ConversationsMessagesArchiveCreateContentErrorComponent
                | ApiV1ConversationsMessagesArchiveCreateContentKindErrorComponent
                | ApiV1ConversationsMessagesArchiveCreateKindErrorComponent
                | ApiV1ConversationsMessagesArchiveCreateMetaErrorComponent
                | ApiV1ConversationsMessagesArchiveCreateNameErrorComponent
                | ApiV1ConversationsMessagesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1ConversationsMessagesArchiveCreateProviderIdErrorComponent
                | ApiV1ConversationsMessagesArchiveCreateStatusErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_archive_create_error_type_0 = (
                        ApiV1ConversationsMessagesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_archive_create_error_type_1 = (
                        ApiV1ConversationsMessagesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_archive_create_error_type_2 = (
                        ApiV1ConversationsMessagesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_archive_create_error_type_3 = (
                        ApiV1ConversationsMessagesArchiveCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_archive_create_error_type_4 = (
                        ApiV1ConversationsMessagesArchiveCreateContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_archive_create_error_type_5 = (
                        ApiV1ConversationsMessagesArchiveCreateContentKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_archive_create_error_type_6 = (
                        ApiV1ConversationsMessagesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_messages_archive_create_error_type_7 = (
                        ApiV1ConversationsMessagesArchiveCreateMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_messages_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_conversations_messages_archive_create_error_type_8 = (
                    ApiV1ConversationsMessagesArchiveCreateConfigErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_conversations_messages_archive_create_error_type_8

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_conversations_messages_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_conversations_messages_archive_create_validation_error.additional_properties = d
        return api_v1_conversations_messages_archive_create_validation_error

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
