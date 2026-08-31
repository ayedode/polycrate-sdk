from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_conversations_conversations_list_conversation_provider_error_component import (
        ApiV1ConversationsConversationsListConversationProviderErrorComponent,
    )
    from ..models.api_v1_conversations_conversations_list_kind_error_component import (
        ApiV1ConversationsConversationsListKindErrorComponent,
    )
    from ..models.api_v1_conversations_conversations_list_organization_error_component import (
        ApiV1ConversationsConversationsListOrganizationErrorComponent,
    )
    from ..models.api_v1_conversations_conversations_list_provider_id_contains_error_component import (
        ApiV1ConversationsConversationsListProviderIdContainsErrorComponent,
    )
    from ..models.api_v1_conversations_conversations_list_provider_id_error_component import (
        ApiV1ConversationsConversationsListProviderIdErrorComponent,
    )
    from ..models.api_v1_conversations_conversations_list_search_error_component import (
        ApiV1ConversationsConversationsListSearchErrorComponent,
    )
    from ..models.api_v1_conversations_conversations_list_status_error_component import (
        ApiV1ConversationsConversationsListStatusErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ConversationsConversationsListValidationError")


@_attrs_define
class ApiV1ConversationsConversationsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ConversationsConversationsListConversationProviderErrorComponent |
            ApiV1ConversationsConversationsListKindErrorComponent |
            ApiV1ConversationsConversationsListOrganizationErrorComponent |
            ApiV1ConversationsConversationsListProviderIdContainsErrorComponent |
            ApiV1ConversationsConversationsListProviderIdErrorComponent |
            ApiV1ConversationsConversationsListSearchErrorComponent |
            ApiV1ConversationsConversationsListStatusErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ConversationsConversationsListConversationProviderErrorComponent
        | ApiV1ConversationsConversationsListKindErrorComponent
        | ApiV1ConversationsConversationsListOrganizationErrorComponent
        | ApiV1ConversationsConversationsListProviderIdContainsErrorComponent
        | ApiV1ConversationsConversationsListProviderIdErrorComponent
        | ApiV1ConversationsConversationsListSearchErrorComponent
        | ApiV1ConversationsConversationsListStatusErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_conversations_conversations_list_conversation_provider_error_component import (
            ApiV1ConversationsConversationsListConversationProviderErrorComponent,
        )
        from ..models.api_v1_conversations_conversations_list_kind_error_component import (
            ApiV1ConversationsConversationsListKindErrorComponent,
        )
        from ..models.api_v1_conversations_conversations_list_organization_error_component import (
            ApiV1ConversationsConversationsListOrganizationErrorComponent,
        )
        from ..models.api_v1_conversations_conversations_list_provider_id_contains_error_component import (
            ApiV1ConversationsConversationsListProviderIdContainsErrorComponent,
        )
        from ..models.api_v1_conversations_conversations_list_provider_id_error_component import (
            ApiV1ConversationsConversationsListProviderIdErrorComponent,
        )
        from ..models.api_v1_conversations_conversations_list_status_error_component import (
            ApiV1ConversationsConversationsListStatusErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ConversationsConversationsListOrganizationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsConversationsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsConversationsListStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsConversationsListProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsConversationsListProviderIdContainsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsConversationsListConversationProviderErrorComponent):
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
        from ..models.api_v1_conversations_conversations_list_conversation_provider_error_component import (
            ApiV1ConversationsConversationsListConversationProviderErrorComponent,
        )
        from ..models.api_v1_conversations_conversations_list_kind_error_component import (
            ApiV1ConversationsConversationsListKindErrorComponent,
        )
        from ..models.api_v1_conversations_conversations_list_organization_error_component import (
            ApiV1ConversationsConversationsListOrganizationErrorComponent,
        )
        from ..models.api_v1_conversations_conversations_list_provider_id_contains_error_component import (
            ApiV1ConversationsConversationsListProviderIdContainsErrorComponent,
        )
        from ..models.api_v1_conversations_conversations_list_provider_id_error_component import (
            ApiV1ConversationsConversationsListProviderIdErrorComponent,
        )
        from ..models.api_v1_conversations_conversations_list_search_error_component import (
            ApiV1ConversationsConversationsListSearchErrorComponent,
        )
        from ..models.api_v1_conversations_conversations_list_status_error_component import (
            ApiV1ConversationsConversationsListStatusErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ConversationsConversationsListConversationProviderErrorComponent
                | ApiV1ConversationsConversationsListKindErrorComponent
                | ApiV1ConversationsConversationsListOrganizationErrorComponent
                | ApiV1ConversationsConversationsListProviderIdContainsErrorComponent
                | ApiV1ConversationsConversationsListProviderIdErrorComponent
                | ApiV1ConversationsConversationsListSearchErrorComponent
                | ApiV1ConversationsConversationsListStatusErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_conversations_list_error_type_0 = (
                        ApiV1ConversationsConversationsListOrganizationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_conversations_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_conversations_list_error_type_1 = (
                        ApiV1ConversationsConversationsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_conversations_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_conversations_list_error_type_2 = (
                        ApiV1ConversationsConversationsListStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_conversations_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_conversations_list_error_type_3 = (
                        ApiV1ConversationsConversationsListProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_conversations_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_conversations_list_error_type_4 = (
                        ApiV1ConversationsConversationsListProviderIdContainsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_conversations_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_conversations_list_error_type_5 = (
                        ApiV1ConversationsConversationsListConversationProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_conversations_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_conversations_conversations_list_error_type_6 = (
                    ApiV1ConversationsConversationsListSearchErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_conversations_conversations_list_error_type_6

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_conversations_conversations_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_conversations_conversations_list_validation_error.additional_properties = d
        return api_v1_conversations_conversations_list_validation_error

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
