from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_assistant_sessions_messages_create_annotations_error_component import (
        ApiV1AssistantSessionsMessagesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_archived_at_error_component import (
        ApiV1AssistantSessionsMessagesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_archived_error_component import (
        ApiV1AssistantSessionsMessagesCreateArchivedErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_archived_reason_error_component import (
        ApiV1AssistantSessionsMessagesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_criticality_error_component import (
        ApiV1AssistantSessionsMessagesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_debug_mode_error_component import (
        ApiV1AssistantSessionsMessagesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_display_name_error_component import (
        ApiV1AssistantSessionsMessagesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_kind_error_component import (
        ApiV1AssistantSessionsMessagesCreateKindErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_labels_error_component import (
        ApiV1AssistantSessionsMessagesCreateLabelsErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_name_error_component import (
        ApiV1AssistantSessionsMessagesCreateNameErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_non_field_errors_error_component import (
        ApiV1AssistantSessionsMessagesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_platform_service_error_component import (
        ApiV1AssistantSessionsMessagesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_provider_error_component import (
        ApiV1AssistantSessionsMessagesCreateProviderErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_provider_id_error_component import (
        ApiV1AssistantSessionsMessagesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_provider_reference_error_component import (
        ApiV1AssistantSessionsMessagesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_reconciliation_enabled_error_component import (
        ApiV1AssistantSessionsMessagesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_sla_availability_error_component import (
        ApiV1AssistantSessionsMessagesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_sla_target_error_component import (
        ApiV1AssistantSessionsMessagesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_slo_availability_error_component import (
        ApiV1AssistantSessionsMessagesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_slo_target_error_component import (
        ApiV1AssistantSessionsMessagesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_status_error_component import (
        ApiV1AssistantSessionsMessagesCreateStatusErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_target_availability_error_component import (
        ApiV1AssistantSessionsMessagesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_tolerations_error_component import (
        ApiV1AssistantSessionsMessagesCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_assistant_sessions_messages_create_workspace_id_error_component import (
        ApiV1AssistantSessionsMessagesCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1AssistantSessionsMessagesCreateValidationError")


@_attrs_define
class ApiV1AssistantSessionsMessagesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AssistantSessionsMessagesCreateAnnotationsErrorComponent |
            ApiV1AssistantSessionsMessagesCreateArchivedAtErrorComponent |
            ApiV1AssistantSessionsMessagesCreateArchivedErrorComponent |
            ApiV1AssistantSessionsMessagesCreateArchivedReasonErrorComponent |
            ApiV1AssistantSessionsMessagesCreateCriticalityErrorComponent |
            ApiV1AssistantSessionsMessagesCreateDebugModeErrorComponent |
            ApiV1AssistantSessionsMessagesCreateDisplayNameErrorComponent |
            ApiV1AssistantSessionsMessagesCreateKindErrorComponent |
            ApiV1AssistantSessionsMessagesCreateLabelsErrorComponent |
            ApiV1AssistantSessionsMessagesCreateNameErrorComponent |
            ApiV1AssistantSessionsMessagesCreateNonFieldErrorsErrorComponent |
            ApiV1AssistantSessionsMessagesCreatePlatformServiceErrorComponent |
            ApiV1AssistantSessionsMessagesCreateProviderErrorComponent |
            ApiV1AssistantSessionsMessagesCreateProviderIdErrorComponent |
            ApiV1AssistantSessionsMessagesCreateProviderReferenceErrorComponent |
            ApiV1AssistantSessionsMessagesCreateReconciliationEnabledErrorComponent |
            ApiV1AssistantSessionsMessagesCreateSlaAvailabilityErrorComponent |
            ApiV1AssistantSessionsMessagesCreateSlaTargetErrorComponent |
            ApiV1AssistantSessionsMessagesCreateSloAvailabilityErrorComponent |
            ApiV1AssistantSessionsMessagesCreateSloTargetErrorComponent |
            ApiV1AssistantSessionsMessagesCreateStatusErrorComponent |
            ApiV1AssistantSessionsMessagesCreateTargetAvailabilityErrorComponent |
            ApiV1AssistantSessionsMessagesCreateTolerationsErrorComponent |
            ApiV1AssistantSessionsMessagesCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AssistantSessionsMessagesCreateAnnotationsErrorComponent
        | ApiV1AssistantSessionsMessagesCreateArchivedAtErrorComponent
        | ApiV1AssistantSessionsMessagesCreateArchivedErrorComponent
        | ApiV1AssistantSessionsMessagesCreateArchivedReasonErrorComponent
        | ApiV1AssistantSessionsMessagesCreateCriticalityErrorComponent
        | ApiV1AssistantSessionsMessagesCreateDebugModeErrorComponent
        | ApiV1AssistantSessionsMessagesCreateDisplayNameErrorComponent
        | ApiV1AssistantSessionsMessagesCreateKindErrorComponent
        | ApiV1AssistantSessionsMessagesCreateLabelsErrorComponent
        | ApiV1AssistantSessionsMessagesCreateNameErrorComponent
        | ApiV1AssistantSessionsMessagesCreateNonFieldErrorsErrorComponent
        | ApiV1AssistantSessionsMessagesCreatePlatformServiceErrorComponent
        | ApiV1AssistantSessionsMessagesCreateProviderErrorComponent
        | ApiV1AssistantSessionsMessagesCreateProviderIdErrorComponent
        | ApiV1AssistantSessionsMessagesCreateProviderReferenceErrorComponent
        | ApiV1AssistantSessionsMessagesCreateReconciliationEnabledErrorComponent
        | ApiV1AssistantSessionsMessagesCreateSlaAvailabilityErrorComponent
        | ApiV1AssistantSessionsMessagesCreateSlaTargetErrorComponent
        | ApiV1AssistantSessionsMessagesCreateSloAvailabilityErrorComponent
        | ApiV1AssistantSessionsMessagesCreateSloTargetErrorComponent
        | ApiV1AssistantSessionsMessagesCreateStatusErrorComponent
        | ApiV1AssistantSessionsMessagesCreateTargetAvailabilityErrorComponent
        | ApiV1AssistantSessionsMessagesCreateTolerationsErrorComponent
        | ApiV1AssistantSessionsMessagesCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_assistant_sessions_messages_create_annotations_error_component import (
            ApiV1AssistantSessionsMessagesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_archived_at_error_component import (
            ApiV1AssistantSessionsMessagesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_archived_error_component import (
            ApiV1AssistantSessionsMessagesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_archived_reason_error_component import (
            ApiV1AssistantSessionsMessagesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_criticality_error_component import (
            ApiV1AssistantSessionsMessagesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_debug_mode_error_component import (
            ApiV1AssistantSessionsMessagesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_display_name_error_component import (
            ApiV1AssistantSessionsMessagesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_kind_error_component import (
            ApiV1AssistantSessionsMessagesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_labels_error_component import (
            ApiV1AssistantSessionsMessagesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_name_error_component import (
            ApiV1AssistantSessionsMessagesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_non_field_errors_error_component import (
            ApiV1AssistantSessionsMessagesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_platform_service_error_component import (
            ApiV1AssistantSessionsMessagesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_provider_error_component import (
            ApiV1AssistantSessionsMessagesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_provider_id_error_component import (
            ApiV1AssistantSessionsMessagesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_provider_reference_error_component import (
            ApiV1AssistantSessionsMessagesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_reconciliation_enabled_error_component import (
            ApiV1AssistantSessionsMessagesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_sla_availability_error_component import (
            ApiV1AssistantSessionsMessagesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_sla_target_error_component import (
            ApiV1AssistantSessionsMessagesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_slo_availability_error_component import (
            ApiV1AssistantSessionsMessagesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_slo_target_error_component import (
            ApiV1AssistantSessionsMessagesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_target_availability_error_component import (
            ApiV1AssistantSessionsMessagesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_tolerations_error_component import (
            ApiV1AssistantSessionsMessagesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_workspace_id_error_component import (
            ApiV1AssistantSessionsMessagesCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AssistantSessionsMessagesCreateWorkspaceIdErrorComponent):
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
        from ..models.api_v1_assistant_sessions_messages_create_annotations_error_component import (
            ApiV1AssistantSessionsMessagesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_archived_at_error_component import (
            ApiV1AssistantSessionsMessagesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_archived_error_component import (
            ApiV1AssistantSessionsMessagesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_archived_reason_error_component import (
            ApiV1AssistantSessionsMessagesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_criticality_error_component import (
            ApiV1AssistantSessionsMessagesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_debug_mode_error_component import (
            ApiV1AssistantSessionsMessagesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_display_name_error_component import (
            ApiV1AssistantSessionsMessagesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_kind_error_component import (
            ApiV1AssistantSessionsMessagesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_labels_error_component import (
            ApiV1AssistantSessionsMessagesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_name_error_component import (
            ApiV1AssistantSessionsMessagesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_non_field_errors_error_component import (
            ApiV1AssistantSessionsMessagesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_platform_service_error_component import (
            ApiV1AssistantSessionsMessagesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_provider_error_component import (
            ApiV1AssistantSessionsMessagesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_provider_id_error_component import (
            ApiV1AssistantSessionsMessagesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_provider_reference_error_component import (
            ApiV1AssistantSessionsMessagesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_reconciliation_enabled_error_component import (
            ApiV1AssistantSessionsMessagesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_sla_availability_error_component import (
            ApiV1AssistantSessionsMessagesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_sla_target_error_component import (
            ApiV1AssistantSessionsMessagesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_slo_availability_error_component import (
            ApiV1AssistantSessionsMessagesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_slo_target_error_component import (
            ApiV1AssistantSessionsMessagesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_status_error_component import (
            ApiV1AssistantSessionsMessagesCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_target_availability_error_component import (
            ApiV1AssistantSessionsMessagesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_tolerations_error_component import (
            ApiV1AssistantSessionsMessagesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_assistant_sessions_messages_create_workspace_id_error_component import (
            ApiV1AssistantSessionsMessagesCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AssistantSessionsMessagesCreateAnnotationsErrorComponent
                | ApiV1AssistantSessionsMessagesCreateArchivedAtErrorComponent
                | ApiV1AssistantSessionsMessagesCreateArchivedErrorComponent
                | ApiV1AssistantSessionsMessagesCreateArchivedReasonErrorComponent
                | ApiV1AssistantSessionsMessagesCreateCriticalityErrorComponent
                | ApiV1AssistantSessionsMessagesCreateDebugModeErrorComponent
                | ApiV1AssistantSessionsMessagesCreateDisplayNameErrorComponent
                | ApiV1AssistantSessionsMessagesCreateKindErrorComponent
                | ApiV1AssistantSessionsMessagesCreateLabelsErrorComponent
                | ApiV1AssistantSessionsMessagesCreateNameErrorComponent
                | ApiV1AssistantSessionsMessagesCreateNonFieldErrorsErrorComponent
                | ApiV1AssistantSessionsMessagesCreatePlatformServiceErrorComponent
                | ApiV1AssistantSessionsMessagesCreateProviderErrorComponent
                | ApiV1AssistantSessionsMessagesCreateProviderIdErrorComponent
                | ApiV1AssistantSessionsMessagesCreateProviderReferenceErrorComponent
                | ApiV1AssistantSessionsMessagesCreateReconciliationEnabledErrorComponent
                | ApiV1AssistantSessionsMessagesCreateSlaAvailabilityErrorComponent
                | ApiV1AssistantSessionsMessagesCreateSlaTargetErrorComponent
                | ApiV1AssistantSessionsMessagesCreateSloAvailabilityErrorComponent
                | ApiV1AssistantSessionsMessagesCreateSloTargetErrorComponent
                | ApiV1AssistantSessionsMessagesCreateStatusErrorComponent
                | ApiV1AssistantSessionsMessagesCreateTargetAvailabilityErrorComponent
                | ApiV1AssistantSessionsMessagesCreateTolerationsErrorComponent
                | ApiV1AssistantSessionsMessagesCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_0 = (
                        ApiV1AssistantSessionsMessagesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_1 = (
                        ApiV1AssistantSessionsMessagesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_2 = (
                        ApiV1AssistantSessionsMessagesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_3 = (
                        ApiV1AssistantSessionsMessagesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_4 = (
                        ApiV1AssistantSessionsMessagesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_5 = (
                        ApiV1AssistantSessionsMessagesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_6 = (
                        ApiV1AssistantSessionsMessagesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_7 = (
                        ApiV1AssistantSessionsMessagesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_8 = (
                        ApiV1AssistantSessionsMessagesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_9 = (
                        ApiV1AssistantSessionsMessagesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_10 = (
                        ApiV1AssistantSessionsMessagesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_11 = (
                        ApiV1AssistantSessionsMessagesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_12 = (
                        ApiV1AssistantSessionsMessagesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_13 = (
                        ApiV1AssistantSessionsMessagesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_14 = (
                        ApiV1AssistantSessionsMessagesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_15 = (
                        ApiV1AssistantSessionsMessagesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_16 = (
                        ApiV1AssistantSessionsMessagesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_17 = (
                        ApiV1AssistantSessionsMessagesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_18 = (
                        ApiV1AssistantSessionsMessagesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_19 = (
                        ApiV1AssistantSessionsMessagesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_20 = (
                        ApiV1AssistantSessionsMessagesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_21 = (
                        ApiV1AssistantSessionsMessagesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_assistant_sessions_messages_create_error_type_22 = (
                        ApiV1AssistantSessionsMessagesCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_assistant_sessions_messages_create_error_type_23 = (
                    ApiV1AssistantSessionsMessagesCreateStatusErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_assistant_sessions_messages_create_error_type_23

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_assistant_sessions_messages_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_assistant_sessions_messages_create_validation_error.additional_properties = d
        return api_v1_assistant_sessions_messages_create_validation_error

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
