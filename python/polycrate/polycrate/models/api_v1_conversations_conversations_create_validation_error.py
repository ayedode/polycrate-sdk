from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_conversations_conversations_create_config_error_component import (
        ApiV1ConversationsConversationsCreateConfigErrorComponent,
    )
    from ..models.api_v1_conversations_conversations_create_conversation_provider_error_component import (
        ApiV1ConversationsConversationsCreateConversationProviderErrorComponent,
    )
    from ..models.api_v1_conversations_conversations_create_kind_error_component import (
        ApiV1ConversationsConversationsCreateKindErrorComponent,
    )
    from ..models.api_v1_conversations_conversations_create_meta_error_component import (
        ApiV1ConversationsConversationsCreateMetaErrorComponent,
    )
    from ..models.api_v1_conversations_conversations_create_name_error_component import (
        ApiV1ConversationsConversationsCreateNameErrorComponent,
    )
    from ..models.api_v1_conversations_conversations_create_non_field_errors_error_component import (
        ApiV1ConversationsConversationsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_conversations_conversations_create_organization_error_component import (
        ApiV1ConversationsConversationsCreateOrganizationErrorComponent,
    )
    from ..models.api_v1_conversations_conversations_create_platform_service_error_component import (
        ApiV1ConversationsConversationsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_conversations_conversations_create_provider_id_error_component import (
        ApiV1ConversationsConversationsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_conversations_conversations_create_status_error_component import (
        ApiV1ConversationsConversationsCreateStatusErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ConversationsConversationsCreateValidationError")


@_attrs_define
class ApiV1ConversationsConversationsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ConversationsConversationsCreateConfigErrorComponent |
            ApiV1ConversationsConversationsCreateConversationProviderErrorComponent |
            ApiV1ConversationsConversationsCreateKindErrorComponent |
            ApiV1ConversationsConversationsCreateMetaErrorComponent |
            ApiV1ConversationsConversationsCreateNameErrorComponent |
            ApiV1ConversationsConversationsCreateNonFieldErrorsErrorComponent |
            ApiV1ConversationsConversationsCreateOrganizationErrorComponent |
            ApiV1ConversationsConversationsCreatePlatformServiceErrorComponent |
            ApiV1ConversationsConversationsCreateProviderIdErrorComponent |
            ApiV1ConversationsConversationsCreateStatusErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ConversationsConversationsCreateConfigErrorComponent
        | ApiV1ConversationsConversationsCreateConversationProviderErrorComponent
        | ApiV1ConversationsConversationsCreateKindErrorComponent
        | ApiV1ConversationsConversationsCreateMetaErrorComponent
        | ApiV1ConversationsConversationsCreateNameErrorComponent
        | ApiV1ConversationsConversationsCreateNonFieldErrorsErrorComponent
        | ApiV1ConversationsConversationsCreateOrganizationErrorComponent
        | ApiV1ConversationsConversationsCreatePlatformServiceErrorComponent
        | ApiV1ConversationsConversationsCreateProviderIdErrorComponent
        | ApiV1ConversationsConversationsCreateStatusErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_conversations_conversations_create_conversation_provider_error_component import (
            ApiV1ConversationsConversationsCreateConversationProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_conversations_create_kind_error_component import (
            ApiV1ConversationsConversationsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_conversations_create_meta_error_component import (
            ApiV1ConversationsConversationsCreateMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_conversations_create_name_error_component import (
            ApiV1ConversationsConversationsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_conversations_create_non_field_errors_error_component import (
            ApiV1ConversationsConversationsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_conversations_create_organization_error_component import (
            ApiV1ConversationsConversationsCreateOrganizationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_conversations_create_platform_service_error_component import (
            ApiV1ConversationsConversationsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_conversations_create_provider_id_error_component import (
            ApiV1ConversationsConversationsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_conversations_create_status_error_component import (
            ApiV1ConversationsConversationsCreateStatusErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ConversationsConversationsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsConversationsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsConversationsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsConversationsCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsConversationsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsConversationsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsConversationsCreateOrganizationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsConversationsCreateConversationProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConversationsConversationsCreateMetaErrorComponent):
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
        from ..models.api_v1_conversations_conversations_create_config_error_component import (
            ApiV1ConversationsConversationsCreateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_conversations_create_conversation_provider_error_component import (
            ApiV1ConversationsConversationsCreateConversationProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_conversations_create_kind_error_component import (
            ApiV1ConversationsConversationsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_conversations_create_meta_error_component import (
            ApiV1ConversationsConversationsCreateMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_conversations_create_name_error_component import (
            ApiV1ConversationsConversationsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_conversations_create_non_field_errors_error_component import (
            ApiV1ConversationsConversationsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_conversations_create_organization_error_component import (
            ApiV1ConversationsConversationsCreateOrganizationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_conversations_create_platform_service_error_component import (
            ApiV1ConversationsConversationsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_conversations_create_provider_id_error_component import (
            ApiV1ConversationsConversationsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_conversations_conversations_create_status_error_component import (
            ApiV1ConversationsConversationsCreateStatusErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ConversationsConversationsCreateConfigErrorComponent
                | ApiV1ConversationsConversationsCreateConversationProviderErrorComponent
                | ApiV1ConversationsConversationsCreateKindErrorComponent
                | ApiV1ConversationsConversationsCreateMetaErrorComponent
                | ApiV1ConversationsConversationsCreateNameErrorComponent
                | ApiV1ConversationsConversationsCreateNonFieldErrorsErrorComponent
                | ApiV1ConversationsConversationsCreateOrganizationErrorComponent
                | ApiV1ConversationsConversationsCreatePlatformServiceErrorComponent
                | ApiV1ConversationsConversationsCreateProviderIdErrorComponent
                | ApiV1ConversationsConversationsCreateStatusErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_conversations_create_error_type_0 = (
                        ApiV1ConversationsConversationsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_conversations_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_conversations_create_error_type_1 = (
                        ApiV1ConversationsConversationsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_conversations_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_conversations_create_error_type_2 = (
                        ApiV1ConversationsConversationsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_conversations_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_conversations_create_error_type_3 = (
                        ApiV1ConversationsConversationsCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_conversations_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_conversations_create_error_type_4 = (
                        ApiV1ConversationsConversationsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_conversations_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_conversations_create_error_type_5 = (
                        ApiV1ConversationsConversationsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_conversations_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_conversations_create_error_type_6 = (
                        ApiV1ConversationsConversationsCreateOrganizationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_conversations_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_conversations_create_error_type_7 = (
                        ApiV1ConversationsConversationsCreateConversationProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_conversations_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conversations_conversations_create_error_type_8 = (
                        ApiV1ConversationsConversationsCreateMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conversations_conversations_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_conversations_conversations_create_error_type_9 = (
                    ApiV1ConversationsConversationsCreateConfigErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_conversations_conversations_create_error_type_9

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_conversations_conversations_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_conversations_conversations_create_validation_error.additional_properties = d
        return api_v1_conversations_conversations_create_validation_error

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
